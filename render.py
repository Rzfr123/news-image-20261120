#!/usr/bin/env python3
"""Render the news-image-20261120 entry: a newspaper front page summing up
Friday 20 November 2026. Output: entry.png (1024x1024, deterministic).
Drawn programmatically with Pillow; no AI image generation, so every
headline is exact text."""
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 229)
INK = (26, 26, 26)
RED = (176, 42, 32)
BLUE = (31, 58, 95)
GREY = (96, 96, 96)
SAND = (214, 196, 150)
SEA = (140, 180, 205)
SKY = (232, 236, 240)
ORANGE = (230, 120, 20)
GREEN = (60, 110, 50)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, xy, s, f, fill=INK):
    d.text(xy, s, font=f, fill=fill)


def text_c(d, cx, y, s, f, fill=INK):
    w = d.textlength(s, font=f)
    d.text((cx - w / 2, y), s, font=f, fill=fill)


def wrap(d, s, f, max_w):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, s, f, max_w, fill=INK, leading=6):
    lines = wrap(d, s, f, max_w)
    lh = f.size + leading
    for i, line in enumerate(lines):
        d.text((x, y + i * lh), line, font=f, fill=fill)
    return y + len(lines) * lh


def starburst(d, cx, cy, r, fill):
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def flag_us(d, x, y, w, h):
    stripe = h / 13
    for i in range(13):
        d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe],
                    fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + w * 0.4, y + stripe * 7], fill=(30, 50, 110))
    for r in range(4):
        for c in range(5):
            d.ellipse([x + 4 + c * 7, y + 3 + r * 6, x + 7 + c * 7,
                       y + 6 + r * 6], fill=(255, 255, 255))


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    starburst(d, x + w * 0.28, y + h * 0.3, 9, (255, 222, 0))


def flag_ru(d, x, y, w, h):
    for i, col in enumerate([(255, 255, 255), (0, 60, 160), (210, 30, 30)]):
        d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)


def flag_ve(d, x, y, w, h):
    for i, col in enumerate([(252, 209, 22), (0, 56, 147), (207, 20, 43)]):
        d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)
    for sx in (w * 0.3, w * 0.5, w * 0.7):
        d.ellipse([x + sx - 2, y + h * 0.42, x + sx + 2, y + h * 0.42 + 4],
                  fill=(255, 255, 255))


def draw_lead_art(d):
    # Shenzhen skyline + three flags + a bridge under attack.
    # Art area: x 650..990, y 235..470.
    base = 440
    towers = [(655, 360, 34), (692, 330, 30), (725, 375, 36),
              (800, 345, 32), (835, 315, 30), (868, 370, 34),
              (905, 335, 30), (938, 360, 32), (972, 385, 18)]
    for bx, top, bw in towers:
        d.rectangle([bx, top, bx + bw, base], fill=BLUE)
    # tallest tower with spire
    d.rectangle([764, 282, 798, base], fill=BLUE)
    d.polygon([(772, 282), (790, 282), (781, 250)], fill=BLUE)
    d.ellipse([777, 240, 785, 248], fill=RED)
    d.line([(650, base), (990, base)], fill=INK, width=3)
    # three flag poles with flags
    for fn, fx in ((flag_us, 670), (flag_cn, 800), (flag_ru, 910)):
        d.line([(fx, 238), (fx, 322)], fill=INK, width=3)
        fn(d, fx + 3, 240, 66, 40)
    # bridge deck below the skyline, broken in the middle
    d.line([(660, 452), (812, 452)], fill=INK, width=6)
    d.line([(838, 452), (985, 452)], fill=INK, width=6)
    d.line([(814, 458), (836, 466)], fill=INK, width=5)
    starburst(d, 825, 452, 13, ORANGE)
    starburst(d, 825, 452, 7, RED)
    d.line([(660, 464), (985, 464)], fill=SEA, width=2)


