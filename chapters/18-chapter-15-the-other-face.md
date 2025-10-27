# Chapter 15: The Other Face

> What we do not understand we do not possess.
> — GOETHE

---

> O give me commentators plain,
> Who with no deep researches vex the brain.
> — CRABBE

*A reconstruction of Stonehenge, the world's largest undocumented computer.*
*The Bettman Archive*

---

A computer program is a message from a person to a machine. The
rigidly marshaled syntax and the scrupulous definitions all exist
to make intention clear to the dumb engine.

But a written program has another face, that which tells its
story to the human user. For even the most private of programs,
some such communication is necessary; memory will fail the author-user, and they will require refreshing on the details of their
handiwork.

How much more vital is the documentation for a public program, whose user is remote from the author in both time and
space! For the program product, the other face to the user is fully
as important as the face to the machine.

Most of us have quietly excoriated the remote and anonymous
author of some skimpily documented program. And many of us
have therefore tried to instill in new programmers an attitude
about documentation that would inspire for a lifetime, overcoming sloth and schedule pressure. By and large we have failed. I
think we have used wrong methods.

Thomas J. Watson, Sr. told the story of his first experience as
a cash register salesperson in upstate New York. Charged with enthusiasm, he sallied out with his wagon loaded with cash registers.
He worked his territory diligently but without selling a one.
Downcast, he reported to his boss. The sales manager listened a
while, then said, "Help me load some registers into the wagon,
harness the horse, and let's go again." They did, and the two called
on customer after customer, with the older man showing how to sell
cash registers. All evidence indicates that the lesson took.

For several years I diligently lectured my software engineering
class on the necessity and propriety of good documentation, exhorting them ever more fervently and eloquently. It didn't work.
I assumed they had learned how to document properly and were
failing from lack of zeal. Then I tried loading some cash registers
into the wagon; i.e., showing them how the job is done. This has
been much more successful. So the remainder of this essay will
downplay exhortation and concentrate on the "how" of good
documentation.

## What Documentation Is Required?

Different levels of documentation are required for the casual user
of a program, for the user who must depend upon a program, and
for the user who must adapt a program for changes in circumstance or purpose.

**To use a program.** Every user needs a prose description of the
program. Most documentation fails in giving too little overview.
The trees are described, the bark and leaves are commented, but
there is no map of the forest. To write a useful prose description,
stand way back and come in slowly:

1. **Purpose.** What is the main function, the reason for the program?
2. **Environment.** On what machines, hardware configurations,
   and operating system configurations will it run?
3. **Domain and range.** What domain of input is valid? What range
   of output can legitimately appear?
4. **Functions realized and algorithms used.** Precisely what does it do?
5. **Input-output formats,** precise and complete.
6. **Operating instructions,** including normal and abnormal ending
   behavior, as seen at the console and on the outputs.
7. **Options.** What choices does the user have about functions?
   Exactly how are those choices specified?
8. **Running time.** How long does it take to do a problem of specified size on a specified configuration?
9. **Accuracy and checking.** How precise are the answers expected
   to be? What means of checking accuracy are incorporated?

Often all this information can be set forth in three or four
pages. That requires close attention to conciseness and precision.
Most of this document needs to be drafted before the program is
written, for it embodies basic planning decisions.

**To believe a program.** The description of how it is used must be
supplemented with some description of how one knows it is working. This means test cases.

Every copy of a program shipped should include some small
test cases that can be routinely used to reassure the user that they
have a faithful copy, accurately loaded into the machine.

Then one needs more thorough test cases, which are normally
run only after a program is modified. These fall into three parts of
the input data domain:

1. **Mainline cases** that test the program's chief functions for commonly encountered data.
2. **Barely legitimate cases** that probe the edge of the input data
   domain, ensuring that largest possible values, smallest possible values, and all kinds of valid exceptions work.
3. **Barely illegitimate cases** that probe the domain boundary from
   the other side, ensuring that invalid inputs raise proper diagnostic messages.

**To modify a program.** Adapting a program or fixing it requires
considerably more information. Of course the full detail is required, and that is contained in a well-commented listing. For the
modifier, as well as the more casual user, the crying need is for a
clear, sharp overview, this time of the internal structure. What are
the components of such an overview?

1. A flow chart or subprogram structure graph. More on this
   later.
2. Complete descriptions of the algorithms used, or else references to such descriptions in the literature.
3. An explanation of the layout of all files used.
4. An overview of the pass structure—the sequence in which
   data or programs are brought from tape or disk—and what is
   accomplished on each pass.
