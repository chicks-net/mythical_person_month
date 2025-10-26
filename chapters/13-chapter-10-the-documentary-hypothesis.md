# Chapter 10: The Documentary Hypothesis

> The hypothesis:
> Amid a wash of paper, a small number of documents
> become the critical pivots around which every project's
> management revolves. These are the manager's chief
> personal tools.

*W. Bengough, "Scene in the old Congressional Library," 1897*
*The Bettman Archive*

---

The technology, the surrounding organization, and the traditions
of the craft conspire to define certain items of paperwork that a
project must prepare. To the new manager, fresh from operating
as a craftsperson themselves, these seem an unmitigated nuisance, an
unnecessary distraction, and a white tide that threatens to engulf
them. And indeed, most of them are exactly that.

Bit by bit, however, they come to realize that a certain small set
of these documents embodies and expresses much of their managerial work. The preparation of each one serves as a major occasion
for focusing thought and crystallizing discussions that otherwise
would wander endlessly. Its maintenance becomes their surveillance
and warning mechanism. The document itself serves as a checklist, a status control, and a database for their reporting.

In order to see how this should work for a software project,
let us examine the specific documents useful in other contexts and
see if a generalization emerges.

## Documents for a Computer Product

Suppose one is building a machine. What are the critical documents?

**Objectives.** This defines the need to be met and the goals,
desiderata, constraints, and priorities.

**Specifications.** This is a computer manual plus performance
specifications. It is one of the first documents generated in proposing a new product, and the last document finished.

**Schedule.**

**Budget.** Not merely a constraint, the budget is one of the manager's most useful documents. Existence of the budget forces technical decisions that otherwise would be avoided; and, more
important, it forces and clarifies policy decisions.

**Organization chart.**

**Space allocations.**

**Estimate, forecast, prices.** These three have cyclic interlocking,
which determines the success or failure of the project:

```text
    ESTIMATE → PRICES
        ↑          ↓
    FORECAST ← (cycle)
```

To generate a market forecast, one needs performance specifications and postulated prices. The quantities from the forecast
combine with component counts from the design to determine the
manufacturing cost estimate, and they determine the per-unit
share of development and fixed costs. These costs in turn determine prices.

If the prices are below those postulated, a joyous success spiral
begins. Forecasts rise, unit costs drop, and prices drop yet further.

If the prices are above those postulated, a disastrous spiral
begins, and all hands must struggle to break it. Performance must
be squeezed up and new applications developed to support larger
forecasts. Costs must be squeezed down to yield lower estimates.
The stress of this cycle is a discipline that often evokes the best
work of marketer and engineer.

It can also bring about ridiculous vacillation. I recall a machine
whose instruction counter popped in or out of memory every six
months during a three-year development cycle. At one phase a
little more performance would be wanted, so the instruction counter was implemented in transistors. At the next phase cost reduction was the theme, so the counter would be implemented as a
memory location. On another project the best engineering manager I ever saw served often as a giant flywheel, his inertia damping the fluctuations that came from market and management
people.

## Documents for a University Department

In spite of the immense differences in purpose and activity, a
similar number of similar documents form the critical set for the
chair of a university department. Almost every decision by
dean, faculty meeting, or chair is a specification or change of
these documents:

- Objectives
- Course descriptions
- Degree requirements
- Research proposals (hence plans, when funded)
- Class schedule and teaching assignments
- Budget
- Space allocation
- Assignment of staff and graduate students

Notice that the components are very like those of the computer project: objectives, product specifications, time allocations,
money allocations, space allocations, and people allocations. Only
the pricing documents are missing; here the legislature does that
task. The similarities are not accidental—the concerns of any management task are what, when, how much, where, and who.

## Documents for a Software Project

In many software projects, people begin by holding meetings to
debate structure; then they start writing programs. No matter how
small the project, however, the manager is wise to begin immediately to formalize at least mini-documents to serve as their database. And they turn out to need documents much like those of other
managers.

**What: objectives.** This defines the need to be met and the goals,
desiderata, constraints, and priorities.

**What: product specifications.** This begins as a proposal and
ends up as the manual and internal documentation. Speed and
space specifications are a critical part.

**When: schedule.**

**How much: budget.**

**Where: space allocation.**

**Who: organization chart.** This becomes intertwined with the
interface specification, as Conway's Law predicts: "Organizations
which design systems are constrained to produce systems which
are copies of the communication structures of these organizations."[^1] Conway goes on to point out that the organization chart
will initially reflect the first system design, which is almost surely
not the right one. If the system design is to be free to change, the
organization must be prepared to change.

## Why Have Formal Documents?

First, writing the decisions down is essential. Only when one
writes do the gaps appear and the inconsistencies protrude. The act
of writing turns out to require hundreds of mini-decisions, and it
is the existence of these that distinguishes clear, exact policies
from fuzzy ones.

Second, the documents will communicate the decisions to others. The manager will be continually amazed that policies they took
for common knowledge are totally unknown by some member of
their team. Since their fundamental job is to keep everybody going in
the same direction, their chief daily task will be communication, not
decision-making, and their documents will immensely lighten this
load.

Finally, a manager's documents give them a database and
checklist. By reviewing them periodically they see where they are, and
they see what changes of emphasis or shifts in direction are needed.

I do not share the salesperson-projected vision of the "management total-information system," wherein the executive strokes an
inquiry into a computer, and a display screen flashes their answer.
There are many fundamental reasons why this will never happen.
One reason is that only a small part—perhaps 20 percent—of the
executive's time is spent on tasks where they need information
from outside their head. The rest is communication: hearing, reporting, teaching, exhorting, counseling, encouraging. But for the fraction that is data-based, the handful of critical documents are vital,
and they will meet almost all needs.

The task of the manager is to develop a plan and then to realize
it. But only the written plan is precise and communicable. Such a
plan consists of documents on what, when, how much, where, and
who. This small set of critical documents encapsulates much of the
manager's work. If their comprehensive and critical nature is recognized in the beginning, the manager can approach them as
friendly tools rather than annoying busywork. They will set their
direction much more crisply and quickly by doing so.

---

[^1]: Conway, M. E. "How do committees invent?" *Datamation*, 14, 4 (April 1968), pp. 28-31.
