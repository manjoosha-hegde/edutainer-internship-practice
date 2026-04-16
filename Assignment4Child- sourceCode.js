import React from "react";

function Assignment4Child(props) {
    const sendMessage = () => {
        props.sendData("Hello from Child Component!");
    };

    return (
        <div>
            <h3>Child Component</h3>
            <button onClick={sendMessage}>Send Message to Parent</button>
        </div>
    );
}

export default Assignment4Child;