# Diego Di Carlo - Personal Website

This is the source code for Diego Di Carlo's personal website, built with Jekyll and hosted on GitHub Pages.

## Tech Stack

- **Jekyll** - Static site generator
- **Foundation CSS** - Frontend framework
- **Ruby 3.4.1** - Runtime environment
- **GitHub Pages** - Hosting

## Running Locally

### Prerequisites

- Ruby 3.4.1 (or compatible version)
- Bundler gem

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/chutlhu/chutlhu.github.io.git
   cd chutlhu.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Build and serve the site:
   ```bash
   bundle exec jekyll serve --livereload
   ```

4. Visit `http://localhost:4000` in your browser

## Project Structure

- `_includes/` - Reusable HTML components
- `_layouts/` - Page templates
- `_posts/` - Blog posts
- `_projects/` - Research projects
- `_musics/` - Music projects
- `_data/` - Data files (CV, navigation, etc.)
- `css/`, `javascripts/`, `images/` - Assets

## Credits

Heavily inspired by the website of [Robin Scheibler](https://github.com/fakufaku/fakufaku.github.io). locally with

    bundle exec jekyll serve
