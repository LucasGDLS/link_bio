import reflex as rx
import datetime
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.styles import Size as Size
from link_bio.styles.fonts import Font as Font

def footer() -> rx.Component:
    return rx.vstack(
        #rx.image(src="favicon.ico"),
        rx.text(f"2022-{datetime.date.today().year} Building Sotfware from Argentina♥"),
        rx.text("Creado con Reflex by LucasGDLS"),
        color=TextColor.FOOTER.value,
        height="100%",
        background_color=Color.CONTENT.value,
        #margin_bottom=Size.BIG.value,
        padding_bottom=Size.SMALL.value,
        padding_top=Size.SMALL.value,
        position="center",
        align="center",
        font_family=Font.DEFAULT.value
        
        
    )