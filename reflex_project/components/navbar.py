import reflex as rx
from reflex_project.components.button_links import button_links
import reflex_project.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "oayala.dev",
                height=styles.Spacer.MEDIUM_MARGIN,
                font_family="Silkscreen",
                font_size="1.5em",
                margin=styles.Spacer.MEDIUM_MARGIN,
                color="#FFFFFF",
            ),
            rx.spacer(),
            button_links("Home",""),
            button_links("Portfolio","portfolio"),
            button_links("Contact Me","contact_me"),
            width="100%",
        ),
        position="sticky",
        bg=styles.PAGE_BACKGROUND_COLOR,
        z_index="999",
    )
