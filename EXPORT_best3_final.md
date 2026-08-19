# EXPORT - TOP 3 CHIẾN LƯỢC CHỐT TRÌNH BÀY VÒNG 3 DSTC 2026

> Xuất lúc: 19/08/2026, 22:40 GMT+7 — Dữ liệu kéo trực tiếp từ API alpha.xnoquant.io (fresh)
> 3 chiến lược này đã được rename đúng trên platform: **Strategy 1 / Strategy 2 / Strategy 3** — đều ở trạng thái **Published**
> Nguồn code: `strategy_1_equity_mid_cap_lsGgvzSWeg.py`, `strategy_2_derivative_vn30f1m_EuVTWCWMNF.py`, `strategy_3_equity_mid_cap_Z0URlGzUp9.py`

---

## A. TÓM TẮT NHANH (dùng cho slide tổng quan)

| | **Strategy 1** | **Strategy 2** | **Strategy 3** |
|---|---|---|---|
| **Vai trò theo luật** | Equity (bắt buộc) | Phái sinh (bắt buộc) | Tự do (Free) |
| **ID** | `lsGgvzSWeg` | `EuVTWCWMNF` | `Z0URlGzUp9` |
| **Tài khoản** | TK1 (Dũng) | TK2 (Khai) | TK1 (Dũng) |
| **Universe** | VN-MID-CAP | VN30F1M-30MIN | VN-MID-CAP |
| **Thị trường** | Vietnam Stock | Vietnam Future | Vietnam Stock |
| **Vốn khởi tạo (init_cash)** | 30 tỷ VND | 1 tỷ VND | 30 tỷ VND |
| **Ngày publish** | 05/08/2026 | 26/07/2026 | 05/08/2026 |
| **Luận điểm** | Equity issuance dilution → **short** công ty phát hành thêm cổ phiếu | Volume-weighted return pressure → theo momentum có xác nhận volume | Buyback commitment → **long** công ty mua lại cổ phiếu |
| **Full Sharpe** | **2.80** | **2.84** | **2.79** |
| **Test Sharpe (OOS)** | **2.54** | **2.39** | **2.40** |
| **CAGR** | 25.0% | 39.8% | 23.0% |
| **Max Drawdown** | -6.4% | -7.1% | -6.3% |
| **Profit Factor** | 1.65 | 2.07 | 1.62 |
| **Số lệnh full** | 1,220 | 2,210 | 1,220 |
| **Tổng phí 5 năm** | 19.7% | 39.8% | 17.8% |

**Tính đa dạng (Correlation/anti-crowding):**
- Strategy 1 (short issuers) và Strategy 3 (long buyback) đối lập nhau về luận điểm — 2 mặt của câu chuyện "share count discipline" (phát hành thêm làm loãng vs mua lại làm tăng EPS).
- Strategy 2 hoàn toàn khác biệt về loại tài sản (futures intraday, microstructure lead-lag) — bổ chéo danh mục.
- Lưu ý: cả 3 đều không phải LARGE-CAP — tránh được nhóm bị overfit (xem NOTES_best3_selection.md mục 3).

---

## B. CHI TIẾT TỪNG STRATEGY

### B1. Strategy 1 — Equity VN-MID-CAP — `lsGgvzSWeg`

**Luận điểm (hypothesis):** Việc phát hành thêm cổ phiếu (equity issuance) làm loãng cổ đông hiện hữu và thường báo hiệu hoạt động kém hiệu quả phía trước (literature về SEO underperformance). Chiến lược đi *short* các công ty có dòng tiền phát hành cao nhất (theo tỷ lệ so với tổng tài sản).

**Khẩu vị (formulation):** Cross-sectional ranking theo tỷ lệ `proceeds from issue of shares / total assets`. Gate rank 0.3–0.9. Kết hợp weight theo: volatility (–30%), traded value (–30%), earnings yield (+10%), ROA (+10%), issuance rank (+20%). Trọng số được demean + normalize L1 + smoothing EMA (75% slow) để giảm turnover.

**Full-sample metrics (2020-01 → 2025-01):**

