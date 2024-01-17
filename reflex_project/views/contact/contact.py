import reflex as rx
import reflex_project.styles.styles as styles


def contact() -> rx.Component:
    return rx.responsive_grid(
        rx.center(
            rx.vstack(
                rx.text(
                    "Hello! If you want to get in touch with me, please fill this form, I'll be glad to answer",
                    color="white",
                ),
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="Name", name="name", width="100%"),
                        rx.input(
                            placeholder="your_email@example.com",
                            name="email",
                        ),
                        rx.text_area(placeholder="Enter your message here!"),
                        rx.button("Send!", type_="submit"),
                    ),
                    width="70%",
                ),
                padding=styles.Spacer.MEDIUM_MARGIN,
            ),
        ),
        rx.center(
            rx.vstack(
                rx.text(
                    "If you feel social, you can contact me through here!",
                    color="white",
                ),
                rx.box(
                    rx.hstack(
                        rx.link(
                            rx.image(src="/github.png", width="50px"),
                            href="https://github.com/oayala775",
                        ),
                        rx.link(
                            rx.image(src="/linkedin.png", width="50px"),
                            href="https://www.linkedin.com/in/omar-ayala-9a6058206/",
                        ),
                        rx.link(
                            rx.image(src="/twitter.png", width="50px"),
                            href="https://github.com/oayala775",
                        ),
                    ),
                ),
                padding=styles.Spacer.MEDIUM_MARGIN,
            ),
        ),
        width="100%",
        bg=styles.PAGE_BACKGROUND_COLOR,
        padding_y=styles.Spacer.MEDIUM_MARGIN,
        columns=[1, 2],
        height="80vh",
    )
