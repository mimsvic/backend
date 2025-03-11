import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './disciplina.css';

const DisciplinaDetail = () => {
  const [disciplina, setDisciplina] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const { id } = useParams(); // Pega o ID da disciplina da URL

  useEffect(() => {
    // Função para buscar a disciplina específica
    const fetchDisciplina = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/disciplinas/${id}`, 
          
        );
        setDisciplina(response.data);
        setLoading(false);
      } catch (err) {
        setError('Erro ao buscar a disciplina');
        setLoading(false);
      }
    };

    fetchDisciplina();
  }, [id]); // Reexecuta quando o ID mudar

  if (loading) {
    return <p>Carregando disciplina...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <p>aaaaaaaa</p>
      <p>{disciplina}aaaaa</p>
      {disciplina ? (
        <div>
          <h2>Detalhes da Disciplina</h2>
          <p><strong>Nome:</strong> {disciplina.nome}</p>
          <p><strong>Sigla:</strong> {disciplina.sigla}</p>
          <p><strong>Curso:</strong> {disciplina.curso}</p>
          <p><strong>Semestre:</strong> {disciplina.semestre}</p>
          <p><strong>Carga Horária:</strong> {disciplina.carga_horaria}</p>
        </div>
      ) : (
        <p>Disciplina não encontrada</p>
      )}
    </div>
  );
};

export default DisciplinaDetail;