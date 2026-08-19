# ABLATION DIAGNOSTIC — KẾT QUẢ & PHÂN TÍCH (3 STRATEGY FINAL)

> Chạy lúc: 19/08/2026 (GMT+7) — Mọi số liệu kéo trực tiếp từ API alpha.xnoquant.io
> Mục đích: **diagnostic, không optimize** — xác định nguồn alpha thực sự của từng chiến lược, kiểm chứng dấu hypothesis, vai trò directional-alpha vs filter, robustness OOS, và mức diversification giữa Strategy 1 và Strategy 3.
> Phương pháp: clone từng strategy gốc → sửa code theo từng variant (như spec) → chạy backtest đầy đủ 5 năm với pipeline/platform mặc định → so sánh. Không một strategy gốc nào bị sửa (3 strategy final vẫn Published nguyên trạng).

---

## 1. BẢNG SO SÁNH TỔNG HỢP

| Label | Variant (so với gốc) | Full Sharpe | Train Sharpe | Test Sharpe | MDD full | PF full | Trades (5y) | Fee (5y) |
|---|---|---|---|---|---|---|---|---|
| **S1-ORIG** | Strategy 1 (issuance + gate + market factors) | **2.80** | 3.00 | 2.54 | -6.4% | 1.65 | 1,220 | 19.7% |
| S1-B | PURE issuance LONG, full base, no gate | **-0.90** | -0.60 | -1.51 | -25.7% | 0.86 | 1,219 | 3.5% |
| S1-C | PURE issuance SHORT, full base, no gate | **0.64** | 0.30 | 1.10 | -13.4% | 1.11 | 1,219 | 4.1% |
| S1-D | Market factors + gate (0.3–0.9), **bỏ c khỏi signal** | **2.94** | 3.11 | 2.65 | -6.1% | 1.69 | 1,220 | 20.0% |
| S1-E | **Bỏ issuance hoàn toàn** (chỉ market factors) | **2.84** | 2.90 | 2.55 | -6.1% | 1.64 | 1,220 | 16.8% |
| S1-BP | STRICT issued>0, long-only (coverage probe) | **0.01** | 0.03 | -0.31 | -24.1% | 1.01 | 1,220 | 6.4% |
| | | | | | | | | |
| **S2-ORIG** | Strategy 2 (volume-weighted pressure + VN30 confirm) | **2.84** | 3.09 | 2.39 | -7.1% | 2.07 | 2,210 | 39.8% |
| S2-B | Momentum thô (futures chỉ, không VW, không confirm) | **2.60** | 2.86 | 2.11 | -7.6% | 1.76 | 3,000 | 54.0% |
| S2-C | + Volume weighting (bỏ VN30 confirm) | **2.87** | 3.09 | 2.44 | -8.9% | 1.80 | 3,084 | 55.5% |
| S2-D | + VN30 confirmation (giữ VW, bỏ threshold filter) | **2.81** | 3.05 | 2.38 | -7.1% | 2.03 | 2,268 | 40.8% |
| S2-T075 | Directional threshold 0.75× gốc (futures_fast 0.0002625, futures_slow 0.00009, spot_fast 0.0001875, spot_slow 0.00006) | **2.86** | 3.11 | 2.40 | -7.1% | 2.06 | 2,304 | 41.5% |
| S2-T125 | Directional threshold 1.25× gốc (futures_fast 0.0004375, futures_slow 0.00015, spot_fast 0.0003125, spot_slow 0.0001) | **2.74** | 3.00 | 2.25 | -7.4% | 2.04 | 2,140 | 38.5% |
| | | | | | | | | |
| **S3-ORIG** | Strategy 3 (buyback + gate + market factors) | **2.79** | 2.92 | 2.40 | -6.3% | 1.62 | 1,220 | 17.8% |
| S3-B | PURE buyback LONG, full base, no gate | **-0.24** | -0.25 | -0.49 | -24.9% | 0.97 | 1,212 | 3.5% |
| S3-C | Market factors + gate, **bỏ c khỏi signal** | **2.79** | 2.92 | 2.40 | -6.3% | 1.62 | 1,220 | 17.8% |
| S3-D | **Bỏ buyback hoàn toàn** (chỉ market factors) | **2.84** | 2.90 | 2.55 | -6.1% | 1.64 | 1,220 | 16.8% |
| S3-BP | STRICT bought>0, long-only (coverage probe) | **0.79** | 0.84 | 0.73 | -16.4% | 1.43 | **8** | 1.5% |

**Lưu ý đọc bảng:** S1-E và S3-D có code giống hệt nhau (đều chỉ giữ market factors skeleton) nên kết quả trùng khớp (2.835) — đây là cross-validation cho thấy pipeline/platform deterministic.

---

## 2. FACTUAL OBSERVATIONS (theo nhóm)

### 2.1. Strategy 1 (Equity MID-CAP — issuance-conditioned multifactor)

