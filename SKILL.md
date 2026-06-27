---
name: lecture-mindmap-html-skill
description: >-
  Create static HTML mind maps and study outlines from lecture slides, PDFs, PPT exports, course notes, or existing chapter HTML examples. Use when Codex is asked to read courseware and produce Chinese/English learning mind maps, especially two variants: a coarse-grained 脉络大纲 version that follows chapter logic and a detailed 全量解析/细致版 version with page references, formulas, algorithms, examples, and exam review cues.
---

# Lecture Mindmap HTML

## Overview

Turn lecture materials into polished static HTML study maps. This skill now includes real HTML template assets. Treat them as the default source of truth for structure and CSS, not just inspiration. Produce either or both of these outputs:

- `第X章脉络大纲.html`: coarse outline, chapter logic, core questions, section cards, comparison table.
- `第X章.html`: detailed analysis, tree-style sections, page ranges, formulas, algorithms, examples, review warnings.

## Workflow

1. Inventory the workspace before writing.
   - Locate lecture files, existing mind-map HTML, output directory, and chapter numbering.
   - Prefer `rg`, `find`, `ls`, and `sed` for quick inspection.
   - If PDFs are involved, use available PDF tooling (`pypdf`, `pdfplumber`, `pdftotext`, or rendering tools) to extract titles, page counts, formulas, examples, and quiz/homework cues.

2. Read style sources in this order.
   - First read `assets/templates/coarse/` and `assets/templates/detailed/`.
   - Treat those HTML files as reusable templates and style anchors.
   - If the user also provides local sample HTML in the target project, prefer the user-provided sample only when they explicitly ask to match that project instead of the built-in style.
   - Read `references/style-patterns.md` before designing HTML structure or CSS.

3. Extract and organize content.
   - Read `references/content-extraction.md` before summarizing courseware.
   - Build a chapter-level spine first: topic progression, bottlenecks solved, and recurring exam ideas.
   - Then collect details: definitions, formulas, hardware structures, algorithm steps, examples, comparisons, and page ranges.

4. Generate HTML.
   - Keep output self-contained: inline CSS, no external CDN, no frontend framework unless the user asks.
   - Start from the closest built-in template asset instead of re-designing from scratch.
   - Preserve the template's CSS structure, spacing system, section anatomy, and comparison-table layout unless the user explicitly asks for a redesign.
   - Replace titles, subtitles, flow boxes, overview items, section cards, formulas, and chapter content with the new lecture material.
   - Match existing file naming unless the user specifies another convention.
   - Do not overwrite existing files unless explicitly asked; if updating, preserve unrelated content and style patterns.

5. Verify.
   - Run `scripts/check_html_structure.py` against generated HTML files.
   - Also inspect line counts and key headings when useful.
   - Fix missing structure, broken headings, obvious truncation, or mismatched style before delivery.

## Output Standards

- Write in Chinese by default while preserving important English technical terms from the slides.
- Do not merely copy slide bullets; synthesize the learning path and exam-oriented review handles.
- Prefer concrete formulas and symbolic forms where the slide uses them.
- Include page ranges in detailed versions when available.
- Use stable HTML/CSS that opens directly in a browser.
- Keep color palettes restrained and readable; avoid relying on images or network resources.
- For coarse outlines, prefer the built-in chapter 6 card-style family unless the user points to another coarse sample.
- For detailed outlines, prefer the built-in chapter 4/5 style family unless the user points to another detailed sample.
- When in doubt, copy a template asset and replace content rather than inventing new layout rules.

## Resource Guide

- `references/style-patterns.md`: visual and structural requirements for the two HTML variants.
- `references/content-extraction.md`: rules for extracting lecture content and turning it into study-map nodes.
- `scripts/check_html_structure.py`: read-only structural checker for generated HTML.
- `assets/templates/coarse/`: built-in coarse “脉络大纲” HTML examples from chapters 1-6.
- `assets/templates/detailed/`: built-in detailed HTML examples from chapters 1-5.
