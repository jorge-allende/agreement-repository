import React from "react";

const APIDocs = () => {
  return (
    <div style={{ backgroundColor: "white", minHeight: "100vh", padding: "20px" }}>
      <h2>API Testing</h2>
      <iframe
        src="http://localhost:8000/api-testing"
        style={{ width: "100%", height: "80vh", border: "none" }}
        title="API Testing"
      ></iframe>
    </div>
  );
};

export default APIDocs;
