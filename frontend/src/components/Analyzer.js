import React, { useState } from "react";
import axios from "../services/api";

function Analyzer() {
    const [review, setReview] = useState("");
    const [result, setResult] = useState(null);

    const analyzeReview = () => {
        axios.post("/analyze", { review }).then((response) => {
            setResult(response.data);
        });
    };

    return (
        <div>
            <h2>Analyze Movie Review</h2>
            <textarea
                value={review}
                onChange={(e) => setReview(e.target.value)}
                placeholder="Paste your movie review here..."
            ></textarea>
            <button onClick={analyzeReview}>Analyze</button>
            {result && (
                <div>
                    <h3>Sentiment: {result.sentiment}</h3>
                    <p>Review: {result.review}</p>
                </div>
            )}
        </div>
    );
}

export default Analyzer;
