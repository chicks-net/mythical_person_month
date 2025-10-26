# Chapter 18: Propositions of The Mythical Man-Month: True or False?

> For brevity is very good,
> Where we are, or are not understood.
> — SAMUEL BUTLER, Hudibras

*Brooks asserting a proposition, 1967*
*Photo by J. Alex Langley for Fortune Magazine*

---

Much more is known today about software engineering than
was known in 1975. Which of the assertions in the original 1975
edition have been supported by data and experience? Which
have been disproved? Which have been obsoleted by the changing world? To help you judge, here in outline form is the essence
of the 1975 book—assertions I believed to be true: facts and
rule-of-thumb-type generalizations from experience—extracted
without change of meaning. (You might ask, "If this is all the
original book said, why did it take 177 pages to say it?") Comments in brackets are new.

Most of these propositions are operationally testable. My
hope in putting them forth in stark form is to focus readers'
thoughts, measurements, and comments.

## Chapter 1. The Tar Pit

1.1. A programming systems product takes about nine times
     as much effort as the component programs written separately for private use. I estimate that productizing imposes a factor of three; and that designing, integrating,
     and testing components into a coherent system imposes a
     factor of three; and that these cost components are essentially independent of each other.

1.2. The craft of programming "gratifies creative longings
     built deep within us and delights sensibilities we have in
     common with all people," providing five kinds of joys:
     - The joy of making things
     - The joy of making things that are useful to other
       people
     - The fascination of fashioning puzzle-like objects of interlocking moving parts
     - The joy of always learning, of a nonrepeating task
     - The delight of working in a medium so tractable—
       pure thought-stuff—which nevertheless exists, moves,
       and works in a way that word-objects do not.

1.3. Likewise the craft has special woes inherent in it.
     - Adjusting to the requirement of perfection is the
       hardest part of learning to program.
     - Others set one's objectives and one must depend
       upon things (especially programs) one cannot control;
       the authority is not equal to the responsibility.
     - This sounds worse than it is: actual authority comes
       from momentum of accomplishment.
     - With any creativity come dreary hours of painstaking
       labor; programming is no exception.
     - The programming project converges more slowly the
       nearer one gets to the end, whereas one expects it to
       converge faster as one approaches the end.
     - One's product is always threatened with obsolescence
       before completion. The real tiger is never a match for
       the paper one, unless real use is wanted.

## Chapter 2. The Mythical Man-Month

2.1. More programming projects have gone awry for lack of
     calendar time than for all other causes combined.

2.2. Good cooking takes time; some tasks cannot be hurried
     without spoiling the result.

2.3. All programmers are optimists: "All will go well."

2.4. Because the programmer builds with pure thought-stuff,
     we expect few difficulties in implementation.

2.5. But our ideas themselves are faulty, so we have bugs.

2.6. Our estimating techniques, built around cost-accounting,
     confuse effort and progress. The person-month is a fallacious
     and dangerous myth, for it implies that people and months are interchangeable.

2.7. Partitioning a task among multiple people occasions extra
     communication effort—training and intercommunication.

2.8. My rule of thumb is 1/3 of the schedule for design, 1/6
     for coding, 1/4 for component testing, and 1/4 for system
     testing.

2.9. As a discipline, we lack estimating data.

2.10. Because we are uncertain about our scheduling estimates,
      we often lack the courage to defend them stubbornly
      against management and customer pressure.

2.11. Brooks's Law: Adding workforce to a late software project makes it later.

2.12. Adding people to a software project increases the total effort necessary in three ways: the work and disruption of
      repartitioning itself, training the new people, and added
      intercommunication.

## Chapter 3. The Surgical Team

3.1. Very good professional programmers are ten times as productive as poor ones, at same training and two-year experience level. (Sackman, Grant, and Erickson)

3.2. Sackman, Grant, and Erickson's data showed no correlation whatsoever between experience and performance. I
     doubt the universality of that result.

3.3. A small sharp team is best—as few minds as possible.

3.4. A team of two, with one leader, is often the best use of
     minds. [Note God's plan for marriage.]

3.5. A small sharp team is too slow for really big systems.

3.6. Most experiences with really large systems show the
     brute-force approach to scaling up to be costly, slow, inefficient, and to produce systems that are not conceptually integrated.

3.7. A chief-programmer, surgical-team organization offers a
     way to get the product integrity of few minds and the total productivity of many helpers, with radically reduced
     communication.

## Chapter 4. Aristocracy, Democracy, and System Design

4.1. "Conceptual integrity is the most important consideration
     in system design."

4.2. "The ratio of function to conceptual complexity is the ultimate test of system design," not just the richness of
     function. [This ratio is a measure of ease of use, valid over
     both simple and difficult uses.]

4.3. To achieve conceptual integrity, a design must proceed
     from one mind or a small group of agreeing minds.

4.4. "Separation of architectural effort from implementation is
     a very powerful way of getting conceptual integration on
     very large projects." [Small ones, too.]

4.5. "If a system is to have conceptual integrity, someone
     must control the concepts. That is an aristocracy that
     needs no apology."

4.6. Discipline is good for art. The external provision of an architecture enhances, not cramps, the creative style of an
     implementing group.

4.7. A conceptually integrated system is faster to build and to
     test.

4.8. Much of software architecture, implementation, and realization can proceed in parallel. [Hardware and software
     design can likewise proceed in parallel.]

## Chapter 5. The Second-System Effect

5.1. Early and continuous communication can give the architect good cost readings and the builder confidence in the
     design, without blurring the clear division of responsibilities.

5.2. How an architect can successfully influence implementation:
     - Remember that the builder has the creative responsibility for implementation; the architect only suggests.
     - Always be ready to suggest a way of implementing
       anything one specifies; be prepared to accept any
       other equally good way.
     - Deal quietly and privately in such suggestions.
     - Be ready to forgo credit for suggested improvements.
     - Listen to the builder's suggestions for architecture improvements.

5.3. The second is the most dangerous system a person ever
     designs; the general tendency is to over-design it.

5.4. OS/360 is a good example of the second-system effect.
     [Windows NT seems to be a 1990s example.]

5.5. Assigning a priori values in bytes and microseconds to
     functions is a worthwhile discipline.

## Chapter 6. Passing the Word

6.1. Even when a design team is large, the results must be reduced to writing by one or two, in order that the mini-decisions be consistent.

6.2. It is important to explicitly define the parts of an architecture that are not prescribed as carefully as those that are.

6.3. One needs both a formal definition of a design, for precision, and a prose definition for comprehensibility.

6.4. One of the formal and prose definitions must be standard,
     and the other derivative. Either definition can serve in
     either role.

6.5. An implementation, including a simulation, can serve as
     an architectural definition; such use has formidable disadvantages.

6.6. Direct incorporation is a very clean technique for enforcing an architectural standard in software. [In hardware,
     too—consider the Mac WIMP interface built into ROM.]

6.7. An architectural "definition will be cleaner and the [architectural] discipline tighter if at least two implementations are built initially."

6.8. It is important to allow telephone interpretations by an architect in response to implementers' queries; it is imperative to log these and publish them. [Electronic mail is
     now the medium of choice.]

6.9. "The project manager's best friend is their daily adversary,
     the independent product-testing organization."

## Chapter 7. Why Did the Tower of Babel Fail?

7.1. The Tower of Babel project failed because of lack of communication and of its consequent, organization.

### Communication

7.2. "Schedule disaster, functional misfit, and system bugs all
     arise because the left hand doesn't know what the right
     hand is doing." Teams drift apart in assumptions.

7.3. Teams should communicate with one another in as many
     ways as possible: informally, by regular project meetings
     with technical briefings, and via a shared formal project
     workbook. [And by electronic mail.]

### Project Workbook

7.4. A project workbook is "not so much a separate document
     as it is a structure imposed on the documents that the
     project will be producing anyway."

7.5. "All the documents of the project need to be part of this
     [workbook] structure."

7.6. The workbook structure needs to be designed carefully
     and early.

7.7. Properly structuring the on-going documentation from
     the beginning "molds later writing into segments that fit
     into that structure" and will improve the product manuals.

7.8. "Each team member should see all the [workbook] material." [I would now say, each team member should be able
     to see all of it. That is, World-Wide Web pages would suffice.]

7.9. Timely updating is of critical importance.

7.10. The user needs to have attention especially drawn to
      changes since their last reading, with remarks on their significance.

7.11. The OS/360 Project workbook started with paper and
      switched to microfiche.

7.12. Today [even in 1975], the shared electronic notebook is a
      much better, cheaper, and simpler mechanism for achieving all these goals.

7.13. One still has to mark the text with [the functional equivalent of] change bars and revision dates. One still needs
      a LIFO electronic change summary.

7.14. Parnas argues strongly that the goal of everyone seeing
      everything is totally wrong; parts should be encapsulated
      so that no one needs to or is allowed to see the internals
      of any parts other than their own, but should see only the
      interfaces.

7.15. Parnas's proposal is a recipe for disaster. [I have been quite
      convinced otherwise by Parnas, and totally changed my mind.]

