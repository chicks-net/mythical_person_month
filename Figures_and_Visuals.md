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

### Opening Illustration - Chapter 1: The Tar Pit

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

### Opening Illustration - Chapter 2: The Mythical Man-Month

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

### Opening Illustration - Chapter 3: The Surgical Team

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

### Opening Illustration - Chapter 4: Aristocracy, Democracy, and System Design

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

### Opening Illustration - Chapter 5: The Second-System Effect

**Image file:** `chapters/08-chapter-05-the-second-system-effect-original-000.png`

**Citation:**
> Adde parvum parvo magnus acervus erit.
> {Add little to little and there will be a big pile.}
> Ovid
>
> Turning house for air traffic. Lithograph, Paris, 1882
> From Le Vingtième Siècle by A. Robida

**Description:** Opening illustration showing an absurdly over-elaborate Victorian-era vision of a futuristic "turning house for air traffic" - a fantastical rotating platform structure with multiple ornate towers, chimneys, weather vanes, and architectural embellishments. This whimsical yet cluttered design perfectly illustrates the "second-system effect" where designers, freed from the constraints of their first project, add every feature they can imagine, creating an overly complex result.

**Historical context:** Albert Robida (1848-1926) was a French illustrator, lithographer, and novelist who is now recognized as a pioneering science fiction artist. His work "Le Vingtième Siècle" (The Twentieth Century) was first published in installments in 1882 and as a complete book in 1883, set in the year 1952. Unlike Jules Verne, Robida imagined technology integrated into everyday life rather than as the creations of mad scientists, and he remarkably anticipated many social developments including the advancement of women, mass tourism, and pollution. His illustrations featured predictions of televisions, telephones, web-cams, submarines, and helicopters, including his famous "Téléphonoscope" depicting flat-screen, home-theater television.

**Related links:**

