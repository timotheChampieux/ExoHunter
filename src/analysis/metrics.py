import lightkurve as lk
import logging
import numpy as np 
from .detection import mask_planet
##gestion de log
logger = logging.getLogger(__name__)

def _get_bin_size(lc,planet_info, points_per_transit : int = 50 ) : 
    duration = planet_info["duration"]
    points = duration / points_per_transit
    cadence_instrument =np.nanmedian(np.diff(lc.time.value))
    return max(cadence_instrument, points)

def _get_phase(lc,period,epoch_time,bin) : 
    return lc.fold(period = period, epoch_time = epoch_time ).bin(bin)


def analyze_planets_metrics(lc : lk.LightCurve,planets_list : list, star_radius=1 ) : 
    for planet in planets_list : 
        pass