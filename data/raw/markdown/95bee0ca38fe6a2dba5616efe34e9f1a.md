![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face⟨1⟩
  *  Models ⟨2⟩
  *  Datasets ⟨3⟩
  *  Spaces ⟨4⟩
  *  Buckets new⟨5⟩
  *  Docs ⟨6⟩
  *  Enterprise ⟨7⟩
  * Pricing⟨8⟩
  *     * Website
      *  Tasks⟨9⟩
      *  HuggingChat⟨10⟩
      *  Collections⟨11⟩
      *  Languages⟨12⟩
      *  Organizations⟨13⟩
    * Community
      *  Blog⟨14⟩
      *  Posts⟨15⟩
      *  Daily Papers⟨16⟩
      *  Hardware⟨17⟩
      *  Learn⟨18⟩
      *  Discord⟨19⟩
      *  Forum⟨20⟩
      *  GitHub⟨21⟩
    * Solutions
      *  Team & Enterprise⟨7⟩
      *  Hugging Face PRO⟨22⟩
      *  Enterprise Support⟨23⟩
      *  Inference Providers⟨24⟩
      *  Inference Endpoints⟨25⟩
      *  Storage Buckets⟨5⟩
  * * * *
  * Log In⟨26⟩
  * Sign Up⟨27⟩


#   Datasets:⟨3⟩
* * *
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b018de31267972b2ff3361/mNZSDpw9cCVlc5bu-S9MW.png) ⟨28⟩
Chess-Nut-Engine⟨28⟩
/
chess-sft-corpus-4x-eval⟨29⟩
like 0
Follow
![⟨30⟩] Chess Nut Engine 1
Tasks:  Text Generation ⟨31⟩
Modalities:  Tabular ⟨32⟩ Text ⟨33⟩
Formats:  json ⟨34⟩
Languages:  English ⟨35⟩
Size:  10K - 100K ⟨36⟩
Tags:  chess ⟨37⟩ sft ⟨38⟩ evaluation ⟨39⟩ benchmark ⟨40⟩ chess960 ⟨41⟩
Libraries:  Datasets ⟨42⟩ Dask ⟨43⟩ Polars ⟨44⟩ + 1
License:
apache-2.0
 Dataset card ⟨29⟩ Data Studio ⟨45⟩ Files Files and versions xet ⟨46⟩ Community ⟨47⟩
Dataset Viewer
 Auto-converted to Parquet⟨48⟩ API Embed  Duplicate⟨49⟩ Data Studio
