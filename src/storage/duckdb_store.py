import json
import os
from typing import List, Dict, Any
import duckdb
from src.config.settings import settings
from src.crawler.logger import logger

class DuckDBStore:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or str(settings.absolute_db_path)
        
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self.conn = None
        self._initialize_db()

    def _initialize_db(self):
        """Establish connection and create tables if they do not exist."""
        try:
            self.conn = duckdb.connect(self.db_path)
            
            # Create Documents Table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    doc_id VARCHAR PRIMARY KEY,
                    url VARCHAR,
                    title VARCHAR,
                    text VARCHAR,
                    metadata VARCHAR,  -- Store JSON as string
                    crawled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create Chunks Table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS chunks (
                    chunk_id VARCHAR PRIMARY KEY,
                    doc_id VARCHAR,
                    text VARCHAR,
                    heading VARCHAR,
                    url VARCHAR,
                    title VARCHAR,
                    word_count INTEGER,
                    metadata VARCHAR  -- Store JSON as string
                )
            """)
            
            logger.info(f"Initialized DuckDB database at {self.db_path}")
        except Exception as e:
            logger.error(f"Failed to initialize DuckDB database: {e}")
            raise e

    def save_documents(self, docs: List[Dict[str, Any]]):
        """
        Insert or update documents in the database.
        """
        if not docs:
            return
        
        try:
            for doc in docs:
                doc_id = doc.get("id") or doc.get("doc_id")
                if not doc_id:
                    import hashlib
                    doc_id = hashlib.md5(doc.get("url", "").encode()).hexdigest()
                
                url = doc.get("url", "")
                title = doc.get("title", "") or "Untitled Page"
                text = doc.get("markdown", "") or doc.get("text", "")
                metadata_str = json.dumps(doc.get("metadata", {}))

                # Use upsert (insert or replace)
                self.conn.execute("""
                    INSERT OR REPLACE INTO documents (doc_id, url, title, text, metadata)
                    VALUES (?, ?, ?, ?, ?)
                """, (doc_id, url, title, text, metadata_str))
                
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error saving documents to DuckDB: {e}")
            raise e

    def save_chunks(self, chunks: List[Dict[str, Any]]):
        """
        Insert or update chunks in the database.
        """
        if not chunks:
            return
        
        try:
            for chunk in chunks:
                chunk_id = chunk.get("chunk_id")
                doc_id = chunk.get("doc_id")
                text = chunk.get("text", "")
                heading = chunk.get("heading", "")
                url = chunk.get("url", "")
                title = chunk.get("title", "")
                word_count = chunk.get("word_count", 0)
                metadata_str = json.dumps(chunk.get("metadata", {}))

                self.conn.execute("""
                    INSERT OR REPLACE INTO chunks (chunk_id, doc_id, text, heading, url, title, word_count, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (chunk_id, doc_id, text, heading, url, title, word_count, metadata_str))
                
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error saving chunks to DuckDB: {e}")
            raise e

    def get_all_chunks(self) -> List[Dict[str, Any]]:
        """
        Fetch all chunks from database.
        """
        try:
            results = self.conn.execute("SELECT chunk_id, doc_id, text, heading, url, title, word_count, metadata FROM chunks").fetchall()
            chunks = []
            for row in results:
                chunks.append({
                    "chunk_id": row[0],
                    "doc_id": row[1],
                    "text": row[2],
                    "heading": row[3],
                    "url": row[4],
                    "title": row[5],
                    "word_count": row[6],
                    "metadata": json.loads(row[7]) if row[7] else {}
                })
            return chunks
        except Exception as e:
            logger.error(f"Error reading chunks from DuckDB: {e}")
            return []

    def get_document_count(self) -> int:
        """Get total documents count."""
        try:
            res = self.conn.execute("SELECT COUNT(*) FROM documents").fetchone()
            return res[0] if res else 0
        except Exception as e:
            logger.error(f"Error counting documents: {e}")
            return 0

    def get_chunk_count(self) -> int:
        """Get total chunks count."""
        try:
            res = self.conn.execute("SELECT COUNT(*) FROM chunks").fetchone()
            return res[0] if res else 0
        except Exception as e:
            logger.error(f"Error counting chunks: {e}")
            return 0

    def clear_database(self):
        """Wipe database contents."""
        try:
            self.conn.execute("DELETE FROM documents")
            self.conn.execute("DELETE FROM chunks")
            self.conn.commit()
            logger.info("Cleared DuckDB database tables.")
        except Exception as e:
            logger.error(f"Error clearing DuckDB database: {e}")

    def close(self):
        """Close connection."""
        if self.conn:
            try:
                self.conn.close()
            except Exception:
                pass
            self.conn = None
