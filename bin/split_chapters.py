#!/usr/bin/env python3
"""
Split The Mythical Man-Month source text into individual chapter files.
"""

import re
from pathlib import Path

def normalize_filename(title):
    """Convert chapter title to filename-friendly format."""
    return (title.lower()
            .replace(' ', '-')
            .replace(',', '')
            .replace('?', '')
            .replace('"', '')
            .replace("'", '')
            .replace('—', '-')
            .replace(':', ''))

def find_chapter_starts(lines):
    """Find all chapter start positions by looking for chapter number patterns."""
    chapter_starts = []

    for i in range(len(lines) - 5):
        line = lines[i].strip()

        # Pattern 1: Title with spaces, then number, blank, number, title without spaces
        # Example: "The Tar Pit" / "1" / "" / "1" / "TheTarPit"
        if i > 260 and len(line) > 5 and any(c.isalpha() for c in line):
            if i + 4 < len(lines):
                line1 = lines[i + 1].strip()
                line2 = lines[i + 2].strip()
                line3 = lines[i + 3].strip()
                line4 = lines[i + 4].strip()

                # Check if line1 is a number, line2 is empty, line3 is same number
                if re.match(r'^\d{1,2}$', line1) and line2 == '' and line1 == line3:
                    chapter_num = int(line1)
                    if 1 <= chapter_num <= 19:
                        # line4 should be title without spaces
                        if line4.replace(' ', '').lower() == line.replace(' ', '').lower():
                            chapter_starts.append((i, chapter_num, line))
                            continue

        # Pattern 2: Number, then title, blank, number, title without spaces
        # Example: "2" / "The Mythical Man-Month" / "" / "2" / "The Mythical Man-Month"
        if re.match(r'^\d{1,2}$', line) and i + 4 < len(lines):
            chapter_num = int(line)
            if 1 <= chapter_num <= 19:
                line1 = lines[i + 1].strip()
                line2 = lines[i + 2].strip()
                line3 = lines[i + 3].strip()
                line4 = lines[i + 4].strip()

                # line1 should be title, line2 blank, line3 same number, line4 similar title
                if len(line1) > 5 and line2 == '' and line3 == line:
                    chapter_starts.append((i, chapter_num, line1))

    # Remove duplicates and sort
    seen = set()
    unique_starts = []
    for start, num, title in chapter_starts:
        if num not in seen:
            seen.add(num)
            unique_starts.append((start, num, title))

    unique_starts.sort(key=lambda x: x[0])
    return unique_starts

def split_book():
    source_file = Path("source_material/Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.txt")
    chapters_dir = Path("chapters")
    chapters_dir.mkdir(exist_ok=True)

    # Read the entire file
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define sections
    sections = []

    # Front matter (everything before first preface)
    sections.append(("00-front-matter", 0, 72))

    # Preface to 20th Anniversary
    sections.append(("01-preface-20th-anniversary", 72, 151))

    # Preface to First Edition
    sections.append(("02-preface-first-edition", 151, 236))

    # Contents
    sections.append(("03-contents", 236, 263))

    # Find all chapters
    chapter_starts = find_chapter_starts(lines)

    print(f"Found {len(chapter_starts)} chapters:")
    for start, num, title in chapter_starts:
        print(f"  Chapter {num}: {title} (line {start})")
    print()

    # Add chapters as sections
    for idx, (start, chapter_num, title) in enumerate(chapter_starts):
        # Determine end: either next chapter or a reasonable endpoint
        if idx + 1 < len(chapter_starts):
            end = chapter_starts[idx + 1][0]
        else:
            # Last chapter - find epilogue
            end = 7200
            for i in range(start + 100, min(start + 3000, len(lines))):
                if lines[i].strip() == "Epilogue":
                    end = i
                    break

        section_name = f"{chapter_num + 3:02d}-chapter-{chapter_num:02d}-{normalize_filename(title)}"
        sections.append((section_name, start, end))

    # Find Epilogue
    epilogue_start = None
    notes_start = None
    index_start = None

    for i in range(7000, len(lines)):
        if lines[i].strip() == "Epilogue" and epilogue_start is None:
            epilogue_start = i
        if lines[i].strip() == "Notes and References" and notes_start is None:
            notes_start = i
        if lines[i].strip() == "Index" and index_start is None and i > 7500:
            index_start = i

    # Update last chapter end if we found epilogue
    if epilogue_start and sections[-1][0].startswith("2"):
        sections[-1] = (sections[-1][0], sections[-1][1], epilogue_start)

    # Add epilogue
    if epilogue_start and notes_start:
        sections.append(("98-epilogue", epilogue_start, notes_start))

    # Add notes and references
    if notes_start and index_start:
        sections.append(("99-notes-and-references", notes_start, index_start))

    # Add index
    if index_start:
        sections.append(("99-index", index_start, len(lines)))

    # Write each section to a file
    print("Creating files:")
    for section_name, start, end in sections:
        output_file = chapters_dir / f"{section_name}.txt"
        section_lines = lines[start:end]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(section_lines)
        print(f"  {output_file.name} ({len(section_lines)} lines, lines {start}-{end})")

    print(f"\nTotal sections created: {len(sections)}")

if __name__ == "__main__":
    split_book()
