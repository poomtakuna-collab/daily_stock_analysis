import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { historyApi } from '../../../api/history';
import { ReportMarkdown } from '../ReportMarkdown';

vi.mock('../../../api/history', () => ({
  historyApi: {
    getMarkdown: vi.fn(),
  },
}));

describe('ReportMarkdown', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('uses localized copy labels for English reports', async () => {
    vi.mocked(historyApi.getMarkdown).mockResolvedValue('# Full report');

    render(
      <ReportMarkdown
        recordId={1}
        stockName="Apple"
        stockCode="AAPL"
        reportLanguage="en"
        onClose={() => {}}
      />
    );

    expect(await screen.findByRole('button', { name: 'Copy Markdown Source' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Copy Plain Text' })).toBeInTheDocument();
  });

  it('localizes known Chinese market review headings without rewriting paragraph text', async () => {
    vi.mocked(historyApi.getMarkdown).mockResolvedValue([
      '# \u5927\u76d8\u590d\u76d8',
      '## \u4e00\u3001\u76d8\u9762\u603b\u89c8',
      '\u8fd9\u662f\u4e00\u6bb5\u81ea\u7531\u5206\u6790\uff0c\u76d8\u9762\u603b\u89c8\u5e94\u4fdd\u6301\u539f\u6587\u3002',
      '### \u4e8c\u3001\u6307\u6570\u7ed3\u6784',
      '- \u76d8\u9762\u4fe1\u53f7\uff1a\u91cf\u80fd\u653e\u5927',
      '## \u8fd1\u4e09\u65e5\u5e02\u573a\u7ebf\u7d22',
    ].join('\n'));

    render(
      <ReportMarkdown
        recordId={2}
        stockName="Market Review"
        stockCode="market_review"
        reportLanguage="zh"
        onClose={() => {}}
      />,
    );

    expect(await screen.findByRole('heading', { name: 'Market Review' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: 'Market Overview' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: 'Index Structure' })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: 'Recent Market Catalysts' })).toBeInTheDocument();
    expect(screen.getByText(/Market Signal/)).toBeInTheDocument();
    expect(screen.getByText(/\u8fd9\u662f\u4e00\u6bb5\u81ea\u7531\u5206\u6790/)).toBeInTheDocument();
  });
});
