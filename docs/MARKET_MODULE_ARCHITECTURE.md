# Market Module Architecture

This document defines the target architecture for evolving the project into a Core Analysis Engine with market-specific modules. The goal is not to replace one market with another. The goal is to keep market-independent analysis in the core engine while moving market rules, data capabilities, and market-specific reasoning into explicit modules.

## Target Architecture

The long-term architecture should be organized around four layers:

1. Core Analysis Engine
2. Market Modules
3. Shared Market-Configurable Capabilities
4. Provider Capability Adapters

The Core Analysis Engine owns orchestration, generic analytics, LLM execution, structured-output handling, validation, and data-quality guardrails. Market Modules provide the market-specific assumptions, rules, metrics, prompt fragments, tool policies, calendars, and provider capabilities needed by the core.

Each market module should expose a consistent capability contract, for example:

- Market identity and labels
- Symbol detection and normalization rules
- Trading calendar and session rules
- Trading mechanics such as settlement, price limits, circuit breakers, and lot rules
- Default indices and benchmark baskets
- Supported market metrics
- Fundamental and intelligence sources
- Prompt fragments and role guidance
- Strategy availability and market tags
- Tool availability and tool descriptions
- Provider capability mapping

The core should call capabilities through market-aware interfaces instead of branching directly on hardcoded region names.

The initial registry skeleton is intentionally importable and testable only. It
must not be wired into production analysis, provider routing, prompts,
strategies, runtime defaults, Ollama logic, or structured-output handling until
later migration phases.

## Core Analysis

Core Analysis includes capabilities that remain valid across markets when supplied with normalized market data.

Core-owned responsibilities:

- Analysis orchestration for single-stock analysis, market review, agents, reports, alerts, and scheduled jobs
- OHLCV normalization and historical data handling
- Market-independent indicators such as moving averages, MACD, RSI, KDJ, CCI, support and resistance, trend state, and volume analysis
- Generic signal scoring and data-quality checks
- LLM provider routing and execution
- Structured-output parsing, validation, compatibility handling, and fallback behavior
- Decision normalization and guardrails that do not depend on a specific market mechanic
- Generic alert engine behavior
- Generic provider fallback framework
- Generic tool registry and execution framework
- Report rendering and persistence contracts

Core should not own market-specific ideas such as A-share chip distribution, dragon-tiger list, US SEC filing semantics, US insider transactions, A-share price-limit breadth, or US volatility/rate regime metrics.

## China Market Module

The China Market Module should own A-share and China-specific assumptions.

China-owned responsibilities:

- A-share symbol rules and normalization
- A-share trading rules, including T+1 assumptions where used by analysis
- Daily price-limit semantics, including limit-up and limit-down breadth
- Main-force capital flow
- Chip distribution
- Dragon-tiger list
- Boards, concepts, and China-specific sector/concept taxonomy
- A-share market breadth statistics
- China-specific market review metrics and news queries
- China-specific prompt fragments and role guidance
- China-specific strategy tags and strategy availability
- China provider capabilities such as Tushare, Akshare, Efinance, Pytdx, and Baostock paths where applicable

The module should provide these capabilities through interfaces rather than letting core analyzers or tools assume that these concepts exist for every market.

## US Market Module

The US Market Module should own US-equity-specific assumptions and data capabilities.

US-owned responsibilities:

- US ticker symbol rules and normalization, including support for common class-share formats where applicable
- US trading sessions, pre-market and after-hours awareness, and settlement/session guidance
- US index and benchmark baskets such as S&P 500, Nasdaq Composite, Nasdaq 100, Dow Jones, Russell 2000, and sector ETFs where supported
- US market mechanics such as market-wide circuit breakers instead of daily price-limit assumptions
- SEC filing context
- Earnings calendar, guidance, analyst revisions, and institutional ownership context where available
- Insider activity context such as Form 4-style signals where available
- US social and alternative sentiment sources where configured
- US sector, industry, volatility, rates, and macro regime metrics where available
- US-specific prompt fragments and role guidance
- US-specific strategy tags and strategy availability
- US provider capabilities such as YFinance, Finnhub, Alpha Vantage, Longbridge, and other US/global adapters where applicable

The US module should be additive. Missing US capabilities should be represented explicitly as unavailable rather than silently mapped to China-specific concepts.

## Shared Market-Configurable Capabilities

