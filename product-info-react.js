import React, { useState } from "react";

function Activity3() {
    const [product] = useState({
        name: "Laptop",
        price: "₹80,000",
        brand: "Dell",
        category: "Electronics",
        stock: "Available"
    });

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>Product Information</h1>

            <p><b>Name:</b> {product.name}</p>
            <p><b>Brand:</b> {product.brand}</p>
            <p><b>Category:</b> {product.category}</p>
            <p><b>Price:</b> {product.price}</p>
            <p><b>Stock Status:</b> {product.stock}</p>

        </div>
    );
}

export default Activity3;
