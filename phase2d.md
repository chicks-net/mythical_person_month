# Phase 2d: Generic Pronoun Modernization

**Chapters:** 9 (Ten Pounds in a Five-Pound Sack), 10 (The Documentary Hypothesis), and 11 (Plan to Throw One Away)

**Date:** 2025-10-27

**Status:** Ready for implementation

## Overview

This document provides a detailed task list for Phase 2 modernization of chapters 9, 10, and 11, focusing on replacing generic masculine pronouns with inclusive alternatives.

**Important discovery:** Chapters 10 and 11 have already been comprehensively modernized with gender-neutral pronouns. Only Chapter 9 requires attention.

## Chapter 9: Ten Pounds in a Five-Pound Sack

**File:** `chapters/12-chapter-09-ten-pounds-in-a-five-pound-sack.md`

**Total instances:** 9 generic pronoun uses requiring attention (across 7 sentences)

### Instance 1: System designer resource allocation (two pronouns)

**Line:** 13

**Current text:**

```markdown
The system designer puts part of his total hardware resource into resident-program memory when he thinks it will do more for the user in that form
```

**Context:** Generic system designer making resource allocation decisions

**Recommended strategy:** Singular they (both instances)

**Suggested replacement:**

```markdown
The system designer puts part of their total hardware resource into resident-program memory when they think it will do more for the user in that form
```

**Alternative (plural reframing):**

```markdown
System designers put part of their total hardware resources into resident-program memory when they think it will do more for the user in that form
```

---

### Instance 2: Manager saving kitty (reflexive pronoun)

**Line:** 19

**Current text:**

```markdown
The wise manager also saves himself a kitty, to be allocated as work proceeds.
```

**Context:** Generic manager setting aside resources

**Recommended strategy:** Singular they (reflexive)

**Suggested replacement:**

```markdown
The wise manager also saves themselves a kitty, to be allocated as work proceeds.
```

**Alternative (remove reflexive):**

```markdown
The wise manager also saves a kitty, to be allocated as work proceeds.
```

---

### Instance 3: Programmer overlaying code (four pronouns/terms)

**Line:** 25

**Current text:**

```markdown
As anyone with 20-20 hindsight would expect, a programmer who found his program slopping over his core target broke it into overlays. This process in itself added to the total size and slowed execution down. Most seriously, our management control system neither measured nor caught this. Each man reported as to how much core he was using, and since he was within target, no one worried.
```

**Context:** Generic programmer dealing with memory constraints, then team members reporting on resource usage

**Recommended strategy:** Singular they for all instances, "person" for "man"

**Suggested replacement:**

```markdown
As anyone with 20-20 hindsight would expect, a programmer who found their program slopping over their core target broke it into overlays. This process in itself added to the total size and slowed execution down. Most seriously, our management control system neither measured nor caught this. Each person reported as to how much core they were using, and since they were within target, no one worried.
```

**Changes made:**

- "his program" → "their program"
- "his core target" → "their core target"
- "Each man" → "Each person"
- "he was using" → "they were using"

**Alternative (avoid repetition with noun):**

```markdown
As anyone with 20-20 hindsight would expect, a programmer whose program was slopping over the core target broke it into overlays.
```

---

### Instance 4: Programmer examining code (two pronouns)

**Line:** 31

**Current text:**

```markdown
As a result, any programmer in size trouble examined his code to see what he could throw over the fence into a neighbor's space.
```

**Context:** Generic programmer optimizing within constraints

**Recommended strategy:** Singular they (both instances)

**Suggested replacement:**

```markdown
As a result, any programmer in size trouble examined their code to see what they could throw over the fence into a neighbor's space.
```

---

### Instance 5: Team member suboptimization (two pronouns)

**Line:** 35

**Current text:**

```markdown
Each suboptimized his piece to meet his targets; few stopped to think about the total effect on the customer.
```

**Context:** Team members individually optimizing their work without considering the whole system

**Recommended strategy:** Singular they (both instances)

**Suggested replacement:**

```markdown
Each suboptimized their piece to meet their targets; few stopped to think about the total effect on the customer.
```

---

### Instance 6: Manager helping team

**Line:** 47

**Current text:**

```markdown
The manager can do two things to help his team make good space-time trade-offs.
```

**Context:** Generic manager supporting their team

**Recommended strategy:** Singular they

