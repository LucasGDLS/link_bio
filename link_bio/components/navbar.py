import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.chakra.box(
            rx.chakra.span("lucasgdls", color=Color.PRIMARY.value),
            rx.chakra.span("dev ", color=Color.SECONDARY.value),
            font_family=Font.LOGO.value,
            font_size=styles.Size.LARGE.value,
        ),
        href="index"
        ),
        position="sticky",
        bg="lightgray",
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0",
        background=Color.CONTENT.value,
        margin_bottom="20px"
    )