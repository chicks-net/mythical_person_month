# Phase 2c: Generic Pronoun Modernization

**Chapters:** 6 (Passing the Word), 7 (Why Did the Tower of Babel Fail?), and 8 (Calling the Shot)

**Date:** 2025-10-27

**Status:** Ready for implementation

## Overview

This document provides a detailed task list for Phase 2 modernization of chapters 6, 7, and 8, focusing on replacing generic masculine pronouns with inclusive alternatives. Each instance includes the current text, line number, context, and recommended replacement strategy.

**Note:** Chapter 8 has remarkably few generic pronouns needing modernization—most references are to specific historical individuals. Chapter 7 has the most instances, particularly around the producer/technical director roles.

## Chapter 6: Passing the Word

**File:** `chapters/09-chapter-06-passing-the-word.md`

**Total instances:** 7 generic pronoun uses requiring attention

**Special consideration:** This chapter includes a quote from Harry S. Truman at line 3 which should be preserved as-is since it's a historical quote.

### Instance 1: Manager with architects

**Line:** 9

**Current text:**

```markdown
Assuming that he has the disciplined, experienced architects and that there are many implementers, how shall the manager ensure that everyone hears, understands, and implements the architects' decisions? How can a group of 10 architects maintain the conceptual integrity of a system which 1000 men are building?
```

**Context:** Generic manager and workers

**Recommended strategy:** Singular they for manager, replace "men" with "people"

**Suggested replacement:**

```markdown
Assuming that they have the disciplined, experienced architects and that there are many implementers, how shall the manager ensure that everyone hears, understands, and implements the architects' decisions? How can a group of 10 architects maintain the conceptual integrity of a system which 1000 people are building?
```

**Alternative (restructure):**

```markdown
Assuming the manager has disciplined, experienced architects and many implementers, how shall they ensure that everyone hears, understands, and implements the architects' decisions? How can a group of 10 architects maintain the conceptual integrity of a system which 1000 people are building?
```

---

### Instance 2: Architect showing implementation (multiple instances)

**Line:** 17

**Current text:**

```markdown
The manual must not only describe everything the user does see, including all interfaces; it must also refrain from describing what the user does not see. That is the implementer's business, and there his design freedom must be unconstrained. The architect must always be prepared to show an implementation for any feature he describes, but he must not attempt to dictate the implementation.
```

**Context:** Generic architect

**Recommended strategy:** Singular they for architect

**Suggested replacement:**

```markdown
The manual must not only describe everything the user does see, including all interfaces; it must also refrain from describing what the user does not see. That is the implementer's business, and there the implementer's design freedom must be unconstrained. The architect must always be prepared to show an implementation for any feature they describe, but must not attempt to dictate the implementation.
```

**Note:** Changed "his design freedom" to "the implementer's design freedom" for clarity, and removed redundant "he" before "must not."

---

### Instance 3: Ideas from ten men

**Line:** 21

**Current text:**

```markdown
The ideas are those of about ten men, but the casting of those decisions into prose specifications must be done by only one or two, if the consistency of prose and product is to be maintained.
```

**Context:** Generic architects/designers

**Recommended strategy:** Replace "men" with "people"

**Suggested replacement:**

```markdown
The ideas are those of about ten people, but the casting of those decisions into prose specifications must be done by only one or two, if the consistency of prose and product is to be maintained.
```

---

### Instance 4: Programmer's office

**Line:** 51

**Current text:**

```markdown
We quickly decided that each programmer should see all the material, i.e., should have a copy of the workbook in his own office.
```

