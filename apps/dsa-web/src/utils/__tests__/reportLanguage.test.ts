import { describe, expect, it } from 'vitest';

import {
  getReportText,
  localizeKnownReportHeading,
  localizeKnownReportMarkdownLabels,
  normalizeReportLanguage,
} from '../reportLanguage';
import { getSentimentLabel } from '../../types/analysis';

describe('reportLanguage ko support', () => {
  it('normalizes ko and falls back to zh for unknown', () => {
    expect(normalizeReportLanguage('ko')).toBe('ko');
    expect(normalizeReportLanguage('en')).toBe('en');
    expect(normalizeReportLanguage('fr')).toBe('zh');
    expect(normalizeReportLanguage(undefined)).toBe('zh');
  });

  it('returns Korean report copy for ko', () => {
    const ko = getReportText('ko');
    expect(ko.keyInsights).toBe('핵심 인사이트');
    expect(ko.actionAdvice).toBe('대응 전략');
    expect(ko.fullReport).toBe('전체 분석 리포트');
  });

  it('uses English display copy for zh/en report labels', () => {
    expect(getReportText('zh').keyInsights).toBe('KEY INSIGHTS');
    expect(getReportText('en').keyInsights).toBe('KEY INSIGHTS');
  });

  it('maps known Chinese report headings to English display labels', () => {
    expect(localizeKnownReportHeading('\u5927\u76d8\u590d\u76d8')).toBe('Market Review');
    expect(localizeKnownReportHeading('\u4e00\u3001\u76d8\u9762\u603b\u89c8')).toBe('Market Overview');
    expect(localizeKnownReportHeading('\u4e8c\u3001\u6307\u6570\u7ed3\u6784')).toBe('Index Structure');
    expect(localizeKnownReportHeading('\u4e09\u3001\u677f\u5757\u4e3b\u7ebf')).toBe('Sector Themes');
    expect(localizeKnownReportHeading('\u76d8\u9762\u4fe1\u53f7')).toBe('Market Signal');
    expect(localizeKnownReportHeading('\u8fd1\u4e09\u65e5\u5e02\u573a\u7ebf\u7d22')).toBe('Recent Market Catalysts');
    expect(localizeKnownReportHeading('\u81ea\u7531\u5206\u6790\u6bb5\u843d')).toBe('\u81ea\u7531\u5206\u6790\u6bb5\u843d');
  });

  it('localizes only known markdown headings and label prefixes', () => {
    const markdown = [
      '# \u5927\u76d8\u590d\u76d8',
      '## \u4e00\u3001\u76d8\u9762\u603b\u89c8',
      '\u5e02\u573a\u4eca\u65e5\u9707\u8361\uff0c\u76d8\u9762\u603b\u89c8\u4e0d\u5e94\u5728\u6bb5\u843d\u5185\u88ab\u6539\u5199\u3002',
      '- \u76d8\u9762\u4fe1\u53f7\uff1a\u91cf\u80fd\u653e\u5927',
      '## \u8fd1\u4e09\u65e5\u5e02\u573a\u7ebf\u7d22',
    ].join('\n');

    expect(localizeKnownReportMarkdownLabels(markdown)).toBe([
      '# Market Review',
      '## Market Overview',
      '\u5e02\u573a\u4eca\u65e5\u9707\u8361\uff0c\u76d8\u9762\u603b\u89c8\u4e0d\u5e94\u5728\u6bb5\u843d\u5185\u88ab\u6539\u5199\u3002',
      '- Market Signal: \u91cf\u80fd\u653e\u5927',
      '## Recent Market Catalysts',
    ].join('\n'));
  });

  it('returns Korean sentiment labels by band', () => {
    expect(getSentimentLabel(90, 'ko')).toBe('매우 낙관');
    expect(getSentimentLabel(50, 'ko')).toBe('중립');
    expect(getSentimentLabel(10, 'ko')).toBe('매우 비관');
    expect(getSentimentLabel(90, 'en')).toBe('Very Bullish');
  });
});
