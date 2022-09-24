import React from "react";
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';


const App = () => {
    return(
        <div>
           
            <Typography align= "center" >    {/*Typography enables text editing*/}
            <h1 id="h1"  > SS# Background Check</h1>
            <TextField id="filled-basic" label="Social Security #" variant="filled" />

            </Typography>
        </div>
        
  
    )
}

export default App;