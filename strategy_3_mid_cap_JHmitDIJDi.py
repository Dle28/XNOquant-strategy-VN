class CustomStrategy(SimpleAlgorithm):
    """Quarterly financing-cash regime relative to assets."""
    def __algorithm__(self):
        close=self.data.pv_close_panel
        volume=self.data.pv_volume_panel
        eps=self.data.fun_is_eps_basis_quarterly_panel
        net_profit=self.data.fun_is_net_profit_loss_after_tax_quarterly_panel
        total_assets=self.data.fun_bs_total_assets_quarterly_panel
        equity=self.data.fun_bs_owners_equity_quarterly_panel
        operating_cash=self.data.fun_cf_net_cash_inflows_outflows_from_operating_activities_quarterly_panel
        revenue=self.data.fun_is_sales_quarterly_panel
        daily_return=self.feat.returns_panel(close)
        volatility=self.feat.rolling_std_panel(daily_return)
        traded_value=self.feat.rolling_value_panel(close,volume)
        earnings_yield=self.feat.safe_divide_panel(eps,close)
        roa=self.feat.safe_divide_panel(net_profit,total_assets)
        fresh_ratio=self.feat.safe_divide_panel(self.data.fun_cf_net_cash_inflows_outflows_from_financing_activities_quarterly_panel,self.data.fun_bs_total_assets_quarterly_panel)
        fresh_fast=self.feat.ema_panel(fresh_ratio,3)
        fresh_slow=self.feat.ema_panel(fresh_fast,8)
        fresh_trend=fresh_fast-fresh_slow
        fresh_impulse=fresh_trend-self.feat.ema_panel(fresh_trend,8)
        base=(close.notna()&volume.notna()&eps.notna()&net_profit.notna()&total_assets.notna()&equity.notna()&operating_cash.notna()&revenue.notna()&(revenue>0)
            &daily_return.notna()&volatility.notna()&traded_value.notna()&earnings_yield.notna()&roa.notna()&fresh_ratio.notna()&fresh_fast.notna()&fresh_slow.notna()&fresh_trend.notna()&fresh_impulse.notna()&(self.data.fun_bs_total_assets_quarterly_panel>0)
            &(close>0)&(volume>0)&(total_assets>0)&(equity>0)&(volatility>0)&(traded_value>0))
        gate=self.op.rank_cs_panel(fresh_trend,mask=base)
        eligible=base&gate.notna()&(gate>=0.1)&(gate<0.9)
        v=self.op.demean_cs_panel(self.op.rank_cs_panel(volatility,mask=eligible),mask=eligible)
        d=self.op.demean_cs_panel(self.op.rank_cs_panel(traded_value,mask=eligible),mask=eligible)
        y=self.op.demean_cs_panel(self.op.rank_cs_panel(earnings_yield,mask=eligible),mask=eligible)
        r=self.op.demean_cs_panel(self.op.rank_cs_panel(roa,mask=eligible),mask=eligible)
        x_pr=self.op.demean_cs_panel(self.op.rank_cs_panel(fresh_trend,mask=eligible),mask=eligible)
        signal=(v*.28-d*.28+y*.10+r*.10)+x_pr*.24
        valid=eligible&signal.notna()
        raw=self.op.normalize_l1_cs_panel(self.op.demean_cs_panel(signal,mask=valid),mask=valid)
        slow=self.feat.ema_panel(raw,18)
        weight_valid=valid&raw.notna()&slow.notna()
        final_weights=self.op.normalize_l1_cs_panel(self.op.demean_cs_panel(raw*0.3+slow*0.7,mask=weight_valid),mask=weight_valid)
        self.set_portfolio_positions(final_weights)
