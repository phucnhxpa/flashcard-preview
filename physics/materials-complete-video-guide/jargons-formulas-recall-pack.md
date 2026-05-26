---
title: "Physics Complete Video Lecture — Jargons, Formula Recall, and Flashcard Source"
source: "complete_video_lecture_physics_guide.md"
lessons: "Measurement/Density; Hooke/Stress/Strain/Young Modulus"
---

# Physics Complete Video Lecture — Recall Pack

This pack is built from the audited complete video lecture guide, then cross-checked against available Edexcel textbook/spec sources. It is not a replacement for the lecture guide; it is the fast-recall layer: jargons, formulas, traps, and prompts for spaced repetition.

Source status:

| Source | Status |
|---|---|
| Complete video lecture guide | Included as the primary source. |
| Raw video-analysis evidence | Represented through the audited lecture guide. |
| Edexcel Year 1 textbook markdown | Included for quantities/units, measurement uncertainty, fluids/density, solid materials, Hooke, stress/strain/Young modulus. |
| Edexcel IAL Physics specification | Included for Unit 1 Materials outcomes 23–32. |
| SaveMyExams Physics markdown | Not available locally: `physics/savemyexams/README.md` says no dedicated source found yet. |

## 1. Mental model of the two lessons

| Lesson | Core idea | What you must recall automatically | Main danger |
|---|---|---|---|
| Measurement and density | Density compares how much mass is packed into a given volume. Measurement questions are usually about choosing the right quantity, converting units, and using the correct geometry. | SI units, volume formula, density rearrangements, instrument resolution, practical uncertainty. | Treating cm, cm² and cm³ conversions as the same; forgetting to halve diameter; mixing mass with weight. |
| Hooke, springs and materials | Elastic materials obey predictable proportional rules only in a limited region. Stress/strain turn a specific force-extension result into a material property. | $$F=kx$$, graph gradient, area under graph, stress, strain, Young modulus, series/parallel spring reasoning. | Using formulae without checking the physical situation: series vs parallel, diameter vs radius, extension vs final length, stress vs pressure context. |

# 2. Jargon glossary

## 2.1 Measurement, units and practical skills

| Term | Student-friendly meaning | Exact physics meaning / notation | What it is NOT / trap | Lesson-specific recall cue |
|---|---|---|---|---|
| Physical quantity | Something measurable about an object or situation. | A property with a numerical value and a unit, e.g. mass $$m$$ in kg, force $$F$$ in N, volume $$V$$ in $$\mathrm{m^3}$$. | Not just a number: the unit tells you what kind of quantity it is. | Before substituting, name the quantity, symbol, unit, and whether it is SI. |
| SI unit | The standard unit system expected in most calculations. | Base/derived units such as kg, m, s, N, Pa, $$\mathrm{kg\,m^{-3}}$$. | Not every unit printed in the question is already SI. | Convert before substitution when final unit contains kg/m/s. |
| Prefix | A shorthand power-of-ten multiplier attached to a unit. | milli $$=10^{-3}$$, centi $$=10^{-2}$$, kilo $$=10^3$$. | Prefix conversion changes when squared or cubed. | $$1\,\mathrm{cm^3}=10^{-6}\,\mathrm{m^3}$$, not $$10^{-2}\,\mathrm{m^3}$$. |
| Resolution | The smallest change an instrument can display. | For analogue/digital instruments, the smallest scale division or displayed increment. | Not the same as accuracy; a high-resolution instrument can still be systematically wrong. | Micrometer/Vernier questions ask you to read the scale and state uncertainty. |
| Accuracy | Closeness to the true value. | Low systematic error means the mean reading is close to the accepted/true value. | Not the same as precision; repeated values can be precise but inaccurate. | Zero error damages accuracy. |
| Precision | How tightly repeated measurements agree. | Small spread/random uncertainty across repeats. | Not guaranteed by one neat-looking reading. | Repeat and average to improve precision. |
| Range | The span of values an instrument can measure. | Maximum measurable value minus minimum measurable value, or the operating interval. | Not the same as resolution. | Choose an instrument with both enough range and suitable resolution. |
| Zero error | A systematic offset when an instrument reads non-zero at true zero. | A correction must be applied to all readings. | Not random scatter; it shifts every reading in the same direction. | Check closed calipers/micrometer before measuring. |
| Percentage uncertainty | Uncertainty compared with the measured value. | $$\%\,\text{uncertainty}=\frac{\text{absolute uncertainty}}{\text{measured value}}\times100\%$$. | A small absolute uncertainty can still be a large percentage if the measured value is tiny. | Measure many sheets and divide to reduce percentage uncertainty. |

## 2.2 Density and fluids

