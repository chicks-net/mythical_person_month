# Chapter 19: The Mythical Man-Month after 20 Years

> I know no way of judging the future but by the past.
> — PATRICK HENRY

---

> You can never plan the future by the past.
> — EDMUND BURKE

*Shooting the Rapids*
*The Bettman Archive*

---

## Why Is There a Twentieth Anniversary Edition?

The plane droned through the night toward LaGuardia. Clouds
and darkness veiled all interesting sights. The document I was
studying was pedestrian. I was not, however, bored. The stranger
sitting next to me was reading *The Mythical Man-Month*, and I
was waiting to see if by word or sign he would react. Finally as
we taxied toward the gate, I could wait no longer:

"How is that book? Do you recommend it?"

"Hmph! Nothing in it I didn't know already."

I decided not to introduce myself.

Why has *The Mythical Man-Month* persisted? Why is it still
seen to be relevant to software practice today? Why does it have
a readership outside the software engineering community, generating reviews, citations, and correspondence from lawyers,
doctors, psychologists, sociologists, as well as from software
people? How can a book written 20 years ago about a software-building experience 30 years ago still be relevant, much less useful?

One explanation sometimes heard is that the software development discipline has not advanced normally or properly.
This view is often supported by contrasting computer software
development productivity with computer hardware manufacturing productivity, which has multiplied at least a thousandfold over the two decades. As Chapter 16 explains, the anomaly
is not that software has been so slow in its progress but rather
that computer technology has exploded in a fashion unmatched
in human history. By and large this comes from the gradual
transition of computer manufacturing from an assembly industry to a process industry, from labor-intensive to capital-intensive manufacturing. Hardware and software development, in
contrast to manufacturing, remain inherently labor-intensive.

A second explanation often advanced is that *The Mythical
Man-Month* is only incidentally about software but primarily
about how people in teams make things. There is surely some
truth in this; the preface to the 1975 edition says that managing
a software project is more like other management than most
programmers initially believe. I still believe that to be true. Human history is a drama in which the stories stay the same, the
scripts of those stories change slowly with evolving cultures,
and the stage settings change all the time. So it is that we see
our twentieth-century selves mirrored in Shakespeare, Homer,
and the Bible. So to the extent *The MM-M* is about people and
teams, obsolescence should be slow.

Whatever the reason, readers continue to buy the book, and
they continue to send me much-appreciated comments. Nowadays I am often asked, "What do you now think was wrong
when written? What is now obsolete? What is really new in the
software engineering world?" These quite distinct questions are
all fair, and I shall address them as best I can. Not in that order,
however, but in clusters of topics. First, let us consider what was
right when written, and still is.

## The Central Argument: Conceptual Integrity and the Architect

**Conceptual integrity.** A clean, elegant programming product
must present to each of its users a coherent mental model of the
application, of strategies for doing the application, and of the
user-interface tactics to be used in specifying actions and parameters. The conceptual integrity of the product, as perceived by
the user, is the most important factor in ease of use. (There are
other factors, of course. The Macintosh's uniformity of user interface across all applications is an important example. Moreover, it is possible to construct coherent interfaces that are
nevertheless quite awkward. Consider MS-DOS.)

There are many examples of elegant software products designed by a single mind, or by a pair. Most purely intellectual
works such as books or musical compositions are so produced.
Product-development processes in many industries cannot,
however, afford this straightforward approach to conceptual integrity. Competitive pressures force urgency; in many modern
technologies the end product is quite complex, and the design
inherently requires many person-months of effort. Software products are both complex and fiercely competitive in schedule.

Any product that is sufficiently big or urgent to require the
effort of many minds thus encounters a peculiar difficulty: the
result must be conceptually coherent to the single mind of the
user and at the same time designed by many minds. How does
one organize design efforts so as to achieve such conceptual integrity? This is the central question addressed by *The MM-M*.
One of its theses is that managing large programming projects
is qualitatively different from managing small ones, just because
of the number of minds involved. Deliberate, and even heroic,
management actions are necessary to achieve coherence.