**Suggested replacement:**

```markdown
The manager can do two things to help their team make good space-time trade-offs.
```

---

### Instance 7: Programmer contemplating data (two pronouns)

**Line:** 63

**Current text:**

```markdown
The programmer at wit's end for lack of space can often do best by disentangling himself from his code, rearing back, and contemplating his data.
```

**Context:** Generic programmer needing to step back and reconsider their approach

**Recommended strategy:** Singular they (all three instances)

**Suggested replacement:**

```markdown
The programmer at wit's end for lack of space can often do best by disentangling themselves from their code, rearing back, and contemplating their data.
```

**Note:** This sentence actually has **three** pronouns that need updating: "himself" and "his" (twice).

---

## Chapter 10: The Documentary Hypothesis

**File:** `chapters/13-chapter-10-the-documentary-hypothesis.md`

**Status:** ✅ Already modernized

**Total instances:** 0 requiring attention

### Analysis

This chapter has already been comprehensively modernized with gender-neutral pronouns throughout:

- Line 17: "a craftsperson themselves" (modernized from "craftsman himself")
- Lines 21-25: Consistent use of "they/their" for "the manager"
- Lines 139-164: Extensive use of "they/their" throughout the manager discussion
- Line 150: "salesperson-projected" (modernized from "salesman")

**One note:** Line 78 contains "his inertia" referring to "the best engineering manager I ever saw" - this appears to reference a specific individual known to the author, not a generic role, so it may be acceptable to preserve. However, for consistency, could be changed to "their inertia."

### Potential optional change

**Line:** 78

**Current text:**

```markdown
On another project the best engineering manager I ever saw served often as a giant flywheel, his inertia damping the fluctuations that came from market and management people.
```

**Context:** Specific individual the author worked with

**Note:** This could refer to a specific person (thus properly masculine) or could be modernized for consistency

**Optional replacement (for consistency):**

```markdown
On another project the best engineering manager I ever saw served often as a giant flywheel, their inertia damping the fluctuations that came from market and management people.
```

**Recommendation:** Review whether this refers to a specific known individual. If so, may be acceptable to preserve. If the author intends this as a generic example, modernize for consistency.

---

## Chapter 11: Plan to Throw One Away

**File:** `chapters/14-chapter-11-plan-to-throw-one-away.md`

**Status:** ✅ Already modernized

**Total instances:** 0 requiring attention

### Analysis of Chapter 11

This chapter has also been comprehensively modernized with gender-neutral pronouns throughout:

- Lines 104-108: "the designer... themselves... they" (complete modernization of designer role)
- Line 172: "the repairer... they" (complete modernization of repairer role)
- Throughout: Consistent use of singular "they" for all generic roles

**No changes needed** - this chapter serves as an excellent example of the target modernization style.

---

## Implementation Checklist

### Pre-implementation

- [ ] Create feature branch: `just branch modernize-ch9-ch10-ch11-pronouns`
- [ ] Review suggested replacements for Chapter 9
- [ ] Decide whether to modernize Chapter 10, line 78 (specific vs. generic individual)

### Chapter 9 Implementation

- [ ] Instance 1: Line 13 - system designer (singular they, two pronouns)
- [ ] Instance 2: Line 19 - manager saving kitty (singular they reflexive)
- [ ] Instance 3: Line 25 - programmer overlaying + team reporting (four pronouns/terms)
- [ ] Instance 4: Line 31 - programmer examining code (singular they, two pronouns)
- [ ] Instance 5: Line 35 - team member suboptimization (singular they, two pronouns)
- [ ] Instance 6: Line 47 - manager helping team (singular they)
- [ ] Instance 7: Line 63 - programmer contemplating data (singular they, three pronouns)
- [ ] Read full chapter aloud to check flow
- [ ] Verify markdown formatting with `markdownlint-cli2`

### Chapter 10 Review

- [ ] Confirm chapter is already modernized
- [ ] Review line 78 and decide on specific vs. generic treatment
- [ ] No other changes needed

### Chapter 11 Review

- [ ] Confirm chapter is already modernized
- [ ] No changes needed

### Post-implementation

- [ ] Run `markdownlint-cli2 chapters/12-chapter-09-ten-pounds-in-a-five-pound-sack.md`
- [ ] Search for any remaining instances: `grep -n '\bhe\b|\bhis\b|\bhim\b' chapters/12-*.md`
- [ ] Commit changes with descriptive message
- [ ] Create PR: `just pr`
- [ ] Request review from fresh eyes

