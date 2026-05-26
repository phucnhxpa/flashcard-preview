# How this edition is different

This is the expanded complete-lecture edition. The previous PDF was a clean structured guide, but it was still too compressed: it gave the map, the key calculations, and the mistake bank, without fully teaching the lesson in the way a tutor would teach it from first principles.

This version is built after re-watching the actual lesson videos with Gemini video analysis:

- the **Measurement and Density** lesson video, duration about 38 minutes;
- the **Hooke's Law, Stress, Strain and Young's Modulus** lesson video, duration about 55 minutes.

The purpose is not to be short. The purpose is to make rewatching unnecessary. For each topic, the guide explains:

1. what prior knowledge is needed;
2. what Alex was teaching in the video;
3. what Phuc asked or hesitated on;
4. what the correct thought process should be;
5. how to write the answer in an exam;
6. what drill Phuc should do next.

# How to read this guide

Read it in three passes.

**Pass 1: Concept pass.** Read the prior-knowledge bootcamp and the first-principles explanations. Do not worry about speed. The goal is to rebuild the ideas.

**Pass 2: Worked-example pass.** For each worked example, cover the solution and force yourself to say the trigger phrase: "What is given? What is asked? What formula is triggered? What unit conversion is dangerous? What does the answer roughly need to look like?"

**Pass 3: Redo pass.** Use the Phuc-specific mistake bank and the drill list. The point is not to reread; it is to remove the exact mistakes that appeared in the videos.

# Video evidence and source status

| Lesson | Video evidence | Status |
|---|---|---|
| Measurement and Density | Local video `fluids_density.mp4`, watched with Gemini video analysis | Direct video analysis completed |
| Hooke's Law, Stress, Strain, Young's Modulus | Local video `stress_low.mp4` / source Hooke lesson, watched with Gemini video analysis | Direct video analysis completed |
| Ordered frame evidence | Existing frame inventories in `analysis/fluids_frames_batch_*.md` and previous generated figures | Supporting evidence |
| Previous guide | `fluids_materials_general_template_redo.tex` and earlier video-grounded guide | Used for continuity and checked arithmetic |

# Prior knowledge bootcamp

Before the actual lesson content, there are several pieces of prior knowledge that must be automatic. If these are not automatic, the later calculations feel like memorising formulas. If they are automatic, the questions become predictable.

## 1. Physical quantities and units

A physical quantity is a measurable property. In these lessons the main quantities are length, mass, volume, force, area, pressure/stress, extension and density.

The exam habit is:

1. name the quantity;
2. write its symbol;
3. write the unit;
4. check whether the unit in the question is already SI.

For example:

| Quantity | Symbol | Common unit in question | SI unit needed | Trap |
|---|---:|---:|---:|---|
| mass | $m$ | g, kg | kg | grams must become kg for SI density |
| length/radius | $L,r,d$ | mm, cm, m | m | if cubed, conversion error is cubed too |
| volume | $V$ | litres, cm$^3$, m$^3$ | m$^3$ | $1\,\mathrm{L}=10^{-3}\,\mathrm{m^3}$ |
| force | $F$ | N | N | force from mass is $mg$, not just mass |
| area | $A$ | mm$^2$, m$^2$ | m$^2$ | from diameter, halve first then square |
| density | $\rho$ | g cm$^{-3}$, kg m$^{-3}$ | kg m$^{-3}$ | $1\,\mathrm{g\,cm^{-3}}=1000\,\mathrm{kg\,m^{-3}}$ |
| stress | $\sigma$ | Pa | Pa | same unit as pressure but different context |
| strain | $\varepsilon$ | no unit | no unit | ratio, so units cancel |

The thought process is: if the final answer unit contains metres, kilograms and seconds, convert the input values before substituting.

## 2. Prefixes and powers of ten

The lessons repeatedly use millimetres, centimetres, grams and litres. These must become automatic:

\[
1\,\mathrm{mm}=10^{-3}\,\mathrm{m},\qquad 1\,\mathrm{cm}=10^{-2}\,\mathrm{m},\qquad 1\,\mathrm{g}=10^{-3}\,\mathrm{kg}.
\]

For volume, the exponent applies to the whole length conversion:

\[
1\,\mathrm{cm^3}=(10^{-2}\,\mathrm{m})^3=10^{-6}\,\mathrm{m^3}.
\]

This is why density conversion is easy to get wrong. One cubic centimetre is much smaller than one cubic metre, so densities in $\mathrm{kg\,m^{-3}}$ look much larger than densities in $\mathrm{g\,cm^{-3}}$.

## 3. Geometry formulas needed

The density questions use volume. The materials questions use area.

For a sphere:

\[
V=\frac{4}{3}\pi r^3.
\]

The trigger phrase is: if the object is a ball or balloon and the question gives radius or diameter, think sphere volume. If diameter is given, halve it to get radius before cubing.

For a cylinder:

\[
V=\pi r^2h.
\]

For a cuboid:

\[
V=lwh.
\]

For cross-sectional area of a circular wire or cable:

\[
A=\pi r^2=\pi\left(\frac{d}{2}\right)^2.
\]

The most dangerous mistake in Young modulus questions is using $\pi d^2$ instead of $\pi(d/2)^2$. That gives an area four times too large and an extension or stress four times too small.

## 4. Proportionality, gradients and graphs

Hooke's law is a proportionality statement:

\[
F\propto x \quad \Rightarrow \quad F=kx.
\]

On a force-extension graph, $k$ is the gradient:

\[
k=\frac{\Delta F}{\Delta x}.
\]

A straight line through the origin means direct proportionality. A curve means the proportionality has broken down. The limit of proportionality is the point where the graph stops being straight.

The area under a force-extension graph is work done/elastic strain energy:

\[
E_e=\frac{1}{2}Fx=\frac{1}{2}kx^2
\]

only for the straight-line Hooke's law region. If the graph is not straight, use area under the graph rather than forcing $\frac12kx^2$.

## 5. Practical uncertainty and instrument resolution

Resolution is the smallest change an instrument can show. Range is maximum minus minimum. Accuracy is closeness to the true value. Precision is repeatability.

The video showed that instrument-reading is not a side detail. Phuc specifically needed guidance on how to read the micrometer and Vernier caliper. These are practical-skill marks in A-level physics.

The exam thought process for practical measurement is:

1. What quantity am I measuring?
2. What instrument has suitable range and resolution?
3. What is the dominant uncertainty?
4. Can I repeat and average?
5. Can I make the measured value larger to reduce percentage uncertainty?
6. What systematic errors must be avoided?

For example, measuring one sheet of paper directly gives a tiny reading with high percentage uncertainty. Measuring ten sheets and dividing by ten is better.

# Core diagrams to redraw

![Instrument-reading rules from the lesson](../figures/instrument_reading_rules.png)

![Density practical methods](../figures/density_methods.png)

![Hooke's law graph](../figures/hooke_graph.png)

![Spring combinations](../figures/spring_combinations.png)

![Stress-strain graph](../figures/stress_strain_curve.png)

![Terminal velocity force diagram](../figures/terminal_velocity_forces.png)

# First-principles calculation template

For every physics calculation in these lessons, use this exact mental template.

## Step 1: Translate the sentence into symbols

Do not start by hunting for a formula. First write what the question gives you.

Example: "A spherical balloon of radius 20 cm contains 50 g of air."

\[
r=20\,\mathrm{cm},\qquad m=50\,\mathrm{g}.
\]

## Step 2: Identify what is asked

If the question asks for density, the target is $\rho$. If it asks for extension, the target is $\Delta L$ or $x$. If it asks for stiffness, the target is $k$ or $E$.

## Step 3: Convert units before substitution

For the balloon:

\[
r=0.20\,\mathrm{m},\qquad m=0.050\,\mathrm{kg}.
\]

## Step 4: Identify the intermediate quantity

Many questions are two-step questions. A sphere density question is not just $\rho=m/V$ because $V$ is not given; it must be calculated.

## Step 5: Choose the formula from the trigger

- mass per volume -> $\rho=m/V$;
- spring force and extension -> $F=kx$;
- force over area in material -> $\sigma=F/A$;
- extension over original length -> $\varepsilon=\Delta L/L$;
- material stiffness -> $E=\sigma/\varepsilon=FL/(A\Delta L)$.

## Step 6: Substitute with powers of ten visible

Do not hide powers of ten in your calculator. Write them down. This protects method marks.

## Step 7: Sanity-check the answer

Ask whether the order of magnitude makes physical sense. Air density around $1\,\mathrm{kg\,m^{-3}}$ is reasonable. Steel Young modulus around $10^{11}\,\mathrm{Pa}$ is reasonable. A spring constant of $59\,\mathrm{N\,m^{-1}}$ for a soft lab spring is reasonable.

# Lesson 1: Measurement and density complete video-grounded lecture

The following section is the detailed video-grounded source pack from the Measurement and Density lesson. It includes chronological walkthrough, prior knowledge, full topic explanation, exercises, diagrams, Phuc mistakes, Alex corrections, exam technique and redo tasks.

## A-Level Physics Revision Guide: Measurement and Density

### 1. Chronological Walkthrough by Timestamp

This section provides a detailed, chronological breakdown of the lesson, capturing all visible and audible information.

**00:50 - 00:55: Micrometer Simulator**
*   **Visible Screen:** Phuc opens a Brave tab to a "Virtual Micrometer in Hundredths Millimeter - Simulator" website (`stefanelli.eng.br`). The page explains how to use a micrometer and shows an interactive diagram.
*   **Alex Teaching:** Alex explains how to read the micrometer, focusing on the main scale (mm) and the thimble scale (hundredths of a mm). He demonstrates by dragging the thimble.
*   **Phuc Doing/Asking:** Phuc asks questions about reading the scales and understanding the resolution.
*   **Exercises/Questions:** Interactive micrometer simulation.
*   **Tutor Correction:** Alex clarifies how to read the main scale (0.5 mm increments) and the thimble scale (0.01 mm increments).

**00:55 - 01:00: Vernier Caliper Simulator**
*   **Visible Screen:** Phuc opens another Brave tab to a "Virtual Vernier Caliper - simulator in 0.05 Millimeter" website (`stefanelli.eng.br`). This simulator shows a Vernier caliper with an interactive diagram.
*   **Alex Teaching:** Alex explains how to read the Vernier caliper, focusing on the main scale (mm) and the Vernier scale (0.05 mm resolution). He demonstrates by dragging the caliper jaws.
*   **Phuc Doing/Asking:** Phuc asks about reading the Vernier scale and how to determine the matching line.
*   **Exercises/Questions:** Interactive Vernier caliper simulation.
*   **Tutor Correction:** Alex clarifies that the main scale is read up to the zero mark of the Vernier scale, and then the Vernier scale is read where its lines align with the main scale.

**01:00 - 01:05: OneNote Worksheet - Micrometer and Vernier Caliper Readings**
*   **Visible Screen:** Phuc returns to OneNote, showing a worksheet with diagrams of micrometers and Vernier calipers, asking for "Actual Reading = ___ cm" or "Actual Reading = ___ mm". Some examples have answers written in.
*   **Alex Teaching:** Alex reviews the worksheet, confirming the readings and explaining the concept of zero error.
*   **Phuc Doing/Asking:** Phuc reviews the worksheet and asks about zero error.
*   **Exercises/Questions:** Multiple diagrams of micrometers and Vernier calipers with readings to be determined.
*   **Tutor Correction:** Alex explains positive and negative zero error and how to correct for it.

**01:05 - 01:10: OneNote - Measuring Density of Regular Object**
*   **Visible Screen:** Phuc scrolls to a new section in OneNote: "A) Measuring density of a regular object". It lists "Equipment list with resolution and range:" and "Method: 1) measure appropriate dimensions of the object such that volume can be calculated 2) measure mass of object".
*   **Alex Teaching:** Alex explains the method for measuring density of a regular object (e.g., a cube), emphasizing the need for appropriate measuring tools (micrometer, Vernier caliper, ruler) and a mass balance. He draws a cube.
*   **Phuc Doing/Asking:** Phuc draws a cube and notes "using mass balance".
*   **Exercises/Questions:** N/A.
*   **Tutor Correction:** N/A.

**01:10 - 01:15: OneNote - Measuring Density of Irregular Object**
*   **Visible Screen:** Phuc scrolls to "B) Measuring density of an irregular object". It lists "Method: 1) measure mass of object 2) tie string round object 3) fill measuring cylinder with water 4) record the volume 5) submerge object in the measuring cylinder and record the new volume".
*   **Alex Teaching:** Alex explains the displacement method using a Eureka can and measuring cylinder. He draws a diagram of a Eureka can with a measuring cylinder.
*   **Phuc Doing/Asking:** Phuc draws the Eureka can setup and notes "collect water in measuring cylinder".
*   **Exercises/Questions:** N/A.
*   **Tutor Correction:** N/A.

**01:15 - 01:20: OneNote - Measuring Density of a Liquid**
*   **Visible Screen:** Phuc scrolls to "C) Measuring density of a liquid". It lists "Method: 1) measure mass of empty measuring cylinder 2) fill measuring cylinder with liquid 3) measure mass of full measuring cylinder 4) record volume of liquid in measuring cylinder".
*   **Alex Teaching:** Alex explains the method for measuring liquid density using a measuring cylinder and mass balance. He draws a measuring cylinder on a mass balance.
*   **Phuc Doing/Asking:** Phuc draws the measuring cylinder on a mass balance and notes "mass balance".
*   **Exercises/Questions:** N/A.
*   **Tutor Correction:** N/A.

**01:20 - 01:25: OneNote - Core Task (Density Calculation Problems)**
*   **Visible Screen:** Phuc scrolls to "Core task". It contains several density calculation problems:
    1.  "A bottle of whiskey contains 1 litre of the drink. The mass of the liquid in the bottle is 0.915 kg. What is the density of this brand of whiskey? (1000 litres = 1 m^3)"
    2.  "The radius of a hockey ball is 36 mm and its mass is 160 g. What is its density (a) in g cm^{-3}? (b) in kg m^{-3}?"
    3.  "Estimate the mass of air in this room."
    4.  "A spherical balloon of radius 20 cm contains 50 g of air. a) Calculate the density of air in the balloon. b) Comment on why it differs from that given in Table 12.1 (page 177) (Total 3 Marks)"
*   **Alex Teaching:** Alex guides Phuc through the problems, emphasizing unit conversions and proper layout for exam answers.
*   **Phuc Doing/Asking:** Phuc attempts the problems, showing his working and asking questions about units and formulas.
*   **Exercises/Questions:** Density calculation problems.
*   **Tutor Correction:** Alex corrects Phuc's unit conversions and guides him on using the formula sheet.

**01:25 - 01:30: OneNote - Further Tasks (Seismometer Problem)**
*   **Visible Screen:** Phuc scrolls to "Further tasks". It shows a diagram of a seismometer and a question: "Q1. A seismometer is a device that is used to record the movement of the ground during an earthquake. A simple seismometer is shown in the diagram. (Diagram of seismometer with rotating drum, pen, spring, heavy ball, axis of rotation, 3.0 cm, 8.0 cm)"
*   **Alex Teaching:** Alex briefly introduces the seismometer problem.
*   **Phuc Doing/Asking:** N/A.
*   **Exercises/Questions:** Seismometer problem.
*   **Tutor Correction:** N/A.

**01:30 - 01:35: OneNote - Brass Alloy Problem**
*   **Visible Screen:** Phuc scrolls to another problem: "Q2. (a) Define the density of a material. (1) (b) Brass, an alloy of copper and zinc, consists of 70% by volume of copper and 30% by volume of zinc. density of copper = 8.9 x 10^3 kg m^{-3} density of zinc = 7.1 x 10^3 kg m^{-3} (i) Determine the mass of copper and the mass of zinc required to make a rod of brass of volume 0.80 x 10^{-3} m^3. (ii) Calculate the density of brass. (Total 5 Marks)"
*   **Alex Teaching:** Alex guides Phuc through the brass alloy problem, focusing on calculating individual volumes and masses, then combining them for the alloy's density.
*   **Phuc Doing/Asking:** Phuc attempts the problem, showing calculations for volumes and masses of copper and zinc, then the overall density.
*   **Exercises/Questions:** Brass alloy density calculation.
*   **Tutor Correction:** Alex confirms the steps and calculations.

**01:35 - 01:40: End of Lesson**
*   **Visible Screen:** Google Meet call.
*   **Alex Teaching:** Alex concludes the lesson, giving Phuc a thumbs up.
*   **Phuc Doing/Asking:** Phuc thanks Alex.
*   **Exercises/Questions:** N/A.
*   **Tutor Correction:** N/A.

---

### 2. Complete Prior-Knowledge Lecture

This section covers the foundational knowledge required to understand the concepts discussed in the lesson.

**2.1. SI Units and Prefixes**
*   **Explanation:** The International System of Units (SI) is the standard system of measurement used in science. It defines seven base units from which all other units are derived. Prefixes are used to denote multiples or submultiples of these units, making it easier to express very large or very small quantities.
*   **Key SI Base Units:**
    *   Length: meter (m)
    *   Mass: kilogram (kg)
    *   Time: second (s)
    *   Electric current: ampere (A)
    *   Temperature: kelvin (K)
    *   Amount of substance: mole (mol)
    *   Luminous intensity: candela (cd)
*   **Common Prefixes:**
    *   Giga (G): 10^9
    *   Mega (M): 10^6
    *   Kilo (k): 10^3
    *   Centi (c): 10^-2
    *   Milli (m): 10^{-3}
    *   Micro (µ): 10^{-6}
    *   Nano (n): 10^-9
*   **Why it matters:** In physics, all calculations must be performed using consistent SI units. Failing to convert units (e.g., cm to m, g to kg) is a common source of error in exams. The lesson explicitly shows conversions for radius (cm to m) and mass (g to kg) in density calculations.

**2.2. Derived Units**
*   **Explanation:** Derived units are combinations of base units. For example, speed is distance/time, so its derived unit is m/s. Volume is length x width x height, so its derived unit is m^3. Density is mass/volume, so its derived unit is kg/m^3.
*   **Why it matters:** Understanding derived units helps in checking the consistency of equations and ensuring that final answers have the correct units. The lesson focuses heavily on density (kg/m^3 or g/cm^3).

**2.3. Significant Figures**
*   **Explanation:** Significant figures (sig figs) indicate the precision of a measurement.
    *   Non-zero digits are always significant.
    *   Zeros between non-zero digits are significant.
    *   Leading zeros (e.g., 0.005) are not significant.
    *   Trailing zeros are significant only if the number contains a decimal point (e.g., 100.0 has 4 sig figs, 100 has 1 sig fig).
*   **Rules for Calculations:**
    *   **Multiplication/Division:** The result should have the same number of significant figures as the measurement with the fewest significant figures.
    *   **Addition/Subtraction:** The result should have the same number of decimal places as the measurement with the fewest decimal places.
*   **Why it matters:** Exam questions often specify the required number of significant figures. Incorrect rounding or reporting too many/too few significant figures can lead to lost marks.

**2.4. Measurement and Uncertainty**
*   **Explanation:** All measurements have some degree of uncertainty.
    *   **Resolution:** The smallest change in a quantity that an instrument can detect. For a ruler, it's typically 1 mm. For a micrometer, it's 0.01 mm.
    *   **Accuracy:** How close a measurement is to the true value.
    *   **Precision:** How close repeated measurements are to each other.
    *   **Range:** The maximum and minimum values that can be measured by an instrument.
*   **Types of Errors:**
    *   **Random errors:** Unpredictable variations in measurements (e.g., fluctuations in reading, environmental changes). Reduced by taking multiple readings and averaging.
    *   **Systematic errors:** Consistent errors that affect all measurements in the same way (e.g., faulty calibration, zero error). Reduced by calibrating instruments and correcting for known errors.
    *   **Zero error:** A type of systematic error where an instrument does not read zero when it should. Can be positive (reads above zero) or negative (reads below zero).
*   **Why it matters:** Physics practicals and exam questions require understanding how to use measuring instruments correctly, identify sources of error, and improve the accuracy and reliability of results. The lesson uses virtual simulators for micrometers and Vernier calipers, which are key tools for precise measurement.

**2.5. Volume Formulae**
*   **Explanation:** Basic geometric formulae for calculating the volume of regular shapes.
    *   **Cube:** V = side3
    *   **Cuboid:** V = length $\times$ width $\times$ height
    *   **Cylinder:** V = $\pi r^2$h
    *   **Sphere:** V = (4/3)$\pi$r3
*   **Why it matters:** These formulae are essential for calculating the density of regular solids, as demonstrated in the lesson's core tasks.

**2.6. Density Intuition**
*   **Explanation:** Density is a measure of how much mass is contained in a given volume. Denser objects have more mass packed into the same space.
    *   Liquid water (1000 kg/m^3) is less dense than liquid mercury (13600 kg/m^3).
    *   Wood (e.g., 700 kg/m^3) is less dense than iron (e.g., 7800 kg/m^3).
    *   Air is much less dense than water.
*   **Why it matters:** Having an intuitive understanding of density helps in sanity-checking answers and understanding real-world phenomena like buoyancy. The lesson includes a "Starter" activity to order objects by density.

**2.7. Practical Method Writing**
*   **Explanation:** The ability to clearly and concisely describe experimental procedures, including equipment, measurements, and steps to improve accuracy.
*   **Key elements:**
    *   List equipment with resolution and range.
    *   Provide step-by-step instructions.
    *   Mention how to improve accuracy (e.g., repeat readings, use appropriate instruments).
    *   Identify sources of uncertainty.
*   **Why it matters:** Practical skills are a significant component of A-level Physics. The lesson explicitly covers how to describe experiments for measuring density.

---

### 3. Complete Topic Lecture based on the Video

This section provides a comprehensive lecture on measurement and density, building from first principles and incorporating the specific examples and teaching points from the video.

**3.1. Introduction to Measurement in Physics**

In physics, accurate and precise measurements are fundamental. Every physical quantity we study, from the smallest subatomic particle to the largest galaxy, relies on our ability to measure it. This lesson focuses on two crucial aspects of measurement: using specialized tools like micrometers and Vernier calipers, and applying these measurements to calculate density.

**Aim:** To be able to know how to measure small amounts accurately and describe how to do an experiment.

**3.2. Measuring Small Lengths Accurately**

When measuring small lengths, standard rulers are often insufficient. We need instruments that offer higher resolution and precision. The two primary tools for this are the micrometer screw gauge and the Vernier caliper.

**3.2.1. The Micrometer Screw Gauge**

*   **Purpose:** Used to measure very small lengths, typically up to 25 mm, with a high degree of precision (resolution of 0.01 mm).
*   **Components (as seen in simulator):**
    *   **Anvil:** The fixed jaw.
    *   **Spindle:** The movable jaw, which moves towards or away from the anvil.
    *   **Sleeve (Main Scale):** The stationary part with a linear scale, usually marked in millimeters (mm) and half-millimeters (0.5 mm).
    *   **Thimble (Rotating Scale):** The rotating part with a circular scale, usually divided into 50 or 100 divisions. Each division typically represents 0.01 mm.
    *   **Ratchet Stop:** Ensures consistent pressure is applied to the object being measured, preventing overtightening and damage.
    *   **Spindle Lock:** Locks the spindle in place to hold a measurement.
    *   **Frame:** The C-shaped body that holds all components.

*   **How to Read a Micrometer (as demonstrated by Alex):**
    1.  **Read the Main Scale (Sleeve):**
        *   Identify the last full millimeter mark visible on the sleeve. This gives you the whole number part of your measurement.
        *   Check if the 0.5 mm mark after the last full millimeter is visible. If it is, add 0.5 mm to your reading.
        *   *Example:* If the last visible mm mark is 10, and the 0.5 mm mark after it is visible, your main scale reading is 10.5 mm. If the 0.5 mm mark is not visible, your main scale reading is 10.0 mm.
    2.  **Read the Thimble Scale:**
        *   Identify the division on the thimble scale that aligns exactly with the main scale line (the horizontal line on the sleeve).
        *   Multiply this division number by the resolution (0.01 mm).
        *   *Example:* If the 37th division aligns, your thimble reading is 37 $\times$ 0.01 mm = 0.37 mm.
    3.  **Add the Readings:** Sum the main scale reading and the thimble scale reading.
        *   *Example:* 10.5 mm (main scale) + 0.37 mm (thimble scale) = 10.87 mm.

*   **Common Traps/Tips:**
    *   **Resolution:** Always remember the 0.01 mm resolution.
    *   **Half-millimeter marks:** Pay close attention to whether the 0.5 mm mark is visible past the last full millimeter.
    *   **Zero Error:**
        *   **Positive Zero Error:** When the jaws are closed, the thimble's zero mark is *below* the main scale line. The reading is positive.
        *   **Negative Zero Error:** When the jaws are closed, the thimble's zero mark is *above* the main scale line. The reading is negative (e.g., if it reads 48, it's -0.02 mm).
        *   **Correction:** Actual Reading = Observed Reading - Zero Error.

