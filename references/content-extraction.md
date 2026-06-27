# Content Extraction Guide

Use this reference when reading lecture slides and turning them into HTML mind maps.

## First Pass: Map the Materials

For each lecture file, collect:

- File name and inferred section number.
- Page count.
- Title slide and contents slide.
- Major headings by page.
- Quiz/homework pages.

For PDFs, prefer the best available extractor in this order when practical:

1. `pdftotext` / `pdfinfo` if installed.
2. Python libraries such as `pypdf` or `pdfplumber`.
3. Render selected pages to images only when layout or diagrams matter.

## Second Pass: Build the Chapter Spine

Before writing HTML, identify the chapter's story:

- What problem starts the chapter?
- What concepts or mechanisms are introduced to solve it?
- What tradeoffs repeat across the chapter?
- What does each later section improve, extend, or contrast with?

Examples of good spines:

- Arithmetic: representation -> adders -> multiplication/division -> floating point -> rounding/errors.
- Memory: addresses -> SRAM/DRAM -> hierarchy -> cache -> virtual memory -> disk.
- I/O: interface -> polling -> interrupts -> multi-device interrupts -> DMA.

## Detail Selection Rules

Always preserve:

- Definitions and vocabulary introduced by the slides.
- Formulas, bit-field layouts, address splits, and state-transition rules.
- Algorithm steps and hardware datapath/control steps.
- Tables of comparison, advantages/disadvantages, and design tradeoffs.
- Quiz points, homework hints, and repeated examples.

Compress or omit:

- Instructor email/title boilerplate.
- Repeated diagrams when the concept can be described once.
- Long raw binary tables unless needed for an algorithm example.
- Full slide text when a study-oriented summary is clearer.

## Page References

- Detailed HTML should include page ranges when available.
- Coarse HTML usually does not need page badges, but may mention lecture file sections.
- If page extraction is unreliable, use section file names or slide section names instead of inventing exact pages.

## Bilingual Handling

- Use Chinese explanations by default.
- Keep English terms that are likely tested or appear on slides: `Hit`, `Miss`, `Opcode`, `Effective Address`, `Booth Algorithm`, `TLB`, etc.
- Use code formatting for registers, instructions, fields, and equations: `PC`, `IR`, `EA`, `Load R2, LOC`.