1. **Pure issuance tự nó không có alpha dương cho LONG** — S1-B là strategy thua lỗ (Sharpe -0.90, MDD -25.7%) khi chỉ long theo rank issuance.
2. **Dấu hypothesis được xác nhận nhưng yếu**: đảo dấu sang SHORT (S1-C) chuyển Sharpe -0.90 → +0.64 (train 0.30 / test 1.10). Tức issuance high → underperformance sau đó là có thật, nhưng tín hiệu thuần yếu và tốn kém để khai thác như directional alpha.
3. **Gần như toàn bộ alpha đến từ market factors skeleton** (`+v*0.30 - d*0.30 + y*0.10 + r*0.10`, tức LONG volatility, SHORT traded-value, LONG earnings-yield, LONG ROA): S1-E (không issuance) đạt 2.84 — tức ~100% Sharpe của bản gốc (2.80) vẫn còn khi bỏ issuance.
4. **Gate issuance (rank 0.3–0.9) vẫn đóng góp hiệu chỉnh nhỏ**: S1-D (có gate, bỏ weight c) = 2.94 > S1-E (không issuance gì) = 2.84. Việc hạn chế universe vào nhóm rank giữa đem lại ~0.1 Sharpe.
5. **Weight thành phần `c*.20` thực tế làm giảm nhẹ hiệu năng**: S1-D (2.94) > bản gốc (2.80). Cần kiểm tra xem ban giám khảo coi đây là overfit hay chỉ là tham số; về mặt diagnostic thì bỏ `c` khỏi signal cho kết quả cao hơn.
6. **Issuance data có giá trị thực**: S1-BP (chỉ giữ cổ phiếu `issued>0`) giữ 13–20 vị thế mở (từ ~58–59 cổ phiếu đủ điều kiện) — tức ~23–34% universe MID-CAP có phát hành thực sự tại các thời điểm; giai đoạn 2020–2022 nhiều hơn (20 cổ) so với 2023–2025 (13 cổ). Sharpe ~0 → bản thân dấu hiệu "có phát hành" không phân biệt được winner/loser; phải dùng rank chi tiết + market factors.

### 2.2. Strategy 2 (Derivative VN30F1M-30MIN — momentum)

1. **Momentum thô đã có hiệu quả**: S2-B đạt Sharpe full 2.60 (train 2.86 / test 2.11) chỉ với pressure futures — nền tảng edge thật (không phụ thuộc volume weighting).
2. **Volume weighting tăng Sharpe rõ rệt**: S2-C = +0.27 Sharpe full so với S2-B (2.87 vs 2.60) và cải thiện cả train lẫn test — cách tính weighted return bằng relative volume là thành phần có giá trị.
3. **VN30 confirmation giảm trade & tăng chất lượng nhưng Sharpe xấp xỉ**: S2-D vs S2-C: Sharpe 2.81 vs 2.87; nhưng trades 2,268 vs 3,084 (-26%), fee 40.8% vs 55.5%, PF 2.03 vs 1.80. Trade-off: ít tốn kém hơn, lệnh chất lượng hơn, nhưng đánh đổi chút Sharpe.
4. **Threshold filter robust**: đổi directional thresholds thành 0.75× và 1.25× (futures_fast 0.0002625 / 0.0004375 thay vì 0.00035) đều giữ Sharpe 2.74–2.86 (T075: 2.86, T125: 2.74) — bộ lọc threshold không phải nguồn alpha nhạy cảm, đúng vai trò risk filter.
5. **Điểm mấu chốt**: toàn bộ alpha của S2 nằm trong cơ chế pressure + volume weighting; VN30 confirm và threshold chỉ là lớp kiểm soát chi phí/risk — cấu hình đang dùng (bản gốc) là hợp lý nhất về net-of-fee.

### 2.3. Strategy 3 (Equity MID-CAP — buyback-conditioned multifactor)

1. **Buyback đơn lẻ không có alpha**: S3-B LONG buyback thuần = thua lỗ (Sharpe -0.24, MDD -24.9%), PF 0.97.
2. **Thành phần `c` đóng góp ~0**: S3-C (bỏ hẳn `c` khỏi signal, code đã verify trên platform) cho kết quả **giống hệt bản gốc** (2.79 / 2.92 / 2.40) — nghĩa là mức rank buyback không ảnh hưởng portfolio.
3. **Nguyên nhân gốc — coverage diagnostic (S3-B vs S3-BP vs S3-D):**
   - S3-D (không cần buyback): 58–59 cổ phiếu đủ điều kiện ở cuối mỗi stage.
   - S3-B (cần `bought>=0`, dữ liệu tồn tại): 55–56 cổ phiếu → **dữ liệu buyback phủ ~95% universe**.
   - S3-BP (cần `bought>0` thực sự): **chỉ 8 trade trong cả 5 năm, 0 vị thế mở** → dòng tiền mua lại/trả cổ tức của hầu hết cổ phiếu VN MID-CAP trong kỳ 2020–2025 bằng 0.
   - Kết luận: biến buyback gần như hằng số 0 → rank cross-sectional của nó gần như vô nghĩa → component `c` không đóng góp alpha.
