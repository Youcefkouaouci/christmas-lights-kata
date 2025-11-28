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
    
    def count_lights_on(self):
        count = 0
        for row in self.grid:
            count += sum(row)
        return count