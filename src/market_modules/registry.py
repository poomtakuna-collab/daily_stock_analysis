# -*- coding: utf-8 -*-
"""Registry for market module skeletons."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.market_modules.base import MarketModule
from src.market_modules.china import CHINA_MARKET_ID, ChinaMarketModule
from src.market_modules.us import US_MARKET_ID, USMarketModule

DEFAULT_MARKET_MODULE_ID = US_MARKET_ID


class UnknownMarketModuleError(KeyError):
    """Raised when a requested market module is not registered."""


class MarketModuleRegistry:
    """In-memory registry for market modules.

    The registry has no production side effects. It only stores explicit module
    instances and returns them by normalized market id.
    """

    def __init__(
        self,
        modules: Optional[Iterable[MarketModule]] = None,
        *,
        default_market_id: str = DEFAULT_MARKET_MODULE_ID,
    ) -> None:
        self._modules: Dict[str, MarketModule] = {}
        self._default_market_id = self._normalize_market_id(default_market_id)
        for module in modules or ():
            self.register(module)

    @staticmethod
    def _normalize_market_id(market_id: str) -> str:
        normalized = str(market_id or "").strip().lower()
        if not normalized:
            raise ValueError("market_id must not be empty")
        return normalized

    @property
    def default_market_id(self) -> str:
        return self._default_market_id

    def register(self, module: MarketModule) -> None:
        market_id = self._normalize_market_id(module.market_id)
        if market_id in self._modules:
            raise ValueError(f"market module already registered: {market_id}")
        self._modules[market_id] = module

    def has(self, market_id: str) -> bool:
        return self._normalize_market_id(market_id) in self._modules

    def get(self, market_id: str) -> MarketModule:
        normalized = self._normalize_market_id(market_id)
        try:
            return self._modules[normalized]
        except KeyError as exc:
            raise UnknownMarketModuleError(normalized) from exc

    def get_default(self) -> MarketModule:
        return self.get(self._default_market_id)

    def ids(self) -> List[str]:
        return sorted(self._modules.keys())

    def modules(self) -> List[MarketModule]:
        return [self._modules[market_id] for market_id in self.ids()]


def build_default_market_module_registry(
    *,
    default_market_id: str = DEFAULT_MARKET_MODULE_ID,
) -> MarketModuleRegistry:
    """Build the placeholder registry with China and US modules registered."""

    return MarketModuleRegistry(
        modules=(ChinaMarketModule(), USMarketModule()),
        default_market_id=default_market_id,
    )
