from typing import Any


class LibraryCanNotBeLoadedHelper():
    """
    Class used to have better import error handling in the case the 'splinepy'
    package is not installed. This is necessary due to that `splinepy` is not
    a requirement of `gustaf`, but some parts of `gustaf` need it to function.

    This class makes it so that `gustaf` is able to provide all non-spline
    based functionality with out `splinepy`, but gives also comprehensive
    errors in case these functionalities are used without the required package.
    """
    _message = None

    def __init__(self, lib_name: str) -> None:
        self._message = \
            "This gustaf functionality can not be provided due to not being "+\
            f"able to load the `{lib_name}` package. Please see the install "+\
            "instructions on how to install it."

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Is called when the object is called by object(). Will notify the user,
        that the functionality is not accessible and how to proceed to access
        the functionality.
        """
        raise ImportError(self._message)

    def __getattr__(self, __name: str) -> Any:
        """
        Is called when any attribute of the object is accessed by object.attr.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        if __name == "_LibraryCanNotBeLoadedHelper__message":
            return object.__getattr__(self, __name[-8:])
        else:
            raise ImportError(self._message)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Is called when any attribute of the object is set by object.attr = new.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        if __name == "_message":
            object.__setattr__(self, __name, __value)
        else:
            raise ImportError(self._message)

    def __getitem__(self, key):
        """
        Is called when the object is subscripted object[x]. Will notify the
        user, that the functionality is not accessible and how to proceed to
        access the functionality.
        """
        raise ImportError(self._message)
