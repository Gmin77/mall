import React from 'react';
import '../css/Main.css'

function Main(){
    return(
        <main>
            <section id="home">
                <h2>home</h2>
                <p>Welcome tothe best Mall experinece online!</p>
            </section>
            <section id="products">
                <h2>Products 1</h2>
                <div className='product-list'>
                    <div className='product-item'>
                        <h3>Product 1</h3>
                        <p>Description of product 1</p>
                    </div>               
                    <div className='product-item'>
                        <h3>Product 2</h3>
                        <p>Description of product 2</p>
                    </div>               
                </div>
            </section>
            <section id="about">
                <h2>About</h2>
                <p>Learn more about our Mall.</p>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <p>Get in touch with us.</p>
            </section>
        </main>
    )
}

export default Main;