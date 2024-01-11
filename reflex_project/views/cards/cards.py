import reflex as rx
from reflex_project.components.card import card
import reflex_project.styles.styles as styles


def cards() -> rx.Component:
    #     return rx.vstack(
    #     rx.center(
    #         rx.heading("Known technologies"),
    #         margin_y = styles.Spacer.MEDIUM_MARGIN
    #     ),
    #     rx.responsive_grid(
    #         card("react.ico","React","Experience: 1 year"),
    #         card("python.ico","Python","Experience: 6 years"),
    #         card("c++.ico","C/C++","Experience: 6 years"),
    #         card("js.png","JavaScript","Experience: 6 years"),
    #         card("html-5.png","HTML","Experience: 6 years"),
    #         card("css-3.png","CSS","Experience: 6 years"),
    #         card("upc.png","Embedded Programming","Experience: 6 years"),

    #         columns=[2,3,4],
    #         gap=4,
    #         padding_bottom = styles.Spacer.MEDIUM_MARGIN,
    #         padding_top = styles.Spacer.MEDIUM_MARGIN,
    #         width="100%",
    #         bg=styles.PAGE_BACKGROUND_COLOR
    #     )
    # )
    return rx.vstack(
        rx.center(
            rx.heading("Known technologies"), margin_y=styles.Spacer.MEDIUM_MARGIN
        ),
        rx.tablet_and_desktop(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        card("react.ico", "React", "Experience: 1 year"),
                        card("python.ico", "Python", "Experience: 6 years"),
                        card("c++.ico", "C/C++", "Experience: 6 years"),
                        card("js.png", "JavaScript", "Experience: 4 years"),
                    ),
                    rx.hstack(
                        card("html-5.png", "HTML", "Experience: 4 years"),
                        card("css-3.png", "CSS", "Experience: 4 years"),
                        card("upc.png", "Embedded Programming", "Experience: 6 years"),
                    ),
                ),
                justify="space_around",
            ),
        ),
        rx.mobile_only(
            rx.responsive_grid(
                card("react.ico", "React", "Experience: 1 year"),
                card("python.ico", "Python", "Experience: 6 years"),
                card("c++.ico", "C/C++", "Experience: 6 years"),
                card("js.png", "JavaScript", "Experience: 4 years"),
                card("html-5.png", "HTML", "Experience: 4 years"),
                card("css-3.png", "CSS", "Experience: 4 years"),
                card("upc.png", "Embedded Programming", "Experience: 6 years"),
                columns=[2, 3, 4],
                gap=4,
                padding_bottom=styles.Spacer.MEDIUM_MARGIN,
                padding_top=styles.Spacer.MEDIUM_MARGIN,
                width="100%",
                bg=styles.PAGE_BACKGROUND_COLOR,
            ),
        ),
    )
