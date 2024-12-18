import React, { useState } from "react";
import "./Login.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/login", {
        username,
        password,
      });
      const token = response.data.access_token;
      localStorage.setItem("token", token); // Save the token
      navigate("/dashboard"); // Redirect to Dashboard
    } catch (err) {
      setError("Invalid username or password");
    }
  };

  return (
    <div>
      <div className="background">
        <div className="shape"></div>
        <div className="shape"></div>
      </div>
      <form onSubmit={handleLogin}>
        <h3>Login Here</h3>
        {error && <p style={{ color: "red", textAlign: "center" }}>{error}</p>}

        <label htmlFor="username">Username</label>
        <input
          type="text"
          placeholder="Email or Phone"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label htmlFor="password">Password</label>
        <input
          type="password"
          placeholder="Password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Log In</button>

        <div className="social">
          <div className="go">
            <i className="fab fa-google"></i> Google
          </div>
        </div>
      </form>
    </div>
  );
};

export default Login;
