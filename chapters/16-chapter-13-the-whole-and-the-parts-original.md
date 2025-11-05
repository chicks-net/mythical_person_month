# 13 - The Whole and the Parts

> I can call spirits from the vasty deep.
> Why so can I, or so can any man; but will they come
> when you do call for them?
>
> SHAKESPEARE, KING HENRY IV, PART I

© The Walt Disney Company

## The Whole and the Parts

The modern magic, like the old, has its boastful practitioners: "I
can write programs that control air traffic, intercept ballistic missiles, reconcile bank accounts, control production lines." To which
the answer comes, "So can I, and so can any man, but do they work
when you do write them?"

How does one build a program to work? How does one test
a program? And how does one integrate a tested set of component
programs into a tested and dependable system? We have touched
upon the techniques here and there; let us now consider them
somewhat more systematically.

## Designing the Bugs Out

**Bug-proofing the definition.** The most pernicious and subtle
bugs are system bugs arising from mismatched assumptions made
by the authors of various components. The approach to conceptual
integrity discussed above in Chapters 4, 5, and 6 addresses these
problems directly. In short, conceptual integrity of the product not
only makes it easier to use, it also makes it easier to build and less
subject to bugs.

So does the detailed, painstaking architectural effort implied
by that approach. V. A. Vyssotsky, of Bell Telephone Laboratories' Safeguard Project, says, "The crucial task is to get the product
defined. Many, many failures concern exactly those aspects that
were never quite specified."[^1] Careful function definition, careful
specification, and the disciplined exorcism of frills of function and
flights of technique all reduce the number of system bugs that
have to be found.

**Testing the specification.** Long before any code exists, the specification must be handed to an outside testing group to be scrutinized for completeness and clarity. As Vyssotsky says, the
developers themselves cannot do this: "They won't tell you they
don't understand it; they will happily invent their way through
the gaps and obscurities."

**Top-down design.** In a very clear 1971 paper, Niklaus Wirth
formalized a design procedure which had been used for years by
the best programmers.[^2] Furthermore, his notions, although stated
for program design, apply completely to the design of complex
systems of programs. The division of system building into architecture, implementation, and realization is an embodiment of
these notions; furthermore, each of the architecture, implementation, and realization can be best done by top-down methods.

Briefly, Wirth's procedure is to identify design as a sequence
of refinement steps. One sketches a rough task definition and a
rough solution method that achieves the principal result. Then one
examines the definition more closely to see how the result differs
from what is wanted, and one takes the large steps of the solution
and breaks them down into smaller steps. Each refinement in the
definition of the task becomes a refinement in the algorithm for
solution, and each may be accompanied by a refinement in the
data representation.

From this process one identifies modules of solution or of data
whose further refinement can proceed independently of other
work. The degree of this modularity determines the adaptability
and changeability of the program.

Wirth advocates using as high-level a notation as is possible
at each step, exposing the concepts and concealing the details until
further refinement becomes necessary.

A good top-down design avoids bugs in several ways. First,
the clarity of structure and representation makes the precise statement of requirements and functions of the modules easier. Second,
the partitioning and independence of modules avoids system bugs.
Third, the suppression of detail makes flaws in the structure more
apparent. Fourth, the design can be tested at each of its refinement
steps, so testing can start earlier and focus on the proper level of
detail at each step.

The process of step-wise refinement does not mean that one
never has to go back, scrap the top level, and start the whole thing
again as he encounters some unexpectedly knotty detail. Indeed,
that happens often. But it is much easier to see exactly when and
why one should throw away a gross design and start over. Many
poor systems come from an attempt to salvage a bad basic design
and patch it with all kinds of cosmetic relief. Top-down design
reduces the temptation.

I am persuaded that top-down design is the most important
new programming formalization of the decade.

**Structured programming.** Another important set of new ideas
for designing the bugs out of programs derives largely from
Dijkstra,[^3] and is built on a theoretical structure by Bohm and
Jacopini.[^4]

