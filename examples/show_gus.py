"""Create gus"""
import gustaf as gus

WITH_PUPILS = False
WITH_DARK_BACKGROUND = False
DARK_WITH_WHITE_OVAL_BACKGROUND = False
WITH_ALPHA_BACKGROUND = False

if __name__ == "__main__":
    if WITH_ALPHA_BACKGROUND:
        import vedo

        vedo.settings.screenshot_transparent_background = 1

    l_eye = gus.spline.create.disk(0.15)
    l_eye.cps += [0.6, 0.2]
    l_eye.show_options["c"] = "black"

    r_eye = gus.spline.create.disk(0.15)
    r_eye.cps += [-0.6, 0.2]
    r_eye.show_options["c"] = "black"

    x_offset = 0.59
    y_offset = 0.16

    l_pupil = gus.spline.create.disk(0.05)
    l_pupil.cps += [x_offset, y_offset]
    l_pupil.show_options["c"] = "white"

    r_pupil = gus.spline.create.disk(0.05)
    r_pupil.cps += [-x_offset, y_offset]
    r_pupil.show_options["c"] = "white"

    upper_lip = gus.Bezier(
        [5, 1],
        [
            [-0.8, -0.1],
            [-0.2, -0.4],
            [-0.5, 0.5],
            [0.5, 0.5],
            [0.2, -0.4],
            [0.8, -0.1],
            [-0.75, -0.15],
            [-0.2, -0.55],
            [-0.5, 0.05],
            [0.5, 0.05],
            [0.2, -0.55],
            [0.75, -0.15],
        ],
    )
    upper_lip.show_options["c"] = "orange7"

    inner_mouth = gus.Bezier(
        [5, 1],
        [
            *upper_lip.cps[6:],
            [-0.75, -0.15],
            [-0.6, -0.325],
            [-0.4, -0.525],
            [0.4, -0.525],
            [0.6, -0.325],
            [0.75, -0.15],
        ],
    )
    inner_mouth.show_options["c"] = "orange5"

    lower_lip = gus.Bezier(
        [5, 1],
        [
            *inner_mouth.cps[6:],
            [-0.8, -0.1],
            [-0.6, -0.4],
            [-0.4, -0.6],
            [0.4, -0.6],
            [0.6, -0.4],
            [0.8, -0.1],
        ],
    )
    lower_lip.show_options["c"] = "orange7"

    item_to_show = [l_eye, r_eye, upper_lip, inner_mouth, lower_lip]
    if WITH_PUPILS:
        item_to_show += [l_pupil, r_pupil]

    plt = gus.show(
        item_to_show,
        control_points=False,
        knots=False,
        lighting="off",
        background="white",
        close=False,
    )

    if WITH_DARK_BACKGROUND:
        background = []

        if DARK_WITH_WHITE_OVAL_BACKGROUND:
            height = 0.6
            width = 0

            x_shift = 0.3
            y_shift = -0.02

            background = [
                gus.spline.create.disk(height),
                gus.spline.create.disk(height),
                gus.spline.create.box(width + 2 * x_shift, 2 * height),
            ]

            background[0].cps += [-x_shift, y_shift]
            background[1].cps += [width + x_shift, y_shift]
            background[2].cps += [-x_shift, -height + y_shift]
            for elem in background:
                elem.show_options["c"] = "white"
                elem.show_options["alpha"] = 0.25
        else:
            l_eye.show_options["c"] = "white"
            r_eye.show_options["c"] = "white"
            l_pupil.show_options["c"] = "black"
            r_pupil.show_options["c"] = "black"

        plt = gus.show(
            [*background, *item_to_show],
            control_points=False,
            knots=False,
            lighting="off",
            background="black",
            close=False,
        )
