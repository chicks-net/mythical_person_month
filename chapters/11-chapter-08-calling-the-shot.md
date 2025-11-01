# Chapter 8: Calling the Shot

> Practice is the best of all instructors.
>
> PUBLILIUS
>
> Experience is a dear teacher, but fools will learn at no other.
>
> POOR RICHARD'S ALMANAC

How long will a system programming job take? How much effort will be required? How does one estimate?

I have earlier suggested ratios that seem to apply to planning time, coding, component test, and system test. First, one must say that one does not estimate the entire task by estimating the coding portion only and then applying the ratios. The coding is only one-sixth or so of the problem, and errors in its estimate or in the ratios could lead to ridiculous results.

Second, one must say that data for building isolated small programs are not applicable to programming systems products. For a program averaging about 3200 words, for example, Sackman, Erikson, and Grant report an average code-plus-debug time of about 178 hours for a single programmer, a figure which would extrapolate to give an annual productivity of 35,800 statements per year. A program half that size took less than one-fourth as long, and extrapolated productivity is almost 80,000 statements per year.[^1] Planning, documentation, testing, system integration, and training times must be added. The linear extrapolation of such sprint figures is meaningless. Extrapolation of times for the hundred-yard dash shows that someone can run a mile in under three minutes.

[^1]: Sackman, H., W. J. Erikson, and E. E. Grant, "Exploratory experimentation studies comparing online and offline programming performance," *CACM*, 11, 1 (Jan., 1968), pp. 3-11.

Before dismissing them, however, let us note that these numbers, although not for strictly comparable problems, suggest that effort goes as a power of size even when no communication is involved except that of someone with their memories.

Figure 8.1 tells the sad story. It illustrates results reported from a study done by Nanus and Farr[^2] at System Development Corporation. This shows an exponent of 1.5; that is:

[^2]: Nanus, B., and L. Farr, "Some cost contributors to large-scale programs," *AFIPS Proc. SJCC*, 25 (Spring, 1964), pp. 239-248.

```text
effort = (constant) × (number of instructions)^1.5
```

Another SDC study reported by Weinwurm[^3] also shows an exponent near 1.5.

[^3]: Weinwurm, G. F., "Research in the management of computer programming," Report SP-2059, System Development Corp., Santa Monica, 1965.

A few studies on programmer productivity have been made, and several estimating techniques have been proposed. Morin has prepared a survey of the published data.[^4] Here I shall give only a few items that seem especially illuminating.

[^4]: Morin, L. H., "Estimation of resources for computer programming projects," M. S. thesis, Univ. of North Carolina, Chapel Hill, 1974.

## Fig. 8.1: Programming effort as a function of program size

```text
Graph showing exponential relationship between program size
(in thousands of machine instructions) and effort
Curve demonstrates effort ∝ (size)^1.5
```

## Portman's Data

Charles Portman, manager of ICL's Software Division, Computer Equipment Organization (Northwest) at Manchester, offers another useful personal insight.[^5]

[^5]: Portman, C., private communication.

Portman found his programming teams missing schedules by about one-half—each job was taking approximately twice as long as estimated. The estimates were very careful, done by experienced teams estimating person-hours for several hundred subtasks on a PERT chart. When the slippage pattern appeared, he asked them to keep careful daily logs of time usage. These showed that the estimating error could be entirely accounted for by the fact that his teams were only realizing 50 percent of the working week as actual programming and debugging time. Machine downtime, higher-priority short unrelated jobs, meetings, paperwork, company business, sickness, personal time, etc. accounted for the rest. In short, the estimates made an unrealistic assumption about the number of technical work hours per person-year. My own experience quite confirms his conclusion.[^6]

[^6]: An unpublished 1964 study by E. F. Bardain shows programmers realizing 27 percent productive time. (Quoted by D. B. Mayer and A. W. Stalnaker, "Selection and evaluation of computer personnel," *Proc. 23rd ACM. Conf.*, 1968, p. 661.)

## Aron's Data

Joel Aron, manager of Systems Technology at IBM in Gaithersburg, Maryland, has studied programmer productivity when working on nine large systems (briefly, large means more than 25 programmers and 30,000 deliverable instructions).[^7] He divides such systems according to interactions among programmers (and system parts) and finds productivities as follows:

[^7]: Aron, J., private communication.

- Very few interactions: 10,000 instructions per person-year
- Some interactions: 5,000
- Many interactions: 1,500

The person-years do not include support and system test activities, only design and programming. When these figures are diluted by a factor of two to cover system test, they closely match Harr's data.

## Harr's Data

