import { readFileSync } from 'node:fs';
import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

describe('landing page content', () => {
  it('introduces the company and keeps both products distinct', () => {
    const page = readFileSync(new URL('./page.tsx', import.meta.url), 'utf8');

    assert.match(page, /ZAR HORIZON/);
    assert.match(page, /AI Business Partner/);
    assert.match(page, /AI Hacker/);
    assert.match(page, /authorised security testing/);
  });
});
