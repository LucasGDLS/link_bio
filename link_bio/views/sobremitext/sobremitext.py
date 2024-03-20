import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
from link_bio.styles.styles import Size as Size
def sobremitext()-> rx.Component:
    return rx.box(
         rx.vstack(
             rx.text("Mi Historia", 
                     color=TextColor.HEADER.value,
                     font_family=Font.TITLE.value,
                     size="9",
                     align_text="center"),
             rx.text('''Mi nombre es Lucas Gabriel De Los Santos, futuro ingeniero en sistemas.''' '''Nací en Buenos Aires, Argentina. Actualmente estoy viviendo en Villa Constitución, Santa Fe. Estudie en la UBA de derecho hasta cuarto año pero siempre sentí que mi vocación y lo que yo quiero para mi vida iba para otro lado, siempre amé la tecnologia, los programas, el pensar todo lo que venía de fondo y estudie de forma autodidacta desarrollo web y distintos lenguajes, los primeros lenguajes que estudie fue javascript y python. Estoy con las esperanzas a mil de conseguir un trabajo en IT y dar lo mejor de mí. Mis hobbies son escuchar música, salir con amigos, estar con mi pareja viendo animes y cantar.''',
                     color=TextColor.BODY.value,
                     font_family=Font.DEFAULT.value,
                     size="4"),
             spacing="8",
             padding=Size.DEFAULT.value,
             width="100%",
             height="auto",

         ),
         width="100%"


    )