### Organization

7.16. The purpose of organization is to reduce the amount of
      communication and coordination necessary.

7.17. Organization embodies division of labor and specialization of
      function in order to obviate communication.

7.18. The conventional tree organization reflects the authority
      structure principle that no person can serve two masters.

7.19. The communication structure in an organization is a network, not a tree, so all kinds of special organization mechanisms ("dotted lines") have to be devised to overcome
      the communication deficiencies of the tree-structured organization.

7.20. Every subproject has two leadership roles to be filled, that
      of the producer and that of the technical director, or architect.
      The functions of the two roles are quite distinct and require different talents.

7.21. Any of three relationships among the two roles can be
      quite effective:
      - The producer and director can be the same.
      - The producer may be boss, and the director the producer's right-hand person.
      - The director may be boss, and the producer the director's right-hand person.

## Chapter 8. Calling the Shot

8.1. One cannot accurately estimate the total effort or schedule
     of a programming project by simply estimating the coding
     time and multiplying by factors for the other parts of the
     task.

8.2. Data for building isolated small systems are not applicable
     to programming systems projects.

8.3. Programming effort goes as a power of program size.

8.4. Some published studies show the exponent to be about
     1.5. [Boehm's data do not at all agree with this, but vary from
     1.05 to 1.2.][^1]