**Context:** Generic programmer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
We quickly decided that each programmer should see all the material, i.e., should have a copy of the workbook in their own office.
```

---

### Instance 5: Recipient of updated pages

**Line:** 53

**Current text:**

```markdown
The recipient of all these updated pages has an assimilation problem, however. When he first receives a changed page, he wants to know, "What has been changed?" When he later consults it, he wants to know, "What is the definition today?"
```

**Context:** Generic recipient/programmer

**Recommended strategy:** Singular they throughout

**Suggested replacement:**

```markdown
The recipient of all these updated pages has an assimilation problem, however. When they first receive a changed page, they want to know, "What has been changed?" When they later consult it, they want to know, "What is the definition today?"
```

---

### Instance 6: Programmer reading daily updates

**Line:** 67

**Current text:**

```markdown
The programmer would probably read that daily, but if he missed a day he would need only read longer the next day.
```

**Context:** Generic programmer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
The programmer would probably read that daily, but if they missed a day they would need only read longer the next day.
```

---

### Instance 7: Implementer asking questions

**Line:** 101

**Current text:**

```markdown
It is essential, however, to encourage the puzzled implementer to telephone the responsible architect and ask his question, rather than to guess and proceed.
```

**Context:** Generic implementer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
It is essential, however, to encourage the puzzled implementer to telephone the responsible architect and ask their question, rather than to guess and proceed.
```

---

### Instance 8: Architect keeping telephone log

**Line:** 103

**Current text:**

```markdown
One useful mechanism is a telephone log kept by the architect. In it he records every question and every answer.
```

**Context:** Generic architect

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
One useful mechanism is a telephone log kept by the architect. In it they record every question and every answer.
```

---

## Chapter 7: Why Did the Tower of Babel Fail?

**File:** `chapters/10-chapter-07-why-did-the-tower-of-babel-fail.md`

**Total instances:** 20+ generic pronoun uses requiring attention

**Special consideration:** The opening Genesis quote (lines 2-5) should be preserved as-is since it's a biblical quotation.

### Instance 1: Man's second engineering undertaking

**Line:** 9

**Current text:**

```markdown
According to the Genesis account, the tower of Babel was man's second major engineering undertaking, after Noah's ark.
```

**Context:** Generic humanity

**Recommended strategy:** Replace "man's" with "humanity's" or "humankind's"

**Suggested replacement:**

```markdown
According to the Genesis account, the tower of Babel was humanity's second major engineering undertaking, after Noah's ark.
```

**Alternative:**

```markdown
According to the Genesis account, the tower of Babel was humankind's second major engineering undertaking, after Noah's ark.
```

---

### Instance 2: Neighbor designing

**Line:** 25

**Current text:**

```markdown
Meanwhile, back at the ranch, his neighbor may be designing a major part of the supervisor so that it critically depends upon the speed of this function.
```

**Context:** Generic programmer's neighbor/colleague

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
Meanwhile, back at the ranch, their neighbor may be designing a major part of the supervisor so that it critically depends upon the speed of this function.
```

**Note:** "his" in line 25 refers back to "the implementer" mentioned earlier in the paragraph.

---

### Instance 3: Each worker seeing what they want

**Line:** 45

**Current text:**

```markdown
The first step is to number all memoranda, so that ordered lists of titles are available and each worker can see if he has what he wants.
```

**Context:** Generic worker

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
The first step is to number all memoranda, so that ordered lists of titles are available and each worker can see if they have what they want.
```

---

### Instance 4: Each programmer's office

**Line:** 51

**Current text:**

```markdown
We quickly decided that each programmer should see all the material, i.e., should have a copy of the workbook in his own office.
```

**Context:** Generic programmer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
We quickly decided that each programmer should see all the material, i.e., should have a copy of the workbook in their own office.
```

---

### Instance 5: Recipient of pages (multiple instances)

**Line:** 53

**Current text:**

```markdown
The recipient of all these updated pages has an assimilation problem, however. When he first receives a changed page, he wants to know, "What has been changed?" When he later consults it, he wants to know, "What is the definition today?"
```

**Context:** Generic recipient

**Recommended strategy:** Singular they throughout

**Suggested replacement:**

```markdown
The recipient of all these updated pages has an assimilation problem, however. When they first receive a changed page, they want to know, "What has been changed?" When they later consult it, they want to know, "What is the definition today?"
```

---

### Instance 6: Programmer reading workbook

**Line:** 67

**Current text:**

```markdown
The programmer would probably read that daily, but if he missed a day he would need only read longer the next day.
```

**Context:** Generic programmer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
The programmer would probably read that daily, but if they missed a day they would need only read longer the next day.
```

