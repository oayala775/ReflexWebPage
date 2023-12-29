import reflex as rx
import reflex_project.styles.styles as styles
import datetime

def footer() -> rx.Component:
    return rx.hstack(    
        rx.flex(
            rx.spacer(),
            rx.text(
                f"© 2021 - {datetime.date.today().year} LOVING SOFTWARE SINCE DISCOVERED IT ❤️",
                color="white"
            ),
            rx.spacer(),
            width="100%",
            padding_y = styles.Spacer.MAX_MARGIN,
        ),
        bg=styles.PAGE_BACKGROUND_COLOR,
        z_index="999",
        width="100%",
    )