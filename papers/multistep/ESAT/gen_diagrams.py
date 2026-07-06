#!/usr/bin/env python3
"""Generate 4 annotated matplotlib diagrams for ESAT 22 May flashcards."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ─── Diagram 1: Semicircle-in-Square ───────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(4.5, 4.5), dpi=150)
# Square
sq = patches.Rectangle((0, 0), 6, 6, linewidth=2, edgecolor='#1d1d1f', facecolor='#e8f4f8')
ax.add_patch(sq)
# Semicircle (cut from right side, curving left into square)
theta = np.linspace(-np.pi/2, np.pi/2, 100)
xc, yc, r = 6, 3, 3
sx = xc - r * np.cos(theta)  # curves leftward
sy = yc + r * np.sin(theta)
ax.fill(sx, sy, color='#fff5f5', edgecolor='#c0392b', linewidth=2)
ax.plot(sx, sy, color='#c0392b', linewidth=2)
# Shading of remaining area (left part)
ax.fill_betweenx(np.linspace(0, 6, 100), 0, np.minimum(6, 6 - 3*np.cos(np.linspace(-np.pi/2, np.pi/2, 100)).repeat(1)), alpha=0)
# Labels
ax.annotate('m', xy=(3, 0), fontsize=13, ha='center', va='top', fontweight='bold', color='#1d1d1f')
ax.annotate('m', xy=(0, 3), fontsize=13, ha='right', va='center', fontweight='bold', color='#1d1d1f')
ax.annotate('r = m/2', xy=(5.5, 5), fontsize=11, ha='center', color='#c0392b', fontstyle='italic')
ax.annotate('remaining\n= 100 cm²', xy=(2, 3), fontsize=12, ha='center', va='center', color='#1d1d1f', fontweight='bold')
# Arrow showing radius
ax.annotate('', xy=(6, 3), xytext=(3, 3), arrowprops=dict(arrowstyle='<->', color='#c0392b', lw=1.5))
ax.set_xlim(-0.5, 7)
ax.set_ylim(-0.5, 7)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Semicircle cut from square', fontsize=13, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'diagram_semicircle.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ diagram_semicircle.png")

# ─── Diagram 2: Similar Triangles ─────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(6, 5), dpi=150)
# Main triangle PQR: Q at origin (right angle), P up, R right
Q = np.array([0, 0])
P = np.array([0, 4])
R = np.array([2, 0])
triangle = plt.Polygon([Q, P, R], fill=True, facecolor='#e8f4f8', edgecolor='#1d1d1f', linewidth=2)
ax.add_patch(triangle)
# Hypotenuse PR
ax.plot([P[0], R[0]], [P[1], R[1]], 'k-', linewidth=2)
# Foot of perpendicular T on PR
# Direction PR
PR = R - P
t_param = np.dot(Q - P, PR) / np.dot(PR, PR)
T = P + t_param * PR
# Perpendicular from Q to T
ax.plot([Q[0], T[0]], [Q[1], T[1]], 'b--', linewidth=1.5, label='x (altitude)')
# Right angle at Q
sq_size = 0.25
sq_pts = [Q, Q + [sq_size, 0], Q + [sq_size, sq_size], Q + [0, sq_size]]
sq_patch = plt.Polygon(sq_pts, fill=False, edgecolor='#1d1d1f', linewidth=1)
ax.add_patch(sq_patch)
# Right angle at T
direction_QT = (T - Q) / np.linalg.norm(T - Q)
direction_TR = (R - T) / np.linalg.norm(R - T)
sq_t_pts = [T, T + direction_QT*0.2, T + direction_QT*0.2 + direction_TR*0.2, T + direction_TR*0.2]
ax.add_patch(plt.Polygon(sq_t_pts, fill=False, edgecolor='#1d1d1f', linewidth=1))
# Angle arcs (single arc at P, double arc at R)
from matplotlib.patches import Arc
# Angle at P
angle_P = np.degrees(np.arctan2(R[1]-P[1], R[0]-P[0]))
ax.add_patch(Arc(P, 0.6, 0.6, angle=0, theta1=angle_P-30, theta2=angle_P+30, color='#0071e3', linewidth=1.5))
# Angle at R
angle_R_from_RP = np.degrees(np.arctan2(P[1]-R[1], P[0]-R[0]))
ax.add_patch(Arc(R, 0.6, 0.6, angle=0, theta1=angle_R_from_RP-30, theta2=angle_R_from_RP+30, color='#34c759', linewidth=1.5))
ax.add_patch(Arc(R, 0.45, 0.45, angle=0, theta1=angle_R_from_RP-30, theta2=angle_R_from_RP+30, color='#34c759', linewidth=1.5))
# Labels
offset = 0.3
ax.annotate('P', P + [-offset, offset], fontsize=14, fontweight='bold', ha='center')
ax.annotate('Q', Q + [-offset, -offset], fontsize=14, fontweight='bold', ha='center')
ax.annotate('R', R + [offset, -offset], fontsize=14, fontweight='bold', ha='center')
ax.annotate('T', T + [0.2, -0.3], fontsize=12, fontweight='bold', ha='center', color='#0071e3')
# Side labels
ax.annotate('PQ = 20', xy=(-0.15, 2), fontsize=11, ha='right', color='#1d1d1f', rotation=90)
ax.annotate('RQ = 10', xy=(1, -0.25), fontsize=11, ha='center', color='#1d1d1f')
ax.annotate('PR = 10√5', xy=(1.2, 2.5), fontsize=11, ha='left', color='#1d1d1f', rotation=-63)
ax.annotate('x', xy=(0.45, 1.5), fontsize=13, ha='left', color='#0071e3', fontweight='bold')
ax.set_xlim(-1, 3.5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Similar triangles — altitude from right angle', fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'diagram_similar_triangles.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ diagram_similar_triangles.png")

# ─── Diagram 3: 3D Pythagoras (Unit Cube) ──────────────────────
fig, ax = plt.subplots(1, 1, figsize=(6, 5), dpi=150, subplot_kw={'projection': '3d'})
# Cube vertices
v = {
    'O': (0,0,0), 'A': (1,0,0), 'B': (1,1,0), 'C': (0,1,0),
    'D': (0,0,1), 'E': (1,0,1), 'F': (1,1,1), 'G': (0,1,1)
}
# Draw cube edges
edges = [('O','A'),('A','B'),('B','C'),('C','O'),  # bottom
         ('D','E'),('E','F'),('F','G'),('G','D'),  # top
         ('O','D'),('A','E'),('B','F'),('C','G')]  # vertical
for s, e in edges:
    ax.plot3D(*zip(v[s], v[e]), 'k-', linewidth=1.2)
# Midpoint of opposite face (face EFGD → midpoint = (0.5, 0.5, 1))
M = (0.5, 0.5, 1)
# Dashed line from O to M
ax.plot3D(*zip(v['O'], M), 'r--', linewidth=2.5, label='y (vertex to midpoint)')
# Intermediate point on base: (0.5, 0, 0) → no, let's trace: O→(1,0,0)→(1,0.5,0)→...
# Actually: Step 1 diagonal across base: O to (1, 0.5, 0) — wait, the guide says
# vertex (0,0,0) to midpoint of opposite face (1, 0.5, 0.5)
# Step 1: x = sqrt(1^2 + (0.5)^2) — diagonal in base plane from (0,0,0) to (1, 0.5, 0)
# Step 2: y = sqrt(x^2 + 0.5^2) — from (1,0.5,0) to (1,0.5,0.5)
P1 = (1, 0.5, 0)
P2 = (1, 0.5, 0.5)  # This is the midpoint of opposite face
# Re-do: opposite face is the face at x=1 (EFG... no). 
# Let me re-read: "vertex to midpoint of opposite face"
# Vertex (0,0,0), opposite face is the face not containing O that is "opposite" = face at x=1? 
# Actually for a cube, the face opposite to vertex O=(0,0,0) is the face containing E,F... 
# which is x=1 face. Midpoint of x=1 face = (1, 0.5, 0.5). That matches the guide.
# Step 1: from O, go along x=1 direction (length 1) and y=0.5 direction → point (1, 0.5, 0)
#   x = sqrt(1^2 + 0.5^2) = sqrt(5/4)
# Step 2: from (1, 0.5, 0), go up z=0.5 → (1, 0.5, 0.5)
#   y = sqrt(x^2 + 0.5^2) = sqrt(5/4 + 1/4) = sqrt(6/4)
ax.plot3D(*zip(v['O'], P1), 'b--', linewidth=1.5, alpha=0.7)
ax.plot3D(*zip(P1, P2), 'g--', linewidth=1.5, alpha=0.7)
# Mark points
for pt, lbl, off in [(v['O'],'O',(-0.1,-0.1,-0.1)), (P1,'(1,½,0)',(0.1,0.1,-0.15)), 
                      (P2,'M (1,½,½)',(0.1,0.1,0.1))]:
    ax.scatter3D(*pt, s=30, c='red' if lbl.startswith('M') else 'black', zorder=5)
    ax.text(pt[0]+off[0], pt[1]+off[1], pt[2]+off[2], lbl, fontsize=9, fontweight='bold')
# Labels for intermediate steps
ax.text(0.5, 0.25, 0, '  x=√5/2', fontsize=9, color='blue', fontstyle='italic')
ax.text(1.05, 0.55, 0.25, '  ½', fontsize=9, color='green')
ax.text(0.3, 0.15, 0.35, '  y=√6/2', fontsize=10, color='red', fontweight='bold')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(-0.2, 1.3)
ax.set_ylim(-0.2, 1.3)
ax.set_zlim(-0.2, 1.3)
ax.set_title('3D Pythagoras — vertex to face midpoint', fontsize=12, fontweight='bold', pad=10)
ax.view_init(elev=20, azim=-60)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'diagram_3d_pythagoras.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ diagram_3d_pythagoras.png")

# ─── Diagram 4: Clock Face at 9:45 ─────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(5, 5), dpi=150)
# Clock circle
circle = plt.Circle((0, 0), 1, fill=True, facecolor='#f0f0f7', edgecolor='#1d1d1f', linewidth=2)
ax.add_patch(circle)
# Hour marks
for i in range(12):
    angle = np.pi/2 - i * np.pi/6  # 12 at top
    x1, y1 = 0.85*np.cos(angle), 0.85*np.sin(angle)
    x2, y2 = 0.95*np.cos(angle), 0.95*np.sin(angle)
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)
    # Numbers
    xn, yn = 0.75*np.cos(angle), 0.75*np.sin(angle)
    num = 12 if i == 0 else i
    ax.text(xn, yn, str(num), fontsize=10, ha='center', va='center', fontweight='bold')
# Minute hand at 9 position (270° from 12 clockwise = pointing left)
# 9:45 → minute at 9 → angle = 270° clockwise from 12 = -90° from x-axis... 
# In standard math: 12 is at 90°, 3 is at 0°, 6 at -90°, 9 at 180°
min_angle = np.pi  # 9 o'clock position
ax.plot([0, 0.7*np.cos(min_angle)], [0, 0.7*np.sin(min_angle)], 'k-', linewidth=3, solid_capstyle='round')
# Hour hand at 9.75 hours → 9 + 45/60 = 9.75 hours
# Each hour = 30°, so 9.75 * 30 = 292.5° from 12 clockwise
# In standard math angle: 90° - 292.5° = -202.5° = 157.5°
hour_angle_deg = 90 - 9.75 * 30
hour_angle = np.radians(hour_angle_deg)
ax.plot([0, 0.5*np.cos(hour_angle)], [0, 0.5*np.sin(hour_angle)], 'b-', linewidth=4, solid_capstyle='round')
# Arc showing the angle between hands
arc = Arc((0,0), 0.4, 0.4, angle=0, theta1=np.degrees(hour_angle), theta2=np.degrees(min_angle), 
          color='#c0392b', linewidth=2, linestyle='--')
ax.add_patch(arc)
# Angle label
mid_angle = (hour_angle + min_angle) / 2
ax.text(0.3*np.cos(mid_angle), 0.3*np.sin(mid_angle), '22.5°', fontsize=11, ha='center', va='center', 
        color='#c0392b', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#c0392b', alpha=0.9))
# Center dot
ax.plot(0, 0, 'ro', markersize=6)
# Labels
ax.text(0.75*np.cos(min_angle), 0.75*np.sin(min_angle)-0.12, 'min', fontsize=8, ha='center', color='#666')
ax.text(0.55*np.cos(hour_angle), 0.55*np.sin(hour_angle)+0.1, 'hour', fontsize=8, ha='center', color='blue')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Clock at 9:45 — angle between hands', fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'diagram_clock.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ diagram_clock.png")

print("\nAll 4 diagrams generated successfully!")
