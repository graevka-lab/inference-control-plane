import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

# --- Configuration ---
T = 300
t = np.linspace(0, 40, T)
output_file = "ICP_Thermodynamics.gif"

print("Initializing Thermodynamic Simulation...")

# --- Synthetic Data Generation ---
# Entropy: Exponential growth without ICP, Bounded with ICP
H_no = np.exp(0.06 * t)
H_icp = np.minimum(H_no, 5)

# Coherence (C) & Meta-Uncertainty (U)
# Coherence drops as entropy rises, but ICP maintains it
C = np.clip(1.1 - 0.15 * H_icp + 0.05*np.random.randn(T), 0, 1)
# Uncertainty pulses (Halo effect)
U = 0.25 + 0.1*np.sin(0.4 * t)

# Multi-agent phases (3 agents)
agents = 3
phi = np.zeros((agents, T))
for i in range(1, T):
    # Random drift + Phase Locking for Agent 1 & 0
    phi[:, i] = phi[:, i-1] + 0.12 + 0.04*np.random.randn(agents)
phi[1] = phi[0] + 0.04*np.sin(0.5 * t)

# --- Visualization Setup ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Axis limits
ax.set_xlim(0, 5)
ax.set_ylim(0, 1)
ax.set_zlim(0, 0.5)

# Labels
ax.set_xlabel("Entropy (H)")
ax.set_ylabel("Coherence (C)")
ax.set_zlabel("Meta-Uncertainty (U)")
ax.set_title("ICP: Phase Space of Intelligence")

# Lines initialization
line_icp, = ax.plot([], [], [], lw=2, color="green", label="With ICP (Stabilized)")
line_no, = ax.plot([], [], [], lw=2, color="red", alpha=0.5, label="Without ICP (Divergent)")
halo, = ax.plot([], [], [], "o", color="blue", alpha=0.6, label="Meta-Cognitive State")

ax.legend()

# --- Animation Function ---
def animate(i):
    # Update trajectories
    line_icp.set_data(H_icp[:i], C[:i])
    line_icp.set_3d_properties(U[:i])
    
    line_no.set_data(H_no[:i], 0.5*C[:i])
    line_no.set_3d_properties(U[:i])

    # Update Halo (Pulsing effect based on Uncertainty)
    halo.set_data([H_icp[i]], [C[i]])
    halo.set_3d_properties([U[i]])
    # Size pulses with uncertainty
    halo.set_markersize(15 + 20*np.sin(i*0.15))
    
    if i % 50 == 0:
        print(f"Rendering frame {i}/{T}...")

    return line_icp, line_no, halo

# --- Render & Save ---
print(f"Generating animation: {output_file}...")
ani = FuncAnimation(fig, animate, frames=T, interval=50)
ani.save(output_file, writer=PillowWriter(fps=20))

print("Done. Visualization saved.")