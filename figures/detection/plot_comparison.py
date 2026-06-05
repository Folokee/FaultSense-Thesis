"""
Comparison plots for the Task A Results and Discussion section.

Plain, glance-readable bar charts:
  - Figure 1: two bar charts (binary | macro per-class) for all six models.
  - Figure 2: grouped bars per fault class, legend placed BELOW the plot so it
    never covers a bar.
  - Figure 3: horizontal size bars (log scale) with the PR-AUC printed at each
    bar end.
One consistent colour per model across every figure. Bars start at zero so
heights are honest.

Run from the FaultSense-Thesis root directory:
    python figures/detection/plot_comparison.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUT = Path(__file__).parent

# ── One consistent colour per model (Wong 2011, colourblind-safe) ─────────────
COLORS = {
    'BOCD':    '#7f7f7f',  # grey
    'IF':      '#E69F00',  # orange
    'OC-SVM':  '#0072B2',  # blue
    'MAAT':    '#CC79A7',  # rose
    'GTBAD':   '#D55E00',  # vermillion
    'PC-Flow': '#009E73',  # green (winner)
}
LABELS = {
    'BOCD': 'BOCD', 'IF': 'Isolation\nForest', 'OC-SVM': 'OC-SVM',
    'MAAT': 'MAAT', 'GTBAD': 'GTBAD', 'PC-Flow': 'PC-Flow',
}

# ── Verified values (thesis tables) ───────────────────────────────────────────
binary_mean = {'BOCD': 0.870, 'IF': 0.974, 'OC-SVM': 0.987,
               'MAAT': 0.982, 'GTBAD': 0.9896, 'PC-Flow': 0.972}
binary_std  = {'BOCD': 0.068, 'IF': 0.028, 'OC-SVM': 0.010,
               'MAAT': 0.017, 'GTBAD': 0.019, 'PC-Flow': 0.013}

macro_mean  = {'BOCD': 0.401, 'IF': 0.822, 'OC-SVM': 0.965,
               'MAAT': 0.924, 'GTBAD': 0.9752, 'PC-Flow': 0.990}
macro_std   = {'BOCD': 0.070, 'IF': 0.098, 'OC-SVM': 0.019,
               'MAAT': 0.083, 'GTBAD': 0.071, 'PC-Flow': 0.005}

# Per-class PR-AUC vs Normal  (order: SC, Degradation, OC, Shadowing)
per_class_mean = {
    'BOCD':    [0.130, 0.121, 0.489, 0.865],
    'IF':      [0.818, 0.496, 1.000, 0.972],
    'OC-SVM':  [0.992, 0.884, 1.000, 0.983],
    'MAAT':    [0.994, 0.753, 1.000, 0.981],
    'GTBAD':   [0.9998, 0.9140, 1.0000, 0.9871],
    'PC-Flow': [1.000, 0.998, 1.000, 0.962],
}
per_class_std = {
    'BOCD':    [0.050, 0.050, 0.191, 0.067],
    'IF':      [0.222, 0.185, 0.000, 0.029],
    'OC-SVM':  [0.009, 0.074, 0.000, 0.014],
    'MAAT':    [0.013, 0.268, 0.000, 0.018],
    'GTBAD':   [0.016, 0.241, 0.004, 0.022],
    'PC-Flow': [0.000, 0.004, 0.000, 0.021],
}

SIZE = {'BOCD': 28, 'OC-SVM': 1_280, 'MAAT': 184_213,
        'GTBAD': 869_769, 'PC-Flow': 20_124}

# Models left-to-right by macro per-class PR-AUC (winner first)
ORDER = ['PC-Flow', 'GTBAD', 'OC-SVM', 'MAAT', 'IF', 'BOCD']

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.titlesize': 12.5,
    'axes.labelsize': 11.5,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.axisbelow': True,
    'ytick.left': True,
})


def style_axis(ax):
    ax.set_ylim(0, 1.08)
    ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.grid(axis='y', ls='--', color='#cccccc', alpha=0.6, zorder=0)
    ax.set_axisbelow(True)


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Binary vs Macro per-class PR-AUC  (two bar charts)
# ═════════════════════════════════════════════════════════════════════════════
fig1, (axA, axB) = plt.subplots(1, 2, figsize=(10.0, 4.4), sharey=True)
x = np.arange(len(ORDER))
cols = [COLORS[m] for m in ORDER]

for ax, mean, std, title in [
    (axA, binary_mean, binary_std, '(a) Binary PR-AUC'),
    (axB, macro_mean,  macro_std,  '(b) Macro per-class PR-AUC'),
]:
    bars = ax.bar(x, [mean[m] for m in ORDER], width=0.68, color=cols,
                  yerr=[std[m] for m in ORDER], capsize=4,
                  error_kw=dict(ecolor='#444444', elinewidth=1.1, capthick=1.1),
                  zorder=3, edgecolor='white', linewidth=0.6)
    style_axis(ax)
    ax.set_title(title, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels([LABELS[m] for m in ORDER])
    # value labels above each bar (clear of the error cap)
    for m, b in zip(ORDER, bars):
        ax.text(b.get_x() + b.get_width() / 2, mean[m] + std[m] + 0.025,
                f'{mean[m]:.3f}', ha='center', va='bottom', fontsize=9)

axA.set_ylabel('PR-AUC')
# no-skill reference on the binary panel
axA.axhline(0.64, color='#999999', ls=':', lw=1.3, zorder=2)
axA.text(len(ORDER) - 0.45, 0.645, 'no-skill (0.64)', ha='right', va='bottom',
         fontsize=8.5, color='#777777', style='italic')

fig1.tight_layout()
fig1.savefig(OUT / 'fig_comparison_binary_macro.png', dpi=300, bbox_inches='tight')
print("Saved fig_comparison_binary_macro.png")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Per-class PR-AUC  (grouped bars, legend below)
# ═════════════════════════════════════════════════════════════════════════════
CLASS_TITLES = ['Short-Circuit', 'Degradation', 'Open-Circuit', 'Shadowing']
HARD = 1
n_mod = len(ORDER)
group_w = 0.82
bw = group_w / n_mod

fig2, ax = plt.subplots(figsize=(10.0, 4.6))
xc = np.arange(len(CLASS_TITLES))

for j, m in enumerate(ORDER):
    offs = (j - (n_mod - 1) / 2) * bw
    ax.bar(xc + offs, [per_class_mean[m][c] for c in range(4)], width=bw * 0.92,
           color=COLORS[m], label=LABELS[m].replace('\n', ' '),
           yerr=[per_class_std[m][c] for c in range(4)], capsize=2,
           error_kw=dict(ecolor='#555555', elinewidth=0.8, capthick=0.8),
           zorder=3, edgecolor='white', linewidth=0.4)

# Highlight the Degradation group
ax.axvspan(xc[HARD] - 0.5, xc[HARD] + 0.5, color='#fff3d6', zorder=0)
ax.text(xc[HARD], 1.045, 'the class that separates the models',
        ha='center', va='bottom', fontsize=9, color='#b07400', style='italic')

style_axis(ax)
ax.set_ylabel('Per-class PR-AUC (fault vs. normal)')
ax.set_xticks(xc)
ax.set_xticklabels([f'{t}\n(cls {i + 1})' for i, t in enumerate(CLASS_TITLES)],
                   fontsize=11)
ax.set_xlim(-0.5, len(CLASS_TITLES) - 0.5)

# Legend BELOW the plot, one row -> never covers a bar
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=6,
          frameon=False, fontsize=9.5, handlelength=1.3, columnspacing=1.4)

fig2.tight_layout()
fig2.savefig(OUT / 'fig_comparison_perclass.png', dpi=300, bbox_inches='tight')
print("Saved fig_comparison_perclass.png")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — Model size (horizontal bars, log scale) with PR-AUC at bar end
# ═════════════════════════════════════════════════════════════════════════════
SIZE_ORDER = ['GTBAD', 'MAAT', 'PC-Flow', 'OC-SVM', 'BOCD']  # top -> bottom
fig3, ax = plt.subplots(figsize=(8.2, 4.2))
yb = np.arange(len(SIZE_ORDER))[::-1]

for yi, m in zip(yb, SIZE_ORDER):
    ax.barh(yi, SIZE[m], height=0.6, color=COLORS[m], zorder=3,
            edgecolor='white', linewidth=0.6)
    ax.text(SIZE[m] * 1.4, yi, f'PR-AUC {macro_mean[m]:.3f}',
            va='center', ha='left', fontsize=10,
            fontweight='bold' if m == 'PC-Flow' else 'normal',
            color=COLORS[m] if m == 'PC-Flow' else '#333333')

ax.set_xscale('log')
ax.set_xlim(10, 1.2e7)
ax.set_yticks(yb)
ax.set_yticklabels([LABELS[m].replace('\n', ' ') for m in SIZE_ORDER])
ax.set_xlabel('Model size (number of parameters, log scale)')
ax.grid(axis='x', ls='--', color='#cccccc', alpha=0.6, zorder=0)
ax.set_axisbelow(True)

# 43x callout between PC-Flow and GTBAD
ax.annotate('', xy=(20124, yb[SIZE_ORDER.index('PC-Flow')] + 0.42),
            xytext=(869769, yb[SIZE_ORDER.index('GTBAD')] - 0.42),
            arrowprops=dict(arrowstyle='<->', color='#888888', lw=1.3))
ax.text(1.3e5, 1.5, '43$\\times$ larger\nfor the same score', ha='center',
        va='center', fontsize=9.5, color='#555555', style='italic')

fig3.text(0.5, -0.02,
          'Isolation Forest is omitted: its size is counted in trees, not in a comparable parameter count.',
          ha='center', fontsize=8.5, color='#777777', style='italic')

fig3.tight_layout()
fig3.savefig(OUT / 'fig_comparison_size.png', dpi=300, bbox_inches='tight')
print("Saved fig_comparison_size.png")

plt.close('all')
print("Done.")