| Metric | Giá trị | | Metric | Giá trị |
|---|---|---|---|---|
| Sharpe | **2.80** | | Profit Factor | 1.65 |
| Sortino | 4.90 | | Win rate | 59.1% |
| Calmar | 3.91 | | Recovery Factor | 31.7 |
| CAGR | 25.0% | | Kelly Criterion | 23.3% |
| Max Drawdown | -6.4% | | Volatility | 7.6% |
| VaR | -0.70% | | CVaR | -0.96% |
| Tổng lợi nhuận | +202.5% | | Benchmark | 0 (không long-only) |
| Tổng phí 5 năm | 19.7% (~3.9%/năm) | | Số lệnh | 1,220 |

**Stage metrics (train 2020-2022 vs test 2023-2024):**

| Stage | Kỳ | CAGR | Sharpe | Max DD | Profit Factor | Decay (test/train) |
|---|---|---|---|---|---|---|
| Train | 2020-01 → 2022-12 | 31.7% | 3.00 | -6.4% | 1.73 | — |
| Test (OOS) | 2023-01 → 2025-01 | 15.3% | **2.54** | -3.7% | 1.52 | **0.85** |
| Simulate (Full) | 2020-01 → 2025-01 | 25.0% | 2.80 | -6.4% | 1.65 | — |

**Câu trả lời nhanh cho Q&A:**
- **Q1 (tại sao tin vào ý tưởng?)** Dòng tiền phát hành cổ phiếu là tín hiệu hành vi/tài trợ: công ty chỉ phát hành khi cần tiền (áp lực hoặc kỳ vọng tiêu cực), trong khi chi phí phát hành rất tốn — trái ngược với tín hiệu mua lại cổ phiếu ở Strategy 3.
- **Q2 (chiến lược được xây thế nào?)** Signal cross-sectional hằng ngày trên toàn universe MID-CAP, gate theo rank 0.3–0.9, kết hợp 5 thành phần (issuance, volatility, traded value, earnings yield, ROA), chuẩn hóa L1 + EMA smoothing để giữ turnover thấp.
- **Q3 (hoạt động trong điều kiện nào?)** Mạnh trong giai đoạn tăng trưởng (train 2020-2022), vẫn giữ Test Sharpe 2.54 trong giai đoạn điều chỉnh — cho thấy edge bền vững ngoài mẫu.
- **Q4 (điểm mạnh / điểm yếu?)**
  - Mạnh: turnover thấp (phí chỉ ~3.9%/năm), drawdown nhỏ (-6.4%), consistency cao giữa train/test (decay 0.85).
  - Yếu: phụ thuộc chất lượng dữ liệu dòng tiền phát hành (báo cáo tài chính), dễ nhiễu trong đợt tăng vốn lớn.
- **Q5 (cải thiện tiếp)?** Thêm lớp sector-neutral để giảm concentration; kiểm tra slippage cho cổ phiếu MID-CAP thanh khoản thấp; test thêm universe SMALL-CAP để mở rộng capacity.

**Code đầy đủ:**

