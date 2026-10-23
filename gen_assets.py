# -*- coding: utf-8 -*-
"""生成模块图标、详情页插画、应用图标（SVG + PNG）"""
import os
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "assets", "img")
ICONS = os.path.join(BASE, "assets", "icons")
os.makedirs(IMG, exist_ok=True)
os.makedirs(ICONS, exist_ok=True)

GREEN = "#1E6F5C"
GREEN2 = "#2E9E7E"
WARM = "#E98A3C"
RED = "#D64545"
BLUE = "#3B82F6"
PURPLE = "#8B5CF6"
TEAL = "#0EA5A4"
AMBER = "#F59E0B"
PINK = "#EC4899"
EMERALD = "#10B981"


def motif(body, stroke=GREEN, sw=3.2):
    return (
        f'<g fill="none" stroke="{stroke}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round">{body}</g>'
    )


# ---------------- 各模块图形（100×100 坐标系） ----------------

def m_fall():
    return motif(f'''
      <rect x="18" y="40" width="64" height="46" rx="6" stroke-dasharray="5 5" opacity=".45"/>
      <circle cx="35" cy="58" r="7" fill="#fff"/>
      <path d="M41 62 L64 72 L82 66"/>
      <path d="M52 66 L60 58"/>
      <path d="M27 86 L90 86"/>
      <path d="M70 26 a10 10 0 0 1 0 14" stroke="{RED}"/>
      <path d="M76 20 a18 18 0 0 1 0 26" stroke="{RED}" opacity=".6"/>
      <circle cx="72" cy="33" r="4" fill="{RED}" stroke="none"/>
    ''')


def m_voice():
    return motif(f'''
      <rect x="42" y="18" width="16" height="30" rx="8" fill="#fff"/>
      <path d="M50 48 L50 64"/>
      <path d="M41 64 L59 64"/>
      <path d="M32 30 a18 18 0 0 0 0 20" opacity=".55"/>
      <path d="M25 24 a27 27 0 0 0 0 32" opacity=".3"/>
      <path d="M68 30 a18 18 0 0 1 0 20" opacity=".55"/>
      <path d="M75 24 a27 27 0 0 1 0 32" opacity=".3"/>
      <rect x="20" y="70" width="34" height="18" rx="9" fill="#fff"/>
      <path d="M28 88 L26 94 L38 88"/>
    ''')


def m_ptz():
    return motif(f'''
      <rect x="30" y="38" width="40" height="26" rx="7" fill="#fff"/>
      <circle cx="50" cy="51" r="9"/>
      <circle cx="50" cy="51" r="3.6" fill="{GREEN2}" stroke="none"/>
      <path d="M50 64 L50 74"/>
      <path d="M38 78 L62 78"/>
      <path d="M22 51 a28 28 0 0 1 6 -17" stroke-dasharray="4 5" opacity=".6"/>
      <path d="M78 51 a28 28 0 0 0 -6 -17" stroke-dasharray="4 5" opacity=".6"/>
      <path d="M17 58 L11 50 L20 47" opacity=".7"/>
      <path d="M83 58 L89 50 L80 47" opacity=".7"/>
    ''')


def m_gesture():
    fingers = '''
      <rect x="37" y="24" width="6" height="22" rx="3" fill="#fff"/>
      <rect x="46" y="18" width="6" height="28" rx="3" fill="#fff"/>
      <rect x="55" y="18" width="6" height="28" rx="3" fill="#fff"/>
      <rect x="64" y="24" width="6" height="22" rx="3" fill="#fff"/>
    '''
    return motif(f'''
      {fingers}
      <rect x="34" y="42" width="40" height="34" rx="12" fill="#fff"/>
      <rect x="24" y="46" width="9" height="20" rx="4.5" fill="#fff"/>
      <circle cx="40" cy="24" r="2" fill="{WARM}" stroke="none"/>
      <circle cx="49" cy="18" r="2" fill="{WARM}" stroke="none"/>
      <circle cx="58" cy="18" r="2" fill="{WARM}" stroke="none"/>
      <circle cx="67" cy="24" r="2" fill="{WARM}" stroke="none"/>
      <path d="M22 84 q28 -10 56 0" opacity=".4"/>
    ''')


