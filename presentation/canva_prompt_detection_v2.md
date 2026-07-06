# Prompt Canva — Section "Détection d'anomalies" (version redessinée)

> **Contexte général** : Soutenance de Projet de Fin d'Études (Diplôme d'Ingénieur d'État en Informatique, ESI × CDER). Sujet : système FDD (Fault Detection and Diagnosis) pour installations photovoltaïques basé sur l'IA. Présenté par GUERRAICHE Ahmed Amine. Durée cible de cette section : 7 minutes maximum. Jury mixte (spécialistes IA/ML + généralistes PV/ingénierie) — maintenir la rigueur scientifique, garder les termes techniques anglais (self-attention, density estimation, normalizing flow, association discrepancy, etc.) tels quels.
>
> **Principe directeur absolu** : une idée par slide, zéro bloc de texte. Chaque slide est un visuel avec un titre. Le texte est dans le script oral, pas sur l'écran. Les chiffres, formules et noms de modèles ci-dessous sont **verrouillés** (ne pas les modifier). La mise en forme, la palette et le style sont libres.
>
> **Exigence animation** : chaque diagramme doit être animé avec des transitions fluides et progressives (apparition séquentielle, morphing entre états, zoom/dézoom). Si une transition ne peut être que statique, le signaler explicitement.
>
> **Note figures externes** : certaines slides référencent des fichiers PNG à importer (indiqués par `[IMPORTER : nom_fichier.png]`). D'autres nécessitent des visuels générés en Python (indiqués `[FIGURE PYTHON]`). Les visuels PPT-natifs sont indiqués `[CRÉER DANS CANVA]`.

---

## Cette section contient 17 slides dans l'ordre suivant :

---

### Slide 1 — "Qu'est-ce qu'une anomalie PV ?"

**Idée unique** : une panne PV est une déviation persistante de la relation physique normale entre irradiance, température et puissance.

**Visuel** : `[FIGURE PYTHON]` — courbe de puissance réelle du dataset Costa sur une fenêtre temporelle. Deux zones colorées :
- Zone **verte** : fonctionnement normal
- Zone **rouge** : anomalie (déviation persistante)
- Une flèche annotée : *"déviation persistante non explicable par G ou T"*

**Titre** : *"Qu'est-ce qu'une anomalie PV ?"*

**Zéro formule, zéro bullet** — la courbe suffit.

---

### Slide 2 — "Pourquoi semi-supervisé ?"

**Idée unique** : les classes de panne sont trop rares et déséquilibrées pour un classifieur supervisé — on entraîne uniquement sur le normal.

**Visuel** : `[CRÉER DANS CANVA]` — deux zones sur la même slide :

**Zone gauche — "Le problème"** : graphique en barres horizontales (distribution réelle du dataset Costa) :
```
Normal          ████████████████████  84,7 %
Shadowing       ████                  ~10 %
Open-Circuit    ██                    ~3 %
Dégradation     █                     ~1 %
Short-Circuit   ▏                     ~0,2 %
```
Annotation discrète : *"facteur 30× entre la classe la plus rare et la plus fréquente"*

**Zone droite — "La solution"** : diagramme 3 boîtes avec flèches :
```
[Données normales] → [Modèle apprend le normal] → [Anomalie = écart au normal]
```

**Titre** : *"Pourquoi semi-supervisé ?"*

**Animation** : zone gauche apparaît d'abord (le problème), puis zone droite (la solution).

---

### Slide 3 — "Paysage de la détection d'anomalie"

**Idée unique** : on a exploré le paysage en sélectionnant un représentant par famille — pas du bruteforce, une exploration raisonnée.

**Visuel** : `[CRÉER DANS CANVA]` — tableau en 2 colonnes et 2 niveaux :