8.5. Portman's ICL data show full-time programmers applying
     only about 50 percent of their time to programming and
     debugging, versus other overhead-type tasks.

8.6. Aron's IBM data show productivity varying from 1.5 K
     lines of code (KLOC) per person-year to 10 KLOC/person-year
     as a function of the number of interactions among system
     parts.

8.7. Harr's Bell Labs data show productivities on operating-systems-type work to run about 0.6 KLOC/person-year and
     on compiler-type work about 2.2 KLOC/person-year for finished products.

8.8. Brooks's OS/360 data agrees with Harr's: 0.6-0.8 KLOC/
     person-year on operating systems and 2-3 KLOC/person-year
     on compilers.

8.9. Corbató's MIT Project MULTICS data show productivity
     of 1.2 KLOC/person-year on a mix of operating systems and
     compilers, but these are PL/I lines of code, whereas all the
     other data are assembler lines of code!

8.10. Productivity seems constant in terms of elementary statements.

8.11. Programming productivity may be increased as much as
      five times when a suitable high-level language is used.

## Chapter 9. Ten Pounds in a Five-Pound Sack

9.1. Aside from running time, the memory space occupied by a
     program is a principal cost. This is especially true for operating systems, where much is resident all the time.

9.2. Even so, money spent on memory for program residence
     may yield very good functional value per dollar, better
     than other ways of investing in configuration. Program
     size is not bad; unnecessary size is.

9.3. The software builder must set size targets, control size,
     and devise size-reduction techniques, just as the hardware builder does for components.

9.4. Size budgets must be explicit not only about resident size
     but also about the disk accesses occasioned by program
     fetches.

9.5. Size budgets have to be tied to function assignments; define exactly what a module must do when you specify
     how big it must be.

9.6. On large teams, subteams tend to suboptimize to meet
     their own targets rather than think about the total effect
     on the user. This breakdown in orientation is a major hazard of large projects.

9.7. All during implementation, the system architects must
     maintain constant vigilance to ensure continued system
     integrity.