Some capabilities are shared across markets but need market-specific configuration.

Shared configurable responsibilities:

- Market profile metadata
- Market labels and display names
- Default ticker examples
- Default benchmark indices
- Currency and turnover units
- Calendar and timezone configuration
- Trading-rule descriptions
- Market review strategy blueprints
- News and intelligence source templates
- Provider priority and fallback policy
- Technical scoring thresholds
- Alert thresholds and enabled alert dimensions
- Market Light dimensions
- Tool descriptions and examples
- Agent role descriptions and market-specific prompt fragments
- Strategy catalog tags and applicability filters

These should be modeled as configuration or module-provided metadata, not duplicated inside core logic.

## Capability Matrix

| Capability | Current implementation | Target category | Dependencies | Move to market module? | Migration difficulty | Recommended order |
| --- | --- | --- | --- | --- | --- | --- |
| Market detection | `src/market_context.py` hardcodes suffix and regex rules | Shared market-configurable | Symbol format, region labels | Partially; rules per market | Medium | 1 |
| Market prompt guidelines | `src/market_context.py` embeds market-specific wording | Shared market-configurable | Prompt assembly | Yes, as module prompt fragments | Medium | 6 |
| Market profiles | `src/core/market_profile.py` defines profile data | Shared market-configurable | Market review, news, metrics | Yes, profile data per module | Medium | 1 |
| Strategy blueprints | `src/core/market_strategy.py` stores market blueprints | Shared market-configurable | Market review prompt/report | Yes, blueprint data per module | Medium | 2 |
| Market review orchestration | `src/market_analyzer.py` fetches overview and builds reviews | Core Analysis | Data manager, profiles, LLM | Keep core; inject market capabilities | High | 4 |
| Main indices | `MarketAnalyzer` and provider manager fetch by region | Shared market-configurable | Providers, region profile | Yes, benchmark baskets per module | Medium | 3 |
| A-share market stats | Market stats include up/down/flat, limit-up/down, turnover | China Market Module | China providers | Yes | Medium | 4 |
| Sector rankings | Market tools and analyzer expose mostly China-oriented rankings | China now; shared interface later | Provider rankings | Yes, with market-specific implementations | Medium | 4 |
| Concept rankings | Market analyzer/provider path exposes concept rankings | China Market Module | China concept taxonomy | Yes | Medium | 4 |
| Market Light dimensions | `src/schemas/market_light.py` uses breadth, index, and limit | Shared market-configurable | Snapshots, alerts, history | Partially; dimensions per module | High | 5 |
| Market Light service | `src/services/market_light_service.py` calls `MarketAnalyzer(region)` | Core Analysis | Snapshot schema, review history | Keep core; inject evaluator | Medium | 5 |
| Market Light alerts | `src/services/market_light_alerts.py` handles status/drop rules | Core Analysis | Calendar, snapshots | Keep core; externalize dimensions/labels | Medium | 5 |
| Technical indicators | `src/stock_analyzer.py` and `src/services/alert_indicators.py` | Core Analysis | OHLCV data | No | Low | 2 |
| Technical thresholds | Scoring uses BIAS, volume, support, and trend heuristics | Shared market-configurable | Config, historical bars | Keep core; thresholds per market | Medium | 3 |
| Chip distribution | Agent tools and technical/intelligence usage | China Market Module | China providers | Yes | Medium | 7 |
| Capital flow | Agent tools and intelligence context | China Market Module | China flow providers | Yes | Medium | 7 |
| Dragon-tiger and boards | Fundamental context blocks and adapters | China Market Module | Akshare/CN metadata | Yes | Medium | 7 |
| Fundamental context bundle | Data tools and fundamental adapters build mixed blocks | Shared market-configurable | China and US adapters | Interface in core; blocks per module | High | 6 |
| YFinance fundamentals | YFinance adapter supports US/HK-style fundamentals | US Market Module | YFinance | Yes | Medium | 6 |
| Akshare fundamentals | Akshare adapter parses China-specific fundamentals | China Market Module | Akshare | Yes | Medium | 6 |
| Realtime quotes | Data tools and provider manager | Core Analysis | Provider routing | Keep core; route by module capabilities | Medium | 3 |
| Daily history | Data tools and provider manager | Core Analysis | Provider routing | Keep core; route by module capabilities | Medium | 3 |
| Provider fallback | Provider manager coordinates multiple providers | Core Analysis | Provider classes, capability checks | Keep core; capabilities per module | High | 3 |
| China providers | Tushare, Akshare, Efinance, Pytdx, Baostock paths | China Market Module | China market APIs | Yes | High | 7 |
| US providers | YFinance, Finnhub, Alpha Vantage, Longbridge paths | US Market Module | US/global APIs | Yes | High | 8 |
| Intelligence search | Intelligence service and search tools | Shared market-configurable | Source templates, market filters | Source templates per module | Medium | 6 |
| US social sentiment | Social sentiment service activates for US tickers | US Market Module | Social and alternative data sources | Yes | Low-Medium | 8 |
| Agent runtime | Base agent orchestration, JSON parsing, tool execution | Core Analysis | LLM provider, tool registry | No | Medium | 6 |
| Agent identities | Agent role descriptions and examples | Shared market-configurable | Prompt text, selected market | Yes, as prompt fragments | Medium | 6 |
| Decision schema prompt | Decision agent structured JSON wording | Core Analysis | Structured output compatibility | Do not move yet | High | 9 |
| Tool descriptions | Agent tool descriptions and examples | Shared market-configurable | Tool registry | Market-aware descriptions later | Low | 6 |
| Strategy catalog | `strategies/*.yaml` mixes generic and market-specific tactics | Core + market modules | Strategy loader and prompt usage | Add tags, then split | Medium | 7 |
| Limit-up/down strategies | Price-limit and emotion-cycle assumptions | China Market Module | A-share trading rules | Yes | Medium | 7 |
| Generic technical strategies | Trend, MA, volume breakout, box, and oscillator logic | Core Analysis | Indicators and OHLCV | No | Low | 2 |
| Event and growth strategies | Event-driven, repricing, and growth-quality logic | Shared market-configurable | Fundamentals, news, events | Keep shared with market taxonomies | Medium | 7 |
| Trading rules | Rules are scattered through profiles and prompts | Shared market-configurable | Market context, calendar, prompts | Yes, rules per module | High | 1 |
| Trading calendar | Calendar checks exist in services and runtime assumptions | Shared market-configurable | Region, timezone, holidays | Yes, calendar adapter per module | High | 5 |
| Currency and units | Market analyzer formats units by region | Shared market-configurable | Region profile | Move to market profile | Low | 4 |

