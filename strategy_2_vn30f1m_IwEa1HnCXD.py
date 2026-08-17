"""
name: VNFutureAlpha_u66_DualKAMAAdaptiveSlope
summary: Trade aligned volatility-normalized slopes of adaptive KAMA trends.

idea:
    Compute a thirty-bar Kaufman adaptive moving average in futures and VN30,
    then measure its six-bar change relative to each market's ATR. At 03:35 and
    07:15 UTC, trade only when both adaptive slopes agree and futures price is
    on the matching side of its KAMA under normal participation.

hypothesis:
    KAMA slope follows the locally efficient price path rather than a fixed-speed
    moving-average crossover, raw return, range-direction or volume-flow state.

failure_condition:
    Reject if Test Sharpe is below 1.0, Test CAGR is non-positive, any stage
    Profit Factor is below 1.1, Simulate drawdown exceeds 15%, or fewer than 200
    full-sample trades occur.
"""


class CustomStrategy(SimpleAlgorithm):
    position_open_times = ["03:35", "07:15"]
    position_close_ranges = ["04:20-04:30", "07:40-07:50"]
    position_close_after_n_candles = 6

    def __algorithm__(self):
        high = self.data.pv_high
        low = self.data.pv_low
        close = self.data.pv_close
        volume = self.data.pv_volume

        vn30_high = self.data.pv_vn30_high
        vn30_low = self.data.pv_vn30_low
        vn30_close = self.data.pv_vn30_close

        futures_kama = self.feat.kama(close, timeperiod=30)
        vn30_kama = self.feat.kama(vn30_close, timeperiod=30)

        futures_atr = self.feat.atr(high, low, close, timeperiod=14)
        vn30_atr = self.feat.atr(
            vn30_high,
            vn30_low,
            vn30_close,
            timeperiod=14,
        )

        futures_slope = self.op.fillna(
            (futures_kama - self.op.shift(futures_kama, periods=6))
            / (futures_atr + 0.000001),
            value=0,
        )
        vn30_slope = self.op.fillna(
            (vn30_kama - self.op.shift(vn30_kama, periods=6))
            / (vn30_atr + 0.000001),
            value=0,
        )

        recent_volume = self.feat.sma(volume, timeperiod=12)
        reference_volume = self.feat.sma(volume, timeperiod=36)
        active_session = recent_volume > 0.75 * reference_volume

        long_setup = (
            (futures_slope > 0.30)
            & (vn30_slope > 0.15)
            & (close > futures_kama)
            & active_session
        )

        short_setup = (
            (futures_slope < -0.30)
            & (vn30_slope < -0.15)
            & (close < futures_kama)
            & active_session
        )

        self.set_positions(long_setup, position=0.70)
        self.set_positions(short_setup, position=-0.70)
