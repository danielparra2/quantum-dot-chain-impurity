import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import ConnectionPatch

# Configuración de estilo académico (Tipo LaTeX/PGFPlot)
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "mathtext.fontset": "cm"
})

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# 1. Definición del dominio circular global (R = 200 nm)
R_ext = 200
theta = np.linspace(0, 2*np.pi, 100)
x_ext = R_ext * np.cos(theta)
y_ext = R_ext * np.sin(theta)

# Dibujar frontera exterior
ax.plot(x_ext, y_ext, color='#003399', lw=2, label='Frontera del Dominio')

# Simulación visual de malla triangular no uniforme con smoothing
# Generar nodos concéntricos con densidad radial exponencial para el smoothing
r_rings = np.logspace(np.log10(0.2), np.log10(R_ext), 25)
nodes_x = [0]
nodes_y = [0]

for r in r_rings:
    n_pts = int(max(6, 2 * np.pi * r / (r**0.6)))
    t = np.linspace(0, 2*np.pi, n_pts, endpoint=False)
    nodes_x.extend(r * np.cos(t))
    nodes_y.extend(r * np.sin(t))

from scipy.spatial import Delaunay
tri = Delaunay(np.column_stack([nodes_x, nodes_y]))

# Dibujar la malla exterior (Azul)
ax.triplot(tri.points[:,0], tri.points[:,1], tri.simplices, color='#1e90ff', lw=0.4, alpha=0.8)

# Indicador de Condición de Frontera Dirichlet \psi = 0
ax.annotate(r'$\psi(\mathbf{r}) = 0$ (Dirichlet)', 
            xy=(R_ext * np.cos(np.pi/4), R_ext * np.sin(np.pi/4)), 
            xytext=(R_ext + 30, R_ext + 20),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
            fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.8))

# Marcar el centro de la impureza
ax.plot(0, 0, 'ro', markersize=4, label='Impureza donadora')

ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-R_ext - 40, R_ext + 120)
ax.set_ylim(-R_ext - 20, R_ext + 60)

# 2. Creación del Inset (Lupa / Zoom de la Sub-malla Hiper-fina)
axins = ax.inset_axes([0.65, 0.1, 0.35, 0.35])

# Sub-malla extremadamente fina en la lupa
r_rings_zoom = np.linspace(0.001, 1.0, 15)
nodes_xz, nodes_yz = [0], [0]
for r in r_rings_zoom:
    n_pts = int(max(8, 2 * np.pi * r * 20))
    t = np.linspace(0, 2*np.pi, n_pts, endpoint=False)
    nodes_xz.extend(r * np.cos(t))
    nodes_yz.extend(r * np.sin(t))

tri_zoom = Delaunay(np.column_stack([nodes_xz, nodes_yz]))
axins.triplot(tri_zoom.points[:,0], tri_zoom.points[:,1], tri_zoom.simplices, color='#004080', lw=0.3)
axins.plot(0, 0, 'ro', markersize=3)

# Detalle de la lupa
axins.set_xlim(-1, 1)
axins.set_ylim(-1, 1)
axins.set_xticks([])
axins.set_yticks([])
axins.set_title('Sub-malla Hiper-fina ($0.001$)', fontsize=9, pad=4)

# Borde circular para la lupa
circle_patch = patches.Circle((0, 0), 1, transform=axins.transData, fill=False, color='black', lw=1.5)
axins.add_patch(circle_patch)

# Conectar la lupa con el foco central
rect_zoom = patches.Circle((0, 0), 15, fill=False, color='black', ls='--', lw=1)
ax.add_patch(rect_zoom)

con = ConnectionPatch(xyA=(0, 15), xyB=(-1, 0), coordsA="data", coordsB="data",
                      axesA=ax, axesB=axins, color="black", ls="--", lw=0.8)
ax.add_artist(con)

plt.tight_layout()
plt.savefig("Punto_Cuantico_Mallafff_Zoom.png", dpi=300, bbox_inches='tight')
plt.show()