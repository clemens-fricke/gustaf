from gustaf.create import vertices

try:
    from gustaf.create import spline
except ImportError:
    from gustaf.utils.init_helper import SplineCanNotBeLoadedHelper
    spline = SplineCanNotBeLoadedHelper()
