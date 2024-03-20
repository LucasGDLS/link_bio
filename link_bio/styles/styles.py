import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

MAX_WIDTH="560px"

#Sizes 

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"



#Styles gral
    
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width":"100%",
        "heigth": "100%",
        "display":"block",
        "padding":Size.BIG.value,
        "border_radius": Size.SMALL.value,
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "font_family":Font.DEFAULT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover":{},
        "spacing":"3"
        
    },
    rx.avatar:{
        "margin":"0",
        "border":"4px solid",
        "border_color":Color.PRIMARY.value,
        "height": "auto"
    }


}

button_body_style= dict(
    font_size=Size.MEDIUM.value,
    width="100%",
    height="100%",
    margin_top="-1em",
    color=TextColor.BODY.value
)

button_title_style= dict(
    font_size=Size.DEFAULT.value,
    width="100%",
    height="100%",
    margin_top="-1em",
    color=TextColor.HEADER.value
)