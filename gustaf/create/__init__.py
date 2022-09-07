from gustaf.create import vertices

try:
    from gustaf.create import spline
except ImportError as err:
    print(err)
    from gustaf.utils.init_helper import LibraryCanNotBeLoadedHelper
    spline = LibraryCanNotBeLoadedHelper("splinepy")
