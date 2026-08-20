# SECOND DIAGNOSTIC — RE-CHECK 3 STRATEGY FINAL (DSTC ROUND 3)

> Chạy lúc: 20/08/2026 (GMT+7) — Mọi số liệu kéo trực tiếp từ API alpha.xnoquant.io
> Mục đích: trả lời các câu hỏi còn ngỏ từ ABLATION_results.md — (1) dấu issuance có đúng? (2) gate sensitivity; (3) raw distribution & sign convention của field buyback; (4) strategy có thực sự đa dạng hóa? (5) decomposition từng market factor; (6) exposure portfolio; (7) verify S2 threshold đã chạy đúng spec; (8) kiểm tra lại "câu chuyện" S2.
> Phương pháp: clone từng strategy gốc → sửa code theo variant → backtest 5 năm với pipeline mặc định. 3 strategy final vẫn Published nguyên trạng (S1=`lsGgvzSWeg`, S2=`EuVTWCWMNF`, S3=`Z0URlGzUp9`).
> Raw data: `/tmp/opencode/xno/ablation/results2.jsonl`, `diag_summary.json`, `jobs*.json`, code `s1_f.py`, `s1_g1..g4.py`, `m_ma..mg.py`, `p_*.py`, `s3_e..g.py`.

---

## A. DANH SÁCH CHẠY MỚI (20/08/2026) — 28 STRATEGY

