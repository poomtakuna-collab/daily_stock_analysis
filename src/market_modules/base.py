# -*- coding: utf-8 -*-
"""Base contract for market module skeletons."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import FrozenSet, Iterable, Tuple


@dataclass(frozen=True)
class MarketModuleMetadata:
    """Static metadata exposed by a market module skeleton."""

    market_id: str
    display_name: str
    default_symbols: Tuple[str, ...]
    capabilities: FrozenSet[str]
    indicators: Tuple[str, ...] = ()
    data_sources: Tuple[str, ...] = ()
    review_sections: Tuple[str, ...] = ()
    llm_features: Tuple[str, ...] = ()
    placeholder: bool = True


class MarketModule(ABC):
    """Base contract for future market-specific analysis modules.

    This contract is intentionally metadata-only for the initial skeleton.
    Production analyzers should not depend on it until module capabilities are
    wired in a later sprint.
    """

    @property
    @abstractmethod
    def metadata(self) -> MarketModuleMetadata:
        """Return static module metadata."""

    @property
    def market_id(self) -> str:
        return self.metadata.market_id

    @property
    def display_name(self) -> str:
        return self.metadata.display_name

    @property
    def default_symbols(self) -> Tuple[str, ...]:
        return self.metadata.default_symbols

    @property
    def capabilities(self) -> FrozenSet[str]:
        return self.metadata.capabilities

    @property
    def is_placeholder(self) -> bool:
        return self.metadata.placeholder

    def supports(self, capability: str) -> bool:
        """Return whether this module declares a placeholder capability."""

        return capability.strip().lower() in self.capabilities

    def supported_indicators(self) -> Iterable[str]:
        """Return placeholder indicators declared by this module."""

        return self.metadata.indicators

    def supported_data_sources(self) -> Iterable[str]:
        """Return placeholder data sources declared by this module."""

        return self.metadata.data_sources

    def supported_review_sections(self) -> Iterable[str]:
        """Return placeholder review sections declared by this module."""

        return self.metadata.review_sections

    def supported_llm_features(self) -> Iterable[str]:
        """Return placeholder LLM features declared by this module."""

        return self.metadata.llm_features