## Migration Order

1. Define the market module contract without changing behavior.
2. Move market profile data, symbol rules, trading rules, labels, currencies, and benchmark baskets behind a registry.
3. Convert provider routing into explicit market capability lookup.
4. Split market metrics into core metrics and module-owned metrics.
5. Make Market Light dimensions market-configurable before expanding market coverage.
6. Move prompt fragments, role descriptions, tool descriptions, and source templates into market-aware configuration while preserving current outputs.
7. Add strategy tags for core, China-only, US-only, and shared-configurable strategies.
8. Move China-only capabilities behind the China module: chip distribution, capital flow, dragon-tiger, concepts, boards, and limit-up/down breadth.
9. Add or formalize US module capabilities: SEC context, earnings, analyst and insider context, social sentiment, sector ETF breadth, volatility, rates, and US macro regime.
10. Evolve schemas only after market modules exist and consumers can handle market-specific optional blocks.

## Blockers and Risks

- `MarketOverview` currently mixes generic market-review fields with A-share-specific fields.
- `MarketLight` currently has a fixed dimension model that includes a price-limit dimension not valid for all markets.
- Fundamental context blocks share one bundle shape while the meaning and availability differ by market.
- Agent prompts include market-specific evidence while some prompts are also structured-output-sensitive.
- Provider fallback behaves like a capability system but is not yet modeled as one.
- Strategy YAML files mix market-independent technical logic with market-specific trading culture and market mechanics.
- Calendar, session, currency, and trading-rule assumptions are spread across prompt text, profiles, services, and tools.
- Silently mapping missing US capabilities to China-specific concepts would produce misleading analysis.

## Structured Output Rule

Do not change structured output schemas until market modules exist.

In particular, do not change decision dashboard schemas, agent JSON contracts, Market Light persisted schemas, or report payload contracts as part of the initial market-module extraction. Schema changes should happen only after the core can request market-specific capabilities explicitly and downstream consumers can handle optional market-specific blocks.
