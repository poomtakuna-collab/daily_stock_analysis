# -*- coding: utf-8 -*-
"""Registry for indicator metadata skeletons."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.indicators_registry.base import Indicator
from src.indicators_registry.indicators import (
    ATRIndicator,
    CapitalFlowIndicator,
    ChipDistributionIndicator,
    ConceptBoardIndicator,
    EMAIndicator,
    EarningsTrendIndicator,
    LimitUpIndicator,
    MACDIndicator,
    MarketBreadthIndicator,
    RSIIndicator,
    RelativeStrengthIndicator,
    SMAIndicator,
    SectorLeadershipIndicator,
    VWAPIndicator,
    VolumeIndicator,
)


class UnknownIndicatorError(KeyError):
    """Raised when a requested indicator is not registered."""


class IndicatorRegistry:
    """In-memory registry for indicator metadata skeletons.

    The registry has no production side effects. It only stores explicit
    indicator instances and returns them by normalized id, market, or category.
    """

    def __init__(self, indicators: Optional[Iterable[Indicator]] = None) -> None:
        self._indicators: Dict[str, Indicator] = {}
        for indicator in indicators or ():
            self.register(indicator)

    @staticmethod
    def _normalize_id(value: str, *, field_name: str) -> str:
        normalized = str(value or "").strip().lower()
        if not normalized:
            raise ValueError(f"{field_name} must not be empty")
        return normalized

    def register(self, indicator: Indicator) -> None:
        indicator_id = self._normalize_id(indicator.indicator_id, field_name="indicator_id")
        if indicator_id in self._indicators:
            raise ValueError(f"indicator already registered: {indicator_id}")
        self._indicators[indicator_id] = indicator

    def has(self, indicator_id: str) -> bool:
        return self._normalize_id(indicator_id, field_name="indicator_id") in self._indicators

    def get(self, indicator_id: str) -> Indicator:
        normalized = self._normalize_id(indicator_id, field_name="indicator_id")
        try:
            return self._indicators[normalized]
        except KeyError as exc:
            raise UnknownIndicatorError(normalized) from exc

    def list_all(self) -> List[Indicator]:
        return [self._indicators[indicator_id] for indicator_id in sorted(self._indicators.keys())]

    def list_for_market(self, market_id: str) -> List[Indicator]:
        normalized = self._normalize_id(market_id, field_name="market_id")
        return [
            indicator
            for indicator in self.list_all()
            if normalized in indicator.supported_markets
        ]

    def list_by_category(self, category: str) -> List[Indicator]:
        normalized = self._normalize_id(category, field_name="category")
        return [
            indicator
            for indicator in self.list_all()
            if self._normalize_id(indicator.category, field_name="category") == normalized
        ]


def build_default_indicator_registry() -> IndicatorRegistry:
    """Build the placeholder registry with core, US, and China indicators."""

    return IndicatorRegistry(
        indicators=(
            ATRIndicator(),
            CapitalFlowIndicator(),
            ChipDistributionIndicator(),
            ConceptBoardIndicator(),
            EMAIndicator(),
            EarningsTrendIndicator(),
            LimitUpIndicator(),
            MACDIndicator(),
            MarketBreadthIndicator(),
            RelativeStrengthIndicator(),
            RSIIndicator(),
            SectorLeadershipIndicator(),
            SMAIndicator(),
            VWAPIndicator(),
            VolumeIndicator(),
        ),
    )
