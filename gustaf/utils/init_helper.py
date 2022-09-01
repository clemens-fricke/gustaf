from typing import Any


class SplineCanNotBeLoadedHelper():
    """
    Class used to have better import error handling in the case the 'splinepy'
    package is not installed. This is necessary due to that `splinepy` is not
    a requirement of `gustaf`, but some parts of `gustaf` need it to function.

    This class makes it so that `gustaf` is able to provide all non-spline
    based functionality with out `splinepy`, but gives also comprehensive
    errors in case these functionalities are used without the required package.
    """

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Is called when the object is called by object(). Will notify the user,
        that the functionality is not accessible and how to proceed to access
        the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )
        pass

    def __getattribute__(self, __name: str) -> Any:
        """
        Is called when any attribute of the object is accessed by object.attr.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Is called when any attribute of the object is set by object.attr = new.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )


class VedoCanNotBeLoadedHelper():
    """
    Class used to have better import error handling in the case the 'vedo'
    package is not installed. This is necessary due to that `vedo` is not
    a requirement of `gustaf`, but some parts of `gustaf` need it to function,
    see visualizations.

    This class makes it so that `gustaf` is able to provide all non-vedo
    based functionality with out `vedo`, but gives also comprehensive
    errors in case these functionalities are used without the required package.
    """

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Is called when the object is called by object(). Will notify the user,
        that the functionality is not accessible and how to proceed to access
        the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )
        pass

    def __getattribute__(self, __name: str) -> Any:
        """
        Is called when any attribute of the object is accessed by object.attr.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Is called when any attribute of the object is set by object.attr = new.
        Will notify the user, that the functionality is not accessible and how
        to proceed to access the functionality.
        """
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )
