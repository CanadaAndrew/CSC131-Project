import React from 'react'; //placeHolder for results page
import { useNavigate } from "react-router-dom";

function Results() {
    const navigate = useNavigate();
    return(
        <div>
            <h1>PlaceHolder for results page with temporary button</h1>
            <button onClick={()=>{navigate("/Mastpage");}}>return</button> {/*button to link master and results page*/}
        </div>
    )
}

export default Results;