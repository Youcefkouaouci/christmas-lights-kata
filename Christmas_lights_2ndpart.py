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