Basically the approach is to design programs whose control
structures consist only of loops defined by a statement such as DO
WHILE, and conditional portions delineated into groups of statements marked with brackets and conditioned by an IF ... THEN
... ELSE. Bohm and Jacopini show these structures to be theoretically sufficient; Dijkstra argues that the alternative, unrestrained
branching via GO TO, produces structures that lend themselves
to logical errors.

The basic notion is surely sound. Many criticisms have been
made, and additional control structures, such as an n-way branch
(the so-called CASE statement) for distinguishing among many
contingencies, and a disaster bail-out (GO TO ABNORMAL
END) are very convenient. Further, some have become very doctrinaire about avoiding all GO TO's, and that seems excessive.

The important point, and the one vital to constructing bugfree programs, is that one wants to think about the control structures of a system as control structures, not as individual branch
statements. This way of thinking is a major step forward.

## Component Debugging

The procedures for debugging programs have been through a great
cycle in the past twenty years, and in some ways they are back
where they started. The cycle has gone through four steps, and it
is fun to trace them and see the motivation for each.

**On-machine debugging.** Early machines had relatively poor input-output equipment, and long input-output delays. Typically,
the machine read and wrote paper tape or magnetic tape and
off-line facilities were used for tape preparation and printing. This
made tape input-output intolerably awkward for debugging, so
the console was used instead. Thus debugging was designed to
allow as many trials as possible per machine session.

The programmer carefully designed his debugging procedure
—planning where to stop, what memory locations to examine,
what to find there, and what to do if he didn't. This meticulous
programming of himself as a debugging machine might well take
half as long as writing the computer program to be debugged.

The cardinal sin was to push START boldly without having
segmented the program into test sections with planned stops.

**Memory dumps.** On-machine debugging was very effective. In
a two-hour session, one could get perhaps a dozen shots. But
computers were very scarce, and very costly, and the thought of
all that machine time going to waste was horrifying.

So when high-speed printers were attached on-line, the technique changed. One ran a program until a check failed, and then
dumped the whole memory. Then began the laborious desk work,
accounting for each memory location's contents. The desk time
was not much different than that for on-machine debugging; but
it occurred after the test run, in deciphering, rather than before,
in planning. Debugging for any particular user took much longer,
because test shots depended upon batch turnaround time. The
whole procedure, however, was designed to minimize computer
time use, and to serve as many programmers as possible.

**Snapshots.** The machines on which memory dumping was developed had 2000-4000 words, or 8K to 16K bytes of memory. But
memory sizes grew by leaps and bounds, and total memory dumping became impractical. So people developed techniques for selective dumping, selective tracing, and for inserting snapshots into
programs. The OS/360 TESTRAN is an end-of-the-line in this
direction, allowing one to insert snapshots into a program without
reassembly or recompilation.

**Interactive debugging.** In 1959 Codd and his coworkers[^5] and
Strachey[^6] each reported work aimed at time-shared debugging, a
way of achieving both the instant turnaround of on-machine
debugging and the efficient machine use of batch debugging. The
computer would have multiple programs in memory, ready for
execution. A terminal, controlled only by program, would be associated with each program being debugged. Debugging would be
under control of a supervisory program. When the programmer at
a terminal stopped his program to examine progress or to make
changes, the supervisor would run another program, thus keeping
the machines busy.

Codd's multiprogramming system was developed, but the emphasis was on throughput enhancement by efficient input-output
utilization, and interactive debugging was not implemented. Strachey's ideas were improved and implemented in 1963 in an experimental system for the 7090 by Corbato and colleagues at MIT.[^7]
This development led to the MULTICS, TSS, and other timesharing systems of today.

The chief user-perceived differences between on-machine
debugging as first practiced and the interactive debugging of today
are the facilities made possible by the presence of the supervisory
program and its associated language interpreters. One can program
and debug in a high-level language. Efficient editing facilities
make changes and snapshots easy.

Return to the instant-turnaround capability of on-machine
debugging has not yet brought a return to the preplanning of
debugging sessions. In a sense such preplanning is not so necessary
as before, since machine time doesn't waste away while one sits
and thinks.

Nevertheless, Gold's interesting experimental results show
that three times as much progress in interactive debugging is made
on the first interaction of each session as on subsequent interactions.[^8] This strongly suggests that we are not realizing the potential of interaction due to lack of session planning. The time has
come to dust off the old on-machine techniques.

