# project justfile

import? '.just/compliance.just'
import? '.just/gh-process.just'

# list recipes (default works without naming it)
[group('example')]
list:
	just --list
	@echo "{{GREEN}}Your justfile is waiting for more scripts and snippets{{NORMAL}}"

# build PDFs from Markdown files
[group('book_project')]
md2pdf markdown_file:
	#!/usr/bin/env bash
	set -euo pipefail # strict mode

	# deal with dirname of markdown_file
	output_pdf="$(dirname {{ markdown_file }})/$(basename {{ markdown_file }} .md).pdf"

	# skipping wait seconds during development, but this might be nicer for users eventually
	WAIT_SECONDS=0
	if [[ -e "$output_pdf" ]]; then
		echo "{{RED}}$output_pdf {{BLUE}}already exists, deleting in {{RED}}$WAIT_SECONDS {{BLUE}}seconds.{{NORMAL}}"
		sleep "$WAIT_SECONDS"
		rm "$output_pdf"
	fi

	set -x # enable tracing
	pandoc {{ markdown_file }} -o "$output_pdf" --pdf-engine=typst \
		-V geometry:margin=0.9in \
		-V mainfont="Libertinus Serif"

# build ALL PDFs from Markdown files
[group('book_project')]
generate_pdfs:
	#!/usr/bin/env bash
	set -euo pipefail # strict mode

	for file in chapters/*.md; do
		just md2pdf "$file"
	done

# TODO: can we get side by side comparisons?
