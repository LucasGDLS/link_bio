import reflex as rx
import link_bio.styles.styles as styles


def link_button(title : str,body: str, url:str,alt:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    margin_top="-0.8em",
                    width=styles.Size.BIG.value,
                    heigth=styles.Size.BIG.value,
                    #margin=styles.Size.MEDIUM.value

                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style,width="100%"),
                    rx.text(body,style=styles.button_body_style,width="100%"),
                    align_item="start",
                    margin="0px",
                    spacing="3"

                )
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        alt="alt"
    )
