import os
import json
import math
from pathlib import Path
from typing import List, Dict, Set, Any
import matplotlib.pyplot as plt
import seaborn as sns

class QueryEvaluation:
    def __init__(self, query: str, query_id: str, relevant_ids: List[str]):
        self.query = query
        self.query_id = query_id
        self.relevant_ids: Set[str] = set(relevant_ids)
        self.retrieved_ids: List[str] = []
        self.metrics: Dict[str, float] = {}

    def set_retrieved(self, retrieved: List[str]):
        """Set list of retrieved document/chunk URLs or IDs."""
        self.retrieved_ids = retrieved

    def evaluate(self, max_k: int = 10) -> Dict[str, float]:
        """Compute standard information retrieval metrics."""
        self.metrics = {}
        
        # Guard clause for no retrieved items
        if not self.retrieved_ids or not self.relevant_ids:
            for k in [1, 3, 5, 10]:
                self.metrics[f"P@{k}"] = 0.0
                self.metrics[f"R@{k}"] = 0.0
                self.metrics[f"NDCG@{k}"] = 0.0
            self.metrics["MRR"] = 0.0
            self.metrics["AP"] = 0.0
            return self.metrics

        # 1. Precision & Recall @ K
        for k in [1, 3, 5, 10]:
            k_val = min(k, len(self.retrieved_ids))
            retrieved_k = self.retrieved_ids[:k_val]
            
            hits = sum(1 for doc in retrieved_k if doc in self.relevant_ids)
            
            precision = hits / k
            recall = hits / len(self.relevant_ids)
            
            self.metrics[f"P@{k}"] = round(precision, 4)
            self.metrics[f"R@{k}"] = round(recall, 4)

            # 2. NDCG @ K
            dcg = 0.0
            for idx, doc in enumerate(retrieved_k):
                if doc in self.relevant_ids:
                    dcg += 1.0 / math.log2(idx + 2)
            
            idcg = 0.0
            # Ideal DCG: top relevant hits at the front
            num_ideal = min(k, len(self.relevant_ids))
            for idx in range(num_ideal):
                idcg += 1.0 / math.log2(idx + 2)
                
            ndcg = dcg / idcg if idcg > 0.0 else 0.0
            self.metrics[f"NDCG@{k}"] = round(ndcg, 4)

        # 3. MRR (Mean Reciprocal Rank)
        mrr = 0.0
        for idx, doc in enumerate(self.retrieved_ids[:max_k]):
            if doc in self.relevant_ids:
                mrr = 1.0 / (idx + 1)
                break
        self.metrics["MRR"] = round(mrr, 4)

        # 4. Average Precision (AP)
        hits = 0
        sum_precision = 0.0
        for idx, doc in enumerate(self.retrieved_ids):
            if doc in self.relevant_ids:
                hits += 1
                precision_at_idx = hits / (idx + 1)
                sum_precision += precision_at_idx
                
        ap = sum_precision / len(self.relevant_ids) if len(self.relevant_ids) > 0 else 0.0
        self.metrics["AP"] = round(ap, 4)

        return self.metrics


class EvaluationSet:
    def __init__(self):
        self.queries: List[QueryEvaluation] = []

    def add_query(self, query_eval: QueryEvaluation):
        self.queries.append(query_eval)

    def get_mean_metrics(self) -> Dict[str, float]:
        """Compute the average of all metrics across all queries."""
        if not self.queries:
            return {}

        total_metrics = {}
        for q in self.queries:
            # Trigger evaluate if metrics are empty
            if not q.metrics:
                q.evaluate()
                
            for k, val in q.metrics.items():
                total_metrics[k] = total_metrics.get(k, 0.0) + val

        mean_metrics = {}
        for k, val in total_metrics.items():
            mean_metrics[k] = round(val / len(self.queries), 4)

        return mean_metrics

    def plot_metrics(self, output_path: str):
        """Generate Seaborn charts and save them."""
        mean_metrics = self.get_mean_metrics()
        if not mean_metrics:
            return

        # Prepare directory
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Plot 1: Precision vs Recall Bar Plot
        ks = [1, 3, 5, 10]
        precisions = [mean_metrics[f"P@{k}"] for k in ks]
        recalls = [mean_metrics[f"R@{k}"] for k in ks]

        x = range(len(ks))
        width = 0.35

        axes[0].bar([i - width/2 for i in x], precisions, width, label='Precision', color='#1f77b4')
        axes[0].bar([i + width/2 for i in x], recalls, width, label='Recall', color='#ff7f0e')
        axes[0].set_xticks(x)
        axes[0].set_xticklabels([f"K={k}" for k in ks])
        axes[0].set_title("Mean Precision and Recall by K")
        axes[0].set_ylabel("Score")
        axes[0].set_ylim(0.0, 1.1)
        axes[0].legend()

        # Plot 2: NDCG Line Plot
        ndcgs = [mean_metrics[f"NDCG@{k}"] for k in ks]
        axes[1].plot(ks, ndcgs, marker='o', linestyle='-', linewidth=2, color='#2ca02c')
        axes[1].set_xticks(ks)
        axes[1].set_title("Mean NDCG by K")
        axes[1].set_ylabel("Score")
        axes[1].set_xlabel("K")
        axes[1].set_ylim(0.0, 1.1)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()

    def save_json(self, output_path: str):
        """Save detailed evaluation results to a JSON file."""
        mean_metrics = self.get_mean_metrics()
        detailed_queries = []
        for q in self.queries:
            detailed_queries.append({
                "query_id": q.query_id,
                "query": q.query,
                "relevant_count": len(q.relevant_ids),
                "retrieved_count": len(q.retrieved_ids),
                "metrics": q.metrics
            })

        output_data = {
            "mean_metrics": mean_metrics,
            "queries": detailed_queries
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
