from typing import Any


class LibraryCanNotBeLoadedHelper():
    """
    Class used to have better import error handling in the case that a package
    package is not installed. This is necessary due to that some packages are
    not a dependency of `gustaf`, but some parts require them to function.
    Examples are `splinepy` and `vedo`.
    """
    _message = None

    def __init__(self, lib_name: str) -> None:
        self._message = str(
           "Parts of the requested functionality in gustaf depend on the "
           f"external `{lib_name}` package which could not be found on your"
           " system. Please refer to the installation instructions for more"
           " information.")

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
