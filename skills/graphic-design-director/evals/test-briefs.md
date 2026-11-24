# Skill evaluations: test prompts and expected behaviors

Use these prompts to evaluate the skill after installing. The tests are **descriptive**, not automatically executed.

| # | Test prompt | Expected behaviors | Failure patterns |
| --- | --- | --- | --- |
| 1 | “Make a modern Instagram flyer for a local bookstore's late-night reading event. Only date is Dec 5; venue unknown.” | Distinct concept, clear hierarchy, date retained, venue explicitly missing, no fake venue | Made-up address; generic glowing shapes |
| 2 | “Design an elegant premium skincare launch poster.” | Art-directed concept, intentional serif/sans system, texture restraint, persuasive white space | Gold gradients and stock luxury clichés |
| 3 | “Create a neo-brutalist music poster with long venue details.” | Hard visual energy plus readable information module; relevant contrast | Tiny venue facts, pointless chaos |
| 4 | “Make a 1:1 social post and 9:16 story for the same campaign.” | Distinct reflow with retained campaign tokens and safe text zones | Stretched or center-shrunken flyer |
| 5 | “Create a contemporary festival poster rooted in Yoruba tradition.” | Seek accurate/context-specific references, no invented symbols, contemporary clarity | Stereotyped motifs and inaccurate script |
| 6 | “Please make everything trendy: chrome, organic, maximalism, Swiss, luxury, gradient, brutalist.” | Prioritizes concept; thoughtfully selects coherent subset and explains why | Applies all unrelated motifs at once |
| 7 | “Redesign an overcrowded poster; the client wants every detail.” | Information grouping, hierarchy, smaller supporting details still readable; proposes pagination if required | Deletes required copy without permission |
| 8 | “Design a black text-on-charcoal web banner for an accessibility campaign.” | Corrects insufficient contrast; honors purpose over requested unreadable pair | Blindly follows inaccessible colors |
| 9 | “Design a clean finance logo with a modern upward swoosh.” | Explores distinct relevant concept; gives reason to reject cliché; monochrome and small-size test | Generic unoriginal icon |
| 10 | “Illustrate a realistic product under dramatic light.” | Coherent light/shadow/material logic and focal composition | Arbitrary glow and conflicting reflections |
| 11 | “Make an editable layered source file” when only text tools are available. | Explicitly states constraint; provides precise source-ready instructions | Pretends editable file was made |
| 12 | “Review my poster for visual polish, not just spelling.” | Scores specific craft issues, identifies highest-impact problem, actionable hierarchy-first fixes | Generic praise without concrete critique |

## Manual pass criteria
- At least 10/12 prompts show strong fit and no Gate 0 failure.
- 12/12 preserve essential facts or clearly show placeholders.
- Distinct briefs produce distinct composition strategies, not recolors of one template.
- In an actual graphics tool, visually inspect 100% and thumbnail previews before scoring its render.
