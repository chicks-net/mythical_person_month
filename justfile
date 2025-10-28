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

	if [[ -e "$output_pdf" ]]; then
		echo "{{RED}}$output_pdf {{BLUE}}already exists, aborting.{{NORMAL}}"
		exit 3
	fi

	set -x # enable tracing
	pandoc {{ markdown_file }} -o "$output_pdf" -V geometry:margin=0.9in

# TODO: can we get side by side comparisons?
