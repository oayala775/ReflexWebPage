import reflex as rx
import reflex_project.styles.styles as styles


def card(route, heading, footer, alternative_text) -> rx.Component:
    return rx.card(
        rx.center(
            rx.image(src=route, width="50px", height="auto", alt=alternative_text),
        ),
        header=rx.heading(f"{heading}", size="lg"),
        footer=rx.heading(f"{footer}", size="sm"),
    )
