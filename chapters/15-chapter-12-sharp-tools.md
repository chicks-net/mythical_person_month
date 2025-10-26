# Chapter 12: Sharp Tools

> A good workman is known by his tools.
> — PROVERB

*A. Pisano, "Lo Scultore," from the Campanile di Santa Maria del Fiore, Florence, c. 1335*
*Scala/Art Resource, NY*

---

Even at this late date, many programming projects are still operated like machine shops so far as tools are concerned. Each master
mechanic has their own personal set, collected over a lifetime and
carefully locked and guarded—the visible evidences of personal
skills. Just so, the programmer keeps little editors, sorts, binary
dumps, disk space utilities, etc., stashed away in their file.

Such an approach, however, is foolish for a programming
project. First, the essential problem is communication, and individualized tools hamper rather than aid communication. Second,
the technology changes when one changes machines or working
language, so tool lifetime is short. Finally, it is obviously much
more efficient to have common development and maintenance of
the general-purpose programming tools.

General-purpose tools are not enough, however. Both specialized needs and personal preferences dictate the need for specialized tools as well; so in discussing programming teams I have
postulated one toolmaker per team. This person masters all the common tools and is able to instruct their client-boss in their use. They
also build the specialized tools their boss needs.

The manager of a project, then, needs to establish a philosophy and set aside resources for the building of common tools. At
the same time they must recognize the need for specialized tools, and
not begrudge their working teams their own tool-building. This
temptation is insidious. One feels that if all those scattered tool
builders were gathered in to augment the common tool team,
greater efficiency would result. But it is not so.

What are the tools about which the manager must philosophize, plan, and organize? First, a computer facility. This requires
machines, and a scheduling philosophy must be adopted. It requires an operating system, and service philosophies must be established. It requires language, and a language policy must be laid
down. Then there are utilities, debugging aids, test-case generators,
and a text-processing system to handle documentation. Let us look
at these one by one.[^1]

## Target Machines

Machine support is usefully divided into the target machine and the
vehicle machines. The target machine is the one for which software
is being written, and on which it must ultimately be tested. The
vehicle machines are those that provide the services used in building the system. If one is building a new operating system for an
old machine, it may serve not only as the target, but as the vehicle
as well.

**What kind of target facility?** Teams building new supervisors or
other system-heart software will of course need machines of their
own. Such systems will need operators and a system programmer
or two who keeps the standard support on the machine current
and serviceable.

If a separate machine is needed, it is a rather peculiar thing—
it need not be fast, but it needs at least a million bytes of main
storage, a hundred million bytes of on-line disk, and terminals.
Only alphanumeric terminals are needed, but they must go much
faster than the 15 characters per second that characterizes typewriters. A large memory adds greatly to productivity by allowing
overlaying and size trimming to be done after functional testing.

The debugging machine, or its software, also needs to be instrumented, so that counts and measurements of all kinds of program parameters can be automatically made during debugging.
Memory-use patterns, for instance, are powerful diagnostics of
the causes of weird logical behavior or unexpectedly slow performance.

**Scheduling.** When the target machine is new, as when its first
operating system is being built, machine time is scarce, and scheduling it is a major problem. The requirement for target machine
time has a peculiar growth curve. In OS/360 development we had
good System/360 simulators and other vehicles. From previous
experience we projected how many hours of S/360 time we would
need, and began to acquire early machines from factory production. But they sat idle, month after month. Then all at once all 16
systems were fully loaded, and rationing was the problem. The
utilization looked something like Fig. 12.1. Everyone began to
debug their first components at the same time, and thereafter most
of the team was constantly debugging something.

```text
Model 40 hours
per month
    |
    |                                     ╱
    |                                   ╱
    |                                 ╱
    |                               ╱
    |                             ╱
    |                           ╱
    |                         ╱
    |_______________________╱___________________
                       Jan '65                '66
```

Fig. 12.1: Growth in use of target machines

We centralized all our machines and tape library and set up a
professional and experienced machine-room team to run them. To
maximize scarce S/360 time, we ran all debugging runs in batch
on whichever system was free and appropriate. We tried for four
shots per day (two-and-one-half-hour turnaround) and demanded four-hour turnaround. An auxiliary 1401 with terminals
was used to schedule runs, to keep track of the thousands of jobs,
and to monitor turnaround time.

But all that organization was quite overdone. After a few
months of slow turnaround, mutual recriminations, and other
agony, we went to allocating machine time in substantial blocks.
The whole fifteen-person sort team, for example, would be given a
system for a four-to-six-hour block. It was up to them to schedule
themselves on it. If it sat idle, no outsider could use it.

