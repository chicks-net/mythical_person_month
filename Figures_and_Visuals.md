# Figures and Visual Elements

## Overview

This document catalogs all figures, tables, charts, diagrams, and other visual
elements referenced throughout _The Mythical Person-Month_ markdown chapters.
These visual elements are crucial to understanding Brooks's arguments and
should be recreated or sourced for the modernized version.

**Analysis Date:** 2025-10-25
**Source:** 23 markdown chapter files

## Summary Statistics

- **Formal Figures:** 18 numbered figures
- **Tables:** 1 formal table
- **Charts Referenced:** PERT charts, organization charts, Gantt charts
- **Other Visual References:** Flow charts, diagrams, structure graphs

## Figures by Chapter

### Chapter 1: The Tar Pit

#### Fig. 1.1: Evolution of the programming systems product

- **Location:** `04-chapter-01-the-tar-pit.md:31`
- **Context:** Shows the relationship between a program, programming product, programming system, and programming systems product
- **Description:** Illustrates that a programming systems product costs 9x more than a simple program
- **Type:** Conceptual diagram with quadrants

### Chapter 2: The Mythical Man-Month

#### Fig. 2.1: Time versus number of workers—perfectly partitionable task

- **Location:** `05-chapter-02-the-mythical-man-month.md:45`
- **Referenced:** Line 43
- **Context:** Tasks like reaping wheat or picking cotton
- **Description:** Shows linear relationship when tasks can be perfectly partitioned with no communication
- **Type:** Graph

#### Fig. 2.2: Time versus number of workers—unpartitionable task

- **Location:** `05-chapter-02-the-mythical-man-month.md:54`
- **Referenced:** Line 52
- **Context:** "The bearing of a child takes nine months, no matter how many women are assigned"
- **Description:** Shows that adding workers has no effect on sequential tasks
- **Type:** Graph

#### Fig. 2.3: Time versus number of workers—partitionable task requiring communication

- **Location:** `05-chapter-02-the-mythical-man-month.md:63`
- **Referenced:** Line 61
- **Context:** Tasks that can be partitioned but require communication
- **Description:** Shows worse than linear trade-off due to communication overhead
- **Type:** Graph

#### Fig. 2.4: Time versus number of workers—task with complex interrelationships

- **Location:** `05-chapter-02-the-mythical-man-month.md:76`
- **Referenced:** Line 74
- **Context:** Tasks with n(n-1)/2 intercommunication requirements
- **Description:** Shows communication overhead fully counteracting division of labor
- **Type:** Graph

#### Fig. 2.5: [Schedule diagram with mileposts A, B, C, D]

- **Location:** `05-chapter-02-the-mythical-man-month.md:126`
- **Context:** Example of 12 man-months task assigned to 3 people for 4 months
- **Description:** Original schedule showing monthly mileposts
- **Type:** Schedule/timeline diagram
- **Note:** Not formally titled but referenced as "Fig. 2.5"

#### Fig. 2.6: [Schedule slippage diagram]

- **Location:** Referenced at lines 130, 132, 137
- **Context:** First milepost not reached until two months elapsed
- **Description:** Shows actual vs. planned schedule
- **Type:** Schedule/timeline diagram

#### Fig. 2.7: [Uniformly low estimate scenario]

- **Location:** Referenced at lines 133, 143
- **Context:** Assumption that whole estimate was uniformly low
- **Description:** Alternative schedule scenario
- **Type:** Schedule/timeline diagram

#### Fig. 2.8: [Regenerative disaster scenario]

- **Location:** Referenced at lines 137 (twice)
- **Context:** Shows effect of adding 2 new people to late project
- **Description:** Demonstrates Brooks's Law in action
- **Type:** Schedule/timeline diagram

**Note on Figs 2.5-2.8:** According to the notes
(98-notes-and-references.md:24), these figures are due to Jerry Ogdin, who
improved illustrations from Brooks's earlier publication.

### Chapter 3: The Surgical Team

#### Fig. 3.1: [Surgical team communication pattern]

- **Location:** `06-chapter-03-the-surgical-team.md:71`
- **Context:** Shows simplified communication pattern in surgical team structure
- **Description:** Illustrates how specialization permits radically simpler communication
- **Type:** Communication diagram/network

### Chapter 8: Calling the Shot

#### Fig. 8.1: Programming effort as a function of program size