**The architect.** I argue in Chapters 4 through 7 that the most
important action is the commissioning of some one mind to be
the product's architect, who is responsible for the conceptual integrity of all aspects of the product perceivable by the user. The
architect forms and owns the public mental model of the product that will be used to explain its use to the user. This includes
the detailed specification of all of its function and the means for
invoking and controlling it. The architect is also the user's agent,
knowledgeably representing the user's interest in the inevitable
tradeoffs among function, performance, size, cost, and schedule. This role is a full-time job, and only on the smallest teams
can it be combined with that of the team manager. The architect
is like the director and the manager like the producer of a motion picture.

**Separation of architecture from implementation and realization.** To make the architect's crucial task even conceivable, it is
necessary to separate the architecture, the definition of the
product as perceivable by the user, from its implementation. Architecture versus implementation defines a clean boundary between parts of the design task, and there is plenty of work on
each side of it.

**Recursion of architects.** For quite large products, one mind
cannot do all of the architecture, even after all implementation
concerns have been split off. So it is necessary for the system
master architect to partition the system into subsystems. The
subsystem boundaries must be at those places where interfaces
between the subsystems are minimal and easiest to define rigorously. Then each piece will have its own architect, who must
report to the system master architect with respect to the architecture. Clearly this process can proceed recursively as required.

**Today I am more convinced than ever.** Conceptual integrity is
central to product quality. Having a system architect is the most
important single step toward conceptual integrity. These principles are by no means limited to software systems, but to the
design of any complex construct, whether a computer, an airplane, a Strategic Defense Initiative, a Global Positioning System. After teaching a software engineering laboratory more than
20 times, I came to insist that student teams as small as four people choose a manager and a separate architect. Defining distinct
roles in such small teams may be a little extreme, but I have observed it to work well and to contribute to design success even
for small teams.

## The Second-System Effect: Featuritis and Frequency-Guessing

**Designing for large user sets.** One of the consequences of the
personal computer revolution is that increasingly, at least in the
business data processing community, off-the-shelf packages
are replacing custom applications. Moreover, standard software
packages sell hundreds of thousands of copies, or even millions.
System architects for machine-vendor-supplied software have
always had to design for a large, amorphous user set rather than
for a single, definable application in one company. Many, many
system architects now face this task.

Paradoxically, it is much more difficult to design a general-purpose tool than it is to design a special-purpose tool, precisely
because one has to assign weights to the differing needs of the
diverse users.

**Featuritis.** The besetting temptation for the architect of a general purpose tool such as a spreadsheet or a word processor is
to overload the product with features of marginal utility, at the
expense of performance and even of ease of use. The appeal of
proposed features is evident at the outset; the performance penalty is evident only as system testing proceeds. The loss of ease
of use sneaks up insidiously, as features are added in little increments, and the manuals wax fatter and fatter.[^1]

For mass-market products that survive and evolve through
many generations, the temptation is especially strong. Millions
of customers request hundreds of features; any request is itself
evidence that "the market demands it." Frequently, the original
system architect has gone on to greater glories, and the architecture is in the hands of people with less experience at representing the user's overall interest in balance. A recent review of
Microsoft Word 6.0 says "Word 6.0 packs in features; update
slowed by baggage. ... Word 6.0 is also big and slow." It notes
with dismay that Word 6.0 requires 4 MB of RAM, and goes on
to say that the rich added function means that "even a Macintosh IIfx [is] just barely up to the Word 6 task".[^2]

**Defining the user set.** The larger and more amorphous the
user set, the more necessary it is to define it explicitly if one is
to achieve conceptual integrity. Each member of the design team
will surely have an implicit mental image of the users, and each
designer's image will be different. Since an architect's image of
the user consciously or subconsciously affects every architectural decision, it is essential for a design team to arrive at a single shared image. And that requires writing down the attributes
of the expected user set, including:

- Who they are
- What they need
- What they think they need
- What they want

**Frequencies.** For any software product, any of the attributes of
the user set is in fact a distribution, with many possible values,
each with its own frequency. How is the architect to arrive at
these frequencies? Surveying this ill-defined population is a dubious and costly proposition.[^3] Over the years I have become
convinced that an architect should guess, or, if you prefer, postulate, a complete set of attributes and values with their frequencies, in order to develop a complete, explicit, and shared
description of the user set.

