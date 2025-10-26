# Chapter 17: "No Silver Bullet" Refired

> Every bullet has its billet.
> — WILLIAM III OF ENGLAND, PRINCE OF ORANGE

---

> Whoever thinks a faultless piece to see,
> Thinks what never was, nor is, nor ever shall be.
> — ALEXANDER POPE, AN ESSAY ON CRITICISM

*Assembling a structure from ready-made parts, 1945*
*The Bettman Archive*

---

## On Werewolves and Other Legendary Terrors

"No Silver Bullet—Essence and Accidents of Software Engineering" (now Chapter 16) was originally an invited paper for the
IFIP '86 conference in Dublin, and it was published in those proceedings.[^1] *Computer* magazine reprinted it, behind a gothic
cover, illustrated with stills from films such as *The Werewolf of
London*.[^2] They also provided an explanatory sidebar "To Slay the
Werewolf," setting forth the (modern) legend that only silver
bullets will do. I was not aware of the sidebar and illustrations
before publication, and I never expected a serious technical paper to be so embellished.

*Computer*'s editors were expert in achieving their desired effect, however, and many people seem to have read the paper. I
have therefore chosen yet another werewolf picture for that
chapter, an ancient depiction of an almost comical creature. I
hope this less garish picture will have the same salutary effect.

## There is Too a Silver Bullet—AND HERE IT IS