4. **Alpha thực tế của S3 hoàn toàn từ skeleton chung**: S3-C/ORIG (2.79) ≈ S1-E/S3-D (2.84) — cùng một bộ market factors (volatility, traded value, earnings yield, ROA).
5. **Vị thế của giao dịch mua lại thực sự có hiệu quả rất nhỏ lẻ**: S3-BP (chỉ 8 trade, Sharpe 0.79 trên mẫu cực nhỏ) — không đủ bằng chứng về buyback anomaly trên VN MID-CAP, chỉ đúng dấu LONG (+). (Kết luận về sign convention của field buyback và variant hiệu chỉnh dấu S3-E/F/G được trình bày chi tiết trong `SECOND_DIAGNOSTIC_RESULTS.md` — nhìn chung việc sửa dấu không tạo ra alpha.)

### 2.4. Correlation / Diversification (S1 vs S3)

| Cặp | Full (n=1,250) | Train (n=751) | Test (n=499) | Monthly (61 tháng) |
|---|---|---|---|---|
| S1 vs S3 (daily returns charts API) | **0.8983** | **0.8921** | **0.9198** | **0.8923** |

1. **Correlation rất cao (~0.90 ở mọi phân khúc)** — về mặt thuật toán hai strategy gần như là một: cùng pipeline, cùng gate, cùng skeleton market factors, khác nhau chỉ ở biến issuance/buyback (mà buyback ~0).
2. **Hệ quả**: Strategy 1 và Strategy 3 **không diversify nhau về mặt thực nghiệm**, dù luận điểm kinh doanh đối lập (issuance vs buyback). Điểm này cần xử lý kỹ trong phần trình bày ("giỏ hàng không trùng" không còn là lập luận mạnh).
3. Về mặt ban tổ chức (1 equity bắt buộc + 1 free), nếu được chọn lại, cặp equity nên đến từ skeleton khác thực sự (ví dụ khác universe hoặc khác cơ chế signal), không phải chỉ khác biến fundamental.

---

## 3. RAW RESULTS (đính kèm để kiểm tra lại)

- `/tmp/opencode/xno/ablation/results.jsonl` — toàn bộ dữ liệu thô từng variant (code, strategy_id, status, full performance, stage performance).
- `/tmp/opencode/xno/ablation/stages_fresh.json` — stage metrics (sharpe/mdd/pf/cagr) kéo fresh cho cả 14 variant.
- `/tmp/opencode/xno/ablation/coverage_open_positions.json` — open positions theo stage (dùng cho coverage diagnostic).
- `/tmp/opencode/xno/ablation/buyback_coverage_summary.json` — tóm tắt coverage (phương pháp + số liệu + kết luận).
- `/tmp/opencode/xno/ablation/s1_returns.json`, `s3_returns.json` — daily returns dùng tính correlation.
- Code từng variant: `/tmp/opencode/xno/ablation/s{1,2,3}_*.py` (đúng code đã chạy; S3-C đã verify trùng với code trên platform).

**Danh sách strategy id của variants (trên platform):**
| Variant | Strategy ID | Trạng thái |
|---|---|---|
| S1-B / S1-BP | `hl5QZNtnWT` / `pygUY0Kiyk` | completed |
| S1-C | `3dn0VN37bS` | completed |
| S1-D / S1-E | `aE1PTKmma9` / `mKThaJiyfw` | published (tự động) |
| S2-B / S2-C / S2-D / S2-T075 / S2-T125 | `wqfzhnsEHk` / `V62HGQM19m` / `gwzPhKRdYi` / `6mQHgQB6vE` / `tGlSLbRgMa` | published (tự động) |
| S3-B / S3-BP | `u99fvfzzJH` / `IxgvXGJsN5` | completed |
| S3-C / S3-D | `9XG2DnSIU3` / `3PXaU23rt4` | published (tự động) |

> Ghi chú: các variant status "published" được platform tự publish do vượt ngưỡng validation — **không phải do chúng tôi cố tình publish**, và không ảnh hưởng tới 3 strategy final (vẫn Published, chưa bị chỉnh sửa). Nếu cần giữ platform sạch, có thể delete các variant này khi không còn cần đối chiếu.

---

## 4. TÓM TẮT Ý NGHĨA (cho phần trình bày)

1. **S1 & S3 có cùng một nguồn alpha** (market factors skeleton + pipeline) — điểm yếu lớn về diversification; câu chuyện cần xoay quanh robustness và cost, không nên nhấn "2 luận điểm đối lập" làm trụ đa dạng hóa.
2. **Variable fundamental (issuance) đóng vai trò filter/hiệu chỉnh, không phải driver chính**; dấu short issuers đúng nhưng edge mỏng.
3. **Variable buyback gần như vô hiệu** do dữ liệu VN MID-CAP ~ toàn 0 — cần loại khỏi narrative "buyback anomaly VN".
4. **S2 là chiến lược có cơ chế alpha độc lập & thật nhất**: momentum pressure + volume weighting đều đóng góp dương; các lớp còn lại (VN30 confirm, threshold) là risk/cost control robust.
5. Khuyến nghị trình bày nên chuyển trọng tâm từ "3 luận điểm kinh doanh khác nhau" sang "3 cơ chế khác nhau về cấu trúc thị trường (equity cross-sectional vs futures intraday) với OOS decay thấp" — trung thực với kết quả ablation.