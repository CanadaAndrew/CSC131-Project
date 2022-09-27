import React from "react";
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './App.css';
//import {BrowserRouter as Router, Routes, Switch} from "react-router-dom"; // trying to entry and results page
//import { useNavigate } from "react-router-dom"; // trying to connect entry and results page
//let navigate = useNavigate(); // onClick={()=>{navigate('/results')}}

const theme1 = createTheme({
    typography: 
    {
        fontFamily: [  '"Segoe UI Symbol"',  ].join(','),
        fontSize: 24,
    },
    palette: 
    {
        primary: {main: "#ff8f00" }, // this changes the textbox to orange?

        background: 
        {
            default: "#666666" //changes whole page background to gray
        },
      },
  });

const App = () => {
    return(
        <ThemeProvider theme={theme1}> {/* ThemeProvider uses the theme function above*/}
        <div>
         <CssBaseline /> {/* This enables changing background color*/}
            <Typography align= "center" color="common.black" >    {/*Typography enables text editing*/}
            <img src="/images/IMG_1183.JPG" alt=""/> {/*USA image for home page*/}
            <h1 id="h1"  > SS# Background Check</h1>
            <TextField id="filled-basic" label="Social Security #" variant="filled" />
            <button>Enter</button> {/*button to link entry and results page*/}
            </Typography>
            
           
        </div>
        </ThemeProvider>
  
    )
}

export default App;