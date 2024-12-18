import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [message, setMessage] = useState("");
  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchProtectedData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/hello", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setMessage(response.data.message);
      } catch (err) {
        setMessage("Failed to load data. Please log in again.");
      }
    };

    fetchProtectedData();
  }, [token]);

  return (
    <div>
      <h2>Dashboard</h2>
      <p>{message}</p>
    </div>
  );
};

export default Dashboard;
