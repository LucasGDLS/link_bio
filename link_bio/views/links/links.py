import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Sobre Mí","Acá podes conocerme un poco", "./aboutme","Sobre Mí"),
        link_button("Mis Projectos","Conoce algunos de mis projectos", "http://www.google.com","Mis projectos"),
        link_button("Contactame", "Contactate conmigo aquí","http://www.google.com","Linkedin"),
        link_button("GitHub","Mi repositorio de GitHub", "http://www.google.com","github"),
        width="100%"
    )