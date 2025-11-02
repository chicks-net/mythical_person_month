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

## Opening Chapter Illustrations

### Chapter 1: The Tar Pit

**Image file:** `chapters/04-chapter-01-the-tar-pit-original-000.png`

**Citation:**
> C R. Knight, Mural of La Brea Tar Pits
> The George C. Page Museum of La Brea Discoveries,
> The Natural History Museum of Los Angeles County

**Description:** Opening illustration showing prehistoric animals trapped in the La Brea Tar Pits, serving as a metaphor for software projects that become mired in complexity. This iconic mural was created by Charles R. Knight in 1925 for the Natural History Museum of Los Angeles County. The mural depicts scavengers descending to feast on the carcasses of megafauna entrapped in asphalt, including mammoths, saber-toothed cats, and dire wolves.

**Historical context:** Knight's mural was considered highly accurate for its time and became hugely influential in shaping public understanding of prehistoric life at La Brea. The dramatic scene perfectly illustrates Brooks's metaphor of the "tar pit" that traps unwary software projects.

**Related links:**
- [Charles R. Knight - Wikipedia](https://en.wikipedia.org/wiki/Charles_R._Knight) - Biography of the renowned paleoartist (1874-1953)
- [La Brea Tar Pits Paleoart](https://palaeo-electronica.org/content/2022/3524-la-brea-tar-pits-paleoart) - Academic article discussing Knight's 1925 mural and its influence
- [La Brea Tar Pits and Museum](https://tarpits.org/) - Official museum website where the mural is housed
- [Natural History Museum of Los Angeles County](https://nhm.org/la-brea-tar-pits) - Parent institution of the Page Museum

---

### Chapter 2: The Mythical Man-Month

**Image file:** `chapters/05-chapter-02-the-mythical-man-month-original-000.png`

**Citation:**
> Good cooking takes time. If you are made to wait, it is to serve you better, and to please you.
> Menu of Restaurant Antoine, New Orleans

**Description:** Opening illustration showing a vintage menu from Restaurant Antoine in New Orleans, founded in 1840. The menu is printed in French and features classic French-Creole dishes including Oysters Rockefeller (invented at Antoine's), various tournedos, entrecôtes, and traditional New Orleans fare. The message at the top of the menu emphasizes that quality work takes time, perfectly illustrating the chapter's central theme that adding more workers to a late project makes it later.

**Historical context:** Antoine's Restaurant was founded by Antoine Alciatore in 1840 and is the oldest family-run restaurant in the United States, having operated continuously for over 180 years through five generations. The restaurant is famous for creating Oysters Rockefeller and other iconic dishes. The philosophy expressed in the menu's opening quote - that good work cannot be rushed - directly parallels Brooks's argument about software development timelines.

**Related links:**
- [Antoine's Restaurant - Wikipedia](https://en.wikipedia.org/wiki/Antoine's) - History of America's oldest family-run restaurant
- [Antoine's Official Website](https://antoines.com/) - The restaurant still operates at 713 St. Louis Street in New Orleans
- [Antoine's Restaurant Collection - Historic New Orleans Collection](https://hnoc.org/research-collections/collection-highlights/the-antoines-restaurant-collection) - Archival materials documenting the restaurant's history
- [Antoine's Restaurant - New Orleans Historical](https://neworleanshistorical.org/items/show/727) - Historical documentation of the restaurant

---

### Chapter 3: The Surgical Team

**Image file:** `chapters/06-chapter-03-the-surgical-team-original-000.png`

**Citation:**
> UPI Photo/The Bettman Archive

**Description:** Opening illustration showing a surgical team in an operating room, with multiple medical professionals surrounding a patient on an operating table. The photograph shows the hierarchical yet coordinated nature of a surgical team, with specialized roles for each team member. This image serves as the central metaphor for the chapter's proposal of organizing programming teams like surgical teams, with one chief surgeon (programmer) supported by specialized team members.

**Historical context:** This photograph is from the United Press International (UPI) collection, which was acquired by the Bettmann Archive in 1984. The Bettmann Archive comprises more than 11 million negatives and prints spanning the 19th and 20th centuries, and is currently managed by Getty Images. The image likely dates from the 1960s-1970s based on the UPI Los Angeles collection that covered this period.

**Related links:**
- [Bettmann Archive - Wikipedia](https://en.wikipedia.org/wiki/Bettmann_Archive) - History of the extensive photographic archive
- [Getty Images - Bettmann Archive](https://www.gettyimages.com/bettmann) - Current repository of the Bettmann collection
- [UPI Photo Collection - Chapman University](https://www.chapman.edu/) - Houses over 48,000 UPI photos from the 1960s-1970s

---

### Chapter 4: Aristocracy, Democracy, and System Design

**Image file:** `chapters/07-chapter-04-aristocracy-democracy-and-system-design-original-000.png`

**Citation:**
> This great church is an incomparable work of art. There is neither aridity nor confusion in the tenets it sets forth... It is the zenith of a style, the work of artists who had understood and assimilated all their predecessors' successes, in complete possession of the techniques of their times, but using them without indiscreet display nor gratuitous feats of skill.
> It was Jean d'Orbais who undoubtedly conceived the general plan of the building, a plan which was respected, at least in its essential elements, by his successors. This is one of the reasons for the extreme coherence and unity of the edifice.
> Reims Cathedral Guidebook
> Photographies Emmanuel Boudot-Lamotte

**Description:** Opening illustration showing the interior nave of Reims Cathedral in France, looking toward the altar with its magnificent rose windows visible. The soaring Gothic arches, perfectly aligned columns, and harmonious proportions exemplify the chapter's theme of conceptual integrity in system design. The photograph captures the coherent vision maintained across multiple architects who succeeded Jean d'Orbais.

**Historical context:** Reims Cathedral (Cathédrale Notre-Dame de Reims) was begun in 1211 under Archbishop Aubry de Humbert with Jean d'Orbais as the first architect. The cathedral was the site of 25 coronations of French kings from 1223 to 1825. Despite having four different architects over its construction period, the cathedral maintains remarkable unity because each architect respected Jean d'Orbais's original design vision. The cathedral is famous for being the first to use bar tracery with rose windows (1211), which became a defining characteristic of Gothic architecture. The Grande Rose was built around 1280 AD and contains tens of thousands of glass pieces in 492 panels.

**Related links:**
- [Reims Cathedral - Wikipedia](https://en.wikipedia.org/wiki/Reims_Cathedral) - Comprehensive history and architectural details
- [Jean d'Orbais - Wikipedia](https://en.wikipedia.org/wiki/Jean_d'Orbais) - Biography of the cathedral's first architect
- [Reims Cathedral - Britannica](https://www.britannica.com/topic/Reims-Cathedral) - Overview of Gothic architecture and significance
- [The Grande Rose of Reims Cathedral - Scientific Reports](https://www.nature.com/articles/s41598-019-39740-y) - Scientific study of the cathedral's rose window
- [Explore Reims Cathedral - French Moments](https://frenchmoments.eu/reims-cathedral/) - Detailed guide to the cathedral's history and features

---

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
