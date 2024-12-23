import React, { useEffect } from "react";

const RapiDoc = () => {
  useEffect(() => {
    // Dynamically add the RapiDoc script when the component mounts
    const script = document.createElement("script");
    script.src = "https://unpkg.com/rapidoc/dist/rapidoc-min.js";
    script.type = "module";
    document.head.appendChild(script);

    // Clean up the script on component unmount
    return () => {
      document.head.removeChild(script);
    };
  }, []);

  return (
    <div style={{ margin: "20px" }}>
      <rapi-doc
        spec-url="http://localhost:8000/static/openapi.json"
        theme="light"
        nav-bg-color="#1A003F"
        nav-text-color="#FFFFFF"
        nav-hover-bg-color="#2A104F"
        nav-hover-text-color="#FFFFFF"
        nav-accent-color="#FF791A"
        nav-accent-text-color="#FFFFFF"
        nav-active-item-marker="colored-block"
        nav-item-spacing="default"
        render-style="focused"
        use-path-in-nav-bar="false"
        show-method-in-nav-bar="true"
        show-header="false"
        style={{
          width: "100%",
          margin: "0 auto",
          padding: "20px",
          boxSizing: "border-box",
          backgroundColor: "#ffffff",
          borderRadius: "8px",
          boxShadow: "0px 4px 12px rgba(0, 0, 0, 0.2)",
        }}
      ></rapi-doc>
    </div>
  );
};

export default RapiDoc;

