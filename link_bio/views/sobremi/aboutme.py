import reflex as rx
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font


def bodyabout()-> rx.Component:
    return rx.image(
        src="/backaboutme.jpg",
        margin_top="-20px",
        padding="0",
        opacity="0.2",
        _hover={"opacity": "1"}



    )