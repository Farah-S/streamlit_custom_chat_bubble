# streamlit_custom_chat

![bubbles_example](https://github.com/Farah-S/streamlit_custom_chat_bubble/blob/main/streamlit_custom_chat_bubble/frontend/public/bubble_example.png)

Streamlit custom chat messages with ability to style them. The parameters are as follow:

Args:

    message (string, optional): 
        Messages that will be displayed.
    
    image (string, optional):
        The icon that will be displayed next to the message, can be empty.
    
    leftPosition (boolean, optional):
        If true the message and icon will be aligned to the left, if False then the
        message and icon will be aligned to the right.
    
    key (string, optional): 
        Uniquely identifies the message instance. Defaults to None.
    
    style (dict, optional): 
        Allows the customization of the chat bubble style with CSS. 
        The values that can be changed and their default values are {
            
            textColor:"#534eb1", 
            backgroundColor:"#f0efff", 
            paddingRight:"10px", 
            paddingLeft:"10px", 
            paddingBottom:"7px", 
            paddingTop:"7px",
            fontWeight:"525", 
            borderRadius:"2rem", 
            fontFamily:"itim",
            imageHeight:35
            
        }.

Returns:
  None

## Installation instructions

```sh
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps streamlit_custom_chat_bubble
```

## Usage instructions

Example of how to use without customization

```python
import streamlit as st

from streamlit_custom_chat_bubble import ChatBubble

ChatBubble(message="Hello!", key="0")

```

Example of how to use with customization

```python
import streamlit as st

from streamlit_custom_chat_bubble import ChatBubble

ChatBubble(message="Hello!", leftPosition=True, image="", key="0", style={"backgroundColor":"rgb(216, 229, 255)"})

```
