# -*- coding: utf-8 -*-
"""Placeholder data source definitions."""

from __future__ import annotations

from src.data_sources.base import DataSource, DataSourceMetadata

YAHOO_FINANCE_SOURCE_ID = "yahoo_finance"
SEC_SOURCE_ID = "sec"
INSIDER_SOURCE_ID = "insider"
EASTMONEY_SOURCE_ID = "eastmoney"
TUSHARE_SOURCE_ID = "tushare"


class YahooFinanceDataSource(DataSource):
    """Skeleton for Yahoo Finance market data capabilities."""

    _metadata = DataSourceMetadata(
        source_id=YAHOO_FINANCE_SOURCE_ID,
        display_name="Yahoo Finance",
        description="Placeholder metadata for US-oriented market prices and fundamentals.",
        supported_markets=frozenset({"us"}),
        supported_capabilities=frozenset({
            "daily_history",
            "realtime_quote",
            "fundamentals",
            "market_indices",
        }),
        is_realtime=True,
        is_free=True,
        requires_api_key=False,
        placeholder=True,
    )

    @property
    def metadata(self) -> DataSourceMetadata:
        return self._metadata


class SECDataSource(DataSource):
    """Skeleton for SEC filing capabilities."""

    _metadata = DataSourceMetadata(
        source_id=SEC_SOURCE_ID,
        display_name="SEC",
        description="Placeholder metadata for US company filing context.",
        supported_markets=frozenset({"us"}),
        supported_capabilities=frozenset({
            "sec_filings",
            "company_disclosures",
            "filing_summary",
        }),
        is_realtime=False,
        is_free=True,
        requires_api_key=False,
        placeholder=True,
    )

    @property
    def metadata(self) -> DataSourceMetadata:
        return self._metadata


class InsiderDataSource(DataSource):
    """Skeleton for insider activity capabilities."""

    _metadata = DataSourceMetadata(
        source_id=INSIDER_SOURCE_ID,
        display_name="Insider Activity",
        description="Placeholder metadata for US insider transaction context.",
        supported_markets=frozenset({"us"}),
        supported_capabilities=frozenset({
            "insider_activity",
            "ownership_changes",
        }),
        is_realtime=False,
        is_free=True,
        requires_api_key=False,
        placeholder=True,
    )

    @property
    def metadata(self) -> DataSourceMetadata:
        return self._metadata


class EastmoneyDataSource(DataSource):
    """Skeleton for Eastmoney A-share market data capabilities."""

    _metadata = DataSourceMetadata(
        source_id=EASTMONEY_SOURCE_ID,
        display_name="Eastmoney",
        description="Placeholder metadata for China A-share market data and capital flow.",
        supported_markets=frozenset({"cn"}),
        supported_capabilities=frozenset({
            "daily_history",
            "realtime_quote",
            "capital_flow",
            "market_indices",
        }),
        is_realtime=True,
        is_free=True,
        requires_api_key=False,
        placeholder=True,
    )

    @property
    def metadata(self) -> DataSourceMetadata:
        return self._metadata


class TushareDataSource(DataSource):
    """Skeleton for Tushare A-share data capabilities."""

    _metadata = DataSourceMetadata(
        source_id=TUSHARE_SOURCE_ID,
        display_name="Tushare",
        description="Placeholder metadata for China A-share structured market data.",
        supported_markets=frozenset({"cn"}),
        supported_capabilities=frozenset({
            "daily_history",
            "fundamentals",
            "trading_calendar",
            "stock_list",
        }),
        is_realtime=False,
        is_free=False,
        requires_api_key=True,
        placeholder=True,
    )

    @property
    def metadata(self) -> DataSourceMetadata:
        return self._metadata