**3.2.2. The Vernier Caliper**

*   **Purpose:** Used to measure lengths with a precision typically of 0.05 mm or 0.02 mm, often for internal or external dimensions, or depth.
*   **Components (as seen in simulator):**
    *   **Main Scale:** The fixed scale, usually marked in centimeters (cm) and millimeters (mm).
    *   **Vernier Scale (Sliding Scale):** The movable scale that slides along the main scale, typically divided into 10 or 20 divisions.
    *   **Jaws:** Used for measuring outer dimensions (external jaws) and inner dimensions (internal jaws).
    *   **Depth Rod:** Extends from the end of the Vernier scale to measure depth.
    *   **Thumb Screw/Clamp:** Used to slide and lock the Vernier scale.

*   **How to Read a Vernier Caliper (as demonstrated by Alex):**
    1.  **Read the Main Scale:**
        *   Identify the last full millimeter mark on the main scale that is *before* the zero mark of the Vernier scale. This gives you the whole number part of your measurement.
        *   *Example:* If the Vernier zero mark is past 21 mm but not yet at 22 mm, your main scale reading is 21 mm.
    2.  **Read the Vernier Scale:**
        *   Identify the division on the Vernier scale that aligns *exactly* with any line on the main scale.
        *   Multiply this division number by the resolution (e.g., 0.05 mm for a 20-division Vernier scale).
        *   *Example:* If the 6th division aligns, your Vernier reading is 6 $\times$ 0.05 mm = 0.30 mm.
    3.  **Add the Readings:** Sum the main scale reading and the Vernier scale reading.
        *   *Example:* 21 mm (main scale) + 0.30 mm (Vernier scale) = 21.30 mm.

*   **Common Traps/Tips:**
    *   **Resolution:** Be aware of the specific resolution of the Vernier caliper (e.g., 0.05 mm or 0.02 mm).
    *   **Zero Error:** Similar to the micrometer, check for zero error when the jaws are fully closed.
        *   **Positive Zero Error:** Vernier zero mark is *to the right* of the main scale zero.
        *   **Negative Zero Error:** Vernier zero mark is *to the left* of the main scale zero.
        *   **Correction:** Actual Reading = Observed Reading - Zero Error.

**3.3. Density**

**Definition:** Density ($\rho$) is defined as the mass (m) per unit volume (V) of a substance.
*   **Formula:** $\rho$ = m / V
*   **SI Units:**
    *   Mass (m): kilogram (kg)
    *   Volume (V): cubic meter (m^3)
    *   Density ($\rho$): kilogram per cubic meter (kg/m^3)
*   **Other Common Units:** gram per cubic centimeter (g/cm^3).
    *   **Conversion:** 1 g/cm^3 = 1000 kg/m^3 (since 1 g = 10^{-3} kg and 1 cm^3 = (10-2 m)3 = 10^{-6} m^3).

**3.3.1. Measuring Density of a Regular Solid Object**

**Aim:** To be able to describe how to do an experiment to measure the density of a regular solid object.

**Equipment List with Resolution and Range:**
*   **Regular solid object:** (e.g., a cube, cuboid, cylinder, or sphere)
*   **Measuring tool for dimensions:**
    *   **Micrometer screw gauge:** Resolution 0.01 mm, Range 0-25 mm (for very small objects like thin wires or small spheres).
    *   **Vernier caliper:** Resolution 0.05 mm, Range 0-150 mm (for small to medium objects).
    *   **Ruler:** Resolution 1 mm, Range 0-30 cm (for larger objects where precision of mm is sufficient).
*   **Mass balance (digital):** Resolution 0.01 g or 0.001 kg, Range up to 200 g or 2 kg.

**Method:**
1.  **Measure appropriate dimensions of the object:**
    *   For a cube/cuboid: Measure length, width, and height using the most appropriate tool (e.g., Vernier caliper for a small block). Take multiple readings for each dimension at different points and calculate the average to reduce random errors.
    *   For a cylinder: Measure diameter (or radius) and height. Take multiple readings for each and average.
    *   For a sphere: Measure diameter. Take multiple readings and average.
2.  **Calculate the volume (V) of the object:** Use the appropriate geometric formula (e.g., V = lwh for a cuboid, V = (4/3)$\pi$r3 for a sphere). Ensure all dimensions are in consistent units (e.g., meters).
3.  **Measure the mass (m) of the object:** Use a digital mass balance. Record the reading.
4.  **Calculate the density ($\rho$):** Use the formula $\rho$ = m / V.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:**
    *   **Repeat readings:** Take multiple measurements for each dimension and the mass, then calculate the average. This reduces the impact of random errors.
    *   **Use appropriate instruments:** Select the measuring tool with the highest possible resolution for the size of the object (e.g., micrometer for very small dimensions, Vernier caliper for slightly larger ones).
    *   **Check for zero error:** Before taking measurements, check the micrometer/Vernier caliper for zero error and apply any necessary corrections.
    *   **Ensure correct technique:** For calipers, ensure the jaws are perpendicular to the surface and apply consistent pressure. For mass balance, ensure it's on a stable, level surface and zeroed before use.
*   **Residual Errors/Uncertainty:**
    *   **Instrumental uncertainty:** The inherent limit of the instrument's precision (e.g., ±0.01 mm for a micrometer).
    *   **Reading uncertainty:** The uncertainty in reading the scale (often half the smallest division).
    *   **Parallax error:** Error due to reading a scale from an angle (less relevant for digital balances or micrometers).
    *   **Irregularities in the object:** If the object is not perfectly regular, the calculated volume may not be entirely accurate.

**3.3.2. Measuring Density of an Irregular Solid Object**

**Aim:** To be able to describe how to do an experiment to measure the density of an irregular solid object.

**Equipment List with Resolution and Range:**
*   **Irregular solid object:** (e.g., a stone, a key)
*   **Eureka can (displacement can):** Used to collect displaced water.
*   **Measuring cylinder:** Resolution 1 ml or 0.5 ml, Range 0-100 ml (to measure the volume of displaced water).
*   **String:** To suspend the object.
*   **Mass balance (digital):** Resolution 0.01 g or 0.001 kg, Range up to 200 g or 2 kg.
*   **Water:** As the displacement liquid.

