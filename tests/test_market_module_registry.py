# -*- coding: utf-8 -*-
"""Tests for the market module registry skeleton."""

import pytest

from src.market_modules import (
    ChinaMarketModule,
    MarketModuleRegistry,
    USMarketModule,
    UnknownMarketModuleError,
    build_default_market_module_registry,
)


def test_default_registry_registers_china_and_us_modules():
    registry = build_default_market_module_registry()

    assert registry.ids() == ["cn", "us"]
    assert isinstance(registry.get("cn"), ChinaMarketModule)
    assert isinstance(registry.get("us"), USMarketModule)


def test_lookup_normalizes_market_id():
    registry = build_default_market_module_registry()

    assert registry.get(" US ").market_id == "us"
    assert registry.get(" CN ").market_id == "cn"


def test_default_module_selection_is_us():
    registry = build_default_market_module_registry()

    default_module = registry.get_default()

    assert default_module.market_id == "us"
    assert default_module.default_symbols == ("MSFT", "AAPL", "NVDA")
    assert default_module.is_placeholder is True


def test_placeholder_modules_declare_market_specific_capabilities():
    registry = build_default_market_module_registry()

    assert registry.get("cn").supports("chip_distribution")
    assert registry.get("cn").supports("capital_flow")
    assert registry.get("us").supports("sec_filings")
    assert registry.get("us").supports("social_sentiment")


def test_unknown_market_raises_registry_error():
    registry = build_default_market_module_registry()

    with pytest.raises(UnknownMarketModuleError):
        registry.get("hk")


def test_duplicate_registration_is_rejected():
    registry = MarketModuleRegistry([USMarketModule()])

    with pytest.raises(ValueError, match="already registered"):
        registry.register(USMarketModule())


def test_custom_default_module_selection_is_supported_for_tests_only():
    registry = build_default_market_module_registry(default_market_id="cn")

    assert registry.default_market_id == "cn"
    assert registry.get_default().market_id == "cn"
