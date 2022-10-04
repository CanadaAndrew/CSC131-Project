import React from "react";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { useState } from "react";

const theme1 = createTheme({
  typography: {
    fontFamily: ['"Segoe UI Symbol"'].join(","),
    fontSize: 24,
  },
  palette: {
    primary: { main: "#ffffff" }, // this changes the textbox to white

    background: {
      default: "#13265C", //changes whole page background to gray
    },
  },
});

{
  /*value = {value} onChange={e => setValue(e.target.value)} error = {!value} helperText = {!value ? 'Required' : 'Do not share your password with anyone'} use for textinput*/
}
const App = () => {
  const [value, setValue] = useState("");
  const ALPHA_NUMERIC_DASH_REGEX = /^[0-9\b]+$/;

  return (
    <ThemeProvider theme={theme1}>
      {" "}
      {/* ThemeProvider uses the theme function above*/}
      <div>
        <CssBaseline /> {/* This enables changing background color*/}
        <Typography align="center" color="common.white">
          {" "}
          {/*Typography enables text editing*/}
          <h1 id="h1"> SS# Background Check</h1>
          <TextField
            onKeyDown={(event) => {
              if (!ALPHA_NUMERIC_DASH_REGEX.test(event.key) && event.key !== "Backspace") 
              {
                {
                  /* regex code above wont work with backspace*/
                }
                event.preventDefault();
              } else if (value.length === 9 && event.key !== "Backspace") {
                event.preventDefault();
              }
            }}
            onChange={(e) => setValue(e.target.value)}
            helperText={
              value.length != 9 && value.length != 0
                ? "SS# length is invalid"
                : " "
            }
            error={value.length < 9 && value.length != 0}
            id="filled-basic"
            label="Social Security #"
            variant="outlined"
            sx={{ input: { color: "white" } }}
          />
        </Typography>
      </div>
    </ThemeProvider>
  );
};

export default App;
