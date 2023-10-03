import point

"""
Permet de séparer les points
"""

class separateur:

    """
    Sépare les points selon si on est devant ou derière le plan YZ
    """
    @staticmethod
    def devant_derriere(p):
        if(p.y >= 0):
            return True
        return False