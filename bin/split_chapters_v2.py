#!/usr/bin/env python3
"""
Split The Mythical Man-Month source text into individual chapter files.
Uses manually identified chapter boundaries for reliability.
"""

from pathlib import Path

def split_book():
    source_file = Path("source_material/Addison.Wesley.The.Mythical.Man-Month.Essays.on.Software.Engineering.20th.Anniversary.Edition.txt")
    chapters_dir = Path("chapters")
    chapters_dir.mkdir(exist_ok=True)

    # Read the entire file
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Manually identified section boundaries (line numbers from grep/search)
    # Format: (filename, start_line, end_line_or_None)
    sections = [
        ("00-front-matter", 0, 72),
        ("01-preface-20th-anniversary", 72, 151),
        ("02-preface-first-edition", 151, 236),
        ("03-contents", 236, 262),
        ("04-chapter-01-the-tar-pit", 262, 454),
        ("05-chapter-02-the-mythical-man-month", 454, 745),
        ("06-chapter-03-the-surgical-team", 745, 963),
        ("07-chapter-04-aristocracy-democracy-and-system-design", 963, 1269),
        ("08-chapter-05-the-second-system-effect", 1269, 1438),
        ("09-chapter-06-passing-the-word", 1438, 1718),
        ("10-chapter-07-why-did-the-tower-of-babel-fail", 1718, 2069),
        ("11-chapter-08-calling-the-shot", 2069, 2267),
        ("12-chapter-09-ten-pounds-in-a-five-pound-sack", 2267, 2457),
        ("13-chapter-10-the-documentary-hypothesis", 2457, 2607),
        ("14-chapter-11-plan-to-throw-one-away", 2607, 2799),
        ("15-chapter-12-sharp-tools", 2799, 3111),
        ("16-chapter-13-the-whole-and-the-parts", 3111, 3435),
        ("17-chapter-14-hatching-a-catastrophe", 3435, 3642),
        ("18-chapter-15-the-other-face", 3642, 3950),
        ("19-chapter-16-no-silver-bullet-essence-and-accident", 3950, 4824),
        ("20-chapter-17-no-silver-bullet-refired", 4824, 5475),
        ("21-chapter-18-propositions-true-or-false", 5475, 6194),
        ("22-chapter-19-after-20-years", 6194, 7200),  # Approximate end, will find epilogue
    ]

    # Find epilogue, notes, and index
    epilogue_start = None
    notes_start = None
    index_start = None

    for i in range(7000, len(lines)):
        line = lines[i].strip()
        if line == "Epilogue" and epilogue_start is None:
            epilogue_start = i
        elif line == "Notes and References" and notes_start is None:
            notes_start = i
        elif line == "Index" and index_start is None and i > 7500:
            index_start = i

    # Update last chapter end with epilogue start
    if epilogue_start:
        last_section = sections[-1]
        sections[-1] = (last_section[0], last_section[1], epilogue_start)

        # Add epilogue
        if notes_start:
            sections.append(("98-epilogue", epilogue_start, notes_start))

    # Add notes and index
    if notes_start and index_start:
        sections.append(("99-notes-and-references", notes_start, index_start))

    if index_start:
        sections.append(("99-index", index_start, len(lines)))

    # Write each section to a file
    print("Creating chapter files:\n")
    for section_name, start, end in sections:
        output_file = chapters_dir / f"{section_name}.txt"
        section_lines = lines[start:end]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(section_lines)
        print(f"  {output_file.name:60} ({len(section_lines):4} lines)")

    print(f"\nTotal files created: {len(sections)}")

if __name__ == "__main__":
    split_book()
