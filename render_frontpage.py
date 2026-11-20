#!/usr/bin/env python3
"""Draw the news-image-20261120 front page: one 1024x1024 newspaper page
summing up Friday 20 November 2026. Pillow only, no network, no randomness:
running this script twice writes byte-identical PNGs.

Stories, verified by web search on 20 Nov 2026 (IMD cyclone advisories,
Jagran Josh, Devdiscourse, Reuters, Drop Site News, Times of India /
Education Times, The Diary of AI, Basis Desk, WARNPOINT):
- LEAD, 20 Nov: Severe Cyclonic Storm Akvan makes landfall on India's east
  coast near Gopalpur, Odisha, around noon, with sustained winds of
  90-100 kmph gusting to 110; schools shut in six Odisha districts and
  evacuations under way along the Andhra Pradesh-Odisha coast.
- RIYADH: a Houthi missile threat over the Saudi capital on 19 Nov; debris
  falls and the 80-storey PIF tower in the financial district is damaged.
  The IEA says the Iran war has caused the largest disruption to global oil
  and gas trade on record (2.8bn barrels of oil, 60 bcm of gas).
- NEW YORK: Anthropic debuts on Nasdaq — priced at $83, opens at $111.50
  and closes at $97.17 in the largest IPO on record (about $81bn raised).
  Google's Gemini 4 Neon tops the benchmark table ahead of Claude Opus 5.5.
- THE HAGUE: the International Court of Justice rules Myanmar committed
  genocide against the Rohingya.
- SHENZHEN: after the first Trump-Xi-Putin three-way meeting at APEC, the
  summit turns to nuclear risks and energy security.
- ALSO TODAY: South Korea's Supreme Court overturns ex-PM Han Duck-soo's
  conviction; PM Modi meets the Prince and Princess of Wales in Delhi;
  Russian strikes damage the Austrian and Dutch embassies in Kyiv; Fiji
  declares a national disaster over drought; the US and Venezuela agree to
  restore military cooperation; Henry Nicholls hits 113 not out as New
  Zealand reach 243/5 against India; Nvidia's board rules out a return for
  ousted chief Jensen Huang; the GTA VI rollout continues.
"""
import math

from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
CRIMSON = (163, 24, 44)
NAVY = (24, 68, 112)
SEA = (52, 110, 158)
LAND = (216, 195, 140)
MUTED = (88, 88, 88)
FAINT = (232, 226, 207)

FONT_DIR = "/usr/share/fonts/truetype/liberation/"


def load(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def serif_b(size):
    return load("LiberationSerif-Bold.ttf", size)


def serif(size):
    return load("LiberationSerif-Regular.ttf", size)


def serif_i(size):
    return load("LiberationSerif-Italic.ttf", size)


def sans_b(size):
    return load("LiberationSans-Bold.ttf", size)


def sans(size):
    return load("LiberationSans-Regular.ttf", size)


page = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
pen = ImageDraw.Draw(page)

LEFT = 36
RIGHT = CANVAS_W - LEFT
SPAN = RIGHT - LEFT


def split_lines(text, face, width):
    out, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if pen.textlength(trial, font=face) <= width:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def block(text, face, x, y, width, gap, colour=INK):
    for line in split_lines(text, face, width):
        pen.text((x, y), line, font=face, fill=colour)
        y += gap
    return y


def hline(x0, y, x1, thick=2, colour=INK):
    pen.line([(x0, y), (x1, y)], fill=colour, width=thick)


def cyclone(cx, cy, rmax):
    """Spiral storm: nested arcs that tighten toward the eye."""
    for k in range(5):
        r = rmax - k * 7
        start = k * 55
        pen.arc([cx - r, cy - r, cx + r, cy + r], start, start + 300,
                fill=(255, 255, 255), width=4)
    pen.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 235, 120))