I find that proper use of a good terminal system requires two
hours at the desk for each two-hour session on the terminal. Half
of this time is spent in sweeping up after the last session: updating
my debugging log, filing updated program listings in my system
notebook, explaining strange phenomena. The other half is spent
in preparation: planning changes and improvements and designing
detailed tests for next time. Without such planning, it is hard to
stay productive for as much as two hours. Without the postsession sweep-up, it is hard to keep the succession of terminal
sessions systematic and forward-moving.

**Test cases.** As for the design of actual debugging procedures and
test cases, Gruenberger has an especially good treatment,[^9] and
there are shorter treatments in other standard texts.[^10][^11]

## System Debugging

The unexpectedly hard part of building a programming system is
system test. I have already discussed some of the reasons for both
the difficulty and its unexpectedness. From all of that, one should
be convinced of two things: system debugging will take longer
than one expects, and its difficulty justifies a thoroughly systematic and planned approach. Let us now see what such an approach
involves.[^12]

**Use debugged components.** Common sense, if not common
practice, dictates that one should begin system debugging only
after the pieces seem to work.

Common practice departs from this in two ways. First is the
bolt-it-together-and-try approach. This seems to be based on the
notion that there will be system (i.e., interface) bugs in addition
to the component bugs. The sooner one puts the pieces together,
the sooner the system bugs will emerge. Somewhat less sophisticated is the notion that by using the pieces to test each other, one
avoids a lot of test scaffolding. Both of these are obviously true,
but experience shows that they are not the whole truth—the use
of clean, debugged components saves much more time in system
testing than that spent on scaffolding and thorough component
test.

A little more subtle is the "documented bug" approach. This
says that a component is ready to enter system test when all the
flaws are found, well before the time when all are fixed. Then in
system testing, so the theory goes, one knows the expected effects
of these bugs and can ignore those effects, concentrating on the
new phenomena.

All this is just wishful thinking, invented to rationalize away
the pain of slipped schedules. One does not know all the expected
effects of known bugs. If things were straightforward, system
testing wouldn't be hard. Furthermore, the fixing of the documented component bugs will surely inject unknown bugs, and
then system test is confused.

**Build plenty of scaffolding.** By scaffolding I mean all programs
and data built for debugging purposes but never intended to be in
the final product. It is not unreasonable for there to be half as
much code in scaffolding as there is in product.

One form of scaffolding is the dummy component, which consists only of interfaces and perhaps some faked data or some small
test cases. For example, a system may include a sort program
which isn't finished yet. Its neighbors can be tested by using a
dummy program that merely reads and tests the format of input
data, and spews out a set of well-formatted meaningless but ordered data.

Another form is the miniature file. A very common form of
system bug is misunderstanding of formats for tape and disk files.
So it is worthwhile to build some little files that have only a few
typical records, but all the descriptions, pointers, etc.

The limiting case of miniature file is the dummy file, which
really isn't there at all. OS/360's Job Control Language provides
such facility, and it is extremely useful for component debugging.

Yet another form of scaffolding are auxiliary programs. Generators for test data, special analysis printouts, cross-reference table
analyzers, are all examples of the special-purpose jigs and fixtures
one may want to build.[^13]

**Control changes.** Tight control during test is one of the impressive techniques of hardware debugging, and it applies as well to
software systems.

First, somebody must be in charge. He and he alone must
authorize component changes or substitution of one version for
another.

Then, as discussed above, there must be controlled copies of
the system: one locked-up copy of the latest versions, used for
component testing; one copy under test, with fixes being installed;
playpen copies where each man can work away on his component,
doing both fixes and extensions.

In System/360 engineering models, one saw occasional
strands of purple wire among the routine yellow wires. When a
bug was found, two things were done. A quick fix was devised and
installed on the system, so testing could proceed. This change was
put on in purple wire, so it stuck out like a sore thumb. It was
entered in the log. Meanwhile, an official change document was
prepared and started into the design automation mill. Eventually
this resulted in updated drawings and wire lists, and a new back
panel in which the change was implemented in printed circuitry
or yellow wire. Now the physical model and the paper were together again, and the purple wire was gone.

