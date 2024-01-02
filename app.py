import streamlit as st
from streamlit_custom_chat_bubble import ChatBubble
import base64
from key_generator.key_generator import generate

st.set_page_config(layout="wide")

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "jpg"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         [data-testid="stHeader"] {{
          background-color: rgba(0,0,0,0);
        }}
        [data-testid="baseButton-secondary"]{{
            border-radius:2rem;
            height: 47px;
            border-color: transparent;
            background-color: #fef8ff;
            font-family: 'Itim';
        }}
        [data-testid="baseButton-secondary"]:hover{{
            border-radius:2rem;
            height: 47px;
            border-color: transparent;
            background-color: #fdf4ff;
            color:black;
            font-family: 'Itim';
        }}
        .stChatFloatingInputContainer{{
            background-color: transparent;
        }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack("images\pastel3.jpg") 


def set_page_container_style(
        max_width: int = 1400, max_width_100_percent: bool = False,
        padding_top: int = 2, padding_right: int = 0, padding_left: int = 1, padding_bottom: int = 1,
        # color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
    if max_width_100_percent:
        max_width_str = f'max-width: 100%;'
    else:
        max_width_str = f'max-width: {max_width}px;'
    st.markdown(
        f'''
        <style>
            
            [data-testid="block-container"]{{
                {max_width_str}
                padding-top: {padding_top}rem;
                padding-right: {padding_right}rem;
                padding-left: {padding_left}rem;
                padding-bottom: {padding_bottom}rem;
                
            }}
        </style>
            
        ''',
        unsafe_allow_html=True,
    )

# Read the image as bytes
with open("images/robot_icon.png", "rb") as image_file:
    image_bytes = image_file.read()

# Encode the image as Base64
encoded_image0 = base64.b64encode(image_bytes).decode("utf-8")
with open("images/person_icon.png", "rb") as image_file:
    image_bytes = image_file.read()

encoded_image1 = base64.b64encode(image_bytes).decode("utf-8")


def refresh(key:str):
    del st.session_state[key]
    st.rerun()
    
set_page_container_style()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"image":encoded_image0,"message":"Hello! How may I help you?","key":"0", "leftPosition":True})
    st.session_state.messages.append({"image":encoded_image1,"message":"Tell me a riddle!","key":"1", "leftPosition":False})
    st.session_state.messages.append({"image":encoded_image0,"message":"Sometimes I fly as fast as the speed of light, sometimes I crawl as slow as a snail. Unknown until I am meausured, but you'll certainly miss me when I'm gone. What am I?","key":"2", "leftPosition":True})
    st.session_state.messages.append({"image":encoded_image1,"message":"A bird??","key":"3", "leftPosition":False})
    st.session_state.messages.append({"image":encoded_image0,"message":"Try again","key":"4", "leftPosition":True})
    st.session_state.messages.append({"image":encoded_image1,"message":"A plane?","key":"5", "leftPosition":False})
    st.session_state.messages.append({"image":encoded_image0,"message":"Try again","key":"6", "leftPosition":True})
    st.session_state.messages.append({"image":encoded_image1,"message":"Time!","key":"7", "leftPosition":False})
    st.session_state.messages.append({"image":encoded_image0,"message":"Correct!","key":"8", "leftPosition":True})
 

col1, col2 = st.columns([2,13]) 
   
with col1:
    st.markdown("#")
    st.markdown("#")
    st.markdown("#")

    if st.button(label="Nice!", key="nice"):
        key = generate()
        st.session_state.messages.append({"message":"Nice!","key":key.get_key(),"leftPosition":not (st.session_state.messages[-1]["leftPosition"])})
        refresh('nice')
        

with col2:
    
    for message in st.session_state.messages:
        style={}
        if not message["leftPosition"]:
            style={"backgroundColor":"rgb(216, 229, 255)"}
        img=None
        if "image" in message:
            img=message["image"]
        
        ChatBubble(message=message["message"], leftPosition=message["leftPosition"], image=img, style=style, key=message["key"])
    