- **Location:** `11-chapter-08-calling-the-shot.md:37`
- **Referenced:** Line 21
- **Context:** Results from Nanus and Farr study at System Development Corporation
- **Description:** Shows exponent of 1.5 (Effort = (constant) × (instructions)^1.5)
- **Type:** Graph/chart
- **Source:** Nanus and Farr study

#### Fig. 8.2: Summary of four No. 1 ESS program jobs

- **Location:** `11-chapter-08-calling-the-shot.md:75`
- **Referenced:** Line 73
- **Context:** John Harr's data from Bell Labs
- **Description:** Detailed productivity data from Electronic Switching System project
- **Type:** Table
- **Data included:**
  - Program name
  - Number of programmers
  - Years
  - Man-years
  - Program words
  - Words/man-year

**Table contents:**

| Program | Number of programmers | Years | Man-years | Program words | Words/man-year |
|---------|----------------------|-------|-----------|---------------|----------------|
| Operational units | 50 | 4 | 101 | 52,000 | 515 |
| Maintenance | 36 | 4 | 81 | 51,000 | 630 |
| Compiler | 13 | 2½ | 12 | 38,000 | 2270 |
| Translator (Data assembler) | 15 | 2½ | 11 | 25,000 | - |

#### Fig. 8.3: ESS predicted and actual programming rates

- **Location:** `11-chapter-08-calling-the-shot.md:88`
- **Referenced:** Line 86
- **Context:** Comparison of predicted vs. actual rates
- **Type:** Comparative chart/graph
- **Source:** John Harr, Bell Labs

#### Fig. 8.4: ESS predicted and actual debugging rates

- **Location:** `11-chapter-08-calling-the-shot.md:95`
- **Referenced:** Line 86
- **Context:** Comparison of predicted vs. actual debugging rates
- **Type:** Comparative chart/graph
- **Source:** John Harr, Bell Labs

### Chapter 11: Plan to Throw One Away

#### Fig. 11.1: IBM dual ladder of advancement

- **Location:** `14-chapter-11-plan-to-throw-one-away.md:137`
- **Referenced:** Line 124
- **Context:** Shows IBM's parallel career advancement paths
- **Description:** Illustrates technical vs. management advancement ladders
- **Type:** Organizational diagram

### Chapter 12: Sharp Tools

#### Fig. 12.1: Growth in use of target machines

- **Location:** `15-chapter-12-sharp-tools.md:93`
- **Referenced:** Line 74
- **Context:** OS/360 project target machine utilization
- **Description:** Shows how everyone began to use target machines simultaneously
- **Type:** Growth chart/graph

#### Fig. 12.2: Comparative productivity under batch and conversational programming

- **Location:** `15-chapter-12-sharp-tools.md:315`
- **Referenced:** Line 320
- **Context:** Data reported by John Harr of Bell Labs
- **Description:** Compares productivity between batch and interactive programming
- **Type:** Comparative chart/graph
- **Source:** John Harr, Bell Labs

### Chapter 14: Hatching a Catastrophe

#### Fig. 14.1: Milestone report excerpt

- **Location:** `17-chapter-14-hatching-a-catastrophe.md:208`
- **Referenced:** Line 162
- **Context:** Example of milestone reporting document
- **Description:** Shows format and content of project milestone reports
- **Type:** Document excerpt/sample

### Chapter 15: The Other Face

#### Fig. 15.1: A program structure graph

- **Location:** `18-chapter-15-the-other-face.md:154`
- **Referenced:** Line 134
- **Context:** Shows subprogram structure
- **Description:** Visual representation of program organization
- **Type:** Structure graph/diagram
- **Credit:** Courtesy of W. V. Wright

#### Fig. 15.2: [Statement-level structure diagram]

- **Location:** Referenced at line 165
- **Context:** Shows how boxes contain statements
- **Description:** Detailed view of program structure
- **Type:** Structure diagram

#### Fig. 15.3: [Self-documenting PL/I program example]

- **Location:** Referenced at line 240
- **Context:** Example of self-documenting code
- **Description:** Shows documentation technique in PL/I
- **Type:** Code listing/example

### Chapter 16: No Silver Bullet—Essence and Accident

#### Fig. 16.1: Exciting products

- **Location:** `19-chapter-16-no-silver-bullet-essence-and-accident.md:757`
- **Referenced:** Line 742
- **Context:** Lists products including Cobol, PL/I, Algol, MVS/370, MS-DOS
- **Description:** Shows timeline or categorization of significant software products
- **Type:** List/table/timeline

