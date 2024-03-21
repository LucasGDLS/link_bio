import reflex as rx
from link_bio.components.link_button import link_button
import link_bio.constanst as const

def links() -> rx.Component:
    return rx.vstack(
        link_button("Sobre Mí","Acá podes conocerme un poco", "./aboutme"),
        link_button("Mis Projectos","Conoce algunos de mis projectos", "./misprojectos"),
        link_button("GitHub","Mi repositorio de GitHub", "https://github.com/LucasGDLS"),
        link_button("Email",
                "lucasgdls@hotmail.com",
            f"mailto:{const.EMAIL}"
            ),
        width="100%"
    )