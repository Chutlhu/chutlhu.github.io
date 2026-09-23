# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic/music website of Diego Di Carlo: a Jekyll site hosted on GitHub Pages (custom domain in `CNAME`), styled with Foundation CSS. There is no test suite or linter. The only check is that the site builds and renders correctly.

## Commands

```bash
bundle install                          # Ruby 3.4.x; Gemfile pins github-pages + jekyll-spaceship
bundle exec jekyll serve --livereload   # dev server at http://localhost:4000
bundle exec jekyll build                # build into _site/ (gitignored)
```

`_config.yml` is not hot-reloaded, so restart `jekyll serve` after editing it.

## Architecture

Nearly all content is data-driven. Pages in `_pages/` (and `index.html`) are mostly Liquid loops over YAML in `_data/` or over collections. To change what the site shows, you usually edit YAML or front matter, not HTML.

- **Collections** (declared in `_config.yml`, all `output: true`):
  - `_projects/` (layout `project`): research projects listed in `_pages/projects.html`.
  - `_musics/` (layout `music_project`): bands and projects listed in `_pages/music.html`.
  - `_pages/`: top-level pages. Each sets its own `permalink` (for example `/pubs.html`) and a `section_id` that the header nav (`_data/nav.yml`) uses to highlight the active item.
- **Gallery filtering**: the projects and music galleries filter by the `klass` front-matter field. In `_musics/` and `_data/albums.yml` it is comma-separated (`klass: electro,rap`) and becomes CSS classes. Projects/music also use `hidden`, `redirect`, `thumbnail`, `banner`, `avatar`, `links` front matter.
- **Home page** (`index.html`): shows the 3 most recent entries of `_data/news.yml`, so new items go at the **top** of that file. `_config.yml` also holds site-wide text (`short_bio`, `motto`, `interest`) and social links.
- **CV** (`_pages/cv.html`): rendered from `_data/cv.yml` (`work`, `education`, `languages`, `skills`). Entries with `hidden: true` are skipped.

### Publications (`_pages/pubs.html`)

This is the most complex page. It reads `_data/papers.yml` and `_data/talks.yml`.

- `papers.yml` has four top-level keys, and the page renders each one as a section: `article` (Journals), `inproceedings` (Conferences), `thesis`, and `other` (Misc). Entries are shown in file order. Nothing sorts them, so keep them in reverse chronological order by hand.
- Each entry can have `resources_link` (icon buttons: `name`, `icon`, `link`) and `resources_popup` (modal popups for Bibtex/Abstract with a `text` block). Icons use Font Awesome (`fa fa-*`) or Academicons (`ai ai-arxiv`, `ai ai-doi`, …).
- A Chart.js bar chart (loaded from a CDN) counts publications per year. Liquid computes the counts from each entry's `year` and from the first comma-separated part of each talk's `when` (`when: 2025, April 25`). Keep those fields in that format, or the chart breaks.
- `papers.yml` is **maintained by hand**. `scripts/bibtex2yaml.py` (run from `scripts/`; needs `bibtexparser` and `pyyaml`, venv in `scripts/venv/`) converts `_data/papers.bib` into a bare version of that YAML. It **overwrites** `papers.yml` and does not produce the `resources_*` fields or the `thesis`/`other` groupings. Do not run it on the current file. Use it only to draft new entries to copy in.

### Layouts, includes, assets

- `_layouts/default.html` is the base layout, wrapping `_includes/head.html`, `header.html`, and `footer.html`. The other layouts (`post`, `blog`, `project`, `music_project`) extend it.
- `_includes/section-header.html` is the reusable page banner (`{% include section-header.html title=... tagline=... %}`).
- Styles: `assets/css/main.sass` plus the Foundation partials in `_sass/`. Scripts: jQuery plugins in `assets/js/`, with site behavior in `app.js` and `popupbox.js`.
- Images live under `assets/images/{projects,music,banners}/…`. PDFs, slides, and posters live under `assets/pdf/` and `assets/slides_posters/`.
- The blog (`_posts/`, paginated at `blog/page:num` by `jekyll-paginate`) is currently hidden from the nav.

## Gotchas

- `jekyll-spaceship` is not on GitHub Pages' plugin whitelist. It works locally but does not run in a standard GitHub Pages build, so don't rely on its features (for example extended tables or math) for published content.
- `_data/nav.yml` links to `teaching.html`, but no teaching page exists yet.