- [Albert Robida - Wikipedia](https://en.wikipedia.org/wiki/Albert_Robida) - Biography of the visionary illustrator (1848-1926)
- [Albert Robida's Le Vingtième siècle - St Andrews University](https://special-collections.wp.st-andrews.ac.uk/2011/10/04/albert-robidas-le-vingtieme-siecle/) - Analysis of the work
- [Albert Robida, The Visionary Illustrator - Moss and Fog](https://mossandfog.com/albert-robida-the-visionary-illustrator-who-sketched-the-future-in-the-1800s/) - Overview of his prescient predictions
- [Le vingtième siècle - Internet Archive](https://archive.org/details/levingtimesiclel00robi) - Digital copy of the original work

---

### Opening Illustration - Chapter 6: Passing the Word

**Image file:** `chapters/09-chapter-06-passing-the-word-original-000.png`

**Citation:**
> He'll sit here and he'll say, "Do this! Do that!" And nothing will happen.
> Harry S. Truman, on Presidential Power
>
> "The Seven Trumpets" from The Wells Apocalypse, 14th century
> The Bettman Archive

**Description:** Opening illustration showing a medieval illuminated manuscript page depicting seven angels blowing trumpets, from the Book of Revelation. The angels are arranged in horizontal rows, each figure elegantly drawn in the Gothic style typical of 14th-century English manuscript illumination. This image metaphorically illustrates the challenge of communication - even when the message is literally trumpeted, ensuring it's heard, understood, and acted upon remains difficult.

**Historical context:** The Wells Apocalypse (also spelled "Welles Apocalypse") is an early fourteenth-century illuminated manuscript of the Book of Revelation. English Apocalypse manuscripts were produced prolifically between 1250 and 1400, and this manuscript exemplifies the tradition with its distinctive miniatures. The Seven Trumpets theme was central to Apocalypse illustrations, representing the catastrophic events narrated through the cryptic symbolism of Revelation, which often revolves around the number seven: the opening of the seven seals, the sounding of the seven trumpets, and the fulfillment of the seven last plagues.

**Related links:**

- [English Apocalypse manuscripts - Wikipedia](https://en.wikipedia.org/wiki/English_Apocalypse_manuscripts) - Overview of the tradition
- [Apocalypse Illuminated - Penn State Press](https://www.psupress.org/books/titles/978-0-271-07865-6.html) - Richard K. Emmerson's scholarly work on medieval Apocalypse manuscripts
- [Bettmann Archive - Wikipedia](https://en.wikipedia.org/wiki/Bettmann_Archive) - Information about the archive housing this image

---

### Opening Illustration - Chapter 7: Why Did the Tower of Babel Fail?

**Image file:** `chapters/10-chapter-07-why-did-the-tower-of-babel-fail-original-000.png`

**Citation:**
> Now the whole earth used only one language, with few words... Then they said, "Come, let us build ourselves a city with a tower whose top shall reach the heavens (thus making a name for ourselves), so that we may not be scattered all over the earth."... The Lord said, "They are just one people, and they all have the same language... Come, let us go down and confuse their language."
> Genesis 11:1-8
>
> P. Breughel, the Elder, "Turmbau zu Babel," 1563
> Kunsthistorisches Museum, Vienna

**Description:** Opening illustration showing Pieter Bruegel the Elder's iconic painting "The Tower of Babel," depicting an enormous, partially constructed tower modeled after the Roman Colosseum. The massive spiral structure dominates the landscape, with countless workers, scaffolding, and building activities visible throughout. The painting illustrates the biblical story of humanity's hubris and the catastrophic communication breakdown that caused the project's failure - a perfect metaphor for large software projects that fail due to communication problems.

**Historical context:** This masterpiece was created in 1563 by Pieter Bruegel the Elder (c. 1525-1569), one of the greatest Flemish Renaissance painters. The oil on panel painting (114 × 155 cm) was commissioned by Nicolaes Jonghelinck, an Antwerp banker who owned 16 of Bruegel's paintings. The basic construct of the tower is loosely based on the Colosseum in Rome, which Bruegel had seen during his visit to Italy. Bruegel created multiple versions of this subject; the Vienna version is signed "BRVEGEL.FE. / M.CCCCC.LXIII." A third version is housed in the Museum Boijmans Van Beuningen in Rotterdam. The painting brilliantly captures the biblical narrative of human pride leading to divine intervention through the confusion of languages.

**Related links:**

- [The Tower of Babel (Bruegel) - Wikipedia](https://en.wikipedia.org/wiki/The_Tower_of_Babel_(Bruegel)) - Detailed article about the painting
- [Smarthistory - Pieter Bruegel the Elder, The Tower of Babel](https://smarthistory.org/pieter-bruegel-the-elder-the-tower-of-babel/) - Art historical analysis
- [The Tower of Babel by Pieter Bruegel - Kunsthistorisches Museum](https://www.humanalens.com/post/the-tower-of-babel-by-pieter-bruegel-the-elder) - Museum guide
- [Bruegel's Tower of Babel - Journal of Art in Society](https://www.artinsociety.com/lost-in-translation-bruegelrsquos-tower-of-babel.html) - Analysis of communication themes

---

### Opening Illustration - Chapter 8: Calling the Shot

**Image file:** `chapters/11-chapter-08-calling-the-shot-original-000.png`

**Citation:**
> Practice is the best of all instructors.
> Publilius
>
> Experience is a dear teacher, but fools will learn at no other.
> Poor Richard's Almanac
>
> Douglass Crockwell, "Ruth calls his shot," World Series, 1932
> Reproduced by permission of Esquire Magazine and Douglass Crockwell, © 1945 (renewed 1973) by Esquire, Inc., and courtesy of the National Baseball Museum.

**Description:** Opening illustration showing Babe Ruth at bat in his famous "called shot" moment during Game 3 of the 1932 World Series at Wrigley Field. Ruth is depicted in his New York Yankees uniform, pointing toward the outfield, with the catcher visible behind him. This legendary moment - whether Ruth actually "called" his home run or was simply gesturing at heckling Cubs players - has been debated for decades, making it a perfect metaphor for the challenges of estimation and prediction in software development.

**Historical context:** The "called shot" occurred on October 1, 1932, during Game 3 of the World Series between the New York Yankees and Chicago Cubs. According to legend, Babe Ruth pointed to center field before hitting a home run to that exact spot. The incident has become one of baseball's most famous and controversial moments. Douglass Crockwell (1904-1968) was an American painter and animator who created this illustration for Esquire Magazine in 1945, capturing the mythic quality of the moment. The chapter uses this story to discuss the importance of experience in making accurate estimates - while bold predictions may succeed, they're more often based on accumulated knowledge than pure bravado.

**Related links:**

- [Babe Ruth - Wikipedia](https://en.wikipedia.org/wiki/Babe_Ruth) - Biography of the legendary baseball player
- [Called shot - Wikipedia](https://en.wikipedia.org/wiki/Babe_Ruth%27s_called_shot) - Details about the famous 1932 World Series moment
- [1932 World Series - Wikipedia](https://en.wikipedia.org/wiki/1932_World_Series) - Context of the game
- [Douglass Crockwell - Wikipedia](https://en.wikipedia.org/wiki/Douglass_Crockwell) - Information about the illustrator

---

### Opening Illustration - Chapter 9: Ten Pounds in a Five-Pound Sack

**Image file:** `chapters/12-chapter-09-ten-pounds-in-a-five-pound-sack-original-000.png`

**Citation:**
> The author should gaze at Noah, and... learn, as they did in the Ark, to crowd a great deal of matter into a very small compass.
> Sydney Smith, Edinburgh Review
>
> Engraved from a painting by Heywood Hardy
> The Bettman Archive

**Description:** Opening illustration showing a classical engraving depicting a dramatic scene with a figure struggling with a large beast (possibly a bull or ox) amid swirling, dynamic movement. The Victorian-era artwork captures the intense physical struggle of trying to contain or manage something too large for its constraints - a perfect visual metaphor for the chapter's theme of fitting too much functionality into limited memory space.

**Historical context:** Heywood Hardy (1842-1933) was one of the foremost English Victorian Romanticism painters, known for his equestrian art, sporting subjects, and genre scenes. Born in Chichester, West Sussex, Hardy studied in Bristol, Paris, and Antwerp before moving to London in 1870. He was also an accomplished engraver and illustrator who contributed to the Illustrated London News and the Graphic. Hardy was elected to several prestigious societies including the Royal Society of Painters and Etchers, the Royal Institute of Oil Painters, and the Royal Society of Portrait Painters. His work was characterized by a notable sensitivity in depicting animals, demonstrating a deep understanding particularly of horses. This engraving exemplifies the Victorian tradition of narrative art that could dramatically illustrate abstract concepts.

**Related links:**

- [Heywood Hardy - WikiArt](https://www.wikiart.org/en/heywood-hardy) - Gallery of his artworks
- [Heywood Hardy - Artnet](https://www.artnet.com/artists/heywood-hardy/) - Artist biography and sales history
- [The Makers Series: Heywood Hardy - BADA](https://www.bada.org/features/makers-series-heywood-hardy) - Overview of his career and style
- [Heywood Hardy - Haynes Fine Art](https://haynesfineart.com/artists/heywood-hardy-uk) - Artist biography and works for sale

---

### Opening Illustration - Chapter 10: The Documentary Hypothesis

**Image file:** `chapters/13-chapter-10-the-documentary-hypothesis-original-000.png`

**Citation:**
> The hypothesis: Amid a wash of paper, a small number of documents become the critical pivots around which every project's management revolves. These are the manager's chief personal tools.
>
> W. Bengough, "Scene in the old Congressional Library," 1897
> The Bettman Archive

**Description:** Opening illustration showing an overwhelmingly crowded scene in the old Congressional Library in Washington, D.C., with visitors navigating through mountainous piles of books and papers. Every visible seat is occupied, and documents are stacked everywhere, creating a chaotic environment that paradoxically illustrates the chapter's theme: amid such chaos, a small number of key documents become the critical organizing tools.

**Historical context:** This illustration by William Bengough was published in Harper's Weekly, Vol. 41, on February 27, 1897, page 201, as part of a 10-part series leading up to the opening of the imposing new Library of Congress building. The drawing depicts the library's "present congested condition" in the months just prior to the library's relocation to its own building across the street. The illustration provided visual evidence of the desperate need for expanded space. The image is now held by the Library of Congress (catalog numbers LC-USZ62-86769 and LC-USZ62-3868) with no known restrictions on publication.

**Related links:**

- [Scene in the Old Congressional Library - Library of Congress](https://www.loc.gov/item/99614270/) - Primary source with full catalog information
- [US House of Representatives Historical Images](https://history.house.gov/Collection/Detail/30596) - Congressional perspective on the illustration
- [125 Years of Binding at the Library of Congress](https://blogs.loc.gov/preservation/2025/01/125-years-of-binding-pt1/) - Context about the library's history

---

### Opening Illustration - Chapter 11: Plan to Throw One Away

**Image file:** `chapters/14-chapter-11-plan-to-throw-one-away-original-000.png`

**Citation:**
> There is nothing in this world constant but inconstancy.
> Swift
>
> It is common sense to take a method and try it. If it fails, admit it frankly and try another. But above all try something.
> Franklin D. Roosevelt
>
> Collapse of the aerodynamically misdesigned Tacoma Narrows Bridge, 1940
> UPI Photo/The Bettman Archive

**Description:** Opening illustration showing the dramatic collapse of the Tacoma Narrows Bridge, with its deck twisting and buckling catastrophically. The bridge, nicknamed "Galloping Gertie," spectacularly failed just months after opening due to aerodynamic flaws in its design. This image perfectly illustrates the chapter's central argument: the first version often fails, and you should plan to build a pilot system that you'll eventually throw away, learning from its failures.

**Historical context:** The Tacoma Narrows Bridge collapsed on November 7, 1940, just four months after opening, due to aerodynamic instability caused by wind-induced vibrations. The collapse was extensively documented on film and photographs, becoming one of the most famous engineering failures in history. The footage was recorded on Kodachrome 16mm film by Barney Elliott and Harbine Monroe and was selected for preservation in the United States National Film Registry by the Library of Congress in 1998. Photographer Howard Clifford of the Tacoma News Tribune was on the bridge and ran to safety seconds before it collapsed. The disaster became a landmark case study in engineering education, illustrating the importance of understanding aerodynamic forces and the value of iterative design - precisely the lesson Brooks advocates in this chapter.

**Related links:**

- [Tacoma Narrows Bridge (1940) - Wikipedia](https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge_(1940)) - Comprehensive article on the bridge and its collapse
- [Tacoma Narrows Bridge History - WSDOT](https://wsdot.wa.gov/TNBhistory/) - Official state historical documentation
- [UW Libraries Tacoma Narrows Bridge Collection](https://content.lib.washington.edu/farquharsonweb/index.html) - Extensive photo and film archive
- [The Collapse - UW Special Collections](https://lib.uw.edu/specialcollections/collections/exhibits/tnb/collapse/) - Detailed documentation of the collapse event

---

### Opening Illustration - Chapter 12: Sharp Tools

**Image file:** `chapters/15-chapter-12-sharp-tools-original-000.png`

**Citation:**
> A good workman is known by his tools.
> Proverb
>
> A. Pisano, "Lo Scultore," from the Campanile di Santa Maria del Fiore, Florence, c. 1335

**Description:** Opening illustration showing a medieval relief sculpture of a craftsman (sculptor) at work with his tools. The figure is seated within a Gothic quatrefoil frame, carefully working with sculpting tools on a piece. This 14th-century relief perfectly embodies the chapter's theme that quality tools are essential to quality work - a principle that has held true from medieval stone carvers to modern programmers.

**Historical context:** Andrea Pisano (c. 1290-1348) was an Italian sculptor and architect who directed the works on the Campanile (bell tower) of Santa Maria del Fiore (Florence Cathedral) after Giotto's death, from 1336 until 1342. His workshop created a series of hexagonal marble reliefs for the lower register of Giotto's Campanile, representing various human activities and crafts - celebrating the progress of civilization and human ingenuity. "Lo Scultore" (The Sculptor) is part of this series, which includes reliefs depicting Navigation, Hunting, Weaving, Plowing, and other crafts. The originals are now preserved in the Museo dell'Opera del Duomo in Florence, with copies on the Campanile itself. These reliefs represent some of the finest examples of early Renaissance sculpture, bridging the Gothic and Renaissance styles.

**Related links:**

- [Andrea Pisano - Treccani Encyclopedia](https://www.treccani.it/enciclopedia/andrea-pisano/) - Comprehensive Italian encyclopedia entry
- [Donatello e l'Opera del Duomo](https://duomo.firenze.it/it/opera-magazine/post/6760/donatello-e-l-opera-del-duomo) - Context about the Opera del Duomo and its sculptural works
- [Santa Maria del Fiore - Wikipedia](https://en.wikipedia.org/wiki/Florence_Cathedral) - Information about the cathedral and its art

---

### Opening Illustration - Chapter 13: The Whole and the Parts

**Image file:** `chapters/16-chapter-13-the-whole-and-the-parts-original-000.png`

**Citation:**
> I can call spirits from the vasty deep.
> Why so can I, or so can any man; but will they come when you do call for them?
> Shakespeare, King Henry IV, Part I
>
> © The Walt Disney Company

**Description:** Opening illustration showing Mickey Mouse as the Sorcerer's Apprentice from Disney's Fantasia (1940). Mickey, wearing the iconic pointed wizard's hat with stars and moon, is shown conducting or commanding with his arms outstretched, surrounded by magical sparkles. This image perfectly captures the chapter's theme: just because you can command individual components doesn't mean they'll work together as a unified whole when you need them to - precisely the apprentice's problem when he loses control of the enchanted brooms.

**Historical context:** "The Sorcerer's Apprentice" is the third and most famous segment in Disney's 1940 animated feature film Fantasia. Based on the poem "Der Zauberlehrling" by Johann Wolfgang von Goethe and the musical piece "L'Apprenti Sorcier" by Paul Dukas, it stars Mickey Mouse as the apprentice of the sorcerer Yen Sid. Originally conceived in 1938 as an elaborate Silly Symphony cartoon designed as a comeback role for Mickey Mouse (whose popularity had declined), it evolved into the centerpiece of Fantasia. Walt Disney himself voiced Mickey Mouse in this segment. The three-hour recording session began at midnight on January 9, 1938, at Culver Studios in California, with 85 Hollywood musicians. The segment tells the story of Mickey attempting his master's magic tricks but not knowing how to control them - a perfect metaphor for system integration challenges where individual components work but the whole system fails.

**Related links:**

- [The Sorcerer's Apprentice - Disney Wiki](https://disney.fandom.com/wiki/The_Sorcerer's_Apprentice) - Comprehensive information about the segment
- [Fantasia (1940) - Wikipedia](https://en.wikipedia.org/wiki/Fantasia_(1940_film)) - Full context of the film
- [8 Fun Facts about "The Sorcerer's Apprentice"](https://creativeenglishteacher.com/blogs/news/8-fun-facts-about-the-sorcerers-apprentice-from-walt-disneys-fantasia-1940) - Behind-the-scenes details

---

### Opening Illustration - Chapter 14: Hatching a Catastrophe

**Image file:** `chapters/17-chapter-14-hatching-a-catastrophe-original-000.png`

**Citation:**
> None love the bearer of bad news.
> Sophocles
>
> How does a project get to be a year late?
> ...One day at a time.
>
> A. Canova, "Ercole e lica," 1802. Hercules hurls to his death the messenger Lycas, who innocently brought the death-garment.
> Scala/Art Resource, NY

**Description:** Opening illustration showing Antonio Canova's dramatic neoclassical sculpture of Hercules violently hurling the young messenger Lichas through the air. Hercules, driven mad by pain from a poisoned tunic, kills the innocent messenger who unknowingly delivered it. The sculpture captures the tragic moment of violent reaction to bad news - illustrating the chapter's theme about how projects fail gradually and the danger of shooting the messenger who reports problems.

**Historical context:** Antonio Canova (1757-1822) was one of the greatest neoclassical sculptors. "Hercules and Lichas" (Ercole e Lica) was created circa 1796 and completed in 1815 (making "1802" in the citation the midpoint of its creation). The work depicts the mythological story where Hercules, maddened by pain caused by a tunic soaked in the poisoned blood of the centaur Nessus, throws the very young Lichas into the air - Lichas who, unaware of the poison, had innocently given the tunic to Hercules. When the occupying French saw this piece in 1798, they believed it represented the French Revolution, with Hercules repelling Lichas as domestic forces had driven away the monarchy. The sculpture received strong acclaim from academics and art critics for its powerful emotional imagery. The marble version is displayed at the National Gallery of Modern Art (GNAM) in Rome, while a plaster version is housed in a museum in Canova's boyhood village.

**Related links:**

- [Hercules and Lichas - Google Arts & Culture](https://artsandculture.google.com/story/hercules-and-lichas-by-antonio-canova-la-galleria-nazionale/SQUhXTx31PC2cQ?hl=en) - Detailed examination of the sculpture
- [Hercules and Lichas - History of Art](https://www.thehistoryofart.org/antonio-canova/hercules-and-lichas/) - Art historical analysis
- [Antonio Canova - Wikipedia](https://en.wikipedia.org/wiki/Antonio_Canova) - Biography of the sculptor

---

### Opening Illustration - Chapter 15: The Other Face

**Image file:** `chapters/18-chapter-15-the-other-face-original-000.png`

**Citation:**
> What we do not understand we do not possess.
> Goethe
>
> O give me commentators plain, Who with no deep researches vex the brain.
> Crabbe
>
> A reconstruction of Stonehenge, the world's largest undocumented computer.
> The Bettman Archive

**Description:** Opening illustration showing an aerial or elevated view of Stonehenge, the ancient megalithic monument on Salisbury Plain in England. The image shows the massive stone circle with its distinctive trilithon arrangement. The caption's reference to Stonehenge as "the world's largest undocumented computer" alludes to the monument's astronomical alignments and its use as a prehistoric calculator for tracking celestial events - yet ironically, much of its 20th-century reconstruction went undocumented, paralleling the chapter's theme about the critical importance of documentation in software projects.

**Historical context:** Stonehenge is a prehistoric monument dating from approximately 3000 BC to 2000 BC. While often thought of as an untouched ancient structure, Stonehenge underwent extensive, largely undocumented restoration throughout the 20th century. From 1901 to 1964, the majority of the stone circle was restored in a series of makeovers that official guidebooks failed to mention - it was "historically cleansed," as researcher Brian Edwards discovered. The catalyst came on New Year's Eve 1900 when one of the stones collapsed, prompting Sir Edmund Antrobus to commission restoration works. During hot summers, turf would peel back to reveal concrete boots into which the stones were set. Visitors are often told about Stonehenge as mankind's "first computer" - its standing stones and precise lintels line up with the heavens and solstice suns, suggesting sophisticated astronomical knowledge. This dual nature - an ancient astronomical calculator that underwent modern undocumented reconstruction - makes it a perfect metaphor for Brooks's chapter about documentation being "the other face" of software development.

**Related links:**

- [Stonehenge - Wikipedia](https://en.wikipedia.org/wiki/Stonehenge) - Comprehensive history and archaeology
- [How They Rebuilt Stonehenge - UK Indymedia](https://www.indymedia.org.uk/en/2005/12/330623.html?c=on) - Documentation of 20th century restoration
- [Restoring Stonehenge - The Past](https://the-past.com/feature/restoring-stonehenge-securing-a-neolithic-monument-over-120-years/) - Detailed history of restoration work

---

### Opening Illustration - Chapter 16: No Silver Bullet—Essence and Accident

**Image file:** `chapters/19-chapter-16-no-silver-bullet-essence-and-accident-original-000.png`

**Citation:**
> There is no single development, in either technology or management technique, which by itself promises even one order-of-magnitude improvement within a decade in productivity, in reliability, in simplicity.
>
> The Werewolf of Eschenbach, Germany: line engraving, 1685.
> Courtesy of The Grainger Collection, New York.

**Description:** Opening illustration showing a dramatic 17th-century German line engraving depicting a werewolf. The woodcut-style image shows a fearsome werewolf figure in an interior setting with checkered floor tiles, capturing European folklore about supernatural creatures. The werewolf - a mythical monster that no silver bullet could kill according to legend - serves as the perfect visual metaphor for the chapter's argument that there is no single "silver bullet" solution that will magically solve the inherent difficulties of software engineering.

**Historical context:** The Werewolf of Eschenbach is a German line engraving from 1685 that depicts werewolf folklore from 17th century Europe. Eschenbach is a town in Germany, and this engraving documents the widespread belief in lycanthropy during this period. According to some versions, the engraving shows the werewolf trapped in a well, with an effigy of the werewolf clothed as a man hanged nearby. Werewolf legends were particularly strong in Germanic regions during the 16th and 17th centuries, coinciding with witch hunts and trials. The folklore held that werewolves could only be killed by silver bullets - hence Brooks's chapter title "No Silver Bullet" arguing that no single magical solution exists for software's essential complexity. This historical engraving is now part of the Granger Historical Picture Archive and represents a fascinating document of European supernatural beliefs.

**Related links:**

- [Werewolf of Eschenbach - Granger Historical Picture Archive](https://www.granger.com/0061070-werewolf-1685-the-werewolf-of-eschenbach-germany-trapped-in-image.html) - Original source
- [Werewolf of Eschenbach - Alamy](https://www.alamy.com/stock-photo-werewolf-1685-nthe-werewolf-of-eschenbach-germany-line-engraving-1685-95469616.html) - Historical stock image
- [Lycanthropy - Wikipedia](https://en.wikipedia.org/wiki/Werewolf) - History of werewolf folklore

---

### Opening Illustration - Chapter 17: No Silver Bullet Refired

**Image file:** `chapters/20-chapter-17-no-silver-bullet-refired-original-000.png`

**Citation:**
> Every bullet has its billet.
> William III of England, Prince of Orange
>
> Whoever thinks a faultless piece to see, Thinks what never was, nor is, nor ever shall be.
> Alexander Pope, An Essay on Criticism
>
> Assembling a structure from ready-made parts, 1945
> The Bettman Archive

**Description:** Opening illustration showing a person (likely a child or young person) enthusiastically assembling a construction from ready-made parts - possibly an Erector Set or similar mechanical building toy. The figure is shown working with metal beams, bolts, and structural components, building upward with visible excitement. This image illustrates the dream of building complex systems by simply assembling pre-fabricated components - an idea Brooks critiques in his discussion of whether reusable components can be the "silver bullet" for software engineering.

**Historical context:** This 1945 photograph captures the post-war optimism about modular construction and standardized parts. The Erector Set, invented by A.C. Gilbert in 1913, became immensely popular and represented the industrial-age dream of building anything from standardized components. By 1945, such construction toys symbolized both the American can-do spirit and the engineering principles that had won World War II - standardization, mass production, and modular assembly. Brooks uses this image to examine the promise and limitations of component-based software development. While mechanical construction from standard parts works well because physical components have precise, predictable interfaces, software components face the challenge of conceptual complexity - the essence of software that no amount of standardization can eliminate. The image captures both the appeal and the oversimplification of the "building blocks" approach to complex systems.

**Related links:**

- [Erector Set - Wikipedia](https://en.wikipedia.org/wiki/Erector_Set) - History of the construction toy
- [A.C. Gilbert - Wikipedia](https://en.wikipedia.org/wiki/A._C._Gilbert) - The inventor and his company
- [Modular programming - Wikipedia](https://en.wikipedia.org/wiki/Modular_programming) - Software engineering concepts

---

### Opening Illustration - Chapter 18: Propositions of The Mythical Man-Month: True or False?

**Image file:** `chapters/21-chapter-18-propositions-true-or-false-original-000.png`

**Citation:**
> For brevity is very good, Where we are, or are not understood.
> Samuel Butler, Hudibras
>
> Brooks asserting a proposition, 1967
> Photo by J. Alex Langley for Fortune Magazine

**Description:** Opening illustration showing Fred Brooks himself in 1967, photographed while teaching or presenting. Brooks is shown in business attire (dark suit and tie), wearing glasses, with his hands raised in an expressive teaching gesture. Behind him on a blackboard are visible words including "Problems," "Teaching," "Computer aided instruction," and "content" - suggesting he's explaining concepts about computer-aided instruction. This personal photograph captures Brooks as an educator and thought leader, appropriate for a chapter where he revisits and evaluates his own earlier propositions.

**Historical context:** This photograph was taken by J. Alex Langley for Fortune Magazine in 1967, during Brooks's early career. At this time, Brooks had recently left IBM (where he was the project manager for System/360 and manager of the Operating System/360 software project) and had founded the Computer Science Department at the University of North Carolina at Chapel Hill in 1964. The image shows him in his role as an academic and educator, exploring computer-aided instruction - a cutting-edge topic in the late 1960s. The photograph predates the publication of _The Mythical Man-Month_ (1975) by eight years, capturing Brooks as a young professor developing the ideas that would later become his influential book. This chapter, added in the 20th anniversary edition, shows Brooks courageously re-examining his own earlier assertions, demonstrating intellectual honesty by asking which of his propositions have stood the test of time.

**Related links:**

- [Fred Brooks - Wikipedia](https://en.wikipedia.org/wiki/Fred_Brooks) - Biography and career
- [Fred Brooks - Computer Pioneers](https://history.computer.org/pioneers/brooks.html) - IEEE Computer Society biography
- [UNC Computer Science History](https://www.cs.unc.edu/~brooks/) - Brooks's academic career

---

### Opening Illustration - Chapter 19: The Mythical Man-Month after 20 Years

**Image file:** `chapters/22-chapter-19-after-20-years-original-000.png`

**Citation:**
> I know no way of judging the future but by the past.
> Patrick Henry
>
> You can never plan the future by the past.
> Edmund Burke
>
> Shooting the Rapids
> The Bettman Archive

**Description:** Opening illustration showing a dramatic scene of people in a canoe navigating dangerous river rapids. The engraving depicts the canoe tilted at a precarious angle as it plunges through turbulent white water, with trees and wilderness visible in the background. The image captures both the danger and excitement of shooting rapids - requiring skill, experience, quick decisions, and the ability to adapt to changing conditions, much like managing software projects over time.

**Historical context:** "Shooting the Rapids" was a popular subject in 19th century adventure art and illustration, capturing the dramatic experience of navigating dangerous river rapids in canoes. This was a common and hazardous activity for explorers, fur traders, and prospectors in North America, particularly in Canada during the fur trade era and later during the Klondike Gold Rush. Notable artists who depicted this subject include Frances Anne Hopkins (who painted "Shooting the Rapids (Quebec)" in 1879 after travelling extensively by canoe along fur trading routes with her Hudson's Bay Company official husband), and Cornelius Krieghoff (mid-19th century). The theme represents the adventure, danger, and unpredictability of navigating wild rivers - an apt metaphor for Brooks's retrospective on how software project management has evolved over twenty years. Just as shooting rapids requires reading the water, making split-second decisions, and adapting to conditions, software management requires learning from experience while remaining flexible enough to adjust to new challenges.

**Related links:**

- [Shooting the Rapids by Frances Anne Hopkins](https://useum.org/artwork/Shooting-the-Rapids-Quebec-Frances-Anne-Hopkins-1879) - 1879 painting
- [Shooting the Rapids - Cornelius Krieghoff](https://collections.gilcrease.org/object/011154) - Gilcrease Museum collection
- [Klondike Gold Rush illustrations](https://www.istockphoto.com/vector/prospectors-shooting-the-rapids-on-the-way-to-the-klondike-gold-rush-19th-century-gm1372493456-441579420) - Historical context

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
