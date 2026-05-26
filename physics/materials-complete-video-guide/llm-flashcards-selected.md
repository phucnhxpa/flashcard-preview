# Physics Complete Video Lecture — Judge-Selected LLM Flashcards

Selected cards: 107

Source: augmented video lecture guide + Edexcel textbook/spec.

## Card 1

**Q:** Starting from the elastic strain energy $$E = \frac{1}{2} F \Delta L$$, derive the expression for energy density (energy per unit volume) for a material obeying Hooke's law, showing that it equals $$\frac{1}{2} \sigma \varepsilon$$. (3 steps)

**A:** - Step 1: Energy density is energy per unit volume. Volume is $$V = A \times L$$, so divide the energy equation by volume: $$\text{Energy Density} = \frac{1}{2} \frac{F \Delta L}{A L}$$.
- Step 2: Rearrange the terms to group force/area and extension/length: $$\text{Energy Density} = \frac{1}{2} \left( \frac{F}{A} \right) \left( \frac{\Delta L}{L} \right)$$.
- Step 3: Recognize that $$F/A$$ is stress ($$\sigma$$) and $$\Delta L / L$$ is strain ($$\varepsilon$$). Therefore, Energy Density = $$\frac{1}{2} \sigma \varepsilon$$.

_Judge source label: GLM 5.1 ①_

---

## Card 2

**Q:** Why is elastic strain energy $$\tfrac{1}{2}Fx$$ rather than $$Fx$$ for a Hooke's-law spring? (3 steps)

**A:** - Step 1: Work done by a *constant* force is $$W = Fx$$. But during stretching, the spring force isn't constant — it starts at zero (when the spring is unstretched) and grows linearly to $$F$$.
- Step 2: The *average* force during the stretch is $$(0 + F)/2 = F/2$$. So work done = average force × distance = $$\tfrac{1}{2}Fx$$.
- Step 3: Equivalently, the area under the linear $$F$$-vs-$$x$$ graph from $$0$$ to $$x$$ is a triangle with base $$x$$ and height $$F$$, area $$\tfrac{1}{2}Fx$$.

The factor of one-half always reflects "linearly varying from zero", whether for springs, kinetic energy ($$\tfrac{1}{2}mv^2$$), or capacitor energy ($$\tfrac{1}{2}CV^2$$).

_Judge source label: Opus 4.7 ②_

---

## Card 3

**Q:** In a Young's modulus experiment, why is a long wire (several metres) preferred over a short wire (a few centimetres)? Explain in terms of measurement uncertainty. (2 steps)

**A:** - Step 1: For a given force, a longer wire extends more (since $$\Delta L = FL/AE$$ and $$\Delta L \propto L$$). A larger extension is easier to measure accurately and has a lower percentage uncertainty.
- Step 2: If the wire is only a few centimetres long, the extension might be a fraction of a millimetre — comparable to the resolution of the measuring instrument. The percentage uncertainty in $$\Delta L$$ would be very large, making the calculated Young modulus unreliable.

Longer wire → larger extension → lower percentage uncertainty → more accurate $$E$$.

_Judge source label: GLM 5.1 ②_

---

## Card 4

**Q:** A force-extension graph for loading and unloading a metal wire in the elastic region shows the loading and unloading paths along the *same* straight line. For rubber, the paths are different (a hysteresis loop). What does this difference tell you about energy conservation in each material? (2 steps)

**A:** - Step 1: For the metal in the elastic region, the loading and unloading paths coincide. All the work done on the wire during loading is returned during unloading — energy is conserved. The material is perfectly elastic.
- Step 2: For rubber, the unloading path lies below the loading path. The area between them (the hysteresis loop) represents energy that is *not* returned — it is dissipated as heat within the material. Rubber is elastic (it returns to its original shape) but not *perfectly* elastic in the energy sense.

Elastic shape recovery ≠ elastic energy recovery. Rubber recovers its shape but loses energy as heat each cycle.

_Judge source label: GLM 5.1 ②_

---

## Card 5

**Q:** Why is "stress" sometimes called the "inverse" of pressure by students, and what's wrong with this thinking?

**A:** - Step 1: This phrasing presumably comes from imagining pressure as "pushing in" on a solid and stress as "pushing out". But mathematically and dimensionally, they are the same quantity — force per unit area — with the same units (Pa).
- Step 2: Tensile stress is a *pulling-apart* internal force per area in a stretched solid; compressive stress is a *pushing-together* internal force per area in a squeezed solid. Pressure (in fluids) is essentially compressive stress that acts in all directions.
- Step 3: So stress is more general (it includes tensile, compressive, and shear varieties with directional information), but it is *not* the inverse of pressure — both are force/area. The corrected mental model: "Stress is like pressure, but applied internally to solids with a definite direction".

_Judge source label: Opus 4.7 ①_

---

## Card 6

**Q:** Why is the area under a *stress–strain* graph "energy per unit volume" rather than total energy? (2 steps)

**A:** - Step 1: Area under a force–extension graph is energy: $$\int F \, dx$$ has units $$\mathrm{N\cdot m = J}$$. Dividing by the volume of the sample gives energy per unit volume.
- Step 2: Stress is $$F/A$$ (force per unit area) and strain is $$\Delta L/L$$ (extension per unit length). Their product $$\sigma\varepsilon = F\Delta L/(AL) = F\Delta L/V$$ has units of $$\mathrm{J\,m^{-3}}$$. So the area under a stress–strain plot, $$\int \sigma\, d\varepsilon$$, is automatically a *volumetric* energy density.

This is convenient because it makes toughness ($$\int \sigma\, d\varepsilon$$ up to fracture) a material property, not a sample property.

_Judge source label: Opus 4.7 ②_

---

## Card 7

**Q:** Why should strain values be quoted as decimals (e.g. $$3.0\times 10^{-4}$$) and not percentages in Edexcel mark schemes?

**A:** - Step 1: Strain entering formulas like $$E = \sigma/\varepsilon$$ or $$\sigma = E\varepsilon$$ must be the dimensionless ratio. If you substitute "$$0.03\%$$" as $$0.03$$, you're off by a factor of $$100$$.
- Step 2: Examiners want the decimal form to avoid that exact confusion. Writing $$\varepsilon = 3.0 \times 10^{-4}$$ is unambiguous; writing "0.03%" introduces a hidden conversion step.
- Step 3: Convention: keep strain as a decimal in calculations and in final answers; only convert to a percentage if the question explicitly asks.

The rule is operational: percentages multiply by an invisible factor of $$1/100$$, which causes silent errors.

_Judge source label: Opus 4.7 ②_

---

## Card 8

**Q:** What is the conceptual difference between the *limit of proportionality* and the *elastic limit*?

