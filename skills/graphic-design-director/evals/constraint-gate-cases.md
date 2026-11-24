# Hard-constraint regression suite — prevent polished wrong designs

## Case A — WAKU reference adapted to Pickam (2026-11-19)

- **Inputs:** `image(6).png` WAKU layout (source 735 × 490, 3:2) and `Pickam Bike Truck Brand Moodboard.png` (1536 × 1024, 3:2). User asks to adapt first image into a Pickam delivery-company design; later explicitly corrects wrong dominant red and wrong portrait output.
- **Hard locks:** 1536 × 1024 PNG, landscape 3:2; Pickam wordmark/logo and Move • Deliver • Haul context; Forest `#0E4B38` / Lime `#C4EE3A` / Paper `#F6F5EC` / Mist `#E1EDD4` as dominant system. Alert Red `#E5301F` and Load Orange `#FF6A13` are optional accents only.
- **Reference locks:** strong multicolumn editorial grid; top identity block, adjacent headline block, hero-photo block and tall right column; lower product/service/category/color content, bottom photographic/product fragments. Replace source imagery and copy, not the overall visual logic.
- **Automatic fails:** portrait 4:5 export, huge saturated-red backgrounds, leftover WAKU name, made-up app store branding or actual QR claims.
- **Fidelity review:** geometric regions and photo hierarchy, preserving role of tall right column; note whether original app demo panel was changed.
- **Current evidence:** `a_detailed_stylized_brand_board_collage_for_pick.png` was 1122 × 1402 (wrong orientation, dominant red) => fail. `a_clean_modern_graphic_design_brand_moodboard_u.png` is 1536 × 1024, Forest/cream dominant, but altered the tall right phone mockup => needed revision. New `a_meticulously_designed_graphic_brand_board_land.png` is 1536 × 1024, with right phone/demo panel restored and measurable saturated-red fraction 0.74%, below the 5% alarm threshold => **mechanical PASS; stronger visual fidelity**, with generated logo/type remaining provisional.

## Case B — Text-free flat transport comparison

Input: 4:5 split road, cargo tricycle left small, mini-truck right larger, top 35% empty, blank pill-shaped tags, Forest livery, Lime stripe, no photo/3D/gradient/outline/text.

Fail for photorealistic trucks, text inside labels, speech-bubble callouts instead of blank pills, or active content in top 35%. No compensatory aesthetic score.

## Case C — Standalone rope poster

Input: concept image only, atmospheric blue, rope/human metaphor and one requested headline, no UI. Fail for nav menu, bookmark icon or portfolio credits.

## Case D — Authorized in-panel UI

A source brand-board intentionally includes a product/app phone preview as one composition panel. In precise ADAPT, its *panel position and function* are reference features, not automatic UI contamination; preserve it with branded content unless user asks to replace it. Exclude any unrelated browser/window chrome.

## Case E — Open originality versus fidelity

Two consecutive unrelated original briefs should explore different structural styles, not repeat floating serif/cream-grid/hand collage by default. A faithful ADAPT is exempt from style-diversity pressure.
