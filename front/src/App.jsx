import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from "./pages/login";
import Home from "./pages/home";
import Env from "./pages/environments";
import DisciplinaDetail from "./pages/disciplina/DisciplinaDetail";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/environments" element={<Env />} />
        
        {/* Adicionando a rota para exibir os detalhes da disciplina */}
        <Route path="/disciplinas/:id/" element={<DisciplinaDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
