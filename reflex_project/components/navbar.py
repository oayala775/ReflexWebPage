import reflex as rx
from reflex_project.components.button_links import button_links

FONTS = [
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
    "https://fonts.googleapis.com/css2?family=Encode+Sans+Expanded:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
]

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "oayala.dev",
                height="30px",
                font_family="Silkscreen",
                font_size="1.5em",
                margin="20px",
                color="#FFFFFF",
            ),
            rx.spacer(),
            button_links("Home",""),
            button_links("Portfolio","None"),
            button_links("Contact Me","contact_me"),
            width="100%",
        ),
        position="sticky",
        bg="#003366",
        z_index="999",
    )
