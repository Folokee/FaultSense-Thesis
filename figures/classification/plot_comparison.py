"""
Comparison plots for the Task B Results and Discussion section.

  - Figure 1: two bar charts — (a) Macro F1  (b) Balanced Accuracy — all three classifiers.
  - Figure 2: grouped bars per fault class (per-class F1), legend below.

Colour palette: RColorBrewer Set2 (colourblind-safe, warm/muted tones —
deliberately different from the Wong palette used in the Task A figures).

Run from the FaultSense-Thesis root directory:
    python figures/classification/plot_comparison.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent

# ── One consistent colour per model (Set2, colourblind-safe) ─────────────────
COLORS = {
    'LightGBM':   '#fc8d62',   # salmon-orange
    'CatBoost':   '#8da0cb',   # periwinkle blue
    'ExtraTrees': '#66c2a5',   # teal-green (winner)
}
ORDER = ['ExtraTrees', 'CatBoost', 'LightGBM']   # winner first

# ── Verified values (kfold_summary JSON files) ────────────────────────────────
macro_f1_mean = {'LightGBM': 0.934, 'CatBoost': 0.948, 'ExtraTrees': 0.959}
macro_f1_std  = {'LightGBM': 0.098, 'CatBoost': 0.090, 'ExtraTrees': 0.078}

bal_acc_mean  = {'LightGBM': 0.925, 'CatBoost': 0.932, 'ExtraTrees': 0.943}
bal_acc_std   = {'LightGBM': 0.131, 'CatBoost': 0.124, 'ExtraTrees': 0.113}

# Per-class F1  (order: SC, Degradation, OC, Shadowing)
per_class_mean = {
    'LightGBM':   [0.886, 0.860, 0.998, 0.994],
    'CatBoost':   [0.921, 0.893, 0.986, 0.995],
    'ExtraTrees': [0.922, 0.922, 0.998, 0.995],
}
per_class_std = {
    'LightGBM':   [0.145, 0.242, 0.002, 0.011],
    'CatBoost':   [0.148, 0.208, 0.027, 0.010],
    'ExtraTrees': [0.147, 0.157, 0.002, 0.009],
}

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
})


def style_axis(ax, ymax=1.08):
    ax.set_ylim(0, ymax)
    ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.grid(axis='y', ls='--', color='#cccccc', alpha=0.6, zorder=0)
    ax.set_axisbelow(True)


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Macro F1 vs Balanced Accuracy  (two bar charts)
# ═════════════════════════════════════════════════════════════════════════════
fig1, (axA, axB) = plt.subplots(1, 2, figsize=(10.0, 4.4), sharey=True)
x = np.arange(len(ORDER))
cols = [COLORS[m] for m in ORDER]

for ax, mean, std, title in [
    (axA, macro_f1_mean, macro_f1_std,  '(a) Macro F1'),
    (axB, bal_acc_mean,  bal_acc_std,   '(b) Balanced Accuracy'),
]:
    bars = ax.bar(x, [mean[m] for m in ORDER], width=0.55, color=cols,
                  yerr=[std[m] for m in ORDER], capsize=4,
                  error_kw=dict(ecolor='#444444', elinewidth=1.1, capthick=1.1),
                  zorder=3, edgecolor='white', linewidth=0.6)
    style_axis(ax)
    ax.set_title(title, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels([m for m in ORDER])
    for m, b in zip(ORDER, bars):
        ax.text(b.get_x() + b.get_width() / 2, mean[m] + std[m] + 0.025,
                f'{mean[m]:.3f}', ha='center', va='bottom', fontsize=9)

axA.set_ylabel('Score')

fig1.tight_layout()
fig1.savefig(OUT / 'fig_classification_macro.png', dpi=300, bbox_inches='tight')
print("Saved fig_classification_macro.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Per-class F1  (grouped bars, Degradation highlighted, legend below)
# ═════════════════════════════════════════════════════════════════════════════
CLASS_TITLES = ['Short-Circuit', 'Degradation', 'Open-Circuit', 'Shadowing']
HARD = 1   # Degradation index

n_mod = len(ORDER)
group_w = 0.72
bw = group_w / n_mod

fig2, ax = plt.subplots(figsize=(10.0, 4.6))
xc = np.arange(len(CLASS_TITLES))

for j, m in enumerate(ORDER):
    offs = (j - (n_mod - 1) / 2) * bw
    ax.bar(xc + offs, [per_class_mean[m][c] for c in range(4)], width=bw * 0.90,
           color=COLORS[m], label=m,
           yerr=[per_class_std[m][c] for c in range(4)], capsize=2,
           error_kw=dict(ecolor='#555555', elinewidth=0.8, capthick=0.8),
           zorder=3, edgecolor='white', linewidth=0.4)

# Highlight Degradation
ax.axvspan(xc[HARD] - 0.5, xc[HARD] + 0.5, color='#fff3d6', zorder=0)
ax.text(xc[HARD], 1.045, 'hardest class across all models',
        ha='center', va='bottom', fontsize=9, color='#b07400', style='italic')

ax.set_ylim(0, 1.08)
ax.set_yticks(np.arange(0, 1.01, 0.2))
ax.grid(axis='y', ls='--', color='#cccccc', alpha=0.6, zorder=0)
ax.set_axisbelow(True)
ax.set_ylabel('Per-class F1 (5-fold mean±std)')
ax.set_xticks(xc)
ax.set_xticklabels([f'{t}\n(cls {i + 1})' for i, t in enumerate(CLASS_TITLES)], fontsize=11)
ax.set_xlim(-0.5, len(CLASS_TITLES) - 0.5)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3,
          frameon=False, fontsize=10, handlelength=1.4, columnspacing=1.6)

fig2.tight_layout()
fig2.savefig(OUT / 'fig_classification_perclass.png', dpi=300, bbox_inches='tight')
print("Saved fig_classification_perclass.png")

plt.close('all')
print("Done.")
