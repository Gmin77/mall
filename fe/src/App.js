import React, { useEffect, useState } from "react";
import MyComponent from "./component/Home";

function App() {
  return (
    <div className="App">
      <MyComponent name="Alice" />
      <article>
        <h1>My First Component</h1>
        <ol>
          <li>Components: UI Building Blocks</li>
          <li>Defining a Component</li>
          <li>Using a Component</li>
        </ol>
      </article>
    </div>
  );
}

export default App;
