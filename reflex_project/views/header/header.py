import reflex as rx


def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.avatar("Omar Ayala", size="xl"), 
            rx.text("Omar Ayala")
        ),
        rx.text("""I'm an undergraduate of Computer Science Bachelor at University of Guadalajara, considering myself a passionate student, family person and a science advocate. Passionate about soccer, self developing, cooking and photography.""", padding_left="20px"),
        padding="50px"
        )
