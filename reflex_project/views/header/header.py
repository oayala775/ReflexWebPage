import reflex as rx
import reflex_project.styles.styles as styles

def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.avatar(
                src="personal_image.jpg",
                size="xl"
            ), 
            rx.text("Omar Ayala")
        ),
        rx.spacer(),
        rx.text("""I'm an undergraduate of Computer Science Bachelor at University of Guadalajara, considering myself a passionate student, family person and a science advocate. Passionate about soccer, self development, cooking and photography."""),
        width="100%"
    )

