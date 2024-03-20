import reflex as rx

import link_bio.styles.styles as styles

def link_icon(url:str,image:str,alt:str) -> rx.Component:
    return rx.link(
        rx.image(src=image),
        href=url,
        is_external=True,
        spacing="2",
        width="2em",
        margin_top="5px",
        alt=alt
    )