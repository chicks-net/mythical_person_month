# Phase 2b: Generic Pronoun Modernization

**Chapters:** 3 (The Surgical Team), 4 (Aristocracy, Democracy, and System Design), and 5 (The Second-System Effect)

**Date:** 2025-10-27

**Status:** Ready for implementation

## Overview

This document provides a detailed task list for Phase 2 modernization of chapters 3, 4, and 5, focusing on replacing generic masculine pronouns with inclusive alternatives. Each instance includes the current text, line number, context, and recommended replacement strategy.

**Note:** Chapter 3 is particularly challenging as it extensively describes team roles using masculine pronouns throughout. This will require careful, systematic revision while maintaining the surgical team metaphor.

## Chapter 3: The Surgical Team

**File:** `chapters/06-chapter-03-the-surgical-team.md`

**Total instances:** 18+ generic pronoun uses requiring attention

**Special consideration:** This chapter describes specific roles (surgeon, copilot, administrator, etc.) extensively using masculine pronouns. The challenge is to maintain the surgical metaphor while making the language inclusive.

### Instance 1: Trading men and months

**Line:** 24

**Current text:**
```markdown
Our postulated 200-person team would have taken 25 years to have brought the product to its present stage, if men and months traded evenly!
```

**Context:** Generic workers

**Recommended strategy:** Replace "men" with "people"

**Suggested replacement:**
```markdown
Our postulated 200-person team would have taken 25 years to have brought the product to its present stage, if people and months traded evenly!
```

---

### Instance 2: Mills's proposal - cutting metaphor

**Line:** 31

**Current text:**
```markdown
That is, instead of each member cutting away on the problem, one does the cutting and the others give him every support that will enhance his effectiveness and productivity.
```

**Context:** Generic team member doing the primary work

**Recommended strategy:** Singular they (both instances)

**Suggested replacement:**
```markdown
That is, instead of each member cutting away on the problem, one does the cutting and the others give them every support that will enhance their effectiveness and productivity.
```

---

### The Surgeon Role (Lines 39-40)

**Line:** 39-40

**Current text:**
```markdown
**The surgeon.** Mills calls him a chief programmer. He personally defines the functional and performance specifications, designs the program, codes it, tests it, and writes its documentation. He writes in a structured programming language such as PL/I, and has effective access to a computing system which not only runs his tests but also stores the various versions of his programs, allows easy file updating, and provides text editing for his documentation. He needs great talent, ten years experience, and considerable systems and application knowledge, whether in applied mathematics, business data handling, or whatever.
```

**Context:** Generic surgeon/chief programmer role

**Recommended strategy:** Singular they throughout

**Suggested replacement:**
```markdown
**The surgeon.** Mills calls them a chief programmer. They personally define the functional and performance specifications, design the program, code it, test it, and write its documentation. They write in a structured programming language such as PL/I, and have effective access to a computing system which not only runs their tests but also stores the various versions of their programs, allows easy file updating, and provides text editing for their documentation. They need great talent, ten years experience, and considerable systems and application knowledge, whether in applied mathematics, business data handling, or whatever.
```

**Note:** This is a key passage that sets the tone for the chapter. Using singular "they" consistently here establishes the pattern.

---

### The Copilot Role (Line 41)

**Line:** 41

**Current text:**
```markdown
**The copilot.** He is the alter ego of the surgeon, able to do any part of the job, but is less experienced. His main function is to share in the design as a thinker, discussant, and evaluator. The surgeon tries ideas on him, but is not bound by his advice. The copilot often represents his team in discussions of function and interface with other teams. He knows all the code intimately. He researches alternative design strategies. He obviously serves as insurance against disaster to the surgeon. He may even write code, but he is not responsible for any part of the code.
```

**Context:** Generic copilot role

**Recommended strategy:** Singular they throughout (9 instances)

**Suggested replacement:**
```markdown
**The copilot.** They are the alter ego of the surgeon, able to do any part of the job, but are less experienced. Their main function is to share in the design as a thinker, discussant, and evaluator. The surgeon tries ideas on them, but is not bound by their advice. The copilot often represents the team in discussions of function and interface with other teams. They know all the code intimately. They research alternative design strategies. They obviously serve as insurance against disaster to the surgeon. They may even write code, but are not responsible for any part of the code.
```

