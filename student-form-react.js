import React, { useState } from "react";

function Activity4() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h2>Student Form</h2>

            <form>
                <div>
                    <label>Name: </label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </div>

                <br />

                <div>
                    <label>Email: </label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
            </form>

            <h3>Live Preview</h3>
            <p>Name: {name}</p>
            <p>Email: {email}</p>
        </div>
    );
}

export default Activity4;
