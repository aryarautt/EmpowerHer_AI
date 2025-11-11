import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./LandingPage";
import App from "./App";
import FadeWrapper from "./FadeWrapper";
import "./index.css";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <FadeWrapper>
              <LandingPage />
            </FadeWrapper>
          }
        />
        <Route
          path="/app"
          element={
            <FadeWrapper>
              <App />
            </FadeWrapper>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<AppRouter />);
