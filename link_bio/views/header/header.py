import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
def header() -> rx.Component:
    return rx.vstack(
    rx.avatar(fallback="LG",src="avatar.png",size="9",radius="full",alt="Mi Avatar"),
    rx.text("Lucas Gabriel", weight="bold", size="4",color=TextColor.HEADER.value,font_family=Font.TITLE.value),
    rx.text("@lucasgabrieldls",margin_top="0px important!",color=Color.PRIMARY.value,font_family=Font.DEFAULT.value),
    rx.hstack(
        link_icon("www.facebook.com/lucasgabrieldls","facebook.png","ir a mi facebook"),
        link_icon("www.instagram.com/lucasgabrieldls","instagram.png","ir a mi instagram"),
        link_icon("www.linkedin.com/lucasgabrieldls","linkedin.png","ir a mi linkedin")

    ),
    
    direction="column",
    spacing="1",
    align="center",
    justify="center",
    is_external="true"
    
)