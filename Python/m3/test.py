import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import numpy as np
from matplotlib.widgets import Button, Slider

# ==========================================
# 1. DÉFINITION DE LA CARTE
# ==========================================

positions = {
    'hub': (0, 0),
    'roof1': (2, 4),      
    'roof2': (5, 3),      
    'corridorA': (3, 2),  
    'tunnelB': (6, 2),    
    'goal': (-9, 5),       
    'obstacleX': (5, 5)   
}

aretes = [
    ('hub', 'roof1'),
    ('hub', 'corridorA'),
    ('roof1', 'roof2'),
    ('roof2', 'goal'),
    ('corridorA', 'tunnelB'),
    ('tunnelB', 'goal')
]

couleurs_noeuds = {
    'hub': 'lightgreen',
    'roof1': 'salmon',      
    'roof2': 'skyblue',     
    'corridorA': 'limegreen',
    'tunnelB': 'lightcoral',
    'goal': 'gold',         
    'obstacleX': 'lightgray'
}

# ==========================================
# 2. CHEMINS DES DRONES (Solution CBS)
# ==========================================

chemins_drones = {
    'D1': ['hub', 'corridorA', 'tunnelB', 'goal', 'goal', 'goal'],
    'D2': ['hub', 'corridorA', 'tunnelB', 'goal', 'goal', 'goal'],
    'D3': ['hub', 'roof1', 'roof2', 'goal', 'goal', 'goal'],
    'D4': ['hub', 'hub', 'roof1', 'roof2', 'goal', 'goal'],       # Attend 1 tour
    'D5': ['hub', 'hub', 'hub', 'roof1', 'roof2', 'goal']         # Attend 2 tours
}

couleurs_drones = {
    'D1': 'darkred',
    'D2': 'darkblue',
    'D3': 'darkgreen',
    'D4': 'orange',
    'D5': 'purple'
}

MAX_T = len(chemins_drones['D1']) - 1  # = 5

# ==========================================
# 3. CONFIGURATION DE L'INTERFACE
# ==========================================

fig = plt.figure(figsize=(13, 8))

# Zone de la carte (grande)
ax_map = plt.axes([0.05, 0.25, 0.7, 0.70])
# Zone pour les boutons et le slider
ax_slider = plt.axes([0.05, 0.15, 0.6, 0.03])
ax_prev = plt.axes([0.70, 0.10, 0.08, 0.06])
ax_play = plt.axes([0.80, 0.10, 0.08, 0.06])
ax_next = plt.axes([0.90, 0.10, 0.08, 0.06])
# Zone pour le panneau d'analyse (texte)
ax_stats = plt.axes([0.05, 0.03, 0.70, 0.06])
ax_stats.axis('off')

# Construction du graphe
G = nx.Graph()
G.add_edges_from(aretes)
G.add_node('obstacleX')

# Variables globales
current_time = 0
timer = None
is_playing = False

# Widgets
slider = Slider(ax_slider, 'Temps', 0, MAX_T, valinit=0, valfmt='%i', valstep=1)
btn_prev = Button(ax_prev, '◀ Préc')
btn_play = Button(ax_play, '▶ Play')
btn_next = Button(ax_next, 'Suiv ▶')

# ==========================================
# 4. FONCTION DE DESSIN (Analyse incluse)
# ==========================================

