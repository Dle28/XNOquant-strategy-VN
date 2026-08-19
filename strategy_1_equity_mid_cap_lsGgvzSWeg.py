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
