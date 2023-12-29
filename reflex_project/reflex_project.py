import reflex as rx
from reflex_project.components.navbar import navbar
from reflex_project.views.header.header import header
from reflex_project.views.cards.cards import cards
from reflex_project.views.video_academic.video_academic import video_academic
from reflex_project.views.footer.footer import footer
import reflex_project.styles.styles as styles



FONTS = [
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
    "https://fonts.googleapis.com/css2?family=Encode+Sans+Expanded:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
]


class State(rx.State):
    pass

@rx.page(route="/")
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                cards(),
                video_academic(),
                max_width=styles.MAX_WIDTH,
                color = "white",
            ),
            # bg=styles.PAGE_BACKGROUND_COLOR,
        ),
        footer(),
        bg=styles.PAGE_BACKGROUND_COLOR,
    )
    
@rx.page(route="/contact_me")
def contact_me() -> rx.Component:
    return rx.vstack(
        navbar(),
        footer()
    )
    
@rx.page(route="/portfolio")
def portfolio() -> rx.Component:
    return rx.vstack(
        navbar(),
        footer()
    )


app = rx.App(stylesheets=FONTS)
app.compile()
