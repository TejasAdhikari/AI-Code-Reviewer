import React, { useState } from "react";
import axios from "axios";
import Editor from "@monaco-editor/react";
import { Spinner } from 'react-bootstrap';


const API_URL = process.env.BACKEND_API_URL || "http://127.0.0.1:5000";

function App() {
  const [code, setCode] = useState("// Write your code here");
  const [feedback, setFeedback] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeCode = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/analyze`, { code });
      setFeedback(response.data.feedback);
    } catch (error) {
      setFeedback("An error occurred while analyzing the code.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Code Reviewer</h2>
      <Editor height="300px" 
              defaultLanguage="python" 
              value={code} 
              onChange={setCode} 
              theme="vs-dark" 
              />
      <button className="btn btn-primary mt-3" 
              onClick={analyzeCode} 
              disabled={loading}>
        {loading ? <Spinner as="span" 
                            animation="border" 
                            size="sm" 
                            role="status" 
                            aria-hidden="true" /> 
                : "Analyze Code"}
      </button>
      <pre className="mt-3">{feedback}</pre>
    </div>
  );
}

export default App;
