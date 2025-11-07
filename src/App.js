// frontend/src/App.js
import React, { useState } from "react";
import "./App.css";

const BACKEND = "http://54.174.20.67:5000";
 // change if backend URL changes

function App() {
  const [isRecording, setIsRecording] = useState(false);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioBlob, setAudioBlob] = useState(null);
  const [audioURL, setAudioURL] = useState(null);
  const [message, setMessage] = useState("");     // general messages
  const [outputText, setOutputText] = useState("System ready"); // visible output for evaluator
  const [showPopup, setShowPopup] = useState(false);
  const [loading, setLoading] = useState(false);


  // --- Recording logic (unchanged) ---
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      const chunks = [];
      recorder.ondataavailable = (e) => chunks.push(e.data);
      recorder.onstop = () => {
        const blob = new Blob(chunks, { type: "audio/wav" });
        const audioUrl = URL.createObjectURL(blob);
        setAudioBlob(blob);
        setAudioURL(audioUrl);
      };
      recorder.start();
      setMediaRecorder(recorder);
      setIsRecording(true);
      setMessage("");
    } catch (err) {
      alert("Microphone permission denied or not available!");
    }
  };

  const stopRecording = () => {
    if (mediaRecorder) {
      mediaRecorder.stop();
      setIsRecording(false);
    }
  };

  // --- Existing: send recorded audio to /predict (keeps yours) ---
  const sendAudioToBackend = async () => {
    if (!audioBlob) {
      alert("Please record something first!");
      return;
    }
    const formData = new FormData();
    formData.append("file", audioBlob, "recording.wav");
    setMessage("Sending audio for analysis...");
    setOutputText("Sending audio...");
    try {
      const response = await fetch(`${BACKEND}/predict`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setMessage(data.message || "Response received");
      setOutputText(data.prediction ? data.prediction : data.message);
      if ((data.message || "").toLowerCase().includes("distress") ||
          (data.prediction || "").toLowerCase().includes("distress")) {
        setShowPopup(true);
        setTimeout(() => setShowPopup(false), 4000);
      }
    } catch (error) {
      setMessage("Failed to connect to backend.");
      setOutputText("Error: cannot reach backend");
    }
  };

  // === NEW: Check Safety button -> sends sample features to /predict as JSON ===
  // ==========================
// CHECK SAFETY BUTTON
// ==========================
const handleCheckSafety = async () => {
  try {
    setOutputText("Checking safety...");
    setMessage("Contacting EmpowerHer backend...");
    setLoading(true); // start spinner

    const response = await fetch(`${BACKEND}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: "I am feeling unsafe" }),
    });

    const data = await response.json();
    setOutputText(`Prediction: ${data.prediction}`);
    setMessage("Prediction received successfully!");

  } catch (error) {
    console.error(error);
    setMessage("Error connecting to backend.");
    setOutputText("Unable to reach EmpowerHer server");
  } finally {
    setLoading(false); // stop spinner
  }
};


// ==========================
// SEND ALERT BUTTON
// ==========================
const handleSendAlert = async () => {
  try {
    setOutputText("Sending alert...");
    setMessage("Contacting EmpowerHer backend...");
    setLoading(true); // start spinner

    const response = await fetch(`${BACKEND}/alert`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: "Help needed",
        location: "Pune"
      }),
    });

    const data = await response.json();

    setOutputText(data.status || "Alert sent successfully!");
    setMessage("Alert API responded.");
  } catch (error) {
    console.error("Error in /alert:", error);
    setMessage("Failed to send alert.");
    setOutputText("Unable to reach EmpowerHer server");
  } finally {
    setLoading(false); // stop spinner
  }
};
  return (
    <div className="page">
      <header className="header">
  <div className="header-left">
    <img src="/logo.png" alt="EmpowerHer Logo" className="app-logo" />
  </div>
  <p className="tagline">AI-Powered Women Safety</p>
</header>


      <div className="container">
        <h2 className="section-title">Voice Distress Detection</h2>

        <div className="button-section">
          {!isRecording ? (
            <button className="record-btn" onClick={startRecording}>
              Start Recording
            </button>
          ) : (
            <button className="stop-btn" onClick={stopRecording}>
              Stop Recording
            </button>
          )}

          {/* NEW interactive demo buttons */}
          <button className="send-btn" onClick={handleCheckSafety} style={{background:"#6f42c1"}}>
            Check Safety
          </button>

          <button className="send-btn" onClick={handleSendAlert} style={{background:"#d9534f"}}>
            Send Alert
          </button>
        </div>

        {audioURL && (
          <div className="audio-section">
            <p>Recorded Audio:</p>
            <audio controls src={audioURL}></audio>
            <br />
            <button className="send-btn" onClick={sendAudioToBackend}>
              Send recorded audio to Backend
            </button>
          </div>
        )}

        {/* OUTPUT BOX for visual result */}
        <div
  className={`output-box ${
    outputText.toLowerCase().includes("distress")
      ? "output-distress"
      : outputText.toLowerCase().includes("safe")
      ? "output-safe"
      : ""
  }`}
>
  {outputText}
</div>


        {message && <p className="message">{message}</p>}
      </div>

      {showPopup && (
        <div className="popup">
          <div className="popup-box">
            <h3>Distress Detected</h3>
            <p>Alert has been sent successfully!</p>
          </div>
        </div>
      )}

      <footer className="footer">
        <p>
          Developed by Team RakshaAI — Srushti Aravandekar | Arya Raut | Shravani Khurpe | Sara Kolas
        </p>
      </footer>
    </div>
  );
}

export default App;
