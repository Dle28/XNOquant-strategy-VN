# PRESENTATION LAYOUT — 7:00 GRAND FINAL PITCH

> Target: **7 slides / exactly 7 minutes**. No title-only slide. Every slide must earn speaking time.
>
> Required coverage from the Grand Final brief:
> - all 3 selected strategies;
> - main backtest metrics;
> - train/test evaluation stages;
> - performance relative to cost;
> - Q1 intuition;
> - Q2 formulation;
> - Q3 stage/regime analysis;
> - Q4 strengths, weaknesses, robustness;
> - Q5 improvements, turnover/cost/capacity.

## Core presentation story

> **We did not stop at high Sharpe. We tried to falsify the explanation behind each strategy. One story was refined, one survived, and one was rejected.**

This framing lets the deck cover both mandatory threads — strategy analysis and research process — without presenting 15 separate Q1-Q5 answers.

---

# TIME BUDGET

| Slide | Topic | Time | Running time |
|---|---|---:|---:|
| 1 | Portfolio + research question | **0:35** | 0:35 |
| 2 | Strategy 1 — REFINE | **1:15** | 1:50 |
| 3 | Strategy 2 — KEEP | **1:15** | 3:05 |
| 4 | Strategy 3 — REJECT STORY | **1:15** | 4:20 |
| 5 | OOS, risk, cost, correlation | **1:00** | 5:20 |
| 6 | Research process — what survived falsification? | **1:00** | 6:20 |
| 7 | Improvements / capacity / conclusion | **0:40** | **7:00** |

Hard rule: if rehearsal exceeds 7:00, cut wording — **do not add an eighth slide**.

---

# SLIDE 1 — THREE PUBLISHED STRATEGIES, ONE RESEARCH QUESTION

**Time: 0:00–0:35**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ FROM BACKTEST TO EVIDENCE                                           │
│ Did the economic story survive diagnostic testing?                  │
├──────────────────────┬──────────────────────┬────────────────────────┤
│ STRATEGY 1           │ STRATEGY 2           │ STRATEGY 3             │
│ VN-MID-CAP           │ VN30F1M 30MIN        │ VN-MID-CAP             │
│ Sharpe 2.80          │ Sharpe 2.84          │ Sharpe 2.79            │
│ Test 2.54            │ Test 2.39            │ Test 2.40              │
│                      │                      │                        │
│ REFINE               │ KEEP                 │ REJECT STORY           │
├──────────────────────────────────────────────────────────────────────┤
│ Published final set | Equity ✓ | Derivative ✓ | Free choice ✓       │
└──────────────────────────────────────────────────────────────────────┘
```

## On-screen content

Headline:

> **From Backtest to Evidence**

Subheadline:

> We challenged the explanation behind each Published strategy instead of fitting a story to the Sharpe ratio.

Three compact cards only:

- **S1 — VN-MID-CAP:** 2.80 full / 2.54 test → **REFINE**
- **S2 — VN30F1M:** 2.84 full / 2.39 test → **KEEP**
- **S3 — VN-MID-CAP:** 2.79 full / 2.40 test → **REJECT STORY**

## Speaking goal

35 seconds maximum:

1. State that the final set satisfies equity + VN30F1M + free-choice constraints.
2. State the central research question.
3. Preview the three outcomes: refine, keep, reject.

Do not explain formulas here.

## Rule coverage

- Strategy selection overview
- Presentation/research framing

---

# SLIDE 2 — STRATEGY 1: ISSUANCE STORY → CONDITIONING SIGNAL

**Time: 0:35–1:50**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ S1 — VN-MID-CAP | ISSUANCE-CONDITIONED MULTIFACTOR                  │
├───────────────────────┬──────────────────────────────────────────────┤
│ Q1 + Q2               │ ABLATION: WHAT ACTUALLY DRIVES ALPHA?       │
│                       │                                              │
│ Hypothesis            │ Pure issuance LONG          -0.90            │
│ High issuance         │ Pure issuance SHORT         +0.64            │
│ → dilution risk       │ Market skeleton             2.84            │
│                       │ Flip issuance sign           2.91            │
│ Published pipeline    │ Gate only, remove c          2.94            │
│ issuance gate         │                                              │
│ +vol -value +EY +ROA  │                [bar chart]                   │
│ +published c          │                                              │
├───────────────────────┴──────────────────────────────────────────────┤
│ Full 2.80 | Train 3.00 → Test 2.54 | MDD -6.4% | Fees 19.7% / 5y   │
│ VERDICT: REFINE — issuance conditions the universe; core = vol/value │
└──────────────────────────────────────────────────────────────────────┘
```

## Visuals

Use one horizontal bar chart with exactly five bars:

1. Pure issuance LONG — -0.90
2. Pure issuance SHORT — +0.64
3. Market skeleton — 2.84
4. Flip issuance sign — 2.91
5. Gate only / remove direct issuance weight — 2.94

Do not show all 20+ diagnostics.

## Speaking order

**0:35–0:55 — Q1 intuition**

- Original idea: high issuance may imply dilution / future underperformance.
- Pure-direction test supports SHORT direction only weakly.

**0:55–1:15 — Q2 formulation**

- Cross-sectional MID-CAP ranks.
- Issuance gate 0.3–0.9.
- Main score: `+volatility -traded value + earnings yield + ROA`, then normalization and EMA smoothing.

**1:15–1:40 — Q4 attribution / robustness**

- Market skeleton without issuance still gives ~2.84.
- Correcting issuance sign gives 2.91.
- Gate-only version gives 2.94.
- Therefore issuance is better interpreted as conditioning than core alpha.

**1:40–1:50 — Q3 result ribbon**

- Full 2.80; test remains 2.54; MDD -6.4%; fees ~3.9%/year.

## Exact takeaway

> **S1 survives, but with a narrower claim: issuance helps condition the opportunity set; the dominant MID-CAP alpha is the volatility/liquidity spread.**

## Do not say

- “The strategy directly shorts high issuers in the published code.”
- “Issuance is the main source of the 2.80 Sharpe.”

---

# SLIDE 3 — STRATEGY 2: THE CLEANEST ALPHA STORY

**Time: 1:50–3:05**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ S2 — VN30F1M 30MIN | VOLUME-BACKED INTRADAY MOMENTUM                │
├──────────────────────────┬───────────────────────────────────────────┤
│ SIGNAL PIPELINE          │ COMPONENT ABLATION                        │
│                          │                                           │
│ Futures return           │ Raw momentum                  2.60         │
│ × relative volume        │ + volume weighting            2.87         │
│ ↓ fast/slow pressure     │ + VN30 confirmation           2.81         │
│ + VN30 confirmation      │ Original                      2.84         │
│ + normal-volume regime   │ Threshold 0.75×               2.86         │
│ ↓                        │ Threshold 1.25×               2.74         │
│ LONG / SHORT ±0.75       │                                           │
├──────────────────────────┴───────────────────────────────────────────┤
│ Full 2.84 | Train 3.09 → Test 2.39 | PF 2.07 | MDD -7.1%            │
│ VN30 confirm: trades -26% | fees 55.5→40.8 | PF 1.80→2.03           │
│ VERDICT: KEEP                                                        │
└──────────────────────────────────────────────────────────────────────┘
```

## Visuals

Right side: six bars or a compact step chart.

Under it, three large efficiency callouts:

- **Trades -26%**
- **Fees 55.5 → 40.8**
- **PF 1.80 → 2.03**

## Speaking order

**1:50–2:10 — Q1**

- Short-horizon momentum is more credible when futures pressure is volume-backed and agrees with VN30.
- Edge type: market microstructure / intraday momentum.

**2:10–2:30 — Q2**

- Return × relative volume.
- 2-bar and 6-bar pressure.
- VN30 fast/slow confirmation.
- Normal-volume filter and fixed intraday execution windows.

**2:30–2:55 — Q4 robustness**

- Raw momentum already 2.60.
- Volume weighting improves to 2.87.
- VN30 confirmation sacrifices little Sharpe but removes ~26% trades and improves PF/cost efficiency.
- ±25% thresholds stay 2.74–2.86.

**2:55–3:05 — Q3 metrics**

- Full 2.84; test 2.39; PF 2.07; MDD -7.1%.

## Exact takeaway

> **S2 is the cleanest strategy: momentum is the alpha engine, volume improves signal quality, and VN30 confirmation is a cost/risk filter.**

---

# SLIDE 4 — STRATEGY 3: A STRONG BACKTEST, A REJECTED HYPOTHESIS

**Time: 3:05–4:20**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ S3 — VN-MID-CAP | BUYBACK HYPOTHESIS FAILED FALSIFICATION           │
├───────────────────────────┬──────────────────────────────────────────┤
│ ORIGINAL HYPOTHESIS       │ DIAGNOSTIC                               │
│                           │                                          │
│ Buyback                   │ Published S3                 2.79         │
│ → management conviction   │ Pure buyback LONG           -0.24         │
│ → long repurchasers       │ Remove buyback component     2.79         │
│                           │ Remove buyback entirely      2.84         │
│                           │ Correct sign variants         < 0 full     │
│ DATA ISSUE                │                                          │
│ genuine cash outflow      │ S1 ↔ S3 correlation          0.898        │
│ is mostly NEGATIVE        │                                          │
│ published filter >= 0     │                                          │
├───────────────────────────┴──────────────────────────────────────────┤
│ Full 2.79 | Train 2.92 → Test 2.40 | MDD -6.3% | Fees 17.8% / 5y   │
│ VERDICT: REJECT BUYBACK STORY — performance = shared factor skeleton │
└──────────────────────────────────────────────────────────────────────┘
```

