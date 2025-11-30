# Christmas Lights Kata - 🎄

Ce projet résout le kata "Christmas Lights". Il simule le contrôle d'une grille de 1000x1000 lumières pour une décoration de Noël.

### Partie 1 : Mode On/Off

Gérer une grille de lumières avec trois types d'instructions :

- `turn on` : allumer les lumières
- `turn off` : éteindre les lumières
- `toggle` : inverser l'état des lumières

### Partie 2 : Mode Luminosité

Les instructions affectent la luminosité des lumières :

- `turn on` : augmente la luminosité de 1
- `turn off` : diminue la luminosité de 1 (minimum 0)
- `toggle` : augmente la luminosité de 2

## Installation et Utilisation

### Prérequis

- Python 3.6 ou supérieur

### Cloner le projet

```bash
git clone <https://github.com/Youcefkouaouci/christmas-lights-kata.git>
cd christmas-lights-kata
```

### Exécuter la Partie 1

```bash
python3 christmas_lights.py
```

### Exécuter la Partie 2

```bash
python3 Christmas_lights_2ndpart.py
```

### Classe `LightGrid` (Partie 1)

```python
- __init__(size): Initialise une grille de taille size×size
- turn_on(x1, y1, x2, y2): Allume les lumières dans la zone
- turn_off(x1, y1, x2, y2): Éteint les lumières dans la zone
- toggle(x1, y1, x2, y2): Inverse l'état des lumières
- parse_instruction(instruction): Parse une instruction textuelle
- execute_instruction(instruction): Exécute une instruction
- count_lights_on(): Retourne le nombre de lumières allumées
```

### Classe `BrightnessLightGrid` (Partie 2)

```python
- __init__(size): Initialise une grille avec luminosité
- turn_on(x1, y1, x2, y2): Augmente la luminosité de 1
- turn_off(x1, y1, x2, y2): Diminue la luminosité de 1 (min 0)
- toggle(x1, y1, x2, y2): Augmente la luminosité de 2
- get_total_brightness(): Retourne la luminosité totale
```

## Apprentissages

- Programmation orientée objet en Python
- Manipulation de structures de données 2D (listes)
- Parsing de chaînes avec regex
- Gestion de version avec Git

## Auteur

Kata réalisé dans le cadre du concours d'admission à la formation **Développeur IA - Simplon**
