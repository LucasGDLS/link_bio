import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Sobre Mí","Acá podes conocerme un poco", "./aboutme","Sobre Mí"),
        link_button("Mis Projectos","Conoce algunos de mis projectos", "./misprojectos","Mis projectos"),
        link_button("Contactame", "Contactate conmigo aquí","./contactame","Contactame"),
        link_button("GitHub","Mi repositorio de GitHub", "https://github.com/LucasGDLS","github"),
        width="100%"
    )