def m_object():
    return motif(f'''
      <rect x="26" y="36" width="32" height="46" rx="4" stroke-dasharray="5 5" opacity=".45"/>
      <path d="M32 50 L52 50 L49 76 L35 76 Z" fill="#fff"/>
      <path d="M52 56 q10 0 10 8 q0 8 -10 8" fill="none"/>
      <rect x="64" y="42" width="18" height="38" rx="5" fill="#fff"/>
      <rect x="69" y="34" width="8" height="8" rx="2"/>
      <path d="M68 56 L78 56" opacity=".5"/>
      <path d="M68 64 L78 64" opacity=".5"/>
    ''')


def m_remote():
    return motif(f'''
      <rect x="32" y="18" width="36" height="62" rx="9" fill="#fff"/>
      <rect x="37" y="26" width="26" height="36" rx="4" opacity=".35"/>
      <path d="M45 40 L45 52 L55 46 Z" fill="{TEAL}" stroke="none"/>
      <path d="M43 70 L57 70"/>
      <path d="M74 30 a14 14 0 0 1 0 18" stroke="{TEAL}" opacity=".7"/>
      <path d="M80 24 a22 22 0 0 1 0 30" stroke="{TEAL}" opacity=".35"/>
    ''')


def m_medicine():
    return motif(f'''
      <g transform="rotate(-28 46 58)">
        <rect x="28" y="50" width="36" height="16" rx="8" fill="#fff"/>
        <path d="M46 50 L46 66"/>
        <path d="M32 50 a8 8 0 0 1 8 -8 a8 8 0 0 1 0 16 z" fill="{AMBER}" stroke="none" opacity=".25"/>
      </g>
      <circle cx="70" cy="34" r="14" fill="#fff"/>
      <path d="M70 26 L70 34 L77 38"/>
      <path d="M64 80 L76 80" opacity=".5"/>
      <path d="M70 74 L70 86" opacity=".5"/>
    ''')


def m_message():
    return motif(f'''
      <rect x="20" y="28" width="46" height="32" rx="12" fill="#fff"/>
      <path d="M32 60 L28 72 L44 60"/>
      <path d="M36 38 L36 52 L48 45 Z" fill="{PINK}" stroke="none"/>
      <path d="M76 26 c4 -6 12 -4 12 2 c0 5 -7 9 -12 13 c-5 -4 -12 -8 -12 -13 c0 -6 8 -8 12 -2 z" fill="{PINK}" stroke="none" opacity=".22"/>
      <path d="M76 26 c4 -6 12 -4 12 2 c0 5 -7 9 -12 13 c-5 -4 -12 -8 -12 -13 c0 -6 8 -8 12 -2 z" stroke="{PINK}" opacity=".7"/>
    ''')


def m_report():
    return motif(f'''
      <rect x="28" y="18" width="36" height="52" rx="5" fill="#fff"/>
      <path d="M36 30 L56 30" opacity=".4"/>
      <rect x="36" y="50" width="6" height="12" rx="2" fill="{EMERALD}" stroke="none" opacity=".55"/>
      <rect x="46" y="42" width="6" height="20" rx="2" fill="{EMERALD}" stroke="none" opacity=".75"/>
      <rect x="56" y="46" width="6" height="16" rx="2" fill="{EMERALD}" stroke="none"/>
      <circle cx="70" cy="66" r="13" fill="#fff"/>
      <path d="M64 66 L68 70 L76 61"/>
    ''')


MODULES = [
    ("fall", m_fall, RED, "#FDECE4"),
    ("voice", m_voice, GREEN2, "#E4F3EC"),
    ("ptz", m_ptz, BLUE, "#E8F1FD"),
    ("gesture", m_gesture, WARM, "#FFF1E2"),
    ("object", m_object, PURPLE, "#F1EBFE"),
    ("remote", m_remote, TEAL, "#E0F5F4"),
    ("medicine", m_medicine, AMBER, "#FFF6E0"),
    ("message", m_message, PINK, "#FDE7F1"),
    ("report", m_report, EMERALD, "#E3F7EF"),
]


def icon_svg(body):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">'
        + body
        + "</svg>"
    )