**Alternative consideration:** Change "his team" to "the team" to avoid possessive pronoun.

---

### The Administrator Role (Line 43)

**Line:** 43

**Current text:**
```markdown
**The administrator.** The surgeon is boss, and he must have the last word on personnel, raises, space, and so on, but he must spend almost none of his time on these matters. Thus he needs a professional administrator who handles money, people, space, and machines, and who interfaces with the administrative machinery of the rest of the organization.
```

**Context:** Generic surgeon and administrator roles

**Recommended strategy:** Singular they for surgeon references

**Suggested replacement:**
```markdown
**The administrator.** The surgeon is boss, and must have the last word on personnel, raises, space, and so on, but must spend almost none of their time on these matters. Thus they need a professional administrator who handles money, people, space, and machines, and who interfaces with the administrative machinery of the rest of the organization.
```

**Note:** Dropped "he" before "must have" and "must spend" as the subject is already clear, making the sentence more concise.

---

### The Program Clerk Role (Line 49)

**Line:** 49

**Current text:**
```markdown
**The program clerk.** He is responsible for maintaining all the technical records of the team in a programming-product library.
```

**Context:** Generic program clerk role

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
**The program clerk.** They are responsible for maintaining all the technical records of the team in a programming-product library.
```

---

### Continuation of Program Clerk Description (Line 51)

**Line:** 51

**Current text:**
```markdown
All computer input goes to the clerk, who logs and keys it if required. The output listings go back to him to be filed and indexed.
```

**Context:** Generic program clerk

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
All computer input goes to the clerk, who logs and keys it if required. The output listings go back to them to be filed and indexed.
```

---

### Continuation of Program Clerk Description (Line 53)

**Line:** 53

**Current text:**
```markdown
When interactive terminals are used, particularly those with no hard-copy output, the program clerk's functions do not diminish, but they change. Now he logs all updates of team program copies from private working copies, still handles all batch runs, and uses his own interactive facility to control the integrity and availability of the growing product.
```

**Context:** Generic program clerk

**Recommended strategy:** Singular they (already has "they" for functions, need to change "he" and "his")

**Suggested replacement:**
```markdown
When interactive terminals are used, particularly those with no hard-copy output, the program clerk's functions do not diminish, but they change. Now the clerk logs all updates of team program copies from private working copies, still handles all batch runs, and uses their own interactive facility to control the integrity and availability of the growing product.
```

**Note:** Changed "he" to "the clerk" to avoid pronoun confusion with "they" (which refers to functions in previous clause).

---

### The Toolsmith Role (Line 55)

**Line:** 55

**Current text:**
```markdown
But these services must be available with unquestionably satisfactory response and reliability; and the surgeon must be sole judge of the adequacy of the service available to him. He needs a toolsmith, responsible for ensuring this adequacy of the basic service and for constructing, maintaining, and upgrading special tools—mostly interactive computer services—needed by his team. Each team will need its own toolsmith, regardless of the excellence and reliability of any centrally provided service, for his job is to see to the tools needed or wanted by his surgeon, without regard to any other team's needs.
```

**Context:** Generic surgeon and toolsmith roles

**Recommended strategy:** Singular they for surgeon, restructure to avoid gendered pronouns for toolsmith

**Suggested replacement:**
```markdown
But these services must be available with unquestionably satisfactory response and reliability; and the surgeon must be sole judge of the adequacy of the service available to them. They need a toolsmith, responsible for ensuring this adequacy of the basic service and for constructing, maintaining, and upgrading special tools—mostly interactive computer services—needed by the team. Each team will need its own toolsmith, regardless of the excellence and reliability of any centrally provided service, for the toolsmith's job is to see to the tools needed or wanted by the surgeon, without regard to any other team's needs.
```

**Note:** Changed "his team" to "the team" and "his job" to "the toolsmith's job" and "his surgeon" to "the surgeon".

---

### The Tester Role (Line 57)

**Line:** 57

**Current text:**
```markdown
**The tester.** The surgeon will need a bank of suitable test cases for testing pieces of his work as he writes it, and then for testing the whole thing.
```