### Chapter 19: After 20 Years

#### Fig. 19.1: Waterfall model of software construction

- **Location:** `22-chapter-19-after-20-years.md:368`
- **Referenced:** Line 351
- **Context:** Sequential model improved by Winton Royce
- **Description:** Classic waterfall development process diagram
- **Type:** Process flow diagram
- **Also described as:** Gantt chart layout (line 350)

## Charts and Diagrams (Non-Numbered)

### PERT Charts

#### References throughout Chapter 14 (Hatching a Catastrophe)

- Line 51: Mentions PERT chart for estimating
- Line 89: Network chart or critical-path schedule
- Line 99: Definition of PERT chart network
- Line 101: "The preparation of a PERT chart is the most valuable part"
- Line 104: "The first chart is always terrible"
- Line 107: "As the project proceeds, the PERT chart provides the answer"
- Line 156: "The PERT chart with its frequent sharp milestones"
- Line 210: "The preparation of the PERT chart is a function of the boss"

#### Referenced in Chapter 18 (Propositions)

- Line 698: "The preparation of a critical-path chart is the most valuable part"
- Line 702: "The first chart is always terrible"
- Line 704: "A critical path chart answers the demoralizing excuse"

### Organization Charts

#### Chapter 10: The Documentary Hypothesis

- Line 46: "Organization chart" listed as key document
- Line 123: "Who: organization chart"
- Line 126: Conway's observation about communication structures

#### Chapter 18: Propositions True or False

- Line 384: Lists organization chart as critical document
- Line 392: Organization chart in document list

### Flow Charts

#### Chapter 15: The Other Face - "The Flow-Chart Curse"

- Line 109: "A flow chart or subprogram structure graph"
- Line 121: Section titled "The Flow-Chart Curse"
- Lines 123-125: Discussion of oversold flow charts
- Lines 127-129: Flow charts show decision structure
- Line 132: "The one-page flow chart for a substantial program"
- Lines 157-159: ANSI flow-charting standards
- Line 161: "The detailed blow-by-blow flow chart"
- Lines 174-176: "I have never seen an experienced programmer who routinely made detailed flow charts"
- Lines 194, 208: Flow charts in documentation
- Line 310: "How about flow charts and structure graphs?"

#### Chapter 16: No Silver Bullet

- Line 464: "considering flowcharts as the ideal program design medium"
- Line 470: "the flow chart is a very poor abstraction"
- Lines 474-475: "the flow chart has today been elaborated, it has proved to be essentially useless as a design tool"
- Line 490: "Whether we diagram control flow"

#### Chapter 18: Propositions

- Lines 754-755: "The flow chart is a most thoroughly oversold piece of program documentation"
- Line 757: "Few programs need more than a one-page flow chart"
- Line 762: "does not need the ANSI flow-charting standards"

### Other Diagrams

**Structure Graphs:**

- Chapter 15, Line 109: "subprogram structure graph"
- Chapter 15, Line 133: "essentially a diagram of program structure"

**Connectivity Schematics:**

- Chapter 16, Line 191-192: "land has maps, silicon chips have diagrams, computers have connectivity schematics"

**Software Structure Diagrams:**

- Chapter 16, Line 192: "we attempt to diagram software structure"
- Chapter 16, Line 479: "software diagram"
- Chapter 16, Line 492: "superimpose all the diagrams"

**Desktop Metaphor:**

- Chapter 16, Line 479: "The so-called 'desktop metaphor'"

**Control Flow/Data Flow:**

- Chapter 16, Line 490: "Whether we diagram control flow"

**Tables Reference:**

- Chapter 12, Line 55: "Show me your flowcharts and conceal your tables, and I shall continue to be mystified. Show me your tables, and I won't usually need your flowcharts"

## Visual Elements by Type

### Graphs and Charts

1. **Time vs. Workers graphs** (Figs 2.1-2.4): Four variants showing different task partition scenarios
2. **Effort vs. Size** (Fig 8.1): Exponential relationship chart
3. **Productivity comparisons** (Figs 8.3, 8.4, 12.2): Comparative data visualizations
4. **Growth chart** (Fig 12.1): Usage over time

### Tables

1. **Productivity table** (Fig 8.2): Detailed project metrics

### Diagrams

1. **Conceptual diagrams** (Figs 1.1, 3.1): System relationships and team structure
2. **Structure graphs** (Figs 15.1, 15.2): Program organization
3. **Process diagrams** (Fig 19.1): Waterfall model
4. **Organizational diagrams** (Fig 11.1): Career advancement paths