Many benefits flow from this unlikely procedure. First, the
process of carefully guessing the frequencies will cause the architect to think very carefully about the expected user set. Second, writing the frequencies down will subject them to debate,
which will illuminate all the participants and bring to the surface the differences in the user images that the several designers
carry. Third, enumerating the frequencies explicitly helps everyone recognize which decisions depend upon which user set
properties. Even this sort of informal sensitivity analysis is valuable. When it develops that very important decisions are hinging on some particular guess, then it is worth the cost to
establish better estimates for that value. (The gIBIS system developed by Jeff Conklin provides a tool for formally and accurately tracking design decisions and documenting the reasons
for each.[^4] I have not had opportunity to use it, but I think it
would be very helpful.)

To summarize: write down explicit guesses for the attributes
of the user set. *It is far better to be explicit and wrong than to be
vague.*

**What about the "Second-System Effect"?** A perceptive student remarked that *The Mythical Man-Month* recommended a
recipe for disaster: Plan to deliver the second version of any new
system (Chapter 11), which Chapter 5 characterizes as the most
dangerous system one ever designs. I had to grant him a
"gotcha."

The contradiction is more linguistic than real. The "second"
system described in Chapter 5 is the second system fielded, the
follow-on system that invites added function and frills. The
"second" system in Chapter 11 is the second try at building
what should be the first system to be fielded. It is built under all
the schedule, talent, and ignorance constraints that characterize
new projects—the constraints that exert a slimness discipline.

## The Triumph of the WIMP Interface

One of the most impressive developments in software during
the past two decades has been the triumph of the Windows,
Icons, Menus, Pointing interface—or WIMP for short. It is today
so familiar as to need no description. This concept was first
publicly displayed by Doug Englebart and his team from the
Stanford Research Institute at the Western Joint Computer
Conference of 1968.[^5] From there the ideas went to Xerox Palo
Alto Research Center, where they emerged in the Alto personal
workstation developed by Bob Taylor and team. They were
picked up by Steve Jobs for the Apple Lisa, a computer too slow
to carry its exciting ease-of-use concepts. These concepts Jobs
then embodied in the commercially successful Apple Macintosh
in 1985. They were later adopted in Microsoft Windows for the
IBM PC and compatibles. The Mac version will be my example.[^6]

**Conceptual integrity via a metaphor.** The WIMP is a superb
example of a user interface that has conceptual integrity,
achieved by the adoption of a familiar mental model, the desktop metaphor, and its careful consistent extension to exploit a
computer graphics implementation. For example, the costly but
proper decision to overlay windows instead of tiling them follows directly from the metaphor. The ability to size and shape
windows is a consistent extension that gives the user the new
powers enabled by the computer graphics medium. Papers on a
desktop cannot be so readily sized and shaped. Dragging and
dropping follow directly from the metaphor; selecting icons by
pointing with a cursor is a direct analog of picking things with
the hand. Icons and nested folders are faithful analogs of desktop documents; so is the trash can. The concepts of cutting,
copying, and pasting faithfully mirror the things we used to do
with documents on desktops. So faithfully is the metaphor followed and so consistent is its extension that new users are positively jarred by the notion of dragging a diskette's icon to the
trash to eject the disk. Were the interface not almost uniformly
consistent, that (pretty bad) inconsistency would not grate so
much.

Where is the WIMP interface forced to go far beyond the
desktop metaphor? Most notably in two respects: menus and
one-handedness. When working with a real desktop, one does
actions to documents, rather than telling someone or something
to do them. And when one does tell someone to do an action,
one usually generates, rather than selects, the oral or written
imperative verb commands: "Please file this." "Please find the
earlier correspondence." "Please send this to Mary to handle."

Alas, the reliable interpretation of free-form generated English commands is beyond the present state of the art, whether
commands are written or spoken. So the interface designers
were two steps removed from direct user action on documents.
They wisely picked up from the usual desktop its one example
of command selection—the printed buck slip, on which the user
selects from among a constrained menu of commands whose semantics are standardized. This idea they extended to a horizontal menu of vertical pull-down submenus.