**Context:** Generic surgeon role

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
**The tester.** The surgeon will need a bank of suitable test cases for testing pieces of their work as they write it, and then for testing the whole thing.
```

---

### The Language Lawyer Role (Line 59)

**Line:** 59

**Current text:**
```markdown
**The language lawyer.** By the time Algol came along, people began to recognize that most computer installations have one or two people who delight in mastery of the intricacies of a programming language. And these experts turn out to be very useful and very widely consulted. The talent here is rather different from that of the surgeon, who is primarily a system designer and who thinks representations. The language lawyer can find a neat and efficient way to use the language to do difficult, obscure, or tricky things. Often he will need to do small studies (two or three days) on good technique.
```

**Context:** Generic language lawyer role

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
**The language lawyer.** By the time Algol came along, people began to recognize that most computer installations have one or two people who delight in mastery of the intricacies of a programming language. And these experts turn out to be very useful and very widely consulted. The talent here is rather different from that of the surgeon, who is primarily a system designer and who thinks representations. The language lawyer can find a neat and efficient way to use the language to do difficult, obscure, or tricky things. Often they will need to do small studies (two or three days) on good technique.
```

---

## Chapter 4: Aristocracy, Democracy, and System Design

**File:** `chapters/07-chapter-04-aristocracy-democracy-and-system-design.md`

**Total instances:** 13 generic pronoun uses requiring attention

### Instance 1: Cathedral builders

**Line:** 15

**Current text:**
```markdown
The joy that stirs the beholder comes as much from the integrity of the design as from any particular excellences. As the guidebook tells, this integrity was achieved by the self-abnegation of eight generations of builders, each of whom sacrificed some of his ideas so that the whole might be of pure design.
```

**Context:** Generic builders

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
The joy that stirs the beholder comes as much from the integrity of the design as from any particular excellences. As the guidebook tells, this integrity was achieved by the self-abnegation of eight generations of builders, each of whom sacrificed some of their ideas so that the whole might be of pure design.
```

---

### Instance 2: Many tasks done by many men

**Line:** 17

**Current text:**
```markdown
Usually this arises not from a serial succession of master designers, but from the separation of design into many tasks done by many men.
```

**Context:** Generic workers

**Recommended strategy:** Replace "men" with "people"

**Suggested replacement:**
```markdown
Usually this arises not from a serial succession of master designers, but from the separation of design into many tasks done by many people.
```

---

### Instance 3: Implementer understanding

**Line:** 24

**Current text:**
```markdown
How does one ensure that every trifling detail of an architectural specification gets communicated to the implementer, properly understood by him, and accurately incorporated into the product?
```

**Context:** Generic implementer

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
How does one ensure that every trifling detail of an architectural specification gets communicated to the implementer, properly understood by them, and accurately incorporated into the product?
```

---

### Instance 4: User doing their job

**Line:** 46

**Current text:**
```markdown
For the entire system it is the union of the manuals the user must consult to do his entire job.
```

