import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LandingPage.css";

function LandingPage() {
  const [fadeOut, setFadeOut] = useState(false);
  const navigate = useNavigate();

  const handleStart = () => {
    // add fade-out class
    setFadeOut(true);

    // wait for animation to finish (same duration as CSS)
    setTimeout(() => {
      navigate("/app");
    }, 1000); // 1000 ms = 1 second
  };

  return (
    <div className={`landing ${fadeOut ? "fade-out" : ""}`}>
      <div className="overlay"></div>

      <div className="landing-content">
        <img src="/logo.png" alt="RakshaAI Logo" className="landing-logo" />
        <h1>Welcome to EmpowerHer</h1>
<p>AI-Powered Women Safety</p>

        <button className="start-btn" onClick={handleStart}>
          Get Started
        </button>
      </div>
    </div>
  );
}

export default LandingPage;
