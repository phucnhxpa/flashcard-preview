#!/usr/bin/env python3
"""Compact teaching diagrams for the Harry 12 Jul differentiation/trig multi-step deck.
Every figure is rendered at max-width:380px in the cards, so kept small and legible.
Colour convention: blue = original/given, red = key construction, green = final answer,
grey dashed = auxiliary."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

OUT = os.path.dirname(os.path.abspath(__file__))
GREEN = "#1b4d2c"
RED = "#961414"
BLUE = "#1f5fa8"
GREY = "#888888"

plt.rcParams.update({
    "font.size": 11,
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "cm",
})


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


# ------------------------------------------------------------ Q1 modulus graph
def q1_modulus():
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    x = np.linspace(-0.5, 9.5, 400)
    f = 2 * np.abs(x - 5) + 10
    ax.plot(x, f, color=BLUE, lw=2.2, label=r"$y=2|x-5|+10$")
    # branch labels
    ax.plot(x[x >= 5], (2 * x)[x >= 5], color=GREY, ls=":", lw=1.2)
    ax.plot(x[x < 5], (-2 * x + 20)[x < 5], color=GREY, ls=":", lw=1.2)
    # line y = 6x
    xl = np.linspace(0, 4.2, 50)
    ax.plot(xl, 6 * xl, color=RED, lw=1.8, label=r"$y=6x$")
    # vertex P
    ax.plot([5], [10], "o", color=GREEN, ms=7, zorder=5)
    ax.annotate(r"$P=(5,10)$", (5, 10), textcoords="offset points",
                xytext=(6, 6), color=GREEN, fontsize=10, fontweight="bold")
    # intersection A at x=2.5 -> y=15
    ax.plot([2.5], [15], "s", color=RED, ms=6, zorder=5)
    ax.annotate(r"$A:\;6x=-2x+20$" "\n" r"$x=\frac{5}{2}$", (2.5, 15),
                textcoords="offset points", xytext=(8, -2), color=RED, fontsize=9)
    ax.text(6.7, 13.2, r"$y=2x$", color=GREY, fontsize=9)
    ax.text(1.0, 17.4, r"$y=-2x+20$", color=GREY, fontsize=9)
    ax.axhline(0, color="#444", lw=0.8)
    ax.axvline(0, color="#444", lw=0.8)
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(0, 22)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(r"$f(x)>6x$ on the left branch $\Rightarrow x<\frac{5}{2}$",
                 fontsize=10)
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.9)
    ax.grid(alpha=0.2)
    save(fig, "q1_modulus.png")


# ------------------------------------------------------------ Q3 log-log line
def q3_loglog():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    X = np.linspace(-0.4, 2.6, 50)
    # straight line through (0,6) and (2,0): gradient -3
    Y = 6 - 3 * X
    ax.plot(X, Y, color=BLUE, lw=2.2)
    ax.plot([0], [6], "o", color=GREEN, ms=7, zorder=5)
    ax.annotate(r"$(0,\,6)$", (0, 6), textcoords="offset points",
                xytext=(8, 2), color=GREEN, fontsize=10, fontweight="bold")
    ax.plot([2], [0], "o", color=GREEN, ms=7, zorder=5)
    ax.annotate(r"$(2,\,0)$", (2, 0), textcoords="offset points",
                xytext=(6, 8), color=GREEN, fontsize=10, fontweight="bold")
    ax.axhline(0, color="#444", lw=0.8)
    ax.axvline(0, color="#444", lw=0.8)
    ax.set_xlim(-0.5, 2.7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel(r"$\log_{10} x$")
    ax.set_ylabel(r"$\log_{10} y$")
    ax.set_title("Sketch: straight line, label intercepts as pairs", fontsize=9.5)
    ax.grid(alpha=0.2)
    save(fig, "q3_loglog.png")


# ------------------------------------------------------------ Q4 R-form triangle
def q4_triangle():
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    ax.set_aspect("equal")
    ax.axis("off")
    adj, opp = 4.0, 2.0
    ax.plot([0, adj], [0, 0], color=BLUE, lw=2)
    ax.plot([adj, adj], [0, opp], color=BLUE, lw=2)
    ax.plot([0, adj], [0, opp], color=RED, lw=2)
    ax.text(adj / 2, -0.28, r"$R\cos\alpha=4$", color=BLUE, ha="center", fontsize=10)
    ax.text(adj + 0.12, opp / 2, r"$R\sin\alpha=2$", color=BLUE, va="center", fontsize=10)
    ax.text(adj / 2 - 0.5, opp / 2 + 0.28, r"$R=2\sqrt{5}$", color=RED,
            rotation=27, fontsize=10)
    th = np.linspace(0, np.arctan2(opp, adj), 30)
    ax.plot(0.9 * np.cos(th), 0.9 * np.sin(th), color=GREEN, lw=1.4)
    ax.text(1.05, 0.22, r"$\alpha$", color=GREEN, fontsize=12)
    ax.add_patch(Rectangle((adj - 0.28, 0), 0.28, 0.28, fill=False, ec="#444", lw=1))
    ax.set_title(r"$\tan\alpha=\frac{2}{4}=\frac{1}{2},\;\;R=\sqrt{4^2+2^2}=2\sqrt{5}$",
                 fontsize=10)
    ax.set_xlim(-0.4, adj + 1.6)
    ax.set_ylim(-0.6, opp + 0.7)
    save(fig, "q4_triangle.png")


# ------------------------------------------------------------ Q4 sine solutions
def q4_sine():
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    a = 0.464
    x = np.linspace(0, 4.6, 600)
    y = np.sin(2 * x + a)
    ax.plot(x, y, color=BLUE, lw=2)
    ax.axhline(1, color=GREY, ls="--", lw=1)
    ax.axhline(0, color="#444", lw=0.8)
    # maxima where 2x+a = pi/2 and 5pi/2
    x1 = (np.pi / 2 - a) / 2
    x2 = (5 * np.pi / 2 - a) / 2
    ax.plot([x1], [1], "o", color=RED, ms=6)
    ax.annotate(r"$x\approx0.553$" "\n" r"(smallest)", (x1, 1),
                textcoords="offset points", xytext=(-6, -34), color=RED, fontsize=8.5,
                ha="center")
    ax.plot([x2], [1], "o", color=GREEN, ms=7)
    ax.annotate(r"$x\approx3.69$" "\n" r"(2nd smallest)", (x2, 1),
                textcoords="offset points", xytext=(-12, -36), color=GREEN,
                fontsize=8.5, fontweight="bold", ha="center")
    ax.set_xlim(0, 4.6)
    ax.set_ylim(-1.3, 1.5)
    ax.set_xlabel("$x$")
    ax.set_ylabel(r"$\sin(2x+\alpha)$")
    ax.set_title(r"Solve the whole angle first: $2x+\alpha=\frac{\pi}{2},\frac{5\pi}{2}$",
                 fontsize=9.5)
    ax.grid(alpha=0.2)
    save(fig, "q4_sine.png")


if __name__ == "__main__":
    q1_modulus()
    q3_loglog()
    q4_triangle()
    q4_sine()
    print("diagrams done")
