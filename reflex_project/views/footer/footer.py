import reflex as rx
import reflex_project.styles.styles as styles
import datetime

def footer() -> rx.Component:
    return rx.hstack(    
        rx.flex(
            rx.mobile_only(
                rx.text(
                    f"© 2021 - {datetime.date.today().year} LOVING SOFTWARE SINCE DISCOVERED IT ❤️",
                    color="white", margin_left=styles.Spacer.MAX_MARGIN
                ),
            ),
            rx.tablet_and_desktop(
                rx.text(
                    f"© 2021 - {datetime.date.today().year} LOVING SOFTWARE SINCE DISCOVERED IT ❤️",
                    color="white"
                ),
            ),
            width="100%",
            padding_y = styles.Spacer.MAX_MARGIN,
            justify="center",
            align="center"
        ),
        bg=styles.PAGE_BACKGROUND_COLOR,
        width="100%",
    )