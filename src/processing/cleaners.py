import lightkurve as lk
import logging

##gestion d'erreur
logger = logging.getLogger(__name__)

def lc_cleaner(lc : lk.Light_Curve, window_length=401, sigma: int = 5) -> lk.LightCurve :
    
    try: 
        #On garde le nombre de point pour verifier que le cleaner n'a pas enlevé tout la courbe par erreur
        initial_length = len(lc)
        
        #on nettoie (outliers retire les pics de lumière parasite et flatten corrige les variation de l'etoile)
        lc_clean = lc.remove_nans().remove_outliers(sigma=sigma).flatten(window_length=window_length)
        
        final_length = len(lc_clean)
        
        logger.info(f"Nettoyage terminé : {initial_length - final_length} points retirés.")

        return lc_clean
    
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage de la courbe : {e}")
        raise