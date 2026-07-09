# -*- coding: utf-8 -*-
"""Base contract for data source skeletons."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class DataSourceMetadata:
    """Static metadata exposed by a data source skeleton."""

    source_id: str
    display_name: str
    description: str
    supported_markets: FrozenSet[str]
    supported_capabilities: FrozenSet[str]
    is_realtime: bool = False
    is_free: bool = True
    requires_api_key: bool = False
    placeholder: bool = True


class DataSource(ABC):
    """Base contract for future market-specific data source providers.

    This contract is intentionally metadata-only. Production analyzers,
    strategies, prompts, and provider routing should continue using their
    existing paths until data source selection is wired in a later sprint.
    """

    @property
    @abstractmethod
    def metadata(self) -> DataSourceMetadata:
        """Return static data source metadata."""

    @property
    def source_id(self) -> str:
        return self.metadata.source_id

    @property
    def display_name(self) -> str:
        return self.metadata.display_name

    @property
    def description(self) -> str:
        return self.metadata.description

    @property
    def supported_markets(self) -> FrozenSet[str]:
        return self.metadata.supported_markets

    @property
    def supported_capabilities(self) -> FrozenSet[str]:
        return self.metadata.supported_capabilities

    @property
    def is_realtime(self) -> bool:
        return self.metadata.is_realtime

    @property
    def is_free(self) -> bool:
        return self.metadata.is_free

    @property
    def requires_api_key(self) -> bool:
        return self.metadata.requires_api_key

    @property
    def is_placeholder(self) -> bool:
        return self.metadata.placeholder

    def supports_market(self, market_id: str) -> bool:
        """Return whether this source declares support for a market."""

        return str(market_id or "").strip().lower() in self.supported_markets

    def supports_capability(self, capability: str) -> bool:
        """Return whether this source declares a placeholder capability."""

        return str(capability or "").strip().lower() in self.supported_capabilities