9.8. Fostering a total-system, user-oriented attitude may well
     be the most important function of the programming manager.

9.9. An early policy decision is to decide how fine-grained the
     user choice of options will be, since packaging them in
     clumps saves memory space [and often marketing costs].

9.10. The size of the transient area, hence of the amount of program per disk fetch, is a crucial decision, since performance is a super-linear function of that size. [This whole
      decision has been obsoleted, first by virtual memory, then
      by cheap real memory. Users now typically buy enough
      real memory to hold all the code of major applications.]

9.11. To make good space-time tradeoffs, a team needs to be
      trained in the programming techniques peculiar to a particular language or machine, especially a new one.

9.12. Programming has a technology, and every project needs
      a library of standard components.

9.13. Program libraries should have two versions of each component, the quick and the squeezed. [This seems obsolete
      today.]

9.14. Lean, spare, fast programs are almost always the result of
      strategic breakthrough, rather than tactical cleverness.

9.15. Often such a breakthrough will be a new algorithm.

9.16. More often, the breakthrough will come from redoing the
      representation of the data or tables. Representation is the essence of programming.

## Chapter 10. The Documentary Hypothesis

10.1. "The hypothesis: Amid a wash of paper, a small number
      of documents become the critical pivots around which
      every project's management revolves. These are the manager's chief personal tools."

10.2. For a computer development project, the critical documents are the objectives, manual, schedule, budget, organization chart, floorspace allocation, and the estimate,
      forecast, and prices of the machine itself.

10.3. For a university department, the critical documents are
      similar: the objectives, degree requirements, course descriptions, research proposals, class schedule and teaching plan, budget, floorspace allocation, and assignments
      of staff and graduate assistants.

10.4. For a software project, the needs are the same: the objectives, user manual, internals documentation, schedule,
      budget, organization chart, and floorspace allocation.

10.5. Even on a small project, therefore, the manager should
      from the beginning formalize such a set of documents.

10.6. Preparing each document of this small set focuses
      thought and crystallizes discussion. The act of writing requires hundreds of mini-decisions, and it is the existence
      of these that distinguish clear, exact policies from fuzzy
      ones.

10.7. Maintaining each critical document provides a status surveillance and warning mechanism.

10.8. Each document itself serves as a checklist and a database.

10.9. The project manager's fundamental job is to keep everybody going in the same direction.

10.10. The project manager's chief daily task is communication,
       not decision-making; the documents communicate the
       plans and decisions to the whole team.

10.11. Only a small part of a technical project manager's time—
       perhaps 20 percent—is spent on tasks where they need information from outside their head.

10.12. For this reason, the touted market concept of a "management total-information system" to support executives is
       not based on a valid model of executive behavior.

## Chapter 11. Plan to Throw One Away

11.1. Chemical engineers have learned not to take a process
      from the lab bench to the factory in one step, but to build
      a pilot plant to give experience in scaling quantities up and
      operating in nonprotective environments.

11.2. This intermediate step is equally necessary for programming products, but software engineers do not yet routinely field-test a pilot system before undertaking to
      deliver the real product. [This has now become common
      practice, with a beta version. This is not the same as a prototype with limited function, an alpha version, which I
      would also advocate.]

11.3. For most projects, the first system built is barely usable:
      too slow, too big, too hard to use, or all three.

11.4. The discard and redesign may be done in one lump, or
      piece-by-piece, but it will be done.

11.5. Delivering the first system, the throwaway, to users will
      buy time, but only at the cost of agony for the user, distraction for the builders supporting it while they do the
      redesign, and a bad reputation for the product that will
      be hard to live down.

11.6. Hence, plan to throw one away; you will, anyhow.

11.7. "The programmer delivers satisfaction of a user need
      rather than any tangible product." (Cosgrove)

11.8. Both the actual need and the user's perception of that
      need will change as programs are built, tested, and used.

11.9. The tractability and the invisibility of the software product expose its builders (exceptionally) to perpetual changes
      in requirements.

11.10. Some valid changes in objectives (and in development
       strategies) are inevitable, and it is better to be prepared for
       them than to assume that they will not come.

