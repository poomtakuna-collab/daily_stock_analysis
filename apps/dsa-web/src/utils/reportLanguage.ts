import type { ReportLanguage } from '../types/analysis';

export const normalizeReportLanguage = (value?: string | null): ReportLanguage =>
  value === 'en' ? 'en' : value === 'ko' ? 'ko' : 'zh';

const REPORT_TEXT = {
  zh: {
    keyInsights: '核心洞察',
    noAnalysisSummary: '暂无分析结论',
    actionAdvice: '操作建议',
    noAdvice: '暂无建议',
    trendPrediction: '趋势预测',
    noPrediction: '暂无预测',
    marketSentiment: '市场情绪',
    strategyPoints: '策略点位',
    sniperLevels: '狙击点位',
    idealBuy: '理想买入',
    secondaryBuy: '二次买入',
    stopLoss: '止损价位',
    takeProfit: '止盈目标',
    noValue: '—',
    newsFeed: '资讯动态',
    relatedNews: '相关资讯',
    refresh: '刷新',
    retry: '重试',
    dismiss: '关闭',
    details: '查看详情',
    loadingNews: '加载资讯中...',
    noNews: '暂无相关资讯',
    noNewsDescription: '可稍后刷新以获取最新资讯。',
    openLink: '跳转',
    transparency: '透明度',
    traceability: '数据追溯',
    rawResult: '原始分析结果',
    analysisSnapshot: '分析快照',
    copy: '复制',
    copied: '已复制',
    recordId: '记录 ID',
    fullReport: '完整分析报告',
    loadingReport: '加载报告中...',
    loadReportFailed: '加载报告失败',
    copyMarkdownSource: '复制 Markdown 源码',
    copyPlainText: '复制纯文本',
    analysisModel: '分析模型',
    fearGreedIndex: '恐惧贪婪指数',
    boardLinkage: '板块联动',
    relatedBoards: '关联板块',
    leadingBoard: '领涨',
    laggingBoard: '领跌',
    neutralBoard: '中性',
    reanalyze: '重新分析',
  },
  en: {
    keyInsights: 'KEY INSIGHTS',
    noAnalysisSummary: 'No analysis summary yet',
    actionAdvice: 'Action Advice',
    noAdvice: 'No advice yet',
    trendPrediction: 'Trend Outlook',
    noPrediction: 'No forecast yet',
    marketSentiment: 'Market Sentiment',
    strategyPoints: 'STRATEGY POINTS',
    sniperLevels: 'Action Levels',
    idealBuy: 'Ideal Entry',
    secondaryBuy: 'Secondary Entry',
    stopLoss: 'Stop Loss',
    takeProfit: 'Take Profit',
    noValue: '—',
    newsFeed: 'NEWS FEED',
    relatedNews: 'Related News',
    refresh: 'Refresh',
    retry: 'Retry',
    dismiss: 'Close',
    details: 'View details',
    loadingNews: 'Loading news...',
    noNews: 'No related news',
    noNewsDescription: 'Refresh later to check for the latest updates.',
    openLink: 'Open',
    transparency: 'TRANSPARENCY',
    traceability: 'Data Traceability',
    rawResult: 'Raw Analysis Result',
    analysisSnapshot: 'Analysis Snapshot',
    copy: 'Copy',
    copied: 'Copied!',
    recordId: 'Record ID',
    fullReport: 'Full Analysis Report',
    loadingReport: 'Loading report...',
    loadReportFailed: 'Failed to load report',
    copyMarkdownSource: 'Copy Markdown Source',
    copyPlainText: 'Copy Plain Text',
    analysisModel: 'Model',
    fearGreedIndex: 'Fear & Greed Index',
    boardLinkage: 'BOARD LINKAGE',
    relatedBoards: 'Related Boards',
    leadingBoard: 'Leading',
    laggingBoard: 'Lagging',
    neutralBoard: 'Neutral',
    reanalyze: 'Reanalyze',
  },
  ko: {
    keyInsights: '핵심 인사이트',
    noAnalysisSummary: '분석 결론 없음',
    actionAdvice: '대응 전략',
    noAdvice: '제안 없음',
    trendPrediction: '추세 전망',
    noPrediction: '예측 없음',
    marketSentiment: '시장 심리',
    strategyPoints: '전략 가격대',
    sniperLevels: '대응 가격대',
    idealBuy: '이상적 매수가',
    secondaryBuy: '추가 매수가',
    stopLoss: '손절가',
    takeProfit: '목표가',
    noValue: '—',
    newsFeed: '뉴스 피드',
    relatedNews: '관련 뉴스',
    refresh: '새로고침',
    retry: '다시 시도',
    dismiss: '닫기',
    details: '상세 보기',
    loadingNews: '뉴스 불러오는 중...',
    noNews: '관련 뉴스 없음',
    noNewsDescription: '잠시 후 새로고침하여 최신 소식을 확인하세요.',
    openLink: '열기',
    transparency: '투명성',
    traceability: '데이터 추적',
    rawResult: '원본 분석 결과',
    analysisSnapshot: '분석 스냅샷',
    copy: '복사',
    copied: '복사됨!',
    recordId: '레코드 ID',
    fullReport: '전체 분석 리포트',
    loadingReport: '리포트 불러오는 중...',
    loadReportFailed: '리포트 불러오기 실패',
    copyMarkdownSource: 'Markdown 소스 복사',
    copyPlainText: '일반 텍스트 복사',
    analysisModel: '분석 모델',
    fearGreedIndex: '공포·탐욕 지수',
    boardLinkage: '섹터 연동',
    relatedBoards: '관련 섹터',
    leadingBoard: '강세',
    laggingBoard: '약세',
    neutralBoard: '중립',
    reanalyze: '재분석',
  },
} as const;

