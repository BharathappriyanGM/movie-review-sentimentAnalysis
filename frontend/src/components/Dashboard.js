import React, { useState, useEffect } from "react";
import axios from "../services/api";

function Dashboard() {
    const [preferences, setPreferences] = useState([]);
    const [history, setHistory] = useState([]);

    useEffect(() => {
        // Fetch user preferences and review history
        axios.get("/dashboard").then((response) => {
            setPreferences(response.data.preferences);
            setHistory(response.data.history);
        }).catch((error) => {
            console.error("Error fetching dashboard data:", error);
        });
        
    }, []);

    return (
        <div>
            <h2>Welcome to your Dashboard</h2>
            <h3>Your Preferences:</h3>
            <ul>
                {preferences.map((genre, index) => (
                    <li key={index}>{genre}</li>
                ))}
            </ul>
            <h3>Review History:</h3>
            <ul>
                {history.map((review, index) => (
                    <li key={index}>{review}</li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;