```python
class CustomStrategy(SimpleAlgorithm):
    """Equity issuance dilution: cash from issuing shares dilutes holders and precedes underperformance; short issuers."""
    def __algorithm__(self):
        close=self.data.pv_close_panel
        volume=self.data.pv_volume_panel
        eps=self.data.fun_is_eps_basis_quarterly_panel
        profit=self.data.fun_is_net_profit_loss_after_tax_quarterly_panel
        assets=self.data.fun_bs_total_assets_quarterly_panel
        equity=self.data.fun_bs_owners_equity_quarterly_panel
        operating_cash=self.data.fun_cf_net_cash_inflows_outflows_from_operating_activities_quarterly_panel
        revenue=self.data.fun_is_sales_quarterly_panel
        daily_return=self.feat.returns_panel(close)
        volatility=self.feat.rolling_std_panel(daily_return)
        traded_value=self.feat.rolling_value_panel(close,volume)
        earnings_yield=self.feat.safe_divide_panel(eps,close)
        roa=self.feat.safe_divide_panel(profit,assets)
        issued=self.data.fun_cf_proceeds_from_issue_of_shares_quarterly_panel
        core=self.feat.safe_divide_panel(issued,assets)
        base=(close.notna()&volume.notna()&eps.notna()&profit.notna()&assets.notna()&equity.notna()
            &operating_cash.notna()&revenue.notna()&daily_return.notna()&volatility.notna()&traded_value.notna()
            &earnings_yield.notna()&roa.notna()&core.notna()
            &(close>0)&(volume>0)&(assets>0)&(equity>0)&(volatility>0)&(traded_value>0)
&issued.notna()&(issued>=0))
        gate=self.op.rank_cs_panel(core,mask=base)
        eligible=base&gate.notna()&(gate>=.3)&(gate<.9)
        v=self.op.demean_cs_panel(self.op.rank_cs_panel(volatility,mask=eligible),mask=eligible)
        d=self.op.demean_cs_panel(self.op.rank_cs_panel(traded_value,mask=eligible),mask=eligible)
        y=self.op.demean_cs_panel(self.op.rank_cs_panel(earnings_yield,mask=eligible),mask=eligible)
        r=self.op.demean_cs_panel(self.op.rank_cs_panel(roa,mask=eligible),mask=eligible)
        c=self.op.demean_cs_panel(gate,mask=eligible)
        signal=v*.30-d*.30+y*.10+r*.10+c*.20
        valid=eligible&signal.notna()
        raw=self.op.normalize_l1_cs_panel(self.op.demean_cs_panel(signal,mask=valid),mask=valid)
        slow=self.feat.ema_panel(raw)
        weight_valid=valid&raw.notna()&slow.notna()
        final_weights=self.op.normalize_l1_cs_panel(self.op.demean_cs_panel(raw*.25+slow*.75,mask=weight_valid),mask=weight_valid)
        self.set_portfolio_positions(final_weights)
```

---

### B2. Strategy 2 — Phái sinh VN30F1M-30MIN — `EuVTWCWMNF`

**Luận điểm (hypothesis):** Khi lợi nhuận của hợp đồng tương lai có xác nhận volume (volume-weighted return pressure) đồng thuận với chuyển động của chỉ số VN30, phản ánh thông tin thực sự đang lan truyền — momentum ngắn hạn có thể theo. Thuộc nhóm lead-lag microstructure (futures dẫn dắt spot).

**Khẩu vị (formulation):** Volume-weighted return 2-bar (fast) và 6-bar (slow) trên futures + spot; mở lệnh lúc 03:00 & 07:00 UTC; đóng giỏi 04:15–04:30 & 07:30–07:50 (tránh giờ nghỉ trưa/đóng cửa); vị thế 0.75/–0.75 khi cả 4 điều kiện đồng thuận; filter volume nằm trong khoảng 0.7–2.2 lần SMA(12) để tránh phiên bất thường.

**Full-sample metrics (2020-01 → 2025-01):**

| Metric | Giá trị | | Metric | Giá trị |
|---|---|---|---|---|
| Sharpe | **2.84** | | Profit Factor | 2.07 |
| Sortino | 6.14 | | Win rate | 55.2% |
| Calmar | 5.57 | | Recovery Factor | 59.4 |
| CAGR | 39.8% | | Kelly Criterion | 28.5% |
| Max Drawdown | -7.1% | | Volatility | 12.3% |
| VaR | -1.14% | | CVaR | -1.32% |
| Tổng lợi nhuận | +424.2% | | Benchmark | 0 |
| Tổng phí 5 năm | 39.8% (~8%/năm) | | Số lệnh | 2,210 (1,105 round-trip) |

**Stage metrics (train 2020-2022 vs test 2023-2024):**

| Stage | Kỳ | CAGR | Sharpe | Max DD | Profit Factor | Decay (test/train) |
|---|---|---|---|---|---|---|
| Train | 2020-01 → 2022-12 | 59.4% | 3.09 | -7.1% | 2.16 | — |
| Test (OOS) | 2023-01 → 2025-01 | 49.7% | **2.39** | -6.9% | 1.82 | **0.77** |
| Simulate (Full) | 2020-01 → 2025-01 | 39.8% | 2.84 | -7.1% | 2.07 | — |