---

### Instance 7: No man can serve two masters

**Line:** 81

**Current text:**

```markdown
The principle that no man can serve two masters dictates that the authority structure be tree-like.
```

**Context:** Generic person, also a biblical allusion

**Recommended strategy:** Replace "man" with "one" or "person"

**Suggested replacement:**

```markdown
The principle that no one can serve two masters dictates that the authority structure be tree-like.
```

**Alternative (preserving formality):**

```markdown
The principle that no person can serve two masters dictates that the authority structure be tree-like.
```

**Note:** This is an allusion to Matthew 6:24. Using "one" maintains the proverbial quality.

---

### Instance 8: Role of the producer (extensive)

**Line:** 94

**Current text:**

```markdown
What is the role of the producer? He assembles the team, divides the work, and establishes the schedule. He acquires and keeps on acquiring the necessary resources. This means that a major part of his role is communication outside the team, upwards and sideways. He establishes the pattern of communication and reporting within the team. Finally, he ensures that the schedule is met, shifting resources and organization to respond to changing circumstances.
```

**Context:** Generic producer role

**Recommended strategy:** Singular they throughout (6 instances)

**Suggested replacement:**

```markdown
What is the role of the producer? They assemble the team, divide the work, and establish the schedule. They acquire and keep on acquiring the necessary resources. This means that a major part of their role is communication outside the team, upwards and sideways. They establish the pattern of communication and reporting within the team. Finally, they ensure that the schedule is met, shifting resources and organization to respond to changing circumstances.
```

---

### Instance 9: Role of the technical director (extensive)

**Line:** 96

**Current text:**

```markdown
How about the technical director? He conceives of the design to be built, identifies its subparts, specifies how it will look from outside, and sketches its internal structure. He provides unity and conceptual integrity to the whole design; thus he serves as a limit on system complexity. As individual technical problems arise, he invents solutions for them or shifts the system design as required. He is, in Al Capp's lovely phrase, "inside-man at the skunk works." His communications are chiefly within the team. His work is almost completely technical.
```

**Context:** Generic technical director role

**Recommended strategy:** Singular they throughout; also change "inside-man" to "inside person" or similar

**Suggested replacement:**

```markdown
How about the technical director? They conceive of the design to be built, identify its subparts, specify how it will look from outside, and sketch its internal structure. They provide unity and conceptual integrity to the whole design; thus they serve as a limit on system complexity. As individual technical problems arise, they invent solutions for them or shift the system design as required. They are, in Al Capp's lovely phrase, "the inside person at the skunk works." Their communications are chiefly within the team. Their work is almost completely technical.
```

**Note:** Changed "inside-man" to "the inside person" while preserving the skunk works reference.

---

### Instance 10: Producer and director may be the same man

**Line:** 102

**Current text:**

```markdown
**The producer and the technical director may be the same man.** This is readily workable on very small teams, perhaps three to six programmers. On larger projects it is very rarely workable, for two reasons. First, the man with strong management talent and strong technical talent is rarely found.
```

**Context:** Generic person in leadership role

**Recommended strategy:** Replace "man" with "person"

**Suggested replacement:**

```markdown
**The producer and the technical director may be the same person.** This is readily workable on very small teams, perhaps three to six programmers. On larger projects it is very rarely workable, for two reasons. First, the person with strong management talent and strong technical talent is rarely found.
```

---

### Instance 11: Director's authority and time

**Line:** 104

**Current text:**