# ---------------- masthead ----------------
pen.text((CANVAS_W // 2, 16), "THE WORLD", font=serif_b(82),
         fill=INK, anchor="ma")
pen.text((CANVAS_W // 2, 102), "The day's news in one page",
         font=serif_i(19), fill=MUTED, anchor="ma")
hline(LEFT, 132, RIGHT, 3)
hline(LEFT, 137, RIGHT, 1)
pen.text((LEFT, 144), "FRIDAY, 20 NOVEMBER 2026", font=sans_b(18), fill=CRIMSON)
pen.text((RIGHT, 144), "WORLD NEWS  •  ONE IMAGE", font=sans_b(18),
         fill=INK, anchor="ra")
hline(LEFT, 170, RIGHT, 1)

# ---------------- lead: Cyclone Akvan ----------------
y = 182
pen.text((LEFT, y), "INDIA  —  THE STORM MAKES LANDFALL", font=sans_b(19),
         fill=CRIMSON)
y = 206
y = block("Cyclone Akvan slams into India's east coast near Gopalpur",
          serif_b(43), LEFT, y, SPAN, 49)
y += 2
y = block("Winds of 110 kmph lash Odisha and Andhra Pradesh as the severe "
          "storm comes ashore at noon; schools shut and thousands move to "
          "shelters.", serif_i(20), LEFT, y, SPAN, 26, colour=(62, 62, 62))
y += 8

map_x, map_y, map_w, map_h = LEFT, y, SPAN, 118
pen.rectangle([map_x, map_y, map_x + map_w, map_y + map_h], fill=SEA)
# India's east coast: land mass on the left, sea on the right.
pen.polygon([(map_x, map_y), (map_x + 470, map_y),
             (map_x + 430, map_y + 34), (map_x + 330, map_y + 30),
             (map_x + 300, map_y + 62), (map_x + 210, map_y + 66),
             (map_x + 120, map_y + 88), (map_x, map_y + 118)],
            fill=LAND)
# Southern tip of the coast, a thin strip along the bottom edge only.
pen.polygon([(map_x + 560, map_y + map_h), (map_x + map_w, map_y + map_h),
             (map_x + map_w, map_y + map_h - 14),
             (map_x + 560, map_y + map_h - 14)], fill=LAND)
pen.text((map_x + 16, map_y + 8), "INDIA", font=sans_b(17), fill=(96, 66, 22))
pen.text((map_x + 14, map_y + 52), "ODISHA", font=sans_b(15),
         fill=(96, 66, 22))
pen.text((map_x + 620, map_y + 8), "BAY OF BENGAL", font=sans_b(15),
         fill=(255, 255, 255))
# The storm sits offshore, its track arrow pointing at Gopalpur.
storm_x, storm_y = map_x + 640, map_y + 58
cyclone(storm_x, storm_y, 34)
for i in range(9):
    t = i / 8
    ax = storm_x - 180 * t
    ay = storm_y + 26 * t - 30 * 4 * t * (1 - t)
    pen.ellipse([ax - 2, ay - 2, ax + 2, ay + 2], fill=(255, 90, 60))
gx, gy = map_x + 452, map_y + 84
pen.ellipse([gx - 5, gy - 5, gx + 5, gy + 5], fill=(255, 255, 255))
pen.text((gx + 10, gy - 9), "GOPALPUR", font=sans_b(14), fill=(255, 255, 255))
pen.text((map_x + map_w - 14, map_y + map_h - 24),
         "LANDFALL ~NOON  •  90–100 KMPH, GUSTS 110",
         font=sans_b(13), fill=(255, 255, 255), anchor="ra")
y = map_y + map_h + 8
y = block("The India Meteorological Department warned of heavy rain and "
          "dangerous seas; six Odisha districts closed schools until 21 "
          "November as the storm weakened inland after landfall.",
          serif(18), LEFT, y, SPAN, 24)
y += 4
hline(LEFT, y, RIGHT, 1)
y += 8

# ---------------- row two: two columns ----------------
HALF = 464
top2 = y


def skyline(x0, y0, w, h):
    """Riyadh at dusk: dark sky, lit towers, one tall tower struck."""
    pen.rectangle([x0, y0, x0 + w, y0 + h], fill=(22, 30, 48))
    heights = [34, 52, 28, 66, 40, 58, 30]
    bx = x0 + 10
    for hh in heights:
        pen.rectangle([bx, y0 + h - hh, bx + 34, y0 + h], fill=(58, 66, 88))
        bx += 44
    # PIF tower: the tallest, centre-right, with a burst at its crown.
    tx = x0 + w - 108
    pen.rectangle([tx, y0 + 6, tx + 42, y0 + h], fill=(120, 128, 150))
    for wy in range(y0 + 14, y0 + h - 6, 12):
        pen.rectangle([tx + 6, wy, tx + 36, wy + 5], fill=(255, 214, 90))
    cx, cy = tx + 21, y0 + 4
    for (dx, dy, rr, c) in [(0, 0, 12, (255, 140, 0)), (-10, 5, 7, (255, 190, 0)),
                            (10, 5, 7, (255, 190, 0)), (0, -9, 7, (255, 210, 60))]:
        pen.ellipse([cx + dx - rr, cy + dy - rr, cx + dx + rr, cy + dy + rr],
                    fill=c)
    # Incoming missile arc with dotted trail.
    for i in range(11):
        t = i / 10
        mx = x0 + 30 + (tx - x0 - 30) * t
        my = y0 + h - 18 - 46 * math.sin(math.pi * t)
        pen.ellipse([mx - 2, my - 2, mx + 2, my + 2], fill=(255, 90, 60))


def chart(x0, y0, w, h):
    """Nasdaq debut: bars climbing to the open, then easing to the close."""
    pen.rectangle([x0, y0, x0 + w, y0 + h], fill=FAINT)
    # Header strip keeps the price line clear of the bars below it.
    bars = [12, 17, 23, 20, 29, 35, 41, 37]
    bw = (w - 40) // len(bars)
    for i, bh in enumerate(bars):
        bx = x0 + 20 + i * bw
        colour = NAVY if i < len(bars) - 1 else CRIMSON
        pen.rectangle([bx, y0 + h - bh - 8, bx + bw - 6, y0 + h - 8],
                      fill=colour)
    pen.text((x0 + 12, y0 + 4), "ANT  •  NASDAQ", font=sans_b(13), fill=INK)
    pen.text((x0 + w - 12, y0 + 4), "$83 → $111.50 → $97.17",
             font=sans_b(13), fill=INK, anchor="ra")


x = LEFT
pen.text((x, top2), "RIYADH  —  MISSILE OVER THE CAPITAL", font=sans_b(15),
         fill=CRIMSON)
yy = block("Houthi missile damages the PIF tower as the Gulf war widens",
           serif_b(28), x, top2 + 22, HALF, 32)
yy += 4
skyline(x, yy, HALF, 74)
yy += 74 + 6
end_left = block("Debris falls on Riyadh's financial district after air "
                 "defences meet the missile; the IEA calls the Iran war the "
                 "largest oil and gas disruption on record.",
                 serif(17), x, yy, HALF, 22)

x = RIGHT - HALF
pen.text((x, top2), "NEW YORK  —  THE $1.5 TRILLION DEBUT", font=sans_b(15),
         fill=CRIMSON)
yy = block("Anthropic opens at $111.50 in the biggest IPO on record",
           serif_b(28), x, top2 + 22, HALF, 32)
yy += 4
chart(x, yy, HALF, 74)
yy += 74 + 6
end_right = block("Priced at $83, the Claude maker closes at $97.17 after "
                  "raising about $81bn; Google's Gemini 4 Neon tops the "
                  "benchmark table.", serif(17), x, yy, HALF, 22)
y = max(end_left, end_right) + 6
hline(LEFT, y, RIGHT, 1)
y += 8

# ---------------- row three: two short items ----------------
def scales(cx, cy):
    pen.line([(cx - 13, cy - 10), (cx + 13, cy - 10)], fill=(90, 90, 100),
             width=3)
    pen.line([(cx, cy - 10), (cx, cy + 12)], fill=(90, 90, 100), width=3)
    pen.line([(cx - 13, cy - 10), (cx - 17, cy + 4)], fill=(90, 90, 100),
             width=2)
    pen.line([(cx + 13, cy - 10), (cx + 17, cy + 4)], fill=(90, 90, 100),
             width=2)
    pen.ellipse([cx - 21, cy + 2, cx - 13, cy + 10], fill=(90, 90, 100))
    pen.ellipse([cx + 13, cy + 2, cx + 21, cy + 10], fill=(90, 90, 100))
    pen.rectangle([cx - 9, cy + 12, cx + 9, cy + 15], fill=(90, 90, 100))


def summit(cx, cy):
    for (ox, c) in [(-14, (222, 41, 16)), (0, (0, 57, 166)),
                    (14, (178, 34, 52))]:
        pen.rectangle([cx + ox - 8, cy - 12, cx + ox + 8, cy + 12], fill=c)
        pen.text((cx + ox - 4, cy - 9), "*", font=sans_b(12),
                 fill=(255, 255, 255))


def short_item(x, kicker, head, body, draw_icon):
    pen.text((x + 44, y), kicker, font=sans_b(13), fill=CRIMSON)
    yy = block(head, sans_b(19), x + 44, y + 16, HALF - 44, 23)
    draw_icon(x + 20, y + 26)
    return block(body, serif(16), x + 44, yy + 2, HALF - 44, 21)


y2 = short_item(LEFT, "THE HAGUE", "ICJ: Myanmar committed genocide",
                "The world court rules against Myanmar over the 2017 "
                "crackdown on the Rohingya, in a case watched by refugees "
                "in Bangladesh.", scales)
y3 = short_item(RIGHT - HALF, "SHENZHEN", "After the three-way summit",
                "Trump, Xi and Putin's first trilateral meeting turns the "
                "APEC summit to nuclear risks, energy and the wars in "
                "Ukraine and the Gulf.", summit)
y = max(y2, y3) + 6
hline(LEFT, y, RIGHT, 1)
y += 6

# ---------------- also today ----------------
pen.text((LEFT, y), "ALSO TODAY", font=sans_b(15), fill=CRIMSON)
y = block("South Korea's top court overturns ex-PM Han Duck-soo's conviction"
          "  ·  Modi meets the Prince and Princess of Wales in Delhi  ·  "
          "Russian strikes damage the Austrian and Dutch embassies in Kyiv"
          "  ·  Fiji declares a national disaster over drought  ·  US and "
          "Venezuela agree to restore military cooperation  ·  Nicholls 113*"
          " as New Zealand reach 243/5 against India  ·  Nvidia's board "
          "rules out a return for ousted chief Jensen Huang  ·  The GTA VI "
          "rollout continues",
          sans(15), LEFT + 118, y, RIGHT - LEFT - 118, 20, colour=(62, 62, 62))
y += 4
hline(LEFT, y, RIGHT, 1)
pen.text((CANVAS_W // 2, y + 5), "Compiled from the day's reporting  •  20 November 2026",
         font=sans(13), fill=MUTED, anchor="ma")

page.save("entry.png")
print("saved; final y =", y)
