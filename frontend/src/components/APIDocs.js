import React from "react";

const APIDocs = () => {
  return (
    <div>
      <h2>API Documentation</h2>
      <iframe
        src="http://localhost:8000/docs"
        style={{ width: "100%", height: "80vh", border: "none" }}
        title="API Documentation"
      ></iframe>
    </div>
  );
};

export default APIDocs;
