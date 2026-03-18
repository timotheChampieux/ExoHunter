import lightkurve as lk
import logging

##gestion d'erreur
logger = logging.getLogger(__name__)

def lc_cleaner(lc : lk.LightCurve, window_length:int = 801, sigma: int = 5) -> lk.LightCurve :
    """ 
    Nettoie la courbe de lumière. Attention : window_length doit être > 3x la durée d'un transit. 
    """
    try: 
        #On garde le nombre de point pour verifier que le cleaner n'a pas enlevé tout la courbe par erreur
        initial_length = len(lc)
        
        #on nettoie (outliers retire les pics de lumière parasite et flatten corrige les variation de l'etoile)
        lc_clean = lc.flatten(window_length=window_length).remove_outliers(sigma=sigma)
        
        final_length = len(lc_clean)
        
        logger.info(f"Nettoyage terminé : {initial_length - final_length} points retirés.")

        return lc_clean
    
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage de la courbe : {e}")
        raise