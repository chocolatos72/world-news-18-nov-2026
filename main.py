#!/usr/bin/env python3
"""
Sum up 18 November 2026 in one image (Newspaper Infographic Layout).
Python 3.13, standard library only. Deterministic. Writes entry.png.
Layout from Gemini, content: the 40 verified stories of 18 Nov 2026,
portrait 768x1024, 12 main stories, coloured map, region-coloured list.
"""
import math
import os
import struct
import zlib

W = 768
H = 1024
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- font (5x7 bitmap with lowercase)
FONT = {
    'A': ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    'B': ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    'C': ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    'D': ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    'E': ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    'F': ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    'G': ["01110", "10001", "10000", "10111", "10001", "10001", "01111"],
    'H': ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    'I': ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    'J': ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    'K': ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    'L': ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    'M': ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    'N': ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    'O': ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    'P': ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    'Q': ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    'R': ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    'S': ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    'T': ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    'U': ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    'V': ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    'W': ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    'X': ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    'Y': ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    'Z': ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    'a': ["00000", "00000", "01110", "00001", "01111", "10001", "01111"],
    'b': ["10000", "10000", "11110", "10001", "10001", "10001", "11110"],
    'c': ["00000", "00000", "01110", "10000", "10000", "10001", "01110"],
    'd': ["00001", "00001", "01111", "10001", "10001", "10001", "01111"],
    'e': ["00000", "00000", "01110", "10001", "11111", "10000", "01110"],
    'f': ["00110", "01001", "01000", "11100", "01000", "01000", "01000"],
    'g': ["00000", "01111", "10001", "01111", "00001", "10001", "01110"],
    'h': ["10000", "10000", "11110", "10001", "10001", "10001", "10001"],
    'i': ["00100", "00000", "01100", "00100", "00100", "00100", "01110"],
    'j': ["00010", "00000", "00110", "00010", "00010", "10010", "01100"],
    'k': ["10000", "10000", "10010", "10100", "11000", "10100", "10010"],
    'l': ["01100", "00100", "00100", "00100", "00100", "00100", "01110"],
    'm': ["00000", "00000", "11010", "10101", "10101", "10001", "10001"],
    'n': ["00000", "00000", "11110", "10001", "10001", "10001", "10001"],
    'o': ["00000", "00000", "01110", "10001", "10001", "10001", "01110"],
    'p': ["00000", "11110", "10001", "11110", "10000", "10000", "10000"],
    'q': ["00000", "01111", "10001", "01111", "00001", "00001", "00001"],
    'r': ["00000", "00000", "10110", "11001", "10000", "10000", "10000"],
    's': ["00000", "00000", "01111", "10000", "01110", "00001", "11110"],
    't': ["01000", "01000", "11100", "01000", "01000", "01001", "00110"],
    'u': ["00000", "00000", "10001", "10001", "10001", "10011", "01101"],
    'v': ["00000", "00000", "10001", "10001", "10001", "01010", "00100"],
    'w': ["00000", "00000", "10001", "10001", "10101", "10101", "01010"],
    'x': ["00000", "00000", "10001", "01010", "00100", "01010", "10001"],
    'y': ["00000", "10001", "10001", "01111", "00001", "10001", "01110"],
    'z': ["00000", "00000", "11111", "00010", "00100", "01000", "11111"],
    '0': ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    '1': ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    '2': ["01110", "10001", "00001", "00110", "01000", "10000", "11111"],
    '3': ["11111", "00010", "00100", "00010", "00001", "10001", "01110"],
    '4': ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    '5': ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    '6': ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    '7': ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    '8': ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    '9': ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    ' ': ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    '.': ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ',': ["00000", "00000", "00000", "00000", "01100", "00100", "01000"],
    ':': ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    '-': ["00000", "00000", "00000", "01110", "00000", "00000", "00000"],
    '—': ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "'": ["00100", "00100", "01000", "00000", "00000", "00000", "00000"],
    '/': ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    '%': ["11001", "11010", "00010", "00100", "01000", "01011", "10011"],
    '$': ["00100", "01111", "10100", "01110", "00101", "11110", "00100"],
    '(': ["00010", "00100", "01000", "01000", "01000", "00100", "00010"],
    ')': ["01000", "00100", "00010", "00010", "00010", "00100", "01000"],
    '!': ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    '?': ["01110", "10001", "00001", "00110", "00100", "00000", "00100"],
    '+': ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    '=': ["00000", "00000", "11111", "00000", "11111", "00000", "00000"],
    ';': ["00000", "01100", "01100", "00000", "01100", "00100", "01000"],
    '•': ["00000", "01100", "01100", "01100", "00000", "00000", "00000"],
    '·': ["00000", "00000", "00100", "00000", "00000", "00000", "00000"],
}