```
┌──────────────────────┬──────────────────────────────────────────┐
│    CLASSIQUES        │           DEEP LEARNING                  │
│    (baselines)       ├──────────────┬───────────────┬──────────┤
│                      │   Séquence   │ Reconstruction │  Densité │
│  BOCD                │              │                │          │
│  Isolation Forest    │    MAAT      │    GTBAD       │ PC-Flow  │
│  OC-SVM              │              │                │          │
└──────────────────────┴──────────────┴───────────────┴──────────┘
```

**Titre** : *"Exploration raisonnée du paysage — 4 familles, 6 représentants"*

**Animation** : colonne "Classiques" apparaît en premier (anchors), puis les 3 colonnes DL apparaissent une par une de gauche à droite. Chaque colonne DL correspondra à une prochaine slide (effet zoom annoncé).

---

### Slide 4 — "Les baselines classiques"

**Idée unique** : 3 familles classiques comme ancres de référence — un représentant par paradigme.

**Visuel** : `[CRÉER DANS CANVA]` — 3 cartes côte à côte (une par modèle), sans prose :

| BOCD | Isolation Forest | OC-SVM |
|---|---|---|
| Online changepoint | Isolation par partitionnement aléatoire | Frontière dans l'espace à noyau |
| Score = probabilité de changepoint | Score = profondeur moyenne d'isolement | Score = distance signée à la frontière |

**Titre** : *"Baselines classiques — 3 paradigmes de référence"*

**Zéro description longue** — 1 ligne par modèle, principe en 5 mots max.

---

### Slide 4a — "MAAT — Cohérence temporelle"

**Idée unique** : MAAT détecte les anomalies en mesurant si un timestep s'inscrit dans le contexte temporel global de la séquence.

**Visuel** : `[CRÉER DANS CANVA]` — diagramme conceptuel en 2 états :

**État normal** — nœuds [t1][t2][t3][t4][t5] reliés par des arêtes denses (chaque nœud est connecté à tous les autres) :
```
[t1]══[t2]══[t3]══[t4]══[t5]
 associations larges et globales
```

**Anomalie à faible amplitude** — un nœud isolé des autres :
```
[t1]══[t2]   [t3]   [t4]══[t5]
              ↑
         isolé du contexte
         → KL(S‖P) élevé → détecté
```

**Titre** : *"MAAT — Cohérence temporelle"*

**Animation** : état normal apparaît, puis les arêtes de t3 disparaissent progressivement (morphing) pour montrer l'isolation. Pas de texte sur la slide sauf les labels des nœuds et la formule KL(S‖P) en annotation discrète.

---

### Slide 4b — "MAAT — Nos 3 adaptations"

**Idée unique** : 3 modifications architecturales apportées à l'implémentation originale de Sellam et al. 2025.

**Visuel** : `[CRÉER DANS CANVA]` — tableau comparatif 2 colonnes :

| ORIGINAL (Sellam et al. 2025) | NOTRE VERSION ✓ |
|---|---|
| Conv1d circulaire (fuite de contexte futur) | nn.Linear pointwise (ordering temporel préservé) |
| Mamba séquentiel après l'attention | Mamba ‖ Attention en parallèle (vues indépendantes) |
| Skip-connection additive (fusion fixe) | Gate sigmoïde apprise (contrôle per-position) |

**Titre** : *"MAAT — 3 adaptations architecturales"*

**Zéro prose** — juste le diff. Le titre annonce "nos adaptations", pas "nos contributions" (PC-Flow est la contribution principale).

---

### Slide 4c — "MAAT — Architecture"

**Idée unique** : vue complète de l'architecture MAAT adaptée.

**Visuel** : `[IMPORTER : maat_architecture.png]` — plein écran, sans callouts ni texte par-dessus.

**Titre** : *"MAAT — Architecture"*

---

### Slide 5 — "GTBAD — Reconstruction"

**Idée unique** : une anomalie à faible amplitude ne peut pas être fidèlement reconstruite.

**Visuel** : `[IMPORTER : gtbad-arch.png]` — plein écran, sans callouts ni texte par-dessus.

**Titre** : *"GTBAD — une anomalie à faible amplitude ne peut pas être bien reconstruite"*

