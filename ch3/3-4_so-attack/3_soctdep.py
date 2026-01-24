import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("saved-checkpoint/k0b1-idx0.pkl", "rb") as f: cp = pickle.load(f)

k_ref = 2
nn_s = 20000
nn_e = 400000
step = 20000

corr = [[], [], [], [], [], [], [], []]

for nn in range(nn_s, nn_e+1, step):
    rho = np.abs(cp[nn]['rho'])
    for k, ct in enumerate(rho):
        corr[k].append(max(ct))

plt.figure(figsize=(6,4))
x_axis = range(nn_s,nn_e+1,step)

plt.plot(x_axis, corr[0], color = "lightgray", label="Wrong keys")
plt.plot(x_axis, corr[1], color = "lightgray")
plt.plot(x_axis, corr[2], color = "lightgray")
plt.plot(x_axis, corr[3], color = "lightgray")
plt.plot(x_axis, corr[4], color = "lightgray")
plt.plot(x_axis, corr[5], color = "lightgray")
plt.plot(x_axis, corr[6], color = "lightgray")
plt.plot(x_axis, corr[7], color = "lightgray")

plt.plot(x_axis, corr[k_ref], label="Correct key")
plt.xlabel("Number of traces")
plt.ylabel("Absolute correlation")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/correlations.png")