**Context:** Generic user

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
For the entire system it is the union of the manuals the user must consult to do their entire job.
```

---

### Instance 5: Architect's job

**Line:** 48

**Current text:**
```markdown
The architect of a system, like the architect of a building, is the user's agent. It is his job to bring professional and technical knowledge to bear in the unalloyed interest of the user, as opposed to the interests of the salesperson, the fabricator, etc.
```

**Context:** Generic architect

**Recommended strategy:** Singular they or restructure

**Suggested replacement:**
```markdown
The architect of a system, like the architect of a building, is the user's agent. It is the architect's job to bring professional and technical knowledge to bear in the unalloyed interest of the user, as opposed to the interests of the salesperson, the fabricator, etc.
```

**Alternative (singular they):**
```markdown
The architect of a system, like the architect of a building, is the user's agent. It is their job to bring professional and technical knowledge to bear in the unalloyed interest of the user, as opposed to the interests of the salesperson, the fabricator, etc.
```

---

### Instance 6: Implementer starting work (Line 107, multiple instances)

**Line:** 107

**Current text:**
```markdown
In computer design, for example, the implementer can start as soon as he has relatively vague assumptions about the manual, somewhat clearer ideas about the technology, and well-defined cost and performance objectives. He can begin designing data flows, control sequences, gross packaging concepts, and so on. He devises or adapts the tools he will need, especially the record-keeping system, including the design automation system.
```

**Context:** Generic implementer

**Recommended strategy:** Singular they (5 instances)

**Suggested replacement:**
```markdown
In computer design, for example, the implementer can start as soon as they have relatively vague assumptions about the manual, somewhat clearer ideas about the technology, and well-defined cost and performance objectives. They can begin designing data flows, control sequences, gross packaging concepts, and so on. They devise or adapt the tools they will need, especially the record-keeping system, including the design automation system.
```

---

### Instance 7: Programming system implementer (Line 110, multiple instances)

**Line:** 110

**Current text:**
```markdown
Long before the external specifications are complete, the implementer has plenty to do. Given some rough approximations as to the function of the system that will be ultimately embodied in the external specifications, he can proceed. He must have well-defined space and time objectives. He must know the system configuration on which his product must run. Then he can begin designing module boundaries, table structures, pass or phase breakdowns, algorithms, and all kinds of tools.
```

**Context:** Generic implementer

**Recommended strategy:** Singular they (6 instances)

**Suggested replacement:**
```markdown
Long before the external specifications are complete, the implementer has plenty to do. Given some rough approximations as to the function of the system that will be ultimately embodied in the external specifications, they can proceed. They must have well-defined space and time objectives. They must know the system configuration on which their product must run. Then they can begin designing module boundaries, table structures, pass or phase breakdowns, algorithms, and all kinds of tools.
```

---

## Chapter 5: The Second-System Effect

**File:** `chapters/08-chapter-05-the-second-system-effect.md`

**Total instances:** 20+ generic pronoun uses requiring attention

**Note:** This chapter extensively discusses "the architect" as a generic role, with many pronoun references throughout.

### Instance 1: Building architect working against budget (Lines 15-16)

**Line:** 15-16

**Current text:**
```markdown
The architect of a building works against a budget, using estimating techniques that are later confirmed or corrected by the contractors' bids. It often happens that all the bids exceed the budget. The architect then revises his estimating technique upward and his design downward for another iteration. He may perhaps suggest to the contractors ways to implement his design more cheaply than they had devised.
```

**Context:** Generic building/system architect

**Recommended strategy:** Singular they throughout

**Suggested replacement:**
```markdown
The architect of a building works against a budget, using estimating techniques that are later confirmed or corrected by the contractors' bids. It often happens that all the bids exceed the budget. The architect then revises their estimating technique upward and their design downward for another iteration. They may perhaps suggest to the contractors ways to implement their design more cheaply than they had devised.
```

---

### Instance 2: System architect advantages (Line 17)

**Line:** 17

**Current text:**
```markdown
An analogous process governs the architect of a computer system or a programming system. He has, however, the advantage of getting bids from the contractor at many early points in his design, almost any time he asks for them.
```

**Context:** Generic system architect

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
An analogous process governs the architect of a computer system or a programming system. They have, however, the advantage of getting bids from the contractor at many early points in their design, almost any time they ask for them.
```

---

### Instance 3: Architect specifying (Line 22)

**Line:** 22

**Current text:**
```markdown
always be prepared to suggest a way of implementing anything he specifies, and be prepared to accept any other way that meets the objectives as well;
```

**Context:** Generic architect (in bulleted list)

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
always be prepared to suggest a way of implementing anything they specify, and be prepared to accept any other way that meets the objectives as well;
```

---

### Instance 4: Builder countering (Line 26)

**Line:** 26

**Current text:**
```markdown
Normally the builder will counter by suggesting changes to the architecture. Often he is right—some minor feature may have unexpectedly large costs when the implementation is worked out.
```

**Context:** Generic builder

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
Normally the builder will counter by suggesting changes to the architecture. Often they are right—some minor feature may have unexpectedly large costs when the implementation is worked out.
```

---

### Instance 5: Architect's first work (Lines 30-32)

**Line:** 30-32

**Current text:**
```markdown
An architect's first work is apt to be spare and clean. He knows he doesn't know what he's doing, so he does it carefully and with great restraint.

As he designs the first work, frill after frill and embellishment after embellishment occur to him. These get stored away to be used "next time."
```