**Légende discrète en bas** : *Score = ‖x − x̂‖²* (petite taille, ne pas réduire la figure).

---

### Slide 6a — "PC-Flow — Estimation de densité"

**Idée unique** : PC-Flow détecte les anomalies en les définissant comme des événements improbables sous la distribution du fonctionnement normal.

**Visuel** : `[CRÉER DANS CANVA]` — schéma conceptuel :

- Une cloche (distribution apprise du normal) dessinée en vert
- Un point rouge tombant dans la queue de faible probabilité (loin du centre)
- Annotation : *"anomalie = événement à faible probabilité sous p(x)"*
- En dessous : texte discret *"normalizing flow f_θ : distribution complexe → gaussienne, probabilité exacte"*

**Titre** : *"PC-Flow — Une anomalie est un événement improbable"*

**Animation** : la cloche se dessine d'abord (distribution normale), puis le point rouge apparaît dans la queue.

---

### Slide 6b — "p(x) → p(x | c)"

**Idée unique** : l'innovation de PC-Flow est de conditionner la probabilité sur le régime physique (irradiance, température) — pas une distribution globale unique.

**Visuel** : `[CRÉER DANS CANVA]` — deux panels côte à côte :

**Panel gauche — "Flow classique p(x)"** :
- Même distribution pour tous les régimes
- Exemple : une mesure de puissance à midi et à l'aube jugées par la même distribution → confusion régime normal / panne

**Panel droit — "PC-Flow p(x | c)"** :
- Distribution différente selon c = (irradiance, T_PV)
- La même mesure de puissance est jugée relativement à son régime → diagnostic juste

Formule verrouillée entre les deux panels :
$$p(x) \longrightarrow p(x \mid c), \quad c = (\text{irradiance},\ T_{\text{PV}})$$

**Titre** : *"L'innovation : conditionner sur le régime physique"*

**Animation** : panel gauche apparaît (problème), flèche de transformation, panel droit apparaît (solution).

---

### Slide 6c — "PC-Flow — Architecture"

**Idée unique** : vue complète de l'architecture PC-Flow.

**Visuel** : `[IMPORTER : pc_flow_architecture.png]` — plein écran, sans callouts.

**Titre** : *"PC-Flow — Architecture"*

---

### Slide 7a — "Protocole en 2 étapes"

**Idée unique** : on choisit d'abord le meilleur modèle (ranking quality, threshold-free), puis on calibre les seuils d'alarme — ces deux étapes ne peuvent pas être inversées.

**Visuel** : `[CRÉER DANS CANVA]` — diagramme 2 blocs en séquence avec flèche :

```
[Étape 1 : Ranking quality]     →     [Étape 2 : Calibration ISA-18.2]
  PR-AUC (threshold-free)               seuils d'alarme sur le modèle
  → choix du modèle                     retenu
```

**Titre** : *"Protocole en 2 étapes — choix du modèle puis calibration"*

**Animation** : bloc 1 apparaît, puis flèche, puis bloc 2.

---

### Slide 7b — "PR-AUC — Capacité discriminante du modèle"

**Idée unique** : PR-AUC mesure la capacité intrinsèque du modèle à discriminer normal et anomalie, indépendamment de tout choix de seuil.

**Visuel** : `[CRÉER DANS CANVA]` — courbe Precision-Recall schématique (pas de données réelles) :

- Axe X : Recall (0 → 1)
- Axe Y : Precision (0 → 1)
- Courbe en forme d'arc, aire sous la courbe colorée
- Annotation : *"aire sous la courbe = PR-AUC"*
- En dessous : *"mesure ce que le modèle vaut intrinsèquement — pas ce qu'il vaut à un seuil donné"*

**Titre** : *"PR-AUC — Capacité discriminante du modèle"*

---

### Slide 8a — "PC-Flow : dernier en binary → premier en macro"

**Idée unique** : le binary PR-AUC masque la vraie performance — le macro PR-AUC révèle le renversement complet du classement.

