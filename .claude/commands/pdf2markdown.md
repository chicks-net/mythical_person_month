Convert the specified chapter PDF file to a Markdown file in the same directory.

Follow these steps:

1. Extract text from the PDF using `pdftotext`
2. Format as proper Markdown with appropriate headings
3. Add footnotes for references
4. Format quotes as blockquotes
5. Run `markdownlint-cli2` to check compliance
6. Fix any linting errors

Maintain the original language.  Don't try to get ahead of the updates.  We need
to have the original language for accurate comparisons.

Ensure the output passes all markdownlint checks.
