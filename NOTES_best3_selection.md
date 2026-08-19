# DSTC 2026 Vong 3 - Chon 3 chien luoc trinh bay tai Chung ket

> Ngay phan tich: 19/08/2026 - Nguon: du lieu truc tiep tu API alpha.xnoquant.io (2 tai khoan)
> TK1 = dung.levc2810@gmail.com (Dung Le) - TK2 = khaiapmops2006@gmail.com (Nguyen Quang Khai)

---

## 1. Quy dinh bat buoc (tu "Bo luat du thi Vong 3 - DSTC 2026")

| # | Yeu cau | Dap ung |
|---|---------|---------|
| 1 | It nhat 1 chien luoc co phieu VN (VN-LARGE/MID/SMALL-CAP) | Equity |
| 2 | It nhat 1 chien luoc phai sinh VN (VN30F1M) | VN30F1M |
| 3 | Chien luoc thu 3 tu do chon | Free |
| 4 | Ca 3 phai dat trang thai **Published** tren XNOQuant | OK (da verify) |
| 5 | Han chot: **17:00 ngay 20/08/2026 (GMT+7)** | Can rename thanh "Strategy 1/2/3" truoc han |

Scoring 50% = Research score tren XNOQuant (Round 1 + 2) + 50% = Presentation & Q&A.
Tieu chi cham tren platform: Performance (Sharpe/CAGR/Sortino/Calmar), Risk (MDD/VaR/CVaR/Ulcer), **Robustness (on dinh qua train/test/simulate/forward)**, Cost (net-of-fee, turnover), Correlation (doc dao, khong trung lap).

---

## 2. Du lieu thu thap tu platform

- TK1: 2,114 strategy published (VN-LARGE-CAP 359 - VN-MID-CAP 1,688 - VN30F1M-05MIN 67)
- TK2: 2,353 strategy published (VN-LARGE-CAP 1,210 - VN-MID-CAP 1,024 - VN30F1M nhieu timeframe 119)
- Da thu thap day du: ma nguon, metrics full-sample, metrics theo stage **train** (2020-2022) va **test** (2023-2025), chi phi, so lenh.
- Diem vong 1 (ca nhan): TK1 rank 34 (1191) - TK2 rank 18 (1591)
- Diem vong 2 (team, private): TK1 rank 10 (4384) - TK2 rank 9 (6129)

---

## 3. Phat hien QUAN TRONG - Chien luoc LARGE-CAP dang bi OVERFIT

Toan bo nhom VN-LARGE-CAP ma team dang co deu roi vao canh **train khoe nhung test yeu** (test la giai doan 2023-2025, out-of-sample):

| Strategy (large-cap) | Acct | Full Sharpe | Train | Test | Decay (test/train) |
|---|---|---|---|---|---|
| 7mNd5gsyLA | TK2 | 2.09 | 3.34 | **1.01** | 0.30 |
| 7cNI7deXQO (**dang chon**) | TK1 | 1.74 | 2.58 | **0.63** | 0.25 |
| wyC42GEp6V | TK2 | 2.07 | 2.88 | 0.67 | 0.23 |
| Ta63REQjBD | TK2 | 2.05 | 2.87 | 0.64 | 0.22 |
| sTNz1OXBGQ | TK2 | 2.04 | 2.87 | 0.57 | 0.20 |

> WARNING: O test stage, Profit Factor chi con ~1.10-1.20, Sharpe < 1.0.
> Luat va tieu chi cham deu noi ro: "Strong results in one stage that collapse in another are treated as evidence of overfitting."
> Ban giam khao se soi ngay diem nay o phan Q&A. Khong nen trinh LARGE-CAP trong top 3.

---

## 4. Nhom VN-MID-CAP - Manh va ON DINH NHAT

| id | Acct | Full Sharpe | Train | Test | Decay | MDD | CAGR | PF | Trades | Chi phi |
|----|------|-----------|-------|------|-------|-----|------|----|--------|------|
| **lsGgvzSWeg** (Untitled 152) | TK1 | **2.80** | 3.00 | **2.54** | 0.85 | -6.4% | 25.0% | 1.65 | 1220 | 19.7% |
| iqw6R31INB (Untitled 7) | TK1 | 2.76 | 3.08 | 2.40 | 0.78 | -6.3% | 25.3% | 1.64 | 1229 | 52.4% |
| Z0URlGzUp9 (Untitled 8) | TK1 | 2.79 | 2.92 | 2.40 | 0.82 | -6.3% | 23.0% | 1.62 | 1220 | 17.8% |
| 3MQIl9aONL (Untitled 151) | TK1 | 2.66 | 2.72 | 2.33 | 0.86 | -7.2% | 23.2% | 1.59 | 1220 | 17.1% |
| JHmitDIJDi (Untitled 139, **dang chon**) | TK1 | 2.49 | 2.76 | 2.35 | 0.85 | -10.8% | 23.3% | 1.56 | 1229 | 24.2% |

