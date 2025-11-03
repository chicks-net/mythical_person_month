# The Mythical Person-Month

![GitHub Issues](https://img.shields.io/github/issues/chicks-net/mythical_person_month)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/chicks-net/mythical_person_month)
![GitHub License](https://img.shields.io/github/license/chicks-net/mythical_person_month)
![GitHub watchers](https://img.shields.io/github/watchers/chicks-net/mythical_person_month)

_The Mythical Person Month_ is a modernized version of the
renowned _Mythical Man Month_ book.

## Motivation

[The Mythical Man-Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month)
by [Fred Brooks](https://en.wikipedia.org/wiki/Fred_Brooks)
is one of the most quoted and insightful books in the history of managing
technology projects.  Yet it is also a product of its times and the stories
[reflect so much sexism](https://psychsafety.com/psychological-safety-66-the-mythical-man-month/)
that it is uncomfortable to encourage our female colleagues to read the book.

Harris, Biencowe, and Telem
([PMC5774006](https://pmc.ncbi.nlm.nih.gov/articles/PMC5774006/))
state it well when they conclude:

> Ultimately, in language, as in medicine, taking the position that our current
> approach is justified because ‘it has always been our approach’ is not
> tenable. Much like the adoption of any new technology or technique, evolving
> our terminology will almost certainly cause growing pains. However, surgical
> workforce demographics have changed and are going to keep changing. Thus, we
> must be rigorous in establishing a nomenclature that promotes not only
> gender-inclusive language, but processes that represent the broad racial,
> social, and sexual identities of our colleagues. In the end, achieving
> linguistic perfection may not be possible, but we should strive for the same
> standards applied to all surgical trainees: make a good faith effort, seek
> consultation when you are unsure, and admit humbly and openly when you have
> erred. The onus is on all of us to challenge our biases and do better.

I could not agree more.  This advice applies just as well to surgeons,
technologists, and any other profession you can imagine.  This repo is
part of my effort to contribute to the "do better" side of the equation.

### Brooks himself evolved

We have not received any approval from Fred Brooks or his family for this
project yet.

One of our earliest observations while working on this project was that
Brooks himself had evolved his use of language during the course of
writing the book.  The earlier chapters were the sole place we found
problematic phrasing.  Chapters 10-20 had no concerning language whatsoever,
and [plenty of examples](inclusive-brooks-quotes.md) of the sort of language we
were aiming for in this project.

In Chapter 10: The Documentary Hypothesis

> "To the new manager, fresh from operating as a **craftsperson themselves**,
> these seem an unmitigated nuisance, an unnecessary distraction, and a white
> tide that threatens to engulf **them**."

In Chapter 11: Plan to Throw One Away

> "Each **person** must be assigned to jobs that broaden **them**, so that the
> whole force is technically flexible."

and

> "Second, the repairer is usually not the **person** who wrote the code, and
> often **they** are a junior programmer or trainee."

In Chapter 12: Sharp Tools

> "This **person** masters all the common tools and is able to instruct
> **their** client-boss in **their** use. **They** also build the specialized
> tools **their** boss needs."

In Chapter 13: The Whole and the Parts

> "First, somebody must be in charge. **They** and **they** alone must
> authorize component changes or substitution of one version for another."

In Chapter 14: Hatching a Catastrophe

> "The boss must first distinguish between action information and status
> information. **They** must discipline **themselves** not to act on problems
> **their** managers can solve, and never to act on problems when **they** are
> explicitly reviewing status."

In Chapter 15: The Other Face

> "if **one** uses it selectively, **they** can ignore most of the bulk most of
> the time. **One** must consider the OS/360 documentation as a library or an
> encyclopedia, not a set of mandatory texts."

In Chapter 16: No Silver Bullet

> "**Programmers** are among the most intelligent part of the population, so
> **they** can learn good practice."

In Chapter 17: No Silver Bullet Refired

> "use the syntax (the external interfaces) and the semantics (the detailed
> functional behavior) of its members if **they** are to achieve all of the
> potential reuse."

In Chapter 18: Propositions True or False

> "A programmer will rarely lie about milestone progress, if the milestone is
> so sharp **they** can't deceive **themselves**."

In Chapter 19: After 20 Years

> "Novices will pull lots of menus; power users very few; and in-between users
> will only occasionally need to pick from a menu, since each will know the few
> short-cuts that make up most of **their** own operations."

The shift from earlier chapters with gendered language to later chapters with
consistently inclusive language could not have happened without Brooks'
awareness or consent.  We may never know what led to Fred's evolution or why
the earlier chapters were not updated.  Until more evidence surfaces, we feel
confident that this project is done in the spirit of the original author.

Chapters 16-19 were written for the 1995 Anniversary Edition of the book, so it
isn't hard to imagine that Brooks had evolved over the intervening decades.  It
is harder to imagine what could have caused chapters 10-15 to have inclusive
language, but hopefully further research will reveal some possibilities.

## Process and Notes

[Our modernization analysis](Modernization_Analysis.md) is the core reason for
this project and repo.  It details the concerns about word choices with
examples and recommendations for solutions.  This led to an analysis of the
individual chapters with details about each issue and options considered
to improve the text:

- [Phase 2a](phase2a.md) covers chapters 1-2
- [Phase 2b](phase2b.md) covers chapters 3-5
- [Phase 2c](phase2c.md) covers chapters 6-8
- [Phase 2d](phase2d.md) covers chapters 9-11 and only chapter 9 had issues
- [Phase 2e](phase2e.md) covers chapters 12-14 which had no issues
- [Phase 2f](phase2f.md) covers chapters 15-17 which had no issues
- [Phase 2g](phase2g.md) covers chapters 18-20 which had no issues

Then a series of pull requests, up to
[#20](https://github.com/chicks-net/mythical_person_month/pull/20),
implemented the language updates to address those concerns.

### Other Notes

- [Figures and Visuals](Figures_and_Visuals.md) summarize the non-text
  elements of the book that we will find some way to handle.
  [Issue #22](https://github.com/chicks-net/mythical_person_month/issues/22)
  is tracking progress on that effort.
- [Claude's guide for itself](CLAUDE.md) explains what's going on in this
  repo in more detail than I'm willing to put the effort into.

## Contributing

- [Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [Contributing Guide](.github/CONTRIBUTING.md) includes a step-by-step guide to our
  [development process](.github/CONTRIBUTING.md#development-process).

## Support & Security

- [Getting Support](.github/SUPPORT.md)
- [Security Policy](.github/SECURITY.md)