**Visuel** : `[IMPORTER : fig_comparison_binary.png]` et `[IMPORTER : fig_comparison_macro.png]` côte à côte, plein écran.

Entre les deux figures : une flèche de transformation et l'annotation :
*"PC-Flow : dernier (binary) → premier (macro)"*

**Titre** : *"Le renversement : binary PR-AUC vs macro PR-AUC"*

**Chiffres verrouillés** (annotations discrètes si l'outil le permet) :
- Binary PC-Flow : 0,972
- Macro PC-Flow : 0,990

---

### Slide 8b — "Les anomalies à faible amplitude révèlent les vraies capacités"

**Idée unique** : Short-Circuit, Open-Circuit et Shadowing sont faciles pour tous les modèles — c'est sur les anomalies à faible amplitude que le classement se fait.

**Visuel** : `[IMPORTER : fig_comparison_perclass.png]` — plein écran.

Une annotation sur la barre correspondante : *"anomalie à faible amplitude — seul PC-Flow maintient un score élevé"*

**Titre** : *"Les anomalies à faible amplitude révèlent les vraies capacités"*

---

### Slide 9a — "PC-Flow — Sélection finale"

**Idée unique** : PC-Flow est le modèle retenu — meilleur score macro PR-AUC ET 43× plus compact que son concurrent le plus proche (GTBAD).

**Visuel** : `[IMPORTER : fig_comparison_size.png]` — plein écran.

**Titre** : *"PC-Flow — meilleur score, 43× plus compact que GTBAD"*

**Chiffres verrouillés** :
- PC-Flow : Macro PR-AUC = 0,990 | Paramètres = 20 124
- GTBAD : Macro PR-AUC = 0,975 | Paramètres = 869 769
- Ratio : 43× (PC-Flow plus compact)

---

### Slide 9b — "Calibration selon ISA-18.2"

**Idée unique** : 3 seuils d'alarme calibrés sur le même score PC-Flow, correspondant aux 3 niveaux de priorité de la norme industrielle ISA-18.2.

**Visuel** : `[CRÉER DANS CANVA]` — échelle de sévérité descendante (style feu tricolore étendu) :

```
🟡  P3  Advisory    →  alerte précoce, haute sensibilité
                       Méthode : GPD/POT, FPR ≤ 20%
                       Précision : 0,9174 | Rappel : 0,9167

🟠  P2  High        →  confiance modérée, FPR contrôlé
                       Méthode : Conformal, α = 0,05
                       Précision : 0,9705 | Rappel : 0,7050

🔴  P1  Critical    →  haute confiance, action immédiate
                       Méthode : CUSUM séquentiel
                       Précision : 1,0000 | Délai médian : 63 échantillons
```

**Titre** : *"Calibration selon ISA-18.2 — 3 degrés d'alerte industriels"*

**Message clé** (1 ligne en bas de slide) : *"3 opérateurs sur le même score PC-Flow — pas de seuil arbitraire, alignement sur la norme industrielle."*

**Animation** : les 3 niveaux apparaissent séquentiellement du haut (P3) vers le bas (P1), montrant l'escalade de sévérité.

---

## Récapitulatif des figures à importer (fichiers PNG existants)

| Slide | Fichier |
|---|---|
| 4c | `figures/detection/maat_architecture.png` |
| 5 | `figures/detection/gtbad-arch.png` |
| 6c | `figures/detection/pc_flow_architecture.png` |
| 8a | `figures/detection/fig_comparison_binary.png` + `fig_comparison_macro.png` |
| 8b | `figures/detection/fig_comparison_perclass.png` |
| 9a | `figures/detection/fig_comparison_size.png` |

## Figures à générer en Python (avant import dans Canva)

| Slide | Description |
|---|---|
| 1 | Courbe de puissance Costa : zone verte (normal) + zone rouge (anomalie) + annotation flèche |
| 2 | Graphique barres horizontales distribution classes Costa (84,7% / 15,3% + facteur 30×) |
