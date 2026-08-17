class CustomStrategy(SimpleAlgorithm):
    """No issuance and buyback combined: share-count discipline from both directions concentrates per-share value reliably."""
    def __algorithm__(self):
        close = self.data.pv_close_panel
        volume = self.data.pv_volume_panel
        eps = self.data.fun_is_eps_basis_quarterly_panel
        net_profit = self.data.fun_is_net_profit_loss_after_tax_quarterly_panel
        total_assets = self.data.fun_bs_total_assets_quarterly_panel
        equity = self.data.fun_bs_owners_equity_quarterly_panel
        operating_cash = self.data.fun_cf_net_cash_inflows_outflows_from_operating_activities_quarterly_panel
        revenue = self.data.fun_is_sales_quarterly_panel
        daily_return = self.feat.returns_panel(close)
        volatility = self.feat.rolling_std_panel(daily_return)
        traded_value = self.feat.rolling_value_panel(close, volume)
        earnings_yield = self.feat.safe_divide_panel(eps, close)
        roa = self.feat.safe_divide_panel(net_profit, total_assets)

        issued = self.data.fun_cf_proceeds_from_issue_of_shares_quarterly_panel
        iss_assets = self.feat.safe_divide_panel(issued, total_assets) 
        iss_improve = self.feat.ema_panel(iss_assets, 4) - iss_assets
        treasury = self.data.fun_bs_treasury_shares_quarterly_panel
        tre_assets = self.feat.safe_divide_panel(treasury, total_assets)
        tre_accel = tre_assets - self.feat.ema_panel(tre_assets, 4)
        combo = iss_improve + 2.0 * tre_accel
        base = (close.notna() & volume.notna() & eps.notna() & net_profit.notna()
            & total_assets.notna() & equity.notna() & operating_cash.notna() & revenue.notna() & (revenue > 0)
            & daily_return.notna() & volatility.notna() & traded_value.notna() & earnings_yield.notna() & roa.notna()
            & (close > 0) & (volume > 0) & (total_assets > 0) & (equity > 0)
            & (volatility > 0) & (traded_value > 0))
        gate = self.op.rank_cs_panel(combo, mask=base)
        eligible = base & gate.notna() & (gate >= 0.5) & (gate < 0.95)
        v = self.op.demean_cs_panel(self.op.rank_cs_panel(volatility, mask=eligible), mask=eligible)
        d = self.op.demean_cs_panel(self.op.rank_cs_panel(traded_value, mask=eligible), mask=eligible)
        y = self.op.demean_cs_panel(self.op.rank_cs_panel(earnings_yield, mask=eligible), mask=eligible)
        r = self.op.demean_cs_panel(self.op.rank_cs_panel(roa, mask=eligible), mask=eligible)
        iss_improve
        tre_accel
        iss_improve_d = self.op.demean_cs_panel(self.op.rank_cs_panel(iss_improve, mask=eligible), mask=eligible)
        tre_accel_d = self.op.demean_cs_panel(self.op.rank_cs_panel(tre_accel, mask=eligible), mask=eligible)
        signal = (v * 0.2 + d * -0.25 + y * 0.1 + r * 0.05) * 1.0 + iss_improve_d * 0.15 + tre_accel_d * 0.1
        valid = eligible & signal.notna()
        raw = self.op.normalize_l1_cs_panel(self.op.demean_cs_panel(signal, mask=valid), mask=valid)
        slow = self.feat.ema_panel(raw)
        weight_valid = valid & raw.notna() & slow.notna()
        final_weights = self.op.normalize_l1_cs_panel(
            self.op.demean_cs_panel(raw * 0.25 + slow * 0.75, mask=weight_valid),
            mask=weight_valid
        )
        self.set_portfolio_positions(final_weights)
