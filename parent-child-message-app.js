import React, { useState } from "react";
import Assignment4Child from "./Assignment4Child";

function Assignment4Parent() {
    const [message, setMessage] = useState("");

    const receiveData = (data) => {
        setMessage(data);
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h2>Parent Component</h2>

            <Assignment4Child sendData={receiveData} />

            <h3>Message from Child:</h3>
            <p>{message}</p>
        </div>
    );
}

export default Assignment4Parent;
