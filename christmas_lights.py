class LightGrid:
    """Classe pour gérer une grille de lumières"""
    
    def __init__(self, size=1000):
        """
        Initialise une grille de lumières
        
        Args:
            size (int): Taille de la grille (par défaut 1000)
        """
        self.size = size
        self.grid = [[False for _ in range(size)] for _ in range(size)]
    
    def count_lights_on(self):
        """
        Compte le nombre de lumières allumées
        
        Returns:
            int: Nombre de lumières allumées
        """
        count = 0
        for row in self.grid:
            count += sum(row)
        return count
    
    def turn_on(self, x1, y1, x2, y2):
        """
        Allume les lumières dans une zone rectangulaire
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] = True
    
    def turn_off(self, x1, y1, x2, y2):
        """
        Éteint les lumières dans une zone rectangulaire
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] = False
    
    def toggle(self, x1, y1, x2, y2):
        """
        Inverse l'état des lumières dans une zone rectangulaire
        Si allumée → éteinte
        Si éteinte → allumée
        
        Args:
            x1, y1: Coordonnées du coin supérieur gauche
            x2, y2: Coordonnées du coin inférieur droit
        """
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x][y] = not self.grid[x][y]

    def parse_instruction(self, instruction):
        """
        Parse (analyse) une instruction textuelle
        
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