5. A discussion of modifications contemplated in the original
   design, the nature and location of hooks and exits, and discursive discussion of the ideas of the original author about what
   modifications might be desirable and how one might proceed.
   Their observations on hidden pitfalls are also useful.

## The Flow-Chart Curse

The flow chart is a most thoroughly oversold piece of program
documentation. Many programs don't need flow charts at all; few
programs need more than a one-page flow chart.

Flow charts show the decision structure of a program, which
is only one aspect of its structure. They show decision structure
rather elegantly when the flow chart is on one page, but the overview breaks down badly when one has multiple pages, sewed
together with numbered exits and connectors.

The one-page flow chart for a substantial program becomes
essentially a diagram of program structure, and of phases or steps.
As such it is very handy. Figure 15.1 shows such a subprogram
structure graph.

```text
                        MAIN PROGRAM
                             |
        ┌────────────────────┼────────────────────┐
        |                    |                    |
    INITIALIZE           PROCESS              FINALIZE
        |                    |                    |
        |          ┌─────────┼─────────┐          |
        |          |         |         |          |
        |       READ      COMPUTE   WRITE         |
        |          |         |         |          |
        |          |    ┌────┼────┐    |          |
        |          |    |    |    |    |          |
        |          | VALIDATE | FORMAT  |          |
        |          |    |    |    |    |          |
```

Fig. 15.1: A program structure graph. (Courtesy of W. V. Wright)

Of course such a structure graph neither follows nor needs the
painfully wrought ANSI flow-charting standards. All the rules on
box shapes, connectors, numbering, etc. are needed only to give
intelligibility to detailed flow charts.

The detailed blow-by-blow flow chart, however, is an obsolete nuisance, suitable only for initiating beginners into algorithmic thinking. When introduced by Goldstine and von Neumann,[^1]
the little boxes and their contents served as a high-level language,
grouping the inscrutable machine-language statements into clusters of significance. As Iverson early recognized,[^2] in a systematic
high-level language the clustering is already done, and each box
contains a statement (Fig. 15.2). Then the boxes themselves
become no more than a tedious and space-hogging exercise in
drafting; they might as well be eliminated. Then nothing is left but
the arrows. The arrows joining a statement to its successor are
redundant; erase them. That leaves only GO TO's. And if one
follows good practice and uses block structure to minimize GO
TO's, there aren't many arrows, but they aid comprehension immensely. One might as well draw them on the listing and eliminate
the flow chart altogether.

In fact, flow charting is more preached than practiced. I have
never seen an experienced programmer who routinely made detailed flow charts before beginning to write programs. Where organization standards require flow charts, these are almost
invariably done after the fact. Many shops proudly use machine
programs to generate this "indispensable design tool" from the
completed code. I think this universal experience is not an embarrassing and deplorable departure from good practice, to be acknowledged only with a nervous laugh. Instead it is the
application of good judgment, and it teaches us something about
the utility of flow charts.

The Apostle Peter said of new Gentile converts and the Jewish
law, "Why lay a load on [their] backs which neither our ancestors
nor we ourselves were able to carry?" (Acts 15:10, TEV). I would
say the same about new programmers and the obsolete practice of
flow charting.

## Self-Documenting Programs

A basic principle of data processing teaches the folly of trying to
maintain independent files in synchronism. It is far better to combine them into one file with each record containing all the information both files held concerning a given key.

Yet our practice in programming documentation violates
our own teaching. We typically attempt to maintain a machine-readable form of a program and an independent set of human-readable documentation, consisting of prose and flow charts.

The results in fact confirm our teachings about the folly of
separate files. Program documentation is notoriously poor, and its
maintenance is worse. Changes made in the program do not
promptly, accurately, and invariably appear in the paper.

The solution, I think, is to merge the files, to incorporate the
documentation in the source program. This is at once a powerful
incentive toward proper maintenance, and an insurance that the
documentation will always be handy to the program user. Such
programs are called self-documenting.

Now clearly this is awkward (but not impossible) if flow
charts are to be included. But grant the obsolescence of flow charts
and the dominant use of high-level language, and it becomes
reasonable to combine the program and the documentation.

The use of a source program as a documentation medium
imposes some constraints. On the other hand, the intimate availability of the source program, line by line, to the reader of the
documentation makes possible new techniques. The time has
come to devise radically new approaches and methods for program
documentation.

As a principal objective, we must attempt to minimize the
burden of documentation, the burden neither we nor our predecessors have been able to bear successfully.

**An approach.** The first notion is to use the parts of the program
that have to be there anyway, for programming language reasons,
to carry as much of the documentation as possible. So labels,
declaration statements, and symbolic names are all harnessed to
the task of conveying as much meaning as possible to the reader.

