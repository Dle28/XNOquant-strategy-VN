# FINAL PRESENTATION SOURCE — DSTC 2026 GRAND FINAL

> Purpose: source of truth for the 7-minute deck and Q&A. This file supersedes the old narrative in `EXPORT_best3_final.md` wherever later diagnostic evidence changed the interpretation.
>
> Competition-facing strategies remain the three already-Published strategies: S1 `lsGgvzSWeg`, S2 `EuVTWCWMNF`, S3 `Z0URlGzUp9`.

---

## 0. What the presentation must prove

The Grand Final brief asks for both:

1. **Strategy results analysis** — main metrics, train/test stages, and performance relative to cost.
2. **Research and improvement process** — Q1 intuition, Q2 formulation, Q3 regime/stage analysis, Q4 strengths/weaknesses/robustness, Q5 improvements/capacity.

The deck should therefore answer one question across all three strategies:

> **Did the economic story survive diagnostic testing, and what actually drives the backtest?**

Research outcomes:

- **S1: REFINE** — issuance intuition partly survives; alpha attribution changes.
- **S2: KEEP** — original momentum story survives ablation.
- **S3: REJECT ORIGINAL HYPOTHESIS** — buyback story fails diagnostic testing; performance comes from shared market factors.

This is the central research narrative. Do not retrofit a positive story to S3.

---

# Strategy 1 — VN-MID-CAP — `lsGgvzSWeg`

## Result ribbon

| Metric | Full | Train | Test |
|---|---:|---:|---:|
| Sharpe | **2.80** | 3.00 | **2.54** |
| CAGR | **25.0%** | 31.7% | 15.3% |
| MaxDD | **-6.4%** | -6.4% | -3.7% |
| Profit Factor | **1.65** | 1.73 | 1.52 |

- Trades: 1,220
- Total fees over 5 years: 19.7% (~3.9%/year)
- OOS Sharpe retention: 2.54 / 3.00 ≈ **0.85**

## Q1 — Market intuition / origin

Original hypothesis: high equity issuance can dilute existing shareholders and may signal future underperformance.

The diagnostic supports the **direction** but not the claim that issuance is the main alpha engine:

- Pure issuance LONG: Sharpe **-0.90**
- Pure issuance SHORT: Sharpe **+0.64**

Interpretation allowed on slide:

> High issuance is economically consistent with a negative future-return signal, but it is weak as a standalone directional alpha.

## Q2 — Formulation

Published implementation:

```text
MID-CAP universe
    ↓
issuance / total assets
    ↓
cross-sectional issuance rank
    ↓
gate: 0.3 ≤ rank < 0.9
    ↓
market-factor score
+ 0.30 volatility
- 0.30 traded value
+ 0.10 earnings yield
+ 0.10 ROA
+ 0.20 issuance rank   ← published code
    ↓
demean + L1 normalize
    ↓
25% raw + 75% EMA-smoothed weights
```

Important: the published code uses `+0.20 * issuance_rank`, which is not aligned with the original "short high issuers" narrative. The diagnostic explicitly tested this mismatch rather than hiding it.

## Q3 — Stage/regime evidence

- Train Sharpe: 3.00
- Test Sharpe: 2.54
- Test MDD: -3.7%

The signal weakens OOS but does not collapse. This is evidence of reasonable stability across evaluation stages, not proof that the original issuance story is correct.

Do **not** claim specific bull/bear regime causality unless the platform data shown in the final slides supports it. Current evidence is stage-based (train/test), not a formal regime decomposition.

## Q4 — Where does the edge actually come from?

Ablation:

| Variant | Sharpe |
|---|---:|
| Volatility only | 0.80 |
| `- traded value` only | 1.14 |
| Earnings yield only | 1.07 |
| ROA only | 0.75 |
| **Volatility + (- traded value)** | **2.60** |
| + earnings yield | 2.82 |
| + ROA | 2.79 |
| Full market skeleton | **2.84** |

Issuance diagnostics:

| Variant | Sharpe |
|---|---:|
| Published S1 | 2.80 |
| Flip issuance weight to SHORT | **2.91** |
| Keep issuance gate, remove direct issuance weight | **2.94** |
| Remove issuance entirely | 2.84 |

Defensible interpretation:

> The persistent alpha is primarily a cross-sectional volatility/liquidity spread in MID-CAP stocks. Issuance is more useful as a conditioning/filter variable than as the core directional score.

Strengths:
- OOS Sharpe remains 2.54.
- MaxDD is modest at -6.4%.
- Cost is materially lower than S2.
- Both long and short sides of the market-factor skeleton are profitable in diagnostics.

