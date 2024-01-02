import { ReactNode }  from "react";
import Typography from '@mui/material/Typography';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import 'bootstrap/dist/css/bootstrap.min.css';
import Col from 'react-bootstrap/Col';
import { StreamlitComponentBase, withStreamlitConnection } from "streamlit-component-lib";

interface BubbleState {
  message:string,
  image:string, 
  leftPosition:Boolean, 
  key:string,
  style:{
    textColor:string, backgroundColor:string, bubblePaddingRight:string, bubblePaddingLeft:string, 
    bubblePaddingBottom:string, bubblePaddingTop:string,
    fontWeight:string, bubbleBorderRadius:string, fontFamily:string
  }
}

document.body.style.backgroundColor = "transparent";

class ChatBubble extends StreamlitComponentBase<BubbleState>{
  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const { message, image, leftPosition, key, style } = this.props.args;
 
    const fontWeight=("fontWeight" in style? style["fontWeight"] : "525")
    const fontFamily=("fontFamily" in style? style["fontFamily"] : "itim")
    const BubbleStyle = {
      color: ("textColor" in style? style["textColor"] : "#534eb1"),
      backgroundColor: ("backgroundColor" in style? style["backgroundColor"] : "#f0efff"), // 
      paddingTop: ("bubblePaddingTop" in style? style["bubblePaddingTop"] : "7px"),
      paddingRight: ("bubblePaddingRight" in style? style["bubblePaddingRight"] : "10px"),
      paddingLeft: ("bubblePaddingLeft" in style? style["bubblePaddingLeft"] : "10px"),
      paddingBottom: ("bubblePaddingBottom" in style? style["bubblePaddingBottom"] : "7px"),
      "fontWeight": "100",
      maxWidth:"90%",
      borderRadius: ("bubbleBorderRadius" in style? style["bubbleBorderRadius"] : "2rem")
    };

    const userContainerStyle = {
      width:"98%", 
      // paddingTop:"10px", 
      // paddingBottom:"10px", 
      height: "fit-content", 
      justifyContent:"center"
    };

    const assistantContainerStyle = {
      width:"98%", 
      // paddingTop:"10px", 
      // paddingBottom:"10px", 
      backgroundColor:"transparent", 
      marginLeft: "5px", 
      height: "fit-content", 
      justifySelf:"end"
    };

    var src=process.env.PUBLIC_URL + "no_image.png";
    
    if(image!=null){
      try {
        let url;
        url = new URL(image);
        src=image;
      } catch (_) {
        src='data:image/png;base64,'+image;
      }
    }
    
    if (leftPosition){
      return (
        <Container key={key} fluid style={assistantContainerStyle}>
          <Row style={{backgroundColor:"transparent"}}>
            <Col xs={1} style={{backgroundColor:"transparent",width:"6%", paddingLeft:"5px", marginLeft: "30px",paddingTop: "2px"}}>
                <img alt="icon" src={src} height={35} />
            </Col>
            <Col xs={10} style={BubbleStyle}>
              <Typography style={{whiteSpace:"pre-line",fontFamily: fontFamily, fontWeight: fontWeight, wordWrap: "break-word",  padding: "5px"}}>
                    {message}
              </Typography>
            </Col>
            <Col xs={1}>
            </Col>
          </Row>
        </Container>
      );
    }
    return (
      <Container key={key} fluid style={userContainerStyle}>
        <Row style={{justifyContent:"end"}}>
          <Col xs={1}>
          </Col>
          <Col xs={10} style={BubbleStyle}>
            <Typography style={{textAlign:"right",whiteSpace:"pre-line",fontFamily: "itim", fontWeight: "525", wordWrap: "break-word",  padding: "5px",}}>
                  {message}
            </Typography>
          </Col>
          <Col xs={1}>
              <img alt="icon" src={src} height={43} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default withStreamlitConnection(ChatBubble);
