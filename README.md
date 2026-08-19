# DSTC 2026 Round 3 — Final 3 Strategies

Top 3 strategies selected for the Grand Final (all **Published**, renamed **Strategy 1/2/3** on platform, deadline 20/08/2026 17:00 GMT+7):

## Strategy 1 — Equity: VN-MID-CAP — `lsGgvzSWeg` (TK1)
- Universe: VN-MID-CAP · init cash 30B VND · published 2026-08-05
- Full: Sharpe 2.80 · CAGR 25.0% · MaxDD -6.4% · PF 1.65 · Calmar 3.91 · 1,220 trades
- Train/Test: Sharpe 3.00 → **2.54** (decay 0.85) · test MDD -3.7%
- Cost: 19.7% total fees over 5y (~3.9%/yr)
- Ý tưởng: **Equity issuance dilution** — short các công ty phát hành thêm cổ phiếu (proceeds from issue / total assets).

## Strategy 2 — Derivative: VN30F1M-30MIN — `EuVTWCWMNF` (TK2)
- Universe: VN30F1M-30MIN · init cash 1B VND · published 2026-07-26
- Full: Sharpe 2.84 · CAGR 39.8% · MaxDD -7.1% · PF 2.07 · Calmar 5.57 · 2,210 trades
- Train/Test: Sharpe 3.09 → **2.39** (decay 0.77) · test MDD -6.9%
- Cost: 39.8% total fees over 5y (~8%/yr)
- Ý tưởng: **Volume-weighted return pressure** — momentum futures có xác nhận volume đồng thuận với VN30 (lead-lag microstructure).

## Strategy 3 — Free: Equity VN-MID-CAP — `Z0URlGzUp9` (TK1)
- Universe: VN-MID-CAP · init cash 30B VND · published 2026-08-05
- Full: Sharpe 2.79 · CAGR 23.0% · MaxDD -6.3% · PF 1.62 · Calmar 3.65 · 1,220 trades
- Train/Test: Sharpe 2.92 → **2.40** (decay 0.82) · test MDD -3.7%
- Cost: 17.8% total fees over 5y (~3.6%/yr)
- Ý tưởng: **Buyback commitment** — long các công ty mua lại cổ phiếu/trả cổ tức (ngược với issuance của Strategy 1).

## Files

- `strategy_1_equity_mid_cap_lsGgvzSWeg.py`
- `strategy_2_derivative_vn30f1m_EuVTWCWMNF.py`
- `strategy_3_equity_mid_cap_Z0URlGzUp9.py`
- `EXPORT_best3_final.md` — số liệu đầy đủ + câu trả lời Q1–Q5 cho slide
- `NOTES_best3_selection.md` — quá trình phân tích & chọn lựa (lý do loại LARGE-CAP overfit)
- `data/` — raw JSON từ API (full/train/test/simulate)