# Wednesday, 18 November 2026 — World News on One Page

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/chocolatos72/world-news-18-nov-2026/rank.svg)](https://make.fun/c/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/chocolatos72/world-news-18-nov-2026/reward.svg)](https://make.fun/c/news-image-20261118)

A program that writes one image summing up the world's news of
Wednesday 18 November 2026, for the make.fun bounty
“Sum up 18 November's world news in one image”
(https://make.fun/bounty/news-image-20261118).

## The image

A one-page newspaper infographic in **portrait format, 768×1024**
(the gate allows at most 1024 px on each side, so portrait means
narrower, not taller than 1024). The header banner (red date box,
navy masthead, “40 STORIES” box) and region chips from the earlier
version are kept. Below them: a full-width lead story with its
image on the left, two medium cards, and nine mini cards — **12
main stories in total** — then a coloured world map, then “the
rest of the day” as a two-column list. A red DATE CHECK box and a
sources footer close the page.

The “THE DAY IN NUMBERS” strip was dropped in this version to make
room for the six extra main stories and the map; it can come back
in place of the DATE CHECK box if the entrant prefers.

Background colour: a stronger warm cream gradient (lighter at the
top, deeper gold at the bottom), a pale cream panel behind the
list, and a pale rose DATE CHECK box. All text stays dark on pale
ground, so it reads at about 300 px across — and at 300 px wide,
portrait text renders slightly larger than on the square page.

40 stories in total, numbered continuously 1–40. The 12 main
stories are:

1. Iran drones hit Bahrain (lead)
2. Xi meets Putin at APEC in Shenzhen
3. Kerch Bridge span falls
4. Nvidia doubles to $115.8B
5. 141 drones fired on Ukraine, 126 downed
6. Peltola wins Alaska Senate
7. Trump in Manila, trade push
8. Cyclone Akvan nears Andhra
9. India inflation 12.29%, 4-year high
10. Gaza winter, cold in the tents
11. Deutsche Bank, 15M docs leaked
12. Ebola in DRC, 3 in 4 children die

Stories 13–40 are the rest of the 40 verified summaries, grouped
by region and **coloured by continent**: ASIA red (QUAD, Putin,
the Philippines, Lee, Canada–China, India–Japan, Modi, ASEAN,
Dhoni), MIDEAST ochre (Qeshm, the Hormuz tankers, Saudi Arabia,
the Houthis, Iran's nuclear refusal, the Knesset), EUROPE blue
(Kyiv's bridges, Ukraine's fighters and refineries, peace talks,
UK sanctions), AMERICAS green (US chip curbs, Waymo, GPT-6.2,
measles), GLOBAL navy (the cyber attack, the NSA outages),
OCEANIA teal (Australia). The number and place name of each item
carry its continent's colour; the headline stays dark ink so it
reads. A legend sits in the empty ocean on the map.

The region chips add up to 40 exactly: ASIA 13, MIDEAST 9,
EUROPE 8, AMERICAS 6, GLOBAL 2, AFRICA 1, OCEANIA 1.

## The map

A stylised world map on a pale-blue ocean, one colour per
continent (Americas green, Europe blue, Africa ochre, Asia red,
Oceania purple). Numbered dark dots mark the 12 main stories at
their locations; ringed badges mark how many stories each region
has (Asia 13, Mideast 9, Europe 8, Americas 6, Africa 1,
Oceania 1). The two GLOBAL stories have no single location, so
they are not on the map. The map is simplified and the dot
positions are approximate, as the caption says.

## What was NOT taken from the Gemini draft

The draft supplied the layout and the mixed-case font, but much
of its content was not verified: it put the QUAD in Canberra
(it met in Manila), said an ADNOC facility was hit (it was a
vessel), said Ukraine had received fighter jets (it is still
seeking them), invented UK “shadow fleet” sanctions, a Canberra
minerals bill, a Geneva winter ceasefire, and a cyber attack on
“EU agencies” (it hit Apple, Zoom, BBC and others), and its
DATE CHECK box claimed a verification that had not happened.
All of that was replaced with the 40 verified stories, in
English. Earlier versions are kept as backups
(`main-portrait-v1.py`, `main-square-gemini.py`,
`main-infographic-backup.py` in the working folder).

## The six photographic illustrations

The six photo-style illustrations (Gulf, summit, Kerch, Nvidia,
drones, Peltola) are the entrant's own artwork, split from the
single image she made (`art/*.png`). The other main-story
illustrations are simple vector drawings made by this program.
The program decodes the PNGs with the standard library only
(see `read_png_rgb` in `main.py`); small square thumbnails are
centre-cropped to their aspect (`paste_cover`) instead of
stretched. The entrant allowed the illustrations to be changed;
the vectors were kept and the photos are hers.

One flaw inside the artwork remains: the chip in the Nvidia
panel reads IDIA. The headline above it says NVIDIA, so the
story is clear.

Rules followed (kit RULES.txt): the program writes one image to
`/output/entry.png`, 768×1024 PNG, 174,212 bytes (under the
1 MiB limit), deterministic, standard library only; the date
“18 November 2026” is in the image; at least 8 stories, all from
18 November 2026, none invented. No photographs or logos are used.

One honest trade-off: with 40 stories on one page the list is
one-line headlines; the detail lives in the 12 main stories.

## Run it

Python 3.13, standard library only. Deterministic: no network,
no clock, no randomness. Two runs write byte-identical files.
The `art/` folder must sit next to `main.py`.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

In the grader it writes `/output/entry.png` (768×1024 PNG,
174,212 bytes, under the 1 MiB limit) in well under a second.

## Submit

1. Create a public GitHub repository **after** 18 Nov 2026 00:00 UTC,
   under an OSI-approved license (MIT is included here), with this
   `main.py` at the root **and the `art/` folder next to it**.
   Do not copy the starter kit files in.
2. In `.makefun/owner.json`, check the `wallet` value is the Solana
   wallet you sign in with on make.fun. It is currently set to the
   agent wallet `EVXmTu6mzipy6LQYhJrr3K7YePkngfuNNHdziSEbst9r` that
   signs this entry — a win can be rerouted to another wallet at
   claim time with `claim --pay-to`.
3. Download the kit from the bounty page and follow its Enter steps:
   sign in with Solana/GitHub, bundle the AI transcripts that built
   this entry (the build session and its research subagent), run
   `node cli/makefun.mjs check`, then submit before
   **Fri 20 Nov 2026, 07:00 WIB (00:00 UTC)**.
4. If it places in the top 50, claim the USDC prize from escrow to
   the wallet that signed the entry.

## Sources

Stories are as reported on 18 November 2026 by Reuters, AP, BBC,
Al Jazeera, and the other wires summarised in the day's news briefs.
No story was invented.