---

## Quality Assurance

### Validation Criteria

For each change, verify:

1. **Meaning preserved:** Does the new text convey the same technical/conceptual meaning?
2. **Natural flow:** Does it read smoothly and naturally?
3. **Brooks's voice:** Is the authorial voice and style maintained?
4. **Consistency:** Are similar constructions handled similarly throughout?
5. **Grammar:** Is the new construction grammatically correct?

### Common Pitfalls to Avoid

- **Awkward repetition:** Don't repeat role nouns too frequently in a single paragraph
- **Forced plural:** Don't pluralize where singular makes more conceptual sense
- **Lost emphasis:** Maintain Brooks's rhetorical emphasis and rhythm

---

## Notes

### Chapters 10 and 11: Already Modernized

**Significant finding:** Two of the three chapters in this phase have already undergone comprehensive pronoun modernization. This suggests:

1. **Partial previous work:** Someone has already modernized portions of this text
2. **Inconsistent coverage:** Not all chapters received the same treatment
3. **Quality model:** These chapters demonstrate the target style and can serve as examples

**Examples of good modernization from Chapter 10:**

```markdown
To the new manager, fresh from operating as a craftsperson themselves, these seem an unmitigated nuisance
```

```markdown
The manager will be continually amazed that policies they took for common knowledge are totally unknown by some member of their team.
```

**Examples of good modernization from Chapter 11:**

```markdown
By documenting a design, the designer exposes themselves to the criticisms of everyone, and they must be able to defend everything they write.
```

These demonstrate natural, fluent use of singular "they" that preserves Brooks's voice while updating the language.

### Workload Implications

This phase is significantly lighter than previous phases:

- **Phase 2a** (Ch 1-2): 11 instances, ~2 hours
- **Phase 2b** (Ch 3-5): 51+ instances, ~5.5 hours
- **Phase 2c** (Ch 6-8): 30+ instances, ~4 hours
- **Phase 2d** (Ch 9-11): 9 instances (7 sentences), ~1 hour (plus optional review)

### Consistency Check for Future Phases

Given that two chapters here have already been modernized, we should:

1. **Check remaining chapters** for similar partial modernization
2. **Document which chapters need work** to avoid duplicate effort
3. **Learn from the modernized chapters** to ensure consistent style

A quick scan of the remaining chapters would help identify which have already been done.

---

## Estimated Effort

- **Review and decision on alternatives:** 15 minutes
- **Implementation (editing Chapter 9):** 20 minutes
- **Review of Chapter 10, line 78:** 5 minutes
- **Quality check (read-through, linting):** 15 minutes
- **Total:** ~1 hour (significantly less than previous phases)

---

## References

- **Source analysis:** `Modernization_Analysis.md` - Phase 2 recommendations
- **Style guides:**
  - APA Style: Singular 'they' is accepted for generic references
  - Chicago Manual of Style: Gender-neutral pronouns guidance
- **Project context:** `CLAUDE.md` - Repository purpose and modernization goals
- **Examples:** Chapters 10 and 11 in this phase demonstrate excellent modernization

---

## Recommendations for Project

### Immediate Actions

1. **Scan all remaining chapters** to identify which have already been modernized
2. **Update Modernization_Analysis.md** to reflect current state
3. **Revise Phase 2 planning** based on actual remaining work

### Investigation

The discovery that some chapters have been modernized raises questions:

- When was this work done?
- Who did it?
- Was it part of the PDF-to-markdown conversion?
- Are there git commits showing this history?

**Suggested command:**

```bash
git log --all --full-history -- chapters/13-chapter-10-the-documentary-hypothesis.md
git log --all --full-history -- chapters/14-chapter-11-plan-to-throw-one-away.md
```

This would help understand the history and potentially identify the author's approach to guide remaining modernization.

---

- **Document prepared by:** Claude Code analysis
- **Analysis scope:** Chapters 9, 10, and 11
- **Total issues identified:** 9 instances (7 sentences) in Chapter 9 requiring attention
- **Status:** Chapters 10 and 11 already modernized
- **Recommendation:** Light implementation load; excellent opportunity to verify consistency with already-modernized chapters