John Harr, manager of programming for the Bell Telephone Laboratories' Electronic Switching System, reported his and others' experience in a paper at the 1969 Spring Joint Computer Conference.[^8] These data are shown in Figs. 8.2, 8.3, and 8.4.

[^8]: Harr, J., "Programming Experience for the Number 1 Electronic Switching System," paper given at the 1969 SJCC.

Of these, Fig. 8.2 is the most detailed and the most useful. The first two jobs are basically control programs; the second two are basically language translators. Productivity is stated in terms of debugged words per person-year. This includes programming, component test, and system test. It is not clear how much of the planning effort, or effort in machine support, writing, and the like, is included.

### Fig. 8.2: Summary of four No. 1 ESS program jobs

| Program | Number of programmers | Years | Person-years | Program words | Words/person-year |
|---------|----------------------|-------|-----------|---------------|----------------|
| Operational units | 50 | 4 | 101 | 52,000 | 515 |
| Maintenance | 36 | 4 | 81 | 51,000 | 630 |
| Compiler | 13 | 2½ | 12 | 38,000 | 2270 |
| Translator (Data assembler) | 15 | 2½ | 11 | 25,000 | - |

The productivities likewise fall into two classifications; those for control programs are about 600 words per person-year; those for translators are about 2200 words per person-year. Note that all four programs are of similar size—the variation is in size of the work groups, length of time, and number of modules. Which is cause and which is effect? Did the control programs require more people because they were more complicated? Or did they require more modules and more person-months because they were assigned more people? Did they take longer because of the greater complexity, or because more people were assigned? One can't be sure. The control programs were surely more complex. These uncertainties aside, the numbers describe the real productivities achieved on a large system, using present-day programming techniques. As such they are a real contribution.

Figures 8.3 and 8.4 show some interesting data on programming and debugging rates as compared to predicted rates.

### Fig. 8.3: ESS predicted and actual programming rates

```text
Graph comparing predicted vs actual programming rates over time
Shows actual rates varying from predicted estimates
```

### Fig. 8.4: ESS predicted and actual debugging rates

```text
Graph comparing predicted vs actual debugging rates over time
Shows actual rates varying from predicted estimates
```

## OS/360 Data

IBM OS/360 experience, while not available in the detail of Harr's data, confirms it. Productivities in range of 600-800 debugged instructions per person-year were experienced by control program groups. Productivities in the 2000-3000 debugged instructions per person-year were achieved by language translator groups. These include planning done by the group, coding component test, system test, and some support activities. They are comparable to Harr's data, so far as I can tell.

Aron's data, Harr's data, and the OS/360 data all confirm striking differences in productivity related to the complexity and difficulty of the task itself. My guideline in the morass of estimating complexity is that compilers are three times as bad as normal batch application programs, and operating systems are three times as bad as compilers.[^9]

[^9]: Wolverton, R. W., "The cost of developing large-scale software," *IEEE Trans. on Computers*, C-23, 6 (June, 1974) pp. 615-636. This important recent paper contains data on many of the issues of this chapter, as well as confirming the productivity conclusions.

## Corbató's Data

Both Harr's data and OS/360 data are for assembly language programming. Little data seem to have been published on system programming productivity using higher-level languages. Corbató of MIT's Project MAC reports, however, a mean productivity of 1200 lines of debugged PL/I statements per person-year on the MULTICS system (between 1 and 2 million words).[^10]

[^10]: Corbató, F. J., "Sensitive issues in the design of multi-use systems," lecture at the opening of the Honeywell EDP Technology Center, 1968.

This number is very exciting. Like the other projects, MULTICS includes control programs and language translators. Like the others, it is producing a system programming product, tested and documented. The data seem to be comparable in terms of kind of effort included. And the productivity number is a good average between the control program and translator productivities of other projects.

But Corbató's number is lines per person-year, not words! Each statement in his system corresponds to about three to five words of handwritten code! This suggests two important conclusions.

- Productivity seems constant in terms of elementary statements, a conclusion that is reasonable in terms of the thought a statement requires and the errors it may include.[^11]
- Programming productivity may be increased as much as five times when a suitable high-level language is used.[^12]

[^11]: W. M. Taliaferro also reports a constant productivity of 2400 statements/year in assembler, Fortran, and Cobol. See "Modularity. The key to system growth potential," *Software*, I, 3 (July 1971) pp. 245-257.

[^12]: E. A. Nelson's System Development Corp. Report TM-3225, *Management Handbook for the Estimation of Computer Programming Costs*, shows a 3-to-1 productivity improvement for high-level language (pp. 66-67), although his standard deviations are wide.
