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
