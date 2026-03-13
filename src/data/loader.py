import lightkurve as lk
import logging

##gestion d'erreur
logger = logging.getLogger(__name__)

def download_target_data(star_name : str, quarter: int = None, author: str="Kepler") -> lk.LightCurve :
    """ 
    Recherche, telecharge, assemble data d'une étoile pour un quarter donné
    """
    try :

    #si quarter est none search renvoie tout les quarter
    search = lk.search_lightcurve(starName, quarter,author)
    #si la recherche est vide on renvoie une error
    if len(search) == 0 :
        raise ValueError(f"Aucune donnée trouvée pour {star_name} au Quarter {quarter}.")


    lc_collection = search.download_all()
    lc = lc_collection.stitch()
    #on informe que c'est tout bon
    logger.info(f"Données téléchargées avec succès pour {star_name}")
    return lc

    except Exception as e :
        #si jamais erreur reseau ou autre
        logger.error(f"Erreur lors du téléchargement : {e}")
        raise