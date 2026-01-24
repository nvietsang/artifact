import pickle
import numpy as np
import matplotlib.pyplot as plt


with open("saved-checkpoint/k0b1-idx0.pkl", "rb") as f: cp = pickle.load(f)

k_ref = 2
nn = 300000
rho = np.abs(cp[nn]['rho'])



plt.plot(rho[0], color = "lightgray", label="Wrong keys")
# plt.plot(rho[1], color = "lightgray")
plt.plot(rho[2], color = "lightgray")
plt.plot(rho[3], color = "lightgray")
plt.plot(rho[4], color = "lightgray")
plt.plot(rho[5], color = "lightgray")
plt.plot(rho[6], color = "lightgray")
plt.plot(rho[7], color = "lightgray")

plt.plot(rho[k_ref], label="Correct key")
plt.xlabel("Sample")
plt.ylabel("Absolute correlation")
plt.legend()
plt.savefig("outputs/peak.png")

plt.clf()
nt_s = 2820
nt_e = 2880
plt.plot(rho[0], color = "lightgray", label="Wrong keys")
plt.plot(rho[1], color = "lightgray")
# plt.plot(rho[2], color = "lightgray")
plt.plot(rho[3], color = "lightgray")
plt.plot(rho[4], color = "lightgray")
plt.plot(rho[5], color = "lightgray")
plt.plot(rho[6], color = "lightgray")
plt.plot(rho[7], color = "lightgray")
    
plt.plot(rho[k_ref], label="Correct key")
plt.xlim((nt_s,nt_e))
plt.xlabel("Sample")
plt.ylabel("Absolute correlation")
plt.legend()
plt.savefig("outputs/peak-zoomed.png")