Weaknesses:
- Published issuance sign is not economically aligned with the original hypothesis.
- Gate sensitivity becomes poor when the universe is restricted to high-issuance names.
- MID-CAP capacity/slippage has not been directly stress-tested in the available research.

## Q5 — Improvement

Next version should:

1. Treat issuance as a **filter/conditioning variable**, not the main alpha weight.
2. Align the direct issuance sign with the economic hypothesis if it is retained.
3. Test sector neutrality and concentration.
4. Explicitly stress transaction costs, execution delay, and liquidity capacity.

Do not claim a measured maximum capacity — it has not been quantified in the current evidence.

---

# Strategy 2 — VN30F1M 30MIN — `EuVTWCWMNF`

## Result ribbon

| Metric | Full | Train | Test |
|---|---:|---:|---:|
| Sharpe | **2.84** | 3.09 | **2.39** |
| CAGR | **39.8%** | 59.4% | 49.7% |
| MaxDD | **-7.1%** | -7.1% | -6.9% |
| Profit Factor | **2.07** | 2.16 | 1.82 |

- Trades: 2,210
- Total fees over 5 years: 39.8% (~8%/year)
- OOS Sharpe retention: 2.39 / 3.09 ≈ **0.77**

## Q1 — Market intuition

Hypothesis:

> Short-horizon futures momentum is more informative when the move is backed by abnormal participation and confirmed by the underlying VN30 index.

Edge type: **market microstructure / short-horizon momentum**.

Do not overstate a proven causal lead-lag relation. The research verifies the trading architecture through ablation; it does not estimate a structural lead-lag model.

## Q2 — Formulation

```text
VN30F1M 30MIN return
        ×
relative volume = volume / SMA12(volume)
        ↓
volume-weighted return pressure
        ↓
fast pressure = SMA2
slow pressure = SMA6
        +
VN30 fast/slow return confirmation
        +
recent volume within 0.70× to 2.20× reference volume
        ↓
LONG / SHORT at ±0.75
```

Published execution rules:
- Open times: 03:00 and 07:00
- Close windows: 04:15–04:30 and 07:30–07:50
- Position close after 2 candles

## Q3 — Stage evidence

- Train Sharpe: 3.09
- Test Sharpe: 2.39
- Test PF: 1.82
- Test MDD: -6.9%

OOS performance decays but remains strong. This is the cleanest of the three strategies in terms of story-to-code consistency.

## Q4 — Ablation and robustness

| Variant | Sharpe | Main observation |
|---|---:|---|
| Raw futures momentum | **2.60** | Core alpha already exists |
| + relative-volume weighting | **2.87** | Improves signal quality |
| + VN30 confirmation | **2.81** | Lower Sharpe but much better trade efficiency |
| Original | **2.84** | Balanced configuration |
| Threshold 0.75× | **2.86** | Robust |
| Threshold 1.25× | **2.74** | Robust |

VN30 confirmation effect versus the volume-weighted variant:
- Trades: 3,084 → 2,268 (~-26%)
- Fees: 55.5% → 40.8%
- PF: 1.80 → 2.03

Defensible interpretation:

> Raw momentum is the alpha engine; relative volume strengthens the signal; VN30 confirmation is mainly a trade-quality and cost-control layer; directional thresholds are not finely tuned.

Strengths:
- Highest full Sharpe of the selected set.
- PF > 2 full sample.
- Component-level story survives ablation.
- Threshold perturbation does not cause collapse.

Weaknesses:
- Highest transaction-cost burden of the three strategies.
- OOS Sharpe is lower than train.
- Explicit execution-delay and extra-slippage stress tests have not yet been run in the available evidence.

## Q5 — Improvement

Next version should focus on implementation rather than adding alpha factors:

1. Explicit slippage and 1-bar execution-delay tests.
2. Cost sensitivity beyond current platform fees.
3. Reduce unnecessary entries while preserving PF.
4. Estimate contract-level capacity under realistic intraday liquidity.

Do not claim a measured maximum capacity yet.

---

# Strategy 3 — VN-MID-CAP — `Z0URlGzUp9`

## Result ribbon

| Metric | Full | Train | Test |
|---|---:|---:|---:|
| Sharpe | **2.79** | 2.92 | **2.40** |
| CAGR | **23.0%** | — | — |
| MaxDD | **-6.3%** | — | -3.7% |
| Profit Factor | **1.62** | — | — |

- Trades: 1,220
- Total fees over 5 years: 17.8% (~3.6%/year)
- OOS Sharpe retention: 2.40 / 2.92 ≈ **0.82**

## Q1 — Original market intuition

Original hypothesis:

> Companies returning capital through share repurchases may signal management conviction and better per-share economics.

This was a reasonable hypothesis to test, but **the diagnostic evidence rejects it for the published implementation and available VN MID-CAP data**.

This rejection should be stated directly in the presentation.

## Q2 — Published formulation

The published strategy uses the same market-factor skeleton as S1, but conditions the universe using:

```text
bought = payments for share returns and repurchases
core = bought / total assets
base requires bought >= 0
rank core
eligible rank 0.3–0.9

signal =
+ 0.30 volatility
- 0.30 traded value
+ 0.10 earnings yield
+ 0.10 ROA
+ 0.20 buyback rank
```

## Q3 — Stage evidence

Despite the weak economic attribution, the published backtest itself is stable:

- Full Sharpe: 2.79
- Train Sharpe: 2.92
- Test Sharpe: 2.40
- Full MaxDD: -6.3%

This distinction is essential:

> **Stable backtest ≠ validated buyback hypothesis.**

## Q4 — Why the original explanation fails

Diagnostics:

- Pure buyback LONG: Sharpe **-0.24**
- Remove buyback score but keep the rest: approximately unchanged at **2.79**
- Remove buyback entirely: **2.84**, above the published 2.79
- Correct negative cash-flow sign for genuine repurchases: corrected variants remain non-robust / negative full-sample
- S1 vs S3 daily-return correlation: **0.898**

Data/sign issue:
- Genuine repurchase cash outflows are predominantly negative-signed.
- The published filter uses `bought >= 0`, so it excludes many genuine repurchase observations.
- Even after correcting the sign, buyback does not create robust alpha.

Defensible interpretation:

> S3 is a strong backtest whose original buyback explanation fails falsification. Its realized performance is mainly the same MID-CAP volatility/liquidity market-factor skeleton already present in S1.

Strengths:
- Full Sharpe 2.79.
- Test Sharpe 2.40.
- Low drawdown and lower fees than S2.

Weaknesses:
- Original buyback story is not supported.
- Buyback data is sparse and sign-sensitive.
- High correlation with S1 means weak diversification.

This should be framed as a **research result**, not hidden as an embarrassment.

## Q5 — Improvement

After the competition, the correct next step is to replace the buyback conditioning with either:

- a better-supported fundamental signal, or
- a genuinely distinct universe/mechanism.

The post-selection SMALL-CAP candidate N-G demonstrated why this direction is promising (Sharpe ~2.60, correlation with S1 ~0.07), but it is **diagnostic research only and not the competition-facing final Strategy 3**.

Capacity, execution delay, and cost-stress beyond platform fees have not been directly measured and should not be invented in the presentation.

---

# Cross-strategy comparison

| | S1 | S2 | S3 |
|---|---:|---:|---:|
| Universe | VN-MID-CAP | VN30F1M-30MIN | VN-MID-CAP |
| Full Sharpe | **2.80** | **2.84** | **2.79** |
| Test Sharpe | **2.54** | **2.39** | **2.40** |
| MaxDD | -6.4% | -7.1% | -6.3% |
| PF | 1.65 | 2.07 | 1.62 |
| 5y Fees | 19.7% | 39.8% | 17.8% |
| Research verdict | **REFINE** | **KEEP** | **REJECT STORY** |

Portfolio-level caveat:
- S1 and S3 are **not independent**: daily-return correlation ≈ 0.898.
- S2 is the genuinely distinct mechanism/asset class in the selected set.

---

# Claims allowed / claims to avoid

## Safe claims

- S1 issuance SHORT direction has positive standalone evidence, but weak magnitude.
- S1 core alpha is mainly the MID-CAP volatility/liquidity spread.
- S2 raw momentum is already profitable; volume weighting improves it; VN30 confirmation improves trade efficiency.
- S2 thresholds are robust to ±25% perturbation around the published values.
- S3 buyback hypothesis is not supported by diagnostics.
- S1 and S3 have high realized-return correlation (~0.90).
- All three published strategies retain positive and substantial Test Sharpe.

## Avoid

- “S1 is mainly a short-issuance alpha.”
- “S3 proves the buyback anomaly in Vietnam.”
- “S1 and S3 diversify each other because issuance and buyback are opposite stories.”
- “All three are independent alpha mechanisms.”
- Specific regime claims not measured by the current research.
- Maximum-capacity numbers not measured by the current research.
- Claims that execution delay or doubled costs were tested when they were not.

---

# One-sentence final takeaway

> **Our research process did not just select high Sharpe backtests; it tried to falsify their stories: one strategy was refined, one survived, and one hypothesis was rejected — while all three selected Published strategies remained robust enough OOS to present transparently.**