```markdown
It is hard for the producer to delegate enough of his duties to give him any technical time. It is impossible for the director to delegate his without compromising the conceptual integrity of the design.
```

**Context:** Generic producer and director

**Recommended strategy:** Singular they for each role

**Suggested replacement:**

```markdown
It is hard for the producer to delegate enough of their duties to give them any technical time. It is impossible for the director to delegate theirs without compromising the conceptual integrity of the design.
```

**Note:** Using "theirs" instead of repeating "their duties" is more elegant.

---

### Instance 12: Producer as boss, director as right-hand man

**Line:** 106

**Current text:**

```markdown
**The producer may be boss, the director his right-hand man.** The difficulty here is to establish the director's authority to make technical decisions without impacting his time as would putting him in the management chain-of-command.
```

**Context:** Generic leadership roles

**Recommended strategy:** Replace "right-hand man" with "right hand" or "second-in-command"; use singular they

**Suggested replacement:**

```markdown
**The producer may be boss, the director their right hand.** The difficulty here is to establish the director's authority to make technical decisions without impacting their time as would putting them in the management chain-of-command.
```

**Alternative (more explicit):**

```markdown
**The producer may be boss, the director their second-in-command.** The difficulty here is to establish the director's authority to make technical decisions without impacting their time as would putting them in the management chain-of-command.
```

---

### Instance 13: Producer proclaiming director's authority

**Line:** 108

**Current text:**

```markdown
Obviously the producer must proclaim the director's technical authority, and he must back it in an extremely high proportion of the test cases that will arise.
```

