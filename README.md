# DSTC 2026 Grand Final — Final Presentation Source

This repository contains the three strategies selected for the Grand Final, plus the diagnostic research used to verify what actually drives their backtests.

## Eligibility lock

The Grand Final brief requires the team to present 3 strategies selected from strategies published in Round 1/2, with at least one Vietnam equity strategy, at least one VN30F1M strategy, and all three strategies at **Published** status.

Therefore the **competition-facing final set remains the three already-Published strategies below**. The later SMALL-CAP candidate `N-G` is retained only as post-selection diagnostic research; it is **not** the final Strategy 3 because it is not an eligible Published selection for the Grand Final deck.

## Final 3 strategies

### Strategy 1 — Equity: VN-MID-CAP — `lsGgvzSWeg`
- Status: **Published** · renamed `Strategy 1`
- Full: Sharpe **2.80** · CAGR 25.0% · MaxDD -6.4% · PF 1.65 · 1,220 trades
- Train/Test Sharpe: 3.00 → **2.54**
- Cost: 19.7% total fees over 5y (~3.9%/yr)
- Original hypothesis: equity issuance dilution predicts underperformance.
- Diagnostic interpretation: the issuance direction is economically consistent when used SHORT, but the published strategy's dominant alpha comes from the MID-CAP cross-sectional market-factor skeleton, especially `+ volatility - traded value`. Issuance is best presented as a conditioning/filter variable rather than the sole alpha engine.

### Strategy 2 — Derivative: VN30F1M-30MIN — `EuVTWCWMNF`
- Status: **Published** · renamed `Strategy 2`
- Full: Sharpe **2.84** · CAGR 39.8% · MaxDD -7.1% · PF 2.07 · 2,210 trades
- Train/Test Sharpe: 3.09 → **2.39**
- Cost: 39.8% total fees over 5y (~8%/yr)
- Interpretation: intraday futures momentum is the core edge; relative-volume weighting improves signal quality; VN30 confirmation reduces trades/cost and raises trade quality; threshold perturbations remain robust.

### Strategy 3 — Free: Equity VN-MID-CAP — `Z0URlGzUp9`
- Status: **Published** · renamed `Strategy 3`
- Full: Sharpe **2.79** · CAGR 23.0% · MaxDD -6.3% · PF 1.62 · 1,220 trades
- Train/Test Sharpe: 2.92 → **2.40**
- Cost: 17.8% total fees over 5y (~3.6%/yr)
- Original hypothesis: buyback commitment predicts outperformance.
- Diagnostic interpretation: the buyback hypothesis is **not supported** by the data. Genuine buyback cash-flow observations are sparse and predominantly negative-signed, while the published filter uses `bought >= 0`. Correcting the sign does not create robust alpha. Performance is therefore attributable mainly to the shared MID-CAP market-factor skeleton. S1/S3 daily-return correlation is ~0.90, so these two strategies should not be presented as independent diversification engines.

## Research conclusion

The diagnostic process produced three different outcomes:

1. **Strategy 1 — REFINE:** the original economic intuition partly survives, but issuance is mainly a conditioning variable; core cross-sectional alpha is the volatility/liquidity spread.
2. **Strategy 2 — KEEP:** the original momentum/volume/VN30 story survives component ablation and threshold robustness checks.
3. **Strategy 3 — REJECT ORIGINAL HYPOTHESIS:** the published strategy still has strong OOS metrics, but the buyback explanation does not survive diagnostic testing and the strategy is highly correlated with S1.

This distinction is intentional and should be visible in the presentation: the research process is not used to retrofit a story to every backtest.

## Source-of-truth files for the deck

- `FINAL_PRESENTATION_SOURCE.md` — corrected Q1-Q5 content, metrics, caveats, and claims allowed on slides.
- `PRESENTATION_LAYOUT_7MIN.md` — 7-minute slide sequence and speaking-time budget.
- `ABLATION_results.md` — first diagnostic ablation.
- `SECOND_DIAGNOSTIC_RESULTS.md` — deeper attribution, sign checks, correlation, and post-selection replacement research.
- `EXPORT_best3_final.md` — historical export of the originally selected three strategies; use metrics/code, but defer to `FINAL_PRESENTATION_SOURCE.md` for the corrected narrative.

## Strategy code

- `strategy_1_equity_mid_cap_lsGgvzSWeg.py`
- `strategy_2_derivative_vn30f1m_EuVTWCWMNF.py`
- `strategy_3_equity_mid_cap_Z0URlGzUp9.py`
- `strategy_3_v2_n_g.py` — diagnostic candidate only, not competition-facing final Strategy 3.