That, it develops, was a better way to allocate and schedule.
Although machine utilization may have been a little lower (and
often it wasn't), productivity was way up. For each person on such
a team, ten shots in a six-hour block are far more productive than
ten shots spaced three hours apart, because sustained concentration reduces thinking time. After such a sprint, a team usually
needed a day or two to catch up on the paperwork before asking
for another block. Often as few as three programmers can fruitfully share and subschedule a block of time. This seems to be the
best way to use a target machine when debugging a new operating
system.

It has always been so in practice, though never in theory.
System debugging has always been a graveyard-shift occupation,
like astronomy. Twenty years ago, on the 701, I was initiated into
the productive informality of the predawn hours, when all the
machine-room bosses are fast asleep at home, and the operators
are disinclined to be sticklers for rules. Three machine generations
have passed; technologies have changed totally; operating systems
have arisen; and yet this preferred method of working hasn't
changed. It endures because it is most productive. The time has
come to recognize its productivity and embrace the fruitful practice openly.

## Vehicle Machines and Data Services

**Simulators.** If the target computer is new, one needs a logical
simulator for it. This gives a debugging vehicle long before the real
target exists. Equally important, it gives access to a dependable
debugging vehicle even after one has a target machine available.

Dependable is not the same as accurate. The simulator will
surely fail in some respect to be a faithful and accurate implementation of the new machine's architecture. But it will be the same
implementation from one day to the next, and the new hardware
will not.

We are accustomed nowadays to having computer hardware
work correctly almost all the time. Unless an application programmer sees a system behaving inconsistently from run to identical
run, they are well advised to look for bugs in their code rather than in
their engine.

This experience, however, is bad training for the programming
of support for a new machine. Lab-built, preproduction, or early
hardware does not work as defined, does not work reliably, and
does not stay the same from day to day. As bugs are found,
engineering changes are made in all machine copies, including
those of the programming group. This shifting base is bad enough.
Hardware failures, usually intermittent, are worse. The uncertainty is worst of all, for it robs one of incentive to dig diligently
in their code for a bug—it may not be there at all. So a dependable
simulator on a well-aged vehicle retains its usefulness far longer
than one would expect.

**Compiler and assembler vehicles.** For the same reasons, one
wants compilers and assemblers that run on dependable vehicles
but compile object code for the target system. This can then start
being debugged on the simulator.

With high-level language programming, one can do much of
the debugging by compiling for and testing object code on the
vehicle machine before beginning to test target-machine code at
all. This gives the efficiency of direct execution, rather than that
of simulation, combined with the dependability of the stable machine.

**Program libraries and accounting.** A very successful and important use of a vehicle machine in the OS/360 development effort
was for the maintenance of program libraries. A system developed
under the leadership of W. R. Crowley had two 7010's connected,
sharing a large disk data bank. The 7010's also provided an S/360
assembler. All the code tested or under test was kept in this library, both source code and assembled load modules. The library
was in fact divided into sublibraries with different access rules.

First, each group or programmer had an area where they kept
copies of their programs, their test cases, and the scaffolding they
needed for component testing. In this playpen area there were no
restrictions on what a person could do with their own programs; they
were theirs.

When a person had their component ready for integration into a
larger piece, they passed a copy over to the manager of that larger
system, who put this copy into a system integration sublibrary. Now
the original programmer could not change it, except by permission
of the integration manager. As the system came together, the latter
would proceed with all sorts of system tests, identifying bugs and
getting fixes.

From time to time a system version would be ready for wider
use. Then it would be promoted to the current version sublibrary.
This copy was sacrosanct, touched only to fix crippling bugs. It
was available for use in integration and testing of all new module
versions. A program directory on the 7010 kept track of each
version of each module, its status, its whereabouts, and its
changes.

Two notions are important here. The first is control, the idea
of program copies belonging to managers who alone can authorize
their change. The second is that of formal separation and progression
from the playpen, to integration, to release.

In my opinion this was one of the best-done things in the
OS/360 effort. It is a piece of management technology that seems
to have been independently developed on several massive programming projects including those at Bell Labs, ICL, and Cambridge University.[^2] It is applicable to documentation as well as to
programs. It is an indispensable technology.

**Program tools.** As new debugging techniques appear, the old
ones diminish but do not vanish. Thus one needs dumps, source-file editors, snapshot dumps, even traces.

Likewise one needs a full set of utilities for putting decks on
disks, making tape copies, printing files, changing catalogs. If one
commissions a project toolmaker early in the process, these can be
done once and can be ready by time they are needed.

**Documentation system.** Among all tools, the one that saves the
most labor may well be a computerized text-editing system, operating on a dependable vehicle. We had a very handy one, devised
by J. W. Franklin. Without it I expect OS/360 manuals would have
been far later and more cryptic. There are those who would argue
that the OS/360 six-foot shelf of manuals represents verbal diarrhea, that the very voluminosity introduces a new kind of incomprehensibility. And there is some truth in that.

But I respond in two ways. First, the OS/360 documentation
is overwhelming in bulk, but the reading plan is carefully laid out;
if one uses it selectively, they can ignore most of the bulk most of
the time. One must consider the OS/360 documentation as a library or an encyclopedia, not a set of mandatory texts.

Second, this is far preferable to the severe underdocumentation that characterizes most programming systems. I will quickly
agree, however, that the writing could be vastly improved in some
places, and that the result of better writing would be reduced bulk.
Some parts (e.g., Concepts and Facilities) are very well-written now.

**Performance simulator.** Better have one. Build it outside-in, as
we will discuss in the next chapter. Use the same top-down design
for the performance simulator, the logical simulator, and the product. Start it very early. Listen to it when it speaks.

## High-Level Language and Interactive Programming

The most important two tools for system programming today are
two that were not used in OS/360 development almost a decade
ago. They are still not widely used, but all evidence points to their
power and applicability. They are (1) high-level language and
(2) interactive programming. I am convinced that only inertia and
sloth prevent the universal adoption of these tools; the technical
difficulties are no longer valid excuses.

**High-level language.** The chief reasons for using a high-level
language are productivity and debugging speed. We have discussed productivity earlier (Chapter 8). There is not a lot of numerical evidence, but what there is suggests improvement by
integral factors, not just incremental percentages.

The debugging improvement comes from the fact that there
are fewer bugs, and they are easier to find. There are fewer because
one avoids an entire level of exposure to error, a level on which
one makes not only syntactic errors but semantic ones, such as
misusing registers. The bugs are easier to find because the compiler
diagnostics help find them and, more important, because it is very
easy to insert debugging snapshots.

For me, these productivity and debugging reasons are overwhelming. I cannot easily conceive of a programming system I
would build in assembly language.

Well, what about the classical objections to such a tool? There
are three: It doesn't let me do what I want. The object code is too
big. The object code is too slow.

As to function, I believe the objection is no longer valid. All
testimony indicates that one can do what they need to do, but that
it takes work to find out how, and one may occasionally need
unlovely artifices.[^3]

As to space, the new optimizing compilers are beginning to be
very satisfactory, and this improvement will continue.

As to speed, optimizing compilers now produce some code
that is faster than most programmer's handwritten code. Furthermore, one can usually solve speed problems by replacing from one
to five percent of a compiler-generated program by handwritten
substitute after the former is fully debugged.[^4]

What high-level language should one use for system programming? The only reasonable candidate today is PL/I.[^5] It has a very
full set of functions; it is matched to operating system environments; and a variety of compilers are available, some interactive,
some fast, some very diagnostic, and some producing highly optimized code. I myself find it faster to work out algorithms in APL;
then I translate these to PL/I for matching to the system environment.

**Interactive programming.** One of the justifications for MIT's
Multics project was its usefulness for building programming systems. Multics (and following it, IBM's TSS) differs in concept from
other interactive computing systems in exactly those respects necessary for systems programming: many levels of sharing and protection for data and programs, extensive library management, and
facilities for cooperative work among terminal users. I am convinced that interactive systems will never displace batch systems
for many applications. But I think the Multics team has made its
most convincing case in the system-programming application.

There is not yet much evidence available on the true fruitfulness of such apparently powerful tools. There is a widespread
recognition that debugging is the hard and slow part of system
programming, and slow turnaround is the bane of debugging. So
the logic of interactive programming seems inexorable.[^6]

```text
Statements debugged
per person-day
       |
    50 |    ■ Conversational
       |
    40 |
       |
    30 |
       |
    20 |
       |            □ Batch
    10 |
       |
     0 |___________________________________
        Control  Language  Language  Editor
        program  translator translator
```

Fig. 12.2: Comparative productivity under batch and conversational programming

Further, we hear good testimonies from many who have built
little systems or parts of systems in this way. The only numbers
I have seen for effects on programming of large systems were
reported by John Harr of Bell Labs. They are shown in Fig. 12.2.
These numbers are for writing, assembling, and debugging programs. The first program is mostly control program; the other three
are language translators, editors, and such. Harr's data suggest that
an interactive facility at least doubles productivity in system programming.[^7]

The effective use of most interactive tools requires that the
work be done in a high-level language, for teletype and typewriter
terminals cannot be used to debug by dumping memory. With a
high-level language, source can be easily edited and selective
printouts easily done. Together they make a pair of sharp tools
indeed.

---

[^1]: For an excellent discussion of tools and their integration into the programming task, see W. M. Talbott, "A software development system," *Computer*, Jan., 1974, pp. 39-43.

[^2]: See, for example, A. L. Scherr, "Managing computing in a large-scale production environment," *IBM Systems J.*, 12, 3 (1973), pp. 213-239, and W. M. Talbott, op. cit.

[^3]: See, for example, F. J. Corbató and J. H. Saltzer, "Some considerations of supervisor program design for multiplexed computer systems," in *Information Processing 1968 (Proc. IFIP Cong. 1968, Edinburgh)*, Amsterdam: North-Holland, 1969, pp. 1366-1371. Also see R. W. Conway, W. L. Maxwell, and H. L. Morgan, "On the implementation of security measures in information systems," *Comm. ACM*, 15, 4 (Apr., 1972), pp. 211-220.

[^4]: D. E. Knuth, "An empirical study of FORTRAN programs," *Software—Practice and Experience*, 1, 2 (1971), pp. 105-133.

[^5]: Of course this is a 1974 opinion. Today (1995) I would say C or C++.

[^6]: B. W. Kernighan and P. J. Plauger, *Software Tools*. Reading, Mass.: Addison-Wesley, 1976, gives a brilliant treatment of the techniques and philosophy of tool-building.

[^7]: J. Harr of Bell Labs, reported in W. M. Talbott, op. cit.
