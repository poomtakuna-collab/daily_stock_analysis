# -*- coding: utf-8 -*-
"""Tests for the data source registry skeleton."""

import pytest

from src.data_sources import (
    DataSourceRegistry,
    EastmoneyDataSource,
    InsiderDataSource,
    SECDataSource,
    TushareDataSource,
    UnknownDataSourceError,
    YahooFinanceDataSource,
    build_default_data_source_registry,
)


def test_default_registry_registers_placeholder_sources():
    registry = build_default_data_source_registry()

    source_ids = [source.source_id for source in registry.list_all()]

    assert source_ids == [
        "eastmoney",
        "insider",
        "sec",
        "tushare",
        "yahoo_finance",
    ]
    assert isinstance(registry.get("eastmoney"), EastmoneyDataSource)
    assert isinstance(registry.get("insider"), InsiderDataSource)
    assert isinstance(registry.get("sec"), SECDataSource)
    assert isinstance(registry.get("tushare"), TushareDataSource)
    assert isinstance(registry.get("yahoo_finance"), YahooFinanceDataSource)


def test_lookup_and_has_normalize_source_id():
    registry = build_default_data_source_registry()

    assert registry.has(" YAHOO_FINANCE ")
    assert registry.has(" SEC ")
    assert registry.get(" TUSHARE ").source_id == "tushare"


def test_duplicate_registration_is_rejected():
    registry = DataSourceRegistry([YahooFinanceDataSource()])

    with pytest.raises(ValueError, match="already registered"):
        registry.register(YahooFinanceDataSource())


def test_unknown_source_raises_registry_error():
    registry = build_default_data_source_registry()

    with pytest.raises(UnknownDataSourceError):
        registry.get("unknown")


def test_list_for_market_us_returns_us_placeholder_sources():
    registry = build_default_data_source_registry()

    source_ids = [source.source_id for source in registry.list_for_market(" US ")]

    assert source_ids == ["insider", "sec", "yahoo_finance"]


def test_list_for_market_cn_returns_china_placeholder_sources():
    registry = build_default_data_source_registry()

    source_ids = [source.source_id for source in registry.list_for_market(" CN ")]

    assert source_ids == ["eastmoney", "tushare"]


def test_source_metadata_is_static_and_iterable():
    sources = build_default_data_source_registry().list_all()

    for source in sources:
        assert source.source_id
        assert source.display_name
        assert source.description
        assert source.is_placeholder is True
        assert isinstance(source.is_realtime, bool)
        assert isinstance(source.is_free, bool)
        assert isinstance(source.requires_api_key, bool)
        assert list(source.supported_markets)
        assert list(source.supported_capabilities)


def test_placeholder_sources_declare_expected_capabilities():
    registry = build_default_data_source_registry()

    assert registry.get("yahoo_finance").supports_market("us")
    assert registry.get("yahoo_finance").supports_capability("realtime_quote")
    assert registry.get("sec").supports_capability("sec_filings")
    assert registry.get("insider").supports_capability("insider_activity")
    assert registry.get("eastmoney").supports_market("cn")
    assert registry.get("eastmoney").supports_capability("capital_flow")
    assert registry.get("tushare").supports_capability("trading_calendar")
    assert registry.get("tushare").requires_api_key is True
