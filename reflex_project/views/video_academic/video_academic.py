import reflex as rx
import reflex_project.styles.styles as styles

def video_academic() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.heading("Academic Formation"),
            margin_y=styles.Spacer.MEDIUM_MARGIN
        ),
        rx.hstack(
            rx.card(
                rx.video(
                    url="https://www.youtube.com/watch?v=PQChtGb3L8M",
                    width="100%"
                ),
                header=rx.center(
                    rx.heading("CETI Colomos",size="md"),
                ),
                width="30em"
            ),
            rx.card(
                rx.video(
                    url="https://www.youtube.com/watch?v=kGJHgmVR9NU",
                    width="100%"
                ),
                header=rx.center(
                    rx.heading("CUCEI",size="md"),
                ),
                width="30em"
            )
        ),
        width="100%"
    )