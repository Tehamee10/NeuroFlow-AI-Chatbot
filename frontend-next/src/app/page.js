"use client";

import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./globals.css";

export default function Home() {

  const [messages, setMessages] = useState([
    {
      sender: "Bot",
      text: "Hi 👋, how may I help you?"
    }
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [messages]);

  const sendMessage = async () => {

    if (!input) return;

    const currentInput = input;

    const userMessage = {
      sender: "You",
      text: currentInput
    };

    setInput("");
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          query: currentInput
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          sender: "Bot",
          text: response.data.answer
        }
      ]);

    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
          sender: "Bot",
          text: "Error connecting to server."
        }
      ]);

    }

    setLoading(false);
  };

  return (
    <div className="app">

      <div className="chat-container">

        <h1>🧠 NeuroFlow Cognitive AI</h1>

        <p className="subtitle">
          AI-powered cognitive load reduction assistant
        </p>

        <div className="chat-box">

          {messages.map((msg, index) => (

            <div
              key={index}
              className={
                msg.sender === "You"
                  ? "user-message"
                  : "bot-message"
              }
            >
              <strong>{msg.sender}</strong>
              <p>{msg.text}</p>
            </div>

          ))}

          {loading && (
            <div className="bot-message">
              <strong>Bot</strong>
              <p>⚡ AI is thinking...</p>
            </div>
          )}

          <div ref={chatEndRef}></div>

        </div>

        <div className="input-area">

          <input
            type="text"
            placeholder="Ask anything..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
          />

          <button onClick={sendMessage}>
            Send
          </button>

        </div>

      </div>

    </div>
  );
}