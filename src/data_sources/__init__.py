# -*- coding: utf-8 -*-
"""Data source skeletons.

Sprint 15 intentionally keeps this package disconnected from production
analysis flows. The registry is importable and testable, but analyzers,
prompts, strategies, dashboards, and provider routing still use their existing
paths.
"""

from src.data_sources.base import DataSource, DataSourceMetadata
from src.data_sources.registry import (
    DataSourceRegistry,
    UnknownDataSourceError,
    build_default_data_source_registry,
)
from src.data_sources.sources import (
    EASTMONEY_SOURCE_ID,
    INSIDER_SOURCE_ID,
    SEC_SOURCE_ID,
    TUSHARE_SOURCE_ID,
    YAHOO_FINANCE_SOURCE_ID,
    EastmoneyDataSource,
    InsiderDataSource,
    SECDataSource,
    TushareDataSource,
    YahooFinanceDataSource,
)

__all__ = [
    "DataSource",
    "DataSourceMetadata",
    "DataSourceRegistry",
    "EASTMONEY_SOURCE_ID",
    "EastmoneyDataSource",
    "INSIDER_SOURCE_ID",
    "InsiderDataSource",
    "SECDataSource",
    "SEC_SOURCE_ID",
    "TUSHARE_SOURCE_ID",
    "TushareDataSource",
    "UnknownDataSourceError",
    "YAHOO_FINANCE_SOURCE_ID",
    "YahooFinanceDataSource",
    "build_default_data_source_registry",
]
