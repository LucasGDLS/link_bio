import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles
from link_bio.views.sobremi.aboutme import bodyabout
from link_bio.views.sobremitext.sobremitext import sobremitext
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import Font as Font
from link_bio.styles.colors import TextColor as TextColor


class State(rx.State):
    pass
def index():
    return rx.box(
        navbar(),
        header(),
        rx.center(
            rx.vstack(           
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
            )

        ),
        footer()
    )
def aboutme():
    return rx.box(
        navbar(),
        rx.box(
            rx.hstack(
                rx.box(
                    bodyabout(),
                    width="30%"
                ),
                rx.box(
                    sobremitext(),
                    max_width=styles.MAX_WIDTH,
                    width="70%",
                )
            )
        ),
        footer(),
        width="100%",
    )

def misprojectos():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(           
                rx.text("Proximamente..", size="9", color= TextColor.HEADER.value, font_family= Font.TITLE.value,width="100%",height="474px", text_align="center",padding="50px"),
                
            ),
        ),
        footer(),
        width="100%",
        height="100%",
    )

def contactame():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(           
                rx.text("Proximamente..", size="9", color= TextColor.HEADER.value, font_family= Font.TITLE.value,width="100%",height="474px", text_align="center",padding="50px"),
                
            ),
        ),
        footer(),
        width="100%",
        height="100%",
    )



app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.add_page(aboutme)
app.add_page(misprojectos)
app.add_page(contactame)
