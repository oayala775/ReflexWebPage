import reflex as rx
import reflex_project.styles.styles as styles

def card(route,heading,footer) -> rx.Component:
    return rx.card(
        rx.center(
            rx.image(src=route, width="30px", height="auto"),
        ),
        header=rx.heading(f"{heading}", size="lg"),
        footer=rx.heading(f"{footer}", size="sm")
    )