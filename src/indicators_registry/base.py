# -*- coding: utf-8 -*-
"""Base contract for indicator metadata skeletons."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import FrozenSet, Tuple


@dataclass(frozen=True)
class IndicatorMetadata:
    """Static metadata exposed by an indicator skeleton."""

    indicator_id: str
    display_name: str
    description: str
    category: str
    supported_markets: FrozenSet[str]
    required_data_sources: Tuple[str, ...]
    output_fields: Tuple[str, ...]
    placeholder: bool = True


class Indicator(ABC):
    """Base contract for future indicator implementations.

    This contract is intentionally metadata-only. It does not define
    calculation hooks and should not be consumed by analyzers or strategies
    until indicator selection is wired in a later sprint.
    """

    @property
    @abstractmethod
    def metadata(self) -> IndicatorMetadata:
        """Return static indicator metadata."""

    @property
    def indicator_id(self) -> str:
        return self.metadata.indicator_id

    @property
    def display_name(self) -> str:
        return self.metadata.display_name

    @property
    def description(self) -> str:
        return self.metadata.description

    @property
    def category(self) -> str:
        return self.metadata.category

    @property
    def supported_markets(self) -> FrozenSet[str]:
        return self.metadata.supported_markets

    @property
    def required_data_sources(self) -> Tuple[str, ...]:
        return self.metadata.required_data_sources

    @property
    def output_fields(self) -> Tuple[str, ...]:
        return self.metadata.output_fields

    @property
    def is_placeholder(self) -> bool:
        return self.metadata.placeholder

    def supports_market(self, market_id: str) -> bool:
        """Return whether this indicator declares support for a market."""

        return str(market_id or "").strip().lower() in self.supported_markets
