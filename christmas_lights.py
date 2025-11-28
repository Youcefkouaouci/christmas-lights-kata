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