import { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "https://notes-app.onrender.com"; // 🔥 use your actual Render URL

function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    axios.get(`${API_URL}/notes`).then((res) => {
      setNotes(res.data);
    });
  }, []);

  const addNote = async () => {
    await axios.post(`${API_URL}/notes`, { title, content });
    const res = await axios.get(`${API_URL}/notes`);
    setNotes(res.data);
    setTitle("");
    setContent("");
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Notes App</h1>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        className="border p-2 m-2"
      />
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Content"
        className="border p-2 m-2"
      />
      <button onClick={addNote} className="bg-blue-500 text-white px-4 py-2">
        Add Note
      </button>

      <ul>
        {notes.map((note) => (
          <li key={note.id} className="border p-2 my-2">
            <h2 className="font-bold">{note.title}</h2>
            <p>{note.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