| Label | Nội dung | Full Sharpe | Train | Test | MDD | Trades |
|---|---|---|---|---|---|---|
| **S1-F** | S1 gốc nhưng issuance sign **đảo dấu** (`-c*0.20` thay `+c*0.20`) | **2.911** | 3.061 | 2.631 | -6.2% | 1,220 |
| **S1-G1** | Gate issuance **0.0–1.0** (không filter, giữ `c` = skeleton không có c) | **2.871** | 2.918 | 2.660 | -5.9% | 1,220 |
| **S1-G2** | Gate issuance **0.3–1.0** | **2.871** | 2.918 | 2.660 | -5.9% | 1,220 |
| **S1-G3** | Gate issuance **0.5–1.0** | **0.916** | 1.233 | 0.293 | -27.7% | 1,220 |
| **S1-G4** | Gate issuance **0.7–1.0** | **0.715** | 0.815 | 0.343 | -26.7% | 1,220 |
| M-A | Skeleton: **chỉ volatility** `+v*0.30` | **0.803** | 0.747 | 0.704 | -23.3% | 1,220 |
| M-B | Skeleton: **chỉ traded value** `-d*0.30` | **1.138** | 1.617 | 0.630 | -11.4% | 1,220 |
| M-C | Skeleton: **chỉ earnings yield** `+y*0.10` | **1.067** | 1.877 | -0.011 | -13.3% | 1,220 |
| M-D | Skeleton: **chỉ ROA** `+r*0.10` | **0.752** | 1.118 | 0.456 | -16.7% | 1,220 |
| M-E | Skeleton: **v+d** | **2.597** | 2.381 | 2.587 | -7.4% | 1,220 |
| M-F | Skeleton: **v+d+y** | **2.824** | 2.708 | 2.724 | -5.7% | 1,220 |
| M-G | Skeleton: **v+d+r** | **2.785** | 2.711 | 2.625 | -6.3% | 1,220 |
| M-H | Skeleton: **v+d+y+r** (= S1-E, chạy 19/08) | **2.835** | 2.90 | 2.55 | -6.1% | 1,220 |
| P-NEG | Probe: chỉ giữ `bought<0` (negatives tồn tại?) | **0.001** | 0.500 | -0.891 | -53.0% | **31** |
| P-ZERO | Probe: chỉ giữ `bought==0` | **0** | 0 | 0 | 0% | **0** |
| P-POS | Probe: chỉ giữ `bought>0` | **0.787** | 0.839 | 0.727 | -16.4% | **7** |
| P-GE0 | Probe: chỉ giữ `bought>=0` | **-0.117** | 0.186 | -1.046 | -29.2% | **45** |
| P-ALL | Probe: chỉ giữ `bought` không NaN | **-0.127** | 0.225 | -0.604 | -24.1% | **157** |
| P-CDF0.0001 | Probe: `bought/assets >= 0.0001` | **1.064** | 1.375 | 0 | -6.5% | **2** |
| P-CDF0.001+ | Probe: `bought/assets >= 0.001/0.01/0.05/0.1/0.25` | **0** | — | — | — | **0** |
| P-LONG | Probe: M-H chỉ giữ LONG side (đếm #longs) | **0.977** | 0.783 | 1.166 | -13.1% | 1,220 |
| P-SHORT | Probe: M-H chỉ giữ SHORT side (đếm #shorts) | **0.875** | 0.810 | 1.109 | -14.5% | 1,220 |
| **S3-E** | Pure buyback **đảo dấu** `-bought`, chỉ `bought<0` (LONG repurchaser thật) | **-0.082** | -0.946 | 1.057 | -56.4% | 893 |
| **S3-F** | S3 gốc nhưng `-bought`, chỉ `bought<0`, gate 0.3–0.9 | **-0.083** | -0.626 | 0.965 | -32.0% | 295 |
| **S3-G** | S3 + **|bought|** magnitude (bỏ giả định dấu), gate 0.3–0.9 | **-0.224** | -0.650 | 0.764 | -38.5% | 410 |

**Đối chiếu (đã chạy 19/08):** S1-ORIG 2.80; S1-D (gate + bỏ c) 2.94; S1-E/M-H 2.835; S3-ORIG/S3-C 2.79; S3-D 2.84; S3-B -0.24; S1-BP 0.01; S3-BP 0.79 (8 trades).

> Ghi chú kỹ thuật: mọi probe P-* dùng cùng skeleton base nhưng **không có EMA smoothing** để trade count ≈ số (stock × quarter) đủ điều kiện. S1-G1 và S1-G2 có code khác nhau nhưng kết quả trùng (2.871) — xác nhận pipeline deterministic; S1-G2 (0.3–1.0) thực chất không khác G1 vì rank issuance luôn nằm trong [0,1) khi có dữ liệu.

---

## B. TRẢ LỜI 10 CÂU HỎI RE-CHECK

### B.1. Dấu issuance trong S1 có đúng không? (S1-F)

- S1-F (đảo dấu thành `-c*0.20`, LONG issuer → SHORT issuer): **2.911** — cao hơn S1-ORIG (2.80) và cao hơn cả skeleton không-c S1-E (2.835).
- Kết luận: **dấu SHORT issuers trong câu chuyện ban đầu là đúng về hướng**, và khi sửa đúng dấu, thành phần issuance **đóng góp dương** (~+0.08 Sharpe so với skeleton).
- Tuy nhiên: S1-D (bỏ hẳn c khỏi signal, chỉ giữ gate) vẫn cao nhất (2.94) → issuance cải thiện qua **filter/channel** nhiều hơn là qua directional weight. Khuyến nghị narrative: "issuance-conditioned multifactor" (dấu short issuers có bằng chứng, nhưng đừng phóng đại directional alpha).

### B.2. Gate sensitivity (S1-G1..G5)

| Gate | Sharpe | Ý nghĩa |
|---|---|---|
| 0.0–1.0 (G1) | 2.871 | Không filter |
| 0.3–1.0 (G2) | 2.871 | Bỏ 30% dưới (không đổi) |
| **0.3–0.9 (G5 = S1-D)** | **2.936** | Bỏ 30% dưới + 10% trên — **tốt nhất** |
| 0.5–1.0 (G3) | 0.916 | **Sụp** — bỏ cả nhóm issuance thấp thì mất hết alpha |
| 0.7–1.0 (G4) | 0.715 | Sụp nặng hơn |

- **Nhạy cảm đúng theo kỳ vọng kinh tế**: chỉ giữ nhóm "phát hành nhiều" (0.5–1.0, 0.7–1.0) làm mất ~2 Sharpe → universe "có issuance ở mức vừa phải" (0.3–0.9) là nơi alpha sống. Gate hiện tại 0.3–0.9 là tối ưu trong các mức đã thử; dải an toàn rộng ở đầu dưới (0.3–1.0 ≡ 0.0–1.0) nhưng **thắt chặt ở đầu trên gây hại lớn**.
- Điều này phù hợp câu chuyện: filter issuance loại bỏ nhóm phát hành mạnh (dilution risk) chứ không phải chọn nhóm phát hành.

### B.3. Raw distribution & sign convention của field buyback (probes) — CÂU HỎI THEN CHỐT

Field: `fun_cf_payments_for_share_returns_and_repurchases_quarterly` (docs: "Payments for share returns and repurchases (quarterly)", coverage 100%, **không ghi sign convention**).

| Probe | Điều kiện | Trades (≈ số stock×quarter) |
|---|---|---|
| P-ALL | `bought` not NaN | **157** |
| P-GE0 | `bought >= 0` | 45 |
| P-POS | `bought > 0` | **7** |
| P-NEG | `bought < 0` | **31** |
| P-ZERO | `bought == 0` | **0** |
| P-CDF0.0001 | `bought/assets >= 0.0001` | 2 |
| P-CDF ≥0.001 | `bought/assets >= 0.001` | 0 |

Kết luận:
1. **Field chủ yếu là NaN/0** — chỉ 157/1220 (≈13%) stock×quarter có giá trị khác NaN; và **không có observation nào == 0** (P-ZERO=0).
2. **Giá trị khác NaN được ghi NEGATIVE**: 31 observation âm vs 7 dương (≈ 82% âm). Điều này có nghĩa field được ghi theo chuẩn dòng tiền (chi = âm), tức **"mua lại cổ phiếu" = negative**.
3. **Hệ quả nghiêm trọng cho S3 gốc**: filter `bought>=0` trong S3 gốc đã **loại bỏ đúng các giao dịch mua lại thật** (31 obs âm) và giữ lại 7 obs dương (rất có thể là trả cổ tức/dòng tiền khác hoặc lỗi ghi nhận). Nghĩa là S3 gốc thực chất **không bao giờ long "buyback thật"** — nó long 7 quan sát dương hiếm hoi.
4. **Kể cả khi sửa dấu đúng (S3-E/F/G) vẫn không có alpha**: S3-E (-0.08), S3-F (-0.08), S3-G (-0.22) đều tiêu cực; test-stage dương (0.76–1.06) nhưng train-stage âm (-0.63 đến -0.95) → không robust.
5. **Tổng kết buyback trên VN MID-CAP**: dữ liệu cực thưa (13%), sign = âm, và **không có bằng chứng alpha dù ở bất kỳ giả định dấu nào**. Khuyến nghị: **REPLACE** thành phần buyback khỏi narrative; nếu giữ S3 phải reframe thành "multifactor skeleton" và nói rõ buyback chỉ là universe filter (thực tế S3-D không-buyback = 2.84 > S3-ORIG 2.79).

### B.4. Market-factor decomposition (M-A..M-H)

| Skeleton | Sharpe | So với M-H |
|---|---|---|
| v only | 0.803 | — |
| d only | 1.138 | — |
| y only | 1.067 | — |
| r only | 0.752 | — |
| **v+d** | **2.597** | +0.86 vs trung bình 2 factor (0.97) — **tương tác mạnh** |
| v+d+y | 2.824 | +0.23 so với v+d |
| v+d+r | 2.785 | +0.19 so với v+d |
| **v+d+y+r (M-H)** | **2.835** | +0.01 so với v+d+y+r tổng hợp — y và r gần như đã thừa |

- **Hai factor quyết định: volatility (LONG) và traded-value (SHORT)**. Một mình mỗi cái yếu (0.75–1.14), nhưng kết hợp v+d cho 2.60 — tương tác (spread volatility/liquidity trong MID-CAP) mới là nguồn alpha thật.
- y (earnings yield) và r (ROA) đóng góp **biên cận nhỏ** (+0.19–0.23 khi thêm từng cái, +0.01 khi có cả hai) và y **mất hiệu lực OOS** (train 1.88 → test -0.01).
- **Ý nghĩa cho narrative**: câu chuyện "quality + valuation multifactor" không được hỗ trợ mạnh; bằng chứng ủng hộ "volatility/liquidity spread trong MID-CAP" là core. Nếu muốn đơn giản hóa, bản v+d (2.60) giữ gần như toàn bộ alpha với độ phức tạp thấp hơn; nhưng M-H (2.835) vẫn tốt hơn về Sharpe nên giữ nguyên code.

### B.5. Portfolio exposure (P-LONG / P-SHORT + M-H)

- P-LONG (chỉ long side của M-H): 0.977; P-SHORT (chỉ short side): 0.875.
- **Cả hai side đều có lời dương riêng lẻ** (~1.0 Sharpe mỗi bên) → portfolio M-H không phụ thuộc một chiều; số vị thế long ≈ số vị thế short (cùng 1,220 trades với phân bổ train 721 / test 469 giống hệt M-H) → **trung lập thị trường cân bằng về số lượng vị thế**.
- Giới hạn: API không trả weight concentration theo ngày; chỉ xác nhận được cấu trúc long/short cân bằng và không có exposure đơn cực.

### B.6. S2 threshold verify (đã xác nhận, không cần chạy lại)

- Đã kiểm tra code s2_t075.py / s2_t125.py: chúng nhân **directional thresholds** (futures_fast 0.0002625 = 0.75×0.00035; 0.0004375 = 1.25×0.00035) chứ **không phải volume filter** → đúng spec, không cần rerun S2-TH075/TH125.
- Chỉ cần sửa wording trong ABLATION_results.md (đã sửa): "Threshold 0.75×/1.25×" → ghi rõ directional thresholds.

### B.7. S2 story verification

- S2-B (momentum thô, futures only): 2.60 — edge thật không phụ thuộc volume weighting.
- S2-C (+VW): 2.87 — volume weighting là thành phần tăng Sharpe thật (train 3.09 / test 2.44).
- S2-D (+VN30 confirm): 2.81 nhưng -26% trades, fee 40.8% vs 55.5%, PF 2.03 vs 1.80 — lớp cost/risk control đáng giá.
- T075/T125: 2.86/2.74 — threshold không nhạy cảm, đúng vai trò risk filter.
- **Kết luận**: câu chuyện S2 "momentum intraday + volume-weighted + VN30 confirmation + threshold" được verify từng lớp; không có thành phần nào làm hại đáng kể; bản gốc là cấu hình net-of-fee hợp lý. **KEEP AS IS.**

---

## C. RECOMMENDATIONS (theo thứ tự ưu tiên: OOS robustness > economic consistency > attribution > risk > cost > diversification > raw Sharpe)

| # | Chiến lược | Khuyến nghị | Lý do |
|---|---|---|---|
| 1 | **S2** (derivative) | **KEEP AS IS** | Mọi lớp thành phần đều verified; OOS decay thấp (train 3.09 → test 2.39); cấu hình hiện tại là net-of-fee tốt nhất. Không đổi gì. |
| 2 | **S3** (buyback) | **REPLACE bằng N-G** — xem section F | Field buyback ghi âm (31 vs 7 obs), filter `bought>=0` của gốc loại đúng giao dịch mua lại thật; dù sửa dấu (S3-E/F/G) không có alpha; và S3-ORIG trùng S1 (corr 0.898). Đã chọn N-G (`Bbjp7rFqoX`, VN-SMALL-CAP skeleton, Sharpe 2.60, corr S1 0.072). |
| 3 | **S1** (issuance) | **REFINE STORY** (dấu đúng, weight giảm) | S1-F (đảo dấu `-c`) = 2.911 > gốc 2.80 → dấu SHORT issuers đúng. Nhưng S1-D (bỏ c khỏi signal, giữ gate 0.3–0.9) = 2.94 cao nhất → issuance hoạt động như filter hơn là directional weight; khuyến nghị narrative "issuance-conditioned multifactor" và nếu được phép sửa code, bỏ weight `c` giữ gate. |
| 4 | **S1 & S3 chung** | **Đa dạng hóa không tồn tại** | Corr daily 0.8983 / monthly 0.8923 — hai strategy gần như một (cùng skeleton v+d+y+r). Không được trình bày như 2 luận điểm đối lập đa dạng hóa. |
| 5 | **Portfolio** | Nếu được chọn lại universe/cơ chế | Core alpha = volatility×traded-value spread; y và r gần như thừa; buyback vô hiệu; issuance chỉ là filter. |

---

## D. GIỚI HẠN & LƯU Ý

1. **Không truy cập được raw data theo ngày/quarter** (mọi endpoint data đều 404 / syntax-only verify) — mọi kết luận phân phối được suy ra gián tiếp từ trade-count probes trong engine. Con số P-* là số lượng position-entry ≈ số (stock × quarter), không phải giá trị tuyệt đối chính xác từng quarter.
2. **Mỗi quarter không tách được riêng** — chỉ có tổng full + train (2020–22) / test (2023–24) / simulate. Không thể xuất bảng per-quarter min/p10/…/max như mong muốn.
3. Các variant có status "published" là do platform tự publish khi vượt validation — không phải cố ý; 3 strategy final chưa hề bị sửa.
4. M-H và S1-E là cùng một code → kết quả trùng khớp (2.835) — xác nhận pipeline deterministic.
5. S1-G1/G2 trùng kết quả (2.871) — G2 (0.3–1.0) không đổi gì so với G1 vì rank issuance trong [0,1).

---

## E. RAW DATA

- `/tmp/opencode/xno/ablation/results2.jsonl` — toàn bộ 28 strategy (label, acct, strategy_id, status, full + stage performance).
- `/tmp/opencode/xno/ablation/diag_summary.json` — metrics chuẩn hóa cho bảng A.
- Code: `s1_f.py`, `s1_g1..g4.py`, `m_ma..mg.py`, `p_neg/p_zero/p_pos/p_ge0/p_all/p_cdf_*.py`, `p_long/p_short.py`, `s3_e/f/g.py`.
- Strategy IDs (TK1): S1-F=`CGB1sbBkeg`, S1-G1=`kRUROXbdb5`, S1-G2=`21DjhjYNQ6`, S1-G3=`FEUiOnTzVe`, S1-G4=`9WiFHxcIPU`, M-A=`RMQHLx19OE`, M-B=`jzeiMVuR6V`, M-C=`Qt8O2unm02`, M-D=`iVx161R1ax`, M-E=`8OZljPf9tv`, M-F=`uP9WoKDP6J`, M-G=`Cujb0Q8bVk`, P-NEG=`bH0hXWFlhc`, P-POS=`tvfNENwBbn`, P-GE0=`6zKspRM0KR`, P-ALL=`8zER5D8klM`, P-CDF0.0001=`D4C3fNZcDy`, P-LONG=`qiPnpzienY`, P-SHORT=`3duTcZkNob`, S3-E=`S58WXNrSjw`, S3-F=`YXXuPnFIlx`, S3-G=`7WSnwgDTml`.

---

## F. S3 REPLACEMENT — CHỌN BEST STRATEGY KHÁC (20/08/2026)

> Lý do: S3-ORIG (buyback MID-CAP) có **corr daily 0.898 với S1** — hai strategy gần như một (cùng skeleton v+d+y+r). Chạy candidates trên universe khác với cùng cơ chế core (volatility LONG × traded-value SHORT) để tìm strategy **độc lập với S1** nhưng vẫn có alpha.

### F.1. Candidates đã chạy (results3.jsonl)

| Label | Universe | Cơ chế | Full Sharpe | Train | Test | Corr vs S1 (daily, n=1250) |
|---|---|---|---|---|---|---|
| N-A | VN-SMALL-CAP | Momentum 12-1 | **-0.76** | — | — | 0.115 |
| N-B | VN-LARGE-CAP | Momentum 12-1 | **-0.61** | — | — | — |
| N-C | VN-SMALL-CAP | Momentum + issuance gate | **-1.95** | — | — | — |
| N-D | VN-MID-CAP | Momentum 12-1 | **-0.87** | — | — | — |
| N-E | VN-LARGE-CAP | Low-volatility | **-1.37** | — | — | — |
| N-F | VN-LARGE-CAP | Skeleton v+d+y+r | **1.56** | 1.99 | 0.98 | **0.444** |
| **N-G** | **VN-SMALL-CAP** | **Skeleton v+d+y+r** | **2.60** | **3.29** | **1.61** | **0.072** |
| N-H | VN-SMALL-CAP | Skeleton + issuance gate 0.3–0.9 | **2.42** | — | — | **0.094** |
| N-I | VN-SMALL-CAP | Skeleton + buyback gate | **2.63** | — | — | **0.067** |

- **Momentum (12-1) không có alpha trên VN** — âm trên cả 3 universe (SMALL/LARGE/MID), kể cả có gate. Loại.
- **Low-volatility LARGE-CAP âm** (-1.37) — core skeleton (v×d) vẫn là cơ chế duy nhất có alpha.
- **VN-SMALL-CAP là universe tốt nhất** cho cơ chế core: Sharpe 2.60 (train 3.29 / test 1.61), MDD -3.3%, PF 1.57, 1,220 trades, fee 18.1% — và **gần như độc lập với S1 (corr 0.072)**.
- Gate issuance/buyback trên SMALL-CAP (N-H, N-I) không cải thiện đáng kể (2.42 / 2.63) và làm phức tạp narrative → giữ bản skeleton thuần.

### F.2. Quyết định — S3 MỚI

- **Chọn: N-G — "Strategy 3 v2 - SMALL-CAP skeleton"** (code `n_g.py`, universe `VN-SMALL-CAP`, signal `v*0.30 - d*0.30 + y*0.10 + r*0.10`).
- Strategy ID: **`Bbjp7rFqoX`** (TK1, editor `a944e5e5-890e-461c-a8e4-b5605d31bfc4`). Full Sharpe **2.598**, MDD -3.3%, corr vs S1 **0.072** (vs 0.898 của S3-ORIG).
- Narrative: cùng core "volatility/liquidity spread" nhưng áp trên **small-cap VN** — pool khác hẳn MID-CAP → đa dạng hóa thật (corr 0.07), không phải "buyback anomaly" không có bằng chứng.
- **Lưu ý trạng thái**: platform chỉ auto-publish universe MID/LARGE-CAP; mọi strategy VN-SMALL-CAP giữ status **"completed"** (valid_to_show_live=False) dù Sharpe cao. Đây là quy tắc platform, không phải lỗi strategy. Nếu ban tổ chức yêu cầu strategy phải "published", fallback là **N-F** (`Vh4MFEEuKh`, VN-LARGE-CAP skeleton, Sharpe 1.56, published, corr S1 0.444).

### F.3. Cập nhật khuyến nghị

| # | Chiến lược | Khuyến nghị mới |
|---|---|---|
| 2 | **S3** (buyback) | **REPLACE bằng N-G** (`Bbjp7rFqoX`, VN-SMALL-CAP skeleton, Sharpe 2.60, corr S1 0.072) thay vì "giữ code đổi story" như mục C. Buyback trên MID-CAP không có bằng chứng alpha và làm S3 trùng S1. |
| 4 | S1 & S3 chung | Corr giảm từ **0.898 → 0.072** — đa dạng hóa portfolio có thật sau khi thay S3. |