import React, { useState, useEffect } from "react";
import axios from "axios";
import { FaEdit, FaTrash, FaPlus, FaSearch } from 'react-icons/fa';
import './styles.css';
import ModalProfessores from "../../components/modal";
import Head from '../../components/head/index.jsx';
import Footer from '../../components/footer/index';

export default function Home() {
    const [dadosProfessores, setDadosProfessores] = useState([]);
    const [dadosDisciplinas, setDadosDisciplinas] = useState([]);
    const [modalOpen, setModalOpen] = useState(false);
    const token = localStorage.getItem('token');
    const [professorSelecionado, setProfessorSelecionado] = useState(null);
    const [texto, setTexto] = useState('');
    const [up, setUp] = useState(false);
    const [abaAtiva, setAbaAtiva] = useState("professores"); // Estado para alternar abas

    useEffect(() => {
        if (!token) return;

        // Buscar professores
        const fetchProfessores = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/professores", {
                    headers: { Authorization: `Bearer ${token}` },
                });
                setDadosProfessores(response.data);
            } catch (error) {
                console.error("Erro ao buscar professores:", error);
            }
        };

        // Buscar disciplinas
        const fetchDisciplinas = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/disciplinas", {
                    headers: { Authorization: `Bearer ${token}` },
                });
                setDadosDisciplinas(response.data);
            } catch (error) {
                console.error("Erro ao buscar disciplinas:", error);
            }
        };

        fetchProfessores();
        fetchDisciplinas();
    }, [up]);

    return (
        <main className="main">
            <Head />
            <div className="container_home">
                
                {/* Botões de navegação entre Professores e Disciplinas */}
                <div className="tab-navigation">
                    <button 
                        className={`tab-button ${abaAtiva === "professores" ? "active" : ""}`} 
                        onClick={() => setAbaAtiva("professores")}
                    >
                        Professores
                    </button>
                    <button 
                        className={`tab-button ${abaAtiva === "disciplinas" ? "active" : ""}`} 
                        onClick={() => setAbaAtiva("disciplinas")}
                    >
                        Disciplinas
                    </button>
                </div>

                <section className="section_home">
                    {/* Exibe Professores ou Disciplinas conforme aba ativa */}
                    {abaAtiva === "professores" ? (
                        <div className="table">
                            {dadosProfessores.map((professor) => (
                                <div key={professor.id} className="lista">
                                    <div className="col1">
                                        <FaEdit className="edit" onClick={() => { setModalOpen(true), setProfessorSelecionado(professor) }} />
                                    </div>
                                    <div className="col2">
                                        <FaTrash className="delete" onClick={() => console.log("Excluir professor:", professor.id)} />
                                    </div>
                                    <div className="col3">
                                        <span className="id">{professor.id}</span>
                                    </div>
                                    <div className="col4">
                                        <span className="ni">{professor.ni}</span>
                                    </div>
                                    <div className="col5">
                                        <span className="nome">{professor.nome}</span>
                                    </div>
                                    <div className="col6">
                                        <span className="email">{professor.email}</span>
                                    </div>
                                    <div className="col7">
                                        <span className="cel">{professor.cel}</span>
                                    </div>
                                    <div className="col8">
                                        <span className="ocup">{professor.ocup}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <div className="table">
                            {dadosDisciplinas.map((disciplina) => (
                                <div key={disciplina.id} className="lista">
                                    <div className="col3">
                                        <span className="id">{disciplina.id}</span>
                                    </div>
                                    <div className="col4">
                                        <span className="codigo">{disciplina.sigla}</span>
                                    </div>
                                    <div className="col5">
                                        <span className="nome">{disciplina.nome}</span>
                                    </div>
                                    <div className="col6">
                                        <span className="professor">{disciplina.curso}</span>
                                    </div>
                                    <div className="col7">
                                        <span className="professor">{disciplina.semestre}</span>
                                    </div>
                                    <div className="col8">
                                        <span className="professor">{disciplina.carga_horaria}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </section>
            </div>
            <Footer />
        </main>
    );
}