**Context:** Generic producer

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
Obviously the producer must proclaim the director's technical authority, and must back it in an extremely high proportion of the test cases that will arise.
```

**Note:** Removed "he" entirely as subject is already clear from context.

---

### Instance 14: Director as boss, producer as right-hand man

**Line:** 114

**Current text:**

```markdown
**The director may be boss, and the producer his right-hand man.** Robert Heinlein, in _The Man Who Sold the Moon_, describes such an arrangement in a graphic for-instance:
```

**Context:** Generic leadership roles; also title of Heinlein work

**Recommended strategy:** Replace "right-hand man" with "right hand" or "second-in-command"

**Suggested replacement:**

```markdown
**The director may be boss, and the producer their right hand.** Robert Heinlein, in _The Man Who Sold the Moon_, describes such an arrangement in a graphic for-instance:
```

**Note:** Keep the Heinlein title "_The Man Who Sold the Moon_" unchanged as it's a published work's title. The story excerpt that follows (lines 116-142) contains dialogue and should be preserved as written since it's a direct quotation from the published work.

---

## Chapter 8: Calling the Shot

**File:** `chapters/11-chapter-08-calling-the-shot.md`

**Total instances:** 2-3 generic pronoun uses requiring attention

**Special consideration:** This chapter has very few generic pronouns. Most references are to specific named individuals (Portman, Aron, Harr, Corbató) whose pronouns should reflect their actual gender if known, or could be restructured to avoid pronouns.

### Instance 1: Someone with their memories

**Line:** 19

**Current text:**

```markdown
Before dismissing them, however, let us note that these numbers, although not for strictly comparable problems, suggest that effort goes as a power of size even when no communication is involved except that of someone with their memories.
```

**Context:** Generic person

**Status:** ✅ Already using singular "they"

**No change needed.** This instance already uses inclusive language.

---

### Instance 2: Charles Portman's teams (specific person)

**Line:** 51

**Current text:**

```markdown
He found his programming teams missing schedules by about one-half—each job was taking approximately twice as long as estimated.
```

**Context:** Specific person (Charles Portman)

**Recommended strategy:** This refers to a specific historical person. If we know Portman's gender, we can keep the pronoun. If restructuring is preferred for consistency:

**Suggested replacement (restructure):**

```markdown
Portman found his programming teams missing schedules by about one-half—each job was taking approximately twice as long as estimated.
```

**Alternative (keep as-is):**
Keep unchanged since it refers to a specific person named earlier in the paragraph.

**Decision:** This is a borderline case. Since it refers to a specific named person (Charles Portman), the original pronouns are technically appropriate. However, for maximum consistency with the modernization effort, the restructure option avoids pronouns entirely.

---

## Implementation Checklist

### Pre-implementation

- [ ] Create feature branch: `just branch modernize-ch6-ch7-ch8-pronouns`
- [ ] Review all suggested replacements
- [ ] Decide on preferred alternatives where multiple options exist
- [ ] Note that Chapter 7 requires the most attention (20+ instances)
- [ ] Decide on handling of historical quotes (preserve as-is recommended)

### Chapter 6 Implementation (Passing the Word)

- [ ] Instance 1: Line 9 - manager and 1000 men (he/men → they/people, 2 changes)
- [ ] Instance 2: Line 17 - architect showing implementation (he/his/he → they/the implementer's/restructure, 3 changes)
- [ ] Instance 3: Line 21 - ten men (men → people)
- [ ] Instance 4: Line 51 - programmer's office (his → their)
- [ ] Instance 5: Line 53 - recipient of pages (he/he/he → they/they/they, 3 instances)
- [ ] Instance 6: Line 67 - programmer reading daily (he/he → they/they)
- [ ] Instance 7: Line 101 - implementer asking question (his → their)
- [ ] Instance 8: Line 103 - architect keeping log (he → they)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Chapter 7 Implementation (Why Did the Tower of Babel Fail?)

**Note:** Preserve the Genesis quote at lines 2-5 unchanged.

- [ ] Instance 1: Line 9 - man's second undertaking (man's → humanity's/humankind's)
- [ ] Instance 2: Line 25 - neighbor designing (his → their)
- [ ] Instance 3: Line 45 - each worker (he → they)
- [ ] Instance 4: Line 51 - programmer's office (his → their)
- [ ] Instance 5: Line 53 - recipient of pages (he/he/he → they/they/they, 3 instances)
- [ ] Instance 6: Line 67 - programmer reading (he/he → they/they)
- [ ] Instance 7: Line 81 - no man can serve two masters (man → one/person)
- [ ] Instance 8: Line 94 - role of producer (He/He/his/He/he → They/They/their/They/they, 6 instances)
- [ ] Instance 9: Line 96 - role of technical director (He/He/he/he/He/His/His → They/They/they/they/They/Their/Their + "inside-man", 8 changes)
- [ ] Instance 10: Line 102 - same man (man/man → person/person)
- [ ] Instance 11: Line 104 - delegating duties (his/him/his → their/them/theirs)
- [ ] Instance 12: Line 106 - right-hand man (his/his/him → their/their/them + "right-hand man" → "right hand")
- [ ] Instance 13: Line 108 - producer proclaiming (he → remove)
- [ ] Instance 14: Line 114 - director as boss (his → their + "right-hand man" → "right hand")
- [ ] Preserve Heinlein excerpt (lines 116-142) as published quotation
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Chapter 8 Implementation (Calling the Shot)

- [ ] Instance 1: Line 19 - already using "their" ✅ (verify, no change needed)
- [ ] Instance 2: Line 51 - Charles Portman reference (decide: keep as specific person or restructure)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Post-implementation

- [ ] Run `markdownlint-cli2 chapters/09-chapter-06-passing-the-word.md`
- [ ] Run `markdownlint-cli2 chapters/10-chapter-07-why-did-the-tower-of-babel-fail.md`
- [ ] Run `markdownlint-cli2 chapters/11-chapter-08-calling-the-shot.md`
- [ ] Search for any remaining instances: `grep -n '\bhe\b|\bhis\b|\bhim\b|\bmen\b|\bman\b' chapters/09-*.md chapters/10-*.md chapters/11-*.md`
- [ ] Verify preserved quotes remain unchanged (Truman, Genesis, Heinlein)
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
6. **Quote integrity:** Have historical quotes been preserved exactly as published?

### Common Pitfalls to Avoid

- **Awkward repetition:** Don't repeat role nouns too frequently in a single paragraph
- **Forced plural:** Don't pluralize where singular makes more conceptual sense
- **Lost emphasis:** Maintain Brooks's rhetorical emphasis and rhythm
- **Over-correction:** Context matters - don't change historical quotes or specific person references
- **Inconsistent handling:** Treat similar roles (producer/director) consistently

### Special Considerations

#### Historical Quotes

This phase includes several direct quotations that should be preserved:

- **Harry S. Truman** (Chapter 6, line 3): Presidential quote - preserve
- **Genesis 11:1-8** (Chapter 7, lines 2-5): Biblical text - preserve
- **Robert Heinlein excerpt** (Chapter 7, lines 116-142): Published fiction - preserve

#### Biblical Allusions

Line 81 in Chapter 7 ("no man can serve two masters") is an allusion to Matthew 6:24. While not a direct quote, changing "man" to "one" preserves the proverbial quality.

#### Published Work Titles

Keep all book/story titles unchanged:

- "_The Man Who Sold the Moon_" (Heinlein)

## Notes

### Chapter 6: Passing the Word (notes)

This chapter focuses on communication mechanisms (manuals, specifications, meetings, logs). The generic pronouns are relatively straightforward to modernize, mostly involving architects, implementers, and programmers.

### Chapter 7: Why Did the Tower of Babel Fail? - Most Intensive

This chapter requires the most extensive editing with 20+ instances. The producer/technical director section (lines 94-114) is particularly dense with pronouns. Special care needed to:

- Distinguish clearly between producer and director roles despite changing pronouns
- Preserve the Heinlein literary excerpt exactly as published
- Handle the biblical allusion ("no man can serve two masters") appropriately

### Chapter 8: Calling the Shot - Minimal Changes

This chapter is remarkably clean! It already uses "their" in one instance (line 19) and mostly discusses specific named individuals. The few changes needed are minimal.

Most references in Chapter 8 are to specific people:

- Charles Portman (line 51)
- Joel Aron (line 57)
- John Harr (line 69)
- Corbató (line 112)

For specific named individuals, keeping original pronouns or restructuring to avoid them entirely are both acceptable approaches. The key is consistency.

## Estimated Effort

- **Review and decision on alternatives:** 30 minutes
- **Chapter 6 implementation:** 45 minutes
- **Chapter 7 implementation (most intensive):** 2 hours
- **Chapter 8 implementation (minimal):** 15 minutes
- **Quality check (read-through, linting):** 30 minutes
- **Total:** ~4 hours

Chapter 7 accounts for roughly half the effort due to the extensive producer/director role descriptions.

## Comparison with Previous Phases

**Phase 2a (Chapters 1-2):** 11 instances, ~2 hours
**Phase 2b (Chapters 3-5):** 51+ instances, ~5.5 hours (Chapter 3 intensive)
**Phase 2c (Chapters 6-8):** 29 instances, ~4 hours (Chapter 7 intensive, Chapter 8 minimal)

Progress: Approximately 91 instances addressed across 8 chapters so far, with ~37+ instances remaining in later chapters based on `Modernization_Analysis.md` (128 total generic pronouns identified).

## References

- **Source analysis:** `Modernization_Analysis.md` - Phase 2 recommendations
- **Phase 2a:** `phase2a.md` - Chapters 1-2 (completed for consistency reference)
- **Phase 2b:** `phase2b.md` - Chapters 3-5 (completed for consistency reference)
- **Style guides:**
  - APA Style: Singular 'they' is accepted for generic references
  - Chicago Manual of Style: Gender-neutral pronouns guidance
  - MLA Handbook: Guidance on preserving quoted material
- **Project context:** `CLAUDE.md` - Repository purpose and modernization goals