**Method:**
1.  **Measure the mass (m) of the object:** Use a digital mass balance. Record the reading.
2.  **Tie a string around the object:** This allows the object to be submerged without touching the sides of the measuring cylinder.
3.  **Fill the Eureka can with water:** Fill it until water just begins to overflow from the spout. Wait until no more water drips out.
4.  **Place a dry measuring cylinder under the spout:** This will collect the displaced water.
5.  **Submerge the object gently into the Eureka can:** Ensure it is fully submerged and no splashing occurs. Collect all the displaced water in the measuring cylinder.
6.  **Record the volume (V) of the displaced water:** The volume of displaced water is equal to the volume of the irregular object (Archimedes' principle).
7.  **Calculate the density ($\rho$):** Use the formula $\rho$ = m / V.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:**
    *   **Repeat readings:** Repeat the entire experiment several times and calculate the average mass and volume.
    *   **Ensure no splashing:** Submerge the object slowly and gently to prevent water from splashing out of the Eureka can.
    *   **Dry the object:** Ensure the object is dry before measuring its mass.
    *   **Read measuring cylinder at eye level:** Avoid parallax error when reading the volume.
    *   **Use a precise measuring cylinder:** Choose one with the smallest possible divisions.
*   **Residual Errors/Uncertainty:**
    *   **Water adhesion:** Some water might stick to the object or the spout, not making it into the measuring cylinder.
    *   **Temperature effects:** Changes in water temperature could slightly affect its density, though usually negligible for this experiment.
    *   **Air bubbles:** Air bubbles trapped on the object when submerged would lead to an overestimation of volume.

**3.3.3. Measuring Density of a Liquid**

**Aim:** To be able to describe how to do an an experiment to measure the density of a liquid.

**Equipment List with Resolution and Range:**
*   **Liquid:** The liquid whose density is to be measured.
*   **Empty measuring cylinder:** Resolution 1 ml or 0.5 ml, Range 0-100 ml.
*   **Mass balance (digital):** Resolution 0.01 g or 0.001 kg, Range up to 200 g or 2 kg.

**Method:**
1.  **Measure the mass of the empty measuring cylinder (m_empty):** Use a digital mass balance. Record the reading.
2.  **Fill the measuring cylinder with the liquid:** Fill it to a specific, easily readable volume (e.g., 50 ml).
3.  **Measure the mass of the full measuring cylinder (m_full):** Use the digital mass balance. Record the reading.
4.  **Record the volume (V_liquid) of the liquid in the measuring cylinder:** Read the volume at eye level to avoid parallax error.
5.  **Calculate the mass of the liquid (m_liquid):** m_liquid = m_full - m_empty.
6.  **Calculate the density ($\rho$):** Use the formula $\rho$ = m_liquid / V_liquid.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:**
    *   **Repeat readings:** Repeat the experiment several times with different volumes of liquid and average the results.
    *   **Use a clean, dry measuring cylinder:** Ensure no residual liquid or contaminants affect the mass or volume.
    *   **Read at eye level:** Avoid parallax error when reading the volume from the measuring cylinder.
    *   **Use a precise mass balance:** Choose one with high resolution.
*   **Residual Errors/Uncertainty:**
    *   **Meniscus reading:** Difficulty in accurately reading the bottom of the meniscus for transparent liquids.
    *   **Evaporation:** Some liquid might evaporate during the measurement process, especially for volatile liquids.

**3.4. Exam Technique for Calculations (as taught by Alex)**

*   **Layout:** Always present your calculations clearly.
    1.  **List Knowns (List Ho):** Write down all given values with their correct units.
    2.  **Equation (Equa):** State the formula you will use.
    3.  **Rearrange (Rearr):** If necessary, rearrange the formula to solve for the unknown variable.
    4.  **Substitute (Subst):** Plug in the numerical values (with units) into the rearranged formula.
    5.  **Answer (Answ):** State the final answer with correct units and appropriate significant figures.
*   **Why it matters:** Examiners award marks for each step (listing knowns, formula, substitution, answer). Skipping steps or having a messy layout can lead to lost marks even if the final answer is correct.
*   **No Blanks:** Attempt every question. For multiple-choice questions, if unsure, make an educated guess last.
*   **Time Management:** Scan the paper first. Tackle easier questions first to build confidence and secure marks. Allocate time based on marks (ee.g., 1 mark per minute).

---

### 4. Exercise-by-Exercise Reconstruction

This section reconstructs the exercises and problems from the video, including Phuc's attempts and Alex's corrections.

**4.1. Micrometer Simulator Readings (00:50 - 00:55)**

*   **Source:** Virtual Micrometer in Hundredths Millimeter - Simulator (`stefanelli.eng.br`).
*   **Prompt:** Read the micrometer.
*   **Prerequisite Idea:** Reading micrometer scales, understanding resolution.

*   **Example 1 (Alex's demonstration):**
    *   **Observed Reading:** Main scale shows 10.5 mm. Thimble scale aligns at 37.
    *   **Phuc's Attempt:** Phuc correctly identifies the main scale reading and the thimble scale reading.
    *   **Step-by-step Solution:**
        1.  Main scale reading: 10.5 mm (last visible 0.5 mm mark).
        2.  Thimble scale reading: 37 divisions $\times$ 0.01 mm/division = 0.37 mm.
        3.  Total reading: 10.5 mm + 0.37 mm = 10.87 mm.
    *   **Final Answer:** 10.87 mm.
    *   **Mark-scheme style notes:** 1 mark for main scale, 1 mark for thimble scale, 1 mark for total.
    *   **Alex's Correction:** Confirms Phuc's reading.

*   **Example 2 (Alex's demonstration):**
    *   **Observed Reading:** Main scale shows 20.5 mm. Thimble scale aligns at 37.
    *   **Phuc's Attempt:** Phuc correctly identifies the main scale reading and the thimble scale reading.
    *   **Step-by-step Solution:**
        1.  Main scale reading: 20.5 mm.
        2.  Thimble scale reading: 37 divisions $\times$ 0.01 mm/division = 0.37 mm.
        3.  Total reading: 20.5 mm + 0.37 mm = 20.87 mm.
    *   **Final Answer:** 20.87 mm.
    *   **Mark-scheme style notes:** 1 mark for main scale, 1 mark for thimble scale, 1 mark for total.
    *   **Alex's Correction:** Confirms Phuc's reading.

*   **Phuc's Mistake/Hesitation (00:57 - 01:00):** Phuc struggles to identify the 0.5 mm mark on the main scale, sometimes reading 10.0 mm when it should be 10.5 mm. He also asks about the "fraction of a millimeter" part.
    *   **What it reveals:** Phuc needs more practice distinguishing between the full millimeter and half-millimeter marks on the sleeve, and correctly combining them with the thimble reading.
    *   **Alex's Correction:** Alex patiently explains the 0.5 mm marks and how they contribute to the reading.
    *   **Drill to fix:** Practice reading micrometers with various settings, specifically focusing on scenarios where the 0.5 mm mark is just visible or just hidden.

**4.2. Vernier Caliper Simulator Readings (01:00 - 01:05)**

*   **Source:** Virtual Vernier Caliper - simulator in 0.05 Millimeter (`stefanelli.eng.br`).
*   **Prompt:** Read the Vernier caliper.
*   **Prerequisite Idea:** Reading Vernier caliper scales, understanding resolution.

*   **Example 1 (Alex's demonstration):**
    *   **Observed Reading:** Vernier zero mark is past 20 mm. The 4th division on the Vernier scale aligns with a main scale line.
    *   **Phuc's Attempt:** Phuc correctly identifies the main scale reading (20 mm) and the aligning Vernier division (4).
    *   **Step-by-step Solution:**
        1.  Main scale reading: 20 mm (last full mm before Vernier zero).
        2.  Vernier scale reading: 4 divisions $\times$ 0.05 mm/division = 0.20 mm.
        3.  Total reading: 20 mm + 0.20 mm = 20.20 mm.
    *   **Final Answer:** 20.20 mm.
    *   **Mark-scheme style notes:** 1 mark for main scale, 1 mark for Vernier scale, 1 mark for total.
    *   **Alex's Correction:** Confirms Phuc's reading.

*   **Phuc's Mistake/Hesitation (01:02 - 01:04):** Phuc asks for clarification on which line to look at on the Vernier scale.
    *   **What it reveals:** Phuc needs to solidify the rule for identifying the aligning line on the Vernier scale.
    *   **Alex's Correction:** Alex reiterates that it's the line on the Vernier scale that perfectly matches *any* line on the main scale.
    *   **Drill to fix:** Practice with more Vernier caliper examples, specifically focusing on identifying the aligning line.

**4.3. Core Task 1: Whiskey Density (01:20 - 01:25)**

*   **Source:** OneNote "Core task" section.
*   **Prompt:** "A bottle of whiskey contains 1 litre of the drink. The mass of the liquid in the bottle is 0.915 kg. What is the density of this brand of whiskey? (1000 litres = 1 m^3)"
*   **Prerequisite Idea:** Density formula, unit conversions (litres to m^3).

*   **Phuc's Attempt (visible in video, partially written):**
    *   List Ho: V = 1 L = 1 x 10^{-3} m^3, m = 0.915 kg, $\rho$ = ?
    *   Equa: $\rho$ = m/V
    *   Subst: $\rho$ = 0.915 / (1 x 10^{-3})
    *   Answ: $\rho$ = 915 kg m^{-3}
*   **Step-by-step Solution:**
    1.  **List Knowns:**
        *   Volume (V) = 1 litre = 1 $\times$ 10^{-3} m^3 (given conversion: 1000 litres = 1 m^3)
        *   Mass (m) = 0.915 kg
        *   Density ($\rho$) = ?
    2.  **Equation:** $\rho$ = m / V
    3.  **Substitute:** $\rho$ = 0.915 kg / (1 $\times$ 10^{-3} m^3)
    4.  **Calculate:** $\rho$ = 915 kg/m^3
    5.  **Answer:** The density of the whiskey is 915 kg/m^3.
*   **Final Answer:** 915 kg/m^3.
*   **Mark-scheme style notes:**
    *   1 mark for correct conversion of volume to m^3.
    *   1 mark for correct formula.
    *   1 mark for correct substitution.
    *   1 mark for correct final answer with units.
*   **Phuc's Mistake/Hesitation:** Phuc initially writes 0.915 / 10^{-3} but then corrects it to 915.
    *   **What it reveals:** Minor arithmetic or calculator input error, quickly self-corrected.
    *   **Alex's Correction:** Confirms the correct calculation and units.
    *   **Drill to fix:** N/A (self-corrected).

**4.4. Core Task 2: Hockey Ball Density (01:20 - 01:25)**

*   **Source:** OneNote "Core task" section.
*   **Prompt:** "The radius of a hockey ball is 36 mm and its mass is 160 g. What is its density (a) in g cm^{-3}? (b) in kg m^{-3}?"
*   **Prerequisite Idea:** Volume of a sphere, unit conversions (mm to cm/m, g to kg).

*   **Phuc's Attempt (visible in video, partially written):**
    *   r = 36 mm = 3.6 cm = 0.036 m
    *   m = 160 g = 0.160 kg
    *   V = (4/3)$\pi$r3
    *   (a) V = (4/3)$\pi$(3.6)3 = 195.43 cm^3
    *   $\rho$ = 160 / 195.43 = 0.818 g cm^{-3}
    *   (b) V = (4/3)$\pi$(0.036)3 = 1.9543 x 10^{-4} m^3
    *   $\rho$ = 0.160 / (1.9543 x 10^{-4}) = 818.7 kg m^{-3}
*   **Step-by-step Solution:**
    1.  **List Knowns:**
        *   Radius (r) = 36 mm
        *   Mass (m) = 160 g
    2.  **Conversions:**
        *   r = 36 mm = 3.6 cm = 0.036 m
        *   m = 160 g = 0.160 kg
    3.  **Equation for Volume of a Sphere:** V = (4/3)$\pi$r3
    4.  **Part (a) - Density in g cm^{-3}:**
        *   Calculate Volume in cm^3: V = (4/3)$\pi$(3.6 cm)3 $\approx$ 195.43 cm^3
        *   Calculate Density: $\rho$ = 160 g / 195.43 cm^3 $\approx$ 0.819 g cm^{-3} (3 s.f.)
    5.  **Part (b) - Density in kg m^{-3}:**
        *   Calculate Volume in m^3: V = (4/3)$\pi$(0.036 m)3 $\approx$ 1.9543 $\times$ 10^{-4} m^3
        *   Calculate Density: $\rho$ = 0.160 kg / (1.9543 $\times$ 10^{-4} m^3) $\approx$ 818.7 kg m^{-3} $\approx$ 819 kg m^{-3} (3 s.f.)
*   **Final Answer:** (a) 0.819 g cm^{-3}, (b) 819 kg m^{-3}.
*   **Mark-scheme style notes:**
    *   1 mark for correct unit conversions (mm to cm/m, g to kg).
    *   1 mark for correct volume formula.
    *   1 mark for correct calculation of volume.
    *   1 mark for correct density calculation in g cm^{-3}.
    *   1 mark for correct density calculation in kg m^{-3}.
*   **Phuc's Mistake/Hesitation:** Phuc correctly performs the calculations.
    *   **What it reveals:** Good understanding of formula application and unit conversion.
    *   **Alex's Correction:** Confirms the correct calculations.
    *   **Drill to fix:** N/A.

**4.5. Core Task 3: Estimate Mass of Air in Room (01:20 - 01:25)**

*   **Source:** OneNote "Core task" section.
*   **Prompt:** "Estimate the mass of air in this room."
*   **Prerequisite Idea:** Density of air (requires external knowledge or estimation), volume of a room (estimation).

*   **Phuc's Attempt:** Not explicitly shown in the video.
*   **Step-by-step Solution (Example):**
    1.  **Estimate Room Dimensions:** Assume a typical room size, e.g., Length = 5 m, Width = 4 m, Height = 2.5 m.
    2.  **Calculate Room Volume:** V = 5 m $\times$ 4 m $\times$ 2.5 m = 50 m^3.
    3.  **Recall/Estimate Density of Air:** The density of air at standard temperature and pressure is approximately 1.2 kg/m^3.
    4.  **Equation for Mass:** m = $\rho$ $\times$ V
    5.  **Substitute and Calculate:** m = 1.2 kg/m^3 $\times$ 50 m^3 = 60 kg.
    6.  **Answer:** The estimated mass of air in the room is 60 kg.
*   **Final Answer:** Approximately 60 kg (depends on estimated room dimensions).
*   **Mark-scheme style notes:**
    *   1 mark for reasonable estimation of room dimensions.
    *   1 mark for correct volume calculation.
    *   1 mark for reasonable density of air.
    *   1 mark for correct mass calculation.
*   **Phuc's Mistake/Hesitation:** N/A.
    *   **What it reveals:** This is an estimation problem, testing practical application of density.
    *   **Alex's Correction:** N/A.
    *   **Drill to fix:** Practice estimation problems, focusing on making reasonable assumptions for unknown values.

**4.6. Core Task 4: Spherical Balloon Density (01:20 - 01:25)**

*   **Source:** OneNote "Core task" section.
*   **Prompt:** "A spherical balloon of radius 20 cm contains 50 g of air. a) Calculate the density of air in the balloon. b) Comment on why it differs from that given in Table 12.1 (page 177) (Total 3 Marks)"
*   **Prerequisite Idea:** Volume of a sphere, unit conversions (cm to m, g to kg), understanding factors affecting air density.

*   **Phuc's Attempt (visible in video, partially written):**
    *   r = 20 cm = 0.20 m
    *   m = 50 g = 0.05 kg
    *   V = (4/3)$\pi$r3
    *   V = (4/3)$\pi$(0.20)3 = 0.0335 m^3
    *   $\rho$ = 0.05 kg / 0.0335 m^3 = 1.49 kg m^{-3}
*   **Step-by-step Solution:**
    1.  **List Knowns:**
        *   Radius (r) = 20 cm
        *   Mass (m) = 50 g
    2.  **Conversions:**
        *   r = 20 cm = 0.20 m
        *   m = 50 g = 0.05 kg
    3.  **Equation for Volume of a Sphere:** V = (4/3)$\pi$r3
    4.  **Part (a) - Calculate Density:**
        *   Calculate Volume: V = (4/3)$\pi$(0.20 m)3 $\approx$ 0.03351 m^3
        *   Calculate Density: $\rho$ = 0.05 kg / 0.03351 m^3 $\approx$ 1.49 kg m^{-3} (3 s.f.)
    5.  **Part (b) - Comment on Difference:**
        *   The density of air in Table 12.1 (standard air density) is typically around 1.2 kg/m^3.
        *   The calculated density (1.49 kg/m^3) is higher.
        *   **Reason:** The balloon is likely inflated to a pressure higher than normal atmospheric pressure. Increased pressure means more air molecules are packed into the same volume, leading to higher density. Temperature could also play a role (cooler air is denser), but pressure is the more direct cause of a significant increase in a balloon.
*   **Final Answer:** (a) 1.49 kg m^{-3}, (b) The air in the balloon is likely under higher pressure than standard atmospheric pressure, causing it to be denser.
*   **Mark-scheme style notes:**
    *   1 mark for correct unit conversions and volume calculation.
    *   1 mark for correct density calculation.
    *   1 mark for a valid comment on the difference (e.g., higher pressure).
*   **Phuc's Mistake/Hesitation:** Phuc correctly performs the calculations.
    *   **What it reveals:** Good understanding of formula application and unit conversion.
    *   **Alex's Correction:** Confirms the correct calculations and guides Phuc on the explanation for part (b).
    *   **Drill to fix:** N/A.

**4.7. Further Task 2: Brass Alloy Density (01:30 - 01:35)**

*   **Source:** OneNote "Further tasks" section.
*   **Prompt:** "Q2. (a) Define the density of a material. (1) (b) Brass, an alloy of copper and zinc, consists of 70% by volume of copper and 30% by volume of zinc. density of copper = 8.9 x 10^3 kg m^{-3} density of zinc = 7.1 x 10^3 kg m^{-3} (i) Determine the mass of copper and the mass of zinc required to make a rod of brass of volume 0.80 x 10^{-3} m^3. (ii) Calculate the density of brass. (Total 5 Marks)"
*   **Prerequisite Idea:** Definition of density, density formula, calculating partial volumes and masses in an alloy.

*   **Phuc's Attempt (visible in video, partially written):**
    *   (a) Density is the mass per unit volume.
    *   (b)(i) VT = 0.80 x 10^{-3} m^3
        *   VC = 0.7 $\times$ 0.80 x 10^{-3} m^3 = 0.56 x 10^{-3} m^3
        *   VZ = 0.3 $\times$ 0.80 x 10^{-3} m^3 = 0.24 x 10^{-3} m^3
        *   MC = $\rho$C $\times$ VC = 8.9 $\times 10^3$ kg m^{-3} $\times$ 0.56 $\times$ 10^{-3} m^3 = 4.984 kg
        *   MZ = $\rho$Z $\times$ VZ = 7.1 $\times 10^3$ kg m^{-3} $\times$ 0.24 $\times$ 10^{-3} m^3 = 1.704 kg
    *   (b)(ii) $\rho$_brass = (MC + MZ) / VT = (4.984 + 1.704) / (0.80 x 10^{-3}) = 8360 kg m^{-3}
*   **Step-by-step Solution:**
    1.  **Part (a) - Define Density:**
        *   Density is the mass per unit volume.
    2.  **Part (b)(i) - Determine Mass of Copper and Zinc:**
        *   **List Knowns:**
            *   Total Volume (VT) = 0.80 $\times$ 10^{-3} m^3
            *   Copper volume % = 70%
            *   Zinc volume % = 30%
            *   Density of Copper ($\rho$C) = 8.9 $\times 10^3$ kg m^{-3}
            *   Density of Zinc ($\rho$Z) = 7.1 $\times 10^3$ kg m^{-3}
        *   **Calculate Volume of Copper (VC):** VC = 0.70 $\times$ VT = 0.70 $\times$ (0.80 $\times$ 10^{-3} m^3) = 0.56 $\times$ 10^{-3} m^3
        *   **Calculate Volume of Zinc (VZ):** VZ = 0.30 $\times$ VT = 0.30 $\times$ (0.80 $\times$ 10^{-3} m^3) = 0.24 $\times$ 10^{-3} m^3
        *   **Calculate Mass of Copper (MC):** MC = $\rho$C $\times$ VC = (8.9 $\times 10^3$ kg m^{-3}) $\times$ (0.56 $\times$ 10^{-3} m^3) = 4.984 kg
        *   **Calculate Mass of Zinc (MZ):** MZ = $\rho$Z $\times$ VZ = (7.1 $\times 10^3$ kg m^{-3}) $\times$ (0.24 $\times$ 10^{-3} m^3) = 1.704 kg
    3.  **Part (b)(ii) - Calculate Density of Brass:**
        *   **Total Mass (MT):** MT = MC + MZ = 4.984 kg + 1.704 kg = 6.688 kg
        *   **Density of Brass ($\rho$_brass):** $\rho$_brass = MT / VT = 6.688 kg / (0.80 $\times$ 10^{-3} m^3) = 8360 kg m^{-3}
*   **Final Answer:** (a) Mass per unit volume. (b)(i) Mass of copper = 4.98 kg, Mass of zinc = 1.70 kg. (b)(ii) Density of brass = 8360 kg m^{-3}.
*   **Mark-scheme style notes:**
    *   (a) 1 mark for definition.
    *   (b)(i) 1 mark for calculating VC, 1 mark for calculating VZ, 1 mark for calculating MC, 1 mark for calculating MZ.
    *   (b)(ii) 1 mark for calculating total mass, 1 mark for final density with units.
*   **Phuc's Mistake/Hesitation:** Phuc correctly performs all steps and calculations.
    *   **What it reveals:** Strong understanding of multi-step density problems and working with percentages by volume.
    *   **Alex's Correction:** Confirms the correct calculations.
    *   **Drill to fix:** N/A.

---

### 5. Diagram and Visual Inventory

This section lists and describes all significant diagrams and visuals presented in the video.

1.  **Loom Video Thumbnail: "Dividing Test Time by Marks"**
    *   **Timestamp:** 00:00 - 00:02, 00:26 - 00:30
    *   **What it shows:** A screenshot of a Loom video player with a title "Dividing Test Time by Marks". The video features Alex Kealy speaking.
    *   **Labels/Values:** "14 min" (video length), "0 views".
    *   **Teaching Purpose:** Introduces the concept of exam time management, which is a meta-skill for physics exams.
    *   **How to Redraw:** A simple screenshot of a video player with the title and play button.

    *   **Timestamp:** 00:03 - 00:06
    *   **Labels/Values:** Numerical values related to model parameters.
    *   **Teaching Purpose:** Shows Phuc's engagement in technical discussions outside of physics, highlighting his analytical skills.

    *   **Timestamp:** 00:06 - 00:10, 01:01 - 01:02
    *   **Labels/Values:** Email subject, sender, recipient, body text.
    *   **Teaching Purpose:** Contextualizes Phuc's request for book names and study materials.
    *   **How to Redraw:** A standard email interface showing the subject, sender, recipient, and body text.

    *   **Timestamp:** 00:16 - 00:19
    *   **Labels/Values:** Channel name, options, message text.
    *   **Teaching Purpose:** Shows Phuc's proactive approach to organizing his studies.

5.  **OneNote Page: "January 2023 (IAL) QP" - Exam Technique Notes**
    *   **Timestamp:** 00:30 - 00:36
    *   **What it shows:** A OneNote page with handwritten notes on exam technique, followed by the first page of a Pearson Edexcel International Advanced Level Physics paper (WPH11/01).
    *   **Labels/Values:**
        *   "Scan - 80 marks 90 mins = 1 mark per min"
        *   "Easy ones first half paper in 30 mins = 1 mark per 2 mins"
        *   "Write answer SO THE EXAMINER GIVES YOU MARKS"
        *   "No blanks - multiple choice LAST"
        *   "UNIT 1: Mechanics and Materials"
        *   "Time 1 hour 30 minutes"
        *   "Total Mark for this paper is 80."
    *   **Teaching Purpose:** Provides explicit advice on exam strategy and layout.
    *   **How to Redraw:** A OneNote page with handwritten text and a partial view of an exam paper.

6.  **PDF: "Edexcel A-Level Physics Year 1.pdf" (Cover and Contents)**
    *   **Timestamp:** 00:40 - 00:45
    *   **What it shows:** The cover page of the Edexcel A-Level Physics Year 1 textbook, followed by its table of contents.
    *   **Labels/Values:** "PHYSICS 1 Includes AS level", "Mike Benn Graham George", "Contents" with sections like "Mechanics", "Electric Circuits", "Materials", "Waves and the Particle Behaviour of Light".
    *   **Teaching Purpose:** Identifies the core textbook used for the lessons.
    *   **How to Redraw:** The book cover and a page from the table of contents.

7.  **Web Page: "A-Level Physics Study Plan"**
    *   **Timestamp:** 00:45 - 00:50
    *   **What it shows:** A Notion-like web page titled "A-Level Physics Study Plan" with sections for "Phase 1: Content Coverage", "Phase 2: A/A* Practice", "Phase 3: A* Polish". It lists chapters with target dates and completion status.
    *   **Labels/Values:** "Current Phase: Content", "Week 7", "Days until exam: 242", "Total Prep Time: 41 weeks", "Progress by Topic" (Mechanics, Waves, E&M Fields, Thermo, Circuits, Further Mech, Particles, Oscillations, Materials, Astro, Nuclear Decay), "Exam Papers" with dates.
    *   **Teaching Purpose:** Demonstrates Phuc's structured approach to revision and allows tracking progress.
    *   **How to Redraw:** A dashboard-style layout with progress bars, chapter lists, and exam dates.

8.  **Web Page: "Virtual Micrometer in Hundredths Millimeter - Simulator"**
    *   **Timestamp:** 00:50 - 00:55
    *   **What it shows:** An interactive simulator for a micrometer screw gauge. It displays the main scale and thimble scale, with draggable elements to change the reading.
    *   **Labels/Values:** "0-25mm", "0.01mm", "drag me vertically", "drag me horizontally", numerical reading (e.g., 10.87).
    *   **Teaching Purpose:** Provides a hands-on way to learn and practice reading micrometer measurements.
    *   **How to Redraw:** A clear diagram of a micrometer with its scales, showing an example reading.

9.  **Web Page: "Virtual Vernier Caliper - simulator in 0.05 Millimeter"**
    *   **Timestamp:** 00:55 - 01:00
    *   **What it shows:** An interactive simulator for a Vernier caliper. It displays the main scale and Vernier scale, with draggable jaws.
    *   **Labels/Values:** "0.05 Millimeter", numerical reading (e.g., 20.20).
    *   **Teaching Purpose:** Provides a hands-on way to learn and practice reading Vernier caliper measurements.
    *   **How to Redraw:** A clear diagram of a Vernier caliper with its scales, showing an example reading.

10. **OneNote Page: "1 - Measuring" - Micrometer and Vernier Caliper Worksheets**
    *   **Timestamp:** 01:00 - 01:05
    *   **What it shows:** A OneNote page with multiple diagrams of micrometers and Vernier calipers, each requiring the "Actual Reading". Some examples have handwritten solutions and zero error calculations.
    *   **Labels/Values:** "Zero Error = +0.02 mm", "Actual Reading = 0.57 mm".
    *   **Teaching Purpose:** Provides practice exercises for reading measurement tools and understanding zero error.
    *   **How to Redraw:** Select a few representative diagrams of micrometers and Vernier calipers, showing the scales and an example reading. Include a section for zero error.

11. **OneNote Page: "2 - Measuring Density" - Regular Object Method**
    *   **Timestamp:** 01:05 - 01:10
    *   **What it shows:** A OneNote page outlining the method for measuring the density of a regular object. Includes a handwritten drawing of a cube.
    *   **Labels/Values:** "Equipment list with resolution and range:", "Method: 1) measure appropriate dimensions... 2) measure mass of object", "using mass balance".
    *   **Teaching Purpose:** Explains the experimental procedure for regular solids.
    *   **How to Redraw:** A clear diagram of a cube with labeled dimensions (l, w, h).

12. **OneNote Page: "2 - Measuring Density" - Irregular Object Method**
    *   **Timestamp:** 01:10 - 01:15
    *   **What it shows:** A OneNote page outlining the method for measuring the density of an irregular object. Includes a handwritten drawing of a Eureka can and measuring cylinder.
    *   **Labels/Values:** "Method: 1) measure mass of object 2) tie string round object 3) fill measuring cylinder with water 4) record the volume 5) submerge object... record new volume", "collect water in measuring cylinder".
    *   **Teaching Purpose:** Explains the experimental procedure for irregular solids using displacement.
    *   **How to Redraw:** A diagram of a Eureka can with a measuring cylinder collecting displaced water, and an irregular object suspended by a string.

13. **OneNote Page: "2 - Measuring Density" - Liquid Density Method**
    *   **Timestamp:** 01:15 - 01:20
    *   **What it shows:** A OneNote page outlining the method for measuring the density of a liquid. Includes a handwritten drawing of a measuring cylinder on a mass balance.
    *   **Labels/Values:** "Method: 1) measure mass of empty measuring cylinder 2) fill measuring cylinder with liquid 3) measure mass of full measuring cylinder 4) record volume of liquid", "mass balance", "100 cm^3 measuring cylinder".
    *   **Teaching Purpose:** Explains the experimental procedure for liquids.
    *   **How to Redraw:** A diagram of a measuring cylinder on a mass balance, with liquid inside.

14. **OneNote Page: "Core Task" - Density Calculation Problems (with solutions)**
    *   **Timestamp:** 01:20 - 01:25, 01:30 - 01:35
    *   **What it shows:** The core task problems with handwritten solutions, including listed knowns, formulas, substitutions, and answers.
    *   **Labels/Values:** All problem prompts, handwritten calculations, units, and final answers.
    *   **Teaching Purpose:** Provides worked examples for density calculations.
    *   **How to Redraw:** Each problem with its step-by-step solution clearly laid out.

15. **OneNote Page: "Further Tasks" - Seismometer Diagram**
    *   **Timestamp:** 01:25 - 01:30
    *   **What it shows:** A diagram of a seismometer with a rotating drum, pen, spring, heavy ball, and labeled dimensions (3.0 cm, 8.0 cm).
    *   **Labels/Values:** "Axis of rotation", "spring", "pen", "rotating drum", "heavy ball", "3.0 cm", "8.0 cm".
    *   **Teaching Purpose:** Introduces a more complex physics problem involving oscillations and measurement.
    *   **How to Redraw:** A clear, labeled diagram of the seismometer.

16. **Pearson Edexcel A-Level Physics Data, Formulae and Relationships Booklet**
    *   **Timestamp:** 01:45 - 01:50
    *   **What it shows:** The official formula booklet for Edexcel A-Level Physics.
    *   **Teaching Purpose:** Highlights the importance of knowing what formulas are provided in the exam and how to use them.
    *   **How to Redraw:** The cover page and a sample page showing a list of constants and formulas.

---

### 6. Phuc-Specific Mistake and Misconception Bank

This section compiles Phuc's specific mistakes, hesitations, and misconceptions observed in the video, along with Alex's corrections and suggested drills.

1.  **Misconception: Micrometer 0.5 mm mark reading**
    *   **Timestamp:** 00:57 - 01:00
    *   **Phuc's Action/Statement:** Phuc struggles to consistently identify and incorporate the 0.5 mm mark on the micrometer's sleeve scale into his reading. He sometimes reads 10.0 mm when the mark is visible, indicating 10.5 mm. He asks for clarification on the "fraction of a millimeter" part.
    *   **What it reveals:** Phuc has a foundational misunderstanding of how the 0.5 mm increments on the main scale contribute to the total reading, especially when combined with the thimble scale.
    *   **Alex's Correction:** Alex patiently explains that each full line on the sleeve is 1 mm, and the smaller lines between them are 0.5 mm. He emphasizes checking if the 0.5 mm mark is visible past the last full millimeter.
    *   **Drill to fix:**
        *   **Targeted Practice:** Use the virtual micrometer simulator. Focus specifically on settings where the 0.5 mm mark is either just visible or just hidden. Practice reading these scenarios until consistent.
        *   **Verbalization:** For each reading, Phuc should verbally state: "The last full millimeter visible is X. The 0.5 mm mark is/is not visible, so the main scale reading is X.0 or X.5. The thimble scale aligns at Y, so that's Y times 0.01 mm. Total is..."

2.  **Hesitation: Vernier Caliper aligning line**
    *   **Timestamp:** 01:02 - 01:04
    *   **Phuc's Action/Statement:** Phuc asks, "Which one do we look from here? This one is one..." indicating uncertainty about which line on the Vernier scale to use for the decimal reading.
    *   **What it reveals:** Phuc understands the concept of finding an aligning line but might be unsure if it has to be a specific line or any aligning line.
    *   **Alex's Correction:** Alex clarifies that it's *any* line on the Vernier scale that aligns perfectly with *any* line on the main scale.
    *   **Drill to fix:**
        *   **Visual Identification:** Practice with the virtual Vernier caliper simulator. Focus on identifying the single best-aligned line on the Vernier scale. Use the magnifying glass feature if available.
        *   **Comparison:** Compare different Vernier caliper diagrams where various lines align, to reinforce the rule.

3.  **Misconception: Skipping steps in exam calculations**
    *   **Timestamp:** 01:20 - 01:25 (implied by Alex's emphasis on layout), 02:05 - 02:10 (Phuc mentions getting it wrong and losing marks).
    *   **Phuc's Action/Statement:** Phuc mentions that in his exams, he sometimes gets things wrong and loses marks. Alex later emphasizes a structured layout.
    *   **What it reveals:** Phuc might be tempted to combine steps or not explicitly state formulas/conversions, especially under time pressure, leading to loss of method marks.
    *   **Alex's Correction:** Alex explicitly teaches a structured layout: "List Ho (Knowns), Equa (Equation), Rearr (Rearrange), Subst (Substitute), Answ (Answer)". He states, "Write answer SO THE EXAMINER GIVES YOU MARKS."
    *   **Drill to fix:**
        *   **Mandatory Layout Practice:** For every calculation problem, Phuc must strictly follow the "List Ho, Equa, Rearr, Subst, Answ" layout. No exceptions.
        *   **Marking Practice:** Phuc should self-mark his solutions using a mock mark scheme, specifically checking for method marks awarded for each step.

4.  **Hesitation: Unit conversions for density problems**
    *   **Timestamp:** 01:20 - 01:25 (Core Task 1 & 2)
    *   **Phuc's Action/Statement:** Phuc initially writes 1 L as 10^{-3} m^3 but then hesitates slightly before confirming. For the hockey ball, he correctly converts mm to cm/m and g to kg.
    *   **What it reveals:** While Phuc generally knows conversions, there might be slight hesitation or a need to double-check, especially for less common ones (like L to m^3).
    *   **Alex's Correction:** Alex confirms the conversions and emphasizes using consistent SI units. He points to the formula booklet for reference.
    *   **Drill to fix:**
        *   **Conversion Table Drill:** Create a table of common physics unit conversions (length, mass, volume, density) and practice converting values back and forth quickly.
        *   **Formula Sheet Familiarity:** Regularly review the formula booklet to know which conversions and constants are provided.

5.  **Misconception: Factors affecting air density in a balloon**
    *   **Timestamp:** 01:20 - 01:25 (Core Task 4, part b)
    *   **Phuc's Action/Statement:** After calculating the density of air in the balloon, Phuc needs to comment on why it differs from the standard value. He might initially think of temperature.
    *   **What it reveals:** Phuc needs to consider the primary factors that influence gas density in a confined space like a balloon.
    *   **Alex's Correction:** Alex guides Phuc to consider pressure. A balloon is typically inflated to a pressure higher than atmospheric pressure, which packs more air molecules into the same volume, increasing density.
    *   **Drill to fix:**
        *   **Conceptual Question:** "List and explain the factors that affect the density of a gas, and how each factor would change the density."
        *   **Application Problem:** "If a balloon is taken from sea level to a high altitude, how would the density of the air inside (assuming it's sealed) and outside the balloon change, and why?"

---

### 7. Exam Technique and Practical Wording

This section extracts and formalizes the exam technique advice and practical method writing from the video, tailored for Edexcel A-level Physics.

**7.1. General Exam Technique Advice**

*   **Paper Scan (Initial Strategy):**
    *   **Advice:** "Scan - 80 marks 90 mins = 1 mark per min". "Easy ones first half paper in 30 mins = 1 mark per 2 mins".
    *   **Edexcel A-level Wording:** Upon receiving the examination paper, candidates should allocate approximately 1 minute per mark. It is advisable to quickly scan the entire paper to identify questions that can be answered efficiently, prioritizing these to secure initial marks. For longer, more complex questions, allocate time proportionally to the marks awarded.
*   **Answering Strategy:**
    *   **Advice:** "Write answer SO THE EXAMINER GIVES YOU MARKS". "No blanks - multiple choice LAST".
    *   **Edexcel A-level Wording:** Candidates must show all working clearly, as marks are awarded for method, formula, and substitution, not just the final answer. Even if the final answer is incorrect, correct working may still earn marks. Do not leave any questions unanswered; attempt all questions, making an educated guess for multiple-choice questions if time is running out.
*   **Layout for Calculations (Crucial for Method Marks):**
    *   **Advice:** "List Ho (Knowns), Equa (Equation), Rearr (Rearrange), Subst (Substitute), Answ (Answer)".
    *   **Edexcel A-level Wording:** For all numerical calculations, a clear and logical presentation is essential. Follow these steps:
        1.  **List Given Data:** Clearly state all known quantities with their correct SI units.
        2.  **State Formula:** Write down the relevant physical formula to be used.
        3.  **Rearrange Formula (if necessary):** Manipulate the formula algebraically to isolate the unknown variable.
        4.  **Substitute Values:** Insert the numerical values (with units) into the rearranged formula.
        5.  **Calculate and State Final Answer:** Perform the calculation and present the final answer with appropriate units and to an appropriate number of significant figures (usually matching the least precise input value, or as specified in the question).

**7.2. Model Practical Method Paragraphs (Measuring Density)**

Practical work at A-Level is very similar to GCSE, but you will just need to include more accurate numbers, more idea of errors, uncertainties, and how to reduce them. Focus today: **accuracy**.

**A) Measuring Density of a Regular Object (e.g., a metal cube)**

**Equipment List with Resolution and Range:**
*   Metal cube (regular solid object)
*   Vernier caliper (resolution: ±0.05 mm, range: 0-150 mm)
*   Digital mass balance (resolution: ±0.01 g, range: 0-200 g)

**Method:**
1.  **Measure the dimensions:** Use the Vernier caliper to measure the length, width, and height of the metal cube. Take three readings for each dimension at different points on the cube to account for any slight irregularities and reduce random errors. Record these readings in a table.
2.  **Calculate average dimensions:** For each dimension (length, width, height), calculate the average of the three readings.
3.  **Calculate the volume:** Use the formula V = average length $\times$ average width $\times$ average height. Ensure all dimensions are converted to metres (m) before calculating the volume in cubic metres (m^3).
4.  **Measure the mass:** Place the metal cube on the digital mass balance and record its mass in kilograms (kg). Ensure the balance is zeroed before use.
5.  **Calculate the density:** Use the formula $\rho$ = mass / volume.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:** Taking multiple readings for each dimension and calculating the average helps to minimise the effect of random errors. Using a Vernier caliper provides a higher resolution (±0.05 mm) compared to a standard ruler, leading to more precise measurements of the dimensions. Ensuring the Vernier caliper is checked for zero error and corrected if necessary would eliminate systematic error.
*   **Residual Errors:** Even with careful measurement, slight imperfections in the regularity of the cube's shape could introduce a small unquantifiable error in the calculated volume. The inherent instrumental uncertainty of the Vernier caliper and mass balance (e.g., ±0.05 mm and ±0.01 g respectively) also contributes to the overall uncertainty in the final density value.

**B) Measuring Density of an Irregular Object (e.g., a stone)**

**Equipment List with Resolution and Range:**
*   Irregular stone
*   Eureka can (displacement can)
*   Measuring cylinder (resolution: ±1 ml, range: 0-100 ml)
*   Thin string
*   Digital mass balance (resolution: ±0.01 g, range: 0-200 g)
*   Water

**Method:**
1.  **Measure the mass:** Place the dry irregular stone on the digital mass balance and record its mass in kilograms (kg).
2.  **Prepare the Eureka can:** Fill the Eureka can with water until it just begins to overflow from the spout. Wait until no more water drips out, ensuring the water level is exactly at the spout's level.
3.  **Collect displaced water:** Place a dry measuring cylinder directly under the spout of the Eureka can.
4.  **Submerge the object:** Gently lower the irregular stone into the Eureka can using the thin string, ensuring it is fully submerged and no water splashes out.
5.  **Record the volume:** Once no more water drips from the spout, read the volume of the collected water in the measuring cylinder. This volume, in cubic metres (m^3), represents the volume of the stone.
6.  **Calculate the density:** Use the formula $\rho$ = mass / volume.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:** Gently lowering the object and waiting for all drips to cease minimises water loss due to splashing or incomplete displacement. Reading the measuring cylinder at eye level reduces parallax error. Repeating the experiment multiple times and averaging the volume of displaced water would reduce random errors.
*   **Residual Errors:** Some water may adhere to the string or the object itself, leading to a slight underestimation of the displaced volume. Air bubbles trapped on the surface of the irregular object during submersion would lead to an overestimation of its volume. These are difficult to quantify precisely.

**C) Measuring Density of a Liquid (e.g., water)**

**Equipment List with Resolution and Range:**
*   Liquid (e.g., water)
*   Measuring cylinder (resolution: ±1 ml, range: 0-100 ml)
*   Digital mass balance (resolution: ±0.01 g, range: 0-200 g)

**Method:**
1.  **Measure mass of empty cylinder:** Place the clean, dry measuring cylinder on the digital mass balance and record its mass (m_empty) in kilograms (kg).
2.  **Fill with liquid:** Carefully pour the liquid into the measuring cylinder up to a specific, easily readable volume (e.g., 50 ml). Read the volume (V_liquid) at eye level to avoid parallax error.
3.  **Measure mass of full cylinder:** Place the measuring cylinder with the liquid back on the digital mass balance and record its mass (m_full) in kilograms (kg).
4.  **Calculate mass of liquid:** Determine the mass of the liquid (m_liquid) by subtracting the mass of the empty cylinder from the mass of the full cylinder: m_liquid = m_full - m_empty.
5.  **Calculate the density:** Use the formula $\rho$ = m_liquid / V_liquid.

**Evaluation - What practical steps did you take to improve accuracy? Were there any residual errors you couldn't quantify?**
*   **Improving Accuracy:** Using a clean and dry measuring cylinder ensures that no contaminants affect the mass or volume. Reading the volume at the bottom of the meniscus (for water) at eye level minimises parallax error. Repeating the experiment with different volumes of liquid and averaging the calculated densities would reduce random errors.
*   **Residual Errors:** The precision of reading the meniscus in the measuring cylinder (e.g., ±1 ml) is a significant source of uncertainty. For volatile liquids, evaporation during the measurement process could lead to a slight underestimation of mass.

---


# Lesson 2: Hooke's law, stress, strain and Young modulus complete video-grounded lecture

The following section is the detailed video-grounded source pack from the Hooke's Law / Stress / Strain / Young Modulus lesson. It includes the chronological walkthrough, full topic explanation, exercises, Phuc's mistakes, tutor corrections, practical wording and redo tasks.

# A-Level Physics Revision Guide: Hooke's Law, Stress, Strain, and Young's Modulus

## 1. Chronological Walkthrough by Timestamp

**00:00 - 00:30: Introduction to Power Exam Questions**
*   **Screen State:** OneNote showing "Phuc-Physics" notebook. Left sidebar shows sections: "1 - Mechanics", "2 - Work Energy and...", "1b - Materials", "2a - Waves", "2b - Electricity", "New Section 1-4". "3 - Power" is highlighted. Main pane shows "Power Exam Qs.docx" and "Power Exam Qs.pdf" files. Google Meet window on the right shows Alex (tutor) and Phuc (student).
*   **Alex Teaching:** Discussing the "Power Exam Qs" document, mentioning it has detail and a practical. He decides to move on from this topic for now.
*   **Phuc Asking/Doing:** Listening, nodding.
*   **Exercises/Questions:** None visible.
*   **Tutor Correction:** None.

**00:30 - 01:00: Transition to Materials Topic**
*   **Screen State:** OneNote still open. Alex navigates the left sidebar, moving from "3 - Power" to "1b - Materials". The main pane briefly shows "1.4 Materials" spec content.
*   **Alex Teaching:** Explaining that they finished "Work Energy and Power" and are now moving to "Materials". He mentions changing the name of a section.
*   **Phuc Asking/Doing:** Asks "So we finished the Work Energy and Power, right?"
*   **Exercises/Questions:** None visible.
*   **Tutor Correction:** Alex confirms they are done with "Work Energy and Power".

**01:00 - 01:45: Hooke's Law and Springs - Retrieval Practice**
*   **Screen State:** OneNote showing "1b - Materials" section, with "1 - Hooke's Law and Springs" page open. The page has a highlighted "Aim: to know how to calculate this" and "Retrieval practice" questions. Alex is seen erasing previous handwritten notes on the page.
    *   Retrieval practice questions:
        1.  Did you study anything to do with stretching springs at GCSE?
        2.  State Hooke's Law
        3.  State the formula linking Force, extension and spring constant
        4.  Describe what "spring constant" is
        5.  Describe what happens at the "elastic limit"
        6.  State the rules for resistors in series and parallel
*   **Alex Teaching:** Explaining he's clearing the page of previous notes. He then starts asking Phuc the retrieval practice questions.
*   **Phuc Asking/Doing:** Listening, nodding.
*   **Exercises/Questions:** Retrieval practice questions 1-6 are visible.
*   **Tutor Correction:** None.

**01:45 - 02:05: Retrieval Practice - Question 1 (Stretching Springs at GCSE)**
*   **Screen State:** Same OneNote page. Alex has written "T" (for tension) and "to elastic limit" next to question 1.
*   **Alex Teaching:** Asks Phuc about prior knowledge of stretching springs from GCSE.
*   **Phuc Asking/Doing:** "So in the last time I have a lecture, this one was not a tutor, but wasn't covered really well." He then says he would prefer if they could "redo it".
*   **Exercises/Questions:** Question 1.
*   **Tutor Correction:** Alex acknowledges Phuc's request and agrees to cover it thoroughly.

**02:05 - 02:40: Retrieval Practice - Question 2 (Hooke's Law)**
*   **Screen State:** Same OneNote page. Alex has written "F = kx" and "shape" next to question 3.
*   **Alex Teaching:** Asks Phuc about Hooke's Law.
*   **Phuc Asking/Doing:** "Okay, so I think I remember there's something like proportional. So the displacement of the spring is proportional to a constant, and that constant is the Hooke constant, if I recall correctly."
*   **Exercises/Questions:** Question 2.
*   **Tutor Correction:** Alex confirms Phuc's understanding is "close enough" and "good".

**02:40 - 03:20: Retrieval Practice - Question 3 (Formula) & Question 4 (Spring Constant)**
*   **Screen State:** Same OneNote page. Alex writes "F = kx" next to question 3. Next to question 4, he writes "Force per unit extension".
*   **Alex Teaching:** Asks Phuc about the formula linking force, extension, and spring constant. Then asks to describe the spring constant.
*   **Phuc Asking/Doing:** For question 3, he says "So because it's proportional, so that's mean have it need to have a proportional constant. So I have to multiply by a proportional constant." For question 4, he says "So maybe like it's the physical property of a material. So it would determine like given the same force, then what is the amount of extension."
*   **Exercises/Questions:** Questions 3 and 4.
*   **Tutor Correction:** Alex confirms Phuc's formula is correct (F=kx) and clarifies the spring constant definition as "force needed per unit extension".

**03:20 - 04:00: Retrieval Practice - Question 5 (Elastic Limit)**
*   **Screen State:** Same OneNote page. Alex writes "< elastic" and "plastic" next to question 5.
*   **Alex Teaching:** Asks Phuc to describe what happens at the elastic limit.
*   **Phuc Asking/Doing:** "Okay, so I think before the point of elastic limit, it's like the extension is linear. After that point, it becomes non-linear, but I don't recall the exact one."
*   **Exercises/Questions:** Question 5.
*   **Tutor Correction:** Alex confirms Phuc's answer is "all correct" and that he remembers "more than you realize".

**04:00 - 04:50: Retrieval Practice - Question 6 (Resistors in Series and Parallel)**
*   **Screen State:** Same OneNote page. Alex draws two resistors in series (R1, R2) with total resistance RT = R1 + R2. He then draws two resistors in parallel with total resistance 1/RT = 1/R1 + 1/R2.
*   **Alex Teaching:** Asks Phuc about rules for resistors in series and parallel, acknowledging it's an electricity topic they haven't fully covered yet.
*   **Phuc Asking/Doing:** "No, I don't recall." Then, "Could you remind me?" After Alex draws the series circuit, Phuc says "So sum up." After Alex draws the parallel circuit, Phuc says "Maybe it's divide by half."
*   **Exercises/Questions:** Question 6.
*   **Tutor Correction:** Alex confirms for series (add them together) and clarifies for parallel (1/RT = 1/R1 + 1/R2), stating they will cover electricity in more detail later. He uses an analogy of walking up stairs for series (total stairs = sum of stairs) and having two paths for parallel (easier to go through).

**04:50 - 05:40: Transition to PhET Simulation**
*   **Alex Teaching:** Mentions finding a simulation for the practical.
*   **Phuc Asking/Doing:** Listening.
*   **Exercises/Questions:** None.
*   **Tutor Correction:** None.

**05:40 - 06:20: PhET Simulation - Hooke's Law Intro**
*   **Screen State:** PhET Interactive Simulations website, "Hooke's Law" simulation. The "Intro" tab is selected, showing a spring attached to a wall, with sliders for "Spring Constant" and "Applied Force". Checkboxes for "Applied Force", "Spring Force", "Displacement", "Equilibrium Position", and "Values" are visible.
*   **Alex Teaching:** Explains the simulation allows changing force, measuring extension, and changing spring constant. He demonstrates by adjusting the applied force and observing the spring's displacement.
*   **Phuc Asking/Doing:** Listening, observing.
*   **Exercises/Questions:** None.
*   **Tutor Correction:** None.

**06:20 - 07:00: Practical Setup and Safety**
*   **Screen State:** OneNote page with a diagram of a spring testing setup (Figure 1: Testing the extension of a spring). The diagram shows a spring hanging from a stand, with weights attached, and a meter rule for measurement. Below it is a table for "Single spring", "2 in series", and "2 in parallel" with columns for "Force" and "Extension".
*   **Alex Teaching:** Explains the experimental setup for Hooke's Law. He then asks about safety measures if this experiment were done in a lab.
*   **Phuc Asking/Doing:** Listening.
*   **Exercises/Questions:** Practical setup diagram and table.
*   **Tutor Correction:** None.

**07:00 - 07:30: Safety Precautions for Spring Experiment**
*   **Screen State:** Same OneNote page. Alex writes "glove" next to "Safety".
*   **Alex Teaching:** Asks Phuc what he would do first with a spring in his hands.
*   **Phuc Asking/Doing:** "Glove." (spells it out)
*   **Exercises/Questions:** Safety section.
*   **Tutor Correction:** Alex confirms "glove" is close, but clarifies the main safety concern: "wear safety glasses" because the spring might fly off and hit someone's eye. He also mentions another precaution: "masses might fall on my feet, so I need to be careful and not stand underneath it."

**07:30 - 08:00: Springs in Series and Parallel - Expected Outcomes**
*   **Screen State:** Same OneNote page, focusing on the table for "Single spring", "2 in series", and "2 in parallel". Alex starts filling in example values for "Single spring": Force (N) 20, 40, 60, 80, 100; Extension (mm) 40, 80, 120, 160, 200.
*   **Alex Teaching:** Asks Phuc to predict the extension for "2 in series" and "2 in parallel" setups, given the same forces.
*   **Phuc Asking/Doing:** For "2 in series", Phuc says "So it would be smaller." Alex clarifies, "So compare it to the single spring on its own." Phuc then says "So it would be double." Alex confirms "double extension". For "2 in parallel", Phuc says "So the extension should be smaller." Alex confirms "extension smaller".
*   **Exercises/Questions:** Table with example data for single spring.
*   **Tutor Correction:** Alex guides Phuc to compare the extensions relative to the single spring. He explains that for series, the extension doubles (each spring extends by the same amount as the single spring for the same force). For parallel, the extension halves (the force is shared between two springs, so each extends less). Alex fills in the expected values for series (80, 160, 240, 320, 400) and parallel (20, 40, 60, 80, 100). He then writes the spring constants: K for single, K/2 for series, and 2K for parallel.

**08:00 - 08:30: Hooke's Law Definition and Example Problem**
*   **Screen State:** OneNote page, scrolled down to "Teacher Notes". Alex writes the definition of Hooke's Law and an example problem.
    *   Hooke's Law: F = kx (Force $\propto$ extension up to elastic limit)
    *   Example: Length = 300mm, stretched length = 385mm with a 5.0N weight on.
    *   A. Calculate the spring constant.
*   **Alex Teaching:** Defines Hooke's Law and introduces an example problem to calculate the spring constant.
*   **Phuc Asking/Doing:** Listening.
*   **Exercises/Questions:** Hooke's Law definition and example problem A.
*   **Tutor Correction:** None.

**08:30 - 09:00: Solving Example Problem A (Spring Constant)**
*   **Screen State:** OneNote page, showing the solution for example problem A.
    *   F = 5.0N
    *   $\Delta$L = 385 - 300 = 85mm = 85 x 10^{-3} m
    *   k = F/$\Delta$L = 5.0 / (85 x 10^{-3}) = 58.8 N m^{-1} (Alex writes 59 N m^{-1})
*   **Alex Teaching:** Guides Phuc through the calculation of the spring constant.
*   **Phuc Asking/Doing:** Explains the steps: convert mm to m, calculate extension, then use F=kx to find k.
*   **Exercises/Questions:** Example problem A.
*   **Tutor Correction:** Alex confirms Phuc's steps and calculation.

**09:00 - 09:30: Example Problem B (Springs in Series)**
*   **Screen State:** OneNote page, showing example problem B.
    *   B. Draw a diagram and calculate the spring constant of 2 in series.
*   **Alex Teaching:** Asks Phuc to draw a diagram and calculate the spring constant for two springs in series.
*   **Phuc Asking/Doing:** Phuc draws two springs in series with a mass at the bottom. He then calculates the spring constant for two springs in series as k/2 = 59/2 = 29.5 N m^{-1}.
*   **Exercises/Questions:** Example problem B.
*   **Tutor Correction:** Alex confirms Phuc's diagram and calculation.

**09:30 - 10:00: Example Problem C (Springs in Parallel)**
*   **Screen State:** OneNote page, showing example problem C.
    *   C. Draw a diagram and calculate the spring constant of 2 in parallel.
*   **Alex Teaching:** Asks Phuc to draw a diagram and calculate the spring constant for two springs in parallel.
*   **Phuc Asking/Doing:** Phuc draws two springs in parallel with a mass at the bottom. He calculates the spring constant for two springs in parallel as 2k = 2 * 59 = 118 N m^{-1}.
*   **Exercises/Questions:** Example problem C.
*   **Tutor Correction:** Alex confirms Phuc's diagram and calculation.

**10:00 - 10:30: Stress, Strain, and Young's Modulus - Retrieval Practice**
*   **Screen State:** OneNote page, showing "2 - Stress, Strain and Young's Modulus" section. Retrieval practice questions are visible.
    *   Retrieval practice questions:
        1.  State Stoke's Law
        2.  State the formula for upthrust
        3.  State Hooke's Law
        4.  State the formula linking Force, extension and spring constant
        5.  Describe what each spring arrangement will do when the same force is applied
        6.  What do these stand for: G, M, K, L, m, p, $\pi$
*   **Alex Teaching:** Introduces the new topic and starts with retrieval practice. He asks Phuc to state Hooke's Law.
*   **Phuc Asking/Doing:** "So Hooke's Law is the amount of force that required to extend per unit area. So by by one meter."
*   **Exercises/Questions:** Question 3.
*   **Tutor Correction:** Alex corrects Phuc, stating it's not "per unit area" but "force is proportional to extension up until the elastic limit". He also clarifies that area is for stress, not Hooke's Law.

**10:30 - 11:00: Stress, Strain, and Young's Modulus - Definitions**
*   **Screen State:** OneNote page, scrolled down to "Teacher Notes". Definitions for "Tensile stress", "Tensile strain", and "Young's Modulus" are visible.
    *   Tensile stress is the "inverse" of pressure. (Alex corrects this to "similar to pressure")
    *   Tensile stress: Force / Cross sectional area ($\sigma$ = F/A)
    *   Tensile strain is the ratio of change in length. ($\varepsilon$ = $\Delta$x/x = change in length / original length)
    *   Young's Modulus is a more detailed version of a spring/force constant. It is used to compare different materials, rather than individual springs. (E = Stress / Strain = $\sigma$ / $\varepsilon$)
*   **Alex Teaching:** Explains the definitions of tensile stress, tensile strain, and Young's modulus. He clarifies that tensile stress is similar to pressure (force per unit area), not its inverse. He also explains the symbols and units.
*   **Phuc Asking/Doing:** Asks for clarification on how to calculate Young's modulus.
*   **Exercises/Questions:** Definitions.
*   **Tutor Correction:** Alex provides the formulas and explains the symbols and units.

**11:00 - 11:30: Example Problem (Crane and Steel Cable)**
*   **Screen State:** OneNote page, showing an example problem.
    *   A crane fitted with a steel cable of uniform diameter 2.3mm and length 28m is used to lift an iron girder of weight 3200N off the ground. Calculate the extension of the cable when it supports the girder at rest. Young modulus for steel = 2.1 x 10^{11} Pa.
*   **Alex Teaching:** Introduces the example problem and guides Phuc to identify the given values and the unknown.
*   **Phuc Asking/Doing:** Identifies given values: diameter, length, force, Young's modulus. Identifies unknown: extension ($\Delta$x). He also mentions needing to calculate the area of a circle.
*   **Exercises/Questions:** Example problem.
*   **Tutor Correction:** Alex confirms the identified values and the need to calculate the area.

**11:30 - 12:00: Solving the Crane Problem**
*   **Screen State:** OneNote page, showing the solution steps.
    *   A = $\pi r^2$ = $\pi$(2.3 x 10^{-3}/2)2 m^2 = 4.15 x 10^{-6} m^2
    *   x = 28m
    *   F = 3200N
    *   $\Delta$x = ?
    *   E = 2.1 x 10^{11} Pa
    *   E = Fx / (A$\Delta$x) => $\Delta$x = Fx / (AE)
    *   $\Delta$x = (3200 * 28) / (4.15 x 10^{-6} * 2.1 x 10^{11}) = 0.103 m
*   **Alex Teaching:** Guides Phuc through calculating the area, rearranging the Young's modulus formula to find $\Delta$x, and substituting the values.
*   **Phuc Asking/Doing:** Calculates the area, rearranges the formula, and substitutes the values.
*   **Exercises/Questions:** Example problem.
*   **Tutor Correction:** Alex confirms the steps and the final answer.

**12:00 - 12:30: Exam Style Questions - Q1 (Steel Rail)**
*   **Screen State:** OneNote page, showing "HW Young's Modulus exam style question" (Q1).
    *   Q1: If lengths of rail track are laid down in cold weather, they may deform as they expand when the weather becomes warmer. Therefore, when rails are laid in cold weather they are stretched and fixed into place while still stretched. This is called pre-straining.
    *   The following data is typical for a length of steel rail:
        *   Young modulus of steel = 2.0 x 10^{11} Pa
        *   Cross-sectional area of a length of rail = 7.5 x 10^{-3} m^2
        *   Amount of pre-strain = 3.0 x 10^{-4}
        *   2.5 x 10^{-5} for each Kelvin rise in temperature the rail is expected to experience.
    *   A steel rail is laid when the temperature is 8°C and the engineer decides to use a pre-strain of 3.0 x 10^{-4}.
    *   (a) Calculate the tensile force required to produce the pre-strain in the rail required by the engineer. (3 marks)
*   **Alex Teaching:** Introduces the exam-style question, highlighting the context and the term "pre-straining". He guides Phuc to identify the relevant formula and values.
*   **Phuc Asking/Doing:** Asks "What do they mean by amount of pre-strain?" Alex explains it's just the strain in this context. Phuc then identifies the formula F = E A $\varepsilon$.
*   **Exercises/Questions:** Exam-style question Q1(a).
*   **Tutor Correction:** Alex confirms the formula and guides Phuc to substitute the values.

**12:30 - 13:00: Solving Q1(a) and Q1(b)**
*   **Screen State:** OneNote page, showing the solution for Q1(a) and Q1(b).
    *   Q1(a) F = E A $\varepsilon$ = (2.0 x 10^{11}) * (7.5 x 10^{-3}) * (3.0 x 10^{-4}) = 45000 N = 45 kN
    *   Q1(b) Calculate the elastic strain energy stored in a rail of unstressed length 45m when pre-strained as in part (a). (2 marks)
*   **Alex Teaching:** Guides Phuc through the calculation for Q1(a) and then introduces Q1(b) about elastic strain energy.
*   **Phuc Asking/Doing:** Calculates F = 45 kN. For Q1(b), Phuc identifies the formula E = 1/2 Fx.
*   **Exercises/Questions:** Exam-style questions Q1(a) and Q1(b).
*   **Tutor Correction:** Alex confirms the formula for elastic strain energy and guides Phuc to use the calculated force and the given length.

**13:00 - 13:30: Solving Q1(b) and Q1(c)**
*   **Screen State:** OneNote page, showing the solution for Q1(b) and Q1(c).
    *   Q1(b) E = 1/2 Fx = 1/2 * (45 x 10^3) * (3.0 x 10^{-4} * 45) = 303.75 J (Alex writes 304 J)
    *   Q1(c) Calculate the temperature at which the steel rail becomes unstressed. (2 marks)
*   **Alex Teaching:** Guides Phuc through the calculation for Q1(b) and introduces Q1(c) about temperature.
*   **Phuc Asking/Doing:** Calculates the energy. For Q1(c), Phuc mentions that he doesn't have a formula for temperature related to strain.
*   **Exercises/Questions:** Exam-style questions Q1(b) and Q1(c).
*   **Tutor Correction:** Alex confirms the energy calculation. For Q1(c), he points out that the question provides a value for "each Kelvin rise in temperature the rail is expected to experience" (2.5 x 10^{-5}). This relates temperature change to strain.

**13:30 - 14:00: Solving Q1(c) and Q1(d)**
*   **Screen State:** OneNote page, showing the solution for Q1(c) and Q1(d).
    *   Q1(c) $\Delta$T = $\varepsilon$ / (2.5 x 10^{-5}) = (3.0 x 10^{-4}) / (2.5 x 10^{-5}) = 12 °C. So, temperature = 8°C + 12°C = 20°C.
    *   Q1(d) Explain why the engineer does not use the highest observed temperature at the location of the railway track to determine the amount of pre-strain to use. (2 marks)
*   **Alex Teaching:** Guides Phuc through the calculation for Q1(c) and introduces Q1(d) about the engineer's decision.
*   **Phuc Asking/Doing:** Calculates the temperature. For Q1(d), Phuc thinks about the question.
*   **Exercises/Questions:** Exam-style questions Q1(c) and Q1(d).
*   **Tutor Correction:** Alex confirms the temperature calculation. For Q1(d), he explains that using the highest temperature would mean the rails are always under tension, which could lead to snapping in cold weather. The engineer needs to find a balance.

**14:00 - 14:30: Searle's Apparatus and Further Questions**
*   **Screen State:** OneNote page, showing "Searle's Apparatus" diagram and "Core questions".
*   **Alex Teaching:** Briefly introduces Searle's Apparatus for measuring Young's Modulus. He then points to the "Core questions" section.
*   **Phuc Asking/Doing:** Listening.
*   **Exercises/Questions:** Searle's Apparatus diagram and Core questions.
*   **Tutor Correction:** None.

**14:30 - 15:00: Core Questions - Q1 (Copper Wire)**
*   **Screen State:** OneNote page, showing Core Question 1.
    *   Q1: A force of 160N extends a copper wire by 2.7 cm. Calculate the stiffness constant of the wire. (2 marks)
*   **Alex Teaching:** Asks Phuc to solve Core Question 1.
*   **Phuc Asking/Doing:** Identifies F=160N, $\Delta$x=2.7cm. Converts cm to m (0.027m). Uses F=kx => k=F/x = 160/0.027 = 5925.9 N m^{-1}.
*   **Exercises/Questions:** Core Question 1.
*   **Tutor Correction:** Alex confirms the answer.

**15:00 - 15:30: Core Questions - Q2 (Weight on Spring)**
*   **Screen State:** OneNote page, showing Core Question 2.
    *   Q2: A 12N weight is hung on a spring 5.0cm long with spring constant 8500 N m^{-1}. Calculate:
        *   a. the extension (1 mark)
        *   b. the new length of the spring. (1 mark)
*   **Alex Teaching:** Asks Phuc to solve Core Question 2.
*   **Phuc Asking/Doing:** Identifies F=12N, original length=5.0cm=0.05m, k=8500 N m^{-1}.
    *   a. $\Delta$x = F/k = 12/8500 = 0.00141 m = 0.141 cm.
    *   b. New length = original length + $\Delta$x = 0.05 + 0.00141 = 0.05141 m = 5.141 cm.
*   **Exercises/Questions:** Core Question 2.
*   **Tutor Correction:** Alex confirms the answers.

**15:30 - 16:00: Core Questions - Q3 (Horizontal Plank)**
*   **Screen State:** OneNote page, showing Core Question 3.
    *   Q3: A horizontal plank is supported at each end. A child of mass 55kg stands on the centre of the plank, which bends, so the centre moves down 4.0mm. Calculate the stiffness constant of the plank. (1 mark)
*   **Alex Teaching:** Asks Phuc to solve Core Question 3.
*   **Phuc Asking/Doing:** Identifies m=55kg, $\Delta$x=4.0mm=0.004m. Calculates F=mg = 55*9.81 = 539.55N. Calculates k=F/$\Delta$x = 539.55/0.004 = 134887.5 N m^{-1}.
*   **Exercises/Questions:** Core Question 3.
*   **Tutor Correction:** Alex confirms the answer.

**16:00 - 16:30: Core Questions - Q4 (Identical Springs)**
*   **Screen State:** OneNote page, showing Core Question 4.
    *   Q4: A student has two identical springs with spring constant 240 N m^{-1} and natural length 210 mm. The weight of the springs is negligible. Calculate the length of each of the springs when:
        *   a. they are joined vertically and stretched with a weight of 8.0N. (2 marks)
        *   b. they are joined in parallel and stretched with a weight of 8.0N. (2 marks)
*   **Alex Teaching:** Asks Phuc to solve Core Question 4.
*   **Phuc Asking/Doing:** Identifies k_single=240 N m^{-1}, original length=210mm=0.21m, F=8.0N.
    *   a. (Series) each spring carries the same $8.0\,\mathrm{N}$ force. The extension of each spring is $x=F/k=8.0/240=0.0333\,\mathrm{m}$. Therefore the length of each spring is $0.210+0.0333=0.243\,\mathrm{m}$. The total length of the two-spring chain is $2(0.243)=0.487\,\mathrm{m}$. If instead the question asks for effective stiffness of the pair, $k_{series}=120\,\mathrm{N\,m^{-1}}$ and the total extension is $0.0667\,\mathrm{m}$.
    *   b. (Parallel) the effective stiffness doubles: $k_{parallel}=480\,\mathrm{N\,m^{-1}}$. The extension is $x=8.0/480=0.0167\,\mathrm{m}$, so the spring length is $0.210+0.0167=0.227\,\mathrm{m}$.
*   **Exercises/Questions:** Core Question 4.
*   **Tutor Correction:** Alex confirms the answers.

**16:30 - 17:00: Further Questions - Q5 (Force-Length Data)**
*   **Screen State:** OneNote page, showing Further Question 5.
    *   Q5: Force is applied to a spring and this data is collected:
        *   Force / N: 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0
        *   Length / cm: 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.9, 4.3
        *   a. Plot a force-extension graph for the spring. (3 marks)
        *   b. Explain the shape of the graph. (3 marks)
        *   c. Calculate the spring constant. (2 marks)
*   **Alex Teaching:** Asks Phuc to solve Further Question 5.
*   **Phuc Asking/Doing:** Identifies the need to calculate extension from the given length data.
    *   Extension (cm): 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.3, 1.7
    *   c. k = $\Delta$F/$\Delta$x = (7.0-0.0) / (1.7-0.0) = 7.0/1.7 = 4.12 N cm^{-1}. (Needs to be N m^{-1}, so 412 N m^{-1}).
*   **Exercises/Questions:** Further Question 5.
*   **Tutor Correction:** Alex confirms the calculation of extension and guides Phuc to calculate the spring constant from the gradient of the force-extension graph. He reminds Phuc to convert units to N m^{-1}.

**17:00 - 17:30: Further Questions - Q6 (Tensile Stress in Bridge Cable)**
*   **Screen State:** OneNote page, showing Further Question 6.
    *   Q6: Calculate the tensile stress in a suspension bridge supporting cables of diameter of 50 mm, which pulls up on the roadway with a force of 4 kN.
*   **Alex Teaching:** Asks Phuc to solve Further Question 6.
*   **Phuc Asking/Doing:** Identifies diameter=50mm=0.05m, F=4kN=4000N. Calculates Area = $\pi$(0.05/2)2 = 1.96 x 10^{-3} m^2. Stress = F/A = 4000 / (1.96 x 10^{-3}) = 2.04 x 10^6 Pa = 2.04 MPa.
*   **Exercises/Questions:** Further Question 6.
*   **Tutor Correction:** Alex confirms the answer.

**17:30 - 18:00: Further Questions - Q7 (Large Crane)**
*   **Screen State:** OneNote page, showing Further Question 7.
    *   Q7: A large crane has a steel lifting cable of diameter 30 mm. The steel used has a Young modulus of 200 GPa. When the crane is used to lift 20 kN, the unstretched cable length is 25.0 m. Calculate the extension of the cable.
*   **Alex Teaching:** Asks Phuc to solve Further Question 7.
*   **Phuc Asking/Doing:** Identifies diameter=30mm=0.03m, E=200GPa=200x10^9 Pa, F=20kN=20000N, original length=25.0m. Calculates Area = $\pi(0.03/2)^2$ = 7.07 x 10^{-4} m^2. $\Delta$x = (F * original length) / (A * E) = (20000 * 25) / (7.07 x 10^{-4} * 200 x 10^9) = 3.53 x 10^{-3} m = 3.53 mm.
*   **Exercises/Questions:** Further Question 7.
*   **Tutor Correction:** Alex confirms the answer.

**18:00 - 18:30: Further Questions - Q8 (Rubber Band)**
*   **Screen State:** OneNote page, showing Further Question 8.
    *   Q8: A rubber band was 8.4 cm long before it was stretched. It is then stretched until its strain is 2.45. Calculate its new total length.
*   **Alex Teaching:** Asks Phuc to solve Further Question 8.
*   **Phuc Asking/Doing:** Identifies original length=8.4cm=0.084m, strain=2.45. $\Delta$x = strain * original length = 2.45 * 0.084 = 0.2058m. New length = original length + $\Delta$x = 0.084 + 0.2058 = 0.2898m = 29.0 cm.
*   **Exercises/Questions:** Further Question 8.
*   **Tutor Correction:** Alex confirms the answer.

**18:30 - 19:00: Further Questions - Q9 (Copper Wire)**
*   **Screen State:** OneNote page, showing Further Question 9.
    *   Q9: A copper wire is put under tension. It was 1.52 m long to begin with, and then stretches by 3.2 mm. Calculate its stress.
*   **Alex Teaching:** Asks Phuc to solve Further Question 9.
*   **Phuc Asking/Doing:** Identifies original length=1.52m, $\Delta$x=3.2mm=0.0032m. Calculates strain = $\Delta$x / original length = 0.0032 / 1.52 = 0.0021. (Stress cannot be calculated without force or Young's modulus).
*   **Exercises/Questions:** Further Question 9.
*   **Tutor Correction:** Alex points out that stress cannot be calculated with the given information. He asks Phuc to identify what's missing (force or Young's modulus).

**19:00 - 19:30: Further Questions - Q10 (Brass Pin)**
*   **Screen State:** OneNote page, showing Further Question 10.
    *   Q10: A brass pin has a cross-sectional area of 0.30 cm^2. Brass has a tensile strength of 190 MPa. Calculate the maximum tensile force it ought to be able to withstand without breaking.
*   **Alex Teaching:** Asks Phuc to solve Further Question 10.
*   **Phuc Asking/Doing:** Identifies A=0.30cm^2=0.30x10^{-4} m^2, tensile strength (stress)=190MPa=190x10^6 Pa. Force = Stress * Area = 190x10^6 * 0.30x10^{-4} = 5700 N = 5.7 kN.
*   **Exercises/Questions:** Further Question 10.
*   **Tutor Correction:** Alex confirms the answer.

**19:30 - 20:00: Further Questions - Q11 (Mild Steel)**
*   **Screen State:** OneNote page, showing Further Question 11.
    *   Q11: Mild steel has a breaking strength of 500 MPa. If you want to support a 200 kg piano using a single steel wire, what is the minimum diameter of wire you require?
*   **Alex Teaching:** Asks Phuc to solve Further Question 11.
*   **Phuc Asking/Doing:** Identifies stress=500MPa=500x10^6 Pa, m=200kg. Calculates F=mg = 200*9.81 = 1962N. Area = F/Stress = 1962 / (500x10^6) = 3.924 x 10^{-6} m^2. Area = $\pi r^2$ => r = sqrt(A/$\pi$) = sqrt(3.924x10^{-6}/$\pi$) = 0.001117m. Diameter = 2r = 0.00223m = 2.23 mm.
*   **Exercises/Questions:** Further Question 11.
*   **Tutor Correction:** Alex confirms the answer.

**20:00 - 20:30: Further Questions - Q12 (Bolt and Harness)**
*   **Screen State:** OneNote page, showing Further Question 12.
    *   Q12: A bolt is needed to attach an actor's harness to a wire across a stage. The bolt is 5.0 cm long with a 0.25 cm^2 cross-sectional area, and must extend by no more than 0.02 mm when supporting a 90.0 kg mass. Calculate the minimum value of Young's modulus of a material if it is to be suitable.
*   **Alex Teaching:** Asks Phuc to solve Further Question 12.
*   **Phuc Asking/Doing:** Identifies original length=5.0cm=0.05m, A=0.25cm^2=0.25x10^{-4} m^2, $\Delta$x=0.02mm=0.02x10^{-3} m, m=90.0kg. Calculates F=mg = 90*9.81 = 882.9N. Stress = F/A = 882.9 / (0.25x10^{-4}) = 3.53 x 10^7 Pa. Strain = $\Delta$x / original length = 0.02x10^{-3} / 0.05 = 4.0 x 10^{-4}. E = Stress / Strain = (3.53x10^7) / (4.0x10^{-4}) = 8.83 x 10^{10} Pa = 88.3 GPa.
*   **Exercises/Questions:** Further Question 12.
*   **Tutor Correction:** Alex confirms the answer.

---

## 2. Complete Prior-Knowledge Lecture

This section outlines the fundamental concepts necessary to understand the topics covered in the lesson.

### 2.1. Force
*   **Definition:** A push or a pull on an object. It is a vector quantity, meaning it has both magnitude and direction.
*   **Units:** The SI unit for force is the Newton (N).
*   **Relevance:** Force is the primary cause of deformation in materials and is central to Hooke's Law, stress, and strain.

### 2.2. Extension/Displacement
*   **Definition:** The change in length of a material from its original length when a force is applied. It can be an increase (extension) or decrease (compression).
*   **Units:** Typically measured in meters (m) in SI units, but often given in millimeters (mm) or centimeters (cm) in problems. Conversion is crucial (1m = 1000mm, 1m = 100cm).
*   **Relevance:** Directly proportional to force in Hooke's Law, and a key component in calculating strain and elastic strain energy.

### 2.3. Proportionality
*   **Definition:** A relationship between two quantities where if one quantity changes, the other quantity changes by a constant factor.
    *   **Direct Proportionality:** If y is directly proportional to x, then y = kx, where k is the constant of proportionality.
*   **Relevance:** Hooke's Law states that force is directly proportional to extension within the elastic limit. Understanding this relationship is fundamental.

### 2.4. Gradients
*   **Definition:** The slope of a line on a graph, representing the rate of change of the y-axis quantity with respect to the x-axis quantity.
*   **Relevance:** On a force-extension graph, the gradient ($\Delta$F/$\Delta$x) represents the spring constant (k).

### 2.5. Area Under Graph
*   **Definition:** The area enclosed by a curve and the x-axis on a graph.
*   **Relevance:** On a force-extension graph, the area under the curve represents the work done on the spring or the elastic strain energy stored in the spring. For a linear force-extension relationship (obeying Hooke's Law), this area is a triangle (1/2 * base * height = 1/2 * x * F).

### 2.6. Units and Prefixes
*   **SI Units:** The International System of Units provides a standard set of units for physical quantities (e.g., meter for length, Newton for force, Pascal for pressure/stress).
*   **Prefixes:** Used to denote multiples or submultiples of SI units (e.g., milli (m) = 10^{-3}, kilo (k) = $10^3$, Giga (G) = $10^9$, Mega (M) = 10^6).
*   **Relevance:** Consistent use of SI units is vital for accurate calculations. Incorrect unit conversions are a common source of error in physics problems.

### 2.7. Stress (and distinction from Pressure)
*   **Definition:** Stress ($\sigma$) is the force applied per unit cross-sectional area. It is a measure of the internal forces acting within a deformable body.
    *   **Formula:** $\sigma$ = F/A
    *   **Units:** Pascal (Pa) or N/m^2. 1 MPa = 10^6 Pa, 1 GPa = 10^9 Pa.
    *   **Tensile Stress:** Occurs when forces pull the material apart.
    *   **Compressive Stress:** Occurs when forces push the material together.
*   **Distinction from Pressure:** While both are force per unit area, pressure is typically associated with fluids and acts perpendicularly to a surface, while stress can be internal to a solid and can have both normal and shear components. In the context of materials, stress refers to the internal resistance of the material to deformation.
*   **Relevance:** Stress is a key concept in understanding how materials respond to external forces and is a component of Young's Modulus.

### 2.8. Strain
*   **Definition:** Strain ($\varepsilon$) is the deformation of a material in response to stress. It is defined as the ratio of the change in length ($\Delta$x) to the original length (x).
    *   **Formula:** $\varepsilon$ = $\Delta$x/x
    *   **Units:** Strain is a dimensionless quantity as it is a ratio of two lengths.
*   **Relevance:** Strain quantifies the relative deformation of a material and is a component of Young's Modulus.

### 2.9. Rearranging Formulae
*   **Definition:** The algebraic manipulation of equations to isolate a specific variable.
*   **Relevance:** Physics problems often require rearranging formulas like F=kx or E=$\sigma$/$\varepsilon$ to solve for an unknown quantity.

### 2.10. Cross-Sectional Area from Diameter
*   **Formula:** For a circular cross-section, the area (A) can be calculated using the radius (r) or diameter (d):
    *   A = $\pi r^2$
    *   Since r = d/2, $A=\pi(d/2)^2=\pi d^2/4$
*   **Relevance:** Many problems involving wires or cables provide the diameter, requiring this calculation to find the cross-sectional area for stress calculations.

### 2.11. Resistors in Series and Parallel (Analogy for Springs)
*   **Series:** When resistors are connected in series, the total resistance is the sum of individual resistances: R_total = R1 + R2 + ...
*   **Parallel:** When resistors are connected in parallel, the reciprocal of the total resistance is the sum of the reciprocals of individual resistances: 1/R_total = 1/R1 + 1/R2 + ...
*   **Relevance:** This electrical analogy is used to understand how the effective spring constant changes when springs are connected in series or parallel.
    *   **Springs in Series:** The effective spring constant decreases (1/k_effective = 1/k1 + 1/k2 + ...). This is analogous to resistors in parallel.
    *   **Springs in Parallel:** The effective spring constant increases (k_effective = k1 + k2 + ...). This is analogous to resistors in series.

---

## 3. Complete Topic Lecture Based on the Video

This lecture covers the core concepts of Hooke's Law, stress, strain, and Young's Modulus, integrating the explanations and examples from the tutoring session.

### 3.1. Hooke's Law and Elasticity

**Hooke's Law** describes the elastic behavior of materials.
*   **Definition:** For many materials, the force (F) required to produce an extension (x) is directly proportional to the extension itself, provided the elastic limit is not exceeded.
*   **Formula:** $F = kx$
    *   **F:** Applied force (N)
    *   **k:** Spring constant or stiffness constant (N m^{-1})
    *   **x:** Extension or displacement (m)
*   **Proportionality:** The relationship $F \propto x$ means that if you double the force, you double the extension.
*   **Spring Constant (k):**
    *   **Definition:** The spring constant (k) is a measure of the stiffness of a spring or material. It represents the force required to produce a unit extension.
    *   **Units:** Newtons per meter (N m^{-1}).
    *   **Interpretation:** A higher 'k' value means the spring is stiffer (requires more force for the same extension). A lower 'k' value means the spring is less stiff (extends more easily).
*   **Elastic Limit:**
    *   **Definition:** The elastic limit is the maximum stress or force a material can withstand and still return to its original shape once the stress or force is removed.
    *   **Behavior:**
        *   **Below Elastic Limit:** The material exhibits elastic deformation. It will return to its original shape. The force-extension graph is typically a straight line, obeying Hooke's Law.
        *   **Beyond Elastic Limit:** The material undergoes plastic deformation. It will not return to its original shape and will be permanently deformed. The force-extension graph becomes non-linear. If the force continues to increase, the material will eventually fracture.

### 3.2. Springs in Series and Parallel

The behavior of multiple springs connected together can be analyzed similarly to resistors in electrical circuits.

#### 3.2.1. Springs in Series
*   **Arrangement:** Springs are connected end-to-end, so the force applied to the combination is transmitted through each spring sequentially.
*   **Force:** The force (F) is the same through each spring.
*   **Extension:** The total extension ($x_{total}$) is the sum of the extensions of individual springs ($x_1 + x_2 + ...$).
*   **Effective Spring Constant ($k_{effective}$):**
    *   Since $F = k_{effective} x_{total}$ and $x_{total} = x_1 + x_2$, we have $F/k_{effective} = F/k_1 + F/k_2$.
    *   Therefore, $1/k_{effective} = 1/k_1 + 1/k_2 + ...$
    *   **Analogy:** This is analogous to resistors connected in parallel.
    *   **Outcome:** Connecting springs in series makes the overall system less stiff (easier to extend), resulting in a smaller effective spring constant.

#### 3.2.2. Springs in Parallel
*   **Arrangement:** Springs are connected side-by-side, so the applied force is shared among them.
*   **Force:** The total force (F) is the sum of the forces exerted by individual springs ($F_1 + F_2 + ...$).
*   **Extension:** The extension (x) is the same for each spring.
*   **Effective Spring Constant ($k_{effective}$):**
    *   Since $F = k_{effective} x$ and $F = F_1 + F_2$, we have $k_{effective} x = k_1 x + k_2 x$.
    *   Therefore, $k_{effective} = k_1 + k_2 + ...$
    *   **Analogy:** This is analogous to resistors connected in series.
    *   **Outcome:** Connecting springs in parallel makes the overall system stiffer (harder to extend), resulting in a larger effective spring constant.

### 3.3. Elastic Strain Energy

*   **Definition:** When a force is applied to stretch or compress a spring, work is done on the spring, and this work is stored as potential energy within the spring. This stored energy is called elastic strain energy.
*   **Formula:** For a spring obeying Hooke's Law (linear force-extension graph):
    *   $E = \frac{1}{2} Fx$ (Area under the force-extension graph, which is a triangle)
    *   Substituting $F=kx$, we can also write: $E = \frac{1}{2} kx^2$
*   **Units:** Joules (J).
*   **Thought Process:** To calculate elastic strain energy, first ensure you have the force and the extension (in SI units). If you have the spring constant and extension, use the second formula. If you have a force-extension graph, calculate the area under the graph.

### 3.4. Stress, Strain, and Young's Modulus

These concepts provide a more detailed way to describe the elastic properties of materials, independent of their specific dimensions.

#### 3.4.1. Stress ($\sigma$)
*   **Definition:** Stress is the internal force per unit cross-sectional area within a material. It quantifies the intensity of the internal forces that particles of a continuous material exert on each other.
*   **Formula:** $\sigma = \frac{F}{A}$
    *   **F:** Applied force (N)
    *   **A:** Cross-sectional area (m^2)
*   **Units:** Pascals (Pa) or N/m^2. Common multiples are MPa (10^6 Pa) and GPa (10^9 Pa).
*   **Types:**
    *   **Tensile Stress:** Occurs when the material is being stretched or pulled apart.
    *   **Compressive Stress:** Occurs when the material is being compressed or pushed together.
*   **Thought Process:** To calculate stress, you need the force applied and the cross-sectional area of the material. Remember to convert units to SI (e.g., cm^2 to m^2).

#### 3.4.2. Strain ($\varepsilon$)
*   **Definition:** Strain is a measure of the deformation of a material, defined as the ratio of the change in length to the original length. It is a dimensionless quantity.
*   **Formula:** $\epsilon = \frac{\Delta x}{x}$
    *   **$\Delta$x:** Change in length or extension (m)
    *   **x:** Original length (m)
*   **Units:** Dimensionless (or sometimes expressed as m/m).
*   **Thought Process:** To calculate strain, ensure both the change in length and the original length are in the same units (preferably meters).

#### 3.4.3. Young's Modulus (E)
*   **Definition:** Young's Modulus is a measure of the stiffness or elastic modulus of a material. It describes the material's resistance to elastic deformation under tensile or compressive stress. Unlike the spring constant (k), Young's Modulus is a property of the material itself, independent of its dimensions.
*   **Formula:** $E = \frac{\text{Stress}}{\text{Strain}} = \frac{\sigma}{\epsilon}$
    *   Substituting the formulas for stress and strain: $E = \frac{F/A}{\Delta x/x} = \frac{Fx}{A\Delta x}$
    *   **F:** Applied force (N)
    *   **x:** Original length (m)
    *   **A:** Cross-sectional area (m^2)
    *   **$\Delta$x:** Change in length or extension (m)
*   **Units:** Pascals (Pa) or N/m^2. Since strain is dimensionless, Young's Modulus has the same units as stress.
*   **Thought Process:**
    1.  Identify all given values (force, original length, cross-sectional area, extension).
    2.  Ensure all values are in SI units (meters, Newtons, square meters).
    3.  Calculate stress (F/A).
    4.  Calculate strain ($\Delta$x/x).
    5.  Calculate Young's Modulus (Stress/Strain).
    6.  Alternatively, use the combined formula $E = \frac{Fx}{A\Delta x}$ directly.
*   **Rearranging for Extension:** Often, you'll need to find the extension ($\Delta$x) given E, F, x, and A.
    *   $\Delta x = \frac{Fx}{AE}$

### 3.5. Young's Modulus Practical (Searle's Apparatus)

**Aim:** To determine the Young's Modulus of a material (e.g., a wire).

**Apparatus:**
*   Searle's apparatus (consisting of two wires, one control and one test, hanging from a rigid support).
*   Micrometer screw gauge (for measuring wire diameter).
*   Meter rule (for measuring original length).
*   Spirit level (to ensure horizontal alignment).
*   Slotted masses/weights.

**Method:**
1.  **Measure Diameter:** Use a micrometer screw gauge to measure the diameter of the test wire at several points along its length and in different orientations. Calculate the average diameter.
2.  **Calculate Cross-sectional Area:** Use the average diameter to calculate the cross-sectional area (A = $\pi$d2/4).
3.  **Measure Original Length:** Measure the original length (x) of the test wire between the clamps.
4.  **Set up Apparatus:**
    *   Hang the control wire and the test wire from a rigid support.
    *   Attach a vernier scale to the test wire and a main scale to the control wire.
    *   Attach a spirit level to the vernier scale to ensure it remains horizontal.
    *   Apply a small initial tension (e.g., a small mass) to both wires to straighten them and remove any kinks. This also sets the zero reading.
5.  **Apply Load:** Gradually add known masses (weights) to the hanger on the test wire.
6.  **Measure Extension:** For each added mass, adjust the spirit level to ensure the vernier scale is horizontal. Read the extension ($\Delta$x) from the vernier scale.
7.  **Repeat and Record:** Take multiple readings for increasing loads.
8.  **Remove Load:** Gradually remove the masses and check if the wire returns to its original length (to confirm elastic behavior).
9.  **Plot Graph:** Plot a graph of force (F) on the y-axis against extension ($\Delta$x) on the x-axis.
10. **Calculate Gradient:** The gradient of the linear portion of the graph is the spring constant (k) for the wire.
11. **Calculate Young's Modulus:** Use the formula $E = \frac{Fx}{A\Delta x}$ or $E = \frac{k x}{A}$ (where k is the gradient).

**Safety Precautions:**
*   **Safety Glasses:** Always wear safety glasses to protect eyes from snapping wires or falling weights.
*   **Sand Tray:** Place a sand tray beneath the weights to cushion any falling masses and prevent injury or damage.
*   **Avoid Overloading:** Do not exceed the elastic limit of the wire to prevent it from snapping.
*   **Secure Clamps:** Ensure all clamps are securely tightened to prevent the apparatus from collapsing.
*   **Clear Area:** Keep the area around the apparatus clear to avoid tripping hazards.

**Uncertainty Improvements:**
*   **Micrometer:** Use a micrometer screw gauge for diameter (more precise than ruler). Take multiple readings and average.
*   **Vernier Scale:** Use a vernier scale for extension readings (more precise than ruler).
*   **Repeat Readings:** Repeat the experiment multiple times and average the results to reduce random errors.
*   **Control Wire:** The control wire compensates for any yielding of the support or temperature changes, ensuring only the extension of the test wire is measured.
*   **Plotting Graph:** Plotting a graph and finding the gradient is more accurate than using a single set of readings.

---

## 4. Exercise-by-Exercise Reconstruction

This section reconstructs the exercises and problems discussed or visible in the video, providing detailed solutions and mark-scheme style notes.

### 4.1. Hooke's Law and Springs Example Problems

**Source:** OneNote, "1 - Hooke's Law and Springs" page (08:00)

**Example Problem A: Calculate the spring constant.**
*   **Prompt:** Length = 300mm, stretched length = 385mm with a 5.0N weight on. Calculate the spring constant. (Alex writes 5.0N, 385-300=85mm, k=?)
*   **Prerequisite Idea:** Hooke's Law (F=kx), definition of extension, unit conversion (mm to m).
*   **Step-by-step Solution:**
    1.  **Identify Force (F):** F = 5.0 N
    2.  **Calculate Extension ($\Delta$x):** $\Delta$x = Stretched length - Original length = 385 mm - 300 mm = 85 mm
    3.  **Convert Extension to SI Units:** $\Delta$x = 85 mm = 85 $\times$ 10^{-3} m
    4.  **Rearrange Hooke's Law to find k:** $k = F / \Delta x$
    5.  **Substitute values and calculate:** $k = 5.0 \, \text{N} / (85 \times 10^{-3} \, \text{m}) = 58.823... \, \text{N/m}$
*   **Final Answer:** $k = 59 \, \text{N/m}$ (to 2 significant figures, as per input force)
*   **Mark-scheme Style Notes:**
    *   1 mark for correctly calculating extension (85 mm or 0.085 m).
    *   1 mark for correct formula ($k=F/x$).
    *   1 mark for correct substitution and final answer with units.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc correctly identifies the steps and performs the calculation.
*   **Alex's Correction/Explanation:** Confirms Phuc's steps and answer.

**Example Problem B: Draw a diagram and calculate the spring constant of 2 in series.**
*   **Prompt:** Draw a diagram and calculate the spring constant of 2 in series. (Given k_single = 59 N m^{-1} from part A).
*   **Prerequisite Idea:** Springs in series rule ($1/k_{effective} = 1/k_1 + 1/k_2$), diagram representation.
*   **Step-by-step Solution:**
    1.  **Draw Diagram:** Two springs connected end-to-end, with a mass hanging from the bottom spring.
    2.  **Identify Individual Spring Constants:** $k_1 = k_2 = 59 \, \text{N/m}$
    3.  **Apply Series Formula:** $1/k_{effective} = 1/k_1 + 1/k_2 = 1/59 + 1/59 = 2/59$
    4.  **Calculate Effective Spring Constant:** $k_{effective} = 59/2 = 29.5 \, \text{N/m}$
*   **Final Answer:** $k_{effective} = 29.5 \, \text{N/m}$
*   **Mark-scheme Style Notes:**
    *   1 mark for correct diagram.
    *   1 mark for correct formula for springs in series.
    *   1 mark for correct substitution and final answer with units.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc correctly draws the diagram and applies the formula, getting 29.5 N m^{-1}.
*   **Alex's Correction/Explanation:** Confirms Phuc's diagram and calculation.

**Example Problem C: Draw a diagram and calculate the spring constant of 2 in parallel.**
*   **Prompt:** Draw a diagram and calculate the spring constant of 2 in parallel. (Given k_single = 59 N m^{-1} from part A).
*   **Prerequisite Idea:** Springs in parallel rule ($k_{effective} = k_1 + k_2$), diagram representation.
*   **Step-by-step Solution:**
    1.  **Draw Diagram:** Two springs connected side-by-side, with a single mass hanging from a bar connecting the bottom ends of both springs.
    2.  **Identify Individual Spring Constants:** $k_1 = k_2 = 59 \, \text{N/m}$
    3.  **Apply Parallel Formula:** $k_{effective} = k_1 + k_2 = 59 + 59 = 118 \, \text{N/m}$
*   **Final Answer:** $k_{effective} = 118 \, \text{N/m}$
*   **Mark-scheme Style Notes:**
    *   1 mark for correct diagram.
    *   1 mark for correct formula for springs in parallel.
    *   1 mark for correct substitution and final answer with units.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc correctly draws the diagram and applies the formula, getting 118 N m^{-1}.
*   **Alex's Correction/Explanation:** Confirms Phuc's diagram and calculation.

### 4.2. Exam Style Questions (Young's Modulus)

**Source:** OneNote, "Exam Style Zone" (12:00)

**Question Q1:**
*   **Prompt:** If lengths of rail track are laid down in cold weather, they may deform as they expand when the weather becomes warmer. Therefore, when rails are laid in cold weather they are stretched and fixed into place while still stretched. This is called pre-straining.
    *   The following data is typical for a length of steel rail:
        *   Young modulus of steel = 2.0 x 10^{11} Pa
        *   Cross-sectional area of a length of rail = 7.5 x 10^{-3} m^2
        *   Amount of pre-strain = 3.0 x 10^{-4}
        *   2.5 x 10^{-5} for each Kelvin rise in temperature the rail is expected to experience.
    *   A steel rail is laid when the temperature is 8°C and the engineer decides to use a pre-strain of 3.0 x 10^{-4}.
*   **Prerequisite Idea:** Young's Modulus (E = Stress/Strain), Stress ($\sigma$ = F/A), Strain ($\varepsilon$ = $\Delta$x/x), rearranging formulae, unit conversion, understanding "pre-strain" and thermal expansion.

**Q1(a): Calculate the tensile force required to produce the pre-strain in the rail required by the engineer. (3 marks)**
*   **Prompt:** Calculate the tensile force required to produce the pre-strain in the rail required by the engineer.
*   **Step-by-step Solution:**
    1.  **Identify Given Values:**
        *   Young modulus (E) = 2.0 x 10^{11} Pa
        *   Cross-sectional area (A) = 7.5 x 10^{-3} m^2
        *   Pre-strain ($\varepsilon$) = 3.0 x 10^{-4}
    2.  **Recall Young's Modulus Formula:** $E = \text{Stress} / \text{Strain} = \sigma / \epsilon$
    3.  **Recall Stress Formula:** $\sigma = F / A$
    4.  **Combine and Rearrange for Force (F):** $E = (F/A) / \epsilon \Rightarrow F = E A \epsilon$
    5.  **Substitute Values and Calculate:** $F = (2.0 \times 10^{11} \, \text{Pa}) \times (7.5 \times 10^{-3} \, \text{m}^2) \times (3.0 \times 10^{-4})$
        $F = 45000 \, \text{N}$
*   **Final Answer:** $F = 45 \, \text{kN}$
*   **Mark-scheme Style Notes:**
    *   1 mark for correct formula ($F = E A \epsilon$ or equivalent rearrangement).
    *   1 mark for correct substitution of values.
    *   1 mark for correct final answer with units (45 kN or 45000 N).
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc correctly identifies the formula and substitutes the values to get the correct answer.
*   **Alex's Correction/Explanation:** Confirms Phuc's steps and answer.

**Q1(b): Calculate the elastic strain energy stored in a rail of unstressed length 45m when pre-strained as in part (a). (2 marks)**
*   **Prompt:** Calculate the elastic strain energy stored in a rail of unstressed length 45m when pre-strained as in part (a).
*   **Step-by-step Solution:**
    1.  **Identify Given/Calculated Values:**
        *   Force (F) = 45000 N (from Q1a)
        *   Original length (x) = 45 m
        *   Strain ($\varepsilon$) = 3.0 x 10^{-4}
    2.  **Calculate Extension ($\Delta$x):** $\epsilon = \Delta x / x \Rightarrow \Delta x = \epsilon x$
        $\Delta x = (3.0 \times 10^{-4}) \times (45 \, \text{m}) = 0.0135 \, \text{m}$
    3.  **Recall Elastic Strain Energy Formula:** $E = \frac{1}{2} F \Delta x$
    4.  **Substitute Values and Calculate:** $E = \frac{1}{2} \times (45000 \, \text{N}) \times (0.0135 \, \text{m})$
        $E = 303.75 \, \text{J}$
*   **Final Answer:** $E = 304 \, \text{J}$ (to 3 significant figures)
*   **Mark-scheme Style Notes:**
    *   1 mark for correctly calculating extension ($\Delta$x).
    *   1 mark for correct formula ($E = \frac{1}{2} F \Delta x$) and final answer with units.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc correctly identifies the formula and calculates the energy.
*   **Alex's Correction/Explanation:** Confirms Phuc's steps and answer.

**Q1(c): Calculate the temperature at which the steel rail becomes unstressed. (2 marks)**
*   **Prompt:** Calculate the temperature at which the steel rail becomes unstressed.
*   **Step-by-step Solution:**
    1.  **Identify Given Values:**
        *   Pre-strain ($\varepsilon$) = 3.0 x 10^{-4}
        *   Strain per Kelvin rise = 2.5 x 10^{-5}
        *   Initial temperature = 8°C
    2.  **Calculate Temperature Change ($\Delta$T):** The rail becomes unstressed when the thermal expansion matches the pre-strain.
        $\Delta T = \text{Pre-strain} / (\text{Strain per Kelvin rise})$
        $\Delta T = (3.0 \times 10^{-4}) / (2.5 \times 10^{-5} \, \text{K}^{-1}) = 12 \, \text{K}$ (or 12 °C)
    3.  **Calculate Final Temperature:** Final Temperature = Initial Temperature + $\Delta$T
        Final Temperature = 8°C + 12°C = 20°C
*   **Final Answer:** Temperature = 20°C
*   **Mark-scheme Style Notes:**
    *   1 mark for correctly calculating the temperature change ($\Delta$T).
    *   1 mark for correctly calculating the final temperature.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc initially states he doesn't have a formula for temperature, but then correctly uses the given strain per Kelvin to find the temperature change and final temperature.
*   **Alex's Correction/Explanation:** Guides Phuc to use the provided thermal expansion data.

**Q1(d): Explain why the engineer does not use the highest observed temperature at the location of the railway track to determine the amount of pre-strain to use. (2 marks)**
*   **Prompt:** Explain why the engineer does not use the highest observed temperature at the location of the railway track to determine the amount of pre-strain to use.
*   **Step-by-step Solution:**
    1.  **Consider the effect of high temperature:** If the rails are laid at the highest observed temperature, they would be unstressed at that temperature.
    2.  **Consider the effect of low temperature:** When the temperature drops significantly (e.g., in cold weather), the rails would contract. Since they are fixed, this contraction would induce significant tensile stress.
    3.  **Consequence:** This high tensile stress could cause the rails to snap or fracture, leading to dangerous situations.
    4.  **Engineer's Goal:** The engineer aims to prevent both buckling (due to compression at high temperatures) and snapping (due to tension at low temperatures) by choosing an appropriate pre-strain that allows for thermal expansion and contraction within the material's elastic limits.
*   **Final Answer (Model Answer):** The engineer does not use the highest observed temperature because if the rails were unstressed at that temperature, they would experience significant tensile stress when the temperature drops to its lowest point. This high tensile stress could cause the rails to snap or fracture, compromising safety and structural integrity.
*   **Mark-scheme Style Notes:**
    *   1 mark for identifying that using the highest temperature would lead to high tensile stress in cold weather.
    *   1 mark for explaining that this high tensile stress could cause the rails to snap/fracture.
*   **Phuc's Attempt/Mistake/Hesitation:** Phuc thinks about the question.
*   **Alex's Correction/Explanation:** Provides the explanation, emphasizing the risk of snapping in cold weather if pre-straining is based on the highest temperature.

---

## 5. Diagram and Visual Inventory

This section details the visual aids used in the lesson.

1.  **OneNote Sidebar (00:00 - 01:00):**
    *   **What it shows:** The hierarchical structure of the "Phuc-Physics" OneNote notebook, with sections like "1 - Mechanics", "2 - Work Energy and...", "1b - Materials", "2a - Waves", "2b - Electricity", and "New Section 1-4".
    *   **Labels/Values:** Section titles.
    *   **Intended Teaching Purpose:** To show the organization of the course material and navigate between topics.
    *   **How to Redraw:** A simple tree-like structure or nested list representing the notebook sections.

2.  **OneNote "Power Exam Qs.docx" (00:00 - 00:30):**
    *   **What it shows:** A preview of a Microsoft Word document titled "Power Exam Qs.docx" and a PDF version.
    *   **Labels/Values:** File names, date (07 May 2024 12:20).
    *   **Intended Teaching Purpose:** To introduce the topic they were about to cover before deciding to switch.
    *   **How to Redraw:** A simple document icon with the title.

3.  **OneNote "1 - Hooke's Law and Springs" Retrieval Practice (01:00 - 08:00):**
    *   **What it shows:** A list of 6 retrieval practice questions. Alex's handwritten notes are initially present, then erased, then new notes are added as Phuc answers.
    *   **Labels/Values:**
        1.  Did you study anything to do with stretching springs at GCSE? (Alex writes "T" and "to elastic limit")
        2.  State Hooke's Law
        3.  State the formula linking Force, extension and spring constant (Alex writes "F = kx" and "shape")
        4.  Describe what "spring constant" is (Alex writes "Force per unit extension")
        5.  Describe what happens at the "elastic limit" (Alex writes "< elastic" and "plastic")
        6.  State the rules for resistors in series and parallel (Alex draws series: R1-R2, RT=R1+R2; parallel: R1||R2, 1/RT=1/R1+1/R2)
    *   **Intended Teaching Purpose:** To activate prior knowledge, identify gaps, and introduce key terms for the lesson.
    *   **How to Redraw:** List the questions and include the handwritten notes as annotations.

4.  **PhET Hooke's Law Simulation (05:40 - 06:20):**
    *   **What it shows:** An interactive simulation of Hooke's Law. A blue spring is attached to a fixed wall on the left and a movable red block on the right. Sliders control "Spring Constant" (100-1000 N m^{-1}) and "Applied Force" (-100 to 100 N). Checkboxes allow displaying "Applied Force", "Spring Force", "Displacement", "Equilibrium Position", and "Values".
    *   **Labels/Values:** "Spring Constant 1: 200 N/m", "Applied Force: 0.0 N". When force is applied, arrows for applied force and spring force appear, and displacement is shown (e.g., 0.036 m for 10 N).
    *   **Intended Teaching Purpose:** To visually demonstrate Hooke's Law, the relationship between force, extension, and spring constant, and the concept of equilibrium.
    *   **How to Redraw:** A diagram of a spring with a block, fixed at one end. Show sliders for spring constant and force. Indicate displacement and force vectors.

5.  **Figure 1: Testing the extension of a spring (06:20 - 08:00):**
    *   **What it shows:** A diagram of an experimental setup to test the extension of a spring. A spring hangs from a retort stand. Weights are attached to the bottom of the spring. A meter rule is positioned vertically next to the spring to measure its length/extension.
    *   **Labels/Values:** "Spring", "Weights", "Meter rule", "Retort stand".
    *   **Intended Teaching Purpose:** To illustrate the practical setup for Hooke's Law experiments and discuss safety precautions.
    *   **How to Redraw:** A clear line drawing of the apparatus, including labels.

6.  **OneNote Table for Spring Experiments (07:30 - 08:00):**
    *   **What it shows:** A table with columns for "Force / N" and "Extension / mm" for three setups: "Single spring", "2 in series", and "2 in parallel".
    *   **Labels/Values:**
        *   Single spring: Force (20, 40, 60, 80, 100), Extension (40, 80, 120, 160, 200)
        *   2 in series: Force (20, 40, 60, 80, 100), Extension (80, 160, 240, 320, 400)
        *   2 in parallel: Force (20, 40, 60, 80, 100), Extension (20, 40, 60, 80, 100)
        *   Below the table: Spring constant: K (for single), K/2 (for series), 2K (for parallel).
    *   **Intended Teaching Purpose:** To compare the extensions and effective spring constants for different spring arrangements.

7.  **OneNote Teacher Notes - Hooke's Law (08:00 - 08:30):**
    *   **What it shows:** Text defining Hooke's Law.
    *   **Labels/Values:** "Hooke's Law: F = kx", "Force x extension up to elastic limit".
    *   **Intended Teaching Purpose:** To provide a concise, formal definition of Hooke's Law.
    *   **How to Redraw:** Write out the definition and formula.

8.  **OneNote Teacher Notes - Stress, Strain, Young's Modulus (10:30 - 11:00):**
    *   **What it shows:** Definitions and formulas for tensile stress, tensile strain, and Young's Modulus.
    *   **Labels/Values:**
        *   "Tensile stress is the 'inverse' of pressure." (Alex corrects to "similar to pressure")
        *   "Stress $\sigma = \text{Force} / \text{Cross sectional area} = F/A$" (Units: N/m^2 or Pa)
        *   "Tensile strain is the ratio of change in length." ($\epsilon = \Delta x / x = \text{change in length} / \text{original length}$)
        *   "Young's Modulus is a more detailed version of a spring/force constant. It is used to compare different materials, rather than individual springs." ($E = \text{Stress} / \text{Strain} = \sigma / \epsilon$)
    *   **Intended Teaching Purpose:** To introduce and define these key material properties.
    *   **How to Redraw:** List the definitions and formulas clearly.

9.  **Searle's Apparatus Diagram (14:00 - 14:30):**
    *   **What it shows:** A detailed diagram of Searle's apparatus. Two wires (control and test) hang from a common support. Weights are attached to the test wire. A micrometer is attached to measure the extension. A spirit level ensures horizontal alignment.
    *   **Labels/Values:** "Control wire", "Test wire", "Micrometer", "Spirit level", "Weights", "Reading of extension".
    *   **Intended Teaching Purpose:** To illustrate the experimental setup for determining Young's Modulus.
    *   **How to Redraw:** A clear, labeled diagram of the apparatus.

---

## 6. Phuc-Specific Mistake and Misconception Bank

This section highlights specific instances where Phuc demonstrated a misunderstanding or hesitation, along with the correction and a suggested drill.

1.  **Mistake:** Initial definition of Hooke's Law (02:05)
    *   **Phuc's Statement/Action:** "So I think I remember there's something like proportional. So the displacement of the spring is proportional to a constant, and that constant is the Hooke constant, if I recall correctly."
    *   **What it Reveals:** Phuc understands the proportionality and the existence of a constant but struggles with the precise wording of Hooke's Law (Force is proportional to extension).
    *   **Correction:** Hooke's Law states that the force applied is directly proportional to the extension produced, provided the elastic limit is not exceeded. The constant of proportionality is the spring constant (k).
    *   **Drill:** Flashcards with "State Hooke's Law" and "What is the constant of proportionality in Hooke's Law called?".

2.  **Mistake:** Spring constant definition (03:20)
    *   **Phuc's Statement/Action:** "So maybe like it's the physical property of a material. So it would determine like given the same force, then what is the amount of extension."
    *   **What it Reveals:** Phuc has a conceptual understanding but struggles with a precise, concise definition. He also mixes up "spring constant" with "Young's modulus" (material property).
    *   **Correction:** The spring constant (k) is the force required per unit extension (F/x). Young's Modulus is the material property.
    *   **Drill:** Practice defining 'spring constant' and 'Young's modulus' and explaining the difference.

3.  **Mistake:** Resistors in parallel (04:00)
    *   **Phuc's Statement/Action:** (After Alex draws parallel resistors) "Maybe it's divide by half."
    *   **What it Reveals:** Phuc has a vague idea of inverse relationship but doesn't recall the exact formula for parallel resistors.
    *   **Correction:** For resistors in parallel, $1/R_{total} = 1/R_1 + 1/R_2$.
    *   **Drill:** Practice calculating total resistance for various series and parallel resistor combinations.

4.  **Mistake:** Safety precaution for spring experiment (07:00)
    *   **Phuc's Statement/Action:** (When asked what to do first with a spring) "Glove."
    *   **What it Reveals:** Phuc thinks about general lab safety but misses the specific hazard of springs.
    *   **Correction:** The primary safety precaution for spring experiments is to wear safety glasses, as springs can detach and fly off, causing eye injury.
    *   **Drill:** List specific hazards and corresponding safety precautions for common physics experiments (e.g., electricity, mechanics, heat).

5.  **Mistake:** Stress definition (10:30)
    *   **Phuc's Statement/Action:** "So Hooke's Law is the amount of force that required to extend per unit area. So by by one meter."
    *   **What it Reveals:** Phuc confuses Hooke's Law with stress and also struggles with the units/meaning of "per unit area" vs "per unit length".
    *   **Correction:** Hooke's Law is F=kx. Stress is Force per unit area (F/A).
    *   **Drill:** Flashcards for definitions of Hooke's Law, stress, and strain, focusing on their distinct formulas and units.

6.  **Mistake:** Calculating stress in Q9 (18:30)
    *   **Phuc's Statement/Action:** Phuc calculates strain but then attempts to calculate stress without force or Young's modulus.
    *   **What it Reveals:** Phuc doesn't immediately recognize when there's insufficient information to solve for a variable.
    *   **Correction:** Stress ($\sigma$ = F/A) requires force and area. Young's Modulus (E = $\sigma$/$\varepsilon$) requires stress and strain. Without force or Young's modulus, stress cannot be calculated.
    *   **Drill:** Practice identifying knowns and unknowns in problems and listing all relevant formulas before attempting calculations.

7.  **Mistake:** Understanding "pre-strain" (12:00)
    *   **Phuc's Statement/Action:** "What do they mean by amount of pre-strain?"
    *   **What it Reveals:** Phuc is unfamiliar with specific terminology used in contextualized exam questions.
    *   **Correction:** "Pre-strain" is simply the initial strain applied to the material before it is subjected to further conditions (e.g., temperature changes). In this context, it is the given strain value.
    *   **Drill:** Review exam-style questions with unfamiliar terminology and practice inferring their meaning from context or relating them to known physics concepts.

---

## 7. Exam Technique and Practical Wording

This section provides advice on exam technique and model answers for practical descriptions, formatted for Edexcel A-level.

### 7.1. General Exam Technique Advice

*   **Don't Give Anything Away:** When asked a question, provide the direct answer first, then elaborate if necessary. Avoid rambling or providing incorrect information.
*   **Show Your Working:** Always present your calculations clearly, step-by-step, including formulas, substitutions, and units. This allows for partial credit even if the final answer is wrong.
*   **Unit Consistency:** Ensure all values are converted to SI units (meters, Newtons, Pascals, etc.) before performing calculations.
*   **Significant Figures:** Pay attention to the number of significant figures in the given data and present your final answer to an appropriate number of significant figures.
*   **Contextual Understanding:** For application-based questions, read the prompt carefully to understand the real-world scenario and how physics principles apply. Unfamiliar terms might just be contextual labels for known quantities (e.g., "pre-strain" is just strain).
*   **Retrieval Practice:** Regularly test yourself on definitions, formulas, and concepts to ensure quick and accurate recall during exams.

### 7.2. Model Answer: Hooke's Law Practical

**Aim:** To investigate the relationship between force and extension for a spring and determine its spring constant.

**Apparatus:**
*   Retort stand and clamp
*   Spring
*   Set of slotted masses (e.g., 100g, 200g, etc.)
*   Mass hanger
*   Meter rule (or ruler with mm scale)
*   Pointer (attached to the bottom of the spring/mass hanger)
*   Safety goggles
*   G-clamp (to secure the retort stand to the bench)

**Method:**
1.  Secure the retort stand firmly to the edge of a workbench using a G-clamp.
2.  Hang the spring from the clamp on the retort stand.
3.  Attach a mass hanger (e.g., 50g) to the bottom of the spring. This provides an initial load to straighten the spring and sets the zero point.
4.  Position the meter rule vertically alongside the spring, ensuring the zero mark aligns with a pointer attached to the bottom of the mass hanger. Record this initial reading as the original length ($L_0$).
5.  Carefully add a known mass (e.g., 100g) to the hanger. Record the total mass (m) and the new reading on the meter rule ($L_1$).
6.  Calculate the force (F) applied to the spring using $F = mg$, where $g$ is the acceleration due to gravity (9.81 N/kg).
7.  Calculate the extension ($\Delta$x) of the spring using $\Delta x = L_1 - L_0$.
8.  Repeat steps 5-7 by adding further masses in equal increments (e.g., 100g at a time), recording the total mass, new length, and calculating the force and extension for each load.
9.  Continue adding masses until the spring's elastic limit is approached (indicated by non-linear extension or permanent deformation). Do not exceed the elastic limit.
10. Plot a graph of Force (y-axis) against Extension (x-axis).

**Calculations and Analysis:**
1.  The gradient of the linear portion of the Force-Extension graph represents the spring constant (k) of the spring ($k = \Delta F / \Delta x$).
2.  The area under the Force-Extension graph represents the elastic strain energy stored in the spring ($E = \frac{1}{2} F \Delta x$).

**Uncertainty Improvements:**
*   **Zero Error:** Ensure the meter rule is correctly aligned with the pointer at zero load, or account for any zero error.
*   **Parallax Error:** Read the meter rule at eye level to minimize parallax error.
*   **Multiple Readings:** Take multiple readings for each mass and average them to reduce random errors.
*   **Repeat Experiment:** Repeat the entire experiment several times and average the calculated spring constants.
*   **Mass Measurement:** Use a digital balance to accurately measure the masses.

### 7.3. Model Answer: Young's Modulus Practical (Searle's Apparatus)

**Aim:** To determine the Young's Modulus of a material in the form of a wire.

**Apparatus:**
*   Searle's apparatus (two identical wires, one control, one test, suspended from a rigid support).
*   Micrometer screw gauge
*   Meter rule
*   Spirit level
*   Slotted masses and hangers
*   Safety goggles
*   Sand tray

**Method:**
1.  **Measure Wire Diameter:** Use a micrometer screw gauge to measure the diameter (d) of the test wire at several different points along its length and in different orientations. Calculate the average diameter.
2.  **Calculate Cross-sectional Area (A):** Use the average diameter to calculate the cross-sectional area of the wire using $A = \pi (d/2)^2$.
3.  **Measure Original Length (x):** Measure the original length (x) of the test wire between the points where it is clamped.
4.  **Set up Apparatus:**
    *   Suspend both the control wire and the test wire from a common, rigid support.
    *   Attach a vernier scale to the test wire and a main scale to the control wire.
    *   Attach a spirit level to the vernier scale.
    *   Apply a small initial tension (e.g., a small mass) to both wires to straighten them and remove any kinks. This also sets the zero reading for the vernier scale.
5.  **Apply Load:** Gradually add known masses (m) to the hanger on the test wire.
6.  **Measure Extension ($\Delta$x):** For each added mass, carefully adjust the spirit level to ensure the vernier scale is horizontal. Read the extension ($\Delta$x) from the vernier scale.
7.  **Record Data:** Record the total mass (m) and the corresponding extension ($\Delta$x). Calculate the force (F) using $F = mg$.
8.  **Repeat and Check:** Continue adding masses in equal increments, recording data, until the wire's elastic limit is approached. Remove the masses gradually and check if the wire returns to its original length.
9.  **Plot Graph:** Plot a graph of Stress (y-axis) against Strain (x-axis).

**Calculations and Analysis:**
1.  **Calculate Stress ($\sigma$):** For each force (F), calculate stress using $\sigma = F/A$.
2.  **Calculate Strain ($\varepsilon$):** For each extension ($\Delta$x), calculate strain using $\epsilon = \Delta x/x$.
3.  **Determine Young's Modulus (E):** The gradient of the linear portion of the Stress-Strain graph represents the Young's Modulus of the material ($E = \Delta \sigma / \Delta \epsilon$).

**Safety Precautions:**
*   **Safety Goggles:** Always wear safety goggles to protect eyes from snapping wires.
*   **Sand Tray:** Place a sand tray beneath the weights to cushion any falling masses.
*   **Avoid Overloading:** Do not exceed the elastic limit of the wire to prevent it from snapping.
*   **Secure Clamps:** Ensure all clamps are securely tightened.

**Uncertainty Improvements:**
*   **Micrometer:** Use a micrometer screw gauge for diameter measurement (high precision). Take multiple readings and average.
*   **Vernier Scale:** Use a vernier scale for extension readings (high precision).
*   **Control Wire:** The control wire is crucial. It compensates for any yielding of the support or changes in temperature, ensuring that only the extension of the test wire due to the applied load is measured.
*   **Plotting Graph:** Plotting a graph and finding the gradient is more accurate than using a single set of readings.
*   **Repeat Readings:** Repeat measurements for diameter, length, and extension multiple times and average to reduce random errors.

---





# Complete worked exercise appendix for the Hooke/stress lesson

This appendix gives the full worked sequence of Core and Further materials questions from the Hooke/stress lesson video.

## Core Q1: copper wire stiffness

**Video prompt.** A force of $160\,\mathrm{N}$ extends a copper wire by $2.7\,\mathrm{cm}$. Calculate the stiffness constant of the wire.

**Thought process.** The question gives force and extension only. It does not give original length or area, so it is not a Young modulus question. Use Hooke's law in the form $F=kx$.

Convert the extension:
\[
2.7\,\mathrm{cm}=2.7\times10^{-2}\,\mathrm{m}=0.027\,\mathrm{m}.
\]
Then
\[
k=\frac{F}{x}=\frac{160}{0.027}=5.93\times10^3\,\mathrm{N\,m^{-1}}.
\]

**Answer.** $5.9\times10^3\,\mathrm{N\,m^{-1}}$.

**Phuc/Alex note.** Phuc correctly identified $F=160\,\mathrm{N}$ and converted $2.7\,\mathrm{cm}$ to $0.027\,\mathrm{m}$; Alex confirmed the method.

## Core Q2: spring extension and new length

**Video prompt.** A $12\,\mathrm{N}$ weight is hung on a spring $5.0\,\mathrm{cm}$ long with spring constant $8500\,\mathrm{N\,m^{-1}}$. Calculate (a) the extension and (b) the new length.

**Thought process.** Force and spring constant trigger $F=kx$. The spring length is separate from extension: first find $x$, then add it to the original length.

\[
x=\frac{F}{k}=\frac{12}{8500}=1.41\times10^{-3}\,\mathrm{m}=0.141\,\mathrm{cm}.
\]
Original length:
\[
5.0\,\mathrm{cm}=0.050\,\mathrm{m}.
\]
New length:
\[
L_{new}=0.050+0.00141=0.05141\,\mathrm{m}=5.141\,\mathrm{cm}.
\]

**Answers.** Extension $=1.41\times10^{-3}\,\mathrm{m}$; new length $=5.14\,\mathrm{cm}$.

## Core Q3: horizontal plank stiffness

**Video prompt.** A horizontal plank is supported at each end. A child of mass $55\,\mathrm{kg}$ stands on the centre; the centre moves down $4.0\,\mathrm{mm}$. Calculate the stiffness constant of the plank.

**Thought process.** The force is not directly given; mass is given. First convert mass to weight, then use stiffness $k=F/x$.

\[
F=mg=55(9.81)=539.55\,\mathrm{N}.
\]
\[
x=4.0\,\mathrm{mm}=4.0\times10^{-3}\,\mathrm{m}.
\]
\[
k=\frac{F}{x}=\frac{539.55}{0.0040}=1.35\times10^5\,\mathrm{N\,m^{-1}}.
\]

**Answer.** $1.3\times10^5\,\mathrm{N\,m^{-1}}$ to two significant figures.

## Core Q4: identical springs in series/parallel

**Video prompt.** Two identical springs have spring constant $240\,\mathrm{N\,m^{-1}}$ and natural length $210\,\mathrm{mm}$. Calculate the length of each spring when (a) they are joined vertically and stretched with $8.0\,\mathrm{N}$, and (b) they are joined in parallel and stretched with $8.0\,\mathrm{N}$.

**Thought process for series.** In a vertical series chain, the same force passes through each spring. Therefore calculate the extension of each individual spring using the original $k$, not the effective $k$ if the question asks for each spring's length.

\[
x_{each}=\frac{F}{k}=\frac{8.0}{240}=0.0333\,\mathrm{m}.
\]
Natural length:
\[
210\,\mathrm{mm}=0.210\,\mathrm{m}.
\]
Length of each spring:
\[
L_{each}=0.210+0.0333=0.243\,\mathrm{m}.
\]
Total chain length, if asked, would be $2(0.243)=0.487\,\mathrm{m}$.

**Thought process for parallel.** In parallel, the force is shared equally, so each spring carries $4.0\,\mathrm{N}$.

\[
x_{each}=\frac{4.0}{240}=0.0167\,\mathrm{m}.
\]
\[
L_{each}=0.210+0.0167=0.227\,\mathrm{m}.
\]

**Answers.** Series: each spring $0.243\,\mathrm{m}$. Parallel: each spring $0.227\,\mathrm{m}$.

**Correction note.** A common misleading shortcut is to use the effective series stiffness and then add the total extension to one spring. That gives the chain extension, not the length of each spring.

## Further Q5: force-extension graph and gradient

**Video prompt.** Force applied to a spring gives data: force/N $=0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0$ and length/cm $=2.6,2.8,3.0,3.2,3.4,3.6,3.9,4.3$. Plot a force-extension graph, explain the shape, and calculate the spring constant.

**Thought process.** The graph must use extension, not raw length. Natural length is the zero-force length, $2.6\,\mathrm{cm}$. Subtract it from every length.

Extensions/cm:
\[
0.0,0.2,0.4,0.6,0.8,1.0,1.3,1.7.
\]
The graph is initially straight, then begins to curve as the spring approaches or passes the limit of proportionality. The spring constant comes from the gradient of the straight part. Using the full rough range gives:
\[
k=\frac{\Delta F}{\Delta x}=\frac{7.0}{1.7\,\mathrm{cm}}=4.12\,\mathrm{N\,cm^{-1}}.
\]
Convert:
\[
4.12\,\mathrm{N\,cm^{-1}}=412\,\mathrm{N\,m^{-1}}.
\]

**Answer.** Approximate stiffness $=4.1\times10^2\,\mathrm{N\,m^{-1}}$.

**Alex note.** Alex reminded Phuc to convert the gradient to $\mathrm{N\,m^{-1}}$.

## Further Q6: tensile stress in a bridge cable

**Video prompt.** Calculate tensile stress in a suspension bridge cable of diameter $50\,\mathrm{mm}$ pulling up on the roadway with force $4\,\mathrm{kN}$.

**Thought process.** Tensile stress is force divided by cross-sectional area. Diameter is given, so halve it to get radius.

\[
F=4\,\mathrm{kN}=4000\,\mathrm{N},\qquad d=50\,\mathrm{mm}=0.050\,\mathrm{m},\qquad r=0.025\,\mathrm{m}.
\]
\[
A=\pi r^2=\pi(0.025)^2=1.96\times10^{-3}\,\mathrm{m^2}.
\]
\[
\sigma=\frac{F}{A}=\frac{4000}{1.96\times10^{-3}}=2.04\times10^6\,\mathrm{Pa}=2.04\,\mathrm{MPa}.
\]

**Answer.** $2.0\,\mathrm{MPa}$.

## Further Q7: crane cable extension

**Video prompt.** A crane has a steel lifting cable of diameter $30\,\mathrm{mm}$. Steel has Young modulus $200\,\mathrm{GPa}$. The crane lifts $20\,\mathrm{kN}$ and the unstretched cable length is $25.0\,\mathrm{m}$. Calculate the extension.

**Thought process.** This is a Young modulus extension question. Use $E=FL/(A\Delta L)$ rearranged to $\Delta L=FL/(AE)$.

\[
d=0.030\,\mathrm{m},\quad r=0.015\,\mathrm{m},\quad A=\pi(0.015)^2=7.07\times10^{-4}\,\mathrm{m^2}.
\]
\[
E=200\,\mathrm{GPa}=200\times10^9\,\mathrm{Pa},\qquad F=20\,\mathrm{kN}=20000\,\mathrm{N}.
\]
\[
\Delta L=\frac{FL}{AE}=\frac{(20000)(25.0)}{(7.07\times10^{-4})(200\times10^9)}=3.53\times10^{-3}\,\mathrm{m}=3.53\,\mathrm{mm}.
\]

**Answer.** $3.5\,\mathrm{mm}$.

## Further Q8: rubber band strain and new length

**Video prompt.** A rubber band was $8.4\,\mathrm{cm}$ long before stretching. It is stretched until its strain is $2.45$. Calculate its new total length.

**Thought process.** Strain is extension divided by original length. Therefore extension equals strain times original length.

\[
L_0=8.4\,\mathrm{cm}=0.084\,\mathrm{m}.
\]
\[
\Delta L=\varepsilon L_0=2.45(0.084)=0.2058\,\mathrm{m}.
\]
\[
L_{new}=L_0+\Delta L=0.084+0.2058=0.2898\,\mathrm{m}=29.0\,\mathrm{cm}.
\]

**Answer.** $29.0\,\mathrm{cm}$.

## Further Q9: impossible stress question / missing data

**Video prompt.** A copper wire under tension is initially $1.52\,\mathrm{m}$ long and stretches by $3.2\,\mathrm{mm}$. Calculate its stress.

**Thought process.** The given data allow strain, not stress. Stress needs force and area, or Young modulus plus strain.

\[
\varepsilon=\frac{\Delta L}{L_0}=\frac{0.0032}{1.52}=2.1\times10^{-3}.
\]
But
\[
\sigma=\frac{F}{A}
\]
requires force and area, neither of which is provided. Alternatively, $\sigma=E\varepsilon$ would require Young modulus, which is also not provided.

**Answer.** Stress cannot be calculated from the information given. The missing information is force and cross-sectional area, or Young modulus.

**Alex note.** Alex pointed out that Phuc should identify what is missing rather than forcing a formula.

## Further Q10: brass pin maximum force

**Video prompt.** A brass pin has cross-sectional area $0.30\,\mathrm{cm^2}$. Brass tensile strength is $190\,\mathrm{MPa}$. Calculate the maximum tensile force before breaking.

**Thought process.** Tensile strength is maximum stress. Rearrange stress to $F=\sigma A$.

\[
A=0.30\,\mathrm{cm^2}=0.30\times10^{-4}\,\mathrm{m^2},
\qquad \sigma=190\times10^6\,\mathrm{Pa}.
\]
\[
F=(190\times10^6)(0.30\times10^{-4})=5700\,\mathrm{N}=5.7\,\mathrm{kN}.
\]

**Answer.** $5.7\,\mathrm{kN}$.

## Further Q11: piano wire minimum diameter

**Video prompt.** Mild steel has breaking strength $500\,\mathrm{MPa}$. A single wire must support a $200\,\mathrm{kg}$ piano. Calculate minimum diameter.

**Thought process.** Convert the mass to weight, calculate required area from stress, then convert area to diameter.

\[
F=mg=200(9.81)=1962\,\mathrm{N}.
\]
\[
A=\frac{F}{\sigma}=\frac{1962}{500\times10^6}=3.924\times10^{-6}\,\mathrm{m^2}.
\]
\[
r=\sqrt{\frac{A}{\pi}}=\sqrt{\frac{3.924\times10^{-6}}{\pi}}=1.117\times10^{-3}\,\mathrm{m}.
\]
\[
d=2r=2.23\times10^{-3}\,\mathrm{m}=2.23\,\mathrm{mm}.
\]

**Answer.** Minimum diameter $=2.23\,\mathrm{mm}$.

## Further Q12: bolt/harness minimum Young modulus

**Video prompt.** A bolt is $5.0\,\mathrm{cm}$ long with cross-sectional area $0.25\,\mathrm{cm^2}$. It must extend by no more than $0.02\,\mathrm{mm}$ when supporting a $90.0\,\mathrm{kg}$ mass. Calculate the minimum Young modulus.

**Thought process.** Use $E=FL/(A\Delta L)$ because the question links load, original length, area and maximum extension.

\[
L=0.050\,\mathrm{m},\quad A=0.25\times10^{-4}\,\mathrm{m^2},\quad \Delta L=0.02\times10^{-3}\,\mathrm{m}.
\]
\[
F=mg=90.0(9.81)=882.9\,\mathrm{N}.
\]
\[
E=\frac{(882.9)(0.050)}{(0.25\times10^{-4})(0.02\times10^{-3})}=8.83\times10^{10}\,\mathrm{Pa}=88.3\,\mathrm{GPa}.
\]

**Answer.** Minimum Young modulus $=8.83\times10^{10}\,\mathrm{Pa}$.

# Consolidated Phuc-specific redo plan

## Immediate drills

1. **Micrometer drill:** 20 readings. For every reading write: sleeve/main scale + thimble scale = final reading.
2. **Vernier drill:** 20 readings. For every reading write: main scale before Vernier zero + aligned Vernier division times resolution = final reading.
3. **Density drill:** Redo whisky, balloon, hockey ball, room air and brass alloy from a blank page.
4. **Hooke vs Young modulus drill:** Sort 20 prompts into: Hooke's law, stress, strain, Young modulus, or density. Only then write formulas.
5. **Diameter-to-area drill:** 10 examples where diameter is given and area is required. Always halve first.

## Minimum standard for a calculation answer

A full-mark calculation answer should show:

1. Given values with units.
2. Unit conversions.
3. Formula.
4. Rearrangement if needed.
5. Substitution.
6. Final answer with units.
7. Comment/sanity check if asked.

## Minimum standard for a practical answer

A full-mark practical method should include:

1. Apparatus.
2. What to measure.
3. How to calculate the needed quantity.
4. Repeats/mean.
5. Uncertainty reduction.
6. Specific systematic errors to avoid.

# Final compact formula sheet

\[
\rho=\frac{m}{V},\qquad p=\frac{F}{A},\qquad p=h\rho g
\]

\[
U=\rho Vg,\qquad F_D=6\pi\eta rv
\]

\[
F=kx,
\qquad E_e=\frac12Fx=\frac12kx^2
\]

\[
\sigma=\frac{F}{A},\qquad \varepsilon=\frac{\Delta L}{L},\qquad E=\frac{\sigma}{\varepsilon}=\frac{FL}{A\Delta L}
\]

\[
A=\pi\left(\frac{d}{2}\right)^2,
\qquad V_{sphere}=\frac43\pi r^3,
\qquad V_{cylinder}=\pi r^2h.
\]

# Final warning list

- Do not read only the main scale on a micrometer.
- Do not read a Vernier caliper from the wrong zero.
- Do not use diameter as radius.
- Do not cube centimetres as if they were metres.
- Do not average densities blindly for a mixture unless the physical condition justifies it.
- Do not write $F=kL$ for Hooke's law unless $L$ has explicitly been defined as extension.
- Do not use $\pi d^2$ for cable/wire area.
- Do not confuse stress with pressure just because they share units.
- Do not give a calculation answer without units.
- Do not write vague practical improvements; name the exact uncertainty and how it is reduced.
