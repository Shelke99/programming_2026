import numpy as np
import matplotlib.pyplot as plt


weight_f = np.array([48, 53, 63, 75])
lift_f = np.array([185, 225, 242.5, 245])

weight_m = np.array([56, 62, 69, 77, 85, 94, 105])
lift_m = np.array([305, 325, 357.5, 376.5, 390, 405, 425])

for name, w, L in [("Female", weight_f, lift_f), ("Male", weight_m, lift_m)]:
    k = L / w**(2/3)  # k = lift / W^(2/3)
    k_mean = k.mean()
    pred = k_mean * w**(2/3)
    print(name)
    print("k values:", np.round(k, 2))
    print("mean k:", round(k_mean, 2), "spread (std/mean) = %.1f%%" % (100 * k.std(ddof=1) / k_mean))
    print("predicted lift:", np.round(pred, 1))
    print("error %:", np.round(100 * (pred - L) / L, 1))
    print("lift - weight:", L - w)  # the contest's own scoring rule

# Plot
plt.figure(figsize=(7, 4.5))
for w, L, col, lab in [(weight_f, lift_f, 'tab:red', 'Female'), (weight_m, lift_m, 'tab:blue', 'Male')]:
    k_mean = np.mean(L / w**(2/3))
    xs = np.linspace(w.min(), w.max(), 100)
    plt.scatter(w, L, color=col, label=lab + " data")
    plt.plot(xs, k_mean * xs**(2/3), '--', color=col, label=f"{lab}: L = {k_mean:.2f} W^(2/3)")

plt.xlabel("Body weight W (kg)")
plt.ylabel("Winning lift L (kg)")
plt.title("Lift vs body weight")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("lift_plot.png", dpi=150)