**A:** - Step 1: The limit of proportionality is the point on a force–extension graph where the line stops being straight — beyond it, $$F$$ is no longer proportional to $$x$$ (Hooke's law breaks down).
- Step 2: The elastic limit is the point beyond which the material no longer returns to its original shape when unloaded — permanent (plastic) deformation begins.
- Step 3: Between them lies a narrow region where deformation is still *elastic* (recoverable) but *not proportional* (the curve bends but the material still snaps back). So: limit of proportionality ≤ elastic limit. They are not synonyms.

_Judge source label: Opus 4.7 ①_

---

## Card 9

**Q:** Two identical springs each with constant $$k$$ are joined in series and a single weight is hung from the bottom. Why does the same force pass through *each* spring, and how does this make the chain "softer"? (3 steps)

**A:** - Step 1: In a vertical series chain, the bottom spring supports the weight, and the top spring supports the bottom spring (plus the weight). Since the springs themselves are taken as massless, the tension is uniform — every cross-section feels the same force $$F$$.
- Step 2: Each spring therefore extends by $$x=F/k$$ individually. The total chain extension is the sum: $$x_{total}=2F/k$$.
- Step 3: Effective stiffness: $$k_{eff}=F/x_{total}=k/2$$. The chain is "softer" (less stiff) because the same force produces double the extension — analogous to resistors in parallel where current finds two paths and resistance drops.

_Judge source label: Opus 4.7 ①_

---

## Card 10

**Q:** Why is checking for *zero error* on a digital instrument just as important as on an analogue one, even though digital displays "look more reliable"?

**A:** - Step 1: A digital display has high *resolution* (small smallest-readable change), but resolution and accuracy are not the same thing.
- Step 2: Internal calibration can drift due to wear, manufacturing tolerances, temperature, or battery voltage. A digital balance might read 0.02 g with nothing on it — this systematic offset contaminates every measurement.
- Step 3: Checking zero (no load, no contact) and either correcting in software or subtracting from every reading is essential. The polished appearance of digital instruments tricks people into assuming they're inherently accurate; they aren't.

_Judge source label: Opus 4.7 ①_

---

## Card 11

**Q:** Archimedes' principle states that the upthrust on an immersed object equals the weight of fluid displaced. A stone of mass 125 g is immersed in water and the spring balance reads 1.00 N. Is the upthrust equal to 1.00 N, or something else? Explain. (2 steps)

**A:** - Step 1: The weight of the stone is $$W = mg = 0.125 \times 9.81 \approx 1.23\,\text{N}$$. The spring balance reads 1.00 N, which is the *apparent weight* (weight minus upthrust).
- Step 2: Upthrust = weight − apparent weight = $$1.23 - 1.00 = 0.23\,\text{N}$$. This equals the weight of water displaced. The reading on the balance is NOT the upthrust — it is the reduced weight.

Spring balance reading = true weight − upthrust. To find upthrust, subtract the reading from the true weight.

_Judge source label: GLM 5.1 ②_

---

## Card 12

**Q:** Why is taking a graphical gradient generally more accurate than computing $$k$$ from a single force-extension pair? (3 steps)

**A:** - Step 1: A single pair of readings contains both random measurement errors and any zero-error offset baked into the apparatus.
- Step 2: A line of best fit through many points averages out random errors statistically. The gradient depends on differences, not absolute values, so a constant zero-error offset cancels out.
- Step 3: Moreover, the gradient method visibly reveals systematic deviations: a non-zero $$y$$-intercept signals zero error or systematic offset; curvature signals departure from Hooke's law. Single-point arithmetic hides both.

Graphs are diagnostic instruments, not just answer-getters.

_Judge source label: Opus 4.7 ②_

---

## Card 13

**Q:** Explain why plotting a graph to determine Young's modulus (or spring constant) is more accurate than using a single pair of force-extension readings. (2 steps)

**A:** - Step 1: A single reading is subject to random errors in both force and extension measurements. The gradient of a best-fit line through multiple points effectively averages out these random errors — individual outliers have limited influence.
- Step 2: A graph also reveals systematic errors (e.g., a non-zero intercept suggests a zero error or an initial extension) and shows whether the material obeys Hooke's law across the range (the line should be straight and pass through the origin).

A graph gives you: (1) averaging of random errors, (2) detection of systematic errors, and (3) verification of the linear model.

_Judge source label: GLM 5.1 ②_

---

## Card 14

**Q:** Why is measuring 10 sheets of paper and dividing by 10 better than measuring 1 sheet?

**A:** - Step 1: A single sheet is, say, 0.1 mm thick. A ruler with 1 mm resolution gives ~1000% percentage uncertainty — useless.
- Step 2: A stack of 10 sheets is ~1 mm thick. Same ruler now gives ~100% — still poor but already much better. A micrometer (0.01 mm) on 10 sheets gives ~1%.
- Step 3: Dividing by 10 at the end reduces the *measured* value while preserving the *absolute* uncertainty of the instrument. The percentage uncertainty in the final per-sheet thickness equals the percentage uncertainty in the stack measurement, which has been driven down by making the measurement larger. *Trick: enlarge the quantity to shrink the percentage uncertainty*.

_Judge source label: Opus 4.7 ①_

---

## Card 15

**Q:** Why is the equation $$\rho=m/V$$ called a *material* property rather than just a property of one specific object?

**A:** - Step 1: For any given substance under fixed conditions (temperature, pressure, phase), packing the molecules together gives a fixed mass per unit volume.
- Step 2: If you double the volume of pure water, you also double the mass — the ratio $$m/V$$ stays the same.
- Step 3: So density is intensive (independent of size of sample), and depends only on what the material *is*, not how much of it you have. This is why we can quote single values like "water = 1000 kg/m³" without specifying how much water.

_Judge source label: Opus 4.7 ①_

---

## Card 16

**Q:** A rubber band stretches very easily at first, then becomes very stiff before breaking. What's happening at the molecular level? (3 steps)

**A:** - Step 1: Natural rubber is a polymer — long tangled chains of carbon atoms held together by weak bonds between chains and stronger covalent bonds along the chain.
- Step 2: Initial stretching mostly *uncoils* and aligns the chains — easy, because it doesn't stretch covalent bonds, just rearranges them. So small force produces large extension.
- Step 3: Once chains are fully extended, further stretching requires stretching the actual covalent bonds along the backbone. These are stiff, so the rubber becomes very resistant — the curve bends upward sharply before breaking.

This is why rubber's force-extension curve is non-linear from the start — there's no Hooke region.

_Judge source label: Opus 4.7 ②_

---

## Card 17

**Q:** Young's modulus is defined as $$E = \sigma / \varepsilon$$. Derive the expanded form $$E = FL / (A\Delta L)$$ from the definitions of stress and strain, and explain why $$E$$ is a property of the *material* while $$k$$ is a property of the *object*. (3 steps)

**A:** - Step 1: Substitute the definitions: $$E = \frac{F/A}{\Delta L / L}$$.
- Step 2: Simplify the compound fraction: $$E = \frac{F}{A} \times \frac{L}{\Delta L} = \frac{FL}{A\Delta L}$$.
- Step 3: The spring constant $$k = F/\Delta L$$ depends on the object's dimensions (a longer wire extends more for the same force; a thicker wire extends less). Young's modulus divides out these dimensional effects by including $$L$$ and $$A$$, so it depends only on the material itself. Two wires of different sizes but the same material have the same $$E$$ but different $$k$$.

$$k$$ describes a specific object; $$E$$ describes a class of material.

_Judge source label: GLM 5.1 ②_

---

## Card 18

**Q:** Why is strain dimensionless, and what's the consequence for the units of Young modulus?

**A:** - Step 1: Strain is $$\varepsilon=\Delta L/L$$ — a ratio of two lengths. The metres cancel, leaving a pure number.
- Step 2: Young modulus $$E=\sigma/\varepsilon$$. Since strain is dimensionless, $$E$$ inherits the units of stress.
- Step 3: So $$E$$ has units of Pa (or N/m²), just like stress. Typical values are huge (steel ≈ $$2\times10^{11}\,\mathrm{Pa}$$) because strains are typically very small (e.g. $$10^{-3}$$ at modest loads), so dividing a modest stress by a tiny strain gives a giant number.

_Judge source label: Opus 4.7 ①_

---

## Card 19

**Q:** On a stress–strain graph, what physical quantity does the *area under the curve* represent, and why?

**A:** - Step 1: Stress = force/area, strain = extension/length. So stress × strain = (F × ΔL)/(A × L) = work done/volume.
- Step 2: The area under a stress–strain curve has units Pa × (dimensionless) = Pa = J/m³ — energy per unit volume.
- Step 3: Physically, this is the *elastic strain energy per unit volume* stored in the material at that strain. It's a measure of *toughness*: a tough material (like copper) has a large area under the curve before fracture; a brittle material (like glass) has a small one.

_Judge source label: Opus 4.7 ①_

---

## Card 20

**Q:** Estimate the mass of air in a 5 m × 4 m × 2.5 m room, using rough mental arithmetic. Why is this a good sanity-check exercise?

**A:** - Step 1: Volume ≈ 50 m³. Air density ≈ 1.2 kg/m³.
- Step 2: Mass ≈ 50 × 1.2 = 60 kg.
- Step 3: That's about the mass of one person! This surprises most people — air seems weightless, but in any sizeable enclosed space it's actually substantial. The exercise builds intuition: density values can be plugged into volume-mass conversions and immediately tested against everyday intuition (does the answer make sense?). Order-of-magnitude estimates are a powerful tool for catching arithmetic errors.

_Judge source label: Opus 4.7 ①_

---

## Card 21

**Q:** When measuring the density of an irregular object using a Eureka can, two potential errors are: (a) air bubbles sticking to the object when submerged, and (b) water adhering to the spout instead of flowing into the measuring cylinder. For each, state whether the measured density would be too high or too low, and why. (2 steps)

**A:** - Step 1: Air bubbles on the object displace extra water, so the measured volume is *larger* than the true volume. Since $$\rho = m/V$$, a larger $$V$$ gives a *smaller* density — the measured density is too low.
- Step 2: Water adhering to the spout means less water reaches the measuring cylinder, so the measured volume is *smaller* than the true volume. A smaller $$V$$ gives a *larger* density — the measured density is too high.

Air bubbles → volume too large → density too low. Water loss → volume too small → density too high. They push in opposite directions.

_Judge source label: GLM 5.1 ②_

---

## Card 22

**Q:** When a micrometer's jaws are fully closed, the thimble reads 0.03 mm instead of zero. Classify this zero error as positive or negative, state the correction rule, and give the actual reading when the observed reading is 5.47 mm. (3 steps)

**A:** - Step 1: When closed, the instrument reads 0.03 mm instead of 0. This means it reads *above* zero, so it is a **positive zero error** of $$+0.03\,\text{mm}$$.
- Step 2: The correction rule is: Actual Reading = Observed Reading − Zero Error.
- Step 3: Actual = $$5.47 - 0.03 = 5.44\,\text{mm}$$.

Positive zero error → subtract; negative zero error → add. The mnemonic: the correction always pushes the reading back toward what it *should* have been.

_Judge source label: GLM 5.1 ②_

---

## Card 23

**Q:** Why can't you just average the densities of copper and zinc, weighted by percentage, to get brass density when the percentages are by *mass* rather than by volume?

**A:** - Step 1: Density is mass-per-volume. If 70% of the mass is copper, that doesn't mean 70% of the volume is copper — because copper is denser, the same mass occupies less volume than the same mass of zinc.
- Step 2: To find total volume from a mass-fraction split, you compute $$V = m_{Cu}/\rho_{Cu} + m_{Zn}/\rho_{Zn}$$, then $$\rho = m_{\text{total}}/V$$.
- Step 3: That's a harmonic-style average, not arithmetic. So the rule is: by-volume mix → arithmetic mean weighted by volume fraction. By-mass mix → harmonic mean weighted by mass fraction.

The structure of the average depends on which quantity (mass or volume) you are partitioning.

_Judge source label: Opus 4.7 ②_

---

## Card 24

**Q:** Explain why a 0.01 mm error in radius calculation leads to a 0.03 mm error in volume for a sphere. (2 steps)

**A:** - Step 1: Volume V = (4/3)πr³ → V ∝ r³.  
- Step 2: A 1% radius error causes ~3% volume error (derivative dV/V = 3×dr/r via power rule).

_Judge source label: Qwen 3 ②_

---

## Card 25

**Q:** Distinguish *limit of proportionality*, *elastic limit*, and *yield point* on a force–extension curve.

**A:** - Step 1: Limit of proportionality: the largest extension for which $$F \propto x$$. Past this, the graph stops being a straight line — but the material may still spring back when unloaded.
- Step 2: Elastic limit: the largest extension after which the material *still* returns to its original length when unloaded. Just beyond this, permanent deformation begins.
- Step 3: Yield point: the load at which the material begins to deform plastically with little or no increase in force — the curve becomes nearly horizontal (or "jerky" for mild steel). Always: limit of proportionality ≤ elastic limit ≤ yield point.

The three landmarks describe progressively more severe departures from ideal elastic behaviour.

_Judge source label: Opus 4.7 ②_

---

## Card 26

**Q:** Why do you take repeated readings of a single measurement in a physics experiment, and what type of error does this address?

**A:** - Step 1: Random errors arise from unpredictable fluctuations: vibrations, slightly different reaction times, instrument noise. They scatter readings symmetrically around the true value.
- Step 2: Taking many readings and averaging causes the random fluctuations to partially cancel — the mean approaches the true value as $$\sqrt{N}$$ (statistical noise drops with more samples).
- Step 3: *Systematic* errors (e.g. miscalibrated instrument, zero error) are *not* reduced by averaging — they shift every reading the same way. Those require a different fix: calibration, zero correction, or improved method.

_Judge source label: Opus 4.7 ①_

---

## Card 27

**Q:** Why is Young modulus a more useful material descriptor than the spring constant $$k$$ for comparing, say, two steel cables of different sizes?

**A:** - Step 1: The spring constant $$k=F/x$$ depends on the geometry of the object: a thicker or shorter cable has a higher $$k$$ even if made of the same steel.
- Step 2: Young modulus normalises out the geometry: $$E=\frac{F/A}{\Delta L/L}=\frac{FL}{A\Delta L}$$. The cross-sectional area and original length are divided out.
- Step 3: Two cables made of identical steel will have *the same* $$E$$ (≈ 200 GPa) regardless of their thickness or length. So $$E$$ is a property of the *material*; $$k$$ is a property of the *object*. This is why textbooks tabulate $$E$$ for materials, not $$k$$.

_Judge source label: Opus 4.7 ①_

---

## Card 28

**Q:** A copper wire has area 0.30 cm² and brass has tensile strength 190 MPa. Why is the maximum *force* the wire can withstand simply $$\sigma \times A$$, and what assumption are you making? (3 steps)

**A:** - Step 1: Tensile strength = maximum stress before breaking. At the failure point, $$\sigma_{max}=F_{max}/A$$.
- Step 2: Rearranging: $$F_{max}=\sigma_{max}\times A=190\times 10^6\,\mathrm{Pa}\times 0.30\times 10^{-4}\,\mathrm{m^2}\approx 5700\,\mathrm{N}\approx 5.7\,\mathrm{kN}$$.
- Step 3: The assumption: the area $$A$$ refers to the *cross-sectional area in the direction of pulling*. For a wire, this is the round cross-section; for a beam under tension, the rectangular face. Mistakenly using the total surface area (e.g. for a square rod) gives nonsense. *Tensile* stress is force per cross-section, not per surface.

_Judge source label: Opus 4.7 ①_

---

## Card 29

**Q:** Why is air density (~$$1\,\mathrm{kg\,m^{-3}}$$) so much smaller than water density (~$$1000\,\mathrm{kg\,m^{-3}}$$), even though both are made of small molecules of similar mass?

**A:** - Step 1: In liquids, molecules are packed shoulder-to-shoulder, in continuous contact — molecular spacing is roughly the molecule size itself.
- Step 2: In gases at atmospheric pressure, molecules are typically ~10 molecular diameters apart in each dimension — so a 1000-fold smaller density (since spacing cubed gives volume).
- Step 3: Both have similar molecular *masses*, but the *volume* taken up per molecule is vastly different. Compressing a gas brings the molecules closer; once they touch, it becomes a liquid. The mass per unit volume ratio reflects how much empty space sits between molecules.

_Judge source label: Opus 4.7 ①_

---

## Card 30

**Q:** Identify which formula is needed: a question asks for *stress* given diameter, force, original length, and Young modulus. Is the Young modulus a red herring, and why?

**A:** - Step 1: Stress = F/A. Force is given. Area: from diameter, $$A=\pi(d/2)^2$$.
- Step 2: That's enough. Stress is directly $$F/(\pi d^2/4)$$. Original length and Young modulus don't enter.
- Step 3: Young modulus would be needed only if the question asked for *strain* or *extension*. Sometimes exam questions deliberately give extra information to test whether you can pick the relevant subset. Always identify what's asked, then trace the minimal formula path — don't try to use every given number.

_Judge source label: Opus 4.7 ①_

---

## Card 31

**Q:** Why measure the diameter of a wire at *several points and orientations* before computing the cross-sectional area?

**A:** - Step 1: Wires are not perfectly uniform — manufacturing leaves slight variations in thickness along the length, and the cross-section may be slightly elliptical rather than circular.
- Step 2: One reading at one orientation could be unrepresentative; if it's high, $$A$$ is overestimated and $$E$$ is underestimated (and vice versa).
- Step 3: Multiple readings at different positions and angles, then averaging, gives a best estimate of the typical diameter. Since $$A\propto d^2$$, any error in $$d$$ is *doubled* in $$A$$, making careful averaging especially important.

_Judge source label: Opus 4.7 ①_

---

## Card 32

**Q:** A mild steel wire and a high-carbon steel wire have the same Young modulus (~200 GPa). A student says "they must have the same strength." Is this correct? Explain. (2 steps)

**A:** - Step 1: Young modulus measures stiffness (resistance to elastic deformation), not strength (resistance to breaking). Two materials can have the same Young modulus but different breaking stresses.
- Step 2: High-carbon steel has a higher breaking stress (UTS) than mild steel — it is stronger. But mild steel has a much longer plastic region (it is tougher, absorbs more energy before breaking). High-carbon steel is more brittle — it fractures with little plastic deformation.

Stiffness (Young modulus), strength (UTS), and toughness (energy to fracture) are three distinct material properties. Do not confuse them.

_Judge source label: GLM 5.1 ③_

---

## Card 33

**Q:** What's the difference between *strength*, *stiffness*, and *toughness* as material properties?

**A:** - Step 1: Strength = maximum stress before fracture (or UTS). High-strength materials can carry large loads per unit area.
- Step 2: Stiffness = resistance to deformation under stress, quantified by Young's modulus. A stiff material has small strain for a given stress.
- Step 3: Toughness = total energy absorbed per unit volume before fracture (area under stress–strain curve). A tough material can absorb impacts; a brittle one cannot.
+ Diamond: stiff and hard but brittle (low toughness).
+ Rubber: low stiffness but very tough — absorbs huge energy through large strains.
+ Mild steel: stiff, strong, AND tough — why it's an excellent structural material.

The three are independent — a material can be strong but not tough (high-carbon steel), or tough but not strong (rubber).

_Judge source label: Opus 4.7 ②_

---

## Card 34

**Q:** What's the difference between *accuracy* and *precision*, and why can a measurement be precise but inaccurate?

**A:** - Step 1: Accuracy is closeness to the *true value*. A measurement is accurate if it's near what it ought to be.
- Step 2: Precision is repeatability — how closely repeated measurements *agree with each other*, regardless of whether they're correct.
- Step 3: An archer who consistently hits the same wrong spot is precise but inaccurate (a systematic error). One who scatters hits widely around the bull is accurate on average but imprecise (random error). A good experiment aims for both: low scatter (precision) *and* the right value (accuracy). Improving averaging fixes precision; calibration fixes accuracy.

_Judge source label: Opus 4.7 ①_

---

## Card 35

**Q:** Distinguish *resolution*, *accuracy*, *precision*, and *range* of a measuring instrument — and explain why high precision does not imply high accuracy.

**A:** - Step 1: Resolution = smallest detectable change (e.g. $$0.01\,\mathrm{mm}$$ on a micrometer). Range = max − min the instrument can read.
- Step 2: Accuracy = closeness of measurement to the true value. Precision = closeness of repeated measurements to *each other*.
- Step 3: A faulty-calibrated instrument (e.g. micrometer with a zero error of $$+0.05\,\mathrm{mm}$$) can give very consistent readings that are all systematically wrong. That is high precision, low accuracy.
+ Random errors hurt precision.
+ Systematic errors hurt accuracy.

The archer analogy: tight grouping in the wrong place = precise but inaccurate.

_Judge source label: Opus 4.7 ②_

---

## Card 36

**Q:** Two identical springs of constant $$k$$ are joined end-to-end (in series) and a weight is hung from the bottom. Why is the combined spring constant $$k/2$$, not $$2k$$? (3 steps)

**A:** - Step 1: The same force $$F$$ passes through both springs (each spring must support the entire load). Each spring extends by $$x_1 = F/k$$.
- Step 2: Total extension = $$x_1 + x_2 = 2F/k$$. So the effective spring constant is $$k_{\text{eff}} = F/(2F/k) = k/2$$.
- Step 3: Physical picture: in series the springs each contribute their full extension, so the combination extends twice as much for the same force — it's *less* stiff.

Series springs are like resistors in parallel: more units in line → easier to deform overall.

_Judge source label: Opus 4.7 ②_

---

## Card 37

**Q:** Why is the area under a *stress–strain* curve called the "elastic strain energy per unit volume", and why is this preferable to the area under a force–extension curve when comparing materials? (3 steps)

**A:** - Step 1: Force–extension area gives total energy (in joules) — but this depends on the *sample size*. A long, thick steel bar stores more energy than a short, thin one, even though both are made of identical steel.
- Step 2: Dividing energy by sample volume gives energy density (J/m³). Mathematically, stress × strain = (F/A)(ΔL/L) = (F × ΔL)/(A × L) = work/volume.
- Step 3: So area under stress–strain curve is a *material property*: it depends only on what the material is, not how much you have. This lets you fairly compare toughness across different sample sizes and shapes.

_Judge source label: Opus 4.7 ①_

---

## Card 38

**Q:** Why does pre-straining steel rails before laying them in cold weather prevent damage later?

**A:** - Step 1: Steel expands when heated and contracts when cooled. If rails are laid relaxed in cold weather, summer heat would make them expand and buckle (compressive stress, sideways deformation).
- Step 2: Pre-straining means stretching the rails first (putting them under tension), then fixing them in place. As temperature rises, the rails *try* to expand — instead they just relieve the tension.
- Step 3: If summer heat is hot enough to relieve all the tension, the rails are merely unstressed (no buckling). The engineer picks a pre-strain matched to the expected temperature rise, so the rails sit somewhere between modest tension (cool weather) and zero stress (hottest expected day), never reaching damaging compression.

_Judge source label: Opus 4.7 ①_

---

## Card 39

**Q:** Brass is 70% copper and 30% zinc *by volume*. Without doing the arithmetic, explain why the brass density must lie between the copper and zinc densities, and closer to which one.

**A:** - Step 1: For a mixture combined by volume, total mass = $$\rho_{Cu}V_{Cu} + \rho_{Zn}V_{Zn}$$, and total volume = $$V_{Cu} + V_{Zn}$$.
- Step 2: The mixture density $$\rho_{\text{brass}} = (\rho_{Cu}V_{Cu} + \rho_{Zn}V_{Zn})/V_{\text{total}}$$ is a *volume-weighted average* of the component densities.
- Step 3: Any weighted average lies between the two extremes, with the result pulled toward whichever component has the larger weight. Since copper takes the larger volume share (70%), $$\rho_{\text{brass}}$$ lies closer to $$\rho_{Cu}$$.

The conceptual point: by-volume mixing → volume-weighted density; by-mass mixing would give a different formula and weighting.

_Judge source label: Opus 4.7 ②_

---

## Card 40

**Q:** Explain the difference between elastic deformation and plastic deformation. What happens at the molecular level in each case? (2 steps)

**A:** - Step 1: In **elastic deformation**, the atoms are displaced from their equilibrium positions but the bonds are only stretched/compressed, not broken. When the force is removed, the interatomic forces pull the atoms back to their original positions — the material recovers its shape completely.
- Step 2: In **plastic deformation**, the applied stress is large enough that layers of atoms slide past each other. Bonds are broken and reformed in new positions. When the force is removed, there are no restoring forces to return the atoms to their original arrangement — the deformation is permanent.

Elastic = bonds stretched (reversible). Plastic = bonds broken and reformed (irreversible).

_Judge source label: GLM 5.1 ②_

---

## Card 41

**Q:** In the formula $$p = h\rho g$$ for fluid pressure, explain what each variable represents and why this formula does *not* work accurately for the Earth's atmosphere over large height differences. (2 steps)

**A:** - Step 1: $$p$$ = pressure at depth $$h$$ in a fluid of density $$\rho$$, where $$g$$ is gravitational field strength. The formula assumes the fluid density $$\rho$$ is constant throughout the column.
- Step 2: For the atmosphere, air is compressible — it is denser at lower altitudes and much less dense at higher altitudes. So $$\rho$$ is not constant with height, and the formula overestimates the height of the atmosphere if you use sea-level density. You would need to use an average density, which is only an approximation.

Liquids are nearly incompressible ($$\rho \approx$$ constant), so $$p = h\rho g$$ works well. Gases are compressible, so it doesn't.

_Judge source label: GLM 5.1 ②_

---

## Card 42

**Q:** A copper wire of length $$1.52\,\mathrm{m}$$ stretches by $$3.2\,\mathrm{mm}$$ under tension. Why is it *impossible* to find the stress from this information alone?

**A:** - Step 1: With these numbers, you can compute strain: $$\varepsilon = 0.0032/1.52 \approx 2.1\times 10^{-3}$$.
- Step 2: But stress is $$\sigma = F/A$$ — you need either the applied force *and* the cross-sectional area, or the Young modulus (so you could use $$\sigma = E\varepsilon$$).
- Step 3: The wire's dimensions and extension alone give strain, but the relationship between strain and stress depends on the *material* (via $$E$$) and on the actual *load* — neither of which is provided.

The exam-skill point: identify what you can and can't compute, and explicitly state what's missing rather than forcing a formula.

_Judge source label: Opus 4.7 ②_

---

## Card 43

**Q:** If a material does *not* obey Hooke's law, why can't you use $$E = \frac{1}{2} k x^2$$ to find the strain energy? How should you find it instead? (2 steps)

**A:** - Step 1: The formula $$E = \frac{1}{2} k x^2$$ relies on the assumption that the force-extension graph is a perfect straight line (a triangle), so the average force is exactly half the maximum. For a non-linear material, the average force is *not* half the maximum.
- Step 2: You must find the area under the force-extension curve directly. This can be done by counting squares on the graph paper or by estimating the area using geometric shapes (trapezoids, etc.).

_Judge source label: GLM 5.1 ①_

---

## Card 44

**Q:** If you're given the *diameter* of a wire and need the cross-sectional area, why is using $$\pi d^2$$ a serious error, and by what factor does it skew the answer?

**A:** - Step 1: The correct area of a circle is $$A=\pi r^2$$ where $$r=d/2$$.
- Step 2: Substituting: $$A=\pi(d/2)^2=\pi d^2/4$$.
- Step 3: Using $$\pi d^2$$ gives an area $$4\times$$ too large. Consequences cascade:
+ Stress $$\sigma=F/A$$ comes out $$4\times$$ too small.
+ Extension $$\Delta L=FL/(AE)$$ comes out $$4\times$$ too small.
+ Required Young modulus comes out $$4\times$$ too small.

The mantra: *halve first, then square*.

_Judge source label: Opus 4.7 ①_

---

## Card 45

**Q:** Water has density $$1000\,\mathrm{kg\,m^{-3}}$$ and air has density about $$1.2\,\mathrm{kg\,m^{-3}}$$. Without a calculator, roughly how many times denser is water than air, and what does that tell you intuitively?

**A:** - Step 1: Ratio is $$1000/1.2 \approx 830$$ — water is nearly a thousand times denser.
- Step 2: This means a cubic metre of water has the same mass as about 800 cubic metres of air. Equivalently, the air in a small room ($$\sim 50\,\mathrm{m^3}$$) weighs about the same as $$\sim 60\,\mathrm{kg}$$ — about one person.
- Step 3: This is why upthrust in air is usually negligible for solids, but upthrust in water can support boats, fish and divers.

The factor of $$\sim 10^3$$ between liquids and gases governs why fluids behave so differently.

_Judge source label: Opus 4.7 ②_

---

## Card 46

**Q:** A ship floats deeper in warm fresh water than in cold salt water. Explain this using the concept of upthrust and density. (2 steps)

**A:** - Step 1: For the ship to float, upthrust must equal the ship's weight. Upthrust = weight of displaced fluid = $$V_{\text{displaced}} \times \rho_{\text{fluid}} \times g$$.
- Step 2: Warm fresh water is less dense than cold salt water (fresh water has no dissolved salt; warm water expands). Since $$\rho_{\text{fluid}}$$ is smaller, the ship must displace a *larger volume* $$V_{\text{displaced}}$$ to generate the same upthrust. Hence it sits deeper in the water.

Lower fluid density → must displace more volume → ship sits lower. This is the principle behind Plimsoll lines on ships.

_Judge source label: GLM 5.1 ②_

---

## Card 47

**Q:** A copper wire and a steel wire have identical diameters and lengths. The same load is hung from each. Which extends more, and what determines the ratio of extensions?

**A:** - Step 1: From $$\Delta L=FL/(AE)$$, when $$F$$, $$L$$, and $$A$$ are identical, extension is inversely proportional to Young modulus.
- Step 2: Steel has $$E\approx 200\,\mathrm{GPa}$$; copper has $$E\approx 120\,\mathrm{GPa}$$. So copper has lower E → copper extends more.
- Step 3: Ratio of extensions: $$\Delta L_{Cu}/\Delta L_{steel}=E_{steel}/E_{Cu}\approx 200/120\approx 1.7$$. Copper extends about 70% more than steel under the same load. This is a direct test of the geometry-free meaning of $$E$$ as a material property.

_Judge source label: Opus 4.7 ①_

---

## Card 48

**Q:** What's the difference in the *underlying microscopic picture* between elastic deformation in a metal and elastic deformation in a polymer like rubber?

**A:** - Step 1: In a metal, elastic deformation stretches inter-atomic bonds — atoms move slightly off their equilibrium lattice positions. The restoring force comes from electron-cloud repulsion and attraction between charged ions. This is why $$E$$ is high and the relationship is linear.
- Step 2: In rubber, elastic deformation is mostly *configurational* — long polymer chains uncoil and rearrange. The "restoring force" comes from entropy, not from bond-stretching: a tangled state is more probable than a stretched state, so when released the chains spontaneously return to a coiled mess.
- Step 3: That's why metals have linear elasticity with high $$E$$, and rubbers have nonlinear, low-$$E$$, but enormous-strain elasticity.

Bond elasticity vs entropic elasticity — completely different physics, both called "elastic".

_Judge source label: Opus 4.7 ②_

---

## Card 49

**Q:** For an irregular object like a stone, why does Archimedes' displacement method give you the *volume* of the stone directly, and what are the dominant sources of error in this method?

**A:** - Step 1: An incompressible solid pushes water out of the way. The water that's displaced must occupy a volume equal to the part of the object below the water line — and for a fully submerged object, that equals the object's full volume.
- Step 2: So if you collect or measure the displaced water in a graduated cylinder, you read off the volume of the stone without ever needing geometry.
- Step 3: Dominant errors:
+ Water adhering to the string or stone — lost from the measurement, underestimating volume.
+ Trapped air bubbles on the stone — *added* volume, overestimating.
+ Splashing — water lost, underestimating.
+ Meniscus reading on the cylinder — parallax.

The technique trades geometry for displacement, but the trade-off is many small handling errors that compound.

_Judge source label: Opus 4.7 ②_

---

## Card 50

**Q:** If you mix equal masses of two liquids with densities $$\rho_1$$ and $$\rho_2$$, is the final density simply their average $$(\rho_1 + \rho_2)/2$$? Explain why or why not. (2 steps)

**A:** - Step 1: No, the final density is not the simple average. Density is mass divided by volume. When you mix equal masses, the total mass is $$2m$$, but the total volume is $$m/\rho_1 + m/\rho_2$$.
- Step 2: The final density is $$\rho_{mix} = 2m / (m/\rho_1 + m/\rho_2) = 2 / (1/\rho_1 + 1/\rho_2)$$. This is the harmonic mean, not the arithmetic mean, and it will always be lower than the simple average unless the densities are identical.

_Judge source label: GLM 5.1 ①_

---

## Card 51

**Q:** Stress and pressure both have units of pascals. What's the conceptual difference, and why don't we just call them the same thing?

**A:** - Step 1: Pressure is force per unit area applied externally by a fluid, acting perpendicular to a surface and in all directions equally (isotropic).
- Step 2: Tensile/compressive stress is the *internal* force per unit area within a solid that resists deformation; it has a definite direction (along the axis of pulling/pushing) and can be tensile (pulling apart) or compressive (pushing together).
- Step 3: They share units because both are force/area, but the *physical situation* differs: pressure is what a fluid exerts on a wall; stress is what particles inside a stretched solid exert on each other to resist further stretching.

_Judge source label: Opus 4.7 ①_

---

## Card 52

**Q:** Why does a rubber band's force–extension graph have a peculiar shape: very easy to stretch at first, then suddenly stiff near the end?

**A:** - Step 1: Rubber is a polymer — long, tangled molecular chains.
- Step 2: For small forces, the molecules simply *untangle* — small force, big extension, because no strong bonds are being stretched.
- Step 3: Once all the chains are aligned and fully extended, further stretching means stretching the *covalent bonds within the chains* — much stronger. Small extra extension requires huge extra force, so the graph turns sharply upward. This explains why rubber can stretch to several times its original length but then suddenly becomes very stiff just before breaking.

_Judge source label: Opus 4.7 ①_

---

## Card 53

**Q:** Why does a digital micrometer read 0.01 mm, while a Vernier caliper typically reads 0.05 mm? What design feature gives each its resolution? (3 steps)

**A:** - Step 1: A micrometer uses a fine-pitch screw thread (typically 0.5 mm per turn). The thimble around it has 50 divisions, so each division = 0.5/50 = 0.01 mm.
- Step 2: A Vernier caliper uses an auxiliary scale that's slightly mismatched with the main scale. A 20-division Vernier scale spans 19 main-scale millimetres, so each Vernier division differs from a main-scale millimetre by 1/20 = 0.05 mm. The "match" between Vernier and main lines pinpoints the fractional reading.
- Step 3: Micrometers achieve finer resolution because amplifying small motions through mechanical gearing (the thread) is more precise than visual interpolation between scale marks. Both are far better than a 1 mm ruler.

_Judge source label: Opus 4.7 ①_

---

## Card 54

**Q:** Why does a method involving displacement in a Eureka can work for measuring the volume of irregular solids?

**A:** - Step 1: By Archimedes' principle, a fully submerged object displaces a volume of water exactly equal to its own volume.
- Step 2: The Eureka can is pre-filled to the spout level, so any extra water added (by the object) overflows into a measuring cylinder.
- Step 3: Reading the volume of overflow directly gives the object's volume, no matter how irregular its shape. This sidesteps the impossibility of using geometric formulas for an irregular object.

_Judge source label: Opus 4.7 ①_

---

## Card 55

**Q:** On a stress–strain graph for mild steel, what physical events do these features correspond to: linear region, yield point, "necking", fracture? (4 steps)

**A:** - Step 1: Linear region — bonds between atoms behave like springs. Atoms move slightly from equilibrium positions; everything is reversible. Slope = $$E$$.
- Step 2: Yield point — sudden drop or plateau in the curve. Layers of atoms begin to slip past each other along dislocations. No further force needed to keep extending.
- Step 3: Strain hardening / further extension — dislocations multiply and get tangled, making further plastic flow harder, so stress rises again toward the UTS (ultimate tensile stress).
- Step 4: After UTS — local cross-section narrows ("necks"), so true stress in that thin region rises rapidly until the wire fractures.

Each kink on the curve maps onto a specific microscopic event in the atomic lattice.

_Judge source label: Opus 4.7 ②_

---

## Card 56

**Q:** A steel rail is "pre-strained" to a strain of $$3.0 \times 10^{-4}$$ when laid at 8°C. The thermal strain per kelvin rise is $$2.5 \times 10^{-5}\,\mathrm{K^{-1}}$$. At what temperature does the rail become unstressed, and why? (2 steps)

**A:** - Step 1: The rail becomes unstressed when thermal expansion exactly cancels the pre-strain. Temperature rise needed: $$\Delta T = \frac{\varepsilon_{pre}}{\text{strain per K}} = \frac{3.0 \times 10^{-4}}{2.5 \times 10^{-5}} = 12\,\mathrm{K}$$.
- Step 2: The temperature at which the rail is unstressed = laying temperature + $$\Delta T$$ = $$8 + 12 = 20°\mathrm{C}$$. Below this temperature, the rail is in tension (it wants to contract but is held in place); above this temperature, it is in compression (it wants to expand but is held in place).

Pre-straining prevents buckling in hot weather by keeping the rail in tension at lower temperatures.

_Judge source label: GLM 5.1 ③_

---

## Card 57

**Q:** Why does a balloon contain air slightly *denser* than atmospheric air, even at the same temperature?

**A:** - Step 1: A balloon's elastic skin pushes inward, so the gas inside must push outward with extra pressure to balance it. Therefore $$P_{\text{inside}} > P_{\text{atm}}$$.
- Step 2: From the ideal gas behaviour ($$PV = nRT$$), at fixed $$T$$ and $$V$$, more pressure means more moles of gas packed into the same volume.
- Step 3: More molecules of (roughly) the same average mass per molecule, in the same volume, means greater density.

The balloon skin is the mechanism: it stores elastic energy and forces a pressure differential, which forces a density differential.

_Judge source label: Opus 4.7 ②_

---

## Card 58

**Q:** Two identical springs of constant $$k$$ are joined in parallel supporting a single weight via a rigid bar. Why does the effective stiffness *double*?

**A:** - Step 1: Both springs are constrained to extend by the same amount $$x$$ (the rigid bar moves down by $$x$$, dragging both equally).
- Step 2: Each spring then exerts an upward force $$kx$$ on the bar, and they share the load: total upward force $$F=2kx$$.
- Step 3: Effective stiffness $$k_{eff}=F/x=2k$$. Each spring carries only half the applied weight, so for a given force the system extends only half as much — stiffer overall. Analogous to resistors in series.

_Judge source label: Opus 4.7 ①_

---

## Card 59

**Q:** Why do we say upthrust = weight of fluid *displaced* (not weight of fluid *above* or *around* the object)?

**A:** - Step 1: Upthrust is the net upward force from fluid pressure differences. Pressure increases with depth: $$p=h\rho g$$.
- Step 2: The bottom face of a submerged object is deeper than its top, so the bottom experiences higher pressure → larger upward force than the downward force on the top.
- Step 3: Doing the geometry for any shape, the net upward force equals the weight of fluid that *would* occupy the object's volume — i.e., the displaced fluid. Archimedes' principle is a direct consequence of pressure varying with depth.

_Judge source label: Opus 4.7 ①_

---

## Card 60

**Q:** Why does the area under a force–extension graph give the elastic strain energy stored in a spring? (3 steps)

**A:** - Step 1: Work done by a variable force is $$W=\int F\,dx$$ — geometrically, the area under the F–x curve.
- Step 2: As you stretch the spring, the force *increases* from 0 to $$F$$, so the *average* force during stretching is $$F/2$$ (for a linear Hooke region). Work done = average force × distance = $$\frac12 Fx$$.
- Step 3: This work is stored in the spring as elastic potential energy (no friction, no plastic flow). For a Hooke-law spring, $$E=\frac12 Fx=\frac12 kx^2$$.

If the graph is non-linear (e.g. rubber), $$\frac12 Fx$$ overestimates; you must actually count the area under the curve.

_Judge source label: Opus 4.7 ①_

---

## Card 61

**Q:** What's the role of plotting a graph in reducing the effect of measurement errors during a Young modulus or Hooke's law experiment?

**A:** - Step 1: A single F/x pair has whatever uncertainty its individual readings carry. The graph plots many such points.
- Step 2: A best-fit straight line through scattered points effectively *averages* all the data — random scatter above and below the line cancels.
- Step 3: A systematic error (e.g. wrong zero) shifts all points by the same amount, but the *gradient* (which gives $$k$$ or $$E$$) is unaffected — only the intercept shifts. So the graph both reduces random error (via averaging) and reveals systematic error (via a non-zero intercept where one is expected).

_Judge source label: Opus 4.7 ①_

---

## Card 62

**Q:** In a force–extension experiment using a stretched copper wire, why is it advisable to use a long wire (e.g. 2–3 m) rather than a short one?

**A:** - Step 1: For a given force, extension scales with original length: $$\Delta L=FL/(AE)$$.
- Step 2: A longer wire produces a larger absolute extension for the same load, which means the extension reading has lower percentage uncertainty (the millimetre-scale ruling on the rule is the same, but the measurement is bigger).
- Step 3: A short wire gives extensions of a fraction of a millimetre — within the noise of the measuring instrument. Long wire → bigger signal → better precision.

_Judge source label: Opus 4.7 ①_

---

## Card 63

**Q:** Why does a hot-air balloon rise when first inflated, and what changes when it reaches a stable altitude? (3 steps)

**A:** - Step 1: Heating the air inside the balloon reduces its density (same mass, larger volume). The cooler, denser surrounding air provides an upthrust equal to the weight of displaced surrounding air.
- Step 2: When upthrust > total weight (balloon fabric + hot air + payload), there's a net upward force → the balloon accelerates upward.
- Step 3: As the balloon rises, surrounding air gets less dense (lower atmospheric pressure), reducing upthrust. The balloon reaches a *floating equilibrium* when upthrust just equals total weight. From there, it neither rises nor sinks (until further heating or cooling shifts the balance).

_Judge source label: Opus 4.7 ①_

---

## Card 64

**Q:** When you remove the load from a copper wire in the plastic region and then reload it, the wire behaves elastically again — almost the same stiffness as before, just from a new "natural length". Why?

**A:** - Step 1: Plastic deformation has rearranged the atoms — dislocations have moved and the lattice is now in a new equilibrium configuration. Strain hardening has often made the wire stiffer than before in the new range.
- Step 2: Unloading from the plastic region leaves the wire at a new permanent length, but the bonds between atoms still behave elastically for small further deformations.
- Step 3: So reloading retraces a linear path with approximately the same Young's modulus, but starting from the new length — the unloading line is parallel to the original elastic line.

This is exactly why metal panels can be pressed into permanent shapes and yet still behave elastically afterward — engineers exploit this in sheet metal forming.

_Judge source label: Opus 4.7 ②_

---

## Card 65

**Q:** A mild steel rail must be analysed for stress and strain. If you only have the rail's length, breadth, height, and load, but not its Young modulus, can you calculate stress? Can you calculate strain?

**A:** - Step 1: Stress is force per cross-sectional area: $$\sigma=F/A$$. You have force (the load × g) and area (from breadth × height). So stress is calculable.
- Step 2: Strain is extension per length: $$\varepsilon=\Delta L/L$$. You have $$L$$ but not $$\Delta L$$ unless it's also given.
- Step 3: Without $$\Delta L$$ or $$E$$ (to compute $$\varepsilon=\sigma/E$$), strain isn't calculable. The crucial lesson: identify which formulas need which inputs *before* trying to plug numbers. Many "impossible" problems become possible when you spot what additional measurement is needed.

_Judge source label: Opus 4.7 ①_

---

## Card 66

**Q:** The specification uses the symbol $$\Delta F = k\Delta x$$ rather than $$F = kx$$. Explain why the $$\Delta$$ notation is used, and what would go wrong if you confused total length with extension. (2 steps)

**A:** - Step 1: The $$\Delta$$ symbols emphasise that it is the *change* in force and the *change* in extension that are proportional. This is important because the spring might already be under some initial tension — the formula still applies to *additional* force and *additional* extension.
- Step 2: If you confuse total length $$L$$ with extension $$\Delta x$$ and write $$F = kL$$, you are saying the force depends on how long the spring is, not on how much it has stretched. A spring at its natural length with no force on it would give $$F = k \times L_{\text{natural}} \neq 0$$, which is clearly wrong.

$$\Delta$$ means "change in." Extension is always measured from the natural (unstretched) length.

_Judge source label: GLM 5.1 ②_

---

## Card 67

**Q:** A plank supported at both ends sags 4 mm when a 55 kg child stands in the middle. Why must you convert mass to weight first before using $$k=F/x$$?

**A:** - Step 1: Hooke's law links *force* (not mass) to extension. Force on the plank from the child equals the child's weight, not mass.
- Step 2: Weight $$F=mg=55\times 9.81\approx 540\,\mathrm{N}$$.
- Step 3: Then $$k=F/x=540/0.004\approx 1.4\times 10^5\,\mathrm{N\,m^{-1}}$$. Skipping the $$g$$ factor and using $$k=55/0.004$$ would give a number ~10× too small — a common slip when the question mentions mass rather than weight.

_Judge source label: Opus 4.7 ①_

---

## Card 68

**Q:** Why must you wear safety glasses when stretching wires or springs in a lab?

**A:** - Step 1: Wires under tension can store substantial elastic energy ($$\tfrac{1}{2}F\Delta L$$). For a thin wire stretched to several Newtons of tension and millimetres of extension, that's joules of stored energy.
- Step 2: When the wire snaps, the stored energy is released suddenly, propelling the broken ends at high speed.
- Step 3: The path of the snap is unpredictable; even a thin wire can lacerate or, more dangerously, penetrate the eye. Safety glasses are non-negotiable. A sand tray under any hanging masses protects feet from falling weights — a separate but parallel concern.

Energy stored = energy that will be released somewhere when something fails.

_Judge source label: Opus 4.7 ②_

---

## Card 69

**Q:** When measuring the diameter of a wire for a Young's modulus experiment, you should take multiple readings at different points along the wire and in different orientations. Explain why both of these practices are necessary. (2 steps)

**A:** - Step 1: Different points along the wire: the wire may not have a perfectly uniform cross-section — some sections may be slightly thicker or thinner due to manufacturing. Averaging over several points gives a more representative mean diameter.
- Step 2: Different orientations (rotating the wire): the wire's cross-section may not be perfectly circular — it could be slightly elliptical. Measuring in different orientations and averaging captures this and reduces the systematic error from assuming a perfect circle.

Both practices reduce random variation and catch non-uniformity that a single measurement would miss.

_Judge source label: GLM 5.1 ②_

---

## Card 70

**Q:** Why does plotting *stress* against *strain* produce a graph that's the same for any sample of a given material, while plotting force against extension does not? (2 steps)

**A:** - Step 1: Force-extension is dimensional: $$F = kx$$ where $$k = EA/L$$ depends on the sample's area and length. Two samples of different size give two different straight lines, even from the same material.
- Step 2: Stress and strain pre-normalise by area and length: $$\sigma = F/A$$, $$\varepsilon = \Delta L/L$$. So $$\sigma = E\varepsilon$$, and the slope is $$E$$ — a material constant. All samples of the same material lie on the same line.

This is why engineers tabulate $$E$$ for materials, not $$k$$ for objects.

_Judge source label: Opus 4.7 ②_

---

## Card 71

**Q:** Why is strain dimensionless, and why is it specifically a *ratio of lengths*?

**A:** - Step 1: Strain $$\varepsilon = \Delta L/L$$ divides one length by another — metres divided by metres — so the units cancel.
- Step 2: It's a ratio (rather than an absolute length) because we want a measure of deformation that doesn't depend on the size of the sample. A 1 mm extension on a 1 m rod (strain $$10^{-3}$$) is a much larger deformation per unit length than a 1 mm extension on a 1 km cable (strain $$10^{-6}$$).
- Step 3: Defining strain as a fraction lets us compare materials independent of geometry — exactly the same role density plays for mass-volume ratio.

The ratio form makes strain an *intensive* deformation measure, scaling-free.

_Judge source label: Opus 4.7 ②_

---

## Card 72

**Q:** On a stress-strain graph, the Ultimate Tensile Strength (UTS) occurs *before* the breaking point. Explain why the stress appears to decrease between the UTS and the fracture point. (2 steps)

**A:** - Step 1: After the UTS, the material begins to "neck"—a small region of the wire becomes significantly thinner than the rest.
- Step 2: Stress is force divided by area. Although the force might still be increasing slightly, the cross-sectional area at the neck decreases much faster. Because the area drops so rapidly, the calculated stress (based on the *original* cross-sectional area in a standard graph) appears to decrease, leading to the curve dropping before the fracture point.

_Judge source label: GLM 5.1 ①_

---

## Card 73

**Q:** On a force-extension graph for a rubber band being loaded and then unloaded, the loading curve lies above the unloading curve, forming a loop. What does the area enclosed by this hysteresis loop represent, and why does the rubber become warm when repeatedly stretched? (2 steps)

**A:** - Step 1: The area between the loading and unloading curves (the hysteresis loop) represents the energy per unit volume transferred to internal energy (heat) during each load-unload cycle. The work done *on* the rubber during loading exceeds the work done *by* the rubber during unloading.
- Step 2: The "missing" energy — the difference — is dissipated as heat in the rubber's molecular structure as the polymer chains slide past each other and experience internal friction. This is why rubber bands become warm when stretched and relaxed repeatedly.

The hysteresis loop is a visual representation of energy dissipation. Larger loop = more energy lost as heat per cycle.

_Judge source label: GLM 5.1 ②_

---

## Card 74

**Q:** Two identical springs of constant $$k=240\,\mathrm{N\,m^{-1}}$$ and natural length 210 mm are joined in series and a 8 N weight is hung. Why does each individual spring extend by $$F/k$$ rather than by $$F/(2k)$$?

**A:** - Step 1: In a series chain, the same force passes through every section — each spring individually feels the full 8 N pulling on it.
- Step 2: Each spring's extension is therefore $$x=F/k=8/240\approx 0.033\,\mathrm{m}$$, giving each spring a length of $$0.21+0.033=0.243\,\mathrm{m}$$.
- Step 3: The *effective* spring constant of the pair is $$k/2=120\,\mathrm{N\,m^{-1}}$$, but this gives the *total chain extension* ($$F/(k_{eff})=0.067\,\mathrm{m}$$), not each spring's individual length. Asking "how long is each spring?" vs. "how long is the chain?" requires different reasoning — and the question wording determines which is required.

_Judge source label: Opus 4.7 ①_

---

## Card 75

**Q:** Why is using ten readings of force–extension and plotting a graph generally better than computing $$k$$ from a single force–extension pair?

**A:** - Step 1: A single pair has individual reading uncertainties from each of $$F$$ and $$x$$. Computing $$k=F/x$$ propagates both uncertainties into the result.
- Step 2: With ten pairs plotted on a graph, the line of best fit averages out random scatter, and the gradient is a *consensus* value of $$k$$ — much more robust than any single pair.
- Step 3: Additionally, the graph reveals patterns: is the line straight (Hooke's law)? Does it pass through the origin (no zero error)? Where does it deviate (limit of proportionality)? These diagnostic insights are invisible from a single calculation.

_Judge source label: Opus 4.7 ①_

---

## Card 76

**Q:** Why does halving a wire's diameter (at fixed length and load) increase its extension by a factor of 4? (2 steps)

**A:** - Step 1: Cross-section $$A = \pi(d/2)^2$$ scales with $$d^2$$. Halving $$d$$ quarters $$A$$.
- Step 2: Extension $$\Delta L = FL/(AE)$$ scales as $$1/A$$. Quartering area means quadrupling extension.

So area-related parameters always scale geometrically with $$d^2$$. If the question says "diameter doubled", expect a factor of 4 reduction in extension and stress, holding everything else fixed.

_Judge source label: Opus 4.7 ②_

---

## Card 77

**Q:** Why is density expressed as mass *per unit volume* rather than just "how heavy something is", and what does the "per unit" structure let you compare?

**A:** - Step 1: Mass alone tells you total quantity of matter, but two objects of vastly different size can have the same mass — a kilogram of feathers and a kilogram of lead. So mass alone cannot capture how tightly packed the matter is.
- Step 2: Dividing by volume gives an *intensive* property: it no longer depends on how big a chunk you took. A small drop of mercury and a bathtub of mercury both have $$\rho \approx 13600\,\mathrm{kg\,m^{-3}}$$.
- Step 3: This lets you compare *materials*, not samples — so density becomes a fingerprint of substance identity (under fixed T, P), which is why it's useful for flotation, identification, and material selection.

The "per unit" structure converts a sample-specific quantity into a material-specific one.

_Judge source label: Opus 4.7 ②_

---

## Card 78

**Q:** Why is a brittle material like glass *strong* (high breaking stress) yet not *tough* (low energy absorbed before fracture)?

**A:** - Step 1: Strength refers to the *maximum stress* the material can withstand — the y-axis value at fracture on a stress–strain graph.
- Step 2: Toughness refers to the *area under the curve* up to fracture — the energy absorbed per unit volume before breaking.
- Step 3: Glass has a high breaking stress (tall on the y-axis) but almost no plastic region (the curve goes nearly straight up and then snaps — narrow on the x-axis). So the area (toughness) is tiny. A small impact concentrates energy at a flaw and shatters it, even though the stress at fracture is high. Copper is opposite: lower breaking stress but huge plastic region → much tougher.

_Judge source label: Opus 4.7 ①_

---

## Card 79

**Q:** Why is using $$\pi d^2$$ instead of $$\pi (d/2)^2$$ for the cross-sectional area of a wire such a damaging error?

**A:** - Step 1: $$\pi d^2 = \pi(2r)^2 = 4\pi r^2$$, so it's *four times* the correct area.
- Step 2: In stress: $$\sigma = F/A$$. If $$A$$ is four times too big, stress comes out four times too small.
- Step 3: In Young's modulus extension: $$\Delta L = FL/(AE)$$. If $$A$$ is four times too big, $$\Delta L$$ is four times too small.

The geometric factor of 4 is the kind of silent error that doesn't show up as a magnitude/units check — the number looks reasonable but is wrong. The fix is automatic: always say aloud "halve the diameter first, then square" when given a diameter.

_Judge source label: Opus 4.7 ②_

---

## Card 80

**Q:** When does $$E=\frac12 kx^2$$ stop being valid for elastic energy stored, and what should you use instead? (3 steps)

**A:** - Step 1: $$\frac12 kx^2$$ is the area of a triangle under a straight (Hooke's law) F–x line. It assumes force is exactly proportional to extension throughout the stretching.
- Step 2: Once you go beyond the limit of proportionality, the graph curves — the relationship is no longer linear, so the "triangle" formula overestimates or underestimates.
- Step 3: Use the actual *area under the curve* on the F–x graph. For complex shapes, count grid squares or split into approximate triangles/trapeziums. This is also why $$\frac12 kx^2$$ never applies to rubber, which has a strongly curved F–x behaviour from the start.

_Judge source label: Opus 4.7 ①_

---

## Card 81

**Q:** Why does a brittle material like glass have a stress–strain curve with virtually no plastic region, while ductile mild steel has a long flat plastic region? (3 steps)

**A:** - Step 1: At the atomic level, plastic deformation in metals occurs by dislocations gliding through the crystal lattice — defects that allow whole rows of atoms to slip without simultaneously breaking all bonds in a plane.
- Step 2: In glass (amorphous, non-crystalline), there are no orderly slip planes, so dislocations can't propagate. Once a microscopic crack starts, stress concentrates at the tip and the crack runs through the material immediately.
- Step 3: In mild steel, dislocations multiply and slide, allowing large plastic strains. The material extends, sometimes by $$20$$–$$30\%$$, before the cross-section narrows enough to fail.

The presence or absence of dislocation slip systems is what separates ductile from brittle behaviour.

_Judge source label: Opus 4.7 ②_

---

## Card 82

**Q:** Why does a rubber band's loading curve not coincide with its unloading curve (hysteresis)?

**A:** - Step 1: Stretching reorients polymer chains, but reorienting requires overcoming internal friction between chains — work done against this friction is dissipated as heat, not stored elastically.
- Step 2: On unloading, the chains slowly relax back, but they take a different path through configuration space, releasing less energy than was put in.
- Step 3: The enclosed area between the loading and unloading curves equals the energy per unit volume dissipated as heat over one cycle.

If you rapidly stretch and release a rubber band several times then touch it to your lip, you'll feel it warm — that's the hysteresis loop in action.

_Judge source label: Opus 4.7 ②_

---

## Card 83

**Q:** A spring obeys Hooke's law. If you double the extension, by what factor does the stored elastic energy increase?

**A:** - Step 1: $$E=\frac12 kx^2$$ — the energy depends on the *square* of the extension.
- Step 2: Doubling $$x$$ gives $$E_{new}=\frac12 k(2x)^2=4\cdot\frac12 kx^2$$.
- Step 3: Energy increases by a factor of 4. This is because force *and* distance both double, so work (force × distance) goes up by 4. This is a classic source of intuition errors: people guess "double" but the square wins.

_Judge source label: Opus 4.7 ①_

---

## Card 84

**Q:** A stress-strain graph and a force-extension graph are drawn for the same wire. Explain why the stress-strain graph is more useful for comparing *materials*, while the force-extension graph depends on the *sample dimensions*. (2 steps)

**A:** - Step 1: A force-extension graph depends on the wire's dimensions: a longer wire extends more (larger $$\Delta L$$ for same $$F$$), and a thicker wire has a larger $$A$$ (so it can carry more force before reaching a given stress). Two wires of the same material but different sizes give different force-extension graphs.
- Step 2: A stress-strain graph normalises for dimensions: stress divides force by area, and strain divides extension by original length. Two samples of the same material — regardless of size — produce the *same* stress-strain graph. This allows direct comparison of material properties.

Stress-strain = material property. Force-extension = object property.

_Judge source label: GLM 5.1 ②_

---

## Card 85

**Q:** Why is the spring-series-parallel rule "backwards" from the resistor-series-parallel rule? (2 steps)

**A:** - Step 1: The mathematical match is by *role*, not by geometry. For resistors, voltage $$V = IR$$ relates "potential drop" to current. For springs, force $$F = kx$$ relates force to extension. The quantity that is *shared* in series is current (for resistors) and force (for springs); the quantity that *sums* is voltage drop (resistors) and extension (springs).
- Step 2: So springs in geometric series behave mathematically like resistors in geometric parallel — both involve adding compliances (reciprocals of stiffness/conductance).

The mapping is: stiffness ↔ conductance ($$1/R$$), compliance ↔ resistance. Spring series geometry = resistor parallel geometry in mathematical form.

_Judge source label: Opus 4.7 ②_

---

## Card 86

**Q:** A student has two identical springs with $$k = 240\,\text{N}\,\text{m}^{-1}$$ and natural length 210 mm. They are joined in series and a force of 8.0 N is applied. What is the length of *each individual spring*, and why is it wrong to add the total chain extension to just one spring? (3 steps)

**A:** - Step 1: In series, each spring carries the full 8.0 N. The extension of each spring is $$x = F/k = 8.0/240 = 0.0333\,\text{m}$$.
- Step 2: The length of each individual spring = natural length + its own extension = $$0.210 + 0.0333 = 0.243\,\text{m}$$.
- Step 3: A common mistake is to use the effective series stiffness ($$k_{\text{eff}} = 120\,\text{N}\,\text{m}^{-1}$$) to find the *total* extension ($$8.0/120 = 0.0667\,\text{m}$$) and then add this total to one spring's natural length. This gives $$0.210 + 0.0667 = 0.277\,\text{m}$$, which is wrong — it represents the total chain length, not the length of one spring.

Read the question carefully: "length of each spring" ≠ "total chain length."

_Judge source label: GLM 5.1 ②_

---

## Card 87

**Q:** An object falling through a viscous fluid reaches terminal velocity. Conceptually, what's happening to the upthrust and viscous drag at that moment?

**A:** - Step 1: At terminal velocity, the object stops accelerating: net force = 0. So weight = upthrust + viscous drag.
- Step 2: Upthrust is constant (depends only on fluid density and submerged volume — both fixed for a given object/fluid pair). Viscous drag, $$F_D = 6\pi\eta rv$$ for a small sphere, grows with velocity.
- Step 3: As the object speeds up, drag grows until weight − upthrust = drag exactly. From then on, it falls at constant velocity.

The system self-regulates: drag automatically rises to match the residual weight.

_Judge source label: Opus 4.7 ②_

---

## Card 88

**Q:** Why do we plot a *force–extension* graph (not a force–length graph) when analysing Hooke's law? (3 steps)

**A:** - Step 1: Hooke's law is $$F=kx$$ where $$x$$ is the *extension from natural length*, not the total length.
- Step 2: If you plot F against total length, the line doesn't pass through the origin — it crosses the length axis at the natural length, adding a constant offset and obscuring the proportional relationship.
- Step 3: Subtracting the natural length to get extension shifts the graph so it passes through the origin, making the gradient ($$k$$) easy to identify and Hooke's law visually obvious. Always: extension = current length − natural (zero-force) length.

_Judge source label: Opus 4.7 ①_

---

## Card 89

**Q:** Why is the gradient of a stress–strain graph numerically equal to the Young modulus, while the gradient of a force–extension graph equals the spring constant $$k$$ (not $$E$$)? (3 steps)

**A:** - Step 1: On a stress–strain graph, x-axis is $$\varepsilon=\Delta L/L$$ and y-axis is $$\sigma=F/A$$. Slope = $$\sigma/\varepsilon=E$$ directly — the Young modulus.
- Step 2: On a force–extension graph, x-axis is $$\Delta L$$ and y-axis is $$F$$. Slope = $$F/\Delta L=k$$ — the spring constant of this particular object.
- Step 3: The two are related: $$k=EA/L$$. So $$k$$ depends on geometry (length and area), while $$E$$ doesn't. Two wires of the same steel but different sizes have different $$k$$'s but the same $$E$$. This is why physicists prefer stress–strain plots for material characterisation: the slope is universal for the material.

_Judge source label: Opus 4.7 ①_

---

## Card 90

**Q:** Why does the maximum extension of a rubber band depend not on stiffness but on the *length of the polymer chains*?

**A:** - Step 1: At low extension, the polymer chains in rubber are tangled. Small forces untangle them without stretching the strong C-C bonds.
- Step 2: As extension increases, more chains align until fully extended. The total extension at this stage depends on how long the chains *are* — longer chains can extend further before becoming fully aligned.
- Step 3: Once all chains are aligned, further stretching means breaking covalent bonds (stretching them strongly). The "maximum extension" of rubber thus reflects how much *slack* exists in the molecular structure, not how stiff each bond is. This is fundamentally different from a metal, where extension comes from stretching atomic bonds throughout.

_Judge source label: Opus 4.7 ①_

---

## Card 91

**Q:** Why does a mixture's density usually *not* equal the simple arithmetic mean of its components' densities, but a *volume-weighted* average?

**A:** - Step 1: Density is mass per volume. The total mass is the sum of component masses; the total volume is the sum of component volumes (assuming no shrinkage/expansion on mixing).
- Step 2: $$\rho_{mix}=\frac{m_1+m_2}{V_1+V_2}=\frac{\rho_1 V_1+\rho_2 V_2}{V_1+V_2}$$ — this is a volume-weighted average.
- Step 3: An arithmetic mean of $$\rho_1$$ and $$\rho_2$$ would only be correct if equal *volumes* were mixed. In a brass alloy that is 70% copper and 30% zinc *by volume*, the answer is closer to copper than a simple average suggests — exactly because more of the volume is copper.

_Judge source label: Opus 4.7 ①_

---

## Card 92

**Q:** Why does adding a small initial mass to the test wire in Searle's apparatus matter before starting Young modulus measurements?

**A:** - Step 1: A new wire has small kinks, bends, and slack from manufacture and handling.
- Step 2: Without an initial load, the first added weights waste their extension just straightening the wire rather than truly stretching it. This contaminates the F–x relationship.
- Step 3: A small pre-load (e.g. a 100 g hanger) removes the kinks, sets a sensible "zero" for the vernier scale, and ensures all subsequent extension readings reflect actual elastic stretching. Skipping this step introduces a systematic underestimate of $$E$$.

_Judge source label: Opus 4.7 ①_

---

## Card 93

**Q:** A student is told that a suspension bridge cable has diameter 50 mm and pulls with force 4 kN. They immediately write $$A = \pi(50)^2$$. List all the errors. (3 steps)

**A:** - Step 1: **Unit error**: 50 mm must be converted to metres: $$50\,\mathrm{mm} = 0.050\,\mathrm{m}$$. Using 50 directly gives an area 10⁶ times too large in SI units.
- Step 2: **Diameter-to-radius error**: The formula requires radius, not diameter. They should use $$r = 0.025\,\mathrm{m}$$, not 0.050 m. Using the diameter as the radius gives an area 4 times too large.
- Step 3: **Force unit**: 4 kN = 4000 N. If they use 4 without converting, the stress would be 1000 times too small.

Combined, these errors could make the stress wrong by a factor of $$4 \times 10^6 \times 1000 = 4 \times 10^9$$ — completely unrecognisable. Always convert units before substituting.

_Judge source label: GLM 5.1 ③_

---

## Card 94

**Q:** A force–extension graph for a non-linear spring rises sharply at first and then bends over. How do you find the elastic strain energy stored at extension $$x_0$$? (2 steps)

**A:** - Step 1: Energy stored = work done = area under the graph from $$0$$ to $$x_0$$. Do *not* use $$\tfrac{1}{2}Fx_0$$, which is only valid when the line is straight through the origin.
- Step 2: For a curve, either:
+ Approximate by trapezia (split the area into strips and add).
+ Count squares under the curve and multiply by the energy per square ($$\Delta F \times \Delta x$$ for each grid square).
+ If the function is known analytically, integrate $$\int_0^{x_0} F(x)\, dx$$.

The "$$\tfrac{1}{2}Fx$$" formula is a special-case shortcut for Hooke-region springs only.

_Judge source label: Opus 4.7 ②_

---

## Card 95

**Q:** Young's modulus combines stress and strain. Conceptually, what does $$E$$ tell you that the spring constant $$k$$ does *not*? (3 steps)

**A:** - Step 1: Spring constant $$k$$ depends on the *object's geometry* — its length, its cross-section, its material. A long thin wire of steel and a short thick rod of steel have very different $$k$$ values.
- Step 2: Young's modulus $$E = \sigma/\varepsilon$$ factors out the geometry: stress already divides force by area, and strain already divides extension by length. So $$E$$ depends only on the *material*.
- Step 3: $$E$$ is a fundamental material property (like density). Steel always has $$E \approx 2\times10^{11}\,\mathrm{Pa}$$ regardless of shape; that lets engineers compare materials cleanly.

$$k$$ is a sample-specific stiffness; $$E$$ is a material-specific stiffness.

_Judge source label: Opus 4.7 ②_

---

## Card 96

**Q:** Steel has $$E \approx 2\times 10^{11}\,\mathrm{Pa}$$; rubber has $$E \sim 10^{7}$$–$$10^{8}\,\mathrm{Pa}$$. By what rough factor is steel stiffer than rubber, and what does that mean for similarly-sized samples under the same load?

**A:** - Step 1: Ratio $$E_{\text{steel}}/E_{\text{rubber}} \sim 10^{11}/10^{7} = 10^{4}$$ — steel is about ten thousand times stiffer.
- Step 2: For samples of the same dimensions and the same load: $$\Delta L \propto 1/E$$. So a rubber rod stretches 10,000 times as much as a steel rod under the same force.
- Step 3: Equivalently, to produce the *same* extension, you'd need 10,000 times more force on the steel — which is why steel is used for structural beams and rubber is used for shock-absorbers.

The four orders of magnitude in $$E$$ are what makes the two materials engineered for completely different roles.

_Judge source label: Opus 4.7 ②_

---

## Card 97

**Q:** A graph of F vs extension passes through the origin if Hooke's law holds. If the intercept is not at zero, what physical situation might explain it?

**A:** - Step 1: A positive y-intercept (extension at F = 0) might mean a measurement offset — for example, the ruler's zero wasn't aligned with the spring's natural length.
- Step 2: A negative y-intercept could indicate the spring was pre-tensioned at "zero force" (e.g. the spring was being held compressed first) or that a small initial load was applied before measurements started.
- Step 3: Either way, the slope ($$k$$) is still correct; only the offset is contaminated. This is why graphs are robust to systematic offset errors — you should always extract physical constants from gradients, not single substitutions.

_Judge source label: Opus 4.7 ①_

---

## Card 98

**Q:** Searle's apparatus uses two wires (a "control" wire and a "test" wire). What's the role of the control wire? (3 steps)

**A:** - Step 1: Both wires hang from the same support, in the same room, so they experience identical temperature changes and any sagging of the support.
- Step 2: The extension measured (via the vernier scale and spirit level) is the *difference* in length between the test wire and the control wire. Common-mode effects — temperature-driven expansion of either wire, or the support flexing — cancel out.
- Step 3: What remains is only the extra extension caused by the load on the test wire. So the control wire isolates the effect of the load from environmental noise.

This is a classic "differential measurement" technique — measure two similar things and subtract.

_Judge source label: Opus 4.7 ②_

---

## Card 99

**Q:** Why doesn't the engineer just use the *highest observed temperature* to set the pre-strain (so the rail is stress-free at the hottest day)?

**A:** - Step 1: If the rail is unstressed at the hottest day, then on a cool day it contracts. Since it's fixed at both ends, contraction means tensile stress — and the colder it gets, the higher the tension.
- Step 2: At the coldest expected temperature, tensile stress could exceed the breaking stress, snapping the rail.
- Step 3: The engineer balances two failure modes: buckling from compression (too little pre-strain) versus snapping from tension (too much pre-strain). The pre-strain is chosen to keep stress within safe limits across the *full temperature range*, not optimised for the hot extreme alone.

_Judge source label: Opus 4.7 ①_

---

## Card 100

**Q:** Two materials have the same Young modulus but very different breaking stresses. What does this mean physically?

**A:** - Step 1: Young modulus only describes behaviour in the *elastic* region — the initial slope of stress–strain.
- Step 2: Two materials can start out equally stiff but diverge dramatically later: one might yield and stretch plastically before breaking, while the other snaps abruptly at a much lower stress.
- Step 3: So $$E$$ tells you "how hard to stretch a tiny bit" but not "when does it break". Designers care about both: $$E$$ controls deflection under normal loads; breaking stress controls failure under extreme loads. Steel and aluminium have similar $$E$$/density ratios but very different breaking stresses and ductilities.

_Judge source label: Opus 4.7 ①_

---

## Card 101

**Q:** Why does the spring constant of a single spring tell you nothing definite about the spring constants of two of them in any combination, unless you know whether they're series or parallel?

**A:** - Step 1: For two identical springs of constant $$k$$ in series, the effective stiffness is $$k/2$$ — half as stiff.
- Step 2: For the same two in parallel, the effective stiffness is $$2k$$ — twice as stiff.
- Step 3: That's a factor-of-4 difference between the two configurations, both made of the same components. Without specifying the arrangement, you can't predict the system's behaviour. This mirrors electrical circuits exactly: identical resistors give different totals in series vs parallel.

_Judge source label: Opus 4.7 ①_

---

## Card 102

**Q:** Why do scientists specify *temperature and pressure* when quoting the density of a gas, but not usually for a solid or liquid?

**A:** - Step 1: Gases are highly compressible: raising the pressure squeezes molecules closer, increasing mass per unit volume. Heating expands them, decreasing density.
- Step 2: Solids and liquids barely change volume with temperature or pressure — their molecules are already in contact, so density is essentially constant under lab conditions.
- Step 3: For a gas, quoting "density = 1.2 kg/m³" is meaningless without conditions; this is why a balloon's air can be denser than free atmospheric air (it's compressed inside).

_Judge source label: Opus 4.7 ①_

---

## Card 103

**Q:** Why is stress *not* the same physical thing as pressure, even though both have units of pascals?

**A:** - Step 1: Both are defined as force per unit area, so they share units. But pressure is associated with fluids pushing on a surface from outside — it's isotropic (acts equally in all directions) and is a *contact* force quantity.
- Step 2: Stress refers to the *internal* state of a solid — how much force per area is being transmitted through a cross-section of the material itself. Stress can be tensile (pulling apart), compressive (pushing together), or shear (sliding along), and is generally a tensor (direction-dependent).
- Step 3: A pressurised gas exerts pressure on a container wall; the container wall material has internal stresses arising from that pressure. They're related but distinct concepts: one describes the agent (fluid), one describes the response (solid).

Same units, different physical role.

_Judge source label: Opus 4.7 ②_

---

## Card 104

**Q:** The elastic strain energy stored in a spring obeying Hooke's law can be written as either $$\frac{1}{2}Fx$$ or $$\frac{1}{2}kx^2$$. Show that these are equivalent, and explain why the factor of $$\frac{1}{2}$$ appears. (3 steps)

**A:** - Step 1: The factor of $$\frac{1}{2}$$ appears because the force increases from 0 to $$F$$ as the spring extends. The average force during this process is $$F/2$$, not $$F$$. Work done = average force × distance = $$(F/2) \times x = \frac{1}{2}Fx$$.
- Step 2: Substitute $$F = kx$$ into $$\frac{1}{2}Fx$$: $$\frac{1}{2}(kx)(x) = \frac{1}{2}kx^2$$.
- Step 3: Geometrically, this is the area of a triangle on the force-extension graph (base = $$x$$, height = $$F$$, area = $$\frac{1}{2} \times \text{base} \times \text{height}$$). The triangle exists because the relationship is linear and starts from the origin.

The $$\frac{1}{2}$$ comes from the linear ramp-up of force. If force were constant (like a weight simply placed on a spring), the energy would be $$Fx$$, not $$\frac{1}{2}Fx$$.

_Judge source label: GLM 5.1 ②_

---

## Card 105

**Q:** A student is asked to calculate the stress in a copper wire given only that it is 1.52 m long and stretches by 3.2 mm. Can the stress be calculated? If not, what information is missing? (2 steps)

**A:** - Step 1: Stress requires $$\sigma = F/A$$. The given data (original length and extension) only allow calculation of strain: $$\varepsilon = \Delta L / L = 0.0032/1.52 \approx 0.0021$$. This is strain, not stress.
- Step 2: To calculate stress, you would also need either (a) the force and the cross-sectional area, or (b) the Young modulus of copper (since $$\sigma = E\varepsilon$$). Without one of these, stress cannot be determined.

This was a trick question from the video. The key skill is recognising when information is insufficient, rather than forcing a formula.

_Judge source label: GLM 5.1 ③_

---

## Card 106

**Q:** A student is asked what safety precaution to take when doing a spring experiment. They answer "wear gloves." What is the more important precaution they are missing, and why? (2 steps)

**A:** - Step 1: The primary hazard in a spring experiment is the spring detaching and flying off, or the masses falling. Gloves do not protect against either of these.
- Step 2: The most important precaution is **wearing safety glasses** (goggles), because a flying spring or wire could cause serious eye injury. A secondary precaution is ensuring masses cannot fall on feet (use a sand tray or keep feet clear).

Think about the specific hazard, not just general lab safety. For spring/wire experiments, eye protection is paramount.

_Judge source label: GLM 5.1 ③_

---

## Card 107

**Q:** A spherical balloon of radius $$20\,\mathrm{cm}$$ contains $$50\,\mathrm{g}$$ of air. Walk through the conceptual steps to find its density without doing a full numerical computation. (4 steps)

**A:** - Step 1: Identify the geometry — sphere — so volume formula triggered is $$V = \frac{4}{3}\pi r^3$$. The radius is given directly (not diameter), so no halving needed.
- Step 2: Convert to SI: $$r = 0.20\,\mathrm{m}$$, $$m = 0.050\,\mathrm{kg}$$. The danger is cubing centimetres without realising; converting first avoids it.
- Step 3: Apply $$\rho = m/V$$. Order of magnitude: $$r^3 \sim 10^{-2}$$, so $$V \sim 10^{-2}\,\mathrm{m^3}$$. Then $$\rho \sim 0.05/0.03 \sim 1.5\,\mathrm{kg\,m^{-3}}$$.
- Step 4: Compare with standard air ($$\sim 1.2\,\mathrm{kg\,m^{-3}}$$). It's slightly higher — physically reasonable because air inside a balloon is at higher pressure than atmospheric.

The whole calculation can be done in your head once you've isolated the conceptual move "sphere → volume formula → density".

_Judge source label: Opus 4.7 ②_

---