| Term | Student-friendly meaning | Exact physics meaning / notation | What it is NOT / trap | Lesson-specific recall cue |
|---|---|---|---|---|
| Mass | How much matter an object contains. | Symbol $$m$$, SI unit kg. | Not weight; weight is a force $$mg$$ in newtons. | Density uses mass, not weight. |
| Volume | How much 3D space an object occupies. | Symbol $$V$$, SI unit $$\mathrm{m^3}$$. | Not area; do not use $$\mathrm{m^2}$$ in density. | Choose sphere/cylinder/cuboid/displacement method. |
| Density | How much mass is packed into each unit volume. | $$\rho=\frac{m}{V}$$, SI unit $$\mathrm{kg\,m^{-3}}$$. | Not heaviness by itself: a large low-density object can have more mass than a small high-density object. | Ask: same volume, which has more mass? Same mass, which has smaller volume? |
| Displacement method | Finding volume by the volume of water pushed out or risen. | For irregular solid, volume of object equals volume of displaced water if fully submerged and no air trapped. | Not valid if object floats partially unless adjusted; avoid trapped air/bubbles. | Use when geometry formula is not available. |
| Meniscus | Curved liquid surface in a measuring cylinder. | Read the bottom of the meniscus at eye level for water-like liquids. | Do not read from above/below: parallax error. | Eye level, bottom of curve. |
| Parallax error | Reading error from viewing a scale at an angle. | Apparent position shifts because eye is not perpendicular to scale. | Not a calculation mistake; it is observational. | Put eye level with the mark. |
| Sphere volume | Volume formula for a ball-like object. | $$V=\frac43\pi r^3$$. | If diameter is given, do not cube diameter as radius. | Diameter first becomes radius; then cube. |
| Unit density conversion | Converting density between common systems. | $$1\,\mathrm{g\,cm^{-3}}=1000\,\mathrm{kg\,m^{-3}}$$. | Do not multiply by only $$10^{-3}$$ from grams; volume conversion also matters. | Mass conversion and volume conversion fight: $$10^{-3}/10^{-6}=10^3$$. |

## 2.3 Hooke's law, springs and graphs

| Term | Student-friendly meaning | Exact physics meaning / notation | What it is NOT / trap | Lesson-specific recall cue |
|---|---|---|---|---|
| Force | A push or pull that can stretch/compress/change motion. | Symbol $$F$$, SI unit N. | Not mass; hanging mass creates force $$mg$$. | If a mass hangs from spring, convert to weight. |
| Extension | Increase in length caused by stretching. | $$x=L-L_0$$, SI unit m. | Not final length; always subtract original length. | Hooke uses extension, not total length. |
| Compression | Decrease in length caused by squeezing. | Magnitude of shortening relative to original length. | Not negative extension unless sign convention is explicit. | Same spring idea, opposite deformation. |
| Hooke's law | Force is proportional to extension in the elastic linear region. | $$F=kx$$ until the limit of proportionality. | Not true forever; it breaks when graph curves. | Straight line through origin means direct proportionality. |
| Spring constant | Stiffness of a spring. | $$k=F/x$$ or graph gradient $$\Delta F/\Delta x$$, unit $$\mathrm{N\,m^{-1}}$$. | Not the force itself; higher $$k$$ means more force for same extension. | Steeper force-extension line means stiffer spring. |
| Limit of proportionality | Point where force and extension stop being directly proportional. | End of straight-line Hooke region. | Not always the same as elastic limit in real material questions. | First point where graph stops being straight. |
| Elastic limit | Boundary beyond which the object will not return fully to original shape. | Permanent deformation begins if exceeded. | Not just the graph becoming curved; wording matters. | Elastic = returns; plastic = permanent. |
| Elastic strain energy | Energy stored when elastically stretched/compressed. | Area under force-extension graph; in Hooke region $$E_e=\frac12Fx=\frac12kx^2$$. | Do not use triangle formula if graph is curved unless approximating area section-by-section. | Area under the graph, not gradient. |
| Springs in series | Springs connected end-to-end. | Same force through each spring; total extension is sum of individual extensions; effective $$k$$ decreases. | Do not share the force between series springs. | Same pull passes through every spring, so extensions add. |
| Springs in parallel | Springs side-by-side supporting the same load. | Load is shared; effective stiffness increases. For identical springs, total $$k$$ doubles. | Do not add extensions; parallel springs stretch by the same extension. | More springs side-by-side = harder to stretch. |

## 2.4 Stress, strain and Young modulus

