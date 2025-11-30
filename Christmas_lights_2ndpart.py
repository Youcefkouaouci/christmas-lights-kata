class BrightnessLightGrid:
    """Classe pour gérer une grille de lumières avec gestion de la luminosité"""
    
    def __init__(self, size=1000):
        """
        Initialise une grille de lumières avec luminosité
        
        Args:
            size (int): Taille de la grille (par défaut 1000)
        """
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
    
    def get_total_brightness(self):
        """
        Calcule la luminosité totale de toutes les lumières
        
        Returns:
            int: Luminosité totale (somme de toutes les valeurs)
        """
        total = 0
        for row in self.grid:
            total += sum(row)
        return total
    
    def turn_on(self, x1, y1, x2, y2):
        """
        Augmente la luminosité de 1 dans une zone rectangulaire
        
        DIFFÉRENCE PARTIE 1 : au lieu de mettre à True,
        on AJOUTE 1 à la valeur actuelle
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] += 1

    def turn_off(self, x1, y1, x2, y2):
        """
        Diminue la luminosité de 1 dans une zone rectangulaire
        La luminosité ne peut PAS être négative (minimum = 0)
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] = max(0, self.grid[x][y] - 1)
    
    def toggle(self, x1, y1, x2, y2):
        """
        Augmente la luminosité de 2 dans une zone rectangulaire
        
        DIFFÉRENCE PARTIE 1 : au lieu d'inverser True/False,
        on AJOUTE 2 à la luminosité
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] += 2
    
    def parse_instruction(self, instruction):
        """
        Parse (analyse) une instruction textuelle
        
        IDENTIQUE À LA PARTIE 1 : le parsing ne change pas!
        Seule l'exécution des actions change.
        
        Args:
            instruction (str): Ex: "turn on 0,0 through 999,999"
        
        Returns:
            tuple: (action, x1, y1, x2, y2)
        """
        import re
        
        pattern = r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'
        match = re.match(pattern, instruction)
        
        if not match:
            raise ValueError(f"Instruction invalide: {instruction}")
        
        action = match.group(1)
        x1, y1, x2, y2 = map(int, match.groups()[1:])
        
        return action, x1, y1, x2, y2
    
    def execute_instruction(self, instruction):
        """
        Exécute une instruction textuelle
        
        IDENTIQUE À LA PARTIE 1 : on appelle les mêmes méthodes,
        mais leur comportement interne a changé!
        
        Args:
            instruction (str): Instruction à exécuter
        """
        action, x1, y1, x2, y2 = self.parse_instruction(instruction)
        
        if action == "turn on":
            self.turn_on(x1, y1, x2, y2)
        elif action == "turn off":
            self.turn_off(x1, y1, x2, y2)
        elif action == "toggle":
            self.toggle(x1, y1, x2, y2)

if __name__ == "__main__":
    print("="*50)
    print("PARTIE 2: Tests des exemples")
    print("="*50)
    
    # Test 1: turn on une seule lumière
    test1 = BrightnessLightGrid()
    test1.turn_on(0, 0, 0, 0)
    print(f"Test 1 - turn on (0,0): {test1.get_total_brightness()}")
    
    # Test 2: toggle toute la grille
    test2 = BrightnessLightGrid()
    test2.toggle(0, 0, 999, 999)
    print(f"Test 2 - toggle all: {test2.get_total_brightness()}")
    
    # Test 3
    test3 = BrightnessLightGrid()
    test3.turn_on(0, 0, 0, 0)
    test3.toggle(0, 0, 0, 0)
    test3.turn_off(0, 0, 0, 0)
    print(f"Test 3 - Scénario mixte: {test3.get_total_brightness()}")

    print("\n" + "="*50)
    print("PARTIE 2: Résolution du kata")
    print("="*50)
    
    santa_lights = BrightnessLightGrid()

    with open('instructions.txt', 'r') as f:
        instructions = f.readlines()

    for instruction in instructions:
        instruction = instruction.strip()
        if instruction:
            santa_lights.execute_instruction(instruction)
            print(f"✓ Exécuté: {instruction}")

    result = santa_lights.get_total_brightness()
    print(f"\n🎄 RÉPONSE PARTIE 2: {result} de luminosité totale 🎄")