from pathlib import Path

import cairo

from contents import load_contents

# A4 canvas
page_height = 842
page_width = 595

# Layout
contents = load_contents(Path("contents.yml"))
sidebar_width = page_width / 3


# Colors
def decimal_color(r, g, b):
    return [r / 255, g / 255, b / 255]


COLOR_WHITE = decimal_color(255, 255, 255)
COLOR_GREY_60 = decimal_color(153, 153, 153)
COLOR_GREY_70 = decimal_color(179, 179, 179)
COLOR_GREY_80 = decimal_color(203, 203, 203)
COLOR_GREY_90 = decimal_color(230, 230, 230)
COLOR_BLACK = decimal_color(0, 0, 0)


def draw_text(ctx: cairo.Context, text: str, x: float, y: float, size: int = 12):
    ctx.save()
    ctx.set_source_rgb(*COLOR_GREY_60)
    ctx.set_font_size(12)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    tw, th = ctx.text_extents(text)[2:4]
    nx = tw / 2
    ny = th / 2

    ctx.translate(x - nx, y - ny)
    ctx.show_text(text)
    ctx.restore()


def draw_sidebar(ctx: cairo.Context):

    # Sidebar container
    ctx.save()
    ctx.rectangle(0, 0, sidebar_width, page_height)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.restore()

    # Sidebar contents
    draw_text(ctx, contents.bio.name, x=sidebar_width / 2, y=200, size=16)


# Create PDF
with cairo.PDFSurface(Path("cv.pdf"), page_width, page_height) as surface:
    ctx = cairo.Context(surface)

    draw_sidebar(ctx)
