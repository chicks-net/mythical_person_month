# 19 - The Mythical Man-Month after 20 Years

> I know no way of judging the future but by the past.
>
> — PATRICK HENRY

<!-- -->

> You can never plan the future by the past.
>
> — EDMUND BURKE

## Why Is There a Twentieth Anniversary Edition?

The plane droned through the night toward LaGuardia. Clouds and darkness veiled all interesting sights. The document I was studying was pedestrian. I was not, however, bored. The stranger sitting next to me was reading The Mythical Man-Month, and I was waiting to see if by word or sign he would react. Finally as we taxied toward the gate, I could wait no longer:

"How is that book? Do you recommend it?"

"Hmph! Nothing in it I didn't know already."

I decided not to introduce myself.

Why has The Mythical Man-Month persisted? Why is it still seen to be relevant to software practice today? Why does it have a readership outside the software engineering community, generating reviews, citations, and correspondence from lawyers, doctors, psychologists, sociologists, as well as from software people? How can a book written 20 years ago about a software-building experience 30 years ago still be relevant, much less useful?

One explanation sometimes heard is that the software development discipline has not advanced normally or properly. This view is often supported by contrasting computer software development productivity with computer hardware manufacturing productivity, which has multiplied at least a thousandfold over the two decades. As Chapter 16 explains, the anomaly is not that software has been so slow in its progress but rather that computer technology has exploded in a fashion unmatched in human history. By and large this comes from the gradual transition of computer manufacturing from an assembly industry to a process industry, from labor-intensive to capital-intensive manufacturing. Hardware and software development, in contrast to manufacturing, remain inherently labor-intensive.

A second explanation often advanced is that The Mythical Man-Month is only incidentally about software but primarily about how people in teams make things. There is surely some truth in this; the preface to the 1975 edition says that managing a software project is more like other management than most programmers initially believe. I still believe that to be true. Human history is a drama in which the stories stay the same, the scripts of those stories change slowly with evolving cultures, and the stage settings change all the time. So it is that we see our twentieth-century selves mirrored in Shakespeare, Homer, and the Bible. So to the extent The MM-M is about people and teams, obsolescence should be slow.

Whatever the reason, readers continue to buy the book, and they continue to send me much-appreciated comments. Nowadays I am often asked, "What do you now think was wrong when written? What is now obsolete? What is really new in the software engineering world?" These quite distinct questions are all fair, and I shall address them as best I can. Not in that order, however, but in clusters of topics. First, let us consider what was right when written, and still is.

## The Central Argument: Conceptual Integrity and the Architect