**Command utterances and the two-cursor problem.** Commands are imperative sentences; they always have a verb and
usually have a direct object. For any action, one needs to specify
a verb and a noun. The pointing metaphor says, to specify two
things at a time, have two distinguished cursors on the screen,
each driven by a separate mouse—one in the right hand and one
in the left. After all, on a physical desktop we normally work
with both hands. (But, one hand is often holding things fixed in
place, which happens by default on the computer desktop.) The
mind is certainly capable of two-handed operation; we regularly
use two hands in typing, driving, cooking. Alas, providing one
mouse was already a big step forward for personal computer
makers; no commercial system accommodates two simultaneous mouse-cursor actions, one driven with each hand.[^7]

The interface designers accepted reality and designed for
one mouse, adopting the syntactic convention that one points
out (selects) the noun first. One points at the verb, a menu item.
This really gives away a lot of ease-of-use. As I watch users, or
videotapes of users, or computer tracings of cursor movements,
I am immediately struck that one cursor is having to do the work
of two: pick an object in the desktop part of the window; pick a
verb in the menu portion; find or re-find an object in the desktop; again pull down a menu (often the same one) and pick a
verb. Back and forth, back and forth the cursor goes, from data-space to menu-space, each time discarding the useful information as to where it was last time it was in this space—altogether,
an inefficient process.

**A brilliant solution.** Even if the electronics and software could
readily handle two simultaneously active cursors, there are
space-layout difficulties. The desktop in the WIMP metaphor
really includes a typewriter, and one must accommodate its real
keyboard in physical space on the real desktop. A keyboard plus
two mouse-pads uses a lot of the arm's-reach real estate. Well,
the problem of the keyboard can be turned into an opportunity—why not enable efficient two-handed operation by using
one hand on the keyboard to specify verbs and the other hand
on a mouse to pick nouns. Now the cursor stays in the data
space, exploiting the high locality of successive noun picks. Real
efficiency, real user power.

**User power versus ease of use.** That solution, however, gives
away the thing that makes menus so easy to use for novices—
menus present the alternative verbs valid at any particular state.
We can buy a package, bring it home, and start using it without
consulting the manual, merely by knowing what we bought it
for, and experimenting with the different menu verbs.

One of the hardest issues facing software architects is exactly how to balance user power versus ease of use. Do they design for simple operation for the novice or the occasional user,
or for efficient power for the professional user? The ideal answer
is to provide both, in a conceptually coherent way—that is
achieved in the WIMP interface. The high-frequency menu
verbs each have single-key + command-key equivalents, mostly
chosen so that they can easily be struck as a single chord with
the left hand. On the Mac, for example, the command key (⌘)
is just below the Z and X keys; therefore the highest-frequency
operations are encoded as ⌘Z (Undo), ⌘X (Cut), ⌘C (Copy),
⌘V (Paste).

**Incremental transition from novice to power user.** This dual
system for specifying command verbs not only meets the low-learning-effort needs of the novice and the efficiency needs of
the power user, it provides for each user to make a smooth transition between modes. The letter encodings, called *short cuts*, are
shown on the menus beside the verbs, so that a user in doubt
can pull down the menu to check the letter equivalent, instead
of just picking the menu item. Each novice learns first the short
cuts for their own high-frequency operations. Any short cut they are
doubtful about they can try, since ⌘Z will undo any single mistake. Alternatively, they can check the menu to see what commands are valid. Novices will pull lots of menus; power users
very few; and in-between users will only occasionally need to
pick from a menu, since each will know the few short-cuts that
make up most of their own operations. Most of us software designers are too familiar with this interface to appreciate fully its
elegance and power.

**The success of direct incorporation as a device for enforcing architecture.** The Mac interface is remarkable in yet another way.
Without coercion, its designers have made it a standard interface across applications, including the vast majority that are
written by third parties. So the user gains conceptual coherence
at the interface level not only within the software furnished with
the machine but across all applications.

This feat the Mac designers accomplished by building the
interface into the read-only memory, so that it is easier and
faster for developers to use it than to build their own idiosyncratic interfaces. These natural incentives for uniformity prevailed widely enough to establish a de facto standard. The
natural incentives were helped by a total management commitment and a lot of persuasion by Apple. The independent reviewers in the product magazines, recognizing the immense
value of cross-application conceptual integrity, have also supplemented the natural incentives by mercilessly criticizing products that do not conform.

This is a superb example of the technique, recommended in
Chapter 6, of achieving uniformity by encouraging others to directly incorporate one's code into their products, rather than attempting to have them build their own software to one's
specifications.