11.11. The techniques for planning a software product for change,
       especially structured programming with careful module
       interface documentation, are well known but not uniformly practiced. It also helps to use table-driven techniques wherever possible. [Modern memory costs and
       sizes make such techniques better and better.]

11.12. Use high-level language, compile-time operations, incorporations of declarations by reference, and self-documenting techniques to reduce errors induced by change.

11.13. Quantify changes into well-defined numbered versions.
       [Now standard practice.]

### Plan the Organization for Change

11.14. Programmer reluctance to document designs comes not
       so much from laziness as from the hesitancy to undertake
       defense of decisions that the designer knows are tentative. (Cosgrove)

11.15. Structuring an organization for change is much harder
       than designing a system for change.

11.16. The project boss must work at keeping the managers and
       the technical people as interchangeable as their talents allow; in particular, one wants to be able to move people
       easily between technical and managerial roles.

11.17. The barriers to effective dual-ladder organization are sociological, and they must be fought with constant vigilance and energy.

11.18. It is easy to establish corresponding salary scales for the
       corresponding rungs on a dual ladder, but it requires
       strong proactive measures to give them corresponding
       prestige: equal offices, equal support services, over-compensating management actions.

11.19. Organizing as a surgical team is a radical attack on all aspects of this problem. It is really the long-run answer to
       the problem of flexible organization.

### Two Steps Forward and One Step Back—Program Maintenance

11.20. Program maintenance is fundamentally different from
       hardware maintenance; it consists chiefly of changes that
       repair design defects, add incremental function, or adapt
       to changes in the use environment or configuration.

11.21. The total lifetime cost of maintaining a widely used program is typically 40 percent or more of the cost of developing it.

11.22. Maintenance cost is strongly affected by the number of
       users. More users find more bugs.

11.23. Campbell points out an interesting drop-and-climb curve
       in bugs per month over a product's life.

11.24. Fixing a defect has a substantial (20 to 50 percent) chance
       of introducing another.

11.25. After each fix, one must run the entire bank of test cases
       previously run against a system to ensure that it has not
       been damaged in an obscure way.

11.26. Methods of designing programs so as to eliminate or at
       least illuminate side effects can have an immense payoff
       in maintenance costs.

11.27. So can methods of implementing designs with fewer people, fewer interfaces, and fewer bugs.

### One Step Forward and One Step Back—System Entropy Rises over Lifetime

11.28. Lehman and Belady find that the total number of modules
       increases linearly with the release number of a large operating system (OS/360), but that the number of modules
       affected increases exponentially with the release number.

11.29. All repairs tend to destroy structure, to increase the entropy and disorder of a system. Even the most skillful program maintenance only delays the program's subsidence
       into unfixable chaos, from which there has to be a
       ground-up redesign. [Many of the real needs for upgrading a program, such as performance, especially attack its
       internal structural boundaries. Often the original boundaries occasioned the deficiencies that surface later.]

## Chapter 12. Sharp Tools

12.1. The manager of a project needs to establish a philosophy
      and set aside resources for the building of common tools,
      and at the same time to recognize the need for personalized tools.

12.2. Teams building operating systems need a target machine
      of their own on which to debug; it needs maximum
      memory rather than maximum speed, and a system programmer to keep the standard software current and
      serviceable.

12.3. The debugging machine, or its software, also needs to be
      instrumented, so that counts and measurements of all
      kinds of program parameters can be automatically made.

12.4. The requirement for target machine use has a peculiar
      growth curve: low activity followed by explosive growth,
      then leveling off.

12.5. System debugging, like astronomy, has always been done
      chiefly at night.

12.6. Allocating substantial blocks of target machine time to
      one subteam at a time proved the best way to schedule,
      much better than interleaving subteam use, despite theory.

12.7. This preferred method of scheduling scarce computers by
      blocks has survived 20 years [in 1975] of technology
      change because it is most productive. [It still is, in 1995].

12.8. If a target computer is new, one needs a logical simulator
      for it. One gets it sooner, and it provides a dependable debugging vehicle even after one has a real machine.

12.9. A master program library should be divided into (1) a set
      of individual playpens, (2) a system integration sublibrary, currently under system test, and (3) a released version. Formal separation and progression gives control.

