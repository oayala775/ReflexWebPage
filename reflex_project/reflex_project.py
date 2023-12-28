import reflex as rx
from reflex_project.components.navbar import navbar
from reflex_project.views.header.header import header


FONTS = [
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
    "https://fonts.googleapis.com/css2?family=Encode+Sans+Expanded:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
]


class State(rx.State):
    pass

@rx.page(route="/")
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        )
    
@rx.page(route="/contact_me")
def contact_me() -> rx.Component:
    return rx.vstack(
        navbar(),
    )
    
@rx.page(route="/portfolio")
def portfolio() -> rx.Component:
    return rx.vstack(
        navbar(),
    )


app = rx.App(stylesheets=FONTS)
# app.add_page(index)
# app.add_page(contact_me)
app.compile()