**Context:** Generic architect

**Recommended strategy:** Singular they throughout

**Suggested replacement:**
```markdown
An architect's first work is apt to be spare and clean. They know they don't know what they're doing, so they do it carefully and with great restraint.

As they design the first work, frill after frill and embellishment after embellishment occur to them. These get stored away to be used "next time."
```

---

### Instance 6: Second system danger (Line 34)

**Line:** 34

**Current text:**
```markdown
This second is the most dangerous system a man ever designs. When he does his third and later ones, his prior experiences will confirm each other as to the general characteristics of such systems, and their differences will identify those parts of his experience that are particular and not generalizable.
```

**Context:** Generic designer/architect

**Recommended strategy:** Replace "a man" with "anyone" or "an architect", use singular they

**Suggested replacement:**
```markdown
This second is the most dangerous system anyone ever designs. When they do their third and later ones, their prior experiences will confirm each other as to the general characteristics of such systems, and their differences will identify those parts of their experience that are particular and not generalizable.
```

**Alternative:**
```markdown
This second is the most dangerous system an architect ever designs. When they do their third and later ones, their prior experiences will confirm each other as to the general characteristics of such systems, and their differences will identify those parts of their experience that are particular and not generalizable.
```

---

### Instance 7: Project manager and senior architect (Line 70)

**Line:** 70

**Current text:**
```markdown
How does the project manager avoid the second-system effect? By insisting on a senior architect who has at least two systems under his belt.
```

**Context:** Generic senior architect

**Recommended strategy:** Singular they

**Suggested replacement:**
```markdown
How does the project manager avoid the second-system effect? By insisting on a senior architect who has at least two systems under their belt.
```

---

## Implementation Checklist

### Pre-implementation

- [ ] Create feature branch: `just branch modernize-ch3-ch4-ch5-pronouns`
- [ ] Review all suggested replacements
- [ ] Decide on preferred alternatives where multiple options exist
- [ ] Note that Chapter 3 will require the most careful attention due to extensive role descriptions

### Chapter 3 Implementation (The Surgical Team)

**General note:** This chapter requires systematic revision of 10 role descriptions, each using masculine pronouns extensively.

