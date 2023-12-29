import reflex as rx
import reflex_project.styles.styles as styles

def button_links(text: str, page_to_go: str, margin_left=styles.Spacer.MIN_MARGIN, margin_right=styles.Spacer.MIN_MARGIN) -> rx.Component:
    return rx.center(
        rx.button(
            f"{text}",
            color_scheme="facebook",
            margin_left=margin_left,
            margin_right=margin_right,
            bg=styles.PAGE_BACKGROUND_COLOR,
            on_click=rx.redirect(page_to_go),
        )
    )