12.10. The tool that saves the most labor in a programming project is probably a text-editing system.

12.11. Voluminosity in system documentation does indeed introduce a new kind of incomprehensibility [see Unix, for
       example], but it is far preferable to the severe underdocumentation that is so common.

12.12. Build a performance simulator, outside in, top down.
       Start it very early. Listen when it speaks.

### High-Level Language

12.13. Only sloth and inertia prevent the universal adoption of
       high-level language and interactive programming. [And
       today they have been adopted universally]

12.14. High-level language improves not only productivity but
       also debugging; fewer bugs and easier to find.

12.15. The classical objections of function, object-code space,
       and object-code speed have been made obsolete by the
       advance of language and compiler technology.

12.16. The only reasonable candidate for system programming
       today is PL/I. [No longer true.]

### Interactive Programming

12.17. Interactive systems will never displace batch systems for
       some applications. [Still true.]

12.18. Debugging is the hard and slow part of system programming, and slow turnaround is the bane of debugging.

12.19. Limited evidence shows that interactive programming at
       least doubles productivity in system programming.

## Chapter 13. The Whole and the Parts

13.1. The detailed, painstaking architectural effort implied in
      Chapters 4, 5, and 6 not only makes a product easier to
      use, it makes it easier to build and reduces the number of
      system bugs that have to be found.

13.2. Vyssotsky says "Many, many failures concern exactly
      those aspects that were never quite specified."

13.3. Long before any code itself, the specification must be
      handed to an outside testing group to be scrutinized for
      completeness and clarity. The developers themselves cannot do this. (Vyssotsky)

13.4. "Wirth's top-down design [by stepwise refinement] is the
      most important new programming formalization of the
      [1965-1975] decade."

13.5. Wirth advocates using as high-level a notation as possible
      on each step.

13.6. A good top-down design avoids bugs in four ways.

13.7. Sometimes one has to go back, scrap a high level, and
      start over.

13.8. Structured programming, designing programs whose
      control structures consist only of a specified set that govern blocks of code (versus miscellaneous branching), is a
      sound way to avoid bugs and is the right way to think.

13.9. Gold's experimental results show three times as much
      progress is made in the first interaction of an interactive
      debugging session as on subsequent interactions. It still
      pays to plan debugging carefully before signing on. [I
      think it still does, in 1995.]

13.10. I find that proper use of a good [quick response interactive debugging] system requires two hours at the desk for
       each two-hour session on the machine: one hour in
       sweeping up and documenting after the session and one
       in planning changes and tests for the next time.

13.11. System debugging (in contrast to component debugging)
       will take longer than one expects.

13.12. The difficulty of system debugging justifies a thoroughly
       systematic and planned approach.

13.13. One should begin system debugging only after the pieces
       seem to work (versus bolt-it-together-and-try in order to
       smoke out the interface bugs; and versus starting system
       debugging when the component bugs are fully known
       but not fixed.) [This is especially true for teams.]

13.14. It is worthwhile to build lots of debugging scaffolding and
       test code, perhaps even 50 percent as much as the product
       being debugged.

13.15. One must control and document changes and versions,
       with team members working in playpen copies.

13.16. Add one component at a time during system debugging.

13.17. Lehman and Belady offer evidence the change quanta
       should be large and infrequent or else very small and
       frequent. The latter is more subject to instability. [A Microsoft team makes small frequent quanta work. The
       growing system is rebuilt every night.]

## Chapter 14. Hatching a Catastrophe

14.1. "How does a project get to be a year late? ... One day at
      a time."

14.2. Day-by-day schedule slippage is harder to recognize,
      harder to prevent, and harder to make up than calamities.

14.3. The first step in controlling a big project on a tight schedule is to have a schedule, made up of milestones and dates
      for them.

14.4. Milestones must be concrete, specific, measurable events
      defined with knife-edge sharpness.

14.5. A programmer will rarely lie about milestone progress, if
      the milestone is so sharp they can't deceive themselves.

14.6. Studies of estimating behavior by government contractors
      on large projects show that activity time estimates revised
      carefully every two weeks do not significantly change as
      the start time approaches, that during the activity overestimates come steadily down; and that underestimates do
      not change until about three weeks before scheduled
      completion.

