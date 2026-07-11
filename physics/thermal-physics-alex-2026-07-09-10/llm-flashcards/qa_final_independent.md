# Final independent QA — curated Thermal Physics LLM flashcard deck

## Release verdict: **FAIL — do not publish unchanged**

- Audited deck: `selected_cards_full.json`
- Frozen deck SHA-256: `ec4fc1f3573581e9369e08b2fff63865f35724072224a7d5385376a82e51c556`
- JSON shape/count: valid array of **108** cards; every card has `question`, `answer`, `source`, and unique `_id`.
- Index convention: **0-based JSON-array index**; card number is index + 1.
- Results: **PASS 107 / FAIL 1 / total 108**.
- No publishing or card edits were performed.

## Method

Every question/answer was read against the current `revision_guide.tex` and the lesson `transcript_evidence_digest.md`, with independent checks of formulas, units, arithmetic, stated conditions, source-safe learner attribution, context, semantic duplication, reasoning-draft leakage, and LaTeX/control-character integrity.

Deterministic checks found:

- 108 cards and 108 unique IDs.
- No duplicate normalized questions; no high-overlap duplicate pair in the final curated set.
- No forbidden control characters, NULs, unmatched `$$` delimiters, malformed slash patterns, or banned reasoning-draft/generator phrases.
- The three previously corrected retained cards are now sound: index 2 (Herschel/thermal-IR mechanism), index 20 (avocado calculation: `c = 3009.302... J kg^-1 K^-1`, `Δθ = 4.64 K` under its stated convention), and index 62 (infrared is electromagnetic, not nuclear, radiation).
- The source-attributed Phuc/Alex cards were checked against the transcript digest; no unsupported learner attribution remains in this 108-card selection.

## Failing card

### Index 75 (card 76) — `glm_2_34` — **HIGH FAIL**

**Exact question:**

> A gas molecule has mass $$5.3 \times 10^{-26}$$ kg. At room temperature (≈ 300 K), roughly what is its average kinetic energy? No calculator needed — estimate the order of magnitude. (2 steps)

**Failure category:** Physics / numerical factual error.

**Issue:** The calculation in the answer is correct:

$$\frac{3}{2}kT \approx 6.3\times10^{-21}\ \mathrm{J}.$$

However, its final explanatory sentence states that there are “~$$10^{25}$$ molecules in a mole.” One mole contains exactly

$$N_A=6.02214076\times10^{23}\ \mathrm{mol^{-1}},$$

so its order of magnitude is $$10^{24}$$, not $$10^{25}$$. This is a standalone factual error in a card intended to build order-of-magnitude intuition.

**Required correction:** Replace “~$$10^{25}$$ molecules in a mole” with “$$6.02\times10^{23}$$ molecules per mole (of order $$10^{24}$$).” Retain the kinetic-energy calculation unchanged.

## Complete audit ledger

`PASS` below means no release-blocking defect was found in this independent pass. The exact question text remains in the frozen source JSON named above; the failed card is reproduced in full above.

| Indices | Verdict | IDs |
|---|---|---|
| 0–11 | PASS | `minimax_1_61`, `opus_2_40`, `minimax_2_7`, `glm_2_44`, `opus_1_61`, `glm_3_17`, `opus_2_35`, `minimax_2_60`, `minimax_1_75`, `minimax_2_74`, `minimax_2_41`, `qwen_2_15` |
| 12–23 | PASS | `opus_2_54`, `glm_3_18`, `opus_1_55`, `minimax_1_77`, `glm_2_37`, `glm_3_15`, `minimax_2_62`, `opus_1_42`, `glm_2_20`, `opus_1_33`, `glm_2_57`, `opus_1_78` |
| 24–35 | PASS | `minimax_1_101`, `minimax_2_8`, `glm_3_19`, `opus_2_38`, `minimax_1_55`, `glm_3_4`, `glm_2_69`, `opus_1_75`, `glm_3_5`, `opus_2_73`, `minimax_1_37`, `minimax_2_77` |
| 36–47 | PASS | `minimax_2_96`, `minimax_1_107`, `opus_2_28`, `opus_1_49`, `opus_1_38`, `opus_2_4`, `opus_2_19`, `minimax_1_63`, `opus_1_57`, `glm_3_40`, `qwen_2_5`, `minimax_1_51` |
| 48–59 | PASS | `glm_2_46`, `glm_3_38`, `glm_2_41`, `minimax_2_92`, `minimax_1_90`, `minimax_1_71`, `qwen_2_6`, `opus_1_54`, `minimax_2_46`, `minimax_1_99`, `opus_1_68`, `minimax_2_55` |
| 60–71 | PASS | `minimax_2_91`, `glm_2_62`, `minimax_2_9`, `glm_2_67`, `glm_2_24`, `opus_2_50`, `glm_2_18`, `minimax_1_102`, `opus_1_82`, `minimax_2_66`, `opus_1_17`, `glm_3_14` |
| 72–74 | PASS | `opus_1_41`, `opus_1_26`, `glm_2_53` |
| 75 | **FAIL** | `glm_2_34` |
| 76–87 | PASS | `glm_2_9`, `opus_1_64`, `glm_2_60`, `minimax_1_66`, `minimax_2_69`, `opus_2_42`, `opus_2_68`, `opus_1_5`, `minimax_2_86`, `minimax_1_62`, `glm_2_39`, `glm_3_25` |
| 88–99 | PASS | `glm_2_42`, `minimax_1_65`, `opus_1_65`, `opus_1_48`, `minimax_1_100`, `glm_3_7`, `glm_3_16`, `minimax_2_97`, `minimax_2_73`, `glm_2_56`, `glm_3_35`, `glm_3_2` |
| 100–107 | PASS | `minimax_1_106`, `minimax_1_43`, `minimax_2_87`, `minimax_2_52`, `minimax_2_48`, `opus_1_59`, `glm_2_64`, `glm_2_58` |

## Publication gate

**FAIL.** Apply the single required correction to index 75/card 76, then re-run this final QA gate. A one-card correction is sufficient; no broad remediation or deduplication pass is required.
