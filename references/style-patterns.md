# HTML Style Patterns

Use this reference when producing lecture mind-map HTML. The built-in assets directory is part of the skill and should be treated as the first-choice template source.

## Template Assets

Read these files before writing any new HTML:

- `assets/templates/coarse/第六章脉络大纲.html`: primary coarse template.
- `assets/templates/coarse/第一章脉络大纲.html` through `第五章脉络大纲.html`: same family with chapter-specific variations.
- `assets/templates/detailed/第四章.html` and `第五章.html`: primary detailed templates.
- `assets/templates/detailed/第一章.html` through `第三章.html`: additional detailed examples.

Default rule:

- Coarse output: clone the chapter 6 family and replace content.
- Detailed output: clone the chapter 4/5 family and replace content.
- Do not redesign CSS from scratch unless the user explicitly asks for a new visual language.

## Coarse “脉络大纲” Version

Purpose: help the learner see the chapter's main logic quickly.

Recommended structure:

1. Header
   - `chapter-tag`: course + chapter.
   - `h1`: chapter topic.
   - `subtitle`: one-sentence chapter arc.
2. Flow diagram
   - Show the progression of ideas across lecture sections.
   - Each flow box should include section number/title and a short role.
3. Overview
   - Compact list of the main stages or concepts.
   - Use dots/arrows or short grid items.
4. Section cards
   - One card per major chapter block.
   - Each section includes a core question and 2-4 subsections.
   - Subsections use short bullets with bold/`em` keywords.
5. Comparison table
   - Summarize high-frequency review distinctions, formulas, or design tradeoffs.
6. Footer
   - State source basis, e.g. “依据 3-1 至 3-8 课件整理”.

Style cues:

- Self-contained CSS in the same file.
- Card background white, page background light gray, subtle borders/shadows.
- Number badges and section-specific accent colors.
- Responsive layout for narrow screens.
- Use ASCII arrows/entities (`&rarr;`, `-`) where practical.
- Keep the same card anatomy as the built-in coarse templates: flow diagram -> overview -> section cards -> comparison table -> footer.

## Detailed “全量解析/细致版” Version

Purpose: provide a review-ready outline close to slide detail.

Recommended structure:

1. Header with `h1` and subtitle.
2. Repeated `.section-header` blocks for major slide sections.
3. `.tree-level-1`, `.tree-level-2`, `.tree-level-3` blocks for hierarchy.
4. `.page-badge` on node titles when page ranges are known.
5. `.math-block` for formulas, instruction sequences, algorithms, and state transitions.
6. `.ai-insight` for conceptual review handles.
7. `.exam-warning` for common traps and quiz-style points.
8. Small `code` spans for registers, instructions, fields, and symbols.

Content density:

- Include important definitions and all major formulas/algorithms.
- Preserve page ranges rather than exact page-by-page transcription.
- Group repeated slide examples into study-oriented patterns.
- Keep the file readable: detailed, but not a raw slide dump.
- Keep the same overall CSS vocabulary as the built-in detailed templates: `.section-header`, `.tree-level-*`, `.page-badge`, `.math-block`, `.ai-insight`, `.exam-warning`.

## Matching Existing Work

When examples exist, use them as the source of truth for CSS and structure. If multiple examples differ, choose the one that corresponds to the requested variant:

- “脉络”, “大纲”, “粗线条”, “主线”: use the coarse pattern.
- “细致”, “全量”, “解析”, “页码”, “考点”: use the detailed pattern.

If the user does not provide project-local samples, the skill's own `assets/templates/` files are the required fallback and should be treated as canonical.
