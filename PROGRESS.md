# Pokémon FireRed Progress Log (Goal: Hall of Fame)

## CURRENT STATE (2026-06-13 09:40) — Mt Moon B2F (grunt room), EXECUTING DELIBERATE BLACKOUT
- カメール **Lv26, 60/75**, no status. PP: Bite 0/25, WaterGun 2/25, **Bubble ~20/30 (slot3)**, RapidSpin 0/30.
- Weedle+Pikachu FAINTED (sacrificed). Bag: げんきのかけら×1, どくけし×3, ふしぎなアメ×1, つきのいし×1. NO balls/potions/ropes.
- **PLAN: faint Wartortle via B2F wilds (Lv9-12 Paras/Zubat chip 4-8/turn) → blackout → Pewter PC → shop (balls/potions/ropes) → re-enter Mt Moon → follow walkthrough EXACTLY from entrance.**
- Battle macro: A(intro)→2000 → A(FIGHT)→1800 → **D200,L200 (clamp slot3 Bubble)** → A→11000 → [turn2: A→1800→A→11000] → A→2500→A (dismiss). Cursor does NOT persist between battles; clamp EVERY battle. In-battle it persists (turn2 = A,A).
- RUN macro (when navigating): A130→2500 → R200→400 → D200→400 → A130→4000 → A130→2200.

## WALKTHROUGH (guidestrats, fetched 08:32) — CANONICAL ROUTE
- 1F: entrance → **N to trainer by SIGN** (Picnicker zone S-center) → **E until rock divider (spine)** → **N until ladder** → take it down.
- B1F: "follow corridor down and to the right" → end ladder → B2F.
- B2F: arrival → N (see Revive ball) → back S near ladder → **steps down to the EAST** → past grunt → **stairs UP to the right** → **S on the rocky hill (the raised road!)** → grunt #2 → N → Super Nerd + 2 fossils → "two ladders up" → Route 4 exit corridor.
- Bulbapedia: FRLG Mt Moon ≈ RBY layout. Revive in fenced pocket = likely needs its own ladder pair ("closed-off room via easternmost ladder").

## SESSION FINDINGS (06:00-09:40)
- Whittle on 1F terrace USELESS: Lv7-8 wilds never get a turn (62/73 static for an hour). B2F Lv10 Paras DOES chip (58/73→ took 4/turn). Lv26 level-up +2 max HP (60/75).
- **Rapid Spin PP exhausted** (0/30); Bite 0; Bubble was 27/30 at 07:10 (NOT ~13 as old note said).
- 1F geography (hours of testing): SE sand corner SEALED (S+E bonk). Sand-on-band crossings ALL fake (graphics only). NW zigzag cliff = decorative, no stairs from below. NE corner (spine×N-wall) sealed. Mid-W sand ramp notch (W of mesa, ~x250 col) — APPROACH BLOCKED by mesa; never tested directly.
- **TWO warp ladders on 1F mid-W confirmed**: (a) plateau-pair ladder (notch between stacked mesas) ⇄ HUB; (b) sand-area ladder (open green W of stepped sand, NW of Picnicker zone, S of plateau pair) ⇄ pocket A.
- HUB layout corrected: spring N-center; SW hole (dark+rungs) → FIELD ROOM; **standing ladder at hub's FAR EAST (by E boulders) → 1F plateau notch**. Hub warps need step-OFF-step-ON to re-trigger.
- FIELD ROOM: S band swept tile-by-tile E-W — **NO stair into pens basin. Sealed everywhere.** W column w/ crater unreachable (inner wall runs N to room wall). Pens basin NOT enterable from field room. Clefairy Lv8+Lv12 seen here (no balls!).
- GRUNT ROOM (B2F via corridor-mid ladder): arrival NE (1S of return ladder, boulders W). Revive on fenced platform W of arrival — platform ringed (fence S, rocks E/W/N), no entry found. Road (raised, sawtooth teeth) rings floor: S band + N-S arm E of arrival + N corridor under thin band. **Road W face tested at MANY columns incl. corner junctions: ALL sealed.** Alcove N of floor (under band): N bonks at x~870/960/1010 = sealed. Lip-road SE junction: sealed. **"Steps to the east" NOT FOUND from floor — suspect canonical route enters B2F from a DIFFERENT B1F ladder (my corridor opens WEST, walkthrough says down-and-RIGHT) and the steps descend from the arrival area I can't reach.**
- Return ladder from grunt room arrival: could NOT relocate after wandering (N sealed everywhere S of it?!) — the arrival anteroom may be separate from the main floor, entered via a S-leading passage I fell through but can't find back. (Don't get stranded here again!)
- OBS: frames sometimes render PARTIAL (quadrant/strip) or small-res — transient; content readable; full frames return next cycle.

## ROUTE AFTER PEWTER RESPAWN
1. Pewter Mart: Poké Balls ×8-10, Potions ×4-6, Escape Ropes ×2-3, Antidotes ×2 (budget ~1500 post-blackout).
2. Route 3 E (trainers beaten) → Mt Moon entrance.
3. **Inside: N to sign-Picnicker → E to spine → N along spine W-side checking EVERY row/column for the FIRST LADDER (it exists per walkthrough; pillars may hide it).** Take it → B1F down-and-RIGHT corridor → end ladder → TRUE B2F arrival → N (Revive) → S → E steps → grunt → E stairs up → S on road → grunt #2 → N → Super Nerd/fossils → 2 ladders up → ROUTE 4.
4. Catch CLEFAIRY when seen (have balls!). Cerulean PC → Misty.

## SCRATCH FILES: obs_fix.py, obs_test2.py, obs_regrab.py — safe to delete.