### Schedule/Timeline Diagrams

1. **Schedule scenarios** (Figs 2.5-2.8): Project timeline examples

### Document Samples

1. **Report excerpt** (Fig 14.1): Milestone reporting format
2. **Code listing** (Fig 15.3): Self-documenting code example
3. **Product list** (Fig 16.1): Software products

## Missing Visual Elements

Visual elements that are **referenced but not formally numbered:**

1. Chapter 3, Line 71: Communication pattern diagram (mentioned but not titled as figure)
2. Chapter 15, Line 165: Statement structure boxes (Fig 15.2 implied but not explicitly titled)
3. Chapter 15, Line 240: PL/I code example (Fig 15.3 implied)

## Implementation Notes

### For Modernization Project

**High Priority - Essential Figures:**

1. **Fig 1.1**: Core concept diagram, foundational to understanding
2. **Figs 2.1-2.4**: Central to Chapter 2's main argument
3. **Figs 2.5-2.8**: Illustrate Brooks's Law
4. **Fig 8.2**: Important productivity data table

**Medium Priority - Supporting Data:**

1. Figs 8.1, 8.3, 8.4: Historical data visualizations
2. Figs 12.1, 12.2: Tool and methodology comparisons
3. Fig 19.1: Waterfall model (widely known, could reference standard version)

**Lower Priority - Supplementary:**

1. Figs 11.1, 14.1, 15.1, 15.2, 15.3: Supporting examples
2. Fig 16.1: Product list (text-only acceptable)

### Source Considerations

**Original figures to recreate:**

- Most diagrams will need recreation as the PDFs are the source
- Consider modernizing graph styles while preserving data
- Ensure accessibility (alt text, descriptions)

**Data to preserve:**

- Fig 8.2 table should be kept exactly as shown (after language modernization)
- Historical data in Figs 8.1, 8.3, 8.4, 12.2 should remain accurate to sources

**Diagrams to update:**

- Fig 1.1: Could benefit from modern design while keeping concept
- Figs 2.1-2.8: Keep mathematical relationships, update visual style
- Fig 19.1: Consider showing modern interpretation alongside original waterfall

### File Format Recommendations

For the markdown files:

- **Inline images**: `![Alt text](path/to/image.png)` for small diagrams
- **Referenced figures**: Link to separate image files for clarity
- **Tables**: Use markdown tables (already done for Fig 8.2)
- **Code listings**: Use markdown code blocks with syntax highlighting

### Accessibility

All figures should include:

1. **Alt text**: Brief description for screen readers
2. **Figure caption**: Detailed explanation in text
3. **Data tables**: For graphs, consider providing data in table format
4. **High contrast**: Ensure visibility for low-vision readers

## References to Illustration in Meta-Content

**Preface (First Edition):**

- Line 75: Thanks to "Professor Joseph C. Sloane for advice on illustration"

**Chapter 17 (No Silver Bullet Refired):**

- Line 24: "I was not aware of the sidebar and illustrations"
- Line 389: "The illustration opening this chapter"

**Notes and References:**

- Line 25: Credit to Jerry Ogdin for improving illustrations of Figs 2.5-2.8
- Line 243: Reference to Bohm and Jacopini flow diagram paper
- Multiple references to papers with diagrams and charts

## Conclusion

The book contains **18 formally numbered figures**, **1 formal table**, and
numerous references to charts, diagrams, and other visual elements that are
essential to understanding Brooks's arguments.

**Key observations:**

1. Chapter 2 is the most figure-heavy with 8 figures
2. Most figures are conceptual diagrams or data visualizations
3. Flow charts are extensively discussed but criticized as oversold
4. PERT/critical path charts are recommended as valuable tools
5. Some figures are referenced but may not have formal numbers in the text

**Next steps for modernization:**

1. Extract or recreate all 18 numbered figures from PDF sources
2. Decide on visual style (preserve historical vs. modernize presentation)
3. Create markdown-compatible image files
4. Add proper accessibility features
5. Verify all figure references are accurate after modernization
6. Consider creating vector graphics (SVG) for scalability

---

- **Document prepared by:** Claude Code analysis
- **Source files:** 23 markdown chapters
- **Total formal figures:** 18
- **Total formal tables:** 1
- **Other visual elements:** Numerous charts, diagrams, and documentation samples