14.7. Chronic schedule slippage is a morale-killer. [Jim McCarthy of Microsoft says, "If you miss one deadline, make
      sure you make the next one."][^2]

14.8. Hustle is essential for great programming teams, just as
      for great baseball teams.

14.9. There is no substitute for a critical-path schedule to enable
      one to tell which slips matter how much.

14.10. The preparation of a critical-path chart is the most valuable part of its use, since laying out the network, identifying the dependencies, and estimating the segments
       force a great deal of very specific planning very early in a
       project.

14.11. The first chart is always terrible, and one invents and invents in making the next one.

14.12. A critical path chart answers the demoralizing excuse,
       "The other piece is late, anyhow."

14.13. Every boss needs both exception information that requires action and a status picture for education and distant early warning.

14.14. Getting the status is hard, since subordinate managers
       have every reason not to share it.

14.15. By bad action, a boss can guarantee to squelch full status
       disclosure; conversely, carefully separating status reports
       and accepting them without panic or preemption will encourage honest reporting.

14.16. One must have review techniques by which true status
       becomes known to all players. For this purpose a milestone schedule and completion document is the key.

14.17. Vyssotsky: "I have found it handy to carry both 'scheduled' (boss's dates) and 'estimated' (lowest-level manager's dates) dates in the milestone report. The project
       manager has to keep their fingers off the estimated dates."

14.18. A small Plans and Controls team that maintains the milestone report is invaluable for a large project.

## Chapter 15. The Other Face

15.1. For the program product, the other face to the user, the
      documentation, is fully as important as the face to the machine.

15.2. Even for the most private of programs, prose documentation is necessary, for memory will fail the user-author.

15.3. Teachers and managers have by and large failed to instill
      in programmers an attitude about documentation that
      will inspire for a lifetime, overcoming sloth and schedule
      pressure.

15.4. This failure is not due so much to lack of zeal or eloquence
      as to a failure to show how to document effectively and
      economically.

15.5. Most documentation fails in giving too little overview.
      Stand way back and zoom in slowly.

15.6. The critical user documentation should be drafted before
      the program is built, for it embodies basic planning decisions. It should describe nine things (see the chapter).

15.7. A program should be shipped with a few test cases, some
      for valid input data, some for borderline input data, and
      some for clearly invalid input data.

15.8. Documentation of program internals, for the person who
      must modify it, also demands a prose overview, which
      should contain five kinds of things (see the chapter).

15.9. The flow chart is a most thoroughly oversold piece of program documentation; the detailed blow-by-blow flow
      chart is a nuisance, obsoleted by written high-level languages. (A flow chart is a diagrammed high-level language.)

15.10. Few programs need more than a one-page flow chart, if
       that. [MILSPEC documentation requirements are really
       wrong on this point.]

15.11. One does indeed need a program structure graph, which
       does not need the ANSI flow-charting standards.

15.12. To keep documentation maintained, it is crucial that it be
       incorporated in the source program, rather than kept as a
       separate document.

15.13. Three notions are key to minimizing the documentation
       burden:
       - Use parts of the program that have to be there anyway, such as names and declarations, to carry as
         much of the documentation as possible.
       - Use space and format to show subordination and
         nesting and to improve readability.
       - Insert the necessary prose documentation into the
         program as paragraphs of comment, especially as
         module headers.

15.14. In documentation for use by program modifiers, tell why
       things are like they are, rather than merely how they are.
       Purpose is the key to understanding; even high-level language syntax does not at all convey purpose.

15.15. Self-documenting programming techniques find their
       greatest use and power in high-level languages used with
       on-line systems, which are the tools one should be using.

## Original Epilogue

E.1. Software systems are perhaps the most intricate and complex (in terms of number of distinct kinds of parts) of the
     things humanity makes.

E.2. The tar pit of software engineering will continue to be
     sticky for a long time to come.

---

[^1]: B. Boehm, *Software Engineering Economics*. Englewood Cliffs, N.J.: Prentice-Hall, 1981, pp. 477-496.

[^2]: J. McCarthy, *Dynamics of Software Development*. Redmond, Wash.: Microsoft Press, 1995, p. 26.