export const getReportText = (language?: string | null) => {
  const normalized = normalizeReportLanguage(language);
  return REPORT_TEXT[normalized === 'zh' ? 'en' : normalized];
};

const KNOWN_REPORT_HEADING_LABELS: Record<string, string> = {
  '\u5927\u76d8\u590d\u76d8': 'Market Review',
  '\u5927\u76d8\u590d\u76d8\u8be6\u60c5': 'Market Review',
  'a\u80a1\u5e02\u573a\u590d\u76d8': 'Market Review',
  'a \u80a1\u5e02\u573a\u590d\u76d8': 'Market Review',
  '\u76d8\u9762\u603b\u89c8': 'Market Overview',
  '\u6307\u6570\u7ed3\u6784': 'Index Structure',
  '\u677f\u5757\u4e3b\u7ebf': 'Sector Themes',
  '\u76d8\u9762\u4fe1\u53f7': 'Market Signal',
  '\u8fd1\u4e09\u65e5\u5e02\u573a\u7ebf\u7d22': 'Recent Market Catalysts',
  '\u590d\u76d8\u6b63\u6587': 'Review Body',
  '\u590d\u76d8\u6982\u89c8': 'Review Overview',
};

const normalizeKnownReportHeading = (value: string): string =>
  value
    .trim()
    .replace(/^#+\s*/, '')
    .replace(/[*_`~]/g, '')
    .replace(/^\s*[一二三四五六七八九十]+[、.．]\s*/, '')
    .replace(/[：:]\s*$/, '')
    .replace(/\s+/g, ' ')
    .toLowerCase();

export const localizeKnownReportHeading = (value: string): string =>
  KNOWN_REPORT_HEADING_LABELS[normalizeKnownReportHeading(value)] ?? value;

export const localizeKnownReportMarkdownLabels = (markdown: string): string =>
  markdown
    .replace(/^(\s{0,3}#{1,6}\s+)(.+?)(\s*#*\s*)$/gm, (line, prefix: string, title: string, suffix: string) => {
      const localizedTitle = localizeKnownReportHeading(title);
      return localizedTitle === title ? line : `${prefix}${localizedTitle}${suffix}`;
    })
    .replace(
      /^(\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*)?)([\u4e00-\u9fa5A-Za-z0-9\s、.．]+?)((?:\*\*)?\s*[：:])/gm,
      (line, prefix: string, label: string, suffix: string) => {
        const localizedLabel = localizeKnownReportHeading(label);
        return localizedLabel === label ? line : `${prefix}${localizedLabel}${suffix.replace(/[：:]\s*$/, ': ')}`;
      },
    );

const KNOWN_REPORT_VOCABULARY_LABELS: Record<string, string> = {
  '\u5206\u6790\u5b8c\u6210': 'Analysis Complete',
  '\u4e70\u5165': 'Buy',
  '\u5f3a\u70c8\u4e70\u5165': 'Strong Buy',
  '\u52a0\u4ed3': 'Add',
  '\u6301\u6709': 'Hold',
  '\u89c2\u671b': 'Watch',
  '\u51cf\u4ed3': 'Reduce',
  '\u5356\u51fa': 'Sell',
  '\u5f3a\u70c8\u5356\u51fa': 'Strong Sell',
  '\u4e2d\u6027': 'Neutral',
  '\u9707\u8361': 'Sideways',
  '\u770b\u6da8': 'Bullish',
  '\u770b\u591a': 'Bullish',
  '\u5f3a\u70c8\u770b\u591a': 'Strongly Bullish',
  '\u770b\u8dcc': 'Bearish',
  '\u770b\u7a7a': 'Bearish',
  '\u5f3a\u70c8\u770b\u7a7a': 'Strongly Bearish',
  '\u6570\u636e\u7f3a\u5931\uff0c\u65e0\u6cd5\u5224\u65ad': 'Insufficient Data',
  '\u6570\u636e\u7f3a\u5931,\u65e0\u6cd5\u5224\u65ad': 'Insufficient Data',
  '\u65e0\u6cd5\u5224\u65ad': 'Unknown',
  '\u98ce\u9669\u504f\u9ad8': 'Elevated Risk',
  '\u504f\u9632\u5b88': 'Defensive',
};

const normalizeKnownReportVocabulary = (value: string): string =>
  value
    .trim()
    .replace(/^[\s"'“”‘’`*_]+|[\s"'“”‘’`*_.。；;!！]+$/g, '')
    .replace(/\s+/g, ' ')
    .toLowerCase();

export const localizeKnownReportVocabulary = (value?: string | null): string => {
  const text = value?.trim();
  if (!text) {
    return value || '';
  }
  return KNOWN_REPORT_VOCABULARY_LABELS[normalizeKnownReportVocabulary(text)] ?? text;
};
