import reflex as rx
from reflex_project.components.card import card
import reflex_project.styles.styles as styles

def cards() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.heading("Known technologies"),
            margin_y = styles.Spacer.MEDIUM_MARGIN
        ),
        rx.hstack(
            card("python.ico","React","Experience: 3 years"),
            card("python.ico","Python","Experience: 6 years"),
            card("python.ico","C/C++","Experience: 6 years"),
            card("python.ico","JavaScript","Experience: 6 years"),
        ),
        rx.hstack(
            card("python.ico","HTML","Experience: 6 years"),
            card("python.ico","CSS","Experience: 6 years"),
            card("python.ico","Embedded Programming","Experience: 6 years"),
        ),
        rx.hstack(
            card("python.ico","HTML","Experience: 6 years"),
            card("python.ico","CSS","Experience: 6 years"),
            card("python.ico","Embedded Programming","Experience: 6 years"),
        ),
        padding_bottom = styles.Spacer.MEDIUM_MARGIN,
        padding_top = styles.Spacer.MEDIUM_MARGIN,
        width="100%",
        bg=styles.PAGE_BACKGROUND_COLOR
    )