def draw_bridge(d, x, y, w, h):
    # Kyiv bridge hit overnight: deck with a broken gap, blast, smoke.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    water_y = y + 122
    d.rectangle([x, water_y, x + w, y + h], fill=SEA)
    d.rectangle([x + 22, y + 28, x + 30, water_y], fill=INK)
    d.rectangle([x + 118, y + 28, x + 126, water_y], fill=INK)
    d.line([(x, y + 52), (x + 60, y + 52)], fill=INK, width=7)
    d.line([(x + 92, y + 52), (x + w, y + 52)], fill=INK, width=7)
    d.line([(x + 62, y + 60), (x + 90, y + 108)], fill=INK, width=6)
    d.line([(x + 26, y + 30), (x + 60, y + 52)], fill=GREY, width=2)
    d.line([(x + 26, y + 30), (x + 4, y + 52)], fill=GREY, width=2)
    d.line([(x + 122, y + 30), (x + 92, y + 52)], fill=GREY, width=2)
    d.line([(x + 122, y + 30), (x + 148, y + 52)], fill=GREY, width=2)
    starburst(d, x + 76, y + 52, 22, ORANGE)
    starburst(d, x + 76, y + 52, 12, RED)
    d.ellipse([x + 52, y + 4, x + 82, y + 28], fill=(150, 150, 150))
    d.ellipse([x + 72, y - 2, x + 102, y + 20], fill=(180, 180, 180))


def draw_scales(d, x, y, w, h):
    # The scales of justice: the ICJ's genocide verdict.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    cx = x + w / 2
    base_y = y + h - 20
    d.rectangle([x + 18, base_y, x + w - 18, base_y + 8], fill=BLUE)
    d.rectangle([cx - 4, y + 22, cx + 4, base_y], fill=BLUE)
    d.ellipse([cx - 7, y + 12, cx + 7, y + 26], fill=BLUE)
    d.line([(cx - 58, y + 34), (cx + 58, y + 34)], fill=BLUE, width=5)
    for px in (cx - 58, cx + 58):
        d.line([(px, y + 34), (px - 24, y + 78)], fill=INK, width=2)
        d.line([(px, y + 34), (px + 24, y + 78)], fill=INK, width=2)
        d.line([(px, y + 34), (px, y + 78)], fill=INK, width=2)
        d.pieslice([px - 26, y + 76, px + 26, y + 104], 0, 180, fill=BLUE)
    d.rectangle([cx - 26, base_y - 14, cx + 26, base_y], fill=BLUE)


def draw_chart(d, x, y, w, h):
    # A market debut that jumps: rising bars and a climbing arrow.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    f = font(SANS_B, 26)
    text_w(d, (x + 8, y + 8), "+34%", f, fill=RED)
    base_y = y + h - 26
    d.line([(x + 12, y + 34), (x + 12, base_y)], fill=INK, width=2)
    d.line([(x + 12, base_y), (x + w - 8, base_y)], fill=INK, width=2)
    bars = [(26, 42), (52, 62), (78, 84), (104, 112)]
    for bx, bh in bars:
        d.rectangle([x + bx, base_y - bh, x + bx + 18, base_y], fill=BLUE)
    d.line([(x + 24, base_y - 34), (x + 128, y + 44)], fill=RED, width=4)
    d.polygon([(x + 128, y + 44), (x + 112, y + 44), (x + 128, y + 60)],
              fill=RED)


def draw_flags_deal(d, x, y, w, h):
    # Two flags and an olive branch: the US–Venezuela military deal.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    flag_us(d, x + 8, y + 18, 62, 38)
    flag_ve(d, x + 88, y + 18, 62, 38)
    d.line([(x + 14, y + h - 34), (x + w - 14, y + h - 62)], fill=GREEN,
           width=4)
    for lx, ly in [(x + 38, y + h - 44), (x + 68, y + h - 52),
                   (x + 98, y + h - 60)]:
        d.ellipse([lx, ly, lx + 22, ly + 10], fill=GREEN)


