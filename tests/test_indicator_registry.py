# -*- coding: utf-8 -*-
"""Tests for the indicator registry skeleton."""

from pathlib import Path

import pytest

from src.indicators_registry import (
    IndicatorRegistry,
    MACDIndicator,
    RSIIndicator,
    SMAIndicator,
    UnknownIndicatorError,
    build_default_indicator_registry,
)


def test_default_registry_registers_placeholder_indicators():
    registry = build_default_indicator_registry()

    indicator_ids = [indicator.indicator_id for indicator in registry.list_all()]

    assert indicator_ids == [
        "atr",
        "capital_flow",
        "chip_distribution",
        "concept_board",
        "earnings_trend",
        "ema",
        "limit_up",
        "macd",
        "market_breadth",
        "relative_strength",
        "rsi",
        "sector_leadership",
        "sma",
        "volume",
        "vwap",
    ]
    assert isinstance(registry.get("macd"), MACDIndicator)
    assert isinstance(registry.get("rsi"), RSIIndicator)
    assert isinstance(registry.get("sma"), SMAIndicator)


def test_lookup_and_has_normalize_indicator_id():
    registry = build_default_indicator_registry()

    assert registry.has(" MACD ")
    assert registry.has(" RSI ")
    assert registry.get(" SMA ").indicator_id == "sma"


def test_duplicate_registration_is_rejected():
    registry = IndicatorRegistry([SMAIndicator()])

    with pytest.raises(ValueError, match="already registered"):
        registry.register(SMAIndicator())


def test_unknown_indicator_raises_registry_error():
    registry = build_default_indicator_registry()

    with pytest.raises(UnknownIndicatorError):
        registry.get("unknown")


def test_list_for_market_us_returns_core_and_us_placeholder_indicators():
    registry = build_default_indicator_registry()

    indicator_ids = [indicator.indicator_id for indicator in registry.list_for_market(" US ")]

    assert indicator_ids == [
        "atr",
        "earnings_trend",
        "ema",
        "macd",
        "market_breadth",
        "relative_strength",
        "rsi",
        "sector_leadership",
        "sma",
        "volume",
        "vwap",
    ]


def test_list_for_market_cn_returns_core_and_china_placeholder_indicators():
    registry = build_default_indicator_registry()

    indicator_ids = [indicator.indicator_id for indicator in registry.list_for_market(" CN ")]

    assert indicator_ids == [
        "atr",
        "capital_flow",
        "chip_distribution",
        "concept_board",
        "ema",
        "limit_up",
        "macd",
        "rsi",
        "sma",
        "volume",
        "vwap",
    ]


def test_list_by_category_core_returns_core_placeholder_indicators():
    registry = build_default_indicator_registry()

    indicator_ids = [indicator.indicator_id for indicator in registry.list_by_category(" CORE ")]

    assert indicator_ids == ["atr", "ema", "macd", "rsi", "sma", "volume", "vwap"]


def test_indicator_metadata_is_static_and_iterable():
    indicators = build_default_indicator_registry().list_all()

    for indicator in indicators:
        assert indicator.indicator_id
        assert indicator.display_name
        assert indicator.description
        assert indicator.category in {"core", "us", "china"}
        assert indicator.is_placeholder is True
        assert list(indicator.supported_markets)
        assert list(indicator.required_data_sources)
        assert list(indicator.output_fields)


def test_placeholder_indicators_declare_expected_metadata():
    registry = build_default_indicator_registry()

    assert registry.get("macd").supports_market("us")
    assert registry.get("macd").supports_market("cn")
    assert registry.get("relative_strength").category == "us"
    assert registry.get("relative_strength").supports_market("us")
    assert registry.get("capital_flow").category == "china"
    assert registry.get("capital_flow").supports_market("cn")
    assert "main_net_inflow" in registry.get("capital_flow").output_fields


def test_indicator_registry_has_no_production_consumers():
    repo_root = Path(__file__).resolve().parents[1]
    production_files = [
        path
        for path in (repo_root / "src").rglob("*.py")
        if "indicators_registry" not in path.parts
    ]

    consumers = [
        str(path.relative_to(repo_root))
        for path in production_files
        if "indicators_registry" in path.read_text(encoding="utf-8")
    ]

    assert consumers == []