- [ ] Instance 1: Line 24 - men and months (men → people)
- [ ] Instance 2: Line 31 - cutting metaphor (him/his → them/their)
- [ ] The Surgeon Role: Line 39-40 - complete role description (him/He/his → them/They/their, ~8 instances)
- [ ] The Copilot Role: Line 41 - complete role description (He/His/him/his → They/Their/them/their, ~9 instances)
- [ ] The Administrator Role: Line 43 - description (he/his → restructure with they/their)
- [ ] The Program Clerk Role: Line 49 - introduction (He → They)
- [ ] Program Clerk continued: Line 51 - description (him → them)
- [ ] Program Clerk continued: Line 53 - functions (he/his → the clerk/their)
- [ ] The Toolsmith Role: Line 55 - description (him/He/his → them/They/the team/the toolsmith's)
- [ ] The Tester Role: Line 57 - description (his/he → their/they)
- [ ] The Language Lawyer Role: Line 59 - description (he → they)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Chapter 4 Implementation (Aristocracy, Democracy, and System Design)

- [ ] Instance 1: Line 15 - cathedral builders (his → their)
- [ ] Instance 2: Line 17 - many men (men → people)
- [ ] Instance 3: Line 24 - implementer understanding (him → them)
- [ ] Instance 4: Line 46 - user's job (his → their)
- [ ] Instance 5: Line 48 - architect's job (his → their or "the architect's")
- [ ] Instance 6: Line 107 - implementer starting (he/his → they/their, 5 instances)
- [ ] Instance 7: Line 110 - programming implementer (he/his → they/their, 6 instances)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Chapter 5 Implementation (The Second-System Effect)

- [ ] Instance 1: Lines 15-16 - building architect (his/He → their/They, 4 instances)
- [ ] Instance 2: Line 17 - system architect (He/his/he → They/their/they, 3 instances)
- [ ] Instance 3: Line 22 - architect specifying (he → they)
- [ ] Instance 4: Line 26 - builder countering (he → they)
- [ ] Instance 5: Lines 30-32 - architect's first work (He/he/him → They/they/them, 6 instances)
- [ ] Instance 6: Line 34 - second system danger (a man/he/his → anyone/they/their, 4 instances)
- [ ] Instance 7: Line 70 - senior architect (his → their)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Post-implementation

- [ ] Run `markdownlint-cli2 chapters/06-chapter-03-the-surgical-team.md`
- [ ] Run `markdownlint-cli2 chapters/07-chapter-04-aristocracy-democracy-and-system-design.md`
- [ ] Run `markdownlint-cli2 chapters/08-chapter-05-the-second-system-effect.md`
- [ ] Search for any remaining instances: `grep -n '\bhe\b|\bhis\b|\bhim\b|\bmen\b' chapters/06-*.md chapters/07-*.md chapters/08-*.md`
- [ ] Commit changes with descriptive message
- [ ] Create PR: `just pr`
- [ ] Request review from fresh eyes

## Quality Assurance

### Validation Criteria

For each change, verify:

1. **Meaning preserved:** Does the new text convey the same technical/conceptual meaning?
2. **Natural flow:** Does it read smoothly and naturally?
3. **Brooks's voice:** Is the authorial voice and style maintained?
4. **Consistency:** Are similar constructions handled similarly throughout?
5. **Grammar:** Is the new construction grammatically correct?
6. **Metaphor integrity:** Especially for Chapter 3, does the surgical team metaphor remain clear and effective?

### Common Pitfalls to Avoid

- **Awkward repetition:** Don't repeat role nouns too frequently in a single paragraph
- **Forced plural:** Don't pluralize where singular makes more conceptual sense
- **Lost emphasis:** Maintain Brooks's rhetorical emphasis and rhythm
- **Over-correction:** Context matters - ensure changes improve readability
- **Metaphor confusion:** In Chapter 3, ensure the surgical team roles remain clear and distinguishable

### Special Considerations for Chapter 3

The Surgical Team chapter presents unique challenges:

1. **Role clarity:** Each role (surgeon, copilot, administrator, etc.) must remain clearly defined
2. **Metaphor consistency:** The surgical metaphor should be preserved while updating pronouns
3. **Extensive revision needed:** Nearly every role description uses masculine pronouns multiple times
4. **Readability:** With so many changes, extra care is needed to maintain natural flow

**Strategy:** Consider revising one role description at a time, reading each aloud before proceeding to the next.

## Notes

### Chapter 3: The Surgical Team - Most Intensive Revision

This chapter will require the most extensive editing of any chapter in Phase 2. Nearly every paragraph describing team roles uses masculine pronouns. The revision must:

- Maintain the clarity of role definitions
- Preserve the surgical team metaphor that is central to Brooks's argument
- Ensure the language flows naturally despite numerous pronoun changes
- Keep the technical precision of role descriptions intact

### Consistency Across Chapters

All three chapters discuss architects, implementers, and builders as generic roles. Ensure consistent treatment:

- "the architect...they" (not mixing with "the architect...he")
- "the implementer...them" (not "the implementer...him")
- "the builder...their" (not "the builder...his")

### Historical vs. Modern Language

Note that these chapters discuss real historical systems (OS/360, Stretch, etc.) and real people (Mills, Blaauw). When referring to specific individuals, original pronouns may be appropriate if those individuals' gender is known. The focus is on generic role references.

## Estimated Effort

- **Review and decision on alternatives:** 45 minutes
- **Chapter 3 implementation (most intensive):** 2 hours
- **Chapter 4 implementation:** 1 hour
- **Chapter 5 implementation:** 1 hour
- **Quality check (read-through, linting):** 45 minutes
- **Total:** ~5.5 hours

This is significantly more time than Phase 2a due to the extensive revisions needed in Chapter 3.

## References

- **Source analysis:** `Modernization_Analysis.md` - Phase 2 recommendations
- **Phase 2a:** `phase2a.md` - Completed chapters 1-2 for consistency reference
- **Style guides:**
  - APA Style: Singular 'they' is accepted for generic references
  - Chicago Manual of Style: Gender-neutral pronouns guidance
- **Project context:** `CLAUDE.md` - Repository purpose and modernization goals