**Conceptual integrity.** A clean, elegant programming product must present to each of its users a coherent mental model of the application, of strategies for doing the application, and of the user-interface tactics to be used in specifying actions and parameters. The conceptual integrity of the product, as perceived by the user, is the most important factor in ease of use. (There are other factors, of course. The Macintosh's uniformity of user interface across all applications is an important example. Moreover, it is possible to construct coherent interfaces that are nevertheless quite awkward. Consider MS-DOS.)

There are many examples of elegant software products designed by a single mind, or by a pair. Most purely intellectual works such as books or musical compositions are so produced. Product-development processes in many industries cannot, however, afford this straightforward approach to conceptual integrity. Competitive pressures force urgency; in many modern technologies the end product is quite complex, and the design inherently requires many man-months of effort. Software products are both complex and fiercely competitive in schedule.

Any product that is sufficiently big or urgent to require the effort of many minds thus encounters a peculiar difficulty: the result must be conceptually coherent to the single mind of the user and at the same time designed by many minds. How does one organize design efforts so as to achieve such conceptual integrity? This is the central question addressed by The MM-M. One of its theses is that managing large programming projects is qualitatively different from managing small ones, just because of the number of minds involved. Deliberate, and even heroic, management actions are necessary to achieve coherence.

**The architect.** I argue in Chapters 4 through 7 that the most important action is the commissioning of some one mind to be the product's architect, who is responsible for the conceptual integrity of all aspects of the product perceivable by the user. The architect forms and owns the public mental model of the product that will be used to explain its use to the user. This includes the detailed specification of all of its function and the means for invoking and controlling it. The architect is also the user's agent, knowledgeably representing the user's interest in the inevitable tradeoffs among function, performance, size, cost, and schedule. This role is a full-time job, and only on the smallest teams can it be combined with that of the team manager. The architect is like the director and the manager like the producer of a motion picture.

**Separation of architecture from implementation and realization.** To make the architect's crucial task even conceivable, it is necessary to separate the architecture, the definition of the product as perceivable by the user, from its implementation. Architecture versus implementation defines a clean boundary between parts of the design task, and there is plenty of work on each side of it.

**Recursion of architects.** For quite large products, one mind cannot do all of the architecture, even after all implementation concerns have been split off. So it is necessary for the system master architect to partition the system into subsystems. The subsystem boundaries must be at those places where interfaces between the subsystems are minimal and easiest to define rigorously. Then each piece will have its own architect, who must report to the system master architect with respect to the architecture. Clearly this process can proceed recursively as required.

**Today I am more convinced than ever.** Conceptual integrity is central to product quality. Having a system architect is the most important single step toward conceptual integrity. These principles are by no means limited to software systems, but to the design of any complex construct, whether a computer, an airplane, a Strategic Defense Initiative, a Global Positioning System. After teaching a software engineering laboratory more than 20 times, I came to insist that student teams as small as four people choose a manager and a separate architect. Defining distinct roles in such small teams may be a little extreme, but I have observed it to work well and to contribute to design success even for small teams.

## The Second-System Effect: Featuritis and Frequency-Guessing

**Designing for large user sets.** One of the consequences of the personal computer revolution is that increasingly, at least in the business data processing community, off-the-shelf packages are replacing custom applications. Moreover, standard software packages sell hundreds of thousands of copies, or even millions. System architects for machine-vendor-supplied software have always had to design for a large, amorphous user set rather than for a single, definable application in one company. Many, many system architects now face this task.

Paradoxically, it is much more difficult to design a general-purpose tool than it is to design a special-purpose tool, precisely because one has to assign weights to the differing needs of the diverse users.

**Featuritis.** The besetting temptation for the architect of a general purpose tool such as a spreadsheet or a word processor is to overload the product with features of marginal utility, at the expense of performance and even of ease of use. The appeal of proposed features is evident at the outset; the performance penalty is evident only as system testing proceeds. The loss of ease of use sneaks up insidiously, as features are added in little increments, and the manuals wax fatter and fatter.[^1]

For mass-market products that survive and evolve through many generations, the temptation is especially strong. Millions of customers request hundreds of features; any request is itself evidence that "the market demands it." Frequently, the original system architect has gone on to greater glories, and the architecture is in the hands of people with less experience at representing the user's overall interest in balance. A recent review of Microsoft Word 6.0 says "Word 6.0 packs in features; update slowed by baggage. . . . Word 6.0 is also big and slow." It notes with dismay that Word 6.0 requires 4 MB of RAM, and goes on to say that the rich added function means that "even a Macintosh Ilfx [is] just barely up to the Word 6 task".[^2]

**Defining the user set.** The larger and more amorphous the user set, the more necessary it is to define it explicitly if one is to achieve conceptual integrity. Each member of the design team will surely have an implicit mental image of the users, and each designer's image will be different. Since an architect's image of the user consciously or subconsciously affects every architectural decision, it is essential for a design team to arrive at a single shared image. And that requires writing down the attributes of the expected user set, including:

- Who they are
- What they need
- What they think they need
- What they want

**Frequencies.** For any software product, any of the attributes of the user set is in fact a distribution, with many possible values, each with its own frequency. How is the architect to arrive at these frequencies? Surveying this ill-defined population is a dubious and costly proposition.[^3] Over the years I have become convinced that an architect should guess, or, if you prefer, postulate, a complete set of attributes and values with their frequencies, in order to develop a complete, explicit, and shared description of the user set.

Many benefits flow from this unlikely procedure. First, the process of carefully guessing the frequencies will cause the architect to think very carefully about the expected user set. Second, writing the frequencies down will subject them to debate, which will illuminate all the participants and bring to the surface the differences in the user images that the several designers carry. Third, enumerating the frequencies explicitly helps everyone recognize which decisions depend upon which user set properties. Even this sort of informal sensitivity analysis is valuable. When it develops that very important decisions are hinging on some particular guess, then it is worth the cost to establish better estimates for that value. (The gIBIS system developed by Jeff Conklin provides a tool for formally and accurately tracking design decisions and documenting the reasons for each.[^4] I have not had opportunity to use it, but I think it would be very helpful.)

To summarize: write down explicit guesses for the attributes of the user set. It is far better to be explicit and wrong man to be vague.

**What about the "Second-System Effect"?** A perceptive student remarked that The Mythical Man-Month recommended a recipe for disaster: Plan to deliver the second version of any new system (Chapter 11), which Chapter 5 characterizes as the most dangerous system one ever designs. I had to grant him a "gotcha."

The contradiction is more linguistic than real. The "second" system described in Chapter 5 is the second system fielded, the follow-on system that invites added function and frills. The "second" system in Chapter 11 is the second try at building what should be the first system to be fielded. It is built under all the schedule, talent, and ignorance constraints that characterize new projects—the constraints that exert a slimness discipline.

## The Triumph of the WIMP Interface

One of the most impressive developments in software during the past two decades has been the triumph of the Windows, Icons, Menus, Pointing interface—or WIMP for short. It is today so familiar as to need no description. This concept was first publicly displayed by Doug Englebart and his team from the Stanford Research Institute at the Western Joint Computer Conference of 1968.[^5] From there the ideas went to Xerox Palo Alto Research Center, where they emerged in the Alto personal workstation developed by Bob Taylor and team. They were picked up by Steve Jobs for the Apple Lisa, a computer too slow to carry its exciting ease-of-use concepts. These concepts Jobs then embodied in the commercially successful Apple Macintosh in 1985. They were later adopted in Microsoft Windows for the IBM PC and compatibles. The Mac version will be my example.[^6]

**Conceptual integrity via a metaphor.** The WIMP is a superb example of a user interface that has conceptual integrity, achieved by the adoption of a familiar mental model, the desktop metaphor, and its careful consistent extension to exploit a computer graphics implementation. For example, the costly but proper decision to overlay windows instead of tiling them follows directly from the metaphor. The ability to size and shape windows is a consistent extension that gives the user the new powers enabled by the computer graphics medium. Papers on a desktop cannot be so readily sized and shaped. Dragging and dropping follow directly from the metaphor; selecting icons by pointing with a cursor is a direct analog of picking things with the hand. Icons and nested folders are faithful analogs of desktop documents; so is the trash can. The concepts of cutting, copying, and pasting faithfully mirror the things we used to do with documents on desktops. So faithfully is the metaphor followed and so consistent is its extension that new users are positively jarred by the notion of dragging a diskette's icon to the trash to eject the disk. Were the interface not almost uniformly consistent, that (pretty bad) inconsistency would not grate so much.

Where is the WIMP interface forced to go far beyond the desktop metaphor? Most notably in two respects: menus and one-handedness. When working with a real desktop, one does actions to documents, rather than telling someone or something to do them. And when one does tell someone to do an action, one usually generates, rather than selects, the oral or written imperative verb commands: "Please file this." "Please find the earlier correspondence." "Please send this to Mary to handle."

Alas, the reliable interpretation of free-form generated English commands is beyond the present state of the art, whether commands are written or spoken. So the interface designers were two steps removed from direct user action on documents. They wisely picked up from the usual desktop its one example of command selection—the printed buck slip, on which the user selects from among a constrained menu of commands whose semantics are standardized. This idea they extended to a horizontal menu of vertical pull-down submenus.

**Command utterances and the two-cursor problem.** Commands are imperative sentences; they always have a verb and usually have a direct object. For any action, one needs to specify a verb and a noun. The pointing metaphor says, to specify two things at a time, have two distinguished cursors on the screen, each driven by a separate mouse—one in the right hand and one in the left. After all, on a physical desktop we normally work with both hands. (But, one hand is often holding things fixed in place, which happens by default on the computer desktop.) The mind is certainly capable of two-handed operation; we regularly use two hands in typing, driving, cooking. Alas, providing one mouse was already a big step forward for personal computer makers; no commercial system accommodates two simultaneous mouse-cursor actions, one driven with each hand.[^7]

The interface designers accepted reality and designed for one mouse, adopting the syntactic convention that one points out (selects) the noun first. One points at the verb, a menu item. This really gives away a lot of ease-of-use. As I watch users, or videotapes of users, or computer tracings of cursor movements, I am immediately struck that one cursor is having to do the work of two: pick an object in the desktop part of the window; pick a verb in the menu portion; find or re-find an object in the desktop; again pull down a menu (often the same one) and pick a verb. Back and forth, back and forth the cursor goes, from dataspace to menu-space, each time discarding the useful information as to where it was last time it was in this space—altogether, an inefficient process.

**A brilliant solution.** Even if the electronics and software could readily handle two simultaneously active cursors, there are space-layout difficulties. The desktop in the WIMP metaphor really includes a typewriter, and one must accommodate its real keyboard in physical space on the real desktop. A keyboard plus two mouse-pads uses a lot of the arm's-reach real estate. Well, the problem of the keyboard can be turned into an opportunity—why not enable efficient two-handed operation by using one hand on the keyboard to specify verbs and the other hand on a mouse to pick nouns. Now the cursor stays in the data space, exploiting the high locality of successive noun picks. Real efficiency, real user power.

**User power versus ease of use.** That solution, however, gives away the thing that makes menus so easy to use for novices—menus present the alternative verbs valid at any particular state. We can buy a package, bring it home, and start using it without consulting the manual, merely by knowing what we bought it for, and experimenting with the different menu verbs.

One of the hardest issues facing software architects is exactly how to balance user power versus ease of use. Do they design for simple operation for the novice or the occasional user, or for efficient power for the professional user? The ideal answer is to provide both, in a conceptually coherent way—that is achieved in the WIMP interface. The high-frequency menu verbs each have single-key + command-key equivalents, mostly chosen so that they can easily be struck as a single chord with the left hand. On the Mac, for example, the command key (⌘) is just below the Z and X keys; therefore the highest-frequency operations are encoded as ⌘Z (Undo), ⌘X (Cut), ⌘C (Copy), ⌘V (Paste).

**Incremental transition from novice to power user.** This dual system for specifying command verbs not only meets the low-learning-effort needs of the novice and the efficiency needs of the power user, it provides for each user to make a smooth transition between modes. The letter encodings, called short cuts, are shown on the menus beside the verbs, so that a user in doubt can pull down the menu to check the letter equivalent, instead of just picking the menu item. Each novice learns first the short cuts for his own high-frequency operations. Any short cut he is doubtful about he can try, since ⌘Z will undo any single mistake. Alternatively, he can check the menu to see what commands are valid. Novices will pull lots of menus; power users very few; and in-between users will only occasionally need to pick from a menu, since each will know the few short-cuts that make up most of his own operations. Most of us software designers are too familiar with this interface to appreciate fully its elegance and power.

**The success of direct incorporation as a device for enforcing architecture.** The Mac interface is remarkable in yet another way. Without coercion, its designers have made it a standard interface across applications, including the vast majority that are written by third parties. So the user gains conceptual coherence at the interface level not only within the software furnished with the machine but across all applications.

This feat the Mac designers accomplished by building the interface into the read-only memory, so that it is easier and faster for developers to use it than to build their own idiosyncratic interfaces. These natural incentives for uniformity prevailed widely enough to establish a de facto standard. The natural incentives were helped by a total management commitment and a lot of persuasion by Apple. The independent reviewers in the product magazines, recognizing the immense value of cross-application conceptual integrity, have also supplemented the natural incentives by mercilessly criticizing products that do not conform.

This is a superb example of the technique, recommended in Chapter 6, of achieving uniformity by encouraging others to directly incorporate one's code into their products, rather than attempting to have them build their own software to one's specifications.

**The fate of WIMP: Obsolescence.** Despite its excellencies, I expect the WIMP interface to be a historical relic in a generation. Pointing will still be the way to express nouns as we command our machines; speech is surely the right way to express the verbs. Tools such as Voice Navigator for the Mac and Dragon for the PC already provide this capability.

## Don't Build One to Throw Away—The Waterfall Model Is Wrong

The unforgettable picture of Galloping Gertie, the Tacoma Narrows Bridge, opens Chapter 11, which radically recommends: "Plan to throw one away; you will, anyhow." This I now perceive to be wrong, not because it is too radical, but because it is too simplistic.

The biggest mistake in the "Build one to throw away" concept is that it implicitly assumes the classical sequential or waterfall model of software construction. The model derives from a Gantt chart layout of a staged process, and it is often drawn as in Figure 19.1. Winston Royce improved the sequential model in a classic 1970 paper by providing for:

- Some feedback from a stage to its predecessors
- Limiting the feedback to the immediately preceding stage only, so as to contain the cost and schedule delay it occasions.

He preceded The MM-M in advising builders to "build it twice."[^8] Chapter 11 is not the only one tainted by the sequential waterfall model; it runs through the book, beginning with the scheduling rule in Chapter 2. That rule-of-thumb allocates 1/3 of the schedule to planning, 1/6 to coding, 1/4 to component test, and 1/4 to system test.

The basic fallacy of the waterfall model is that it assumes a project goes through the process once, that the architecture is excellent and easy to use, the implementation design is sound, and the realization is fixable as testing proceeds. Another way of saying it is that the waterfall model assumes the mistakes will all be in the realization, and thus that their repair can be smoothly interspersed with component and system testing.

"Plan to throw one away" does indeed attack this fallacy head on. It is not the diagnosis that is wrong; it is the remedy. Now I did suggest that one might discard and redesign the first system piece by piece, rather than in one lump. This is fine so far as it goes, but it fails to get at the root of the problem. The waterfall model puts system test, and therefore by implication user testing, at the end of the construction process. Thus one can find impossible awkwardnesses for users, or unacceptable performance, or dangerous susceptibility to user error or malice, only after investing in full construction. To be sure, the Alpha test scrutiny of the specifications aims to find such flaws early, but there is no substitute for hands-on users.

The second fallacy of the waterfall model is that it assumes one builds a whole system at once, combining the pieces for an end-to-end system test after all of the implementation design, most of the coding, and much of the component testing has been done.

The waterfall model, which was the way most people thought about software projects in 1975, unfortunately got enshrined into DOD-STD-2167, the Department of Defense specification for all military software. This ensured its survival well past the time when most thoughtful practitioners had recognized its inadequacy and abandoned it. Fortunately, the DoD has since begun to see the light.[^9]

**There has to be upstream movement.** Like the energetic salmon in the chapter-opening picture, experience and ideas from each downstream part of the construction process must leap upstream, sometimes more than one stage, and affect the upstream activity.

Designing the implementation will show that some architectural features cripple performance; so the architecture has to be reworked. Coding the realization will show some functions to balloon space requirements; so there may have to be changes to architecture and implementation.

One may well, therefore, iterate through two or more architecture-implementation design cycles before realizing anything as code.

## An Incremental-Build Model Is Better—Progressive Refinement

### Building an end-to-end skeleton system

Harlan Mills, working in a real-time system environment, early advocated that we should build the basic polling loop of a real-time system, with subroutine calls (stubs) for all the functions (Fig. 19.2), but only null subroutines. Compile it; test it. It goes round and round, doing literally nothing, but doing it correctly.[^10]

Next, we flesh out a (perhaps primitive) input module and an output module. Voilà! A running system that does something, however dull. Now, function by function, we incrementally build and add modules. At every stage we have a running system. If we are diligent, we have at every stage a debugged, tested system. (As the system grows, so does the burden of regression-testing each new module against all the previous test cases.)

After every function works at a primitive level, we refine or rewrite first one module and then another, incrementally growing the system. Sometimes, to be sure, we have to change the original driving loop, and or even its module interfaces.

Since we have a working system at all times:

- we can begin user testing very early, and
- we can adopt a build-to-budget strategy that protects absolutely against schedule or budget overruns (at the cost of possible functional shortfall).

For some 22 years, I taught the software engineering laboratory at the University of North Carolina, sometimes jointly with David Parnas. In this course, teams of usually four students built in one semester some real software application system. About halfway through those years, I switched to teaching incremental development. I was stunned by the electrifying effect on team morale of that first picture on the screen, that first running system.

### Parnas Families

David Parnas has been a major thought leader in software engineering during this whole 20-year period. Everyone is familiar with his information-hiding concept. Rather less familiar, but very important, is Parnas's concept of designing a software product as a family of related products.[^11] He urges the designer to anticipate both lateral extensions and succeeding versions of a product, and to define their function or platform differences so as to construct a family tree of related products (Fig 19.3).

The trick in the design of such a tree is to put near its root those design decisions that are less likely to change.

Such a design strategy maximizes the re-use of modules. More important, the same strategy can be broadened to include not only deliverable products but also the successive intermediate versions created in an incremental-build strategy. The product then grows through its intermediate stages with minimum backtracking.

### Microsoft's Daily Build Procedure

The Microsoft development process for large products follows this incremental-build model. Every day the pieces are compiled and linked together into an executable system. The linkage may fail; if not, the system may crash. That's ok. For years now Microsoft has had a zero-defect policy for the daily build. If it compiles and links and runs, one is not allowed, as a matter of team discipline, to make any change that causes the executable to fail. One goes to the chief programmer and confesses one's error. The chief programmer decides whether to roll back the product to yesterday's version, or to press forward, depending upon the nature of the defect and its fix.[^12]

The daily-build incremental-build technique is in diametric contrast to the waterfall-model weekly-build practice that had previously prevailed across the industry. A system built with the incremental-build model may not have any particular functionality present yet, and it may have a lot of scaffolding code that will later come out. But what is there should work properly. This is a profoundly different view of the software construction process.

For its Windows NT project, Jim McCarthy says Microsoft made several critical changes when it switched from the prevailing industry practice to the incremental-build model:[^13]

1. Daily build
2. Continuous code integration
3. Smoke test
4. All programmers assigned to features, none to components

Daily build and smoke test. The daily build discipline has many effects. Developers come to depend upon a reliable system base. When the base fails on some particular day, activity immediately focuses on fixing it. All the members of a team are sharply aware of any failure, and so peer pressure is strong to avoid breaking the build. Morale soars because there is a running system, something tangible to be proud of, to be scrutinized by users, to be shown to visitors. It may seem crazy to have a zero-tolerance defect rule. One can see developers not making desirable system improvements because of the fear of breaking the build. This obviously slows forward progress. But somehow the net effect is that progress is faster, not slower.

How can this be? As I understand it, it is a direct analog of a famous bridge-construction procedure from nineteenth-century civil engineering. When building long truss bridges, no truss was modified by adding any member unless that addition actually improved the strength of the whole, sometimes by enabling further additions. And new trusses were not started until previous trusses were completed and strong. Most people would have designed the whole bridge, built each truss, and then assembled the trusses. That takes too long. Moreover, miscalculations or member flaws may not show up until the whole is assembled. Defects are harder to find and to fix; schedules are less predictable. So it is with software.

**Continuous code integration.** For 30 years the industry practice had been not to write to a shared code base. One practiced branching and isolating, with only rare code integration. This had several bad effects:

- Bugs were introduced during integration
- It was unclear when a feature was really complete
- Progress was obscured
- Shared ownership of code was inhibited

Microsoft decided to require every developer to write to the shared code base. There is a master version of every piece. Changes are tried out locally first, but then put in the same day as master modules. This speeds debugging—one doesn't have to wonder whether a bug appeared in the branch. It clarifies feature-completion—a feature is only complete when the code is in the master base. Progress visibility improves—everyone can see what is really working. Developers browse each other's work, find opportunities for code sharing, and develop a team style.

**The development team is organized by product features, not by implementation components.** Microsoft abandoned the traditional division of labor in which there are user-interface designers, database designers, graphics designers, query designers, etc. Instead, one designer gets assigned a feature, usually as a specification. He then writes the code to implement it, across all of the components. This sounds like the direct opposite of David Parnas's information-hiding principle.

Actually, I think what is going on is much more subtle. The feature-oriented organization is needed for conceptual integrity of the features. Each user-visible feature needs to have been conceived in a single mind, tested by a single agent. Incoherence shows up immediately. Consider the alternative, a component-oriented organization. To get a user feature, one must traverse the whole decision tree and accumulate all the separately-made component choices. Conceptual integrity is terribly difficult to achieve, and there is no one mind responsible for each feature, no one test of each feature. This is a formula for bad ease-of-use.

On the other hand, is not one defeating the whole modular structure by breaking up the responsibility for components? How can common data and common presentation get assured? I think the answer is in the product design prior to feature implementation. That is, the user-interface designer, the screen designer, the database designer must still do their architecture, each designing for consistency across the whole product. The master interface architect defines the metaphor. The screen designer defines the detailed look and feel. The database designer defines the information structures. Each gives his component of the specification to the feature implementer, who then builds his feature. Provided the architectural boundaries have been cleanly drawn, most of the feature implementation will be in one component, but a feature implementer will work across boundaries wherever necessary. The architect's challenge is to design so that such boundary-crossing is rare.

The conclusion seems to be that feature-oriented organization is very powerful for two reasons:

- It puts a single mind in control of each user feature.
- It facilitates both design-stage and build-stage user testing of features.

**Growing great designers.** What about the MMM thesis that great design comes from great designers, not from committee processes and that the designer learns by doing—that one does not start with a great designer, but with someone of promise who is grown into a great designer? The Microsoft experience is consistent with that thesis. The technical leaders are grown in house. Microsoft offers a fine milieu for learning software design. One receives much computer science theory in college; learning to design superb software products requires continual guided practice. This Microsoft seems to provide.

## What Is Really New?—Buy versus Build

Arguably the most powerful software productivity strategy to come along in the last 20 years is to Buy versus Build. The computer magazine that arrives in my office contains about 200 pages of ads each month for commercially available software products—thousands and thousands of them. Not only do there exist such tools as have been built in the past, operating systems, compilers, editors, but also there are specialized generators for many kinds of applications. Moreover, one can buy sophisticated software components such as fine color-output modules or graph-plotting modules, and embed them in one's products. It would be foolish to ignore this fecundity.

Why is there such a rich supply today? First, the hardware/ software economy has changed, as Chapter 16 discusses. I believe the crucial modern development is that installed software bases tend to be of one kind of machine or one software platform. Software bases of half a million machines are not uncommon. This is a big change from the 1970s, when the industry standard was an installed base of at most 1000 machines. Even among that thousand, compatibility problems across models of the same line of machines often defeated the portability, so that software packages seldom had a user community larger than a few hundred.

- The microprocessor revolution that brought the low-cost personal computers also brought a standardization of hardware platforms. Instead of each manufacturer offering a one-of-a-kind architecture as in the mainframe world, the microprocessor itself became a well-defined product with a multisource market. Some, such as the Motorola 68000 family and the Intel 8080 family, are each used by many system integrators to build many computer models. This in turn has made possible the evolution of standard software platforms. Today MS-DOS has been licensed for use on probably 100 million machines, Windows for 50 million. The standardization of platform enables software package developers to invest heavily in highly functional products and recoup that investment from a sales volume that achieves an economy of scale, dropping unit price and further extending market.

Even where no single package serves one's need directly, the wide variety of packages makes it cost-effective to buy two or three packages and craft a few interfaces among them. The richness of the commercial software base and the ease of interpackage interfacing depends directly upon the emergence and widespread adoption of standard platforms—common hardware, common operating systems, and common user interfaces. Commercial software tends to be of better quality than home-grown, too. The package builder can afford to hire the best people and build team morale and continuity. He can afford professional user-interface designers. (I have come to believe that graphical user interface design is best separated as a profession from both software architecture and software implementation.) He can afford better testing, including running focus groups to test ease of use. He can afford to build and maintain much more extensive test scaffolding. Such scaffolding is peculiarly leveraged, since it is used on all the copies of the product. In the bad old days, builders of home-grown software were reluctant to invest heavily in test scaffolding for a single shot. But they couldn't afford not to invest heavily in test scaffolding for a tool used by millions.

One of the most important developments in software engineering in the past 20 years is the emergence of published interface definitions that can now serve as accepted standards for programmable interfaces. Books describing the published interfaces for the Macintosh and for Windows occupy feet of shelf space in computer bookstores. This is remarkably different from the 1970s. Not only does the published definition serve those who want to build products for these platforms, the publication itself stamps the interface design as a de facto standard, which makes it much safer to depend upon that interface for systems of long lifetime.

My colleague Dave Gifford was on the team at the MIT Laboratory for Computer Science that developed the X-windows facility and gave it to the world. It has become a standard, in competition with several proprietary windowing systems offered by computer vendors. Gifford's rationale for the give-away was, "The best way to make something a standard is to give it away."

At the same time, the development of the various object-oriented design methods and languages, whether one buys into the whole methodology or not, has prompted a salutary movement toward the more explicit definition of interfaces and the modularization of software. This too has facilitated the build-or-buy decisions in favor of buying. Software packages can be thought of as black boxes, and the craftsman can just read specifications and not worry about the how.

Although this trend toward the explicit publication of interface standards is very wholesome, the software industry still has a long way to go in defining and adopting interface standards systematically. Many wheels still get reinvented. The WIMP graphical interface, for example, is still not a formally adopted industry standard, even for newly designed systems. We find such systems still appearing with command-line interfaces. New user interfaces for hand-held systems are proliferating wildly, although here the proper design still remains an open question. Each vendor proprietary windowing system still has its proprietary data-stream formatting. Too few programmers even know that standard data-interchange formats exist.

These deficiencies are so glaring, the gains from standardization so evident, that I think we shall see steady progress toward more standardization and more explicit publication of interfaces as de facto standards.

## What About the Mythical Man-Month? How Does It Stand Up Today?

The central thesis of the book is that, because of the working time lost in cross-communication, adding people to a late software project just makes it later. Expressed more carefully:

> The number of months of a project depends upon its sequential constraints. The maximum number of men depends upon the number of independent subtasks. From these two quantities one can derive schedules using fewer men and more months. (The only risk is product obsolescence.) One cannot, however, get workable schedules using more men and fewer months. More software projects have gone awry for lack of calendar time than for all other causes combined.

This turns out to be a simplification and needs some serious qualifications. First, it assumes a project running late is still on the learning curve, that the net effect of adding people is negative because they cost more in communication than they contribute in work. Boehm reports that this is true for very large projects only (see Chapter 8).[^14]

Second, my rule oversimplifies the matter of partitionability. Any big system will have some parts that are inherently sequential and cannot be divided, so these set a lower bound on the total elapsed time. But usually there are many loosely coupled parts that offer numerous opportunities for parallel work. The trick is to get at these. Having separate designers for separate features is an important example. The incremental build model is another.

Third, I failed to allow for the fact that the number of people on some large software projects is determined by the calendar constraints, not the workload or other more rational criteria. When delivery by a certain date is a matter of life and death, lots of people are going to be put on the task. So then one needs really to study how to use many people effectively, rather than to show how they will certainly impede one another.

Finally, I did not allow for the "Maintenance Traffic Jam" effect noted in Chapter 8. If a late project has started to be used, then parallel to the push for finishing the new functions, there is the inevitable push to issue urgent fixes to the installed but immature product. The resources these fixes require depend upon the defect level of the installed product. If the original people are assigned to these fixes, the new functions will get delayed even more.

Now if more people are added to work on fixing the installed product, they can indeed make a contribution to unblocking the pipeline. Similarly, since the crises usually come from inadequate testing capacity, skilled testing people added to a late project can indeed have a positive near-term effect.

The central thesis has stood up well under 20 years of scrutiny and development of the state of the art in software project management. Although adding people to a late project doesn't always make it later, the cost-effectiveness of doing so is debatable. We are far from having repealed Brooks's Law.

## Excitement and Skepticism about Silver Bullets

When Chapter 16 was published separately as "No Silver Bullet" in 1986, Parnas called it "a very refreshing paper," and it won the IFIP's award for the best Information Processing paper of that year. Many practitioners have told me that it cleared the air, helping them combat irrational management insistence on machine or method miracles. Other practitioners have said it was too negative, dampening hopes of progress and rationalizing resistance to innovation. Macintosh designer Bill Atkinson objected that if everyone believed there were no silver bullets, none would ever be invented.

I see the situation differently. Enthusiasm is infectious; skepticism also. A promising technical idea can be adopted with faddish hype, everyone expecting miracles. When these fail to materialize, there may be wholesale rejection. I think one can distinguish two critical transitions in the reception cycle of a new technology:

1. Invention, dissemination, adoption
2. Inflation of expectations, disillusionment, solid payoff

The second transition is what Parnas calls the "trough of disillusionment." If one can ride through it, if the technical innovation survives both the hype and the consequent backlash, then it can make a solid contribution. By calling attention to the limits on what any technical innovation can contribute, the "No Silver Bullet" thesis may paradoxically lengthen the productive life of promising ideas, helping them bridge the trough of disillusionment.

## Propositions of The Mythical Man-Month: True or False?

Chapter 18 offers a summary of the management propositions advanced in The Mythical Man-Month. It also invites readers to offer their opinions based on their experience. Many have. Some reviews of the anniversary edition have also responded to that invitation. I find general consensus for most of the propositions. Even sharper, I find consensus on which five propositions are most important:

- Fostering a total-system, architectural, user-oriented attitude is the most important function of the programming manager.
- The separation of architectural effort from implementation is a very powerful way of getting conceptual integrity on very large projects.
- To make that separation, one must have small, sharp architects, each responsible for the conceptual integrity of his or her work.
- The ratio of software installation work to delivery of the product is well over 1:1.
- V. A. Vyssotsky's observation that "Maintenance is the normal state of a programming system."

Other propositions have evoked challenges. A few readers have reported cases where adding people to a late project did help. I concede there are exceptions, as I noted above.

Some readers have vigorously objected to the proposition that good managers are rare, and that one should expect to get good managers only by growing them. These readers note that lots of businesses need managers, and that managers can be recruited from outside software engineering. I still hold that software engineering project management is a special discipline, requiring substantial experience in software engineering, and that one builds managers.

Several readers have objected to the proposition that extrapolating yesterday's progress is a reliable technique for estimating tomorrow's progress. I should have phrased this better. Extrapolation is better than any other estimation technique, but it is by no means reliable. Its reliability is much enhanced if one is in the incremental-build mode, and much degraded if one is in the waterfall mode.

## A Parting Farewell—Pride, Joy, and Excitement

Teaching is great fun, too. I love to see students excited by some insight, thrilled by some experiment, stretching their wings and finding that they really can do a hard task on their own—or more important, as a team.

The software product-building enterprise has it all. It has the pure intellectual challenge of mathematics, the craftsmanship of creating fine things, the exhilaration of doing what has never been done before, the pressure of an application to real human need and aspiration. Teaching it has the same rewards.

> The programmer, like the poet, works only slightly removed from pure thought-stuff. He builds his castles in the air, from air, creating by exertion of the imagination. Few media of creation are so flexible, so easy to polish and rework, so readily capable of realizing grand conceptual structures. Yet the program construct, unlike the poet's words, is real in the sense that it moves and works, producing visible outputs separate from the construct itself. It prints results, draws pictures, produces sounds, moves arms. The magic of myth and legend has come true in our time. One types the correct incantation on a keyboard, and a display screen comes to life, showing things that never were nor could be.
>
> Programming then is fun because it gratifies creative longings built deep within us and delights sensibilities we have in common with all men.

[^1]: D. L. Parnas, "Software Aspects of Strategic Defense Systems," American Scientist (Nov.-Dec., 1985), makes this point most eloquently. The same issue has several other pointed articles on software.

[^2]: T. R. Braun, "Word 6.0 packs in features; update slowed by baggage," Macworld (Apr., 1994), p. 53.

[^3]: Dennis Wixon of Digital Equipment Corporation has undertaken customer surveys to find what features are really important to users. He first discovers to his surprise, and confirms by replication, that each and every feature of a product is rated "most important" by some user. People remember the individual features, not the overall experience. They are not good at judging what makes a product hard to learn or hard to use.

[^4]: J. Conklin and M. Begeman, "gIBIS: A hypertext tool for exploratory policy discussion," ACM Transactions on Office Information Systems, 6, 4 (1988).

[^5]: D. Englebart and W. English, "A research center for augmenting human intellect," AFIPS Conference Proceedings, FJCC (1968), pp. 395–410.

[^6]: B. Lampson, "Personal Distributed Computing: The Alto and Ethernet Software," in A History of Personal Workstations, A. Goldberg, ed. Reading, MA: Addison-Wesley, 1988, pp. 291–344, is a fascinating account. Apple Computer, Inc., Macintosh Human Interface Guidelines. Reading, MA: Addison-Wesley, 1992, documents many reasons for design decisions.

[^7]: B. A. Meyers, "A brief history of human-computer interaction technology," ACM Interactions, V, 2 (Mar., 1996), pp. 44–54, shows a 1963 Sketchpad system designed by Ivan Sutherland that used two hands, one holding a light pen, the other operating a button box.

[^8]: W. W. Royce, "Managing the development of large software systems: Concepts and techniques," WESCON (1970).

[^9]: Thanks to Col. Don Anderson for instruction on this subject.

[^10]: H. D. Mills, M. Dyer, and R. Linger, "Cleanroom Software Engineering," IEEE Software (Sept., 1987), pp. 19–25.

[^11]: D. L. Parnas, "Designing software for ease of extension and contraction," IEEE Transactions on Software Engineering, 5, 2 (1979).

[^12]: J. McCarthy, Dynamics of Software Development. Redmond, WA: Microsoft Press, 1995, pp. 14–19.

[^13]: Ibid., pp. 14–66.

[^14]: B. Boehm, Software Engineering Economics. Englewood Cliffs, NJ: Prentice-Hall, 1981, p. 40.