def draw_step(t):
    ax_map.clear()
    ax_stats.clear()
    ax_stats.axis('off')
    
    # --- Dessin des arêtes ---
    for u, v in aretes:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        if (u == 'corridorA' and v == 'tunnelB') or (u == 'tunnelB' and v == 'corridorA'):
            ax_map.plot([x1, x2], [y1, y2], 'k-', lw=5, zorder=0, label='_nolegend_')
            # Ajout d'une petite indication "Capacité lien"
            mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
            ax_map.text(mid_x, mid_y-0.3, 'Capacité lien: 2', ha='center', fontsize=8, style='italic', color='darkblue', 
                        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', alpha=0.7))
        else:
            ax_map.plot([x1, x2], [y1, y2], 'gray', lw=2, zorder=0, label='_nolegend_')
    
    # --- Dessin des nœuds ---
    for noeud, (x, y) in positions.items():
        couleur = couleurs_noeuds[noeud]
        size = 600 if noeud in ['hub', 'goal'] else 400
        ax_map.scatter(x, y, c=couleur, s=size, zorder=1, edgecolors='black', linewidth=2)
        ax_map.text(x, y-0.35, noeud, ha='center', va='top', fontsize=9, weight='bold')
        
        # Annotation des contraintes sur la carte
        if noeud == 'corridorA':
            ax_map.text(x, y-0.65, 'Max 2 drones', ha='center', fontsize=8, style='italic', color='darkgreen', weight='bold')
        if noeud == 'roof1':
            ax_map.text(x, y+0.35, '⛔ Restricted', ha='center', fontsize=8, style='italic', color='red')
    
    # --- Comptage des drones sur les nœuds critiques (pour l'analyse) ---
    counts_corridor = 0
    counts_roof1 = 0
    counts_goal = 0
    positions_drones = {}
    
    for nom, chemin in chemins_drones.items():
        noeud_actuel = chemin[t] if t < len(chemin) else chemin[-1]
        positions_drones[nom] = noeud_actuel
        
        if noeud_actuel == 'corridorA':
            counts_corridor += 1
        if noeud_actuel == 'roof1':
            counts_roof1 += 1
        if noeud_actuel == 'goal':
            counts_goal += 1
    
    # --- Dessin des drones (cercles) ---
    for nom, noeud in positions_drones.items():
        x, y = positions[noeud]
        ax_map.scatter(x, y, c=couleurs_drones[nom], s=250, zorder=3, edgecolors='white', linewidth=2.5)
        ax_map.text(x, y+0.25, nom, ha='center', va='bottom', fontsize=9, weight='bold', color='white',
                    bbox=dict(boxstyle="round,pad=0.1", facecolor='black', alpha=0.6))
    
    # --- Mise en page de la carte ---
    ax_map.set_title(f"Simulation MAPF - Temps t = {t}", fontsize=14, pad=15)
    ax_map.set_xlim(-1.5, 11)
    ax_map.set_ylim(-1.5, 7)
    ax_map.set_aspect('equal')
    ax_map.axis('off')
    
    # --- Panneau d'analyse (statistiques) ---
    # Vérification du respect des contraintes
    status_corridor = "✅ OK" if counts_corridor <= 2 else "❌ SURCHARGÉ !"
    status_roof1 = "⚠️ Détour coûteux" if counts_roof1 > 0 else "✅ Inactif"
    # On vérifie aussi l'arête corridorA-tunnelB (on regarde qui est sur corridorA ET va vers tunnelB à l'étape suivante)
    edge_count = 0
    for nom, chemin in chemins_drones.items():
        if t < len(chemin)-1:
            if chemin[t] == 'corridorA' and chemin[t+1] == 'tunnelB':
                edge_count += 1
    status_edge = "✅ OK" if edge_count <= 2 else "❌ CONFLIT SUR L'ARÊTE !"
    
    stats_text = (
        f"📊 ANALYSE À t={t} ::\n"
        f"   Drones sur corridorA : {counts_corridor} / 2  ({status_corridor})\n"
        f"   Drones sur roof1 : {counts_roof1} (Zone restricted)\n"
        f"   Drones sur goal : {counts_goal} / 5 (arrivés)\n"
        f"   Drones traversant l'arête corridorA→tunnelB : {edge_count} / 2  ({status_edge})"
    )
    ax_stats.text(0, 0.5, stats_text, transform=ax_stats.transAxes, fontsize=10, 
                  verticalalignment='center', horizontalalignment='left',
                  bbox=dict(boxstyle="round,pad=0.5", facecolor='whitesmoke', alpha=0.9, edgecolor='gray'))
    
    fig.canvas.draw_idle()

# ==========================================
# 5. GESTION DES ÉVÉNEMENTS INTERACTIFS
# ==========================================

def update_slider(val):
    global current_time
    current_time = int(slider.val)
    draw_step(current_time)

def next_step(event):
    global current_time
    if current_time < MAX_T:
        current_time += 1
        slider.set_val(current_time)  # Déclenche update_slider
    else:
        print("Déjà à la dernière étape.")

def prev_step(event):
    global current_time
    if current_time > 0:
        current_time -= 1
        slider.set_val(current_time)
    else:
        print("Déjà à la première étape.")

def toggle_play(event):
    global is_playing, timer
    if is_playing:
        # Arrêter
        is_playing = False
        btn_play.label.set_text('▶ Play')
        if timer is not None:
            timer.stop()
            timer = None
    else:
        # Démarrer
        is_playing = True
        btn_play.label.set_text('⏸ Pause')
        # Créer un timer qui appelle next_step toutes les 1.2 secondes
        timer = fig.canvas.new_timer(interval=1200)
        timer.add_callback(lambda: next_step(None))
        timer.start()

def on_key(event):
    if event.key == 'right':
        next_step(None)
    elif event.key == 'left':
        prev_step(None)
    elif event.key == ' ':
        toggle_play(None)

# Connexion des événements
slider.on_changed(update_slider)
btn_next.on_clicked(next_step)
btn_prev.on_clicked(prev_step)
btn_play.on_clicked(toggle_play)
fig.canvas.mpl_connect('key_press_event', on_key)

# Dessin initial
draw_step(0)

plt.tight_layout()
plt.subplots_adjust(bottom=0.2)  # Laisser de la place pour les contrôles
plt.show()
