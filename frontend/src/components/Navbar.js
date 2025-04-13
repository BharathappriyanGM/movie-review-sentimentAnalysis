import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav className="navbar">
            <h1>Movie Review Analyzer</h1>
            <ul>
                <li>
                    <Link to="/dashboard">Dashboard</Link>
                </li>
                <li>
                    <Link to="/analyzer">Analyze Review</Link>
                </li>
                <li>
                    <Link to="/admin">Admin Panel</Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
