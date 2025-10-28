# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

**Mythical Person-Month** is a modernized version of Fred Brooks' classic _The Mythical Man-Month_ book. The goal is to preserve the insights and wisdom of this influential text on managing technology projects while updating the language to be more inclusive and welcoming to all readers. The original work contains valuable technical and management lessons but reflects dated assumptions that can make it uncomfortable for modern audiences.

## Development Workflow

This repo uses `just` (command runner) for all development tasks. The workflow is entirely command-line based using `just` and the GitHub CLI (`gh`).

### Requirements

- `just` - Command runner
- `gh` - GitHub CLI
- `bash` - Shell for scripts
- `markdownlint-cli2` - Markdown linting (used by CI)
- `pandoc` - Document converter (for MD to PDF conversion)

### Standard development cycle

1. `just branch <name>` - Create a new feature branch (format: `$USER/YYYY-MM-DD-<name>`)
2. Make changes and commit (last commit message becomes PR title)
3. `just pr` - Create PR, push changes, and watch checks (waits 10s for GitHub API)
4. `just merge` - Squash merge PR, delete branch, return to main, and pull latest
5. `just sync` - Return to main branch and pull latest (escape hatch)

### Additional commands

- `just` or `just list` - Show all available recipes
- `just prweb` - Open current PR in browser
- `just release <version>` - Create a GitHub release with auto-generated notes
- `just compliance_check` - Run custom repo compliance checks
- `just utcdate` - Print UTC date in ISO format (used in branch names)
- `just md2pdf <markdown_file>` - Convert a Markdown file to PDF using pandoc (aborts if PDF already exists)

### Git aliases used

The justfile assumes these git aliases exist:

- `git stp` - Show status (likely `status --short` or similar)
- `git pushup` - Push and set upstream tracking
- `git co` - Checkout

## Architecture

### Modular justfile structure

The main `justfile` imports two modules:

- `.just/compliance.just` - Custom compliance checks for repo health
- `.just/gh-process.just` - Git/GitHub workflow automation

### GitHub Actions

Six workflows run on PRs and pushes to main:

- **markdownlint** - Enforces markdown standards using `markdownlint-cli2`
- **checkov** - Security scanning for GitHub Actions
- **actionlint** - Lints GitHub Actions workflow files
- **auto-assign** - Automatically assigns issues
- **claude.yml** - Claude Code integration workflow
- **claude-code-review.yml** - Automated code review via Claude Code

### Markdown linting

Configuration in `.markdownlint.yml`:

- MD013 (line length) is disabled
- MD041 (first line h1) is disabled
- MD042 (no empty links) is disabled
- MD004 (list style) enforces dashes
- MD010 (tabs) ignores code blocks

Run locally: `markdownlint-cli2 **/*.md`

## Content Structure

### Directories

- `source_material/` - Original PDFs and text conversion of _The Mythical Man-Month_
- `chapters/` - Individual chapter files in both PDF and Markdown formats
  - Naming: `##-chapter-##-title.{md,pdf}` or `##-preface-*.{md,pdf}`
  - Front matter, contents, epilogue, notes, and index also included
- `bin/` - Python scripts for splitting the source text into chapters

### Content Processing Workflow

**Splitting chapters from source:**

- `bin/split_chapters_v2.py` - Splits source text into individual chapter files
  - Uses manually identified line number boundaries
  - Creates numbered files in `chapters/` directory

**PDF extraction (reference only):**

- Original PDFs split using `qpdf` commands (see `source_material/README.md`)
- PDF page numbers don't align with table of contents initially

## Working with Content

This is a documentation/writing project rather than a software project. The primary content will be markdown files containing the modernized text. When working on the content:

- Maintain the original structure and insights from _The Mythical Man-Month_
- Update gendered language (e.g., "man-month" → "person-month", "manpower" → "workforce")
- Preserve the technical accuracy and management wisdom
- Keep references to historical context but make them more inclusive where appropriate
- Chapter files exist in both PDF (original) and Markdown (modernized) formats

**Reference:** See `Modernization_Analysis.md` for comprehensive documentation of language modernization goals, including:

- 150+ specific instances of gendered language requiring attention
- Research evidence on the psychological impact of gendered language
- Detailed recommendations organized by category (compound terms, generic pronouns, occupational terms)
- Implementation strategy with phases and timeline
- Quality assurance checklist