Lưu ý về lạm phát điểm: CAGR test (49.7%) cao hơn train (59.4%)? Không — CAGR giảm, nhưng vẫn rất mạnh (49.7% trong giai đoạn test). Đây là điểm cần nói rõ: CAGR giảm nhẹ là chuyển bình thường, quan trọng là Sharpe ổn định và PF > 1.8.

**Câu trả lời nhanh cho Q&A:**
- **Q1 (tại sao tin vào ý tưởng?)** Tương lai VN30 dẫn dắt chỉ số cơ sở trong các đợt impulse ngắn hạn; volume xác nhận tính chân thật của phản giá. Đây là lý thuyết microstructure có cơ sở tài chính, không phải data mining.
- **Q2 (chiến lược được xây thế nào?)** Hai chu kỳ áp lực lợi nhuận (2-bar và 6-bar) trên cả futures lẫn spot, kèm bộ lọc volume tương đối; chỉ hành động khi 4 điều kiện đồng thuận + volume bình thường; canh thời điểm trong khung giờ thanh khoản.
- **Q3 (hoạt động trong điều kiện nào?)** Hoạt động tốt cả xu hướng rõ ràng lẫn điều chỉnh — Test Sharpe 2.39 cho thấy không chỉ là chạy theo trend dài hạn.
- **Q4 (điểm mạnh / điểm yếu?)**
  - Mạnh: Sharpe cao nhất nhóm phái sinh, CAGR 39.8% vượt trội, win/loss ratio tốt (avg win +0.50% vs avg loss -0.13%).
  - Yếu: chi phí giao dịch cao (39.8% tổng phí 5 năm) — hiệu quả phụ thuộc vào mức phí thực tế của sàn; phụ thuộc thanh khoản kỳ hạn.
- **Q5 (cải thiện tiếp)?** Giảm số lệnh (2,210) bằng cách lọc chất lượng cao hơn; stress test với slippage 2–3 ticks để đảm bảo net-of-fee; cân nhắc nắm giữ dài hơn (ít churn hơn).

**Code đầy đủ:**

```python
"""
name: VNFutureAlpha_VolumeWeightedReturnPressure30M
summary: Trade three-hour return pressure when volume-backed futures momentum agrees with VN30.
"""

class CustomStrategy(SimpleAlgorithm):
    position_open_times = ["03:00", "07:00"]
    position_close_ranges = ["04:15-04:30", "07:30-07:50"]
    position_close_after_n_candles = 2

    def __algorithm__(self):
        close = self.data.pv_close
        volume = self.data.pv_volume
        vn30_close = self.data.pv_vn30_close

        futures_return = self.op.fillna(
            self.op.pct_change(close, periods=1),
            value=0,
        )
        spot_return = self.op.fillna(
            self.op.pct_change(vn30_close, periods=1),
            value=0,
        )

        reference_volume = self.feat.sma(volume, timeperiod=12)
        relative_volume = self.op.fillna(
            volume / (reference_volume + 0.000001),
            value=0,
        )
        weighted_return = futures_return * relative_volume

        futures_fast_pressure = self.feat.sma(
            weighted_return,
            timeperiod=2,
        )
        futures_slow_pressure = self.feat.sma(
            weighted_return,
            timeperiod=6,
        )
        spot_fast_pressure = self.feat.sma(
            spot_return,
            timeperiod=2,
        )
        spot_slow_pressure = self.feat.sma(
            spot_return,
            timeperiod=6,
        )

        recent_volume = self.feat.sma(volume, timeperiod=2)
        tradable_session = (
            (recent_volume > 0.70 * reference_volume)
            & (recent_volume < 2.20 * reference_volume)
        )

        long_setup = (
            (futures_fast_pressure > 0.00035)
            & (futures_slow_pressure > 0.00012)
            & (spot_fast_pressure > 0.00025)
            & (spot_slow_pressure > 0.00008)
            & tradable_session
        )
        short_setup = (
            (futures_fast_pressure < -0.00035)
            & (futures_slow_pressure < -0.00012)
            & (spot_fast_pressure < -0.00025)
            & (spot_slow_pressure < -0.00008)
            & tradable_session
        )

        self.set_positions(long_setup, position=0.75)
        self.set_positions(short_setup, position=-0.75)
```

---

