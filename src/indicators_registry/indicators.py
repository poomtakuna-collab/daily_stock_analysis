# -*- coding: utf-8 -*-
"""Placeholder indicator definitions."""

from __future__ import annotations

from src.indicators_registry.base import Indicator, IndicatorMetadata

SMA_INDICATOR_ID = "sma"
EMA_INDICATOR_ID = "ema"
RSI_INDICATOR_ID = "rsi"
MACD_INDICATOR_ID = "macd"
ATR_INDICATOR_ID = "atr"
VOLUME_INDICATOR_ID = "volume"
VWAP_INDICATOR_ID = "vwap"
RELATIVE_STRENGTH_INDICATOR_ID = "relative_strength"
MARKET_BREADTH_INDICATOR_ID = "market_breadth"
SECTOR_LEADERSHIP_INDICATOR_ID = "sector_leadership"
EARNINGS_TREND_INDICATOR_ID = "earnings_trend"
LIMIT_UP_INDICATOR_ID = "limit_up"
CAPITAL_FLOW_INDICATOR_ID = "capital_flow"
CHIP_DISTRIBUTION_INDICATOR_ID = "chip_distribution"
CONCEPT_BOARD_INDICATOR_ID = "concept_board"

CORE_MARKETS = frozenset({"cn", "us"})


class SMAIndicator(Indicator):
    """Skeleton for simple moving average metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=SMA_INDICATOR_ID,
        display_name="SMA",
        description="Placeholder metadata for simple moving average.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("sma",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class EMAIndicator(Indicator):
    """Skeleton for exponential moving average metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=EMA_INDICATOR_ID,
        display_name="EMA",
        description="Placeholder metadata for exponential moving average.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("ema",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class RSIIndicator(Indicator):
    """Skeleton for relative strength index metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=RSI_INDICATOR_ID,
        display_name="RSI",
        description="Placeholder metadata for relative strength index.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("rsi",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class MACDIndicator(Indicator):
    """Skeleton for MACD metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=MACD_INDICATOR_ID,
        display_name="MACD",
        description="Placeholder metadata for MACD.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("macd", "signal", "histogram"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class ATRIndicator(Indicator):
    """Skeleton for average true range metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=ATR_INDICATOR_ID,
        display_name="ATR",
        description="Placeholder metadata for average true range.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("atr",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class VolumeIndicator(Indicator):
    """Skeleton for volume metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=VOLUME_INDICATOR_ID,
        display_name="Volume",
        description="Placeholder metadata for volume analysis.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("daily_history",),
        output_fields=("volume",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class VWAPIndicator(Indicator):
    """Skeleton for VWAP metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=VWAP_INDICATOR_ID,
        display_name="VWAP",
        description="Placeholder metadata for volume weighted average price.",
        category="core",
        supported_markets=CORE_MARKETS,
        required_data_sources=("intraday_history",),
        output_fields=("vwap",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class RelativeStrengthIndicator(Indicator):
    """Skeleton for US relative strength metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=RELATIVE_STRENGTH_INDICATOR_ID,
        display_name="Relative Strength",
        description="Placeholder metadata for US relative strength versus benchmarks.",
        category="us",
        supported_markets=frozenset({"us"}),
        required_data_sources=("daily_history", "market_indices"),
        output_fields=("relative_strength",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class MarketBreadthIndicator(Indicator):
    """Skeleton for US market breadth metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=MARKET_BREADTH_INDICATOR_ID,
        display_name="Market Breadth",
        description="Placeholder metadata for US market breadth.",
        category="us",
        supported_markets=frozenset({"us"}),
        required_data_sources=("market_indices", "daily_history"),
        output_fields=("advance_decline", "breadth_score"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class SectorLeadershipIndicator(Indicator):
    """Skeleton for US sector leadership metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=SECTOR_LEADERSHIP_INDICATOR_ID,
        display_name="Sector Leadership",
        description="Placeholder metadata for US sector leadership.",
        category="us",
        supported_markets=frozenset({"us"}),
        required_data_sources=("sector_performance",),
        output_fields=("leading_sectors", "sector_rank"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class EarningsTrendIndicator(Indicator):
    """Skeleton for US earnings trend metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=EARNINGS_TREND_INDICATOR_ID,
        display_name="Earnings Trend",
        description="Placeholder metadata for US earnings trend.",
        category="us",
        supported_markets=frozenset({"us"}),
        required_data_sources=("earnings_context",),
        output_fields=("earnings_trend",),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class LimitUpIndicator(Indicator):
    """Skeleton for China limit-up metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=LIMIT_UP_INDICATOR_ID,
        display_name="Limit Up",
        description="Placeholder metadata for China limit-up behavior.",
        category="china",
        supported_markets=frozenset({"cn"}),
        required_data_sources=("daily_history",),
        output_fields=("limit_up", "limit_down"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class CapitalFlowIndicator(Indicator):
    """Skeleton for China capital flow metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=CAPITAL_FLOW_INDICATOR_ID,
        display_name="Capital Flow",
        description="Placeholder metadata for China capital flow.",
        category="china",
        supported_markets=frozenset({"cn"}),
        required_data_sources=("capital_flow",),
        output_fields=("main_net_inflow", "capital_flow_score"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class ChipDistributionIndicator(Indicator):
    """Skeleton for China chip distribution metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=CHIP_DISTRIBUTION_INDICATOR_ID,
        display_name="Chip Distribution",
        description="Placeholder metadata for China chip distribution.",
        category="china",
        supported_markets=frozenset({"cn"}),
        required_data_sources=("chip_distribution",),
        output_fields=("chip_concentration", "cost_distribution"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata


class ConceptBoardIndicator(Indicator):
    """Skeleton for China concept board metadata."""

    _metadata = IndicatorMetadata(
        indicator_id=CONCEPT_BOARD_INDICATOR_ID,
        display_name="Concept Board",
        description="Placeholder metadata for China concept board leadership.",
        category="china",
        supported_markets=frozenset({"cn"}),
        required_data_sources=("concept_board",),
        output_fields=("concept_boards", "board_strength"),
    )

    @property
    def metadata(self) -> IndicatorMetadata:
        return self._metadata
