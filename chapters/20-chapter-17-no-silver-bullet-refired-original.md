# Chapter 17: "No Silver Bullet" Refired

> Every bullet has its billet.
>
> — WILLIAM III OF ENGLAND, PRINCE OF ORANGE
>
> Whoever thinks a faultless piece to see,
> Thinks what never was, nor is, nor ever shall be.
>
> — ALEXANDER POPE, AN ESSAY ON CRITICISM

## On Werewolves and Other Legendary Terrors

"No Silver Bullet—Essence and Accidents of Software Engineering" (now Chapter 16) was originally an invited paper for the IFIP '86 conference in Dublin, and it was published in those proceedings.[^1] Computer magazine reprinted it, behind a gothic cover, illustrated with stills from films such as The Werewolf of London.[^2] They also provided an explanatory sidebar "To Slay the Werewolf," setting forth the (modern) legend that only silver bullets will do. I was not aware of the sidebar and illustrations before publication, and I never expected a serious technical paper to be so embellished.

Computer's editors were expert in achieving their desired effect, however, and many people seem to have read the paper. I have therefore chosen yet another werewolf picture for that chapter, an ancient depiction of an almost comical creature. I hope this less garish picture will have the same salutary effect.

## There is Too a Silver Bullet—AND HERE IT IS