def hero_svg(body, accent, tint):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F4FBF8"/>
      <stop offset="1" stop-color="{tint}"/>
    </linearGradient>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{accent}" stop-opacity=".22"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="640" height="360" fill="url(#bg)"/>
  <circle cx="320" cy="180" r="150" fill="url(#ring)"/>
  <circle cx="320" cy="180" r="150" fill="none" stroke="{accent}" stroke-opacity=".18" stroke-dasharray="3 7"/>
  <circle cx="320" cy="180" r="112" fill="#fff" fill-opacity=".72"/>
  <circle cx="112" cy="78" r="7" fill="{accent}" fill-opacity=".35"/>
  <circle cx="540" cy="270" r="9" fill="{accent}" fill-opacity=".28"/>
  <circle cx="500" cy="76" r="5" fill="{accent}" fill-opacity=".5"/>
  <circle cx="140" cy="286" r="5" fill="{accent}" fill-opacity=".45"/>
  <path d="M60 300 q40 -26 86 -10" stroke="{accent}" stroke-opacity=".25" fill="none" stroke-width="2"/>
  <path d="M500 300 q40 -26 86 -10" stroke="{accent}" stroke-opacity=".25" fill="none" stroke-width="2"/>
  <g transform="translate(205 65) scale(2.3)">{body}</g>
</svg>'''


for mid, fn, accent, tint in MODULES:
    body = fn()
    with open(os.path.join(IMG, f"icon-{mid}.svg"), "w", encoding="utf-8") as f:
        f.write(icon_svg(body))
    with open(os.path.join(IMG, f"hero-{mid}.svg"), "w", encoding="utf-8") as f:
        f.write(hero_svg(body, accent, tint))
    print("svg", mid)

# 品牌小图标
leaf = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <path d="M50 84 C50 56 68 34 88 28 C88 56 72 80 50 84 Z" fill="#2E9E7E"/>
  <path d="M52 84 C36 78 20 62 18 40 C40 44 52 62 52 84 Z" fill="#1E6F5C" opacity=".85"/>
  <path d="M50 86 L50 96" stroke="#1E6F5C" stroke-width="6" stroke-linecap="round"/>
</svg>'''
with open(os.path.join(IMG, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(leaf)

# ---------------- 应用图标（PNG） ----------------

def make_icon(size, path, padding_ratio=0.0):
    S = size * 2
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 渐变背景
    for y in range(S):
        t = y / S
        r = int(0x33 + (0x1E - 0x33) * t)
        g = int(0xC0 + (0x6F - 0xC0) * t)
        b = int(0x8E + (0x5C - 0x8E) * t)
        d.line([(0, y), (S, y)], fill=(r, g, b, 255))
    # 圆角
    mask = Image.new("L", (S, S), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
    img.putalpha(mask)

    # 白色机器人头
    cx, cy = S * 0.5, S * 0.55
    w, h = S * 0.46, S * 0.36
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2],
                        radius=int(S * 0.09), fill=(255, 255, 255, 255))
    # 天线
    d.line([(cx, cy - h / 2), (cx, cy - h / 2 - S * 0.09)], fill=(255, 255, 255, 255), width=int(S * 0.028))
    d.ellipse([cx - S * 0.028, cy - h / 2 - S * 0.12, cx + S * 0.028, cy - h / 2 - S * 0.066],
              fill=(255, 255, 255, 255))
    # 眼睛
    eye = S * 0.042
    for ex in (cx - S * 0.095, cx + S * 0.095):
        d.ellipse([ex - eye, cy - eye, ex + eye, cy + eye], fill=(0x1E, 0x6F, 0x5C, 255))
    # 微笑
    d.arc([cx - S * 0.07, cy + S * 0.005, cx + S * 0.07, cy + S * 0.085],
          start=20, end=160, fill=(0x1E, 0x6F, 0x5C, 255), width=int(S * 0.022))
    # 叶子点缀
    d.ellipse([cx + S * 0.16, cy - S * 0.24, cx + S * 0.25, cy - S * 0.15],
              fill=(255, 255, 255, 120))

    img = img.resize((size, size), Image.LANCZOS)
    img.save(path, "PNG")
    print("png", path)


make_icon(512, os.path.join(ICONS, "icon-512.png"))
make_icon(192, os.path.join(ICONS, "icon-192.png"))
make_icon(180, os.path.join(ICONS, "apple-touch-icon.png"))
make_icon(32, os.path.join(BASE, "favicon.png"))
print("done")
