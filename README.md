# Md Muntaqim Meherab — academic portfolio

A self-contained academic website for https://meherabb.github.io/.

## Fastest way to publish

1. Open https://github.com/meherabb/meherabb.github.io and select the `main` branch.
2. Download the supplied `index.html`. Keep that exact filename.
3. Use **Add file → Upload files** to upload `index.html` to the repository root, replacing the existing `index.html`. Commit the change. Do not upload the ZIP itself, or put the page inside an extra folder.
4. Go to **Settings → Pages**. Your repository already contains a static Pages deployment workflow. Set **Build and deployment → Source → GitHub Actions** to use that workflow.
5. Check the repository's **Actions** tab for a successful deployment, then use **Visit site** in Pages settings. The intended address is https://meherabb.github.io/.

The inspected repository was private. On GitHub Free, Pages requires a public repository. If applicable, use a public repository containing only the website files; a qualifying paid plan can support private source repositories. This package does not change your account, repository visibility, or Pages settings.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## What you need to upload

Only `index.html` is needed with JavaScript enabled or disabled. The portrait, styles, diagrams, scripts, favicon, and downloadable PDF CV are embedded in that single file. There is no installation, build command, external font, tracking service, or runtime API dependency. All website sections are present in the static HTML.

The ZIP also contains:

- `Md_Muntaqim_Meherab_CV.pdf` — the public CV embedded in the website.
- `Md_Muntaqim_Meherab_CV.tex` — editable source for that public CV.
- `.nojekyll` — useful if you instead choose branch-based Pages publishing.
- `CONTENT_NOTES.md` — sources and editorial decisions.
- `update_embedded_assets.py` — optional local helper for changing the photo or embedded CV later.

You can upload these files too, but the single page is sufficient. Download and open `index.html` in your normal browser to preview it before uploading.

## Features

- Responsive desktop, tablet, and mobile layout.
- Original supplied portrait, with layout cropping only.
- Research focus and two illustrated featured projects.
- Nine publications and research outputs, with topic filters.
- Google Scholar, LinkedIn, GitHub, and institutional email links.
- Research and education, peer review, leadership, honors, and books.
- Light and dark themes, keyboard navigation, skip link, and reduced-motion support.
- PDF CV download, metadata for search engines, canonical URL, and Person structured data.

## Edit the content

The page has clear HTML sections: `about`, `research`, `publications`, `background`, `writing`, and `contact`. Edit visible content directly in `index.html`. Publication items are static `<article class="publication">` elements; `data-area` controls their filter membership. The filters do not make network requests.

Update the visible date and copyright year when appropriate. If publications are added or removed, update the initial `pub-count` text; filtering then calculates counts automatically. Preserve the two featured publication IDs, or update their corresponding links.

The PDF is embedded in both download links. Replacing only the separate PDF file does not change those embedded copies. After updating the PDF, run the helper below in this folder and upload the updated `index.html`:

```bash
python3 update_embedded_assets.py --cv Md_Muntaqim_Meherab_CV.pdf
```

For a replacement JPEG portrait:

```bash
python3 update_embedded_assets.py --photo new-portrait.jpg
```

To change the website domain, update the canonical URL, `og:url`, structured-data `url`, print URL, and this README. No `CNAME` is included because no custom domain was specified.
