import React from "react";

// 함수형 컴포넌트 정의
function MyComponent(props) {
  return (
    <div>
      <h1>Hello, {props.name}!</h1>
      <p>This is a functional component.</p>
    </div>
  );
}

export default MyComponent;