"No Silver Bullet" asserts and argues that no single software engineering development will produce an order-of-magnitude improvement in programming productivity within ten years (from the paper's publication in 1986). We are now nine years into that decade, so it is timely to see how this prediction is holding up.

Whereas The Mythical Man-Month generated many citations but little argument, "No Silver Bullet" has occasioned rebuttal papers, letters to journal editors, and letters and essays that continue to this day.[^3] Most of these attack the central argument that there is no magical solution, and my clear opinion that there cannot be one. Most agree with most of the arguments in "NSB," but then go on to assert that there is indeed a silver bullet for the software beast, which the author has invented. As I reread the early responses today, I can't help noticing that the nostrums pushed so vigorously in 1986 and 1987 have not had the dramatic effects claimed.

I buy hardware and software chiefly by the "happy user" test—conversations with bona fide cash-paying customers who use the product and are pleased. Likewise, I shall most readily believe a silver bullet has materialized when a bona fide independent user steps forth and says, "I used this methodology, tool, or product, and it gave me a tenfold improvement in software productivity."

Many correspondents have made valid emendations or clarifications. Some have undertaken point-by-point analysis and rebuttal, for which I am grateful. In this chapter, I shall share the improvements and address the rebuttals.

## Obscure Writing Will Be Misunderstood

Some writers show that I failed to make some arguments clear.

**Accident.** The central argument of "NSB" is as clearly stated in the Abstract to Chapter 16 as I know how to put it. Some have been confused, however, by the terms accident and accidental, which follow an ancient usage going back to Aristotle.[^4] By accidental, I did not mean occurring by chance, nor misfortunate, but more nearly incidental, or appurtenant.

I would not denigrate the accidental parts of software construction; instead I follow the English dramatist, detective story writer, and theologian Dorothy Sayers in seeing all creative activity to consist of (1) the formulation of the conceptual constructs, (2) implementation in real media, and (3) interactivity with users in real uses.[^5] The part of software building I called essence is the mental crafting of the conceptual construct; the part I called accident is its implementation process.

**A question of fact.** It seems to me (although not to everyone) that the truthfulness of the central argument boils down to a question of fact: What fraction of total software effort is now associated with the accurate and orderly representation of the conceptual construct, and what fraction is the effort of mentally crafting the constructs? The finding and fixing of flaws falls partly in each fraction, according to whether the flaws are conceptual, such as failing to recognize some exception, or representational, such as a pointer mistake or a memory allocation mistake.

It is my opinion, and that is all, that the accidental or representational part of the work is now down to about half or less of the total. Since this fraction is a question of fact, its value could in principle be settled by measurement.[^6] Failing that, my estimate of it can be corrected by better informed and more current estimates. Significantly, no one who has written publicly or privately has asserted that the accidental part is as large as 9/10.

"NSB" argues, indisputably, that if the accidental part of the work is less than 9/10 of the total, shrinking it to zero (which would take magic) will not give an order of magnitude productivity improvement. One must attack the essence.

Since "NSB," Bruce Blum has drawn my attention to the 1959 work of Herzberg, Mausner, and Sayderman.[^7] They find that motivational factors can increase productivity. On the other hand, environmental and accidental factors, no matter how positive, cannot; but these factors can decrease productivity when negative. "NSB" argues that much software progress has been the removal of such negative factors: stunningly awkward machine languages, batch processing with long turnaround times, poor tools, and severe memory constraints.

Are the essential difficulties therefore hopeless? An excellent 1990 paper by Brad Cox, "There Is a Silver Bullet," argues eloquently for the reusable, interchangeable component approach as an attack on the conceptual essence of the problem.[^8] I enthusiastically agree.

Cox however misunderstands "NSB" on two points. First, he reads it as asserting that software difficulties arise "from some deficiency in how programmers build software today." My argument was that the essential difficulties are inherent in the conceptual complexity of the software functions to be designed and built at any time, by any method. Second, he (and others) read "NSB" as asserting that there is no hope of attacking the essential difficulties of software building. That was not my intent. Crafting the conceptual construct does indeed have as inherent difficulties complexity, conformity, changeability, and invisibility. The troubles caused by each of these difficulties can, however, be ameliorated.

**Complexity is by levels.** For example, complexity is the most serious inherent difficulty, but not all complexity is inevitable. Much, but not all, of the conceptual complexity in our software constructs comes from the arbitrary complexity of the applications themselves. Indeed, Lars Sødahl of MYSIGMA Sødahl and Partners, a multinational management consulting firm, writes:

> In my experience most of the complexities which are encountered in systems work are symptoms of organizational malfunctions. Trying to model this reality with equally complex programs is actually to conserve the mess instead of solving the problems.

Steve Lukasik of Northrop argues that even organizational complexity is perhaps not arbitrary but may be susceptible to ordering principles:

> I trained as a physicist and thus see "complex" things as susceptible to description in terms of simpler concepts. Now you may be right; I will not assert that all complex things are susceptible to ordering principles. . . . by the same rules of argument you cannot assert that they can not be.
>
> . . . Yesterday's complexity is tomorrow's order. The complexity of molecular disorder gave way to the kinetic theory of gases and the three laws of thermodynamics. Now software may not ever reveal those kinds of ordering principles, but the burden is on you to explain why not. I am not being obtuse or argumentative. I believe that someday the "complexity" of software will be understood in terms of some higher order notions (invariants to the physicist).

I have not undertaken the deeper analysis Lukasik properly calls for. As a discipline, we need an extended information theory that quantifies the information content of static structures, just as Shannon's theory does for communicated streams. That is quite beyond me. To Lukasik I simply respond that system complexity is a function of myriad details that must each be specified exactly, either by some general rule or detail-by-detail, but not just statistically. It seems very unlikely that uncoordinated works of many minds should have enough coherence to be exactly described by general rules.

Much of the complexity in a software construct is, however, not due to conformity to the external world but rather to the implementation itself—its data structures, its algorithms, its connectivity. Growing software in higher-level chunks, built by someone else or reused from one's own past, avoids facing whole layers of complexity. "NSB" advocates a wholehearted attack on the problem of complexity, quite optimistic that progress can be made. It advocates adding necessary complexity to a software system:

- Hierarchically, by layered modules or objects
- Incrementally, so that the system always works.

## Harel's Analysis

David Harel, in the 1992 paper, "Biting the Silver Bullet," undertakes the most careful analysis of "NSB" that has been published.[^9]

**Pessimism vs. optimism vs. realism.** Harel sees both "NSB" and Parnas's 1984 "Software Aspects of Strategic Defense Systems,"[^10] as "far too bleak." So he aims to illuminate the brighter side of the coin, subtitling his paper "Toward a Brighter Future for System Development." Cox as well as Harel reads "NSB" as pessimistic, and he says, "But if you view these same facts from a new perspective, a more optimistic conclusion emerges." Both misread the tone.

First, my wife, my colleagues, and my editors find me to err far more often in optimism than in pessimism. I am, after all, a programmer by background, and optimism is an occupational disease of our craft.

"NSB" says explicitly "As we look to the horizon of a decade hence, we see no silver bullet. . . . Skepticism is not pessimism, however. . . . There is no royal road, but there is a road." It forecasts that the innovations under way in 1986, if developed and exploited, would together indeed achieve an order-of-magnitude improvement in productivity. As the 1986-1996 decade proceeds, this prediction appears, if anything, too optimistic rather than too gloomy.

Even if "NSB" were universally seen as pessimistic, what is wrong with that? Is Einstein's statement that nothing can travel faster than the speed of light "bleak" or "gloomy?" How about Godel's result that some things cannot be computed? "NSB" undertakes to establish that "the very nature of software makes it unlikely that there will ever be any silver bullets." Turski, in his excellent response paper at the IFIP Conference, said eloquently:

> Of all misguided scientific endeavours, none are more pathetic than the search for the philosophers' stone, a substance supposed to change base metals into gold. The supreme object of alchemy, ardently pursued by generations of researchers generously funded by secular and spiritual rulers, is an undiluted extract of wishful thinking, of the common assumption that things are as we would like them to be. It is a very human belief. It takes a lot of effort to accept the existence of insoluble problems. The wish to see a way out, against all odds, even when it is proven that it does not exist, is very, very strong. And most of us have a lot of sympathy for these courageous souls who try to achieve the impossible. And so it continues. Dissertations on squaring a circle are being written. Lotions to restore lost hair are concocted and sell well. Methods to improve software productivity are hatched and sell very well.
>
> All too often we are inclined to follow our own optimism (or exploit the optimistic hopes of our sponsors). All too often we are willing to disregard the voice of reason and heed the siren calls of panacea pushers.[^11]

Turski and I both insist that pipe-dreaming inhibits forward progress and wastes effort.

**"Gloom" themes.** Harel perceives gloom in "NSB" to arise from three themes:

- Sharp separation into essence and accident
- Treatment of each silver bullet candidate in isolation
- Predicting for only 10 years, instead of a long enough time in which "to expect any significant improvement."

As to the first, that is the whole point of the paper. I still believe this separation is absolutely central to understanding why software is hard. It is a sure guide as to what kinds of attacks to make.

As to treating candidate bullets in isolation, "NSB" does so indeed. The various candidates have been proposed one by one, with extravagant claims for each one by itself. It is fair to assess them one by one. It is not the techniques I oppose, it is expecting them to work magic. Glass, Vessey, and Conger in their 1992 paper offer ample evidence that the vain search for a silver bullet has not yet ended.[^12]

As to choosing 10 years versus 40 years as a prediction period, the shorter period was in part a concession that our predictive powers have never been good beyond a decade. Which of us in 1975 predicted the microcomputer revolution of the 1980s?

There are other reasons for the decade limit: the claims made for candidate bullets all have had a certain immediacy about them. I recollect none that said "Invest in my nostrum, and you will start winning after 10 years." Moreover, hardware performance/price ratios have improved by perhaps a hundredfold per decade, and the comparison, though quite invalid, is subconsciously inevitable. We will surely make substantial progress over the next 40 years; an order of magnitude over 40 years is hardly magical.

**Harel's thought experiment.** Harel proposes a thought experiment in which he postulates "NSB" as having been written in 1952, instead of 1986, but asserting the same propositions. This he uses as a reducto ad absurdum to argue against attempting to separate essence from accident.

The argument doesn't work. First, "NSB" begins by asserting that the accidental difficulties grossly dominated the essential ones in 1950s programming, that they no longer do so, and that eliminating them has effected orders-of-magnitude improvements. Translating that argument back 40 years is unreasonable; one can hardly imagine asserting in 1952 that the accidental difficulties do not occasion a major part of the effort.

Second, the state of affairs Harel imagines to have prevailed in the 1950s is inaccurate:

> That was the time when instead of grappling with the design of large, complex systems, programmers were in the business of developing conventional one-person programs (which would be on the order of 100—200 lines in a modern programming language) that were to carry out limited algorithmic tasks. Given the technology and methodology available then, such tasks were similarly formidable. Failures, errors, and missed deadlines were all around.

He then describes how the postulated failures, errors, and missed deadlines in the conventional little one-person programs were improved by an order of magnitude over the next 25 years.

But the state of the art in the 1950s was not in fact small one-person programs. In 1952, the Univac was at work processing the 1950 census with a complex program developed by about eight programmers.[^13] Other machines were doing chemical dynamics, neutron diffusion calculations, missile performance calculations, etc.[^14] Assemblers, relocating linkers and loaders, floating-point interpretive systems, etc. were in routine use.[^15]

By 1955 people were building 50 to 100 man-year business programs.[^16] By 1956 General Electric had in operation a payroll system in its Louisville appliance plant with more than 80,000 words of program. By 1957, the SAGE ANFSQ/7 air defense computer had been running two years, and a 75,000 instruction communications-based, fail-safe-duplexed real-time system was in operation in 30 sites.[^17] One can hardly maintain that it is evolution of techniques for one-person programs that chiefly describes software engineering efforts since 1952.

**AND HERE IT IS.** Harel goes on to offer his own silver bullet, a modeling technique called "The Vanilla Framework." The approach itself is not described in enough detail for evaluation, but reference is given to a paper, and to a technical report to appear in book form in due time.[^18] Modeling does address the essence, the proper crafting and debugging of concepts, so it is possible that the Vanilla Framework will be revolutionary. I hope so. Ken Brooks reports he found it a helpful methodology when he tried it for a real task.

**Invisibility.** Harel argues strongly that much of the conceptual construct of software is inherently topological in nature and these relationships have natural counterparts in spatial/graphical representations:

> Using appropriate visual formalisms can have a spectacular effect on engineers and programmers. Moreover, this effect is not limited to mere accidental issues; the quality and expedition of their very thinking was found to be improved. Successful system development in the future will revolve around visual representations. We will first conceptualize, using the "proper" entities and relationships, and then formulate and reformulate our conceptions as a series of increasingly more comprehensive models represented in an appropriate combination of visual languages. A combination it must be, since system models have several facets, each of which conjures up different kinds of mental images.
>
> . . . . Some aspects of the modeling process have not been as forthcoming as others in lending themselves to good visualization. Algorithmic operations on variables and data structures, for example, will probably remain textual.

Harel and I are quite close. What I argued is that software structure is not embedded in three-space, so there is no natural single mapping from a conceptual design to a diagram, whether in two dimensions or more. He concedes, and I agree, that one needs multiple diagrams, each covering some distinct aspect, and that some aspects don't diagram well at all.

I completely share his enthusiasm for using diagrams as thought and design aids. I have long enjoyed asking candidate programmers, "Where is next November?" If the question is too cryptic, then, "Tell me about your mental model of the calendar." The really good programmers have strong spatial senses; they usually have geometric models of time; and they quite often understand the first question without elaboration. They have highly individualistic models.

## Jones's Point—Productivity Follows Quality

Capers Jones, writing first in a series of memoranda and later in a book, offers a penetrating insight, which has been stated by several of my correspondents. "NSB," like most writings at the time, was focused on productivity, the software output per unit of input. Jones says, "No. Focus on quality, and productivity will follow."[^19] He argues that costly and late projects invest most of the extra work and time in finding and repairing errors in specification, in design, in implementation. He offers data that show a strong correlation between lack of systematic quality controls and schedule disasters. I believe it. Boehm points out that productivity drops again as one pursues extreme quality, as in IBM's space-shuttle software.

Coqui similarly argues that systematic software development disciplines were developed in response to quality concerns (especially avoidance of major disasters) rather than productivity concerns.

> But note: the goal of applying Engineering principles to Software production in the 1970s was to increase the Quality, Testability, Stability, and Predictability of software products—not necessarily the efficiency of Software production.
>
> The driving force to use Software Engineering principles in software production was the fear of major accidents that might be caused by having uncontrollable artists responsible for the development of ever more complex systems.[^20]

## So What Has Happened to Productivity?

**Productivity numbers.** Productivity numbers are very hard to define, hard to calibrate, and hard to find. Capers Jones believes that for two equivalent COBOL programs written 10 years apart, one without structured methodology and one with, the gain is a factor of three.

Ed Yourdon says, "I see people getting a fivefold improvement due to workstations and software tools." Tom DeMarco believes "Your expectation of an order-of-magnitude improvement in 10 years, due to the whole basket of techniques, was optimistic. I haven't seen organizations making an order-of-magnitude improvement."

**Shrink-wrapped software—Buy; don't build.** One 1986 assessment in "NSB" has, I think, proved to be correct: "The development of the mass market is . . . the most profound long-run trend in software engineering." From the discipline's viewpoint, the mass-market software is almost a new industry compared to that of the development of custom software, whether in-house or out-house. When packages sell in the millions—or even the thousands—quality, timeliness, product performance, and support cost become dominant issues, rather than the development cost that is so crucial for custom software.

**Power tools for the mind.** The most dramatic way to improve the productivity of management information systems (MIS) programmers is to go down to your local computer store and buy off the shelf what they would have built. This is not ridiculous; the availability of cheap, powerful shrink-wrapped software has met many needs that formerly would have occasioned custom packages. These power tools for the mind are more like electric drills, saws, and sanders than they are like big complex production tools. The integration of these into compatible and cross-linked sets such as Microsoft Works and the better-integrated ClarisWorks give immense flexibility. And like the homeowner's collection of power hand tools, frequent use of a small set, for many different tasks, develops familiarity. Such tools must emphasize ease of use for the casual user, not the professional.

Ivan Selin, Chairman of American Management Systems, Inc., wrote me in 1987:

> I quibble with your statement that packages have not really changed that much. . . : I think you too lightly throw off the major implications of your observation that, [the software packages] "may be somewhat more generalized and somewhat more customizable than formerly, but not much." Even accepting this statement at face value, I believe that the users see the packages as being both more generalized and easier to customize, and that this perception leads the users to be much more amenable to packages. In most cases that my company finds, it is the [end] users, not the software people, who are reluctant to use packages because they think they will lose essential features or functions, and hence the prospect of easy customization is a big selling point to them.

I think Selin is quite right—I underestimated both the degree of package customizability and its importance.

## Object-Oriented Programming—Will a Brass Bullet Do?

**Building with bigger pieces.** The illustration opening this chapter reminds us that if one assembles a set of pieces, each of which may be complex, and all of which are designed to have smooth interfaces, quite rich structures go together rapidly.

One view of object-oriented programming is that it is a discipline that enforces modularity and clean interfaces. A second view emphasizes encapsulation, the fact that one cannot see, much less design, the inner structure of the pieces. Another view emphasizes inheritance, with its concomitant hierarchical structure of classes, with virtual functions. Yet another view emphasizes strong abstract data-typing, with its assurance that a particular data-type will be manipulated only by operations proper to it.

Now any of these disciplines can be had without taking the whole Smalltalk or C++ package—many of them predated object-oriented technology. The attractiveness of object-oriented approach is that of a multivitamin pill: in one fell swoop (that is, programmer retraining), one gets them all. It is a very promising concept.

**Why has object-oriented technique grown slowly?** In the nine years since "NSB," the expectancy has steadily grown. Why has growth been slow? Theories abound. James Coggins, author for four years of the column, "The Best of comp.lang.c++" in The C++ Report, offers this explanation:

> The problem is that programmers in O-O have been experimenting in incestuous applications and aiming low in abstraction, instead of high. For example, they have been building classes such as linked-list or set instead of classes such as user-interface or radiation beam or finite-element model. Unfortunately the selfsame strong type-checking in C++ that helps programmers to avoid errors also makes it hard to build big things out of little ones.[^21]

He goes back to the basic software problem, and argues that one way to address unmet software needs is to increase the size of the intelligent workforce by enabling and coopting our clients. This argues for top-down design:

> If we design large-grained classes that address concepts our clients are already working with, they can understand and question the design as it grows, and they can cooperate in the design of test cases. My ophthalmology collaborators don't care about stacks; they do care about Legendre polynomial shape descriptions of corneas.

Small encapsulations yield small benefits.

David Parnas, whose paper was one of the origins of object-oriented concepts, sees the matter differently. He writes me:

> The answer is simple. It is because [O-O] has been tied to a variety of complex languages. Instead of teaching people that O-O is a type of design, and giving them design principles, people have taught that O-O is the use of a particular tool. We can write good or bad programs with any tool. Unless we teach people how to design, the languages matter very little. The result is that people do bad designs with these languages and get very little value from them. If the value is small, it won't catch on.

**Front-loaded costs, down-stream benefits.** My own belief is that object-oriented techniques have a peculiarly severe case of a malady that characterizes many methodological improvements. The up-front costs are very substantial—primarily retraining programmers to think in a quite new way, but also extra investment in fashioning functions into generalized classes. The benefits, which I think are real and not merely putative, occur all along the development cycle; but the big benefits pay off during successor building, extension, and maintenance activities.

Coggins says, "Object-oriented techniques will not make the first project development any faster, or the next one. The fifth one in that family will go blazingly fast."[^22]

Betting real up-front money for the sake of projected but iffy benefits later is what investors do every day. In many programming organizations, however, it requires real managerial courage, a commodity much scarcer than technical competence or administrative proficiency. I believe the extreme degree of cost front-loading and benefit back-loading is the largest single factor slowing the adoption of O-O techniques. Even so, C++ seems to be steadily replacing C in many communities.

## What About Reuse?

The best way to attack the essence of building software is not to build it at all. Package software is only one of the ways of doing this. Program reuse is another. Indeed, the promise of easy reuse of classes, with easy customization via inheritance, is one of the strongest attractions of object-oriented techniques.

As is so often the case, as one gets some experience with a new way of doing business the new mode is not so simple as first appears.

Of course, programmers have always reused their own handiwork. Jones says,

> Most experienced programmers have private libraries which allow them to develop software with about 30% reused code by volume. Reusability at the corporate level aims for 75% reused code by volume, and requires special library and administrative support. Corporate reusable code also implies changes in project accounting and measurement practices to give credit for reusability.[^23]

W. Huang proposed organizing software factories with a matrix management of functional specialists, so as to harness the natural propensity of each to reuse his own code.[^24]

Van Snyder of JPL points out to me that the mathematical software community has a long tradition of reusing software:

> We conjecture that barriers to reuse are not on the producer side, but on the consumer side. If a software engineer, a potential consumer of standardized software components, perceives it to be more expensive to find a component that meets his need, and so verify, than to write one anew, a new, duplicative component will be written. Notice we said perceives above. It doesn't matter what the true cost of reconstruction is.
>
> Reuse has been successful for mathematical software for two reasons: (1) It is arcane, so software engineers [who aren't mathematicians] don't think they can reconstruct it or verify it. (2) It has been catalogued very well, which reduces the cost of finding it.

We have to catalogue our reusable components very well indeed, and we have to teach programmers both how to catalogue and how to retrieve.

## Learning to Design—The Incremental-Build Model

Lloyd Williams of IBM challenged me with this assertion:

> The problem with always finding and fixing defects is that you'll never learn to do it right. Students need feedback on the quality of their designs before they have been implemented. Unfortunately, software has been invisible. Now that we can achieve some visibility through very high level graphical languages, [students can be taught better, earlier.]

Williams is arguing that we will never learn to design well by jumping straight into implementations. The student, indeed the journeyman designer, needs practice and feedback on designs themselves. We need ways of rendering designs, particularly the conceptual constructs, concrete enough to criticize. Pictures and diagrams have classically been the way to achieve this concreteness.

Williams advocates teaching programming with LabView, an interactive graphic programming language with simultaneous display of a block diagram view of the program and a front panel view. LabView has the great disadvantage that it is geared toward a narrow range of problems—instrumentation and control. It has the great advantage of allowing students to design test setups, build virtual instruments, see and adjust the designs, and then see them run.

Object-oriented techniques are teaching many people that to build right, one must build an initial implementation quickly, then iteratively refine it based on user experience and user feedback. This is the theme running through Cox's and Harel's suggestions. James Coggins teaches another dimension—the importance of starting with truly high-level abstractions. That, as he points out, is how one keeps the user engaged in the design conversation.

Certainly we want students to design first, then build. The incremental-build model does it both ways—one builds, then one designs the next iteration. A crucial part of the learning process is to have one's designs examined—and critiqued—by master designers. Harlan Mills pioneered the technique of a design review before any code was written; his experience in the IBM Federal Systems Division [FSB] convinced both management and programmers.[^25]

## The Skeptical View of All-in-One Environments

"NSB" says:

> It is difficult to see how [object-oriented programming, artificial intelligence, expert systems, or "automatic programming"] provide the revolutionary [order-of-magnitude] advances that are needed.

My implicit assumption was that revolutionary breakthroughs would be most likely to come from focused individual technologies—silver bullets—rather than from all-in-one combinations of attack approaches—bullets of brass, or baser alloys. Harel strongly challenges this view:

> [Brooks] might have a point if breakthroughs emerge singly and separately from powerful attempts to push forward one idea at the expense of others. But if they work in concert or in tandem, if the magic emerges from the combination and interaction of various ideas and tools, then I believe his conclusion is too bleak.[^26]

Harel goes on to talk about modeling as
... a large multidimensional space, with a multiplicity of modeling languages each geared toward some aspects of the problem but not to others. Devising a way to link [them] so that they complement each other is the key.

This is what object-oriented programming is all about—at least linking data structures and algorithms through encapsulation, data abstractions, abstract data types, and inheritance. The several views can usually have the same names for things. More is at stake than just the fact that OOP practitioners believe all of these disciplines to be synergistic. We have empirical evidence of this: Stroustrup's C++ has caught on far faster than the simple and elegant Niklaus Wirth languages—Modula-2 and Oberon—that embody only parts of the OOP package.[^27]

What about bigger packages than just object-oriented programming environments? How about full Program Support Environments, including compilers, editors, dependency-controlled builders, version-control managers, etc., all with one uniform user interface? Surely that is a Good Thing?

Well, I am not so sure. I see today two kinds of all-in-one environments. Emacs[^28] is one kind—extensible and customizable. It embodies a vision and a discipline, and it is packaged for convenience. One does not, however, have to take all-or-none. One can use only parts, and one can buy compilers, etc. from others and integrate them oneself, at some cost. The other kind of all-in-one environment is a total package, whose tools are more or less tightly bound together. Often only the vendor's own compiler, builder, etc. are included.

I hold a prejudice, no more, that the all-in-one-package total environments are a snare. First, they are built around some framework and methodology, whose implicit assumptions constrain the user whether or not he is aware. Second, one is stuck with the vendor's tool set. If I want to take advantage of some truly superior tool—perhaps even a revolutionary one—it is difficult or impossible to substitute that new tool for one in the proffered set. Moreover, the package as a whole gets obsoleted by the weakest of its components. In both these ways, the all-in-one environment deprives me of the flexibility I have learned I desperately need.

The counterargument to this view is that a single-sourced, tightly-coupled environment will usually have a better user interface, in the sense that all the tools fit together harmoniously. That is an advantage I think is far less than its advocates believe, and one that is typically obtained at high price in terms of dollars and in terms of lost flexibility.

The most powerful argument of all is that a harmoniously integrated environment enables higher productivity if not richer programming. Boehm's large study of software engineering productivity found that use of integrated tools was indeed one of the top two factors in achieving high productivity—along with high-level language use. It beat out all of the other technical factors.[^29] Moreover, Boehm's data show tool-integration as second in importance, not far behind high-level language. Clearly there is something worth pursuing here.

## Hopes for the Hype: Does Anything Really Promising Loom on the Software Engineering Horizon?

All silver bullets aside, are there innovations on the horizon that seem to offer real promise? To this I answer yes, with some optimism.

### Object-Oriented Programming

The integrated set of concepts, discipline, and tools offers promise of an easing of accidental difficulties, not a breakthrough, but steady progress at least.

### Reusable software component libraries

As the UNIX community discovered a decade ago, and as DoD is now learning, reusable software components from high quality subroutine libraries can give real productivity boosts. Capers Jones estimates, from his large industrial database, that it takes about 4000 hours to build, document, and integrate a well-designed and implemented 1000-line component into a reusable subroutine library. He further estimates that use and reuse will buy that investment back in about three uses.[^30]

### Rapid prototyping

As Harel and others argue, iterative extract-from-the-user, build, let-him-try-it cycles are the most effective way to converge on a good product design.

### Incremental development

Growing, not building, software: Harlan Mills's insight that one should plan to build an initial skeletal implementation very early and then to flesh it out, always keeping a working system, is one of the biggest discoveries in my software engineering lifetime. The incremental-build model is now routinely but incompletely practiced; it needs to be universally taught and practiced.[^31]

### Great designers

Capers Jones's data show that the differences between the best software designers and the poorest is not as great as that which has been measured between the best and poorest programmers. Nevertheless the difference is real—about an order of magnitude.[^32] So the most important thing we can do for software productivity and quality is to develop our people.

First, we must carefully select people who have, or can develop, those design talents. Sheer intelligence is not enough; one also needs interest, the kind that keeps one thinking and playing with design issues in off hours, and some experience.

Second, we must provide career paths for these designers so that we can keep them designing. Hierarchical organizations offer one kind of career path. Matrix organizations need to ensure that designers continue as designers.

Third, we can study and disseminate the best design practices. A great designer is not likely to be made out of an indifferent one. Yet we can teach even journeyman designers many of the tricks, heuristics, and strategies that are part of the toolkits and kits of tricks of the great designers.

Fourth, and still more controversial, we need to allow the designers to interact directly with users. Parnas makes a compelling case for having the designers build an initial implementation before turning the design over to production teams for extension and maintenance. At least as important, designers need to watch real people use their programs.[^33]

## Greatness Cannot Be Taught, But It Can Be Learned

The British, with a keener sense of the distinction between science, engineering, and craft, call their best programmers "cutters." At American universities we do not often think of ourselves as teaching a craft, or as taking on apprentices. Nevertheless I think what the software engineer most needs to learn, what he will be able to use 40 years hence, is what I once heard a dean of engineering call the "fundamental engineering verities," by which he meant not engineering science, but craft. One learns these like one learns to design sailboats—on the knees of master designers. The great English naval architect John Scott Russell said:

> A scientific education . . . which does not commence with actual practice, but with rules of theory . . . inverts the natural order, reverses the method which has created every existing art, and is certain to produce nothing but failure and disappointment.[^34]

The most powerful and effective training for great designers, therefore, is to put apprentice designers under the guidance of master designers for years, and to get them into direct contact with users of real systems. How can we arrange this?

One way is to have the best designers be team leaders. More on this later.

Another way is to study what Pirsig calls the "high-quality product."[^35] In an appendix to The Mythical Man-Month I listed some classic programs and systems that seemed to me to be breakthrough designs. More such lists would be helpful, as would careful and deep case study of these systems, as to their design, the design process, the people who designed them. We need far more documentation of why the designers made the choices they made.

We also need to study how much various practices help or hinder. For example, Boehm's study shows that the use of modern programming practices is indeed associated with high productivity.[^36] The study also shows, however, that top-down design bears little correlation with productivity.

Finally, I think we need to recognize programming as an individual creative activity and deal with it as such. In our zeal to "get software development under control," we have rushed to regiment and straijacket the process. Now the time has come to try libertarian rather than totalitarian approaches. We need to empower the individual programmer to be productive his way. James Coggins, with decades of software engineering experience, puts it as strongly as words can put it:

> Ultimately, the disciplined application of old and new software engineering techniques will not save us. It never really has. What saves any project is the emergence of leaders who are zealous in their pursuit of truth—truth in the form of a good design, truth in the form of a correct implementation, truth in the form of quality software. How can we instill this into people? I don't know that it can be taught, but if it can it will not be done by inculcating disciplines and imposing standards. It must be learned, and to be learned it must be experienced.[^37]

## "No Silver Bullet" Refined—Not Retracted

After nine years, the central argument of "No Silver Bullet" is not yet disproved. No technological breakthrough has become available that would enable an order-of-magnitude improvement in software productivity, reliability, simplicity.

Some will read this chapter as a resounding of the pessimism. I disagree. Indeed, the main point of "NSB" is one of joy. Our "software crisis" is not a crisis of being able to meet only psychological needs; Maslow would assure us that the crisis will not go away.[^38] The main point of "NSB" is that, if we look carefully at the nature of software engineering, we can see that it is inherently a complex activity, quite different from other engineering. This difference, far from being discouraging, opens the door to truly exciting possibilities.

We can learn what it is that intrinsically characterizes software construction, and we can use that understanding to improve radically the way we engineer software systems. In seeking the nature of our discipline, we find that most of the difficulties are conceptual, and so they can best be attacked by better thinking, not by more technology. We must set about devising strategies for conceptualizing, for conceptual integrity, for abstract data typing. We must provide incentives for reuse. We must find ways to grow trial implementations cheaply and quickly. We must train and nourish great designers.

I see this as most exciting and hopeful. The agrarian revolution, the industrial revolution, the electronic revolution all took long development times and then swept forward. We have the great good fortune of living in the infancy of a revolution—the software revolution. However difficult its problems, however slow the progress to date, let us give thanks that our lot is cast not where the work is routine and repetitive, but rather where the work is an intellectual adventure.

Even if my premise turns out to be wrong, I hope the central argument of "NSB" will have proved useful. If it has provoked and stimulated discussion and research into the nature of software engineering, that is enough contribution for any single paper. One could hardly ask for more.

[^1]: F. P. Brooks, "No Silver Bullet—Essence and Accidents of Software Engineering," Information Processing 1986, the Proceedings of the IFIP Tenth World Computing Conference, H.-J. Kugler, ed., Amsterdam: Elsevier Science, pp. 1069-1076.

[^2]: F. P. Brooks, "No Silver Bullet—Essence and Accidents of Software Engineering," Computer, 20, 4 (April, 1987), pp. 10-19.

[^3]: P. Kjelldahl, ed., "Special Issue—No Silver Bullet Revisited," American Programmer, 5, 10 (November, 1992), pp. 2-69. Although billed as "revisited," the papers in this issue are (chiefly) rebuttals.

[^4]: Aristotle, Metaphysics, 8, 2, 1042b - 1043a.

[^5]: D. Sayers, The Mind of the Maker, San Francisco: Harper and Row (1979—first published 1941). She explicitly develops the analogy between God the Creator and the human creator, showing how each made work has (1) the Creative Idea, "the complete, fundamental, self-consistent concept of the whole work," existing only in the creator's mind; (2) the Creative Execution, "the Expression . . . in a form perceptible to the bodily senses," including the act of creation and the work; (3) the Creative Response, "the power of the [work] to evoke a corresponding response in other human beings," that is, its use and enjoyment.

[^6]: H. D. Mills, M. Dyer, and R. Linger, "Cleanroom Software Engineering," IEEE Software, 4, 5 (September, 1987), pp. 19-25.

[^7]: F. Herzberg, B. Mausner, B. B. Snyderman, The Motivation to Work, New York: Wiley (1959).

[^8]: B. Cox, "There Is a Silver Bullet," Byte, 15, 10 (October, 1990), pp. 209-218.

[^9]: D. Harel, "Biting the Silver Bullet—Toward a Brighter Future for System Development," Computer, 25, 1 (January, 1992), pp. 8-20. Harel's paper is somewhat unusual in the sense that he analyzes Brooks' argument rather than just attacking or defending it.

[^10]: D. L. Parnas, "Software Aspects of Strategic Defense Systems," Communications of the ACM, 28, 12 (December, 1985), pp. 1326-1335.

[^11]: A. M. Turski, Discussion of papers, Information Processing 1986, the Proceedings of the IFIP Tenth World Computing Conference, H.-J. Kugler, ed., Amsterdam: Elsevier Science, pp. 1077-1078.

[^12]: R. L. Glass, I. Vessey, and S. A. Conger, "Software Tasks: Intellectual or Clerical?" Information and Software Technology, 34, 4 (April, 1992), pp. 209-214.

[^13]: E. W. Pugh, Building IBM: Shaping an Industry and Its Technology, Cambridge: MIT Press (1995), pp. 182ff.

[^14]: H. H. Goldstine, The Computer from Pascal to Von Neumann, Princeton: Princeton University Press (1972), Ch. 7.

[^15]: S. Rosen, "Programming Systems and Languages: A Historical Survey," AFIPS Spring Joint Computer Conference, 25 (1964), pp. 1-15.

[^16]: D. D. McCracken, "The Mythology of Software Development," Datamation (December, 1973), pp. 65-70.

[^17]: T. F. Hughes, Rescuing Prometheus, New York: Pantheon (1998), pp. 15-68.

[^18]: D. Harel and E. Gery, "Executable Object Modeling with Statecharts," IEEE Computer, 30, 7 (July, 1997), pp. 31-42.

[^19]: T. C. Jones, Programming Productivity, New York: McGraw-Hill (1986); "The Limits of Programming Productivity," Guide and Share Application Development Symposium Proceedings, (1979), pp. 195-206.

[^20]: Coqui, correspondence to the author (1987).

[^21]: J. Coggins, correspondence to the author (1993).

[^22]: J. Coggins, correspondence to the author (1993).

[^23]: T. C. Jones, correspondence to the author (1987).

[^24]: W. Huang, correspondence to the author (1987).

[^25]: H. D. Mills, "Software Engineering Education," Proceedings of the IEEE, 68, 9 (September, 1980), pp. 1158-1162.

[^26]: D. Harel, "Biting the Silver Bullet—Toward a Brighter Future for System Development," Computer, 25, 1 (January, 1992), p. 10.

[^27]: B. Stroustrup, The C++ Programming Language, 3rd ed., Reading: Addison-Wesley (1997).

[^28]: R. M. Stallman, GNU Emacs Manual, 15th ed., Boston: Free Software Foundation (1999).

[^29]: B. W. Boehm, Software Engineering Economics, Englewood Cliffs: Prentice-Hall (1981), pp. 468-470.

[^30]: T. C. Jones, correspondence to the author (1987).

[^31]: H. D. Mills, "Top-Down Programming in Large Systems," in R. Ruskin, ed., Debugging Techniques in Large Systems, Englewood Cliffs: Prentice-Hall (1971).

[^32]: T. C. Jones, Programming Productivity, New York: McGraw-Hill (1986), Ch. 12.

[^33]: D. L. Parnas, letter to the author, December 28, 1994.

[^34]: J. S. Russell, Systematic Technical Education for the English People (1869).

[^35]: R. M. Pirsig, Zen and the Art of Motorcycle Maintenance: An Inquiry into Values, New York: Morrow (1974).

[^36]: B. W. Boehm, Software Engineering Economics, Englewood Cliffs: Prentice-Hall (1981), pp. 472-475.

[^37]: J. Coggins, correspondence to the author (1993).

[^38]: A. H. Maslow, Toward a Psychology of Being, 3rd ed., New York: Wiley (1998—first published 1962).
