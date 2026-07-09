# -*- coding: utf-8 -*-
"""Placeholder US market module."""

from __future__ import annotations

from src.market_modules.base import MarketModule, MarketModuleMetadata

US_MARKET_ID = "us"


class USMarketModule(MarketModule):
    """Skeleton for US equity market-specific capabilities."""

    _metadata = MarketModuleMetadata(
        market_id=US_MARKET_ID,
        display_name="US Equity Market Module",
        default_symbols=("MSFT", "AAPL", "NVDA"),
        capabilities=frozenset({
            "symbol_rules",
            "trading_rules",
            "calendar",
            "market_metrics",
            "fundamentals",
            "intelligence_sources",
            "prompt_fragments",
            "strategy_tags",
            "provider_capabilities",
            "sec_filings",
            "earnings_context",
            "insider_activity",
            "social_sentiment",
        }),
        indicators=(
            "moving_average",
            "rsi",
            "macd",
            "earnings_momentum",
        ),
        data_sources=(
            "yfinance",
            "alphavantage",
            "finnhub",
            "sec_filings",
        ),
        review_sections=(
            "market_overview",
            "sector_rotation",
            "earnings_context",
            "risk_factors",
        ),
        llm_features=(
            "earnings_context",
            "sec_filing_summary",
            "social_sentiment",
        ),
        placeholder=True,
    )

    @property
    def metadata(self) -> MarketModuleMetadata:
        return self._metadata
