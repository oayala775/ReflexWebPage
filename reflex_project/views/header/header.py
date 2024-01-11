import reflex as rx
import reflex_project.styles.styles as styles

def header() -> rx.Component:
    return rx.hstack(
        rx.responsive_grid(
            rx.vstack(
                rx.avatar(
                    src="personal_image.jpg",
                    size="xl"
                ), 
                rx.heading("Omar Ayala", size="md")
            ),
            rx.spacer(),
            rx.mobile_only(
                rx.text(
                    """I'm an undergraduate of Computer Science Bachelor at University of Guadalajara, considering myself a passionate student, family person and a science advocate. Passionate about soccer, self development, cooking and photography.""",
                ),
                margin_left = styles.Spacer.MEDIUM_MARGIN
            ),
            rx.tablet_and_desktop(
                rx.text(
                    """I'm an undergraduate of Computer Science Bachelor at University of Guadalajara, considering myself a passionate student, family person and a science advocate. Passionate about soccer, self development, cooking and photography.""",
                )
            )
        ),
        columns=[1,2],
        gap=4
    )