## Visual design rule

Make this slide visually different from S1/S2:

- Left = hypothesis card.
- Center = large red/crossed arrow from “Buyback hypothesis” to “Rejected”.
- Right = four diagnostic numbers.
- Bottom-right = big **0.898 correlation** callout.

The purpose is to signal scientific falsification, not embarrassment.

## Speaking order

**3:05–3:25 — Q1 + Q2**

- Original idea: repurchases may signal management conviction.
- Published code gates on the buyback cash-flow field and combines it with the same factor skeleton as S1.

**3:25–3:55 — Q4 diagnostic**

- Genuine repurchase cash outflows are predominantly negative-signed.
- Published filter uses `bought >= 0`.
- Pure buyback is negative Sharpe.
- Removing buyback does not hurt; removing it entirely actually raises Sharpe to ~2.84.
- Correcting sign does not create robust alpha.

**3:55–4:10 — correlation weakness**

- S1/S3 daily-return correlation ≈ 0.90.
- Therefore they are not independent equity alphas.

**4:10–4:20 — Q3 metrics**

- The backtest itself still retains test Sharpe 2.40.
- Stable backtest does not validate the original economic explanation.

## Exact takeaway

> **S3 is our most important negative research result: the performance is real in the backtest, but the buyback explanation does not survive falsification.**

## Do not say

- “S3 proves a Vietnamese buyback anomaly.”
- “S1 and S3 diversify because issuance and buyback are opposite.”

---

# SLIDE 5 — RESULTS THAT SURVIVE OUT OF SAMPLE, BUT COST AND CORRELATION MATTER

**Time: 4:20–5:20**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ CROSS-STRATEGY ROBUSTNESS                                            │
├──────────────────────────────────────────────────────────────────────┤
│                 S1                 S2                 S3             │
│ Full Sharpe      2.80               2.84               2.79          │
│ Train            3.00               3.09               2.92          │
│ Test             2.54               2.39               2.40          │
│ MDD             -6.4%              -7.1%              -6.3%          │
│ PF               1.65               2.07               1.62          │
│ 5y Fees          19.7%              39.8%              17.8%         │
├──────────────────────────────────────────────────────────────────────┤
│ OOS RETENTION:     0.85               0.77               0.82        │
│                                              S1 ↔ S3 corr = 0.898    │
└──────────────────────────────────────────────────────────────────────┘
```

## Best visual

Use three dumbbell charts for Train → Test Sharpe, one per strategy, plus a narrow cost bar underneath.

Avoid equity curves unless they are clean, directly exported from XNOQuant, and readable at presentation distance.

## Speaking goal

One minute only:

- All three retain substantial positive Test Sharpe; none collapses OOS.
- S2 pays the highest implementation cost.
- S1 has the best OOS retention among the three.
- S1/S3 correlation is the main portfolio weakness.
- Therefore headline Sharpe alone is not enough to rank research quality.

## Rule coverage

- Main performance metrics
- Evaluation stages
- Performance relative to cost
- Weakness / robustness

---

# SLIDE 6 — THE RESEARCH PROCESS: REFINE, KEEP, REJECT

**Time: 5:20–6:20**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ HOW WE RESEARCHED THE STRATEGIES                                     │
├──────────────────┬──────────────────┬────────────────────────────────┤
│ S1 — REFINE      │ S2 — KEEP        │ S3 — REJECT STORY             │
│                  │                  │                                │
│ Idea             │ Idea             │ Idea                           │
│ ↓                │ ↓                │ ↓                              │
│ Pure signal test │ Raw momentum     │ Sign / coverage probe          │
│ ↓                │ ↓                │ ↓                              │
│ Factor ablation  │ Component add    │ Remove component               │
│ ↓                │ ↓                │ ↓                              │
│ Gate sensitivity │ Threshold ±25%   │ Correct sign                   │
│ ↓                │ ↓                │ ↓                              │
│ REFINE CLAIM     │ KEEP STORY       │ REJECT CLAIM                   │
└──────────────────┴──────────────────┴────────────────────────────────┘
```

## Speaking goal

This slide is the answer to “research process”, not a repetition of results.

Say:

- We started from an intuition.
- We isolated the core signal.
- We removed components.
- We checked signs/coverage.
- We changed thresholds where appropriate.
- We accepted different conclusions instead of forcing every strategy into a positive narrative.

One sentence per strategy:

- **S1:** economic direction partly survives, attribution changes.
- **S2:** hypothesis survives component and threshold tests.
- **S3:** hypothesis fails data/sign/ablation checks.

