# -*- coding: utf-8 -*-
"""Market module skeletons.

Sprint 13 intentionally keeps this package disconnected from production
analysis flows. The registry is importable and testable, but analyzers,
prompts, strategies, and provider routing still use their existing paths.
"""

from src.market_modules.base import MarketModule, MarketModuleMetadata
from src.market_modules.china import ChinaMarketModule
from src.market_modules.registry import (
    DEFAULT_MARKET_MODULE_ID,
    MarketModuleRegistry,
    UnknownMarketModuleError,
    build_default_market_module_registry,
)
from src.market_modules.us import USMarketModule

__all__ = [
    "ChinaMarketModule",
    "DEFAULT_MARKET_MODULE_ID",
    "MarketModule",
    "MarketModuleMetadata",
    "MarketModuleRegistry",
    "UnknownMarketModuleError",
    "USMarketModule",
    "build_default_market_module_registry",
]
