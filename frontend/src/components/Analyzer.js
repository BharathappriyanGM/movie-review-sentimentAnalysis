import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Analyzer.css';

// Icons
import { FaStar, FaStarHalfAlt, FaRegStar } from 'react-icons/fa';
import { BiCameraMovie, BiLoaderAlt } from 'react-icons/bi';
import { MdSentimentSatisfiedAlt, MdSentimentDissatisfied, MdSentimentNeutral } from 'react-icons/md';

const Analyzer = () => {
  // State variables
  const [reviewText, setReviewText] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [charCount, setCharCount] = useState(0);
  
  // Handle input changes and count characters
  const handleInputChange = (e) => {
    const text = e.target.value;
    setReviewText(text);
    setCharCount(text.length);
  };
  
  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!reviewText.trim()) {
      setError('Please enter a movie review to analyze');
      return;
    }
    
    setIsLoading(true);
    setError('');
    
    try {
      const response = await axios.post('http://localhost:8000/analyze/', {
        review_text: reviewText
      });
      
      setAnalysis(response.data);
      setIsLoading(false);
    } catch (err) {
      console.error('Error analyzing review:', err);
      setError(err.response?.data?.detail || 'Failed to analyze the review. Please try again.');
      setIsLoading(false);
    }
  };
  
  // Clear form and results
  const handleClear = () => {
    setReviewText('');
    setAnalysis(null);
    setError('');
    setCharCount(0);
  };
  
  // Generate rating stars based on confidence score
  const renderRatingStars = (confidence) => {
    // Convert confidence to a 5-star scale
    const rating = confidence * 5;
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    
    const stars = [];
    
    // Add full stars
    for (let i = 0; i < fullStars; i++) {
      stars.push(<FaStar key={`full-${i}`} className="star filled" />);
    }
    
    // Add half star if needed
    if (hasHalfStar) {
      stars.push(<FaStarHalfAlt key="half" className="star half" />);
    }
    
    // Add empty stars
    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<FaRegStar key={`empty-${i}`} className="star empty" />);
    }
    
    return stars;
  };
  
  // Get sentiment icon based on sentiment
  const getSentimentIcon = (sentiment) => {
    switch (sentiment.toLowerCase()) {
      case 'positive':
        return <MdSentimentSatisfiedAlt className="sentiment-icon positive" />;
      case 'negative':
        return <MdSentimentDissatisfied className="sentiment-icon negative" />;
      default:
        return <MdSentimentNeutral className="sentiment-icon neutral" />;
    }
  };
  
  // Get confidence bar color based on sentiment
  const getConfidenceColor = (sentiment) => {
    switch (sentiment.toLowerCase()) {
      case 'positive':
        return '#4CAF50';
      case 'negative':
        return '#F44336';
      default:
        return '#607D8B';
    }
  };
  
  // Format confidence percentage
  const formatConfidence = (confidence) => {
    return (confidence * 100).toFixed(1) + '%';
  };
  
  return (
    <div className="analyzer-container">
      <div className="analyzer-header">
        <BiCameraMovie className="movie-icon" />
        <h1>Movie Review Sentiment Analyzer</h1>
        <p className="subtitle">Analyze your movie reviews with advanced AI models</p>
      </div>
      
      <div className="analyzer-content">
        <div className="input-section">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="reviewText">
                <span>Enter your movie review</span>
                <span className="char-count">{charCount}/1000</span>
              </label>
              <textarea
                id="reviewText"
                value={reviewText}
                onChange={handleInputChange}
                placeholder="Type or paste your movie review here..."
                maxLength={1000}
                rows={8}
                disabled={isLoading}
              />
            </div>
            
            {error && <div className="error-message">{error}</div>}
            
            <div className="button-group">
              <button 
                type="submit" 
                className="analyze-button"
                disabled={isLoading || !reviewText.trim()}
              >
                {isLoading ? (
                  <>
                    <BiLoaderAlt className="spinner" />
                    Analyzing...
                  </>
                ) : 'Analyze Sentiment'}
              </button>
              
              <button 
                type="button" 
                className="clear-button"
                onClick={handleClear}
                disabled={isLoading || (!reviewText && !analysis)}
              >
                Clear
              </button>
            </div>
          </form>
          
          {isLoading && (
            <div className="loading-overlay">
              <div className="loading-content">
                <BiLoaderAlt className="loading-spinner" />
                <p>Analyzing your review...</p>
              </div>
            </div>
          )}
        </div>
        
        {analysis && (
          <div className="results-section">
            <div className="results-header">
              <h2>Analysis Results</h2>
              <div className="divider"></div>
            </div>
            
            <div className={`sentiment-card ${analysis.sentiment.toLowerCase()}`}>
              <div className="sentiment-header">
                {getSentimentIcon(analysis.sentiment)}
                <h3>Overall Sentiment: <span>{analysis.sentiment}</span></h3>
              </div>
              
              <div className="confidence-container">
                <div className="confidence-label">
                  <span>Confidence:</span>
                  <span>{formatConfidence(analysis.confidence)}</span>
                </div>
                <div className="confidence-bar-container">
                  <div 
                    className="confidence-bar-fill" 
                    style={{ 
                      width: `${analysis.confidence * 100}%`,
                      backgroundColor: getConfidenceColor(analysis.sentiment)
                    }}
                  ></div>
                </div>
              </div>
              
              <div className="rating-stars">
                {renderRatingStars(analysis.confidence)}
              </div>
            </div>
            
            {analysis.themes && analysis.themes.length > 0 && (
              <div className="themes-section">
                <h3>Detected Themes</h3>
                <div className="themes-container">
                  {analysis.themes.map((theme, index) => (
                    <span key={index} className="theme-tag">
                      {theme}
                    </span>
                  ))}
                </div>
              </div>
            )}
            
            <div className="models-section">
              <h3>Model Breakdown</h3>
              <div className="models-grid">
                {analysis.model_breakdown && Object.entries(analysis.model_breakdown).map(([model, data]) => (
                  <div key={model} className="model-card">
                    <h4>{model.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}</h4>
                    <div className={`model-sentiment ${data.sentiment}`}>
                      {getSentimentIcon(data.sentiment)}
                      <span>{data.sentiment}</span>
                    </div>
                    <div className="model-confidence">
                      <div className="confidence-label">
                        <span>Confidence:</span>
                        <span>{formatConfidence(data.confidence)}</span>
                      </div>
                      <div className="confidence-bar-container">
                        <div 
                          className="confidence-bar-fill" 
                          style={{ 
                            width: `${data.confidence * 100}%`,
                            backgroundColor: getConfidenceColor(data.sentiment)
                          }}
                        ></div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Analyzer;