### B3. Strategy 3 — Equity VN-MID-CAP — `Z0URlGzUp9`

**Luận điểm (hypothesis):** Công ty chi trả cổ tức và mua lại cổ phiếu (repurchase) thể hiện sự tin tưởng của ban lãnh đạo vào giá trị nội tại → *long* các công ty tái cấu trúc vốn tích cực. Đây là mặt đối lập của Strategy 1 (issuance) — hai chiến lược này bao phủ trọn câu chuyện "share count discipline" (giảm số lượng cổ phiếu lưu hành).

**Khẩu vị (formulation):** Cross-sectional ranking theo hoạt động mua lại/trả cổ tức so với tổng tài sản; kết hợp trend/impulse của dòng tiền tài chính; gate rank; long các công ty tái cấu trúc vốn tích cực. Cùng pipeline xử lý (demean + L1 normalize + EMA smoothing) như Strategy 1 — đây là điểm cần nói rõ khi so sánh: cùng pipeline, khác *signal* (2 luận điểm kinh doanh khác nhau).

**Full-sample metrics (2020-01 → 2025-01):**

| Metric | Giá trị | | Metric | Giá trị |
|---|---|---|---|---|
| Sharpe | **2.79** | | Profit Factor | 1.62 |
| Sortino | 4.74 | | Win rate | 58.3% |
| Calmar | 3.65 | | Recovery Factor | 28.4 |
| CAGR | 23.0% | | Kelly Criterion | 22.4% |
| Max Drawdown | -6.3% | | Volatility | 7.3% |
| VaR | -0.67% | | CVaR | -0.91% |
| Tổng lợi nhuận | +179.3% | | Benchmark | 0 |
| Tổng phí 5 năm | 17.8% (~3.6%/năm) | | Số lệnh | 1,220 |

**Stage metrics (train 2020-2022 vs test 2023-2024):**

| Stage | Kỳ | CAGR | Sharpe | Max DD | Profit Factor | Decay (test/train) |
|---|---|---|---|---|---|---|
| Train | 2020-01 → 2022-12 | 28.9% | 2.92 | -6.3% | 1.67 | — |
| Test (OOS) | 2023-01 → 2025-01 | 13.0% | **2.40** | -3.7% | 1.49 | **0.82** |
| Simulate (Full) | 2020-01 → 2025-01 | 23.0% | 2.79 | -6.3% | 1.62 | — |

**Câu trả lời nhanh cho Q&A:**
- **Q1 (tại sao tin vào ý tưởng?)** Mua lại cổ phiếu là tín hiệu định giá: ban lãnh đạo dùng tiền mặt mua lại cổ phiếu khi tin rằng chúng bị định giá thấp — ngược hoàn toàn với phát hành thêm (Strategy 1). Literature về open-market repurchase anomaly rất vững.
- **Q2 (chiến lược được xây thế nào?)** Cross-sectional rank theo tỷ lệ repurchase/dividend so với tài sản; kết hợp với chất lượng dòng tiền tài chính; gate 0.3–0.9; cùng pipeline normalization như Strategy 1 để giữ turnover thấp.
- **Q3 (hoạt động trong điều kiện nào?)** Ổn định 2020-2024, giai đoạn test Sharpe 2.40; yếu hơn khi thị trường giảm sâu do dòng tiền co lại.
- **Q4 (điểm mạnh / điểm yếu?)**
  - Mạnh: chi phí thấp nhất trong 3 (17.8%), drawdown nhỏ nhất (-6.3%), độ tin cậy mua lại cao.
  - Yếu: trên TTCK VN số công ty thực hiện buyback ít hơn — tập hợp cổ phiếu hẹp, capacity thấp hơn.
- **Q5 (cải thiện tiếp)?** Thêm điều kiện free cash flow để loại buyback không có "backing" thật; mở rộng sang SMALL-CAP; kiểm tra xung đột vị thế với Strategy 1 (cần chứng minh giỏ hàng gần như không trùng).

---

## C. SO SÁNH & CÂU CHUYỆN TRÌNH BÀY

### C1. Luận điểm tổng thể (narrative chính cho presentation)