Subset (20)
bench_chess960 · 500 rows
bench_chess960 (500 rows) bench_endgames (1.5k rows) bench_evaluation (1.5k rows) bench_mate (1k rows) bench_openings (500 rows) bench_perception (2k rows) bench_planning (2k rows) bench_rules (2k rows) bench_tactics (2k rows) benchmark eval_chess960 (500 rows) eval_endgames (1.5k rows) eval_evaluation (1.5k rows) eval_mate (1k rows) eval_openings (500 rows) eval_perception (2k rows) eval_planning (2k rows) eval_rules (2k rows) eval_splits eval_tactics (2k rows)
Split (1)
test · 500 rows
test (500 rows)
SQL
Console  
|  example_id string  |  split string  |  task_type string  |  fen string  |  prompt string  |  gold_answer string  |  metric_type string  |  metadata dict  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
|  chess960_00000  |  chess960  |  legal_moves_960  |  r1nnqrbb/k1p1pppp/1p6/p7/3p1PPQ/P3P3/1PPP3P/RKNN1RBB b KQ - 0 7  |  FEN: r1nnqrbb/k1p1pppp/1p6/p7/3p1PPQ/P3P3/1PPP3P/RKNN1RBB b KQ - 0 7 List all legal moves.  |  Side to move: black. Legal moves: a5a4 a7a6 a7b8 a8b8 b6b5 c7c5 c7c6 c8d6 d4d3 d4e3 d8b7 d8c6 d8e6 e7e5 e7e6 e8a4 e8b5 e8c6 e8d7 f7f5 f7f6 g7g5 g7g6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 751 }  |  
|  chess960_00001  |  chess960  |  check_detection_960  |  1n1knbbr/r1pp1ppp/pB4Q1/1p2p3/PP3P1P/R7/3PP1P1/1N1KNB1R b - - 5 10  |  FEN: 1n1knbbr/r1pp1ppp/pB4Q1/1p2p3/PP3P1P/R7/3PP1P1/1N1KNB1R b - - 5 10 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 526 }  |  
|  chess960_00002  |  chess960  |  castling_rules_960  |  r1bkqnrb/pppppppp/n7/8/2P1P3/8/PP1P1PPP/RNBKQNRB b KQkq - 0 2  |  FEN: r1bkqnrb/pppppppp/n7/8/2P1P3/8/PP1P1PPP/RNBKQNRB b KQkq - 0 2 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 535 }  |  
|  chess960_00003  |  chess960  |  legal_moves_960  |  brnbqkrn/ppppp1pp/5p2/8/8/P7/1PPPPPPP/BRNBQKRN w KQkq - 0 2  |  FEN: brnbqkrn/ppppp1pp/5p2/8/8/P7/1PPPPPPP/BRNBQKRN w KQkq - 0 2 List all legal moves.  |  Side to move: white. Legal moves: a3a4 b2b3 b2b4 c1a2 c1b3 c1d3 c2c3 c2c4 d2d3 d2d4 e2e3 e2e4 f1g1 f2f3 f2f4 g2g3 g2g4 h1g3 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 609 }  |  
|  chess960_00004  |  chess960  |  check_detection_960  |  b1nbnkrq/1r1ppp1p/p7/2p3p1/5P1P/3N2P1/PPPPP2K/BR1BNR2 b k - 4 7  |  FEN: b1nbnkrq/1r1ppp1p/p7/2p3p1/5P1P/3N2P1/PPPPP2K/BR1BNR2 b k - 4 7 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 465 }  |  
|  chess960_00005  |  chess960  |  castling_rules_960  |  rbk1nr1n/pppp2pp/4b3/4pP2/7q/3P4/PPPK1PPP/RBQ1NRBN w kq - 3 6  |  FEN: rbk1nr1n/pppp2pp/4b3/4pP2/7q/3P4/PPPK1PPP/RBQ1NRBN w kq - 3 6 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 812 }  |  
|  chess960_00006  |  chess960  |  legal_moves_960  |  nqbrkrnb/pppppppp/8/8/7P/8/PPPPPPP1/NQBRKRNB b KQkq - 0 1  |  FEN: nqbrkrnb/pppppppp/8/8/7P/8/PPPPPPP1/NQBRKRNB b KQkq - 0 1 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 a8b6 b7b5 b7b6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 311 }  |  
|  chess960_00007  |  chess960  |  check_detection_960  |  qb1rbnkr/ppp1ppQp/1n6/3p4/1P6/4P3/P1PP1PPP/1BNRBNKR b KQkq - 0 3  |  FEN: qb1rbnkr/ppp1ppQp/1n6/3p4/1P6/4P3/P1PP1PPP/1BNRBNKR b KQkq - 0 3 Detect the game state: check, checkmate, stalemate, or none.  |  Check.  |  check_state  |  { "is_chess960": true, "chess960_id": 104 }  |  
|  chess960_00008  |  chess960  |  castling_rules_960  |  rbnkrqbn/pppppp1p/8/6p1/P3P3/8/1PPP1PPP/RBNKRQBN b KQkq - 0 2  |  FEN: rbnkrqbn/pppppp1p/8/6p1/P3P3/8/1PPP1PPP/RBNKRQBN b KQkq - 0 2 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 652 }  |  
|  chess960_00009  |  chess960  |  legal_moves_960  |  r1knqrbb/pppp1ppp/2n5/4p3/P3P3/8/1PPP1PPP/RNKNQRBB w KQkq - 1 3  |  FEN: r1knqrbb/pppp1ppp/2n5/4p3/P3P3/8/1PPP1PPP/RNKNQRBB w KQkq - 1 3 List all legal moves.  |  Side to move: white. Legal moves: a1a2 a1a3 a4a5 b1a3 b1c3 b2b3 b2b4 c2c3 c2c4 d1c3 d1e3 d2d3 d2d4 e1e2 e1e3 f2f3 f2f4 g2g3 g2g4 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 559 }  |  
|  chess960_00010  |  chess960  |  check_detection_960  |  nbb1r1qr/ppp1pppk/8/3P3p/2n1P1P1/3PRP2/PP1B3P/NB1N1QKR w K - 1 10  |  FEN: nbb1r1qr/ppp1pppk/8/3P3p/2n1P1P1/3PRP2/PP1B3P/NB1N1QKR w K - 1 10 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 52 }  |  
|  chess960_00011  |  chess960  |  castling_rules_960  |  bn1r1bq1/pp1pk1p1/1n2pp1r/N1p4p/3P4/2N2PP1/PPP1P2P/B2RKBQR w KQ - 1 8  |  FEN: bn1r1bq1/pp1pk1p1/1n2pp1r/N1p4p/3P4/2N2PP1/PPP1P2P/B2RKBQR w KQ - 1 8 What castling options are available?  |  Castling available: queenside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 66 }  |  
|  chess960_00012  |  chess960  |  legal_moves_960  |  rqnb1rbn/p1pkpppp/1p6/3p4/6P1/1N4N1/PPPPPP1P/RQ1BKRB1 w KQ - 2 4  |  FEN: rqnb1rbn/p1pkpppp/1p6/3p4/6P1/1N4N1/PPPPPP1P/RQ1BKRB1 w KQ - 2 4 List all legal moves.  |  Side to move: white. Legal moves: a2a3 a2a4 b1c1 b3a5 b3c1 b3c5 b3d4 c2c3 c2c4 d2d3 d2d4 e2e3 e2e4 f2f3 f2f4 g3e4 g3f5 g3h1 g3h5 g4g5 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 605 }  |  
|  chess960_00013  |  chess960  |  check_detection_960  |  brk1rbnq/ppppp2p/2n2pp1/8/1PP4P/8/P2PPPP1/BRKNRBNQ w KQkq - 0 4  |  FEN: brk1rbnq/ppppp2p/2n2pp1/8/1PP4P/8/P2PPPP1/BRKNRBNQ w KQkq - 0 4 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 850 }  |  
|  chess960_00014  |  chess960  |  castling_rules_960  |  qrnkb1rn/pppp1ppp/8/4p3/8/b1PP4/PP2PPPP/QRNKBBRN w KQkq - 1 3  |  FEN: qrnkb1rn/pppp1ppp/8/4p3/8/b1PP4/PP2PPPP/QRNKBBRN w KQkq - 1 3 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 586 }  |  
|  chess960_00015  |  chess960  |  legal_moves_960  |  rkbbqnnr/pppppppp/8/8/8/6P1/PPPPPP1P/RKBBQNNR b KQkq - 0 1  |  FEN: rkbbqnnr/pppppppp/8/8/8/6P1/PPPPPP1P/RKBBQNNR b KQkq - 0 1 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b7b5 b7b6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 f8e6 f8g6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 709 }  |  
|  chess960_00016  |  chess960  |  check_detection_960  |  q1rnb1kr/1p1pp1p1/p1pb1pn1/7p/P1PPB2P/Q3N3/1P2PPP1/2R1BNKR w KQkq - 2 8  |  FEN: q1rnb1kr/1p1pp1p1/p1pb1pn1/7p/P1PPB2P/Q3N3/1P2PPP1/2R1BNKR w KQkq - 2 8 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 392 }  |  
|  chess960_00017  |  chess960  |  castling_rules_960  |  rknrbn1b/ppppp1pp/5p2/8/P7/1q4P1/1PPPPP1P/RKNRBNQB w KQkq - 1 3  |  FEN: rknrbn1b/ppppp1pp/5p2/8/P7/1q4P1/1PPPPP1P/RKNRBNQB w KQkq - 1 3 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 859 }  |  
|  chess960_00018  |  chess960  |  legal_moves_960  |  qn1rbbkr/pppppppp/3n4/8/7P/8/PPPPPPP1/QNNRBBKR w KQkq - 1 2  |  FEN: qn1rbbkr/pppppppp/3n4/8/7P/8/PPPPPPP1/QNNRBBKR w KQkq - 1 2 List all legal moves.  |  Side to move: white. Legal moves: a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 c1b3 c1d3 c2c3 c2c4 d2d3 d2d4 e2e3 e2e4 f2f3 f2f4 g1h2 g2g3 g2g4 h1h2 h1h3 h4h5  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 10 }  |  
|  chess960_00019  |  chess960  |  check_detection_960  |  rbnk1rbn/ppppp1pp/5p2/8/P2N4/1P2P1qP/2PP1P2/RB1KQRBN w KQkq - 3 7  |  FEN: rbnk1rbn/ppppp1pp/5p2/8/P2N4/1P2P1qP/2PP1P2/RB1KQRBN w KQkq - 3 7 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 636 }  |  
|  chess960_00020  |  chess960  |  castling_rules_960  |  qnbrkrnb/ppppp2p/8/5pp1/2P5/1P2P3/P2P1PPP/QNBRKRNB b KQkq - 0 3  |  FEN: qnbrkrnb/ppppp2p/8/5pp1/2P5/1P2P3/P2P1PPP/QNBRKRNB b KQkq - 0 3 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 295 }  |  
|  chess960_00021  |  chess960  |  legal_moves_960  |  r2knbqr/1bppp1pp/p1n2p2/1p5P/P7/3N1P1R/1PPPP1P1/RNBK1BQ1 b Qkq - 1 6  |  FEN: r2knbqr/1bppp1pp/p1n2p2/1p5P/P7/3N1P1R/1PPPP1P1/RNBK1BQ1 b Qkq - 1 6 List all legal moves.  |  Side to move: black. Legal moves: a6a5 a8a7 a8b8 a8c8 b5a4 b5b4 b7c8 c6a5 c6a7 c6b4 c6b8 c6d4 c6e5 d7d5 d7d6 d8a8 d8c8 e7e5 e7e6 e8d6 f6f5 g7g5 g7g6 g8a2 g8b3 g8c4 g8d5 g8e6 g8f7 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 550 }  |  
|  chess960_00022  |  chess960  |  check_detection_960  |  rqkrbnnb/pppppp1p/8/6p1/8/4P3/PPPP1PPP/RQKRBNNB w KQkq - 0 2  |  FEN: rqkrbnnb/pppppp1p/8/6p1/8/4P3/PPPP1PPP/RQKRBNNB w KQkq - 0 2 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 891 }  |  
|  chess960_00023  |  chess960  |  castling_rules_960  |  nrkrbb1n/pppppp1q/8/6pp/1P4P1/5P2/P1PPPB1P/NRKR1BQN b KQkq - 0 5  |  FEN: nrkrbb1n/pppppp1q/8/6pp/1P4P1/5P2/P1PPPB1P/NRKR1BQN b KQkq - 0 5 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 362 }  |  
|  chess960_00024  |  chess960  |  legal_moves_960  |  rkbqn1rb/ppp2p1p/8/P2pp1p1/3nPP2/2P5/1PNP2PP/RKBQ1NRB b KQkq - 0 6  |  FEN: rkbqn1rb/ppp2p1p/8/P2pp1p1/3nPP2/2P5/1PNP2PP/RKBQ1NRB b KQkq - 0 6 List all legal moves.  |  Side to move: black. Legal moves: a7a6 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d4b3 d4b5 d4c2 d4c6 d4e2 d4e6 d4f3 d4f5 d5e4 d8d6 d8d7 d8e7 d8f6 e5f4 e8d6 e8f6 e8g7 f7f5 f7f6 g5f4 g5g4 g8f8 g8g6 g8g7 h7h5 h7h6 h8f6 h8g7  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 711 }  |  
|  chess960_00025  |  chess960  |  check_detection_960  |  1n1kbbrq/1pn1pppp/8/8/p4P2/1P4P1/P1RPP1QP/NN1KB1R1 b Kk - 0 8  |  FEN: 1n1kbbrq/1pn1pppp/8/8/p4P2/1P4P1/P1RPP1QP/NN1KB1R1 b Kk - 0 8 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 90 }  |  
|  chess960_00026  |  chess960  |  castling_rules_960  |  rbbkr2q/p1p1ppp1/2Qp2n1/1p5p/4nP2/3P2P1/PPPB3P/RB1KRNN1 w KQkq - 0 7  |  FEN: rbbkr2q/p1p1ppp1/2Qp2n1/1p5p/4nP2/3P2P1/PPPB3P/RB1KRNN1 w KQkq - 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 948 }  |  
|  chess960_00027  |  chess960  |  legal_moves_960  |  1n1qrb1k/p1ppp1p1/2bn4/1p1N1p1B/5P1p/1PN1P3/1BPP2PP/3QR1KR w KQ - 4 11  |  FEN: 1n1qrb1k/p1ppp1p1/2bn4/1p1N1p1B/5P1p/1PN1P3/1BPP2PP/3QR1KR w KQ - 4 11 List all legal moves.  |  Side to move: white. Legal moves: b2a1 b2a3 b2c1 b3b4 c3a2 c3a4 c3b1 c3b5 c3e2 c3e4 d1a1 d1b1 d1c1 d1e2 d1f3 d1g4 d2d3 d2d4 d5b4 d5b6 d5c7 d5e7 d5f6 e1e2 e1f1 e3e4 g1f1 g1f2 g1h1 g2g3 g2g4 h2h3 h5e2 h5e8 h5f3 h5f7 h5g4 h5g6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 34 }  |  
|  chess960_00028  |  chess960  |  check_detection_960  |  rkrb1qbn/pp1pp3/2pn2p1/5p1p/1P2B3/2P4P/PK1PPPP1/R1R1NQBN b kq - 1 6  |  FEN: rkrb1qbn/pp1pp3/2pn2p1/5p1p/1P2B3/2P4P/PK1PPPP1/R1R1NQBN b kq - 1 6 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 941 }  |  
|  chess960_00029  |  chess960  |  castling_rules_960  |  2brkbnr/1ppnpp1p/3p4/p5p1/1P1P3P/2Pq1P2/P3P1P1/QNB1KBNR w Kkq - 0 7  |  FEN: 2brkbnr/1ppnpp1p/3p4/p5p1/1P1P3P/2Pq1P2/P3P1P1/QNB1KBNR w Kkq - 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 198 }  |  
|  chess960_00030  |  chess960  |  legal_moves_960  |  qbr3nr/ppppkb1p/2n2pp1/1N2p3/P7/2PP1PP1/1P2P2P/QBR1BKNR b KQ - 0 7  |  FEN: qbr3nr/ppppkb1p/2n2pp1/1N2p3/P7/2PP1PP1/1P2P2P/QBR1BKNR b KQ - 0 7 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b7b6 c6a5 c6b4 c6d4 c6d8 c8d8 c8e8 c8f8 d7d5 d7d6 e5e4 e7d8 e7e6 e7e8 e7f8 f6f5 f7a2 f7b3 f7c4 f7d5 f7e6 f7e8 g6g5 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 488 }  |  
|  chess960_00031  |  chess960  |  check_detection_960  |  rb1rbqnn/pp2kppp/4p3/2pp4/3P4/1P2P1PN/P1P2PQP/RBKRB2N w KQ - 2 8  |  FEN: rb1rbqnn/pp2kppp/4p3/2pp4/3P4/1P2P1PN/P1P2PQP/RBKRB2N w KQ - 2 8 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 920 }  |  
|  chess960_00032  |  chess960  |  castling_rules_960  |  1rb1kr1b/ppp1pqp1/1n2n2p/3p1p2/1PP4P/4P3/PN1P1PPQ/NRB1KR1B b KQkq - 1 7  |  FEN: 1rb1kr1b/ppp1pqp1/1n2n2p/3p1p2/1PP4P/4P3/PN1P1PPQ/NRB1KR1B b KQkq - 1 7 What castling options are available?  |  Castling available: kingside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 183 }  |  
|  chess960_00033  |  chess960  |  legal_moves_960  |  rkbqn1rb/2p1p1p1/5pnp/pp1p1P2/PP4P1/2P2N2/2QPP2P/RKB2NRB b KQk - 0 9  |  FEN: rkbqn1rb/2p1p1p1/5pnp/pp1p1P2/PP4P1/2P2N2/2QPP2P/RKB2NRB b KQk - 0 9 List all legal moves.  |  Side to move: black. Legal moves: a5b4 a8a6 a8a7 b5a4 b8a7 b8b7 c7c5 c7c6 c8a6 c8b7 c8d7 c8e6 c8f5 d5d4 d8d6 d8d7 e7e5 e7e6 e8d6 g6e5 g6f4 g6f8 g6h4 g8f8 h6h5  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 711 }  |  
|  chess960_00034  |  chess960  |  check_detection_960  |  rnqbkrbn/ppp1pppp/8/3p4/1P6/8/P1PPPPPP/RNQBKRBN w KQkq - 0 2  |  FEN: rnqbkrbn/ppp1pppp/8/3p4/1P6/8/P1PPPPPP/RNQBKRBN w KQkq - 0 2 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 621 }  |  
|  chess960_00035  |  chess960  |  castling_rules_960  |  rnqkbr1b/pppp1ppp/3P4/4P3/8/8/PPPNP1Pn/R1QKBRNB b KQkq - 0 6  |  FEN: rnqkbr1b/pppp1ppp/3P4/4P3/8/8/PPPNP1Pn/R1QKBRNB b KQkq - 0 6 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 619 }  |  
|  chess960_00036  |  chess960  |  legal_moves_960  |  bnqrkrn1/pp1p1p1p/4pbp1/2p3N1/8/P2P4/1PPRPPPP/BNQ1KR1B b Kkq - 1 5  |  FEN: bnqrkrn1/pp1p1p1p/4pbp1/2p3N1/8/P2P4/1PPRPPPP/BNQ1KR1B b Kkq - 1 5 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 c5c4 c8c6 c8c7 d7d5 d7d6 e6e5 e8e7 f6b2 f6c3 f6d4 f6e5 f6e7 f6g5 f6g7 f6h8 g8e7 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 307 }  |  
|  chess960_00037  |  chess960  |  check_detection_960  |  rkqbrnb1/pppp2pp/6n1/4pp2/2P1P2P/6N1/PP1P1PP1/RKQBR1BN b KQkq - 1 4  |  FEN: rkqbrnb1/pppp2pp/6n1/4pp2/2P1P2P/6N1/PP1P1PP1/RKQBR1BN b KQkq - 1 4 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 909 }  |  
|  chess960_00038  |  chess960  |  castling_rules_960  |  nrknb1rq/p1pp1ppp/3b4/Bp2p3/P2P4/1P6/2P1PPPP/NRKN1BRQ b KQkq - 2 4  |  FEN: nrknb1rq/p1pp1ppp/3b4/Bp2p3/P2P4/1P6/2P1PPPP/NRKN1BRQ b KQkq - 2 4 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 282 }  |  
|  chess960_00039  |  chess960  |  legal_moves_960  |  brnnkr1b/1pppp1p1/p4p2/3q4/8/2N1PP2/PPPPNKpP/BRR3QB w kq - 2 8  |  FEN: brnnkr1b/1pppp1p1/p4p2/3q4/8/2N1PP2/PPPPNKpP/BRR3QB w kq - 2 8 List all legal moves.  |  Side to move: white. Legal moves: a2a3 a2a4 b2b3 b2b4 c1d1 c1e1 c1f1 c3a4 c3b5 c3d1 c3d5 c3e4 d2d3 d2d4 e2d4 e2f4 e2g3 e3e4 f2e1 f2g2 f2g3 f3f4 g1d1 g1e1 g1f1 g1g2 h1g2 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 467 }  |  
|  chess960_00040  |  chess960  |  check_detection_960  |  qrn2krb/pppbp1np/5pp1/3p4/PP4P1/2P5/2NPPP1P/QRN1BKRB w KQkq - 1 7  |  FEN: qrn2krb/pppbp1np/5pp1/3p4/PP4P1/2P5/2NPPP1P/QRN1BKRB w KQkq - 1 7 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 395 }  |  
|  chess960_00041  |  chess960  |  castling_rules_960  |  nrbqnkrb/pppppppp/8/8/8/3P4/PPPQPPPP/NRB1NRKB b kq - 4 3  |  FEN: nrbqnkrb/pppppppp/8/8/8/3P4/PPPQPPPP/NRB1NRKB b kq - 4 3 What castling options are available?  |  Castling available: kingside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 135 }  |  
|  chess960_00042  |  chess960  |  legal_moves_960  |  bqrnkbnr/1pppp1pp/5p2/p7/8/3P1P2/PPP1PKPP/BQRN1BNR b kq - 1 3  |  FEN: bqrnkbnr/1pppp1pp/5p2/p7/8/3P1P2/PPP1PKPP/BQRN1BNR b kq - 1 3 List all legal moves.  |  Side to move: black. Legal moves: a5a4 b7b5 b7b6 b8a7 c7c5 c7c6 d7d5 d7d6 d8c6 d8e6 d8f7 e7e5 e7e6 e8f7 f6f5 g7g5 g7g6 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 482 }  |  
|  chess960_00043  |  chess960  |  check_detection_960  |  bnrqkbrn/pp1pppp1/2p5/7p/6Q1/2N1P3/PPPP1PPP/B1R1KBRN b KQkq - 1 3  |  FEN: bnrqkbrn/pp1pppp1/2p5/7p/6Q1/2N1P3/PPPP1PPP/B1R1KBRN b KQkq - 1 3 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 322 }  |  
|  chess960_00044  |  chess960  |  castling_rules_960  |  rqk1nrbb/pppppppp/4n3/8/8/2P5/PP1PPPPP/RQKNNRBB w KQkq - 1 2  |  FEN: rqk1nrbb/pppppppp/4n3/8/8/2P5/PP1PPPPP/RQKNNRBB w KQkq - 1 2 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 703 }  |  
|  chess960_00045  |  chess960  |  legal_moves_960  |  1nrkq1br/p1ppbppp/1p6/1N2p3/n1P1P3/1PR5/3P1PPP/N2KQBBR b Kkq - 0 7  |  FEN: 1nrkq1br/p1ppbppp/1p6/1N2p3/n1P1P3/1PR5/3P1PPP/N2KQBBR b Kkq - 0 7 List all legal moves.  |  Side to move: black. Legal moves: a4b2 a4c3 a4c5 a7a5 a7a6 b8a6 b8c6 c7c5 c7c6 d7d5 d7d6 d8c8 e7a3 e7b4 e7c5 e7d6 e7f6 e7f8 e7g5 e7h4 e8f8 f7f5 f7f6 g7g5 g7g6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 78 }  |  
|  chess960_00046  |  chess960  |  check_detection_960  |  bnqrkrnb/p1ppppp1/8/1p5p/8/4PN2/PPPP1PPP/BNQRKR1B w KQkq - 0 3  |  FEN: bnqrkrnb/p1ppppp1/8/1p5p/8/4PN2/PPPP1PPP/BNQRKR1B w KQkq - 0 3 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 307 }  |  
|  chess960_00047  |  chess960  |  castling_rules_960  |  1rkrnbbn/1qpp1pp1/4p3/pp6/7p/PPP1PB2/1Q1P1PPP/1RKRN1BN b KQkq - 1 7  |  FEN: 1rkrnbbn/1qpp1pp1/4p3/pp6/7p/PPP1PB2/1Q1P1PPP/1RKRN1BN b KQkq - 1 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 878 }  |  
|  chess960_00048  |  chess960  |  legal_moves_960  |  b1qnkr2/p2pnpb1/1rp4p/1p2B3/3P1p2/1P2P3/PRP2KPP/Q2N1RNB w k - 0 10  |  FEN: b1qnkr2/p2pnpb1/1rp4p/1p2B3/3P1p2/1P2P3/PRP2KPP/Q2N1RNB w k - 0 10 List all legal moves.  |  Side to move: white. Legal moves: a1b1 a1c1 a2a3 a2a4 b2b1 b3b4 c2c3 c2c4 d1c3 d4d5 e3e4 e3f4 e5b8 e5c7 e5d6 e5f4 e5f6 e5g7 f1e1 f2e1 f2e2 f2f3 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 595 }  |  
|  chess960_00049  |  chess960  |  check_detection_960  |  rnknqrbb/pppppp1p/8/6p1/8/N7/PPPPPPPP/R1KNQRBB w KQkq - 0 2  |  FEN: rnknqrbb/pppppp1p/8/6p1/8/N7/PPPPPPPP/R1KNQRBB w KQkq - 0 2 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 559 }  |  
|  chess960_00050  |  chess960  |  castling_rules_960  |  brk1q1rn/ppppbppp/2n5/4p3/2PP4/4N3/PP2PPPP/BRK1QBRN w KQkq - 1 4  |  FEN: brk1q1rn/ppppbppp/2n5/4p3/2PP4/4N3/PP2PPPP/BRK1QBRN w KQkq - 1 4 What castling options are available?  |  Castling available: queenside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 818 }  |  
|  chess960_00051  |  chess960  |  legal_moves_960  |  qrkrbnnb/1ppppppp/p7/8/3PP3/8/PPP2PPP/QRKRBNNB b KQkq - 0 2  |  FEN: qrkrbnnb/1ppppppp/p7/8/3PP3/8/PPP2PPP/QRKRBNNB b KQkq - 0 2 List all legal moves.  |  Side to move: black. Legal moves: a6a5 a8a7 b7b5 b7b6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 f8e6 f8g6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 875 }  |  
|  chess960_00052  |  chess960  |  check_detection_960  |  rbk2qrn/2ppp1p1/p4pb1/np5p/2PP2P1/2NB1PN1/PP1BP2P/RK3QR1 w kq - 0 11  |  FEN: rbk2qrn/2ppp1p1/p4pb1/np5p/2PP2P1/2NB1PN1/PP1BP2P/RK3QR1 w kq - 0 11 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 824 }  |  
|  chess960_00053  |  chess960  |  castling_rules_960  |  1bqr1nkr/2pppp2/1p3B1p/p7/8/1P1N3P/P1PPPPK1/1BQR1N1R w kq - 0 7  |  FEN: 1bqr1nkr/2pppp2/1p3B1p/p7/8/1P1N3P/P1PPPPK1/1BQR1N1R w kq - 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 384 }  |  
|  chess960_00054  |  chess960  |  legal_moves_960  |  r1qnnkbr/1p1ppppp/p1p5/8/4Pb2/3N4/PPPP1KPP/RBQN2BR b kq - 1 5  |  FEN: r1qnnkbr/1p1ppppp/p1p5/8/4Pb2/3N4/PPPP1KPP/RBQN2BR b kq - 1 5 List all legal moves.  |  Side to move: black. Legal moves: a6a5 a8a7 a8b8 b7b5 b7b6 c6c5 c8b8 c8c7 d7d5 d7d6 d8e6 e7e5 e7e6 e8c7 e8d6 e8f6 f4b8 f4c7 f4d2 f4d6 f4e3 f4e5 f4g3 f4g5 f4h2 f4h6 f7f5 f7f6 g7g5 g7g6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 412 }  |  
|  chess960_00055  |  chess960  |  check_detection_960  |  rqkr2bb/pp1p1Np1/3n1p2/2p1p2p/2P3Pn/1P1Q4/P2PPP1P/R1KR1NBB b KQkq - 0 8  |  FEN: rqkr2bb/pp1p1Np1/3n1p2/2p1p2p/2P3Pn/1P1Q4/P2PPP1P/R1KR1NBB b KQkq - 0 8 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 895 }  |  
|  chess960_00056  |  chess960  |  castling_rules_960  |  1rnkrqnb/p1pppp1p/2b5/5Qp1/P3P3/1P6/2PP1PPP/BRNKR1NB b KQk - 0 7  |  FEN: 1rnkrqnb/p1pppp1p/2b5/5Qp1/P3P3/1P6/2PP1PPP/BRNKR1NB b KQk - 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 643 }  |  
|  chess960_00057  |  chess960  |  legal_moves_960  |  nb1nbq1r/p4kpp/1Pr1p3/3p1p2/1P3P2/6P1/P1P1PBQP/NBRN2KR b KQ - 0 8  |  FEN: nb1nbq1r/p4kpp/1Pr1p3/3p1p2/1P3P2/6P1/P1P1PBQP/NBRN2KR b KQ - 0 8 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 a7b6 a8b6 a8c7 b8c7 b8d6 b8e5 b8f4 c6b6 c6c2 c6c3 c6c4 c6c5 c6c7 c6c8 c6d6 d5d4 d8b7 e6e5 e8d7 f7e7 f7f6 f7g6 f7g8 f8b4 f8c5 f8d6 f8e7 f8g8 g7g5 g7g6 h7h5 h7h6 h8g8  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 152 }  |  
|  chess960_00058  |  chess960  |  check_detection_960  |  nnrq1rbb/p2p1kpp/1pp1p3/5p2/5PP1/5R1P/PPPPP2B/NNRQK2B b Q - 2 6  |  FEN: nnrq1rbb/p2p1kpp/1pp1p3/5p2/5PP1/5R1P/PPPPP2B/NNRQK2B b Q - 2 6 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 63 }  |  
|  chess960_00059  |  chess960  |  castling_rules_960  |  bqnbrknr/1ppp2p1/5p2/p3p2p/5Q2/P1P5/1P1PPPPP/B1NBRKNR w KQq - 0 7  |  FEN: bqnbrknr/1ppp2p1/5p2/p3p2p/5Q2/P1P5/1P1PPPPP/B1NBRKNR w KQq - 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 193 }  |  
|  chess960_00060  |  chess960  |  legal_moves_960  |  bnnqrbkr/p1pp1ppp/1p2p3/8/P2P4/8/1PP1PPPP/BNNQRBKR w KQkq - 0 3  |  FEN: bnnqrbkr/p1pp1ppp/1p2p3/8/P2P4/8/1PP1PPPP/BNNQRBKR w KQkq - 0 3 List all legal moves.  |  Side to move: white. Legal moves: a4a5 b1a3 b1c3 b1d2 b2b3 b2b4 c1a2 c1b3 c1d3 c2c3 c2c4 d1d2 d1d3 d4d5 e2e3 e2e4 f2f3 f2f4 g2g3 g2g4 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 34 }  |  
|  chess960_00061  |  chess960  |  check_detection_960  |  br1b1qkr/1pp1p1pp/pn6/3p1p2/1N2nP2/PN6/1PPPP1PP/BR1BQRK1 b kq - 3 7  |  FEN: br1b1qkr/1pp1p1pp/pn6/3p1p2/1N2nP2/PN6/1PPPP1PP/BR1BQRK1 b kq - 3 7 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 433 }  |  
|  chess960_00062  |  chess960  |  castling_rules_960  |  rnbkqb1r/pppppppp/5n2/8/8/3P4/PPP1PPPP/RNBKQBNR w KQkq - 1 2  |  FEN: rnbkqb1r/pppppppp/5n2/8/8/3P4/PPP1PPPP/RNBKQBNR w KQkq - 1 2 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 534 }  |  
|  chess960_00063  |  chess960  |  legal_moves_960  |  brqkrbnn/ppppppp1/8/7p/4P3/8/PPPP1PPP/BRQKRBNN w KQkq - 0 2  |  FEN: brqkrbnn/ppppppp1/8/7p/4P3/8/PPPP1PPP/BRQKRBNN w KQkq - 0 2 List all legal moves.  |  Side to move: white. Legal moves: a2a3 a2a4 b2b3 b2b4 c2c3 c2c4 d1e2 d2d3 d2d4 e1e2 e1e3 e4e5 f1a6 f1b5 f1c4 f1d3 f1e2 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h1g3 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 882 }  |  
|  chess960_00064  |  chess960  |  check_detection_960  |  bb1rkrn1/p1pppp1p/1n4p1/1p6/2P3PP/2q2P2/PP1PP3/BBNRKRNQ w KQkq - 1 5  |  FEN: bb1rkrn1/p1pppp1p/1n4p1/1p6/2P3PP/2q2P2/PP1PP3/BBNRKRNQ w KQkq - 1 5 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 368 }  |  
|  chess960_00065  |  chess960  |  castling_rules_960  |  1qkr1r1b/ppBpp2p/4b3/5pp1/N2n2P1/7P/PPPPP3/Q1RKRN1B w KQ - 1 11  |  FEN: 1qkr1r1b/ppBpp2p/4b3/5pp1/N2n2P1/7P/PPPPP3/Q1RKRN1B w KQ - 1 11 What castling options are available?  |  Castling available: queenside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 303 }  |  
|  chess960_00066  |  chess960  |  legal_moves_960  |  rkq1nrb1/p1p1pp1p/1pBp4/4b1p1/1n6/2PP2P1/P3PP1P/RKQNNRB1 b KQkq - 1 8  |  FEN: rkq1nrb1/p1p1pp1p/1pBp4/4b1p1/1n6/2PP2P1/P3PP1P/RKQNNRB1 b KQkq - 1 8 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b4a2 b4a6 b4c2 b4c6 b4d3 b4d5 b6b5 c8a6 c8b7 c8d7 c8d8 c8e6 c8f5 c8g4 c8h3 d6d5 e5c3 e5d4 e5f4 e5f6 e5g3 e5g7 e5h8 e7e6 e8f6 e8g7 f7f5 f7f6 g5g4 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 719 }  |  
|  chess960_00067  |  chess960  |  check_detection_960  |  rbbnqknr/ppppp1pp/8/8/5p2/2N4N/PPPPPPPP/RBB1QK1R w KQkq - 0 3  |  FEN: rbbnqknr/ppppp1pp/8/8/5p2/2N4N/PPPPPPPP/RBB1QK1R w KQkq - 0 3 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 516 }  |  
|  chess960_00068  |  chess960  |  castling_rules_960  |  rnbnqbkr/1p2ppp1/3p3p/p1p5/5P2/P1P1K1Q1/1P1PP1PP/RNBN1B1R w kq - 1 7  |  FEN: rnbnqbkr/1p2ppp1/3p3p/p1p5/5P2/P1P1K1Q1/1P1PP1PP/RNBN1B1R w kq - 1 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 438 }  |  
|  chess960_00069  |  chess960  |  legal_moves_960  |  rnbnqbkr/pppppppp/8/8/8/8/PPPPPPPP/RNBNQBKR w KQkq - 0 1  |  FEN: rnbnqbkr/pppppppp/8/8/8/8/PPPPPPPP/RNBNQBKR w KQkq - 0 1 List all legal moves.  |  Side to move: white. Legal moves: a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 c2c3 c2c4 d1c3 d1e3 d2d3 d2d4 e2e3 e2e4 f2f3 f2f4 g2g3 g2g4 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 438 }  |  
|  chess960_00070  |  chess960  |  check_detection_960  |  r1b1rb1n/1p1ppp1p/pq4pn/k1p3N1/2B5/2P1PPP1/PP1P1N1P/RKBQR3 w KQ - 4 9  |  FEN: r1b1rb1n/1p1ppp1p/pq4pn/k1p3N1/2B5/2P1PPP1/PP1P1N1P/RKBQR3 w KQ - 4 9 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 902 }  |  
|  chess960_00071  |  chess960  |  castling_rules_960  |  brnbnqkr/pp1ppppp/8/2p5/7P/1N6/PPPPPPP1/BR1BNQKR b KQkq - 0 2  |  FEN: brnbnqkr/pp1ppppp/8/2p5/7P/1N6/PPPPPPP1/BR1BNQKR b KQkq - 0 2 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 433 }  |  
|  chess960_00072  |  chess960  |  legal_moves_960  |  nrqbbkrn/pppp1pp1/4p2p/8/2P5/7P/PP1PPPP1/NRQBBKRN w KQkq - 0 3  |  FEN: nrqbbkrn/pppp1pp1/4p2p/8/2P5/7P/PP1PPPP1/NRQBBKRN w KQkq - 0 3 List all legal moves.  |  Side to move: white. Legal moves: a1b3 a1c2 a2a3 a2a4 b2b3 b2b4 c1c2 c1c3 c4c5 d1a4 d1b3 d1c2 d2d3 d2d4 e2e3 e2e4 f1g1 f2f3 f2f4 g2g3 g2g4 h1g3 h3h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 329 }  |  
|  chess960_00073  |  chess960  |  check_detection_960  |  nr1nkqrb/ppp1ppp1/7p/3p1b2/4P3/4NP2/PPPP2PP/NRB1KQRB w KQkq - 1 4  |  FEN: nr1nkqrb/ppp1ppp1/7p/3p1b2/4P3/4NP2/PPPP2PP/NRB1KQRB w KQkq - 1 4 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 167 }  |  
|  chess960_00074  |  chess960  |  castling_rules_960  |  bnrbkq1r/1pppp1pp/7n/p4p2/6PP/N7/PPPPPP2/B1RBKQNR b KQkq - 0 4  |  FEN: bnrbkq1r/1pppp1pp/7n/p4p2/6PP/N7/PPPPPP2/B1RBKQNR b KQkq - 0 4 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 241 }  |  
|  chess960_00075  |  chess960  |  legal_moves_960  |  rnn1kbbr/p1p1p2p/3q2p1/1p1p1p2/P7/1P1P3P/N1P1PPP1/RN1QKBBR w KQkq - 1 7  |  FEN: rnn1kbbr/p1p1p2p/3q2p1/1p1p1p2/P7/1P1P3P/N1P1PPP1/RN1QKBBR w KQkq - 1 7 List all legal moves.  |  Side to move: white. Legal moves: a2b4 a2c1 a2c3 a4a5 a4b5 b1a3 b1c3 b1d2 b3b4 c2c3 c2c4 d1c1 d1d2 d3d4 e1d2 e2e3 e2e4 f2f3 f2f4 g1h2 g2g3 g2g4 h1h2 h3h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 446 }  |  
|  chess960_00076  |  chess960  |  check_detection_960  |  1bnkr1b1/rppp2q1/4p1n1/p4ppp/P4P1P/6P1/NPPPPQ2/RB1KR1BN w KQk - 5 9  |  FEN: 1bnkr1b1/rppp2q1/4p1n1/p4ppp/P4P1P/6P1/NPPPPQ2/RB1KR1BN w KQk - 5 9 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 652 }  |  
|  chess960_00077  |  chess960  |  castling_rules_960  |  rqkbr1b1/p1pnpppp/1B1p4/1p6/2P1Q1P1/4NP2/PP1PP2P/R1KB1R1N b Q - 7 10  |  FEN: rqkbr1b1/p1pnpppp/1B1p4/1p6/2P1Q1P1/4NP2/PP1PP2P/R1KB1R1N b Q - 7 10 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 893 }  |  
|  chess960_00078  |  chess960  |  legal_moves_960  |  r1krqbbn/p2pp3/nB6/5ppp/5P1P/1P1P2N1/P1P1P1P1/RNKRQB2 b KQkq - 0 7  |  FEN: r1krqbbn/p2pp3/nB6/5ppp/5P1P/1P1P2N1/P1P1P1P1/RNKRQB2 b KQkq - 0 7 List all legal moves.  |  Side to move: black. Legal moves: a6b4 a6b8 a6c5 a6c7 a7b6 a8b8 c8b7 c8b8 d7d5 d7d6 e7e5 e7e6 e8f7 e8g6 f8g7 f8h6 g5f4 g5g4 g5h4 g8b3 g8c4 g8d5 g8e6 g8f7 g8h7 h8f7 h8g6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 654 }  |  
|  chess960_00079  |  chess960  |  check_detection_960  |  rbbk1qnr/1ppp1p1p/p2n4/4p1p1/1P5P/5PP1/P1PPP3/RBBKNQNR w KQkq - 1 5  |  FEN: rbbk1qnr/1ppp1p1p/p2n4/4p1p1/1P5P/5PP1/P1PPP3/RBBKNQNR w KQkq - 1 5 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 724 }  |  
|  chess960_00080  |  chess960  |  castling_rules_960  |  1bqkrn1n/1pppp2p/r4p2/p1B2B2/1P2Pp1P/2P5/b2P2P1/R1QKRN1N b KQk e3 0 7  |  FEN: 1bqkrn1n/1pppp2p/r4p2/p1B2B2/1P2Pp1P/2P5/b2P2P1/R1QKRN1N b KQk e3 0 7 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 892 }  |  
|  chess960_00081  |  chess960  |  legal_moves_960  |  1nrknrqb/2ppppp1/1p5p/p2b4/3P4/NP4PP/P1P1PP1Q/B1RKNR1B w KQkq - 0 7  |  FEN: 1nrknrqb/2ppppp1/1p5p/p2b4/3P4/NP4PP/P1P1PP1Q/B1RKNR1B w KQkq - 0 7 List all legal moves.  |  Side to move: white. Legal moves: a1b2 a1c3 a3b1 a3b5 a3c4 b3b4 c1b1 c2c3 c2c4 d1c1 d1d2 e1d3 e1f3 e1g2 e2e3 e2e4 f1g1 f2f3 f2f4 g3g4 h1d5 h1e4 h1f3 h1g2 h2g1 h2g2 h3h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 275 }  |  
|  chess960_00082  |  chess960  |  check_detection_960  |  brnbnkqr/pppp1ppp/4p3/8/8/3P1N2/PPP1PPPP/BRNB1KQR b KQkq - 0 2  |  FEN: brnbnkqr/pppp1ppp/4p3/8/8/3P1N2/PPP1PPPP/BRNB1KQR b KQkq - 0 2 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 449 }  |  
|  chess960_00083  |  chess960  |  castling_rules_960  |  n2kqrnb/p2ppp1p/br6/1pp3p1/7P/5BP1/PPPPPP2/NRBKQRN1 w KQk - 4 6  |  FEN: n2kqrnb/p2ppp1p/br6/1pp3p1/7P/5BP1/PPPPPP2/NRBKQRN1 w KQk - 4 6 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 343 }  |  
|  chess960_00084  |  chess960  |  legal_moves_960  |  nrbnqk1r/1pppp3/7b/5ppp/5P1P/P3P3/1PPP1NP1/NRB1QBKR b KQ - 1 7  |  FEN: nrbnqk1r/1pppp3/7b/5ppp/5P1P/P3P3/1PPP1NP1/NRB1QBKR b KQ - 1 7 List all legal moves.  |  Side to move: black. Legal moves: a8b6 b7b5 b7b6 c7c5 c7c6 d7d5 d7d6 d8c6 d8e6 d8f7 e7e5 e7e6 e8f7 e8g6 f8f7 f8g7 f8g8 g5f4 g5g4 g5h4 h6g7 h8g8 h8h7  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 150 }  |  
|  chess960_00085  |  chess960  |  check_detection_960  |  qnr1bbrn/ppk1pp2/2pp4/6Pp/8/N5NP/PPPPP1P1/Q1KRBBR1 w - - 1 7  |  FEN: qnr1bbrn/ppk1pp2/2pp4/6Pp/8/N5NP/PPPPP1P1/Q1KRBBR1 w - - 1 7 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 298 }  |  
|  chess960_00086  |  chess960  |  castling_rules_960  |  qrbbkr2/ppppp1pp/2n5/5p2/1PPP1P2/P3P1nP/1R6/Q1B1KRNN b Kkq - 1 10  |  FEN: qrbbkr2/ppppp1pp/2n5/5p2/1PPP1P2/P3P1nP/1R6/Q1B1KRNN b Kkq - 1 10 What castling options are available?  |  Castling available: kingside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 869 }  |  
|  chess960_00087  |  chess960  |  legal_moves_960  |  rkr1nb1n/1b1p2pp/ppp2p2/P3p3/1P1PP2P/3B4/2N2PP1/RKBR2QN w KQq - 0 10  |  FEN: rkr1nb1n/1b1p2pp/ppp2p2/P3p3/1P1PP2P/3B4/2N2PP1/RKBR2QN w KQq - 0 10 List all legal moves.  |  Side to move: white. Legal moves: a1a2 a1a3 a1a4 a5b6 b1a2 b1b2 b4b5 c1a3 c1b2 c1d2 c1e3 c1f4 c1g5 c1h6 c2a3 c2e1 c2e3 d1d2 d1e1 d1f1 d3a6 d3b5 d3c4 d3e2 d3f1 d4d5 d4e5 f2f3 f2f4 g1e1 g1f1 g1h2 g2g3 g2g4 h1g3 h4h5  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 934 }  |  
|  chess960_00088  |  chess960  |  check_detection_960  |  brq1nkrn/pppp1ppp/4p3/6b1/4P3/P4B2/1PPP1PPP/BRQ1NKRN w KQkq - 1 4  |  FEN: brq1nkrn/pppp1ppp/4p3/6b1/4P3/P4B2/1PPP1PPP/BRQ1NKRN w KQkq - 1 4 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 593 }  |  
|  chess960_00089  |  chess960  |  castling_rules_960  |  q1brkn1r/pp1pp1pp/3b3n/2p2p2/7P/4PN2/PPPP1PP1/QBBRKN1R w KQkq - 3 5  |  FEN: q1brkn1r/pp1pp1pp/3b3n/2p2p2/7P/4PN2/PPPP1PP1/QBBRKN1R w KQkq - 3 5 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 676 }  |  
|  chess960_00090  |  chess960  |  legal_moves_960  |  nbbrkrqn/ppppppp1/8/7p/4P3/2P5/PPNP1PPP/1BBRKRQN b KQkq - 1 3  |  FEN: nbbrkrqn/ppppppp1/8/7p/4P3/2P5/PPNP1PPP/1BBRKRQN b KQkq - 1 3 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 a8b6 b7b5 b7b6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 g7g5 g7g6 g8h7 h5h4 h8g6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 356 }  |  
|  chess960_00091  |  chess960  |  check_detection_960  |  rkbbnrnq/ppppp1p1/5p1p/8/2P5/1P6/P2PPPPP/RKBBNRNQ w KQkq - 0 3  |  FEN: rkbbnrnq/ppppp1p1/5p1p/8/2P5/1P6/P2PPPPP/RKBBNRNQ w KQkq - 0 3 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 853 }  |  
|  chess960_00092  |  chess960  |  castling_rules_960  |  nrnkB1r1/1pp1ppbp/4q3/p5p1/4P3/1N1P4/PPP2PPP/NR1KB1RQ w KQkq - 1 8  |  FEN: nrnkB1r1/1pp1ppbp/4q3/p5p1/4P3/1N1P4/PPP2PPP/NR1KB1RQ w KQkq - 1 8 What castling options are available?  |  Castling available: queenside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 186 }  |  
|  chess960_00093  |  chess960  |  legal_moves_960  |  rq1nbbkr/ppppppp1/3n3p/8/8/2P1P2P/PP1P1PP1/RQNNBBKR b KQkq - 0 3  |  FEN: rq1nbbkr/ppppppp1/3n3p/8/8/2P1P2P/PP1P1PP1/RQNNBBKR b KQkq - 0 3 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b7b5 b7b6 b8c8 c7c5 c7c6 d6b5 d6c4 d6c8 d6e4 d6f5 d8c6 d8e6 e7e5 e7e6 f7f5 f7f6 g7g5 g7g6 h6h5 h8h7  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 410 }  |  
|  chess960_00094  |  chess960  |  check_detection_960  |  nbrqbkrn/pppppppp/8/8/5P2/8/PPPPP1PP/NBRQBKRN b KQkq - 0 1  |  FEN: nbrqbkrn/pppppppp/8/8/5P2/8/PPPPP1PP/NBRQBKRN b KQkq - 0 1 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 328 }  |  
|  chess960_00095  |  chess960  |  castling_rules_960  |  bbkr1rqn/p1pp1ppp/1p2pn2/5P2/6P1/4P3/PPPP3P/BBRKNRQN w KQ - 1 5  |  FEN: bbkr1rqn/p1pp1ppp/1p2pn2/5P2/6P1/4P3/PPPP3P/BBRKNRQN w KQ - 1 5 What castling options are available?  |  Castling available: queenside.  |  exact_match  |  { "is_chess960": true, "chess960_id": 832 }  |  
|  chess960_00096  |  chess960  |  legal_moves_960  |  rbnn1kbr/pp1qpppp/2p5/2Bp4/5P2/8/PPPPPNPP/RBN1QK1R b KQkq - 3 4  |  FEN: rbnn1kbr/pp1qpppp/2p5/2Bp4/5P2/8/PPPPPNPP/RBN1QK1R b KQkq - 3 4 List all legal moves.  |  Side to move: black. Legal moves: a7a5 a7a6 b7b5 b7b6 b8c7 b8d6 b8e5 b8f4 c8b6 c8d6 d5d4 d7c7 d7d6 d7e6 d7e8 d7f5 d7g4 d7h3 d8e6 f7f5 f7f6 f8e8 g7g5 g7g6 h7h5 h7h6  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 444 }  |  
|  chess960_00097  |  chess960  |  check_detection_960  |  nrb1knrq/1ppp3p/p3ppp1/8/2P2P2/P2PK1N1/1P1BP1PP/NR1B1R1Q b kq - 0 10  |  FEN: nrb1knrq/1ppp3p/p3ppp1/8/2P2P2/P2PK1N1/1P1BP1PP/NR1B1R1Q b kq - 0 10 Detect the game state: check, checkmate, stalemate, or none.  |  Normal position -- no check, checkmate, or stalemate.  |  check_state  |  { "is_chess960": true, "chess960_id": 277 }  |  
|  chess960_00098  |  chess960  |  castling_rules_960  |  rkr2qb1/pp1pp3/2p2n2/1n2bppp/PB6/R1P2PP1/1P1PP2P/1KRNQ2B b Kkq - 1 10  |  FEN: rkr2qb1/pp1pp3/2p2n2/1n2bppp/PB6/R1P2PP1/1P1PP2P/1KRNQ2B b Kkq - 1 10 What castling options are available?  |  No castling available.  |  exact_match  |  { "is_chess960": true, "chess960_id": 959 }  |  
|  chess960_00099  |  chess960  |  legal_moves_960  |  bbrkqnrn/2p2ppp/p7/1p1pp3/4P3/1P3P2/P1PPK1PP/BBR1QNRN w kq - 0 5  |  FEN: bbrkqnrn/2p2ppp/p7/1p1pp3/4P3/1P3P2/P1PPK1PP/BBR1QNRN w kq - 0 5 List all legal moves.  |  Side to move: white. Legal moves: a1b2 a1c3 a1d4 a1e5 a2a3 a2a4 b3b4 c1d1 c2c3 c2c4 d2d3 d2d4 e1d1 e1f2 e1g3 e1h4 e2d1 e2d3 e2e3 e2f2 e4d5 f1e3 f1g3 f3f4 g2g3 g2g4 h1f2 h1g3 h2h3 h2h4  |  uci_set_jaccard  |  { "is_chess960": true, "chess960_id": 800 }  |  
End of preview. Expand in Data Studio⟨50⟩
* * *
  *  Previous⟨29⟩
  * 1⟨51⟩
  * 2⟨52⟩
  * 3⟨53⟩
  * ...⟨54⟩
  * 5⟨55⟩
  * Next ⟨52⟩


  * Loading⟨56⟩
  * Eval Splits⟨57⟩
  * Frozen Benchmark⟨58⟩


