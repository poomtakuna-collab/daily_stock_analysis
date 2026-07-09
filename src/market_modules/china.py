# -*- coding: utf-8 -*-
"""Placeholder China market module."""

from __future__ import annotations

from src.market_modules.base import MarketModule, MarketModuleMetadata

CHINA_MARKET_ID = "cn"


class ChinaMarketModule(MarketModule):
    """Skeleton for China A-share market-specific capabilities."""

    _metadata = MarketModuleMetadata(
        market_id=CHINA_MARKET_ID,
        display_name="China A-share Market Module",
        default_symbols=("600519", "300750", "002594"),
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
            "chip_distribution",
            "capital_flow",
            "limit_up_down",
        }),
        indicators=(
            "moving_average",
            "rsi",
            "macd",
            "chip_distribution",
        ),
        data_sources=(
            "akshare",
            "tushare",
            "efinance",
            "baostock",
        ),
        review_sections=(
            "market_overview",
            "capital_flow",
            "policy_context",
            "limit_up_down",
        ),
        llm_features=(
            "policy_context",
            "capital_flow_summary",
            "theme_rotation",
        ),
        placeholder=True,
    )

    @property
    def metadata(self) -> MarketModuleMetadata:
        return self._metadata
