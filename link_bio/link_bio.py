import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles
from link_bio.views.sobremi.aboutme import bodyabout
from link_bio.views.sobremitext.sobremitext import sobremitext

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

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.add_page(aboutme)