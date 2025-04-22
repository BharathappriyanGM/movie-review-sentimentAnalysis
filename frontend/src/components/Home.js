import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

// Icons
import { FaRobot, FaBrain, FaChartBar, FaDatabase, FaReact } from 'react-icons/fa';
import { BiCameraMovie } from 'react-icons/bi';
import { MdSentimentSatisfiedAlt, MdSentimentDissatisfied } from 'react-icons/md';
import { AiOutlineArrowRight } from 'react-icons/ai';

const Home = () => {
  return (
    <div className="home-container">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <BiCameraMovie className="hero-icon" />
          <h1>Movie Review Sentiment Analysis</h1>
          <p className="hero-subtitle">
            Analyze movie reviews instantly with our advanced AI-powered sentiment analysis platform
          </p>
          <div className="hero-cta">
            <Link to="/analyzer" className="cta-button primary">
              Try It Now <AiOutlineArrowRight />
            </Link>
            <Link to="/dashboard" className="cta-button secondary">
              View Dashboard
            </Link>
          </div>
        </div>
        <div className="sentiment-animation">
          <div className="sentiment-faces">
            <MdSentimentSatisfiedAlt className="face positive" />
            <MdSentimentDissatisfied className="face negative" />
          </div>
          <div className="reviews-animation">
            <div className="review-bubble positive">
              "This movie was absolutely fantastic! The plot and characters were amazing."
            </div>
            <div className="review-bubble negative">
              "One of the worst films I've seen. Poor acting and confusing storyline."
            </div>
            <div className="review-bubble positive">
              "Loved everything about this film! The cinematography was breathtaking."
            </div>
          </div>
        </div>
      </section>
      
      {/* Features Section */}
      <section className="features-section">
        <div className="section-header">
          <h2>How It Works</h2>
          <div className="section-divider"></div>
        </div>
        
        <div className="feature-cards">
          <div className="feature-card">
            <div className="feature-icon">
              <FaRobot />
            </div>
            <h3>AI-Powered Analysis</h3>
            <p>Our platform uses state-of-the-art natural language processing to understand the sentiment of movie reviews.</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">
              <FaBrain />
            </div>
            <h3>Multiple ML Models</h3>
            <p>Combines predictions from Logistic Regression, LSTM neural networks, and Transformer models for accuracy.</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">
              <FaChartBar />
            </div>
            <h3>Detailed Analytics</h3>
            <p>Get comprehensive breakdowns of sentiment analysis with confidence scores and thematic insights.</p>
          </div>
        </div>
      </section>
      
      {/* Steps Section */}
      <section className="steps-section">
        <div className="section-header">
          <h2>Three Simple Steps</h2>
          <div className="section-divider"></div>
        </div>
        
        <div className="steps-container">
          <div className="step">
            <div className="step-number">1</div>
            <div className="step-content">
              <h3>Enter Your Review</h3>
              <p>Type or paste a movie review you want to analyze</p>
            </div>
          </div>
          
          <div className="step-connector"></div>
          
          <div className="step">
            <div className="step-number">2</div>
            <div className="step-content">
              <h3>Let AI Analyze</h3>
              <p>Our machine learning models process the text and detect sentiment</p>
            </div>
          </div>
          
          <div className="step-connector"></div>
          
          <div className="step">
            <div className="step-number">3</div>
            <div className="step-content">
              <h3>View Results</h3>
              <p>Get detailed sentiment analysis with confidence scores and themes</p>
            </div>
          </div>
        </div>
      </section>
      
      {/* Tech Stack Section */}
      <section className="tech-section">
        <div className="section-header">
          <h2>Built With Modern Technology</h2>
          <div className="section-divider"></div>
        </div>
        
        <div className="tech-grid">
          <div className="tech-item">
            <FaReact className="tech-icon" />
            <h3>React</h3>
            <p>Modern, responsive frontend with intuitive UI</p>
          </div>
          
          <div className="tech-item">
            <i className="tech-icon">F</i>
            <h3>FastAPI</h3>
            <p>High-performance Python backend API</p>
          </div>
          
          <div className="tech-item">
            <FaBrain className="tech-icon" />
            <h3>ML Models</h3>
            <p>Cutting-edge sentiment analysis algorithms</p>
          </div>
          
          <div className="tech-item">
            <FaDatabase className="tech-icon" />
            <h3>MongoDB</h3>
            <p>Scalable NoSQL database for storing reviews</p>
          </div>
        </div>
      </section>
      
      {/* CTA Section */}
      <section className="cta-section">
        <h2>Ready to analyze your movie reviews?</h2>
        <p>Get started with our sentiment analysis tool today</p>
        <Link to="/analyzer" className="cta-button primary">
          Start Analyzing Now <AiOutlineArrowRight />
        </Link>
      </section>
    </div>
  );
};

export default Home;