| Term | Student-friendly meaning | Exact physics meaning / notation | What it is NOT / trap | Lesson-specific recall cue |
|---|---|---|---|---|
| Cross-sectional area | The area of the cut face perpendicular to the force. | For circular wire, $$A=\pi r^2=\pi(d/2)^2$$. | Not $$\pi d^2$$. Using diameter as radius gives area four times too large. | Diameter must be halved before squaring. |
| Stress | Force spread over cross-sectional area. | $$\sigma=\frac{F}{A}$$, unit Pa or $$\mathrm{N\,m^{-2}}$$. | Same unit as pressure, but stress is internal loading in material. | Bigger force or smaller area means bigger stress. |
| Strain | Fractional extension compared with original length. | $$\varepsilon=\frac{x}{L}$$, no unit. | Not extension alone; same extension is more serious for a shorter wire. | Ratio: extension divided by original length. |
| Young modulus | Stiffness of the material, independent of sample size in elastic region. | $$E=\frac{\sigma}{\varepsilon}=\frac{FL}{Ax}$$, unit Pa. | Not the spring constant of one sample. Spring constant depends on geometry; Young modulus is material property. | Turn force-extension into stress-strain to compare materials. |
| Stress-strain graph | Material-level graph of loading response. | Gradient in linear region equals Young modulus. | Not the same axes as force-extension graph. | Force-extension = object; stress-strain = material. |
| Ultimate tensile stress | Maximum stress before breaking. | Peak stress on a stress-strain graph. | Not necessarily breaking stress if fracture occurs after the peak at lower stress. | Highest point of stress curve. |
| Brittle material | Material that breaks with little plastic deformation. | Small/no plastic region after elastic behaviour. | Not simply “weak”; brittle can be strong but not ductile. | Snaps rather than stretches. |
| Ductile material | Material that stretches plastically before breaking. | Significant plastic deformation region. | Not necessarily more stiff; stiffness is Young modulus. | Warns before breaking by stretching. |

# 3. Formula recall tables

## 3.1 Unit and conversion formulas

| Recall prompt | Formula / fact | Symbols and units | Use when | Trap |
|---|---|---|---|---|
| Convert mm to m | $$1\,\mathrm{mm}=10^{-3}\,\mathrm{m}$$ | length | Small lengths in spring/wire questions | Do not leave mm inside $$F=kx$$ or strain. |
| Convert cm to m | $$1\,\mathrm{cm}=10^{-2}\,\mathrm{m}$$ | length | Radii/diameters/lengths | If cubed, conversion becomes $$10^{-6}$$. |
| Convert cm³ to m³ | $$1\,\mathrm{cm^3}=10^{-6}\,\mathrm{m^3}$$ | volume | Density and displacement | Biggest density trap. |
| Convert g to kg | $$1\,\mathrm{g}=10^{-3}\,\mathrm{kg}$$ | mass | Density | Combine with volume conversion. |
| Convert litres to m³ | $$1\,\mathrm{L}=10^{-3}\,\mathrm{m^3}$$ | volume | Fluid/container questions | 1 mL = 1 cm³ = $$10^{-6}\,\mathrm{m^3}$$. |
| Convert g cm⁻³ to kg m⁻³ | $$1\,\mathrm{g\,cm^{-3}}=1000\,\mathrm{kg\,m^{-3}}$$ | density | Material density tables | Result should look much larger in SI. |

## 3.2 Geometry formulas used by the lessons

| Object / quantity | Formula | Trigger | Trap | Mental check |
|---|---|---|---|---|
| Cuboid volume | $$V=lwh$$ | Rectangular block | All lengths must be in same unit first. | Units cube. |
| Cylinder volume | $$V=\pi r^2h$$ | Tube, cylinder, measuring cylinder geometry | Use radius, not diameter. | Area times height. |
| Sphere volume | $$V=\frac43\pi r^3$$ | Ball, spherical drop/object | Diameter must be halved before cubing. | Cubing makes small radius errors huge. |
| Circular cross-sectional area | $$A=\pi r^2=\pi(d/2)^2$$ | Wire/cable/rod in stress questions | Not $$\pi d^2$$. | Area scales with square of diameter. |

## 3.3 Density formulas and rearrangements

| Target | Formula | Thought process | Common trap | Mini example cue |
|---|---|---|---|---|
| Density | $$\rho=\frac{m}{V}$$ | “Mass per unit volume”: divide mass by volume. | Using weight instead of mass; not converting volume. | Heavy-for-size means high density. |
| Mass | $$m=\rho V$$ | If each cubic metre has $$\rho$$ kg, multiply by volume. | Forgetting that density is already per volume. | Same density, double volume, double mass. |
| Volume | $$V=\frac{m}{\rho}$$ | For a fixed mass, denser material occupies less volume. | Rearranging upside-down. | Larger density gives smaller volume. |
| Percentage uncertainty | $$\frac{\Delta x}{x}\times100\%$$ | Compare absolute uncertainty with measured size. | Tiny measured value makes percentage large. | Measure more sheets / larger length. |

