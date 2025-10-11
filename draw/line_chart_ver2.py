import json
import numpy as np
import matplotlib.pyplot as plt

# ─── Load saved data ────────────────────────────────────────────────────────────
with open("data.json", "r") as f:
    data = json.load(f)

# ─── Line styles for each variant ───────────────────────────────────────────────
styles = {
    "Full model (Ours)": ("black", "-"),
    "– SCA":             ("red",   "--"),
    "– FA":              ("blue",  "-."),
    "No pretraining":    ("gray",  "--"),
}

# ─── Compute object indices ────────────────────────────────────────────────────
# assume all lists have the same length
first = next(iter(data.values()))
num_objects = len(first["Point Level AUROC"])
object_indices = np.arange(1, num_objects + 1)

# ─── Y‑axis bounds per metric ─────────────────────────────────────────────────
metric_bounds = {
    "Point Level AUROC":  (0.3,  0.9),
    "Point Level AUPR":   (0.0,  0.3),
    "Object Level AUROC": (0.3,  0.95),
    "Object Level AUPR":  (0.3,  0.95),
}

# ─── Plotting function ─────────────────────────────────────────────────────────
def plot_metric(metric_name, ylabel, title=None):
    plt.figure(figsize=(12, 4))
    for label, metrics in data.items():
        values = np.array(metrics[metric_name])
        color, linestyle = styles[label]
        plt.plot(object_indices, values, label=label, color=color, linestyle=linestyle)
    plt.xlabel("Object Index")
    plt.ylabel(ylabel)
    #plt.title(title or ylabel)
    ymin, ymax = metric_bounds.get(metric_name, (0.0, 1.0))
    plt.ylim(ymin, ymax)
    plt.grid(True)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.0),
               fontsize="medium", ncol=len(styles))
    plt.tight_layout()
    plt.show()

# ─── Generate all four plots ───────────────────────────────────────────────────
plot_metric("Point Level AUROC", "Point Level AUROC", "")
plot_metric("Point Level AUPR", "Point Level AUPR", "")
plot_metric("Object Level AUROC", "Object Level AUROC", "")
plot_metric("Object Level AUPR", "Object Level AUPR", "")