> Day la universe duy nhat co do tru vung tot: test Sharpe 2.3-2.5, decay >= 0.78.
> De xuat thay the mid-cap hien tai (JHmitDIJDi) bang **lsGgvzSWeg** - cao diem hon toan dien (Sharpe +0.31, MDD -6.4% thay vi -10.8%).

---

## 5. Nhom VN30F1M (phai sinh) - Co lua chon manh hon

| id | Timeframe | Acct | Full Sharpe | Train | Test | Decay | MDD | CAGR | PF | Trades | Chi phi |
|----|-----------|------|-----------|-------|------|-------|-----|------|----|--------|------|
| **EuVTWCWMNF** (Untitled 9) | 30MIN | TK2 | **2.84** | 3.09 | **2.39** | 0.77 | -7.1% | 39.8% | 2.07 | 2210 | 39.8% |
| Kkdt9m4QQv (Untitled 8) | 10MIN | TK2 | 2.54 | 2.77 | 2.07 | 0.75 | -6.0% | 29% | 2.18 | 2031 | 30.6% |
| xX2lGXjNOj (Untitled 8) | 10MIN | TK2 | 2.54 | 2.78 | 2.06 | 0.74 | -6.2% | 31% | 2.18 | 2031 | 30.6% |
| IwEa1HnCXD (Untitled 102, **dang chon**) | 05MIN | TK1 | 2.35 | 2.62 | 1.77 | 0.67 | -4.5% | 27.4% | 2.06 | 1346 | 22.6% |
| OHCXUf6S1S (Untitled 3) | 05MIN | TK1 | 2.06 | 1.97 | 2.18 | 1.10 | -4.6% | 18.1% | 1.60 | 6648 | 62.7% |

> VN30F1M-30MIN (EuVTWCWMNF) to diem nhat: Sharpe 2.84, CAGR 39.8%, chi phi 8%/nam tuong duong.
> Giu IwEa1HnCXD (05MIN) cung hop ly: chi phi thap, MDD chi -4.5%, nhung test-consistency yeu hon (1.77 so voi 2.39).

---

## 6. DE XUAT: TOP 3 CHIEN LUOC TRINH BAY

Lua chon toi uu theo quy dinh (it nhat 1 equity + it nhat 1 VN30F1M + 1 tu do):

| Vai tro | ID | Acct | Universe | Full Sharpe | Test Sharpe | MDD | CAGR | Ly thuyet |
|---|---|---|---|---|---|---|---|---|
| Strategy 1 (Equity) | **lsGgvzSWeg** = "Strategy 1" | TK1 | VN-MID-CAP | **2.80** | **2.54** | -6.4% | 25.0% | Equity issuance dilution - short issuers |
| Strategy 2 (Derivative) | **EuVTWCWMNF** = "Strategy 2" | TK2 | VN30F1M-30MIN | **2.84** | **2.39** | -7.1% | 39.8% | Volume-weighted return pressure |
| Strategy 3 (Free) | **Z0URlGzUp9** = "Strategy 3" | TK1 | VN-MID-CAP | **2.79** | **2.40** | -6.3% | 23.0% | Buyback commitment - long repurchasers |

Phuong an thay the (neu muon 3 universe khac nhau):

| Vai tro | ID | Acct | Universe | Full Sharpe | Test Sharpe | MDD | CAGR | Ghi chu |
|---|---|---|---|---|---|---|---|---|
| Strategy 1 (Equity) | lsGgvzSWeg | TK1 | VN-MID-CAP | 2.80 | 2.54 | -6.4% | 25.0% | Equity issuance dilution |
| Strategy 2 (Derivative) | IwEa1HnCXD | TK1 | VN30F1M-05MIN | 2.35 | 1.77 | -4.5% | 27.4% | Dual KAMA slope (giu nguyen) |
| Strategy 3 (Free) | Z0URlGzUp9 | TK1 | VN-MID-CAP | 2.79 | 2.40 | -6.3% | 23.0% | Buyback commitment |

**KHUYEN NGHI:** Loai bo LARGE-CAP (overfit), chon 2 equity MID-CAP (issuance vs buyback - 2 ly thuyet doi lap, bao phu ca hai phia cua cau chuyen share count) + 1 VN30F1M-30MIN hoac giu 05MIN.

---

## 7. Ghi chu cho phan Presentation (Q1-Q5)