**The fate of WIMP: Obsolescence.** Despite its excellencies, I expect the WIMP interface to be a historical relic in a generation.
Pointing will still be the way to express nouns as we command
our machines; speech is surely the right way to express the
verbs. Tools such as Voice Navigator for the Mac and Dragon for
the PC already provide this capability.

## Don't Build One to Throw Away—The Waterfall Model Is Wrong

The unforgettable picture of Galloping Gertie, the Tacoma Narrows Bridge, opens Chapter 11, which radically recommends:
"Plan to throw one away; you will, anyhow." This I now perceive to be wrong, not because it is too radical, but because it is
too simplistic.

The biggest mistake in the "Build one to throw away" concept is that it implicitly assumes the classical sequential or waterfall model of software construction. The model derives from
a Gantt chart layout of a staged process, and it is often drawn
as in Figure 19.1. Winton Royce improved the sequential model
in a classic 1970 paper by providing for[^8]

- Some feedback from a stage to its predecessors
- Limiting the feedback to the immediately preceding stage
  only, so as to contain the cost and schedule delay it occasions.

He preceded *The MM-M* in advising builders to "build it twice."
Chapter 11 is not the only one tainted by the sequential waterfall
model; it runs through the book, beginning with the scheduling
rule in Chapter 2. That rule-of-thumb allocates 1/3 of the schedule to planning, 1/6 to coding, 1/4 to component test, and 1/4 to
system test.

```text
Requirements → Design → Code → Test → Deploy
```

Fig. 19.1: Waterfall model of software construction

The basic fallacy of the waterfall model is that it assumes a
project goes through the process once, that the architecture is excellent and easy to use, the implementation design is sound,
and the realization is fixable as testing proceeds. Another way
of saying it is that the waterfall model assumes the mistakes will
all be in the realization, and thus that their repair can be
smoothly interspersed with component and system testing.

"Plan to throw one away" does indeed attack this fallacy
head on. It is not the diagnosis that is wrong; it is the remedy.

**Note:** Due to length constraints, I'm including key sections. The full chapter continues with sections on Incremental Building, Microsoft's Experience, Information Hiding and the Use of Standard Interfaces, Parnas Was Right, Brooks's Law Repealed, The Documentary Hypothesis, Excitement About Incremental Development, Peopleware, The Power of Giving Up Power, What's the Biggest New Surprise, Shrink-Wrapped Software, Buy and Build, and The State and Future of Software Engineering.

---

[^1]: For a witty and insightful discussion of the featuritis problem, see M. A. Cusumano and R. W. Selby, "How Microsoft builds software," *Comm. ACM*, 40, 6 (June, 1997), pp. 53-61.

[^2]: "Word 6.0 packs in features; update slowed by baggage," *MacWEEK*, 8, 4 (Jan. 24, 1994), p. 1.

[^3]: For a thoughtful discussion of this problem, see P. Denning, "The science of computing: Blindness in designing for people," *American Scientist*, Nov.-Dec. 1990, pp. 498-501.

[^4]: J. Conklin, "Hypertext: An introduction and survey," *Computer*, Sept. 1987, pp. 17-41; J. Conklin and M. L. Begeman, "gIBIS: A hypertext tool for exploratory policy discussion," *ACM Trans. Office Information Systems*, 6, 4 (Oct. 1988), pp. 303-331.

[^5]: D. C. Engelbart and W. K. English, "A research center for augmenting human intellect," *Proc. AFIPS Fall Joint Computer Conference*, 33 (1968), pp. 395-410.

[^6]: For a fuller account of the history and evolution of the WIMP interface, see S. Levy, *Insanely Great: The Life and Times of Macintosh, the Computer That Changed Everything*. New York: Viking, 1994.

[^7]: One interesting exception: Steve Perlman and others at Apple have demonstrated a setup in which two users can simultaneously use separate mice on a single screen, cooperating on a single task.

[^8]: W. W. Royce, "Managing the development of large software systems," *Proc. IEEE WESCON*, Aug. 1970, pp. 1-9. Reprinted in *Proc. 9th Int. Conf. on Software Engineering*. Los Alamitos, Calif.: IEEE Computer Society Press, 1987, pp. 328-338.
