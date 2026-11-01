# Articles (public Lighthouse Letters)

One file per letter: `YYYY-MM-DD-slug.html`. Top lines are settings, then a line with `---`, then the letter body as HTML
(the same body as the Kajabi archive post, without the first "The Lighthouse Letter / Issue / date" paragraph).

    title: NCAA Recruiting Is Changing
    date: 2026-10-25
    issue: 6
    description: One or two sentences for Google and the Articles list (under 160 characters).
    ---
    <p>...</p>

gen.py turns each file into /articles/<slug> and lists them, newest first, on /articles. They also go into the sitemap.

Labels (from Nov 3, 2026, Brad's rule):
- Weekly letters (Tuesdays from Nov 3, 2026) add `series: weekly` and restart numbering: Nov 3 is `issue: 1`, then 2, 3... They show "Lighthouse Weekly Letter · Issue #N · date".
- Everything else (Issues 1-8 and any in-between articles) shows only the date above the title. `issue:` is optional for these.