"No Silver Bullet" asserts and argues that no single software engineering development will produce an order-of-magnitude improvement in programming productivity within ten years (from
the paper's publication in 1986). We are now nine years into
that decade, so it is timely to see how this prediction is holding up.

Whereas *The Mythical Man-Month* generated many citations
but little argument, "No Silver Bullet" has occasioned rebuttal
papers, letters to journal editors, and letters and essays that continue to this day.[^3] Most of these attack the central argument that
there is no magical solution, and my clear opinion that there
cannot be one. Most agree with most of the arguments in
"NSB," but then go on to assert that there is indeed a silver bullet for the software beast, which the author has invented. As I
reread the early responses today, I can't help noticing that the
nostrums pushed so vigorously in 1986 and 1987 have not had
the dramatic effects claimed.

I buy hardware and software chiefly by the "happy user"
test—conversations with bona fide cash-paying customers who
use the product and are pleased. Likewise, I shall most readily
believe a silver bullet has materialized when a bona fide independent user steps forth and says, "I used this methodology, tool,
or product, and it gave me a tenfold improvement in software
productivity."

Many correspondents have made valid emendations or clarifications. Some have undertaken point-by-point analysis and
rebuttal, for which I am grateful. In this chapter, I shall share
the improvements and address the rebuttals.

## Obscure Writing Will Be Misunderstood

Some writers show that I failed to make some arguments clear.

**Accident.** The central argument of "NSB" is as clearly stated in
the Abstract to Chapter 16 as I know how to put it. Some have
been confused, however, by the terms *accident* and *accidental*,
which follow an ancient usage going back to Aristotle.[^4] By *accidental*, I did not mean occurring by chance, nor misfortunate, but
more nearly incidental, or appurtenant.

I would not denigrate the accidental parts of software construction; instead I follow the English dramatist, detective story
writer, and theologian Dorothy Sayers in seeing all creative activity to consist of (1) the formulation of the conceptual constructs, (2) implementation in real media, and (3) interactivity
with users in real uses.[^5] The part of software building I called
essence is the mental crafting of the conceptual construct; the
part I called accident is its implementation process.

**A question of fact.** It seems to me (although not to everyone)
that the truthfulness of the central argument boils down to a
question of fact: What fraction of total software effort is now associated with the accurate and orderly representation of the conceptual construct, and what fraction is the effort of mentally
crafting the constructs? The finding and fixing of flaws falls
partly in each fraction, according to whether the flaws are conceptual, such as failing to recognize some exception, or representational, such as a pointer mistake or a memory allocation
mistake.

It is my opinion, and that is all, that the accidental or representational part of the work is now down to about half or less
of the total. Since this fraction is a question of fact, its value
could in principle be settled by measurement.[^6] Failing that, my
estimate of it can be corrected by better informed and more current estimates. Significantly, no one who has written publicly or
privately has asserted that the accidental part is as large as 9/10.

"NSB" argues, indisputably, that if the accidental part of the
work is less than 9/10 of the total, shrinking it to zero (which
would take magic) will not give an order of magnitude productivity improvement. One must attack the essence.

Since "NSB," Bruce Blum has drawn my attention to the
1959 work of Herzberg, Mausner, and Sayderman.[^7] They find
that motivational factors can increase productivity. On the other
hand, environmental and accidental factors, no matter how positive, cannot; but these factors can decrease productivity when
negative. "NSB" argues that much software progress has been
the removal of such negative factors: stunningly awkward machine languages, batch processing with long turnaround times,
poor tools, and severe memory constraints.

**Are the essential difficulties therefore hopeless?** An excellent
1990 paper by Brad Cox, "There Is a Silver Bullet," argues eloquently for the reusable, interchangeable component approach
as an attack on the conceptual essence of the problem.[^8] I enthusiastically agree.

Cox however misunderstands "NSB" on two points. First,
he reads it as asserting that software difficulties arise "from
some deficiency in how programmers build software today."
My argument was that the essential difficulties are inherent in
the conceptual complexity of the software functions to be designed and built at any time, by any method. Second, he (and
others) read "NSB" as asserting that there is no hope of attacking the essential difficulties of software building. That was not
my intent. Crafting the conceptual construct does indeed have
as inherent difficulties complexity, conformity, changeability,
and invisibility. The troubles caused by each of these difficulties
can, however, be ameliorated.

**Complexity is by levels.** For example, complexity is the most
serious inherent difficulty, but not all complexity is inevitable.
Much, but not all, of the conceptual complexity in our software
constructs comes from the arbitrary complexity of the applications themselves. Indeed, Lars Sødahl of MYSIGMA Sødahl and
Partners, a multinational management consulting firm, writes:

> In my experience most of the complexities which are encountered in
> systems work are symptoms of organizational malfunctions. Trying
> to model this reality with equally complex programs is actually to
> conserve the mess instead of solving the problems.

Steve Lukasik of Northrop argues that even organizational
complexity is perhaps not arbitrary but may be susceptible to ordering principles:

> I trained as a physicist and thus see "complex" things as susceptible
> to description in terms of simpler concepts. Now you may be right;
> I will not assert that all complex things are susceptible to ordering
> principles. ... by the same rules of argument you cannot assert
> that they can not be.
>
> ... Yesterday's complexity is tomorrow's order. The complexity of
> molecular disorder gave way to the kinetic theory of gases and the
> three laws of thermodynamics. Now software may not ever reveal
> those kinds of ordering principles, but the burden is on you to explain why not. I am not being obtuse or argumentative. I believe
> that someday the "complexity" of software will be understood in
> terms of some higher order notions (invariants to the physicist).

I have not undertaken the deeper analysis Lukasik properly
calls for. As a discipline, we need an extended information theory that quantifies the information content of static structures,
just as Shannon's theory does for communicated streams. That
is quite beyond me. To Lukasik I simply respond that system
complexity is a function of myriad details that must each be
specified exactly, either by some general rule or detail-by-detail,
but not just statistically. It seems very unlikely that uncoordinated works of many minds should have enough coherence to
be exactly described by general rules.

Much of the complexity in a software construct is, however,
not due to conformity to the external world but rather to the implementation itself—its data structures, its algorithms, its connectivity. Growing software in higher-level chunks, built by
someone else or reused from one's own past, avoids facing
whole layers of complexity. "NSB" advocates a wholehearted attack on the problem of complexity, quite optimistic that progress
can be made. It advocates adding necessary complexity to a software system:

- Hierarchically, by layered modules or objects
- Incrementally, so that the system always works.

## Harel's Analysis

David Harel, in the 1992 paper, "Biting the Silver Bullet," undertakes the most careful analysis of "NSB" that has been published.[^9]

**Pessimism vs. optimism vs. realism.** Harel sees both "NSB"
and Parnas's 1984 "Software Aspects of Strategic Defense Systems,"[^10] as "far too bleak." So he aims to illuminate the brighter
side of the coin, subtitling his paper "Toward a Brighter Future
for System Development." Cox as well as Harel reads "NSB" as
pessimistic, and he says, "But if you view these same facts from
a new perspective, a more optimistic conclusion emerges." Both
misread the tone.

First, my wife, my colleagues, and my editors find me to err
far more often in optimism than in pessimism. I am, after all, a
programmer by background, and optimism is an occupational
disease of our craft.

"NSB" says explicitly "As we look to the horizon of a decade
hence, we see no silver bullet. ... Skepticism is not pessimism,
however. ... There is no royal road, but there is a road." It
forecasts that the innovations under way in 1986, if developed
and exploited, would together indeed achieve an order-of-magnitude improvement in productivity. As the 1986-1996 decade
proceeds, this prediction appears, if anything, too optimistic
rather than too gloomy.

Even if "NSB" were universally seen as pessimistic, what is
wrong with that? Is Einstein's statement that nothing can travel
faster than the speed of light "bleak" or "gloomy?" How about
Gödel's result that some things cannot be computed? "NSB" undertakes to establish that "the very nature of software makes
it unlikely that there will ever be any silver bullets." Turski, in
his excellent response paper at the IFIP Conference, said eloquently:

> Of all misguided scientific endeavours, none are more pathetic than
> the search for the philosophers' stone, a substance supposed to
> change base metals into gold. The supreme object of alchemy, ardently pursued by generations of researchers generously funded by
> secular and spiritual rulers, is an undiluted extract of wishful
> thinking, of the common assumption that things are as we would
> like them to be. It is a very human belief. It takes a lot of effort to
> accept the existence of insoluble problems. The wish to see a way
> out, against all odds, even when it is proven that it does not exist,
> is very, very strong. And most of us have a lot of sympathy for
> these courageous souls who try to achieve the impossible. And so
> it continues. Dissertations on squaring a circle are being written.
> Lotions to restore lost hair are concocted and sell well. Methods to improve software productivity are hatched and sell very
> well.
>
> All too often we are inclined to follow our own optimism (or exploit
> the optimistic hopes of our sponsors). All too often we are willing
> to disregard the voice of reason and heed the siren calls of panacea
> pushers.[^11]

Turski and I both insist that pipe-dreaming inhibits forward progress and wastes effort.

**"Gloom" themes.** Harel perceives gloom in "NSB" to arise
from three themes:

- Sharp separation into essence and accident
- Treatment of each silver bullet candidate in isolation
- Predicting for only 10 years, instead of a long enough time
  in which "to expect any significant improvement."

As to the first, that is the whole point of the paper. I still
believe this separation is absolutely central to understanding
why software is hard. It is a sure guide as to what kinds of attacks to make.

As to treating candidate bullets in isolation, "NSB" does so
indeed. The various candidates have been proposed one by one,
with extravagant claims for each one by itself. It is fair to assess
them one by one. It is not the techniques I oppose, it is expecting them to work magic. Glass, Vessey, and Conger in their 1992
paper offer ample evidence that the vain search for a silver bullet
has not yet ended.[^12]

As to choosing 10 years versus 40 years as a prediction period, the shorter period was in part a concession that our predictive powers have never been good beyond a decade. Which
of us in 1975 predicted the microcomputer revolution of the
1980s?

There are other reasons for the decade limit: the claims
made for candidate bullets all have had a certain immediacy
about them. I recollect none that said "Invest in my nostrum,
and you will start winning after 10 years." Moreover, hardware
performance/price ratios have improved by perhaps a hundredfold per decade, and the comparison, though quite invalid, is
subconsciously inevitable. We will surely make substantial progress over the next 40 years; an order of magnitude over 40 years
is hardly magical.

**Harel's thought experiment.** Harel proposes a thought experiment in which he postulates "NSB" as having been written in
1952, instead of 1986, but asserting the same propositions. This
he uses as a *reductio ad absurdum* to argue against attempting to
separate essence from accident.

The argument doesn't work. First, "NSB" begins by asserting that the accidental difficulties grossly dominated the essential ones in 1950s programming, that they no longer do so, and
that eliminating them has effected orders-of-magnitude improvements. Translating that argument back 40 years is unreasonable; one can hardly imagine asserting in 1952 that the
accidental difficulties do not occasion a major part of the effort.

Second, the state of affairs Harel imagines to have prevailed
in the 1950s is inaccurate:

> That was the time when instead of grappling with the design of
> large, complex systems, programmers were in the business of developing conventional one-person programs (which would be on the
> order of 100—200 lines in a modern programming language) that
> were to carry out limited algorithmic tasks. Given the technology
> and methodology available then, such tasks were similarly formidable. Failures, errors, and missed deadlines were all around.

He then describes how the postulated failures, errors, and
missed deadlines in the conventional little one-person programs
were improved by an order of magnitude over the next 25 years.

But the state of the art in the 1950s was not in fact small one-person programs. In 1952, the Univac was at work processing
the 1950 census with a complex program developed by about
eight programmers.[^13] Other machines were doing chemical dynamics, neutron diffusion calculations, missile performance
calculations, etc.[^14] Assemblers, relocating linkers and loaders,
floating-point interpretive systems, etc. were in routine use.[^15]
By 1955 people were building 50 to 100 person-year business programs.[^16] By 1956 General Electric had in operation a payroll system in its Louisville appliance plant with more than 80,000
words of program. By 1957, the SAGE AN/FSQ/7 air defense
computer had been running two years, and a 75,000 instruction
communications-based, fail-safe-duplexed real-time system was
in operation in 30 sites.[^17] One can hardly maintain that it is evolution of techniques for one-person programs that chiefly describes software engineering efforts since 1952.

**AND HERE IT IS.** Harel goes on to offer his own silver bullet,
a modeling technique called "The Vanilla Framework." The approach itself is not described in enough detail for evaluation, but
reference is given to a paper, and to a technical report to appear
in book form in due time.[^18] Modeling does address the essence,
the proper crafting and debugging of concepts, so it is possible
that the Vanilla Framework will be revolutionary. I hope so. Ken
Brooks reports he found it a helpful methodology when he tried
it for a real task.

**Invisibility.** Harel argues strongly that much of the conceptual
construct of software is inherently topological in nature and
these relationships have natural counterparts in spatial/graphical representations:

> Using appropriate visual formalisms can have a spectacular effect
> on engineers and programmers. Moreover, this effect is not limited
> to mere accidental issues; the quality and expedition of their very
> thinking was found to be improved. Successful system development in the future will revolve around visual representations. We
> will first conceptualize, using the "proper" entities and relationships, and then formulate and reformulate our conceptions as a series of increasingly more comprehensive models represented in an
> appropriate combination of visual languages. A combination it
> must be, since system models have several facets, each of which conjures up different kinds of mental images.
>
> ... Some aspects of the modeling process have not been as forthcoming as others in lending themselves to good visualization. Algorithmic operations on variables and data structures, for example,
> will probably remain textual.

Harel and I are quite close. What I argued is that software structure is not embedded in three-space, so there is no natural single
mapping from a conceptual design to a diagram, whether in two
dimensions or more. He concedes, and I agree, that one needs
multiple diagrams, each covering some distinct aspect, and that
some aspects don't diagram well at all.

I completely share his enthusiasm for using diagrams as
thought and design aids. I have long enjoyed asking candidate
programmers, "Where is next November?" If the question is too
cryptic, then, "Tell me about your mental model of the calendar." The really good programmers have strong spatial senses;
they usually have geometric models of time; and they quite
often understand the first question without elaboration. They
have highly individualistic models.

## Jones's Point—Productivity Follows Quality

Capers Jones, writing first in a series of memoranda and later in
a book, offers a penetrating insight, which has been stated by
several of my correspondents. "NSB," like most writings at the
time, was focused on productivity, the software output per unit
of input. Jones says, "No. Focus on quality, and productivity will
follow."[^19] He argues that costly and late projects invest most of
the extra work and time in finding and repairing errors in specification, in design, in implementation. He offers data that show
a strong correlation between lack of systematic quality controls
and schedule disasters. I believe it. Boehm points out that productivity drops again as one pursues extreme quality, as in
IBM's space-shuttle software.

Coqui similarly argues that systematic software development disciplines were developed in response to quality concerns
(especially avoidance of major disasters) rather than productivity concerns.

> But note: the goal of applying Engineering principles to Software
> production in the 1970s was to increase the Quality, Testability,
> Stability, and Predictability of software products—not necessarily
> the efficiency of Software production.
>
> The driving force to use Software Engineering principles in software production was the fear of major accidents that might be
> caused by having uncontrollable artists responsible for the development of ever more complex systems.[^20]

## So What Has Happened to Productivity?

**Productivity numbers.** Productivity numbers are very hard to
define, hard to calibrate, and hard to find. Capers Jones believes
that for two equivalent COBOL programs written 10 years
apart, one without structured methodology and one with, the
gain is a factor of three.

Ed Yourdon says, "I see people getting a fivefold improvement due to workstations and software tools." Tom DeMarco
believes "Your expectation of an order-of-magnitude improvement in 10 years, due to the whole basket of techniques, was
optimistic. I haven't seen organizations making an order-of-magnitude improvement."

**Shrink-wrapped software—Buy; don't build.** One 1986 assessment in "NSB" has, I think, proved to be correct: "The development of the mass market is ... the most profound long-run
trend in software engineering." From the discipline's viewpoint,
the mass-market software is almost a new industry compared to
that of the development of custom software, whether in-house
or out-house. When packages sell in the millions—or even the
thousands—quality, timeliness, product performance, and support cost become dominant issues, rather than the development
cost that is so crucial for custom software.

**Power tools for the mind.** The most dramatic way to improve
the productivity of management information systems (MIS) programmers is to go down to your local computer store and buy
off the shelf what they would have built. This is not ridiculous;
the availability of cheap, powerful shrink-wrapped software has
met many needs that formerly would have occasioned custom
packages. These power tools for the mind are more like electric
drills, saws, and sanders than they are like big complex production tools. The integration of these into compatible and cross-linked sets such as Microsoft Works and the better-integrated
ClarisWorks give immense flexibility. And like the homeowner's
collection of power hand tools, frequent use of a small set, for
many different tasks, develops familiarity. Such tools must emphasize ease of use for the casual user, not the professional.

Ivan Selin, Chairman of American Management Systems,
Inc., wrote me in 1987:

> I quibble with your statement that packages have not really changed
> that much. ...: I think you too lightly throw off the major implications of your observation that, [the software packages] "may be
> somewhat more generalized and somewhat more customizable than
> formerly, but not much." Even accepting this statement at face
> value, I believe that the users see the packages as being both more
> generalized and easier to customize, and that this perception leads
> the users to be much more amenable to packages. In most cases that
> my company finds, it is the [end] users, not the software people,
> who are reluctant to use packages because they think they will lose
> essential features or functions, and hence the prospect of easy customization is a big selling point to them.

I think Selin is quite right—I underestimated both the degree of
package customizability and its importance.

## Object-Oriented Programming—Will a Brass Bullet Do?

**Building with bigger pieces.** The illustration opening this
chapter reminds us that if one assembles a set of pieces, each of
which may be complex, and all of which are designed to have
smooth interfaces, quite rich structures go together rapidly.

One view of object-oriented programming is that it is a discipline that enforces modularity and clean interfaces. A second
view emphasizes encapsulation, the fact that one cannot see,
much less design, the inner structure of the pieces. Another
view emphasizes inheritance, with its concomitant hierarchical
structure of classes, with virtual functions. Yet another view emphasizes strong abstract data-typing, with its assurance that a particular data-type will be manipulated only by operations proper
to it.

Now any of these disciplines can be had without taking the
whole Smalltalk or C++ package—many of them predated object-oriented technology. The attractiveness of object-oriented
approach is that of a multivitamin pill: in one fell swoop (that is,
programmer retraining), one gets them all. It is a very promising
concept.

**Why has object-oriented technique grown slowly?** In the nine
years since "NSB," the expectancy has steadily grown. Why has
growth been slow? Theories abound. James Coggins, author for
four years of the column, "The Best of comp.lang.c++" in *The
C++ Report*, offers this explanation:

> The problem is that programmers in O-O have been experimenting
> in incestuous applications and aiming low in abstraction, instead
> of high. For example, they have been building classes such as
> linked-list or set instead of classes such as user-interface or radiation beam or finite-element model. Unfortunately the self-same strong type-checking in C++ that helps programmers to
> avoid errors also makes it hard to build big things out of little
> ones.[^21]

He goes back to the basic software problem, and argues that one
way to address unmet software needs is to increase the size of
the intelligent workforce by enabling and coopting our clients.
This argues for top-down design:

> If we design large-grained classes that address concepts our clients
> are already working with, they can understand and question the
> design as it grows, and they can cooperate in the design of test
> cases. My ophthalmology collaborators don't care about stacks; they
> do care about Legendre polynomial shape descriptions of corneas.
> Small encapsulations yield small benefits.

David Parnas, whose paper was one of the origins of object-oriented concepts, sees the matter differently. He writes me:

> The answer is simple. It is because [O-O] has been tied to a variety
> of complex languages. Instead of teaching people that O-O is a type
> of design, and giving them design principles, people have taught
> that O-O is the use of a particular tool. We can write good or bad
> programs with any tool. Unless we teach people how to design, the
> languages matter very little. The result is that people do bad designs with these languages and get very little value from them. If
> the value is small, it won't catch on.

**Front-loaded costs, down-stream benefits.** My own belief is
that object-oriented techniques have a peculiarly severe case of
a malady that characterizes many methodological improvements. The up-front costs are very substantial—primarily retraining programmers to think in a quite new way, but also extra
investment in fashioning functions into generalized classes. The
benefits, which I think are real and not merely putative, occur
all along the development cycle; but the big benefits pay off during successor building, extension, and maintenance activities.
Coggins says, "Object-oriented techniques will not make the
first project development any faster, or the next one. The fifth
one in that family will go blazingly fast."[^22]

Betting real up-front money for the sake of projected but iffy
benefits later is what investors do every day. In many programming organizations, however, it requires real managerial courage, a commodity much scarcer than technical competence or
administrative proficiency. I believe the extreme degree of cost
front-loading and benefit back-loading is the largest single factor
slowing the adoption of O-O techniques. Even so, C++ seems
to be steadily replacing C in many communities.

## What About Reuse?

The best way to attack the essence of building software is not to
build it at all. Package software is only one of the ways of doing
this. Program reuse is another. Indeed, the promise of easy
reuse of classes, with easy customization via inheritance, is one
of the strongest attractions of object-oriented techniques.

As is so often the case, as one gets some experience with a
new way of doing business the new mode is not so simple as
first appears.

Of course, programmers have always reused their own handiwork. Jones says,

> Most experienced programmers have private libraries which allow
> them to develop software with about 30% reused code by volume.
> Reusability at the corporate level aims for 75% reused code by volume, and requires special library and administrative support. Corporate reusable code also implies changes in project accounting and
> measurement practices to give credit for reusability.[^23]

W. Huang proposed organizing software factories with a matrix
management of functional specialists, so as to harness the natural propensity of each to reuse their own code.[^24]

Van Snyder of JPL points out to me that the mathematical
software community has a long tradition of reusing software:

> We conjecture that barriers to reuse are not on the producer side,
> but on the consumer side. If a software engineer, a potential consumer of standardized software components, perceives it to be more
> expensive to find a component that meets their need, and so verify,
> than to write one anew, a new, duplicative component will be written. Notice we said perceives above. It doesn't matter what the true
> cost of reconstruction is.
>
> Reuse has been successful for mathematical software for two reasons: (1) It is arcane, requiring an enormous intellectual input per
> line of code; and (2) there is a rich and standard nomenclature,
> namely mathematics, to describe the functionality of each component. Thus the cost to reconstruct a component of mathematical
> software is high, and the cost to discover the functionality of an
> existing component is low. The long tradition of professional journals publishing and collecting algorithms, and offering them at
> modest cost, and commercial concerns offering very high quality
> algorithms at somewhat higher but still modest cost, makes discovering a component that meets one's need simpler than in many
> other disciplines, where it is sometimes not possible to specify one's
> need precisely and tersely. These factors collaborate to make it more
> attractive to reuse rather than to reinvent mathematical software.

The same reuse phenomenon is found among several communities, such as those that build codes for nuclear reactors, climate models, and ocean models, and for the same reasons. The
communities each grew up with the same textbooks and standard notations.

**How does corporate-level reuse fare today?** Lots of study; relatively little practice in the United States; anecdotal reports of
more reuse abroad.[^25]

Jones reports that all of his firm's clients with over 5000 programmers have formal reuse research, whereas fewer than 10
percent of the clients with under 500 programmers do.[^26] He reports that in industries with the greatest reuse potential, reusability research (not deployment) "is active and energetic, even
if not yet totally successful." Ed Yourdon reports a software
house in Manila that has 50 of its 200 programmers building
only reusable modules for the rest to use; "I've seen a few
cases—adoption is due to organizational factors such as the reward structure, not technical factors."

DeMarco tells me that the availability of mass-market packages and their suitability as providers of generic functions such
as database systems has substantially reduced both the pressure
and the marginal utility of reusing modules of one's application
code. "The reusable modules tended to be the generic functions
anyway."

Parnas writes,

> Reuse is something that is far easier to say than to do. Doing it
> requires both good design and very good documentation. Even
> when we see good design, which is still infrequently, we won't see
> the components reused without good documentation.

Ken Brooks comments on the difficulty of anticipating which
generalization will prove necessary: "I keep having to bend
things even on the fifth use of my own personal user-interface
library."

Real reuse seems to be just beginning. Jones reports that a
few reusable code modules are being offered on the open market at prices between 1 percent and 20 percent of the normal development costs.[^27] DeMarco says,

> I am becoming very discouraged about the whole reuse phenomenon. There is almost a total absence of an existence theorem for
> reuse. Time has confirmed that there is a big expense in making
> things reusable.

Yourdon estimates the big expense: "A good rule of thumb
is that such reusable components will take twice the effort of a
'one-shot' component."[^28] I see that expense as exactly the effort
of productizing the component, discussed in Chapter 1. So my
estimate of the effort ratio would be threefold.

Clearly we are seeing many forms and varieties of reuse, but
not nearly so much of it as we had expected by now. There is
still a lot to learn.

## Learning Large Vocabularies—A Predictable but Unpredicted Problem for Software Reuse

The higher the level at which one thinks, the more numerous
the primitive thought-elements one has to deal with. So programming languages are much more complex than machine
languages, and natural languages are more complex still.
Higher-level languages have larger vocabularies, more complex
syntax, and richer semantics.

As a discipline, we have not pondered the implications of
this fact for program reuse. To improve quality and productivity,
we want to build programs by composing chunks of debugged
function that are substantially higher than statements in programming languages. Therefore, whether we do this by object
class libraries or procedure libraries, we must face the fact that
we are radically raising the sizes of our programming vocabularies. Vocabulary learning constitutes no small part of the intellectual barrier to reuse.

So today people have class libraries with over 3000 members. Many objects require specification of 10 to 20 parameters
and option variables. Anyone programming with that library
must learn the syntax (the external interfaces) and the semantics
(the detailed functional behavior) of its members if they are to
achieve all of the potential reuse.

This task is far from hopeless. Native speakers routinely use
vocabularies of over 10,000 words, educated people far more.
Somehow we learn the syntax and very subtle semantics. We
correctly differentiate among giant, huge, vast, enormous, mammoth; people just do not speak of mammoth deserts or vast elephants.

We need research to appropriate for the software reuse
problem the large body of knowledge as to how people acquire
language. Some of the lessons are immediately obvious:

- People learn in sentence contexts, so we need to publish
  many examples of composed products, not just libraries of
  parts.
- People do not memorize anything but spelling. They learn
  syntax and semantics incrementally, in context, by use.
  People group word composition rules by syntactic classes,
  not by compatible subsets of objects.

## Net on Bullets—Position Unchanged

So we come back to fundamentals. Complexity is the business
we are in, and complexity is what limits us. R. L. Glass, writing
in 1988, accurately summarizes my 1995 views:

> So what, in retrospect, have Parnas and Brooks said to us? That
> software development is a conceptually tough business. That magic
> solutions are not just around the corner. That it is time for the practitioner to examine evolutionary improvements rather than to
> wait—or hope—for revolutionary ones.
>
> Some in the software field find this to be a discouraging picture.
> They are the ones who still thought breakthroughs were near at
> hand.
>
> But some of us—those of us crusty enough to think that we are
> realists—see this as a breath of fresh air. At last, we can focus on
> something a little more viable than pie in the sky. Now, perhaps,
> we can get on with the incremental improvements to software productivity that are possible, rather than waiting for the breakthroughs that are not likely to ever come.[^29]

---

[^1]: F. P. Brooks, Jr., "No silver bullet—essence and accidents of software engineering," *Information Processing 1986*, the Proceedings of the IFIP Tenth World Computing Conference, H.-J. Kugler, ed., pp. 1069-1076.

[^2]: *Computer*, April, 1987.

[^3]: See the bibliography.

[^4]: Aristotle, *Metaphysics*, Bk. V, Ch. 30.

[^5]: D. L. Sayers, *The Mind of the Maker*. London: Methuen, 1941.

[^6]: D. N. Card's paper, "Understanding process improvement," *IEEE Software*, July, 1991, suggests ways to do this.

[^7]: F. Herzberg, B. Mausner, and B. Snyderman, *The Motivation to Work*. New York: John Wiley, 1959.

[^8]: B. Cox, "There is a silver bullet," *Byte*, Oct., 1990, pp. 209-218.

[^9]: D. Harel, "Biting the silver bullet," *Computer*, Jan., 1992, pp. 8-20.

[^10]: D. L. Parnas, "Software aspects of strategic defense systems," *American Scientist*, Nov., 1985.

[^11]: W. M. Turski, "And no philosophers' stone, either," *Information Processing 1986*, op. cit., pp. 1077-1080.

[^12]: R. L. Glass, I. Vessey, and S. A. Conger, "Software tasks: Intellectual or clerical?" *Information and Software Technology*, 34, 4 (April, 1992), pp. 209-214.

[^13]: H. H. Goldstine, *The Computer from Pascal to von Neumann*. Princeton, N.J.: Princeton University Press, 1972, p. 321.

[^14]: Ibid., Ch. 7.

[^15]: M. V. Wilkes, D. J. Wheeler, and S. Gill, *Preparation of Programs for an Electronic Digital Computer*. Cambridge, Mass.: Addison-Wesley, 1951.

[^16]: W. Bemer, private communication.

[^17]: G. E. Valley, Jr., "How the SAGE development began," *Annals of the History of Computing*, 7, 3 (July, 1985), pp. 196-226.

[^18]: D. Harel, H. Lachover, A. Naamad, A. Pnueli, M. Politi, R. Sherman, and A. Shtul-Trauring, "STATEMATE: A working environment for the development of complex reactive systems," *IEEE Trans. Soft. Eng.*, 16, 4 (April, 1990), pp. 403-414; D. Harel and E. Gery, "Executable object modeling with Statecharts," *IEEE Computer*, July, 1997, pp. 31-42.

[^19]: C. Jones, private correspondence.

[^20]: A. Coqui, private correspondence.

[^21]: J. Coggins, private communication.

[^22]: Ibid.

[^23]: C. Jones, private communication.

[^24]: W. Huang, "A software factory methodology based on reusability," in *Approches par objets dans les bases de données et les languages de programmation*, C. Chrisment, ed., Paris: INRIA, 1990, pp. 125-144.

[^25]: C. Jones, private communication; W. B. Frakes and B. A. Nejmeh, "Software reuse through information retrieval," *Proc. 20th Hawaii Int. Conf. on Systems Sciences*, Kona, Hawaii, Jan., 1987.

[^26]: C. Jones, private communication.

[^27]: Ibid.

[^28]: E. Yourdon, private communication.

[^29]: R. L. Glass, "The realities of software technology payoffs," *Comm. ACM*, 31, 2 (Feb., 1988), p. 102.