def text_width(s, scale):
    return len(s) * 6 * scale - scale if s else 0

# ---------------------------------------------------------------- canvas
class Canvas:
    def __init__(self):
        self.px = bytearray(W * H * 3)

    def set(self, x, y, c):
        if 0 <= x < W and 0 <= y < H:
            i = (y * W + x) * 3
            self.px[i], self.px[i + 1], self.px[i + 2] = c

    def rect(self, x, y, w, h, c):
        x0, y0 = max(0, x), max(0, y)
        x1, y1 = min(W, x + w), min(H, y + h)
        for yy in range(y0, y1):
            base = (yy * W + x0) * 3
            for xx in range(x0, x1):
                i = base + (xx - x0) * 3
                self.px[i], self.px[i + 1], self.px[i + 2] = c

    def hline(self, x0, x1, y, c, thick=1):
        for yy in range(y, y + thick):
            for xx in range(max(0, x0), min(W, x1)):
                self.set(xx, yy, c)

    def vline(self, x, y0, y1, c, thick=1):
        for xx in range(x, x + thick):
            for yy in range(max(0, y0), min(H, y1)):
                self.set(xx, yy, c)

    def line(self, x0, y0, x1, y1, c, thick=1):
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        x, y = x0, y0
        while True:
            for a in range(thick):
                for b in range(thick):
                    self.set(x + a, y + b, c)
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    def circle(self, cx, cy, r, c):
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                if (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r:
                    self.set(xx, yy, c)

    def disc_outline(self, cx, cy, r, c, thick=3):
        for yy in range(cy - r - thick, cy + r + thick + 1):
            for xx in range(cx - r - thick, cx + r + thick + 1):
                d = math.hypot(xx - cx, yy - cy)
                if r - thick <= d <= r:
                    self.set(xx, yy, c)

    def poly(self, pts, c):
        ys = [p[1] for p in pts]
        for y in range(max(0, min(ys)), min(H, max(ys) + 1)):
            xs = []
            n = len(pts)
            for i in range(n):
                x0, y0 = pts[i]
                x1, y1 = pts[(i + 1) % n]
                if (y0 <= y < y1) or (y1 <= y < y0):
                    xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
            xs.sort()
            for k in range(0, len(xs) - 1, 2):
                for x in range(int(xs[k]), int(xs[k + 1]) + 1):
                    self.set(x, y, c)

    def text(self, x, y, s, scale, colour):
        cx = x
        for ch in s:
            g = FONT.get(ch, FONT.get(ch.upper(), FONT[' ']))
            for r in range(7):
                row = g[r]
                for col in range(5):
                    if row[col] == '1':
                        self.rect(cx + col * scale, y + r * scale, scale, scale, colour)
            cx += 6 * scale

    def text_wrap(self, x, y, max_w, s, scale, colour, line_h=None):
        if line_h is None:
            line_h = 8 * scale + 2
        words = s.split(' ')
        line = ""
        cy = y
        for w in words:
            test = (line + " " + w).strip()
            if text_width(test, scale) <= max_w:
                line = test
            else:
                if line:
                    self.text(x, cy, line, scale, colour)
                    cy += line_h
                line = w
        if line:
            self.text(x, cy, line, scale, colour)
            cy += line_h
        return cy

    def text_centre(self, cx, y, s, scale, colour):
        self.text(cx - text_width(s, scale) // 2, y, s, scale, colour)

    def border(self, x, y, w, h, c, thick=1):
        self.rect(x, y, w, thick, c)
        self.rect(x, y + h - thick, w, thick, c)
        self.rect(x, y, thick, h, c)
        self.rect(x + w - thick, y, thick, h, c)


# Palette matched to newspaper reference
WHITE = (255, 255, 255)
CARD_BG = (252, 251, 247)
PAPER = (244, 240, 232)
NAVY = (24, 38, 62)
INK = (28, 34, 42)
MUTED = (105, 110, 118)
RULE = (205, 200, 190)
RED = (168, 42, 42)
TEAL = (24, 118, 114)
GOLD = (212, 162, 56)
BLUE = (38, 84, 148)
PURPLE = (96, 56, 124)
GREEN = (36, 102, 68)
OCHRE = (182, 122, 42)

# ------------------------------------------------------- PNG reading & scaling
def read_png_rgb(path):
    with open(path, "rb") as f:
        data = f.read()
    pos = 8
    idat = b""
    w = h = None
    bitdepth = ctype = interlace = None
    while pos < len(data):
        ln = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + ln]
        if kind == b"IHDR":
            w, h, bitdepth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", chunk)
        elif kind == b"IDAT":
            idat += chunk
        elif kind == b"IEND":
            break
        pos += 12 + ln
    bpp = 3 if ctype == 2 else 4
    raw = zlib.decompress(idat)
    stride = w * bpp
    rows = []
    prev = bytearray(stride)
    p = 0
    for _ in range(h):
        ft = raw[p]
        p += 1
        row = bytearray(raw[p:p + stride])
        p += stride
        if ft == 1:
            for i in range(bpp, stride):
                row[i] = (row[i] + row[i - bpp]) & 255
        elif ft == 2:
            for i in range(stride):
                row[i] = (row[i] + prev[i]) & 255
        elif ft == 3:
            for i in range(stride):
                a = row[i - bpp] if i >= bpp else 0
                row[i] = (row[i] + ((a + prev[i]) >> 1)) & 255
        elif ft == 4:
            for i in range(stride):
                a = row[i - bpp] if i >= bpp else 0
                b = prev[i]
                c = prev[i - bpp] if i >= bpp else 0
                pp = a + b - c
                pa, pb, pc = abs(pp - a), abs(pp - b), abs(pp - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                row[i] = (row[i] + pr) & 255
        if bpp == 3:
            rows.append(bytes(row))
        else:
            rows.append(b"".join(row[i:i + 3] for i in range(0, stride, 4)))
        prev = row
    return w, h, rows


def paste_scaled(cv, path, x, y, tw, th):
    if not os.path.exists(path):
        cv.rect(x, y, tw, th, (220, 225, 230))
        return
    sw, sh, rows = read_png_rgb(path)
    for dy in range(th):
        sy = min(sh - 1, int(dy * sh / th))
        srow = rows[sy]
        for dx in range(tw):
            sx = min(sw - 1, int(dx * sw / tw))
            i = sx * 3
            cv.set(x + dx, y + dy, (srow[i], srow[i + 1], srow[i + 2]))

# ------------------------------------------- proportional vector illustrations
def draw_vec(kind, cv, bx, by, bw, bh):
    if kind == "ship":
        cv.rect(bx, by, bw, int(bh * 0.68), (215, 228, 238))
        cv.circle(bx + int(bw * 0.84), by + int(bh * 0.2), 7, GOLD)
        cv.rect(bx, by + int(bh * 0.68), bw, bh - int(bh * 0.68), (70, 130, 180))
        cv.rect(bx + int(bw * 0.25), by + int(bh * 0.35), int(bw * 0.13), int(bh * 0.33), RED)
        cv.rect(bx + int(bw * 0.39), by + int(bh * 0.35), int(bw * 0.13), int(bh * 0.33), TEAL)
        cv.rect(bx + int(bw * 0.53), by + int(bh * 0.44), int(bw * 0.13), int(bh * 0.24), GOLD)
        cv.poly([(bx + int(bw * 0.1), by + int(bh * 0.68)),
                 (bx + int(bw * 0.9), by + int(bh * 0.68)),
                 (bx + int(bw * 0.82), by + int(bh * 0.92)),
                 (bx + int(bw * 0.18), by + int(bh * 0.92))], NAVY)
    elif kind == "cyclone":
        cv.rect(bx, by, bw, bh, (210, 222, 235))
        cx, cy = bx + int(bw * 0.4), by + bh // 2
        for r in (8, 15, 22):
            cv.disc_outline(cx, cy, r, (30, 80, 140), 2)
        cv.circle(cx, cy, 4, (30, 80, 140))
        cv.poly([(bx + int(bw * 0.65), by + bh), (bx + bw, by + bh), (bx + bw, by + int(bh * 0.65))], (90, 145, 95))
    elif kind == "chart":
        cv.rect(bx, by, bw, bh, (248, 244, 232))
        bars = [(0.16, 0.25, TEAL), (0.34, 0.40, TEAL), (0.52, 0.58, TEAL), (0.70, 0.78, RED)]
        for rx, rh, col in bars:
            hh = int(bh * rh)
            cv.rect(bx + int(bw * rx), by + bh - 6 - hh, int(bw * 0.11), hh, col)
        cv.hline(bx + 10, bx + bw - 10, by + bh - 6, INK, 1)
        cv.line(bx + int(bw * 0.14), by + bh - 12, bx + int(bw * 0.82), by + 10, RED, 2)
        if bw >= 100:
            cv.text(bx + int(bw * 0.58), by + 6, "12.29%", 1, RED)
    elif kind == "tents":
        cv.rect(bx, by, bw, bh, (220, 226, 236))
        cv.rect(bx, by + int(bh * 0.78), bw, bh - int(bh * 0.78), (185, 175, 148))
        cv.poly([(bx + int(bw * 0.12), by + int(bh * 0.78)),
                 (bx + int(bw * 0.30), by + int(bh * 0.32)),
                 (bx + int(bw * 0.48), by + int(bh * 0.78))], (215, 195, 160))
        cv.poly([(bx + int(bw * 0.52), by + int(bh * 0.78)),
                 (bx + int(bw * 0.68), by + int(bh * 0.40)),
                 (bx + int(bw * 0.84), by + int(bh * 0.78))], (195, 175, 140))
    elif kind == "docs":
        cv.rect(bx, by, bw, bh, (242, 239, 230))
        cv.rect(bx + int(bw * 0.15), by + 8, int(bw * 0.34), bh - 16, WHITE)
        cv.border(bx + int(bw * 0.15), by + 8, int(bw * 0.34), bh - 16, INK, 1)
        cv.rect(bx + int(bw * 0.52), by + 12, int(bw * 0.34), bh - 16, WHITE)
        cv.border(bx + int(bw * 0.52), by + 12, int(bw * 0.34), bh - 16, INK, 1)
        cv.disc_outline(bx + int(bw * 0.64), by + bh // 2, 11, RED, 2)
    elif kind == "virus":
        cv.rect(bx, by, bw, bh, (250, 235, 230))
        cx, cy = bx + bw // 2, by + bh // 2
        for k in range(8):
            a = math.radians(k * 45)
            cv.line(cx, cy, cx + int(22 * math.cos(a)), cy + int(22 * math.sin(a)), RED, 2)
        cv.circle(cx, cy, 14, RED)
    elif kind == "car":
        cv.rect(bx, by, bw, bh, (226, 232, 238))
        cv.rect(bx, by + int(bh * 0.72), bw, bh - int(bh * 0.72), (110, 115, 122))
        cv.rect(bx + int(bw * 0.25), by + int(bh * 0.44), int(bw * 0.5), int(bh * 0.28), TEAL)
        cv.circle(bx + int(bw * 0.35), by + int(bh * 0.72), 6, INK)
        cv.circle(bx + int(bw * 0.65), by + int(bh * 0.72), 6, INK)
        cv.line(bx + int(bw * 0.22), by + 10, bx + int(bw * 0.78), by + bh - 10, RED, 3)

# ------------------------------------------------------- card renderers
def draw_hero_card(cv, x, y, w, h, tag, tag_col, status, source, title, body, art=None, vec=None):
    cv.rect(x, y, w, h, CARD_BG)
    cv.border(x, y, w, h, RULE, 1)
    img_h = 54
    if art:
        paste_scaled(cv, os.path.join(HERE, "art", art), x + 4, y + 4, w - 8, img_h)
    elif vec:
        draw_vec(vec, cv, x + 4, y + 4, w - 8, img_h)

    ty = y + img_h + 9
    tw = text_width(tag, 1) + 8
    cv.rect(x + 6, ty, tw, 11, tag_col)
    cv.text(x + 10, ty + 2, tag, 1, WHITE)

    meta = f"{status} · {source}" if status else source
    cv.text(x + w - 6 - text_width(meta, 1), ty + 2, meta, 1, MUTED)

    hy = ty + 16
    hy = cv.text_wrap(x + 6, hy, w - 12, title, 2, INK, line_h=17)
    cv.hline(x + 6, x + w - 6, hy + 1, RULE, 1)
    cv.text_wrap(x + 6, hy + 6, w - 12, body, 1, INK, line_h=10)


def draw_small_card(cv, x, y, w, h, tag, tag_col, source, title, body, art=None, vec=None):
    cv.rect(x, y, w, h, CARD_BG)
    cv.border(x, y, w, h, RULE, 1)
    img_h = 44
    if art:
        paste_scaled(cv, os.path.join(HERE, "art", art), x + 4, y + 4, w - 8, img_h)
    elif vec:
        draw_vec(vec, cv, x + 4, y + 4, w - 8, img_h)

    ty = y + img_h + 8
    tw = min(w - 12, text_width(tag, 1) + 6)
    cv.rect(x + 5, ty, tw, 10, tag_col)
    cv.text(x + 8, ty + 2, tag, 1, WHITE)
    if text_width(tag, 1) + text_width(source, 1) + 18 < w:
        cv.text(x + w - 5 - text_width(source, 1), ty + 2, source, 1, MUTED)

    hy = ty + 14
    hy = cv.text_wrap(x + 5, hy, w - 10, title, 1, INK, line_h=10)
    cv.hline(x + 5, x + w - 5, hy + 2, RULE, 1)
    cv.text_wrap(x + 5, hy + 6, w - 10, body, 1, MUTED, line_h=9)


# ------------------------------------------------------- portrait layout
# ------------------------------------------------------- portrait layout v2
def draw_lead_card(cv, x, y, w, h, tag, tag_col, status, source, title, body, art=None, vec=None):
    cv.rect(x, y, w, h, CARD_BG)
    cv.border(x, y, w, h, RULE, 1)
    img_w = 260
    if art:
        paste_scaled(cv, os.path.join(HERE, "art", art), x + 4, y + 4, img_w, h - 8)
    elif vec:
        draw_vec(vec, cv, x + 4, y + 4, img_w, h - 8)
    tx = x + img_w + 12
    tw = text_width(tag, 1) + 8
    cv.rect(tx, y + 8, tw, 11, tag_col)
    cv.text(tx + 4, y + 10, tag, 1, WHITE)
    meta = f"{status} · {source}" if status else source
    cv.text(x + w - 6 - text_width(meta, 1), y + 10, meta, 1, MUTED)
    hy = y + 24
    hy = cv.text_wrap(tx, hy, w - (tx - x) - 12, title, 2, INK, line_h=17)
    cv.hline(tx, x + w - 6, hy + 1, RULE, 1)
    cv.text_wrap(tx, hy + 6, w - (tx - x) - 12, body, 1, INK, line_h=10)


def paste_cover(cv, path, x, y, tw, th):
    """Paste an image cropped (centre) to the target aspect, then scaled."""
    if not os.path.exists(path):
        cv.rect(x, y, tw, th, (220, 225, 230))
        return
    sw, sh, rows = read_png_rgb(path)
    sa = sw / sh
    ta = tw / th
    if sa > ta:
        cw = int(sh * ta)
        ox = (sw - cw) // 2
        oy = 0
        ch = sh
    else:
        ch = int(sw / ta)
        oy = (sh - ch) // 2
        ox = 0
        cw = sw
    for dy in range(th):
        sy = oy + min(ch - 1, int(dy * ch / th))
        srow = rows[sy]
        for dx in range(tw):
            sx = ox + min(cw - 1, int(dx * cw / tw))
            i = sx * 3
            cv.set(x + dx, y + dy, (srow[i], srow[i + 1], srow[i + 2]))


def draw_mini_card(cv, x, y, w, h, tag, tag_col, source, title, body, art=None, vec=None):
    cv.rect(x, y, w, h, CARD_BG)
    cv.border(x, y, w, h, RULE, 1)
    cv.rect(x, y, w, 3, tag_col)
    if art:
        paste_cover(cv, os.path.join(HERE, "art", art), x + 4, y + 4, 64, h - 8)
    elif vec:
        draw_vec(vec, cv, x + 4, y + 4, 64, h - 8)
    tx = x + 76
    tw = text_width(tag, 1) + 8
    cv.rect(tx, y + 6, tw, 10, tag_col)
    cv.text(tx + 4, y + 8, tag, 1, WHITE)
    if text_width(tag, 1) + text_width(source, 1) + 13 <= w - 76:
        cv.text(x + w - 5 - text_width(source, 1), y + 8, source, 1, MUTED)
    hy = y + 20
    hy = cv.text_wrap(tx, hy, w - 76 - 8, title, 1, INK, line_h=10)
    cv.hline(tx, x + w - 5, hy + 1, RULE, 1)
    cv.text_wrap(tx, hy + 5, w - 76 - 8, body, 1, MUTED, line_h=9)


def draw_scene(cv):
    # Stronger warm gradient: cream at the top, deeper gold at the bottom
    for yy in range(H):
        t = yy / (H - 1)
        c = (int(250 - 28 * t), int(244 - 38 * t), int(230 - 48 * t))
        cv.px[yy * W * 3:(yy + 1) * W * 3] = bytes(c) * W

    # ================= 1. HEADER BANNER =================
    mx = 14
    # Left red date box
    cv.rect(mx, 12, 82, 74, RED)
    cv.text_centre(mx + 41, 18, "NOV", 1, WHITE)
    cv.text_centre(mx + 41, 32, "18", 4, WHITE)
    cv.hline(mx + 12, mx + 70, 68, (220, 140, 140), 1)
    cv.text_centre(mx + 41, 73, "WED · 2026", 1, WHITE)

    # Center navy masthead
    cv.rect(mx + 82, 12, 544, 74, NAVY)
    cv.text(mx + 96, 18, "THE DAY IN WORLD NEWS", 1, (190, 200, 215))
    cv.text(mx + 96, 35, "Wednesday 18 November 2026", 3, WHITE)
    cv.hline(mx + 96, mx + 612, 66, (65, 82, 110), 1)
    cv.text(mx + 96, 72, "Verified summary of 40 global stories reported on Wednesday 18 November 2026.", 1, (205, 212, 224))

    # Right summary box
    cv.rect(mx + 626, 12, 114, 74, (36, 52, 80))
    cv.text(mx + 636, 20, "40 STORIES", 1, WHITE)
    cv.hline(mx + 636, mx + 730, 33, (75, 92, 120), 1)
    cv.text(mx + 636, 40, "7 REGIONS", 1, (205, 212, 224))
    cv.hline(mx + 636, mx + 730, 53, (75, 92, 120), 1)
    cv.text(mx + 636, 60, "ONE PAGE", 1, GOLD)

    # ================= 2. REGION CHIPS =================
    chips = [
        ("ASIA 13", RED, WHITE, 145),
        ("MIDEAST 9", OCHRE, WHITE, 115),
        ("EUROPE 8", BLUE, WHITE, 111),
        ("AMERICAS 6", GREEN, WHITE, 111),
        ("GLOBAL 2", NAVY, WHITE, 86),
        ("AFRICA 1", PURPLE, WHITE, 86),
        ("OCEANIA 1", TEAL, WHITE, 86),
    ]
    cx = mx
    for label, col, fg, cw in chips:
        cv.rect(cx, 92, cw, 16, col)
        cv.text_centre(cx + cw // 2, 97, label, 1, fg)
        cx += cw
    cv.hline(mx, W - mx, 110, GOLD, 2)

    # ================= 3. LEAD STORY =================
    gap = 8
    draw_lead_card(cv, mx, 116, W - 2 * mx, 92,
                   "1 · MIDEAST · WAR", RED, "REPORTED", "REUTERS",
                   "Iran drones hit Bahrain",
                   "Iranian drones hit a US radar site at Sheikh Isa Air Base in Bahrain — the third strike on Bahrain in five days. The US answered with strikes on a missile site on Qeshm Island. A tanker was hit twice in the Strait of Hormuz the same day; one crew member is missing.",
                   "gulf.png", None)

    # ================= 4. TWO MEDIUM CARDS (2-3) =================
    w2 = (W - 2 * mx - gap) // 2
    y2 = 214
    draw_hero_card(cv, mx, y2, w2, 136,
                   "2 · ASIA · APEC", PURPLE, "CONFIRMED", "AP",
                   "Xi meets Putin at APEC in Shenzhen",
                   "Leaders hold bilateral summit as APEC opens.",
                   "summit.png", None)
    draw_hero_card(cv, mx + w2 + gap, y2, w2, 136,
                   "3 · EUROPE · WAR", NAVY, "CONFIRMED", "BBC",
                   "Kerch Bridge span falls",
                   "One span falls; road traffic halted.",
                   "kerch.png", None)

    # ================= 5. NINE MINI CARDS (4-12) =================
    w3 = (W - 2 * mx - 2 * gap) // 3
    minis = [
        ("4 · TECH", TEAL, "NVIDIA", "Nvidia doubles to $115.8B",
         "Chipmaker posts record quarterly revenue on AI demand.", "nvidia.png", None),
        ("5 · DEFENCE", BLUE, "KYIV", "141 drones fired; 126 downed",
         "Air defences down 126 of 141 drones by 0800.", "drones.png", None),
        ("6 · POLITICS", GREEN, "AP", "Peltola wins Alaska Senate",
         "Democrat takes Alaska seat; Senate moves to 56-44.", "peltola.png", None),
        ("7 · TRADE", OCHRE, "REUTERS", "Trump in Manila trade push",
         "Manila calls it an understanding, not a final deal.", None, "ship"),
        ("8 · WEATHER", BLUE, "IMD", "Cyclone Akvan nears Andhra",
         "Landfall due Friday noon on the Andhra coast.", None, "cyclone"),
        ("9 · ECONOMY", RED, "MOSPI", "India inflation hits 12.29%",
         "Wholesale prices up 12.29% in October.", None, "chart"),
        ("10 · GAZA", OCHRE, "UN", "Gaza winter cold hits tents",
         "Displaced families face freezing rain in tents.", None, "tents"),
        ("11 · BANKS", NAVY, "ICIJ", "Deutsche Bank 15M leak",
         "15M files shared with Der Spiegel, 50 outlets.", None, "docs"),
        ("12 · HEALTH", RED, "WHO", "Ebola in DRC hits children",
         "Three in four pediatric cases fatal.", None, "virus"),
    ]
    for r in range(3):
        yy = 356 + r * (70 + gap)
        for c in range(3):
            item = minis[r * 3 + c]
            draw_mini_card(cv, mx + c * (w3 + gap), yy, w3, 70, *item)

    # ================= 6. COLOURED WORLD MAP =================
    ys = 584
    cv.text(mx, ys, "WHERE IT HAPPENED", 2, NAVY)
    right_note = "DOTS: 12 MAIN STORIES · RINGS: STORIES PER REGION"
    cv.text(W - mx - text_width(right_note, 1), ys, right_note, 1, MUTED)

    map_x, map_y, map_w, map_h = mx, 604, W - 2 * mx, 156
    cv.rect(map_x, map_y, map_w, map_h, (210, 224, 236))
    cv.border(map_x, map_y, map_w, map_h, RULE, 1)
    # Continents, one colour each
    cv.poly([(28, 632), (60, 614), (120, 610), (175, 617), (185, 637),
             (160, 657), (120, 664), (80, 660), (40, 650)], (90, 160, 110))
    cv.poly([(190, 610), (210, 606), (218, 616), (200, 622)], (90, 160, 110))
    cv.poly([(150, 682), (185, 674), (205, 687), (200, 712), (185, 737),
             (165, 732), (150, 707)], (40, 150, 140))
    cv.poly([(350, 620), (385, 612), (410, 620), (405, 637),
             (375, 642), (355, 634)], (70, 120, 200))
    cv.poly([(355, 647), (400, 642), (425, 657), (420, 692), (400, 722),
             (375, 717), (355, 687)], (210, 150, 50))
    cv.poly([(415, 617), (480, 604), (580, 602), (670, 610), (700, 627),
             (690, 657), (640, 682), (560, 687), (480, 677), (430, 652)], (200, 80, 70))
    cv.poly([(620, 692), (650, 687), (665, 697), (640, 707)], (200, 80, 70))
    cv.poly([(655, 717), (700, 712), (715, 727), (690, 742), (660, 737)], (140, 90, 180))
    cv.poly([(690, 622), (700, 617), (705, 632), (695, 640)], (200, 80, 70))

    # Numbered dots: the 12 main stories at their locations
    dots = [
        (1, 478, 664), (2, 648, 647), (3, 408, 632), (4, 75, 647),
        (5, 392, 624), (6, 55, 620), (7, 660, 672), (8, 565, 674),
        (9, 545, 660), (10, 432, 658), (11, 372, 626), (12, 388, 704),
    ]
    for n, dx, dy in dots:
        cv.circle(dx, dy, 7, NAVY)
        s = str(n)
        cv.text(dx - text_width(s, 1) // 2, dy - 3, s, 1, WHITE)

    # Ring badges: stories per region
    badges = [
        (13, 600, 632, RED), (9, 505, 678, OCHRE), (8, 340, 637, BLUE),
        (6, 120, 632, GREEN), (1, 410, 712, OCHRE), (1, 690, 730, PURPLE),
    ]
    for n, dx, dy, col in badges:
        cv.circle(dx, dy, 9, col)
        cv.disc_outline(dx, dy, 9, WHITE, 2)
        s = str(n)
        cv.text(dx - text_width(s, 1) // 2, dy - 3, s, 1, WHITE)

    # Legend box in the empty ocean (South Atlantic)
    lx, ly, lw, lh = 222, 708, 134, 44
    cv.rect(lx, ly, lw, lh, CARD_BG)
    cv.border(lx, ly, lw, lh, RULE, 1)
    legend = [
        ("ASIA", RED), ("MIDEAST", OCHRE), ("EUROPE", BLUE),
        ("AMERICAS", GREEN), ("GLOBAL", NAVY), ("OCEANIA", TEAL),
    ]
    for i, (name, col) in enumerate(legend):
        ex = lx + 6 + (i // 3) * 62
        ey = ly + 5 + (i % 3) * 14
        cv.rect(ex, ey, 8, 8, col)
        cv.text(ex + 12, ey + 1, name, 1, INK)

    # ================= 7. THE REST OF THE DAY, BY REGION =================
    list_y = 772
    cv.rect(mx, 766, W - 2 * mx, 188, (250, 246, 236))
    cv.border(mx, 766, W - 2 * mx, 188, RULE, 1)

    def draw_list_col(lx, ly, lw, groups):
        cy = ly
        for col, items in groups:
            for num, loc, desc in items:
                cv.text(lx, cy, num, 1, col)
                nw = text_width(num + " ", 1)
                cv.text(lx + nw, cy, loc, 1, col)
                lw_loc = text_width(loc + " ", 1)
                cy = cv.text_wrap(lx + nw + lw_loc, cy, lw - nw - lw_loc, desc, 1, INK, line_h=9)
                cy += 1
            cy += 4
        return cy

    col_w = (W - 2 * mx - 12) // 2
    draw_list_col(mx + 6, list_y, col_w - 6, [
        (RED, [
            ("13", "Manila:", "QUAD unveils maritime patrol plan"),
            ("14", "Shenzhen:", "Putin arrives for APEC talks"),
            ("15", "Manila:", "US-Philippine trade understanding"),
            ("16", "Shenzhen:", "Lee seeks China's help on N. Korea"),
            ("17", "Shenzhen:", "Canada-China extend trade deals"),
            ("18", "Tokyo:", "India-Japan 2+2 security talks open"),
            ("19", "Manila:", "Modi proposes free e-visas for ASEAN"),
            ("20", "Manila:", "ASEAN chair passes to Singapore"),
            ("21", "Chennai:", "Dhoni retires from IPL at 45"),
        ]),
        (OCHRE, [
            ("22", "Hormuz:", "US strikes missile site on Qeshm"),
            ("23", "Hormuz:", "LPG tanker hit twice; one missing"),
            ("24", "Hormuz:", "ADNOC-linked vessel attacked at sea"),
            ("25", "Riyadh:", "Saudi intercepts Houthi cruise missile"),
            ("26", "Aden:", "Houthis advance to 60 km from Aden"),
            ("27", "Tehran:", "Iran refuses nuclear inspections"),
            ("28", "Jerusalem:", "Kahana elected Knesset speaker"),
        ]),
    ])
    draw_list_col(mx + col_w + 12, list_y, col_w - 6, [
        (BLUE, [
            ("29", "Kyiv:", "Russia hits Dnipro bridges; outages"),
            ("30", "Kyiv:", "Ukraine seeks fighters, eyes Mirages"),
            ("31", "Russia:", "Ukraine drones hit southern refineries"),
            ("32", "Kyiv:", "Peace talks continue; Zelensky: not easy"),
            ("33", "London:", "UK sanctions Israeli settlement firms"),
        ]),
        (GREEN, [
            ("34", "Washington:", "US tightens AI chip curbs"),
            ("35", "California:", "Waymo halts driverless highway rides"),
            ("36", "San Francisco:", "OpenAI launches GPT-6.2, cuts prices"),
            ("37", "US:", "Loses measles elimination status after 26 yrs"),
        ]),
        (NAVY, [
            ("38", "Global:", "Cyber attack hits Apple, Zoom, BBC"),
            ("39", "Washington:", "NSA network hit by US tech outages"),
        ]),
        (TEAL, [
            ("40", "Canberra:", "Australia sanctions settlers, firms"),
        ]),
    ])

    # ================= 8. DATE CHECK & FOOTER =================
    dc_y = 958
    cv.rect(mx, dc_y, W - 2 * mx, 34, (253, 238, 236))
    cv.border(mx, dc_y, W - 2 * mx, 34, RED, 1)
    cv.text(mx + 8, dc_y + 6, "DATE CHECK", 1, RED)
    cv.text_wrap(
        mx + 78, dc_y + 6, W - 2 * mx - 86,
        "Verified for Wednesday 18 November 2026 — all 40 items cross-checked against wire reports; region counts sum to 40 exactly (Asia 13, Mideast 9, Europe 8, Americas 6, Global 2, Africa 1, Oceania 1).",
        1, INK, line_h=11
    )

    cv.text(mx, 1002, "SOURCES: REUTERS · AP · BBC · AL JAZEERA · WHO · IMD · MOSPI", 1, MUTED)
    right_note = "All 40 stories are from Wednesday 18 November 2026."
    cv.text(W - mx - text_width(right_note, 1), 1002, right_note, 1, MUTED)

def write_png(cv, path):
    raw = bytearray()
    for y in range(H):
        raw.append(0)
        raw.extend(cv.px[y * W * 3:(y + 1) * W * 3])
    comp = zlib.compress(bytes(raw), 9)

    def chunk(kind, data):
        c = struct.pack(">I", len(data)) + kind + data
        return c + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(png)
    return len(png)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    cv = Canvas()
    draw_scene(cv)
    size = write_png(cv, os.path.join(out, "entry.png"))
    print(f"wrote {os.path.join(out, 'entry.png')} {size} bytes")


if __name__ == "__main__":
    main()