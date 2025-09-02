import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState("");

  useEffect(() => {
    axios.get("https://notes-api.onrender.com/notes")
      .then(res => setNotes(res.data))
      .catch(err => console.error(err));
  }, []);

  const addNote = () => {
    axios.post("https://notes-api.onrender.com/notes", { content: newNote })
      .then(res => setNotes([...notes, res.data]))
      .catch(err => console.error(err));
    setNewNote("");
  };

  const deleteNote = (id) => {
    axios.delete(`https://notes-api.onrender.com/notes/${id}`)
      .then(() => setNotes(notes.filter(note => note.id !== id)))
      .catch(err => console.error(err));
  };

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Notes App</h1>
      <div className="flex mb-4">
        <input value={newNote} onChange={(e) => setNewNote(e.target.value)} placeholder="Write a note..." className="border p-2 flex-1" />
        <button onClick={addNote} className="bg-blue-500 text-white px-4">Add</button>
      </div>
      <ul>
        {notes.map(note => (
          <li key={note.id} className="flex justify-between border-b py-2">
            {note.content}
            <button onClick={() => deleteNote(note.id)} className="text-red-500">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