#   ⟨59⟩ Chess SFT Eval and Benchmark 
Held-out evaluation splits and a frozen benchmark for Chess-Nut-Engine/chess-sft-corpus-4x⟨60⟩. Every FEN in these files is excluded from generated training data (the blocklist is game-scoped: sibling positions of eval games are excluded too).
  * Frozen from the 4x corpus generation run of 2026-07-06 (generator revision 3cd161b1078cdfa6598fba939f40250072adb524)
  * Benchmark: 13,000 frozen examples across 9 splits; eval splits share the game-scoped blocklist (182,061 FENs) excluded from the training corpus

  
|   |   |  
| --- | --- |  
| **Eval examples**  | 13,000  |  
| **Benchmark examples**  | 13,000  |  
| **Format**  | JSONL  |  
##   ⟨56⟩ Loading 

```
from datasets import load_dataset

eval_ds = load_dataset("Chess-Nut-Engine/chess-sft-corpus-4x-eval", "eval_splits")
bench_ds = load_dataset("Chess-Nut-Engine/chess-sft-corpus-4x-eval", "benchmark")

```

##   ⟨57⟩ Eval Splits   
| Split  | Description  | Examples  | Size  |  
| --- | --- | --- | --- |  
| `chess960`  | Fischer Random positions  | 500  | 0.1 MB  |  
| `endgames`  | Tablebase-backed endgame play  | 1,500  | 0.2 MB  |  
| `evaluation`  | Position assessment  | 1,500  | 0.3 MB  |  
| `mate`  | MATE move-choice examples  | 1,000  | 0.1 MB  |  
| `openings`  | Opening knowledge with ECO holdout  | 500  | 0.2 MB  |  
| `perception`  | Board reading and representation  | 2,000  | 0.3 MB  |  
| `planning`  | Best move, puzzle, and consequence tasks  | 2,000  | 1.0 MB  |  
| `rules`  | Move legality and chess rules  | 2,000  | 0.3 MB  |  
| `tactics`  | Tactical motifs and puzzle labels  | 2,000  | 1.0 MB  |  
##   ⟨58⟩ Frozen Benchmark   
| Split  | Description  | Examples  | Size  |  
| --- | --- | --- | --- |  
| `chess960`  | Fischer Random positions  | 500  | 0.2 MB  |  
| `endgames`  | Tablebase-backed endgame play  | 1,500  | 0.5 MB  |  
| `evaluation`  | Position assessment  | 1,500  | 0.7 MB  |  
| `mate`  | MATE move-choice examples  | 1,000  | 0.4 MB  |  
| `openings`  | Opening knowledge with ECO holdout  | 500  | 0.3 MB  |  
| `perception`  | Board reading and representation  | 2,000  | 1.5 MB  |  
| `planning`  | Best move, puzzle, and consequence tasks  | 2,000  | 1.4 MB  |  
| `rules`  | Move legality and chess rules  | 2,000  | 1.6 MB  |  
| `tactics`  | Tactical motifs and puzzle labels  | 2,000  | 1.4 MB  |  
Copy to bucket new
Use this dataset 

Downloads last month
    132
Number of rows: 26,000 Total file size: 12 MB
System theme
Company
TOS⟨61⟩ Privacy⟨62⟩ About⟨63⟩ Careers⟨64⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