A second notion is to use space and format as much as possible
to improve readability and show subordination and nesting.

The third notion is to insert the necessary prose documentation into the program as paragraphs of comment. Most programs
tend to have enough line-by-line comments; those programs produced to meet stiff organizational standards for "good documentation" often have too many. Even these programs, however, are
usually deficient in the paragraph comments that really give intelligibility and overview to the whole thing.

Since the documentation is built into the structure, naming,
and formats of the program, much of it must be done when the
program is first written. But that is when it should be written. Since
the self-documentation approach minimizes extra work, there are
fewer obstacles to doing it then.

**Some techniques.** Figure 15.3 shows a self-documenting PL/I
program.[^3] The numbers in the circles are not part of it; they are
meta-documentation keyed to the discussion.

1. Use a separate job name for each run, and maintain a run log
   showing what was tried, when, and the results. If the name is
   composed of a mnemonic part (here QLT) and a numerical
   suffix (here 4), the suffix can be used as a run number, tying
   listings and log together. This technique requires a new job
   card for each run, but they can be made up in batches, duplicating the common information.

2. Use a program name that is mnemonic but also contains a
   version identifier. That is, assume there will be several versions. Here the index is the low order digit of the year 1967.

3. Incorporate the prose description as comments to PROCEDURE.

4. Refer to standard literature to document basic algorithms
   wherever possible. This saves space, usually points to a much
   fuller treatment than one would provide, and allows the
   knowledgeable reader to skip it with confidence that they understand you.

5. Show the relationship to the book algorithm:
   - a) changes
   - b) specialization
   - c) representation

6. Declare all variables. Use mnemonic names. Use comments to
   convert DECLARE into a complete legend. Note that it already
   contains names and structural descriptions, it needs only to be
   augmented with descriptions of purpose. By doing so here, one
   can avoid repeating the names and structural descriptions in
   a separate treatment.

7. Mark the initialization by a label.

8. Label statements in groups to show correspondences to the
   statements in the algorithm description in the literature.

9. Use indenting to show structure and grouping.

10. Add logical flow arrows to the listing by hand. They are very
    helpful in debugging and changing. They may be incorporated
    in the right margin of the comments space, and made part of
    the machine-readable text.

11. Use line comments or remark anything that is not obvious. If
    the techniques above have been used, these will be short and
    fewer in number than is customary.

12. Put multiple statements on one line, or one statement on several lines to match thought-grouping and to show correspondence to other algorithm description.

**Why not?** What are the drawbacks of such an approach to documentation? There are several, which have been real but are becoming imaginary with changing times.

The most serious objection is the increase in the size of the
source code that must be stored. As the discipline moves more and
more toward on-line storage of source code, this has become a
growing consideration. I find myself being briefer in comments to
an APL program, which will live on a disk, than on a PL/I one that
I will store as cards.

Yet simultaneously we are moving also toward on-line storage
of prose documents for access and for updating via computerized
text-editing. As shown above, amalgamating prose and program
reduces the total number of characters to be stored.

A similar answer applies to the argument that self-documenting programs require more keystrokes. A typed document requires
at least one keystroke per character per draft. A self-documenting
program has fewer total characters and also fewer strokes per
character, since drafts aren't retyped.

How about flow charts and structure graphs? If one uses only
a highest-level structure graph, it might safely be kept as a separate document, for it is not subject to frequent change. But it can
certainly be incorporated into the source program as a comment,
and that seems wise.

To what extent are the techniques used above applicable to
assembly language programs? I think the basic approach of self-documentation is thoroughly applicable. Space and formats are
less free, and thus cannot be so flexibly used. Names and structural
declarations can surely be exploited. Macros can help a great deal.
The extensive use of paragraph comments is good practice in any
language.

But the self-documentation approach is stimulated by the use
of high-level languages and finds its greatest power and its greatest justification in high-level languages used with on-line systems,
whether batch or interactive. As I have argued, such languages and
systems help programmers in very powerful ways. Since machines
are made for people, not people for machines, their use makes
every form of sense, economic and human.

---

[^1]: H. H. Goldstine and J. von Neumann, "Planning and coding problems for an electronic computing instrument," in John von Neumann, *Collected Works*, A. H. Taub, ed. New York: Macmillan, 1963, Vol. V, pp. 80-235.

[^2]: K. E. Iverson, *A Programming Language*. New York: Wiley, 1962.

[^3]: This example is taken from F. P. Brooks, Jr., and K. E. Iverson, *Automatic Data Processing, System/360 Edition*. New York: Wiley, 1969, Chapter 6.