### Strategy 1 - Equity (VN-MID-CAP): lsGgvzSWeg - da rename thanh "Strategy 1" (19/08 22:12 GMT+7)
- **Q1 (hypothesis):** Equity issuance scheme dilutes existing holders va thuong tien bao cac hoat dong kem hieu qua. Gia dinh rang cong ty phat hanh co phieu moi de huy dong von dang gap ap luc tai chinh hoac co thong tin bat loi. (Ideas tu literature ve seasoned equity offerings - SEO underperformance).
- **Q2 (formulation):** Using cash flow from issuing shares / total assets; EMA smoothing; long issuers with high issuance vs short issuers with low issuance (cross-sectional); gate rank 0.1-0.95; weights via demean + L1 normalize + EMA smoothing.
- **Q3 (regime):** Manh o giai doan thinh thinh thi truong (2020-2022), van duy tri tot o giai doan dieu chinh (test 2.54).
- **Q4 (strength/weakness):** Edge tu fundamental/behavioral (issuance signaling). Ye mon: gap sau dot cap von lon hoac trong thi truong co so phan hoa manh.
- **Q5 (improvement):** Turnover thap (chi phi 19.7% tong 5 nam), tot cho capacity lon; co the them sector-neutral layer de giam concentration.

### Strategy 2 - Derivative (VN30F1M): EuVTWCWMNF - da rename thanh "Strategy 2" (19/08 22:12 GMT+7)
- **Q1 (hypothesis):** Su dong bo giua cau futures va cau VN30 khi co volume xac nhan phan anh dong thong tin that su - momentum trend-following ngắn han.
- **Q2 (formulation):** Volume-weighted return pressure; open 03:00 & 07:00 UTC; close 04:15-04:30 & 07:30-07:50; position -0.7/+0.7 theo dieu kien dong thuan ca hai thi truong.
- **Q3 (regime):** Hoat dong tot ca trong xu huong ro rang lan dieu chinh (test 2.39 van cao).
- **Q4 (strength/weakness):** Edge tu market microstructure (lead-lag futures vs spot). Ye diem: chi phi giao dich cao hon (39.8% tong 5 nam), phu thuoc vao thanh khoan cua ky han.
- **Q5 (improvement):** Giam so lenh (2210) bang cach loc quality cao hon; test them slippage 2-3 ticks de dam bao net-of-fee.

### Strategy 3 (Free) - Equity (VN-MID-CAP): Z0URlGzUp9 - da rename thanh "Strategy 3" (19/08 22:12 GMT+7)
- **Q1 (hypothesis):** Chi tra co tuc + mua lai co phieu (repurchase) khang dinh su tin nhiem cua ban lanh dao ve gia tri noi tai - long repurchasers. Nganh nghich voi Strategy 1 (issuance) - hai ben cua "share count discipline".
- **Q2 (formulation):** Buyback/treasury shares tren total assets; trend + impulse cua financing cash; gate rank; long cac cong ty tai cau truc von tich cuc.
- **Q3 (regime):** On dinh 2021-2024, giam nhe khi thi truong giam manh do dong vao cash quality.
- **Q4 (strength/weakness):** Edge tu hành vi/co cau (share buyback signaling). Ye diem: it cong ty thuc hien buyback tren TTCK VN, nen tap hop be.
- **Q5 (improvement):** Them dieu kien ve free cash flow de loc buyback co "backing" thuc su.

---

## 8. Viec can lam truoc deadline 20/08 17:00

1. [x] Rename 3 strategy tren platform thanh **"Strategy 1"**, **"Strategy 2"**, **"Strategy 3"** (dung thu tu trinh bay) - **DA THUC HIEN 19/08 22:12 GMT+7** (API: PUT /xalpha-api/v2/strategies/{id}/update)
2. [x] Xac nhan lai trang thai Published cua 3 strategy da chon (verify qua API 19/08 22:40)
3. [x] Export code + metrics day du vao **EXPORT_best3_final.md** + thua vao `data/` (19/08 22:40)
4. [ ] Chup/save do thi equity curve + drawdown tren platform (lam tren UI)
5. [ ] Kiem tra overlap gio hang giua Strategy 1 va Strategy 3 (tra loi cau hoi correlation)
6. [ ] Gui slide qua form: https://forms.gle/8fobtBcVauKFQNHt5
7. [ ] Chuan bi ki nang tra loi Q&A 5 phut + 5 phut thoi gian cho doi thu.

---

## 9. Du lieu tham khao da luu

- /tmp/opencode/xno/tk1_all_summary.json - tom tat toan bo TK1 published
- /tmp/opencode/xno/tk2_all_summary.json - tom tat toan bo TK2 published
- /tmp/opencode/xno/tk1_codes.json - ma nguon toan bo TK1
- /tmp/opencode/xno/tk2_codes.json - ma nguon toan bo TK2
- /tmp/opencode/xno/stage/*.json - metrics theo stage (train/test) cho cac ung vien