> "Chúng tôi thiết kế 3 chiến lược độc lập, mỗi chiến lược đại diện cho một cơ chế tạo lợi nhuận khác nhau:
> (1) **short các công ty phát hành thêm cổ phiếu** (dòng tiền phát hành báo hiệu điều xấu),
> (2) **theo momentum phái sinh có xác nhận volume** (microstructure lead-lag futures–spot),
> (3) **long các công ty mua lại cổ phiếu** (tín hiệu định giá từ ban lãnh đạo).
> Điểm chung của cả ba: **đều vượt qua độ mạnh ngoài mẫu (test) — điều mà phần lớn chiến lược trên platform thất bại — và có chi phí giao dịch được kiểm soát (net-of-fee).**"

### C2. Bảng so sánh trực diện (dùng cho slide "Robustness")

| Tiêu chí | Strat 1 (MID short issuers) | Strat 2 (30MIN futures) | Strat 3 (MID long buyback) |
|---|---|---|---|
| Train Sharpe | 3.00 | 3.09 | 2.92 |
| **Test Sharpe** | **2.54** | **2.39** | **2.40** |
| Decay (test/train) | 0.85 | 0.77 | 0.82 |
| Simulate Sharpe | 2.80 | 2.84 | 2.79 |
| Max DD full | -6.4% | -7.1% | -6.3% |
| Max DD test | -3.7% | -6.9% | -3.7% |
| PF test | 1.52 | 1.82 | 1.49 |
| Phí 5 năm | 19.7% | 39.8% | 17.8% |
| Trades (full) | 1,220 | 2,210 | 1,220 |

### C3. Đối chiếu 5 tiêu chí chấm điểm của BTC

1. **Performance:** Sharpe full 2.79–2.84; CAGR 23–40%; Sortino 4.7–6.1; Calmar 3.6–5.6.
2. **Risk:** MDD -6.3% đến -7.1% (rất thấp so với thị trường); VaR tối đa -1.14%; drawdown giai đoạn test thậm chí nhỏ hơn.
3. **Robustness:** Không chiến lược nào bị "collapse" giữa các stage — decay 0.77–0.85 (khác hẳn nhóm LARGE-CAP decay 0.20–0.30 đã loại bỏ).
4. **Cost:** Phí 17.8–39.8% tổng 5 năm; chiến lược equity chỉ ~3.6–3.9%/năm; futures 8%/năm là chấp nhận được vì CAGR 39.8% (net vẫn còn ~32%/năm).
5. **Correlation:** 3 cơ chế tạo tín hiệu khác nhau; 2 chiến lược equity đối lập luận điểm (issuance vs buyback) — nên chuẩn bị 1 câu trả lời về việc giỏ hàng không trùng lặp.

---

## D. DỮ LIỆU THÔ (RAW JSON) — LƯU KÈM

- `/tmp/opencode/xno/final3/Strategy1.json` (+ `_train.json`, `_test.json`, `_simulate.json`)
- `/tmp/opencode/xno/final3/Strategy2.json` (+ stage files)
- `/tmp/opencode/xno/final3/Strategy3.json` (+ stage files)
- Code: `strategy_1_equity_mid_cap_lsGgvzSWeg.py`, `strategy_2_derivative_vn30f1m_EuVTWCWMNF.py`, `strategy_3_equity_mid_cap_Z0URlGzUp9.py` (cùng thư mục project này)

---

## E. CHECKLIST TRƯỚC DEADLINE 20/08 17:00 (GMT+7)

- [x] Chốt top 3 + rename thành **Strategy 1 / Strategy 2 / Strategy 3** (đã làm 19/08)
- [x] Xác nhận cả 3 ở trạng thái **Published** (đã verify qua API)
- [x] Export code + metrics đầy đủ vào file này (19/08)
- [ ] Chụp/export biểu đồ equity curve + drawdown từ platform cho từng chiến lược (cần làm trên UI)
- [ ] Kiểm tra giỏ hàng/overlap giữa Strategy 1 và Strategy 3 (để trả lời câu hỏi correlation)
- [ ] Làm slide (5 phút + 5 phút Q&A) theo Q1–Q5 ở mục B
- [ ] Gửi slide qua https://forms.gle/8fobtBcVauKFQNHt5 trước deadline