Programming needs a purple-wire technique, and it badly
needs tight control and deep respect for the paper that ultimately
is the product. The vital ingredients of such technique are the
logging of all changes in a journal and the distinction, carried
conspicuously in source code, between quick patches and
thought-through, tested, documented fixes.

**Add one component at a time.** This precept, too, is obvious, but
optimism and laziness tempt us to violate it. To do it requires
dummies and other scaffolding, and that takes work. And after all,
perhaps all that work won't be needed? Perhaps there are no bugs?

No! Resist the temptation! That is what systematic system
testing is all about. One must assume that there will be lots of
bugs, and plan an orderly procedure for snaking them out.

Note that one must have thorough test cases, testing the partial systems after each new piece is added. And the old ones, run
successfully on the last partial sum, must be rerun on the new one
to test for system regression.

**Quantize updates.** As the system comes up, the component
builders will from time to time appear, bearing hot new versions
of their pieces—faster, smaller, more complete, or putatively less
buggy. The replacement of a working component by a new version
requires the same systematic testing procedure that adding a new
component does, although it should require less time, for more
complete and efficient test cases will usually be available.

Each team building another component has been using the
most recent tested version of the integrated system as a test bed
for debugging its piece. Their work will be set back by having that
test bed change under them. Of course it must. But the changes
need to be quantized. Then each user has periods of productive
stability, interrupted by bursts of test-bed change. This seems to
be much less disruptive than a constant rippling and trembling.

Lehman and Belady offer evidence that quanta should be very
large and widely spaced or else very small and frequent.[^14] The
latter strategy is more subject to instability, according to their
model. My experience confirms it: I would never risk that strategy
in practice.

Quantized changes neatly accommodate a purple-wire technique. The quick patch holds until the next regular release of the
component, which should incorporate the fix in tested and documented form.

[^1]: Private communication.

[^2]: N. Wirth, "Program development by stepwise refinement," CACM, 14, 4 (April, 1971), pp. 221-227.

[^3]: E. W. Dijkstra, "Structured programming," in J. N. Buxton and B. Randell, eds., Software Engineering Techniques. Brussels: NATO Scientific Affairs Division, 1970, pp. 84-88.

[^4]: C. Bohm and G. Jacopini, "Flow diagrams, Turing machines, and languages with only two formation rules," CACM, 9, 5 (May, 1966), pp. 366-371.

[^5]: E. F. Codd, E. S. Lowry, E. McDonough, and C. A. Scalzi, "Multiprogramming STRETCH: Feasibility considerations," CACM, 2, 11 (Nov., 1959), pp. 13-17.

[^6]: C. Strachey, "Time sharing in large fast computers," Proc. International Conference on Information Processing, Paris: UNESCO, 1959, pp. 336-341.

[^7]: F. J. Corbato, M. Merwin-Daggett, and R. C. Daley, "An experimental time-sharing system," Proc. SJCC, 21 (1962), pp. 335-344.

[^8]: M. M. Gold, "Time-sharing and batch-processing: an experimental comparison of their values in a problem-solving situation," CACM, 12, 5 (May, 1969), pp. 249-259.

[^9]: F. Gruenberger and G. Jaffray, Problems for Computer Solution. New York: Wiley, 1965.

[^10]: T. B. Steel, Jr., in W. Buchholz, ed., Planning a Computer System. New York: McGraw-Hill, 1962.

[^11]: G. J. Myers, "A controlled experiment in program testing and code walkthroughs/inspections," CACM, 21, 9 (Sept., 1978), pp. 760-768.

[^12]: B. W. Boehm, "Software and its impact: a quantitative assessment," Datamation, 19, 5 (May, 1973), pp. 48-59, offers an especially good treatment.

[^13]: A. Evans, Jr., "Basic design concepts," ACM Computer Science Conference, February, 1968, pp. 303-308.

[^14]: M. M. Lehman and L. A. Belady, "Programming system dynamics," presented at ACM SIGOPS Third Symposium on Operating System Principles, October, 1971.
