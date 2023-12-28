import reflex as rx

def button_links(text: str, page_to_go: str) -> rx.Component:
    # return rx.button(
    #             f"{text}",
    #             bg="#003366",
    #             color="white",
    #             variant="link",
    #             margin_right="20px",
    #             on_click=rx.link(f"{text}",href=f"/{page_to_go}")
    #         )
    return rx.center(
        rx.link(
            rx.button(
                f"{text}",
                bg="#003366",
                color="white",
                variant="link",
                margin_right="20px",
                ),
            href=f"/{page_to_go}",
        )
    )