## 3.4 Hooke and spring formulas

| Situation | Formula | Meaning | Use when | Trap |
|---|---|---|---|---|
| Hooke law | $$F=kx$$ | Force proportional to extension. | Linear elastic spring region. | $$x$$ is extension, not final length. |
| Spring constant | $$k=F/x$$ | Stiffness: force needed per metre extension. | Given one force-extension pair. | Convert cm/mm to m. |
| Graph gradient | $$k=\Delta F/\Delta x$$ | Slope of force-extension graph. | Force-extension graph straight section. | Use two points from straight region. |
| Elastic energy | $$E_e=\frac12Fx$$ | Area of triangular region under straight force-extension graph. | Hooke region, final force $$F$$ and extension $$x$$. | Not rectangle $$Fx$$. |
| Elastic energy alternative | $$E_e=\frac12kx^2$$ | Substitute $$F=kx$$ into $$\frac12Fx$$. | Given $$k$$ and $$x$$. | Only linear region. |
| Series identical springs | $$x_{\text{total}}=x_1+x_2+\cdots$$; same $$F$$ | Each spring feels same force; extensions add. | End-to-end springs. | Do not split force. |
| Parallel identical springs | $$k_{\text{total}}=k_1+k_2+\cdots$$ | Springs share load; combined system stiffer. | Side-by-side load sharing. | Same extension, shared force. |

## 3.5 Materials formulas

| Target | Formula | Meaning | Use when | Trap |
|---|---|---|---|---|
| Stress | $$\sigma=\frac{F}{A}$$ | Force per cross-sectional area. | Wire/rod/cable under tension/compression. | Area must be $$\mathrm{m^2}$$. |
| Strain | $$\varepsilon=\frac{x}{L}$$ | Fractional extension. | Comparing extension to original length. | No unit; use original length, not final length. |
| Young modulus | $$E=\frac{\sigma}{\varepsilon}$$ | Material stiffness from stress-strain graph. | Linear elastic material region. | Gradient of stress-strain, not force-extension. |
| Young modulus combined | $$E=\frac{FL}{Ax}$$ | Substitute stress and strain. | Given force, length, area, extension. | Diameter-to-area and mm-to-m conversions. |
| Extension from Young modulus | $$x=\frac{FL}{AE}$$ | Rearranged combined formula. | Predict cable/wire extension. | Larger area or modulus gives smaller extension. |
| Force from stress | $$F=\sigma A$$ | Total load from stress and area. | Stress limit / breaking load. | Area in $$\mathrm{m^2}$$. |

# 4. Cross-topic mistake bank

| Mistake | Why it is tempting | Correct repair question | Correct habit |
|---|---|---|---|
| Using diameter as radius | The formula says circular object and the question gives diameter. | “Does the formula require $$r$$ or $$d$$?” | If diameter appears, write $$r=d/2$$ before any formula. |
| Treating cm³ like cm | Prefix memorised for length gets copied to volume. | “Is this length, area, or volume?” | Cube the length conversion for volume. |
| Using final length as extension | Spring length changes are described visually. | “What was the original length?” | Always write $$x=L-L_0$$. |
| Thinking series springs share force | Parallel intuition gets applied to end-to-end springs. | “Is the same pull transmitted through each spring?” | Series: same force, extensions add. Parallel: same extension, forces add. |
| Calling stress “pressure” without context | Both have unit Pa. | “Is the force acting in a fluid/contact context or internal material loading?” | Use stress for material deformation under load. |
| Forgetting strain is unitless | Extension has units so answer feels like metres. | “Am I dividing two lengths?” | Strain is a ratio, no unit. |
| Using $$\frac12kx^2$$ outside linear region | Formula is memorable. | “Is the graph straight through origin up to this point?” | If not linear, use area under graph. |

# 5. LLM flashcard generation spec

The multi-LLM flashcard pipeline should generate cards with these section tags:

1. Units and prior knowledge
2. Measurement practical skills
3. Density and volume reasoning
4. Hooke's law and graph interpretation
5. Springs in series and parallel
6. Stress, strain and Young modulus
7. Mistake diagnosis and exam wording
8. Short mental worked examples

Card quality rules:

- Questions must be standalone but not reveal the target answer.
- Answers should teach in short step-by-step explanation where reasoning is involved.
- Prefer conceptual recall over exact arithmetic.
- Use exact calculation only when the arithmetic is mentally light and captures a trap.
- Label Phuc-specific mistakes only when evidenced by the lecture guide; otherwise label as “common trap”.
- Do not include LLM chain-of-thought style text such as “hmm”, “let me think”, “actually”, or “perhaps”.
