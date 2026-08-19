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
