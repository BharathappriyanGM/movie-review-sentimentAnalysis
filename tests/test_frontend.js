import React from "react";
import { render, screen } from "@testing-library/react";
import Navbar from "../components/Navbar";
import Dashboard from "../components/Dashboard";
import Analyzer from "../components/Analyzer";
import axios from "axios";

jest.mock("axios"); // Mock Axios calls

// Test Navbar rendering
test("renders Navbar component", () => {
    render(<Navbar />);
    expect(screen.getByText(/Movie Review Analyzer/i)).toBeInTheDocument();
});

// Test Dashboard rendering
test("renders Dashboard component", () => {
    render(<Dashboard />);
    expect(screen.getByText(/Welcome to your Dashboard/i)).toBeInTheDocument();
});

// Test Analyzer component rendering
test("renders Analyzer component", () => {
    render(<Analyzer />);
    expect(screen.getByText(/Analyze Movie Review/i)).toBeInTheDocument();
});

// Test API call to /analyze endpoint
test("calls analyze API successfully", async () => {
    axios.post.mockResolvedValueOnce({
        data: { review: "Fantastic!", sentiment: "positive" }
    });

    const response = await axios.post("/analyze", { review: "Fantastic!" });
    expect(response.data.sentiment).toBe("positive");
});
