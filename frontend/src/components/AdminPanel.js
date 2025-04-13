import React, { useState, useEffect } from "react";
import axios from "../services/api";

function AdminPanel() {
    const [stats, setStats] = useState({});

    useEffect(() => {
        // Fetch user activity statistics
        axios.get("/admin/stats").then((response) => {
            setStats(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Admin Panel</h2>
            <h3>User Statistics:</h3>
            <p>Registered Users: {stats.totalUsers}</p>
            <p>Reviews Submitted: {stats.totalReviews}</p>
            <p>Positive Sentiments: {stats.positiveSentiments}</p>
            <p>Negative Sentiments: {stats.negativeSentiments}</p>
        </div>
    );
}

export default AdminPanel;
