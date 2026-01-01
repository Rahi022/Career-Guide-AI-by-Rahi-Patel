import { useState } from "react";
import axios from "axios";

function CareerForm() {
  const [form, setForm] = useState({
    background: "",
    interests: "",
    skills: "",
    goals: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    setLoading(true);

    const message = `
Background: ${form.background}
Interests: ${form.interests}
Skills: ${form.skills}
Goals: ${form.goals}
`;

    try {
      const res = await axios.post("http://localhost:8000/career", {
        message,
      });

      setResult(res.data);
    } catch (err) {
      alert("Backend not running or API error");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>CareerGuide🌍 AI</h1>
      <p>AI-powered career guidance aligned with Rahi Patel's Creation (SDG8)</p>

      <input
        name="background"
        placeholder="Your education or background"
        onChange={handleChange}
      />

      <input
        name="interests"
        placeholder="Your interests"
        onChange={handleChange}
      />

      <input
        name="skills"
        placeholder="Your skills"
        onChange={handleChange}
      />

      <input
        name="goals"
        placeholder="Your career goals"
        onChange={handleChange}
      />

      <button onClick={handleSubmit}>
        {loading ? "Thinking..." : "Get Career Advice"}
      </button>

      {result && (
        <div className="result">
          <h3>🎯 Career Options</h3>
          <ul>
            {result.career_options.map((c, i) => (
              <li key={i}>{c}</li>
            ))}
          </ul>

          <h3>🧠 Required Skills</h3>
          <ul>
            {result.required_skills.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <h3>🛤️ Learning Path</h3>
            <p style={{ whiteSpace: "pre-line" }}>
                {result.learning_path}
            </p>

          <h3>💡 Career Advice</h3>
          <p style={{ whiteSpace: "pre-line" }}>
            {result.career_advice}
          </p>
        </div>
      )}
    </div>
  );
}

export default CareerForm;
