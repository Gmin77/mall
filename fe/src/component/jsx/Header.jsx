import React from "react"
import '../css/Header.css';

function Header(){
    return(
        <header className="App-header">
            <h1>Welcome to the Mall</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#home">Products</a></li>
                    <li><a href="#home">About</a></li>
                    <li><a href="#home">Contact</a></li>
                </ul>
            </nav>
        </header>
    )
}

export default Header;