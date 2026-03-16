import lightkurve as lk
import logging
import numpy as np 
from detection.py import 
##gestion de log
logger = logging.getLogger(__name__)

def _get_bin() : 
    pass

def analyze_planets_metrics(lc : lk.LightCurve,planets_list : list, star_radius=1 ) : 
    for planet in planets_list : 
