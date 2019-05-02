import numpy as np

def transport(loc, vel, dt):
    """transport equations
    Args:
         loc: initial location (can be int/float or array)
         vel: velocity (can be int/float or array)
         dt: time step

    Returns:
        location after one time step
     """
    # if loc, vel are simple numbers
    if isinstance(loc, (int, float)) and isinstance(vel, (int, float)):
        loc = loc + vel * dt

    if isinstance(loc, list):
        loc = np.array(loc)

    if isinstance(vel, list):
        vel = np.array(vel)

    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        loc = loc.astype(np.double)
        vel = vel.astype(np.double)
        loc = loc + vel * dt
    return loc