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
            rx.tablet_and_desktop(
                rx.hstack(
                    button_links("Home", "/"),
                    # button_links("Portfolio","portfolio"),
                    button_links(
                        "Contact Me",
                        "contact_me",
                        margin_right=styles.Spacer.MEDIUM_MARGIN,
                    ),
                    width="100%",
                    margin=styles.Spacer.MEDIUM_MARGIN,
                )
            ),
            rx.mobile_only(
                rx.menu(
                    rx.menu_button(rx.center(rx.icon(tag="hamburger", color="white"))),
                    rx.menu_list(
                        rx.menu_item(
                            rx.link("Home", href="/"),
                        ),
                        # rx.menu_item(
                        #     rx.link("Portfolio",href="/portfolio")
                        # ),
                        rx.menu_item(rx.link("Contact", href="/contact_me")),
                    ),
                ),
                padding_y=styles.Spacer.MAX_MARGIN,
                padding_x=styles.Spacer.MAX_MARGIN,
            ),
            width="100%",
        ),
        position="sticky",
        bg=styles.PAGE_BACKGROUND_COLOR,
        z_index="999",
        width="100%",
        top="0",
    )
