from typing import Any

class SplineCanNotBeLoadedHelper():

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )
        pass

    def __getattribute__(self, __name: str) -> Any:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `splinepy` package. Please see the install "
            "instructions on how to install it."
        )

class VedoCanNotBeLoadedHelper():

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )
        pass

    def __getattribute__(self, __name: str) -> Any:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise ImportError(
            "This gustaf functionality can not be provided due to not being "
            "able to load the `vedo` package. Please see the install "
            "instructions on how to install it."
        )