def panel(d, x, y, w, h, kicker, headline, caption, art):
    art(d, x + 8, y + 8, 158, h - 16)
    tx = x + 178
    f_k = font(SANS_B, 20)
    f_h = font(SANS_B, 27)
    f_c = font(SANS, 22)
    text_w(d, (tx, y + 10), kicker, f_k, fill=RED)
    hl = wrap(d, headline, f_h, w - 186)
    hy = y + 36
    for i, line in enumerate(hl):
        d.text((tx, hy + i * 32), line, font=f_h, fill=INK)
    cy = hy + len(hl) * 32 + 4
    para(d, tx, cy, caption, f_c, w - 186, leading=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # frames
    d.rectangle([10, 10, 1014, 1014], outline=INK, width=5)
    d.rectangle([20, 20, 1004, 1004], outline=INK, width=2)

    # ---- masthead ----
    f_small = font(SANS_B, 24)
    text_w(d, (38, 36), "FRIDAY", f_small)
    wr = d.textlength("WORLD NEWS", font=f_small)
    text_w(d, (986 - wr, 36), "WORLD NEWS", f_small)
    f_mast = font(SERIF_B, 92)
    text_c(d, 512, 66, "20 NOVEMBER 2026", f_mast)
    f_sub = font(SANS_B, 25)
    text_c(d, 512, 168, "THE WORLD'S NEWS IN ONE IMAGE", f_sub, fill=GREY)
    d.line([(36, 208), (988, 208)], fill=INK, width=4)
    d.line([(36, 216), (988, 216)], fill=INK, width=2)

    # ---- lead story: Shenzhen summit, then missiles over Kyiv ----
    f_k = font(SANS_B, 22)
    f_h = font(SANS_B, 34)
    f_c = font(SANS, 25)
    text_w(d, (36, 236), "SHENZHEN  ·  DIPLOMACY", f_k, fill=RED)
    text_w(d, (36, 264), "PEACE TALK IN SHENZHEN,", f_h)
    text_w(d, (36, 300), "THEN MISSILES OVER KYIV", f_h)
    para(d, 36, 344, "Trump, Xi and Putin hold the first three-way talks "
       "and declare peace — hours later Russia fires 100+ missiles and "
       "400 drones at Ukraine: 8 killed, 28 injured, three Kyiv bridges "
       "hit.", f_c, 600, leading=5)
    draw_lead_art(d)
    d.line([(36, 478), (988, 478)], fill=INK, width=3)

    # ---- 2x2 grid ----
    gx, gy = 36, 494
    cw, ch = 466, 200
    panel(d, gx, gy, cw, ch, "KYIV · WAR", "RUSSIA'S NIGHT BARRAGE",
          "Bridges hit, power cut as cold bites; Poland scrambles jets.",
          draw_bridge)
    panel(d, gx + cw + 20, gy, cw, ch, "THE HAGUE · JUSTICE",
          "MYANMAR GUILTY OF GENOCIDE",
          "The UN's top court rules 9–6: Myanmar bears state "
          "responsibility.", draw_scales)
    d.line([(36, gy + ch + 6), (988, gy + ch + 6)], fill=GREY, width=1)
    panel(d, gx, gy + ch + 12, cw, ch, "WALL STREET · MARKETS",
          "ANTHROPIC UP 34% ON DEBUT",
          "The first purely AI company to list publicly jumps on debut.",
          draw_chart)
    panel(d, gx + cw + 20, gy + ch + 12, cw, ch, "CARACAS · DIPLOMACY",
          "US–VENEZUELA MILITARY DEAL",
          "Ties restored months after the US captured Venezuela's "
          "president.", draw_flags_deal)
    d.line([(36, 916), (988, 916)], fill=INK, width=3)

    # ---- footer briefs ticker ----
    f_b = font(SANS_B, 18)
    f_bt = font(SANS, 16)
    briefs = [
        ("UKRAINE AID", "UK pledges 1,000+ drones for Ukraine in a £260m package."),
        ("PETE ROSE", "Trump posthumously pardons baseball legend Pete Rose."),
        ("ENERGY TRUCE", "Europe's E3 leaders call for a winter energy ceasefire in Ukraine."),
        ("SENATE", "US Senate rejects the Iran war-powers resolution 51–48."),
    ]
    bx = 36
    bw = 226
    for kicker, txt in briefs:
        text_w(d, (bx, 924), kicker, f_b, fill=RED)
        para(d, bx, 944, txt, f_bt, bw, leading=3)
        bx += bw + 16

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