This is the slide most likely to differentiate the team in Q&A.

---

# SLIDE 7 — WHAT WE WOULD IMPROVE NEXT

**Time: 6:20–7:00**

## Layout

```text
┌──────────────────────────────────────────────────────────────────────┐
│ NEXT VERSION: IMPLEMENTATION BEFORE MORE FACTORS                     │
├───────────────────────┬───────────────────────┬──────────────────────┤
│ S1                    │ S2                    │ S3                   │
│                       │                       │                      │
│ • issuance as filter  │ • 1-bar delay test   │ • replace buyback    │
│ • correct sign        │ • extra slippage     │ • distinct mechanism │
│ • sector neutral      │ • reduce entries     │ • lower correlation  │
│ • capacity test       │ • capacity estimate  │ • capacity test      │
├──────────────────────────────────────────────────────────────────────┤
│ MEASURED: platform fees, train/test, ablations, threshold robustness │
│ NOT YET MEASURED: max capacity, explicit execution delay, doubled TC │
├──────────────────────────────────────────────────────────────────────┤
│ FINAL: We prefer a falsified story to an unsupported story.          │
└──────────────────────────────────────────────────────────────────────┘
```

## Speaking order

**6:20–6:45 — Q5**

- S1: align issuance use with evidence and test sector/liquidity capacity.
- S2: implementation robustness — delay, slippage, entry reduction.
- S3: replace the unsupported buyback conditioning with a truly distinct source of alpha.

**6:45–7:00 — close**

Use one closing sentence:

> **The main result is not three high Sharpe numbers; it is knowing which parts of those numbers we can actually defend.**

Then stop. Do not use the remaining seconds to add caveats.

---

# Q1–Q5 COVERAGE MAP

Use this during rehearsal to verify nothing required is missing.

| Requirement | Where covered |
|---|---|
| Q1 — intuition/origin | Slides 2, 3, 4 |
| Q2 — formula/operators/entry-exit/weights | Slides 2, 3, 4 |
| Q3 — performance by evaluation stage | Slides 2, 3, 4 + Slide 5 |
| Q4 — strengths/weaknesses/robustness | Slides 2, 3, 4 + Slide 5 + Slide 6 |
| Q5 — improvements/cost/capacity | Slide 7 |
| Main metrics | Slides 2–5 |
| Train/Test | Slides 2–5 |
| Cost | Slides 2–5 |
| Research process | Slide 6 |

---

# DATA THAT MUST BE VISIBLE SOMEWHERE

Minimum numbers to put on the deck:

```text
S1: Full 2.80 | Train 3.00 | Test 2.54 | MDD -6.4 | Fees 19.7
S2: Full 2.84 | Train 3.09 | Test 2.39 | MDD -7.1 | PF 2.07 | Fees 39.8
S3: Full 2.79 | Train 2.92 | Test 2.40 | MDD -6.3 | Fees 17.8
S1-S3 correlation: 0.898
```

Ablation numbers that matter:

```text
S1: issuance long -0.90 | issuance short +0.64 | no issuance 2.84 | flip sign 2.91 | gate-only 2.94
S2: raw 2.60 | +volume 2.87 | +VN30 2.81 | original 2.84 | 0.75× 2.86 | 1.25× 2.74
S3: pure buyback -0.24 | remove component 2.79 | remove buyback 2.84
```

Everything else belongs in backup/Q&A slides, not the 7-minute main deck.

---

# BACKUP SLIDES FOR 5-MIN JUDGE Q&A

Prepare these after the 7-slide main deck:

1. **S1 factor decomposition** — volatility, traded value, EY, ROA, combinations.
2. **S1 gate sensitivity** — 0–1, 0.3–1, 0.3–0.9, 0.5–1, 0.7–1.
3. **S2 exact thresholds and execution windows.**
4. **S2 threshold perturbation details.**
5. **S3 buyback sign/coverage diagnostic.**
6. **S1 vs S3 correlation evidence.**
7. **Full metric table / platform screenshots.**
8. **Research limitations** — capacity, explicit delay, additional transaction-cost stress not yet measured.

Do not consume main-pitch time with these details unless a judge asks.

---

# FINAL DESIGN RULES

- 16:9 widescreen.
- One idea per slide.
- Maximum 5–6 visual elements per slide.
- Metrics in large numerals; explanatory prose kept to one-line claims.
- Use the same top result ribbon on Slides 2–4 for visual consistency.
- Use consistent verdict labels: **REFINE / KEEP / REJECT STORY**.
- Never put source code blocks on the main deck; use signal-flow diagrams.
- Every number must match XNOQuant or the diagnostic files.
- Keep detailed methodology and raw diagnostics in backup slides.
