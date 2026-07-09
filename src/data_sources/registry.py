# -*- coding: utf-8 -*-
"""Registry for data source skeletons."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.data_sources.base import DataSource
from src.data_sources.sources import (
    EastmoneyDataSource,
    InsiderDataSource,
    SECDataSource,
    TushareDataSource,
    YahooFinanceDataSource,
)


class UnknownDataSourceError(KeyError):
    """Raised when a requested data source is not registered."""


class DataSourceRegistry:
    """In-memory registry for data source metadata skeletons.

    The registry has no production side effects. It only stores explicit source
    instances and returns them by normalized source id or market id.
    """

    def __init__(self, sources: Optional[Iterable[DataSource]] = None) -> None:
        self._sources: Dict[str, DataSource] = {}
        for source in sources or ():
            self.register(source)

    @staticmethod
    def _normalize_id(value: str, *, field_name: str) -> str:
        normalized = str(value or "").strip().lower()
        if not normalized:
            raise ValueError(f"{field_name} must not be empty")
        return normalized

    def register(self, source: DataSource) -> None:
        source_id = self._normalize_id(source.source_id, field_name="source_id")
        if source_id in self._sources:
            raise ValueError(f"data source already registered: {source_id}")
        self._sources[source_id] = source

    def has(self, source_id: str) -> bool:
        return self._normalize_id(source_id, field_name="source_id") in self._sources

    def get(self, source_id: str) -> DataSource:
        normalized = self._normalize_id(source_id, field_name="source_id")
        try:
            return self._sources[normalized]
        except KeyError as exc:
            raise UnknownDataSourceError(normalized) from exc

    def list_all(self) -> List[DataSource]:
        return [self._sources[source_id] for source_id in sorted(self._sources.keys())]

    def list_for_market(self, market_id: str) -> List[DataSource]:
        normalized = self._normalize_id(market_id, field_name="market_id")
        return [
            source
            for source in self.list_all()
            if normalized in source.supported_markets
        ]


def build_default_data_source_registry() -> DataSourceRegistry:
    """Build the placeholder registry with US and China sources registered."""

    return DataSourceRegistry(
        sources=(
            EastmoneyDataSource(),
            InsiderDataSource(),
            SECDataSource(),
            TushareDataSource(),
            YahooFinanceDataSource(),
        ),
    )
