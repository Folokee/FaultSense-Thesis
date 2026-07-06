# Prompts Canva — Soutenance PFE FaultSense (FDD photovoltaïque)

Contexte commun à coller en tête de chaque session Canva si l'outil le permet (sinon l'inclure dans chaque prompt) :

> Soutenance de Projet de Fin d'Études (Diplôme d'Ingénieur d'État en Informatique, ESI x CDER). Sujet : système de détection et diagnostic de défauts (FDD) pour installations photovoltaïques, basé sur l'IA. Présenté par GUERRAICHE Ahmed Amine et MENASSEL Rayane Ibrahim. Durée totale visée : 30 minutes maximum. Jury mixte (quelques spécialistes IA/ML, d'autres plus généralistes PV/ingénierie) — vulgariser les concepts techniques sans perdre la rigueur scientifique, garder les termes techniques anglais consacrés (self-attention, density estimation, normalizing flow, etc.) tels quels. Ne fige aucun choix de format, de palette ou de style visuel — uniquement le contenu ci-dessous est verrouillé (chiffres, formules, noms de modèles, ordre logique). Reformule librement les phrases.
>
> **Exigence non négociable sur les diagrammes** : chaque diagramme, schéma ou arborescence listé ci-dessous doit être **animé avec des transitions fluides et progressives** (apparition séquentielle des branches/blocs, zoom/dézoom smooth, morphing entre états) — pas une révélation statique par à-coups (simple fade-in ou apparition brute d'éléments figés). C'est le critère qui a fait abandonner l'outil précédent (LaTeX/Beamer, dont les animations étaient jugées trop rigides et non fluides) : si l'outil ne peut produire qu'une transition abrupte sur un diagramme donné, le signaler explicitement plutôt que de livrer une version statique sans le dire.

Chaque section ci-dessous est un prompt autonome à coller séparément. ~30 min / 6 sections ≈ 5 min par section à l'oral, donc viser une densité de slides cohérente avec ça (ne pas surcharger).

---

## Prompt 1 — Introduction & État de l'art

**Objectif de cette partie** : poser le contexte PV/FDD, montrer la taxonomie des méthodes existantes, et faire émerger le gap de recherche qui justifie le projet.

**Contenu verrouillé, dans cet ordre :**

1. **Contexte et fondements théoriques** : effet photovoltaïque et modèles physiques ; composants d'un système PV ; taxonomie des défauts PV ; limites des méthodes classiques *model-driven*.
2. **Pourquoi la modalité électrique + météo** (comparaison à 3 options) :
   - Imagerie thermique : coût 0,5 à 3 €/module, acquisition événementielle par drone, pas de continuité temporelle.
   - Courbe I-V : mesure discrète, interrompt la production, sensible aux variations d'irradiance pendant le balayage.
   - **Électrique + météo (retenu)** : suivi à haute résolution temporelle, déjà collecté par l'infrastructure SCADA existante — seule modalité compatible avec une surveillance continue et near real-time, condition nécessaire pour une détection précoce.
3. **Arborescence de l'état de l'art** — à représenter visuellement comme un arbre/taxonomie en 2 branches :
   - **Approches classiques** : SVM & noyau (Suliman et al. 2024 ; Cai & Wai 2022 ; Saiprakash et al. 2024), Forêts aléatoires (Amiri et al. 2024b), Boosting de gradient (Suliman et al. 2024 ; Noura et al. 2025 ; Kull et al. 2025).
   - **Approches profondes** : RNN/LSTM/GRU (Hajji et al. 2023 ; Amiri et al. 2024a), Auto-encodeurs (Seghiour et al. 2023 ; Titouni et al. 2025 ; Attouri et al. 2026), Transformers/Graphes (Khalil et al. 2024 ; Balachandran et al. 2025 ; Yan et al. 2025).
   - C'est la slide la plus importante de cette section pour l'animation : idéalement un arbre qui se déploie progressivement (racine → branches → feuilles/références), pas un mur de texte statique.
4. **Lacunes de recherche identifiées** (3 points, à numéroter visuellement) :
   1. Prédominance des jeux de données simulés.
   2. États défaillants difficiles à distinguer.
   3. Absence d'évaluation embarquée.
5. **Objectifs du mémoire** :
   - But général : développer un système basé sur l'IA pour la détection et le diagnostic des défauts dans les systèmes photovoltaïques.
   - Construire un pipeline de données rigoureux pour le traitement de mesures PV réelles.
   - Concevoir et évaluer des modèles FDD pour deux tâches complémentaires : détection d'anomalies et classification des défauts.
   - Déploiement embarqué de la solution sur Jetson Nano avec une interface de monitoring temps réel.

**Consigne d'animation** : transition fluide de l'arbre état de l'art (déploiement progressif des branches) vers les lacunes de recherche, puis vers les objectifs — donner le sentiment d'un entonnoir narratif (large panorama → gap → objectif précis).

---

## Prompt 2 — Conception & Pipeline de données

**Objectif de cette partie** : présenter le processus FDD global, le choix du dataset, et le pipeline de traitement des données.

**Contenu verrouillé :**

1. **Phases du processus FDD** — diagramme en 4 blocs séquentiels avec branchement conditionnel :
   `Collecte & transformation → Détection d'anomalies → (si anomalie) → Diagnostic → Interface de monitoring`
2. **Sélection du jeu de données — dataset Costa** (ne jamais l'introduire comme "Costa" en première mention dans le flux narratif si une formulation plus neutre est possible, mais le nom peut être affiché en titre de slide) :
   - Données réelles de terrain issues d'une installation photovoltaïque.
   - Mesures électriques et météorologiques adaptées au FDD.
   - Quatre défauts annotés : ombrage (shadowing), dégradation, circuit ouvert (open-circuit), court-circuit (short-circuit).
   - Volume important de données, exploitable pour l'apprentissage et l'évaluation.
   - Intérêt : conditions plus proches du réel, compatible avec une approche détection puis diagnostic.
3. **Pipeline de données — 5 étapes séquentielles**, à animer en zoom progressif (un bloc grossit avec son détail, les autres s'estompent, puis retour à la vue d'ensemble avant de passer au suivant) :
   - **Ingestion** → sortie : table opérationnelle unifiée.
     - Détail : merge fichiers météo + électrique sur timestamp, renommage unifié, sérialisation Parquet + manifeste JSON ; conversion `.mat` → Numpy, filtrage des irradiances négatives (capteur), timestamp synthétique 1 Hz ancré au solar noon local, trimming nocturne (irradiance < 100 W/m²).
   - **Découpage** → sortie : ensembles train / val / test.
     - Détail : `episode_id` / `continuity_segment_id`, split hybride semi-supervisé, split temporel-stratifié, sous-échantillonnage de la classe normale avec extraction chronologique en tête.
   - **Prétraitement** → sortie : jeu de données nettoyé.
     - Détail : imputation par paliers (ffill/interpolation, classe normale uniquement), règle de suppression des trous de données sur les fenêtres de panne, winsorizing IQR (×3, train-normal uniquement), recalcul déterministe des canaux de puissance.
   - **Extraction des caractéristiques** → sortie : profils enrichis en caractéristiques.
     - Détail : profils d'ablation additifs (baseline_raw < plus_physics < plus_temporal < plus_tsfresh_minimal/extensive < plus_wavelet < plus_differential < plus_all) ; profil retenu = `baseline_raw` (7+2 features) pour l'équilibre simplicité/performance, ou `plus_physics` selon la tâche.
   - **Entraînement** : Optuna TPE (35 essais), validation croisée 5-fold, suivi MLflow/DagsHub, répartition de ressources CPU/GPU (A100).

**Consigne d'animation** : c'est la 2e slide la plus prioritaire en richesse visuelle après l'arbre état de l'art — un vrai effet de zoom/transition fluide entre les 5 blocs est attendu, pas 5 slides statiques indépendantes.

---

## Prompt 3 — Détection d'anomalies (Task A)

**Objectif de cette partie** : formuler le problème de détection, justifier le choix de modélisation semi-supervisé, présenter les modèles évalués (baselines + MAAT + GTBAD + PC-Flow), et le cœur scientifique : PC-Flow.

**Contenu verrouillé, dans cet ordre :**

1. **Formulation mathématique** : sous irradiance et température données, les mesures électriques normales suivent une relation physique attendue. Une panne est une **déviation persistante** de cette relation, non explicable par $G$ (irradiance) ou $T$ (température) :
   $$\mathbf{X}(t) = [\mathbf{x}(t-w+1), \ldots, \mathbf{x}(t)] \in \mathbb{R}^{w \times d}, \qquad d(t) = \mathbf{1}[s(\mathbf{X}(t)) > \tau]$$
2. **Choix de modélisation — Défi/Solution** :
   - Défi : les classes de panne sont trop rares et déséquilibrées pour apprendre un classifieur supervisé fiable.
   - Solution : formuler le problème comme une détection **semi-supervisée** (apprendre uniquement sur des fenêtres normales, évaluer sur toutes les fenêtres) pour minimiser la dépendance à l'annotation des classes de panne. C'est un détournement de paradigme motivé par la rareté des données, pas juste une solution générique de bibliothèque.
3. **Détecteurs évalués** (liste famille → modèle) :
   - Online → Bayesian Online Changepoint Detection (BOCD)
   - Kernel-based → One-Class SVM (OC-SVM)
   - Ensemble → Isolation Forest
   - Sequence Modeling (DL) → Mamba Adaptive Anomaly Transformer (MAAT)
   - Reconstruction-based (DL) → Gated Transformer-BiLSTM Anomaly Detector (GTBAD)
   - Normalizing Flow (DL) → **PC-Flow** (contribution propre)
4. **Baselines classiques — principe** (une slide, pas trois) :
   - BOCD : maintient une distribution sur le *run length* ; mise à jour récursive en streaming, sans fenêtre fixe ; anomalie = forte probabilité de changepoint.
   - Isolation Forest : hypothèse que les anomalies sont rares et peu nombreuses, donc plus faciles à isoler ; score = profondeur moyenne d'isolement sur arbres de partitionnement aléatoire.
   - OC-SVM : apprend une frontière (hyperplan dans l'espace à noyau RBF) englobant la région normale ; le kernel trick calcule les produits scalaires d'un espace de dimension infinie sans le construire explicitement ; score = distance signée à la frontière.
5. **MAAT — principe + architecture** :
   - Combine Mamba (selective state-space, séquence longue en temps linéaire) et le principe *association-discrepancy* de l'Anomaly Transformer.
   - Une reconstruction pure ne regarde que l'erreur ponctuelle $\|x_t - \hat{x}_t\|^2$, sans tenir compte de la position de chaque instant dans la série.
   - Nouveauté : compare les poids de **self-attention** entre pas de temps ($S$, issus de l'encodeur) à un prior gaussien local ($P$) — normal = association globale, anomalie = association locale seulement.
   - Score pondère l'erreur de reconstruction par cet écart $D_t = \mathrm{KL}(S\|P) + \mathrm{KL}(P\|S)$.
   - Citation : variante adaptée de l'algorithme original (Sellam et al., 2025).
   - Inclure le schéma d'architecture (référence figure `maat_architecture.png` disponible si besoin de la reproduire visuellement).
6. **GTBAD — principe + architecture** :
   - Transformer encoder + décodeur BiLSTM.
   - Apprend à reconstruire les motifs de fonctionnement normal ; anomalie = erreur de reconstruction.
   - Citation : variante adaptée de l'algorithme original (Zhu et al., 2026).
   - Inclure le schéma d'architecture (référence figure `gtbad-arch.png`).
7. **PC-Flow — principe** (cœur de la présentation, à développer sur 2 slides minimum) :
   - Caractériser le fonctionnement normal revient à estimer sa distribution de probabilité $p(x)$ : un problème de **density estimation**.
   - Cette distribution n'est pas simple : les mesures réelles suivent une forme complexe, pas une gaussienne.
   - Un **normalizing flow** apprend une transformation $f_\theta$ parfaitement réversible qui ramène cette distribution complexe vers une gaussienne simple.
   - Réversible ⇒ probabilité exacte pour n'importe quel point, sans approximation.
   - Score d'anomalie = à quel point l'échantillon est improbable sous la distribution apprise.
8. **Probabilité marginale vs conditionnelle** (la contribution propre, à mettre en évidence visuellement, idéalement avec une géométrie de variété/manifold conditionnée vs non-conditionnée) :
   - Les normalizing flows existants apprennent une probabilité **marginale** $p(x)$ : une seule distribution du normal, valable à tout instant.
   - Formule : $p(x)_{\text{flow classique}} \longrightarrow p(x \mid c)_{\text{PC-Flow}}$, avec $c = (\text{irradiance}, T_{\text{PV}})$.
   - Cycle diurne fort (irradiance, température) : une même puissance peut être normale ou suspecte selon le moment.
   - Probabilité marginale ⇒ confond changement de régime et panne.
   - **La solution** : conditionner sur $c$ — jugement relatif au régime, pas à une moyenne globale.
   - Citation RealNVP inline (sans phrase de justification supplémentaire) : (Dinh et al., 2017).
   - Inclure le schéma d'architecture (référence figure `pc_flow_architecture.png`).

**Consigne d'animation** : pour PC-Flow, privilégier un visuel de géométrie (manifold conditionné vs non-conditionné par le régime) plutôt qu'un texte dense — c'est la transition $p(x) \to p(x\mid c)$ qui doit être visuellement marquante. Pour MAAT, un schéma simple self-attention vs prior gaussien local aide mais reste secondaire en priorité.

---

## Prompt 4 — Protocole d'évaluation & Résultats de détection

**Objectif de cette partie** : expliquer pourquoi PR-AUC (et macro PR-AUC), présenter le protocole de sélection en 2 étapes (ranking quality → compacité), puis les résultats.

**Contenu verrouillé, dans cet ordre (le diagramme du protocole doit être présenté en 2 temps, entrecoupé par l'explication du ranking quality) :**

1. **Protocole d'évaluation — étape 1 seule** : afficher uniquement le bloc "1. Ranking quality (PR-AUC, threshold-free)".
2. **Ranking quality : de quoi parle-t-on ?**
   - F1, precision, recall sont figés à un seuil unique $\tau$ — ils ne mesurent qu'un seul point de fonctionnement.
   - Le ranking quality évalue si le détecteur ordonne correctement les échantillons par score d'anomalie, sur tous les seuils possibles — d'où son caractère threshold-free.
   - Nécessaire ici : le choix du modèle (étape 1) précède tout choix de seuil (étape 4, traité plus tard).
3. **PR-AUC : la métrique retenue (formule)** :
   $$\mathrm{Precision} = \frac{TP}{TP+FP}, \quad \mathrm{Recall} = \frac{TP}{TP+FN}, \quad \mathrm{PR\text{-}AUC} = \int_0^1 \mathrm{Precision}(r)\,dr$$
   PR-AUC = aire sous la courbe precision-recall ; résume, sur tous les seuils, la precision conservée à chaque niveau de recall.
4. **Pourquoi PR-AUC (et pas ROC-AUC) ?**
   - La phase d'EDA a montré ≈84,7% de lignes normales / ≈15,3% en panne, et parmi les pannes un facteur ≈30× entre la classe la plus rare (Short-Circuit, 5 999) et la plus fréquente (Shadowing, 184 311) — déséquilibre sévère à deux niveaux.
   - PR-AUC se base uniquement sur precision et recall de la classe positive (la panne) — sensible à l'imbalance, contrairement à ROC-AUC.
   - **Macro PR-AUC** : moyenne non pondérée par classe — Shadowing ne domine plus le score, chaque classe de panne compte autant.
5. **Protocole d'évaluation — diagramme complété** : `1. Ranking quality (PR-AUC) → 2. Compactness (nombre de paramètres) → Modèle retenu → Threshold calibration`.
6. **Résultats : qualité** (tableau, agrandi/lisible) :

   | Détecteur | Binary | Macro | SC | Dégrad. | OC | Shad. |
   |---|---|---|---|---|---|---|
   | BOCD | 0,870 | 0,401 | 0,130 | 0,121 | 0,489 | 0,865 |
   | Isolation Forest | 0,974 | 0,822 | 0,818 | 0,496 | 1,000 | 0,972 |
   | OC-SVM | 0,987 | 0,965 | 0,992 | 0,884 | 1,000 | 0,983 |
   | MAAT | 0,982 | 0,924 | 0,994 | 0,753 | 1,000 | 0,981 |
   | GTBAD | 0,9896 | 0,9752 | 0,9998 | 0,9140 | 1,0000 | 0,9871 |
   | **PC-Flow** | 0,972 | **0,990** | 1,000 | 0,998 | 1,000 | 0,962 |

7. **Limite du binary PR-AUC** : ne demande qu'une chose — distinguer une panne, n'importe laquelle, du fonctionnement normal. Cinq modèles sur six entre 0,97 et 0,99, presque tous "excellents" en apparence. Shadowing domine le calcul : un modèle qui n'attrape que Shadowing score déjà très haut. (figure `fig_comparison_binary.png`)
8. **La révélation : macro PR-AUC** : les modèles qui semblaient tous proches s'étalent désormais de 0,401 (BOCD) à 0,990 (PC-Flow) — PC-Flow passe du dernier rang à la première place. C'est ce renversement qui motive le choix de la macro PR-AUC comme métrique de sélection. (figure `fig_comparison_macro.png`)
9. **Les défauts à faible amplitude** : Short-Circuit, Open-Circuit, Shadowing — tous les modèles compétitifs frôlent 1,0 (signatures abruptes, faciles à séparer). La Dégradation est un défaut de contact à haute résistance : chaque mesure isolée reste proche de la normale, sans événement net. PC-Flow score par probabilité conditionnelle (irradiance, température), pas par magnitude d'erreur — un écart discret par rapport à la variété physique attendue tombe dans la queue de faible probabilité même quand chaque signal a l'air ordinaire. (figure `fig_comparison_perclass.png`)
10. **Résultats : compacité** (tableau) :

    | Détecteur | Macro PR-AUC | Paramètres |
    |---|---|---|
    | BOCD | 0,401 | 28 (NIG) |
    | MAAT | 0,924 | 184 213 |
    | OC-SVM | 0,965 | 1 280 (SV) |
    | GTBAD | 0,975 | 869 769 |
    | **PC-Flow** | **0,990** | **20 124** |

    (Isolation Forest omise : taille comptée en arbres, non comparable.)
11. **Performance vs compacité** : GTBAD, le concurrent le plus proche en macro PR-AUC, n'est pas proche en taille — PC-Flow est 43× plus petit pour un score égal ou supérieur. Sur Jetson Nano, mémoire et temps d'inférence croissent avec le nombre de paramètres : facteur décisif pour la cible embarquée. (figure `fig_comparison_size.png`)
12. **Calibration des seuils ISA-18.2** (chaîne d'escalade séquentielle, calibrée uniquement sur les scores normaux d'entraînement) :

    | Tier | Méthode | Précision | Rappel / Délai |
    |---|---|---|---|
    | P3 — Advisory | GPD/POT, FPR ≤ 20% | 0,9174 | 0,9167 |
    | P2 — High | Conformal, α=0,05 | 0,9705 | 0,7050 |
    | P1 — Critical | CUSUM séquentiel | 1,0000 | 63 échantillons |

    P3 favorise le rappel comme alerte précoce ; P2 garantit un FPR ≤ 5% (distribution-free) ; P1 n'alarme que sur une dérive persistante, au prix d'un délai médian de 63 échantillons.

**Consigne d'animation** : le diagramme du protocole d'évaluation doit apparaître en 2 temps distincts (étape 1 seule, puis explication du ranking quality sur 3 slides, puis le diagramme complet) — pas tout le diagramme animé d'un coup suivi des explications séparément.

---

## Prompt 5 — Diagnostic de défauts (Task B)

**Objectif de cette partie** : sélection du classifieur de pannes et calibration de ses probabilités. Pas de volet transfert sim-to-réel (hors scope actuel) — uniquement classification multi-classes sur le dataset retenu.

**Contenu verrouillé :**

1. **Sélection du classifieur de pannes** : 3 ensembles d'arbres, 35 essais Optuna TPE chacun, objectif macro F1, sur le profil `plus_physics` :

   | Modèle | Macro F1 | Bal. Acc. | Worst-class F1 |
   |---|---|---|---|
   | LightGBM | 0,934 ± 0,098 | 0,925 ± 0,131 | 0,860 (Dégrad.) |
   | CatBoost | 0,948 ± 0,090 | 0,932 ± 0,124 | 0,893 (Dégrad.) |
   | **ExtraTrees** | **0,959 ± 0,078** | **0,943 ± 0,113** | **0,922** |

   ExtraTrees l'emporte sur tous les critères avec le plus faible écart entre folds. Son double aléa (features et seuils) agit comme régularisateur naturel — précieux quand les classes minoritaires comptent très peu d'épisodes (15-23).
   `voltage_imbalance` (41%) et `pdc_temp_corrected` (16%) dominent l'importance des features — la feature engineering physique se valide elle-même.
2. **Calibration des probabilités** : les scores bruts d'ExtraTrees ne sont pas garantis calibrés (confiance de 0,9 ≠ 90% de fiabilité réelle). Recalibration par Platt scaling (sigmoïde, fit sur validation) :

   | Métrique (test, calibré) | Valeur |
   |---|---|
   | Log-loss | 0,059 |
   | Brier score | 0,008 |
   | ECE | 0,019 |
   | MCE | 0,754 |

   Log-loss et Brier confirment un bon alignement global ; l'ECE de 0,019 montre une faible erreur moyenne. Le MCE (effet de bin extrême) capture le pire cas, pas la qualité moyenne — la confiance affichée à l'opérateur reste fiable dans l'ensemble.

**Consigne d'animation** : pas de besoin d'animation complexe ici, deux tableaux clairs avec mise en évidence du modèle/de la métrique gagnante suffisent. Une transition simple entre les deux slides (sélection → calibration) suffit.

---

## Prompt 6 — Déploiement & Conclusion

**Objectif de cette partie** : montrer la validation embarquée (Jetson Nano), le monitoring de dérive, conclure sur les résultats, limites et perspectives.

**Contenu verrouillé, dans cet ordre :**

1. **Plateforme embarquée : NVIDIA Jetson Nano** :
   - Plateforme edge AI compacte et basse consommation.
   - GPU NVIDIA Maxwell intégré pour l'accélération matérielle.
   - Mémoire LPDDR4 suffisante pour des modèles légers.
   - Environnement JetPack avec CUDA, cuDNN et TensorRT.
2. **Latence du système complet sur Jetson Nano** :
   - Protocole : rejeu de 162 453 échantillons PV réels, mesure du temps de traitement par échantillon, budget temps réel de 1000 ms par échantillon.
   - Tableau :

     | Étape | p50 | p95 | p99 |
     |---|---|---|---|
     | Détecteur PC-Flow | 8,97 ms | 13,58 ms | 19,04 ms |
     | Classifieur ExtraTrees | 5,10 ms | 9,50 ms | 14,75 ms |
     | **Pipeline complet** | **12,94 ms** | **21,44 ms** | **30,04 ms** |

   - Résultat clé : le pipeline complet reste largement sous la contrainte temps réel, avec une marge d'environ 33× au 99e centile.
3. **Détection de dérive opérationnelle** :
   - Objectif : vérifier que les conditions de déploiement restent proches du domaine vu à l'entraînement ; signaler une dérive avant qu'elle ne dégrade silencieusement la qualité de détection.
   - Principe : surveillance du régime d'exploitation (irradiance, température PV), agrégation quotidienne pour distinguer une dérive persistante du cycle jour/nuit, test Page-Hinkley bidirectionnel.
   - Niveaux : Normal (aucune dérive) ; Advisory (dérive persistante 7 jours consécutifs) ; Action-ready (dérive persistante 14 jours consécutifs).
   - Architecture du module de monitoring : inclure un schéma (référence figure `monitoring-arch.png`).
4. **Conclusion — résultats atteints** :
   - Système FDD complet : pipeline bout-en-bout (ingestion, découpage temporel, prétraitement, caractéristiques informées par la physique), détection par PC-Flow conditionné par le régime, diagnostic par ExtraTrees avec pondération des classes, déploiement embarqué Jetson Nano avec export ONNX et interface de monitoring.
   - Résultats clés : PC-Flow PR-AUC binaire 0,989 ± 0,008 avec moins de 25 000 paramètres ; ExtraTrees macro F1 0,959 ± 0,078 et balanced accuracy 0,943 ± 0,113 ; pipeline complet temps réel sur Jetson Nano avec marge 33× au 99e centile.
5. **Limites du système** :
   - Données : évaluation réalisée sur un seul dataset ; défauts induits dans des conditions contrôlées (généralisation terrain encore limitée) ; couverture limitée à quatre classes seulement.
   - Opérationnelles : campagne d'acquisition courte sans cycle annuel complet (pas de variations saisonnières) ; hypothèse d'un seul défaut dominant par fenêtre d'observation.
6. **Perspectives futures** :
   - Données et validation : étendre l'évaluation à plusieurs sites PV et conditions climatiques ; collecter des défauts plus variés à différents niveaux de sévérité ; valider la robustesse sur des campagnes longues couvrant les variations saisonnières.
   - Évolution du système : diagnostic multi-défauts pour pannes simultanées ; mécanismes de recalibration/mise à jour pour l'adaptation aux dérives ; explicabilité et aide à la décision dans l'interface opérateur.

**Consigne d'animation** : une transition simple entre déploiement (technique) et conclusion (synthèse) suffit ; pas de besoin d'animation complexe ici, sauf si l'outil propose un visuel de synthèse type "résumé en un coup d'œil" pour la slide de conclusion.
