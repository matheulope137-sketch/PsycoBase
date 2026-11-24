# -*- coding: utf-8 -*-
"""
Builder para o index.html da PsicoBase
Integra todo o conteúdo pedagógico original de 47 aulas + glossários
com a nova interface moderna, responsiva, intuitiva e o Professor Digital de Psicologia.
"""

import os
import re

with open(r"c:\Users\MatheusRochaLopes\Desktop\PsycoBase\PsicoBase_downloaded.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Extrair bloco de dados curriculares (constantes de conteúdo)
start_data = orig.find("const CHAVE=")
end_data = orig.find("/* ==================== ESTADO ==================== */")
dados_curriculares = orig[start_data:end_data]

novo_html = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#4A1525">
<meta name="description" content="PsicoBase - Plataforma interativa de estudos e apoio pedagógico em Psicologia">
<title>PsicoBase · Plataforma Estudantil de Psicologia</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
  --primaria:#4A1525;
  --primaria-hover:#38101C;
  --primaria-leve:rgba(74,21,37,0.08);
  --secundaria:#7D5295;
  --acento:#9D71E8;
  --lavanda:#EEDBFA;
  --verde:#2E6B4A;
  --verde-leve:rgba(46,107,74,0.1);
  --vermelho:#A62626;
  --vermelho-leve:rgba(166,38,38,0.1);
  --amarelo:#B27B10;
  
  --bg:#F9F6F0;
  --bg-card:#FFFFFF;
  --bg-subtil:#F2ECE4;
  --fg:#221E24;
  --fg-muted:#6B6471;
  --borda:#E4DCD3;
  --sombra:0 4px 20px rgba(45,30,40,0.06);
  --sombra-card:0 2px 10px rgba(45,30,40,0.04);
  --raio:16px;
  --raio-sm:10px;
  --fonte-sans:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --fonte-serif:'Lora', Georgia, serif;
}

body.escuro{
  --primaria:#D992A8;
  --primaria-hover:#E6B0C0;
  --primaria-leve:rgba(217,146,168,0.15);
  --secundaria:#C09EE6;
  --acento:#B887FF;
  --lavanda:#382747;
  --verde:#5CC48C;
  --verde-leve:rgba(92,196,140,0.15);
  --vermelho:#FF7575;
  --vermelho-leve:rgba(255,117,117,0.15);
  --amarelo:#F5BA42;
  
  --bg:#141318;
  --bg-card:#1F1D26;
  --bg-subtil:#292733;
  --fg:#F5F2F8;
  --fg-muted:#A69EB1;
  --borda:#383444;
  --sombra:0 4px 20px rgba(0,0,0,0.4);
  --sombra-card:0 2px 10px rgba(0,0,0,0.25);
}

*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{margin:0;padding:0;font-family:var(--fonte-sans);background:var(--bg);color:var(--fg);line-height:1.65;-webkit-font-smoothing:antialiased}
body.grande{font-size:112%}

/* Layout principal */
.app-header{
  position:sticky;top:0;z-index:50;
  background:rgba(255,255,255,0.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid var(--borda);
  padding:10px 18px;display:flex;align-items:center;justify-content:space-between;gap:12px;
}
body.escuro .app-header{background:rgba(31,29,38,0.85)}

.header-brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--primaria);font-weight:800;font-size:1.25rem}
.header-brand .logo-icon{width:32px;height:32px;border-radius:10px;background:var(--primaria);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.15rem;font-weight:700}
body.escuro .header-brand .logo-icon{background:var(--lavanda);color:var(--primaria)}

.header-actions{display:flex;align-items:center;gap:8px}

.btn-header{
  display:inline-flex;align-items:center;gap:6px;
  background:var(--bg-subtil);color:var(--fg);border:1px solid var(--borda);
  padding:6px 12px;border-radius:20px;font-size:0.85rem;font-weight:600;cursor:pointer;
  transition:all 0.2s ease;
}
.btn-header:hover{background:var(--lavanda);border-color:var(--secundaria)}

/* Pomodoro Widget */
.pomo-widget{
  display:inline-flex;align-items:center;gap:6px;
  background:var(--primaria-leve);border:1px solid var(--borda);
  padding:4px 10px;border-radius:20px;font-size:0.85rem;font-weight:700;color:var(--primaria);
}
.pomo-btn{background:none;border:none;cursor:pointer;color:inherit;font-size:0.9rem;padding:2px 4px}

/* Navegação */
nav.inferior{
  position:fixed;bottom:0;left:0;right:0;
  background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-top:1px solid var(--borda);
  display:flex;justify-content:space-around;z-index:40;
  padding-bottom:env(safe-area-inset-bottom);
}
body.escuro nav.inferior{background:rgba(31,29,38,0.95)}

nav.inferior a{
  flex:1;text-align:center;padding:8px 4px;font-size:0.75rem;font-weight:600;
  text-decoration:none;color:var(--fg-muted);display:flex;flex-direction:column;
  align-items:center;gap:4px;min-height:56px;justify-content:center;
  transition:color 0.2s, transform 0.1s;
}
nav.inferior a svg{width:22px;height:22px;stroke-width:2.1}
nav.inferior a[aria-current="page"]{color:var(--primaria);font-weight:700}
nav.inferior a[aria-current="page"] svg{stroke:var(--primaria)}

.wrap{max-width:820px;margin:0 auto;padding:20px 18px 100px}

/* Desktop */
@media (min-width:920px){
  body{padding-left:260px;padding-bottom:0}
  .app-header{left:260px;width:calc(100% - 260px)}
  nav.inferior{
    top:0;bottom:0;left:0;right:auto;width:260px;
    flex-direction:column;justify-content:flex-start;gap:6px;
    padding:24px 16px;border-top:0;border-right:1px solid var(--borda);
  }
  .nav-header{padding:0 8px 16px;margin-bottom:8px;border-bottom:1px solid var(--borda);display:flex;align-items:center;gap:10px}
  nav.inferior a{
    flex:none;flex-direction:row;justify-content:flex-start;gap:12px;
    padding:12px 14px;border-radius:12px;font-size:0.95rem;min-height:46px;
  }
  nav.inferior a[aria-current="page"]{
    background:var(--primaria-leve);color:var(--primaria);border-left:4px solid var(--primaria);
  }
  .wrap{max-width:960px;padding:32px 36px 60px}
}

/* Tipografia e Componentes */
h1,h2,h3{color:var(--fg);font-weight:700;line-height:1.25}
h1{font-size:1.75rem;margin:0.5rem 0 1rem;letter-spacing:-0.02em}
h2{font-size:1.3rem;margin:1.6rem 0 0.8rem;color:var(--primaria)}
h3{font-size:1.1rem;margin:1rem 0 0.4rem}
a{color:var(--primaria);text-decoration:none}
a:hover{text-decoration:underline}
.muted{color:var(--fg-muted);font-size:0.92rem}

.card{
  background:var(--bg-card);border:1px solid var(--borda);
  border-radius:var(--raio);padding:20px;margin:16px 0;
  box-shadow:var(--sombra-card);
  transition:transform 0.15s ease, box-shadow 0.15s ease;
}
.card.destaque{border-left:5px solid var(--primaria);background:linear-gradient(135deg, var(--bg-card), var(--bg-subtil))}

.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:8px;
  background:var(--primaria);color:#fff;border:2px solid var(--primaria);
  border-radius:12px;padding:10px 18px;font-family:inherit;font-weight:600;font-size:0.95rem;
  cursor:pointer;min-height:44px;text-decoration:none;margin:4px 6px 4px 0;
  box-shadow:0 2px 6px rgba(74,21,37,0.15);transition:all 0.2s ease;
}
.btn:hover{background:var(--primaria-hover);border-color:var(--primaria-hover);text-decoration:none;transform:translateY(-1px)}
.btn.sec{background:transparent;color:var(--primaria);border-color:var(--borda);box-shadow:none}
.btn.sec:hover{background:var(--primaria-leve);border-color:var(--primaria)}
.btn.sm{padding:6px 12px;font-size:0.85rem;min-height:36px;border-radius:8px}
.btn.sucesso{background:var(--verde);border-color:var(--verde)}
.btn:disabled{opacity:0.5;cursor:not-allowed;transform:none}

.grid{display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:16px;margin:16px 0}
.grid-stats{display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:12px;margin:14px 0}

.stat-box{
  background:var(--bg-card);border:1px solid var(--borda);
  border-radius:14px;padding:14px;text-align:center;
  box-shadow:var(--sombra-card);
}
.stat-box .num{font-size:1.6rem;font-weight:800;color:var(--primaria);display:block;line-height:1.2}
.stat-box .rotulo{font-size:0.82rem;font-weight:600;color:var(--fg-muted);text-transform:uppercase;letter-spacing:0.04em}

.barra{height:8px;background:var(--borda);border-radius:99px;overflow:hidden;margin:8px 0}
.barra>div{height:100%;background:var(--verde);transition:width 0.4s ease}

.tag{
  display:inline-flex;align-items:center;gap:4px;
  background:var(--lavanda);color:#221E24;padding:3px 10px;
  border-radius:99px;font-size:0.8rem;font-weight:600;
}
.tag.concluido{background:var(--verde-leve);color:var(--verde)}
.tag.pendente{background:var(--primaria-leve);color:var(--primaria)}

.campo{
  width:100%;padding:12px 14px;border-radius:12px;
  border:1px solid var(--borda);background:var(--bg-card);color:var(--fg);
  font:inherit;font-size:0.95rem;transition:border-color 0.2s, box-shadow 0.2s;
}
.campo:focus{outline:none;border-color:var(--acento);box-shadow:0 0 0 3px rgba(157,113,232,0.2)}

.toast{
  position:fixed;top:20px;left:50%;transform:translateX(-50%);
  background:#221E24;color:#FFFFFF;padding:12px 22px;border-radius:30px;
  z-index:9999;max-width:90%;font-size:0.92rem;font-weight:600;
  box-shadow:0 8px 30px rgba(0,0,0,0.3);animation:fadeUp 0.3s ease;
}
@keyframes fadeUp{from{opacity:0;transform:translate(-50%, 15px)} to{opacity:1;transform:translate(-50%, 0)}}

/* Flashcard 3D */
.flashcard-wrap{perspective:1000px;margin:24px 0}
.flashcard{
  background:var(--bg-card);border:2px solid var(--borda);border-radius:20px;
  min-height:260px;padding:28px;box-shadow:var(--sombra);cursor:pointer;
  display:flex;flex-direction:column;justify-content:center;align-items:center;
  text-align:center;transition:transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style:preserve-3d;position:relative;user-select:none;
}
.flashcard.virado{transform:rotateY(180deg)}
.flashcard-lado{position:relative;backface-visibility:hidden;width:100%}
.flashcard-verso{position:absolute;top:0;left:0;right:0;bottom:0;padding:28px;backface-visibility:hidden;transform:rotateY(180deg);display:flex;flex-direction:column;justify-content:center;align-items:center}

/* Opções de quiz */
.alt{
  display:flex;align-items:center;gap:12px;padding:12px 16px;
  border:1px solid var(--borda);border-radius:12px;margin:8px 0;
  cursor:pointer;min-height:48px;background:var(--bg-card);
  transition:all 0.15s ease;
}
.alt:hover{border-color:var(--secundaria);background:var(--primaria-leve)}
.alt:has(input:checked){border-color:var(--primaria);background:var(--lavanda);color:#221E24;font-weight:600}

.res{border-radius:12px;padding:14px;margin:10px 0;background:var(--bg-card);border:1px solid var(--borda)}
.res.ok{border-left:5px solid var(--verde);background:var(--verde-leve)}
.res.erro{border-left:5px solid var(--vermelho);background:var(--vermelho-leve)}

/* Chat do Professor */
.chat-container{display:flex;flex-direction:column;gap:14px;margin:18px 0;max-height:480px;overflow-y:auto;padding-right:6px}
.chat-msg{display:flex;gap:12px;max-width:88%}
.chat-msg.prof{align-self:flex-start}
.chat-msg.aluno{align-self:flex-end;flex-direction:row-reverse}
.chat-avatar{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0}
.chat-msg.prof .chat-avatar{background:var(--primaria);color:#fff}
.chat-msg.aluno .chat-avatar{background:var(--secundaria);color:#fff}
.chat-bubble{padding:14px 18px;border-radius:18px;font-size:0.95rem;line-height:1.6}
.chat-msg.prof .chat-bubble{background:var(--bg-card);border:1px solid var(--borda);border-top-left-radius:4px;box-shadow:var(--sombra-card)}
.chat-msg.aluno .chat-bubble{background:var(--primaria);color:#FFFFFF;border-top-right-radius:4px}
body.escuro .chat-msg.aluno .chat-bubble{background:var(--secundaria);color:#fff}

/* Busca Modal */
.modal-overlay{
  position:fixed;top:0;left:0;right:0;bottom:0;
  background:rgba(0,0,0,0.5);backdrop-filter:blur(4px);
  z-index:999;display:flex;align-items:flex-start;justify-content:center;padding:60px 16px;
}
.modal-content{background:var(--bg-card);border:1px solid var(--borda);border-radius:20px;max-width:640px;width:100%;max-height:80vh;display:flex;flex-direction:column;box-shadow:var(--sombra)}
.modal-header{padding:16px 20px;border-bottom:1px solid var(--borda);display:flex;align-items:center;gap:12px}
.modal-body{padding:16px 20px;overflow-y:auto;flex:1}

/* Anotações Drawer */
.notes-box{background:var(--bg-subtil);border:1px solid var(--borda);border-radius:14px;padding:16px;margin:16px 0}
.notes-box textarea{min-height:100px;resize:vertical}

/* Leitor de voz */
.tts-bar{display:inline-flex;align-items:center;gap:8px;background:var(--bg-subtil);padding:6px 12px;border-radius:10px;font-size:0.88rem;margin:10px 0}
</style>
</head>
<body>
<div id="aviso" class="toast" role="status" aria-live="polite" hidden></div>

<!-- Top Header -->
<header class="app-header" id="header" hidden>
  <a href="#/inicio" class="header-brand">
    <div class="logo-icon">ψ</div>
    <span>PsicoBase</span>
  </a>
  <div class="header-actions">
    <!-- Streak -->
    <div class="btn-header" title="Sequência diária de estudo" id="streak-badge">🔥 0 dias</div>
    
    <!-- Pomodoro -->
    <div class="pomo-widget" id="pomo-box" title="Pomodoro de Estudo">
      <span id="pomo-icon">⏱️</span>
      <span id="pomo-display">25:00</span>
      <button class="pomo-btn" id="pomo-toggle" onclick="togglePomodoro()" title="Iniciar/Pausar">▶</button>
      <button class="pomo-btn" id="pomo-reset" onclick="resetPomodoro()" title="Reiniciar">↺</button>
    </div>
    
    <!-- Busca Rápida -->
    <button class="btn-header" onclick="abrirBuscaModal()" title="Busca Rápida (Ctrl+K)">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <span style="display:none" class="d-md-inline">Buscar</span>
    </button>

    <!-- Tema -->
    <button class="btn-header" onclick="alternarTema()" title="Alternar Modo Escuro / Claro">
      <span id="tema-icon">🌙</span>
    </button>
  </div>
</header>

<!-- Navegação Principal -->
<nav class="inferior" id="nav" aria-label="Navegação principal" hidden>
  <div class="nav-header" style="display:none">
    <div class="header-brand">
      <div class="logo-icon">ψ</div>
      <span>PsicoBase</span>
    </div>
  </div>
  <a href="#/inicio" data-nav="inicio">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
    <span>Início</span>
  </a>
  <a href="#/aprender" data-nav="aprender">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
    <span>Aprender</span>
  </a>
  <a href="#/revisar" data-nav="revisar">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
    <span>Revisar</span>
  </a>
  <a href="#/professor" data-nav="professor">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path><circle cx="9" cy="10" r="1"></circle><circle cx="15" cy="10" r="1"></circle></svg>
    <span>Professor IA</span>
  </a>
  <a href="#/biblioteca" data-nav="biblioteca">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
    <span>Biblioteca</span>
  </a>
  <a href="#/perfil" data-nav="perfil">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    <span>Perfil</span>
  </a>
</nav>

<!-- Conteúdo Dinâmico -->
<main id="app" class="wrap" tabindex="-1"></main>

<!-- Modal de Busca Rápida -->
<div id="modal-busca" class="modal-overlay" style="display:none" onclick="if(event.target===this) fecharBuscaModal()">
  <div class="modal-content">
    <div class="modal-header">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <input id="input-busca-modal" class="campo" type="search" placeholder="Buscar qualquer aula, termo ou autor..." oninput="executarBuscaModal(this.value)" autocomplete="off">
      <button class="btn sec sm" onclick="fecharBuscaModal()">✕</button>
    </div>
    <div id="modal-busca-resultados" class="modal-body">
      <p class="muted">Digite uma palavra-chave para encontrar aulas e conceitos em toda a PsicoBase.</p>
    </div>
  </div>
</div>

<script>
(()=>{
'use strict';

/* ==================== DADOS CURRICULARES (47 AULAS E GLOSSÁRIO) ==================== */
""" + dados_curriculares + r"""

/* ==================== ESTADO E PERSISTÊNCIA ==================== */
function estadoPadrao(){
 return {
   perfil:null, aulasConcluidas:{}, tentativas:[], cartoes:{}, minPorDia:{},
   anotacoes:{}, ultimaAula:null, abertas:{}, tema:'claro', fonte:'normal',
   apiServidor:'http://localhost:8000/api', chaveIA:'', criadoEm:Date.now()
 };
}
function carregar(){
 let s=null;
 try{ s=JSON.parse(localStorage.getItem(CHAVE)); }catch(e){ s=null; }
 return Object.assign(estadoPadrao(), (s && typeof s==='object')?s:{});
}
let estado=carregar();
const app=document.getElementById('app');
const nav=document.getElementById('nav');
const header=document.getElementById('header');
let sessao=null;
let obPasso=1;
let obDados={nivel:'',objetivo:'',tempo:'',preferencias:[],apelido:''};
let filaRev=null;
let revIndice=0;
let revVerso=false;

/* Pomodoro Timer */
let pomoTempo=25*60;
let pomoInterval=null;
let pomoAtivo=false;

function salvar(){
 try{ localStorage.setItem(CHAVE, JSON.stringify(estado)); return true; }
 catch(e){ aviso('Não foi possível salvar neste navegador. Exporte um backup pelo Perfil.'); return false; }
}

function garantirCartoes(aulaId){
 const a=AULAS[aulaId]; if(!a||!a.cartoes) return;
 a.cartoes.forEach(c=>{ if(!estado.cartoes[c.id]) estado.cartoes[c.id]={stage:0,prox:diaNum(),vezes:0,historico:[]}; });
}
function garantirTodos(){ Object.keys(AULAS).forEach(garantirCartoes); }
garantirTodos();

/* ==================== UTILITÁRIOS ==================== */
const $=(s,r=document)=>r.querySelector(s);
function esc(s){ return String(s===undefined||s===null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function dataISO(d){ d=d||new Date(); return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
function diaNum(d){ d=d||new Date(); return Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/86400000); }

function aviso(msg){
 const t=$('#aviso'); t.textContent=msg; t.hidden=false;
 clearTimeout(aviso._t); aviso._t=setTimeout(()=>{ t.hidden=true; },3500);
}

function rota(){ return (location.hash||'#/inicio').replace(/^#/,''); }

function alternarTema(){
 estado.tema = estado.tema==='escuro'?'claro':'escuro';
 salvar();
 aplicarVisual();
}
window.alternarTema = alternarTema;

function aplicarVisual(){
 document.body.classList.toggle('escuro', estado.tema==='escuro');
 document.body.classList.toggle('grande', estado.fonte==='grande');
 const ic=$('#tema-icon'); if(ic) ic.textContent = estado.tema==='escuro'?'☀️':'🌙';
 atualizarStreak();
}

function calcularStreak(){
 const dias = Object.keys(estado.minPorDia).filter(k=>estado.minPorDia[k]>0).sort().reverse();
 if(!dias.length) return 0;
 let streak=0;
 let atual=new Date();
 let check=dataISO(atual);
 // Se não estudou hoje, checa se estudou ontem
 if(!dias.includes(check)){
   atual.setDate(atual.getDate()-1);
   check=dataISO(atual);
   if(!dias.includes(check)) return 0;
 }
 while(dias.includes(check)){
   streak++;
   atual.setDate(atual.getDate()-1);
   check=dataISO(atual);
 }
 return streak;
}

function atualizarStreak(){
 const el=$('#streak-badge');
 if(el){
   const s=calcularStreak();
   el.textContent='🔥 ' + s + (s===1?' dia':' dias');
 }
}

/* ==================== POMODORO ==================== */
function formatarTempoPomo(s){
 const m=Math.floor(s/60);
 const seg=s%60;
 return String(m).padStart(2,'0')+':'+String(seg).padStart(2,'0');
}
function togglePomodoro(){
 pomoAtivo=!pomoAtivo;
 const btn=$('#pomo-toggle');
 if(pomoAtivo){
   if(btn) btn.textContent='⏸';
   pomoInterval=setInterval(()=>{
     if(pomoTempo>0){
       pomoTempo--;
       const disp=$('#pomo-display'); if(disp) disp.textContent=formatarTempoPomo(pomoTempo);
     }else{
       clearInterval(pomoInterval);
       pomoAtivo=false;
       if(btn) btn.textContent='▶';
       aviso('🎉 Parabéns! Ciclo Pomodoro concluído (+25 min registrados).');
       const k=dataISO();
       estado.minPorDia[k]=(estado.minPorDia[k]||0)+25;
       salvar();
       pomoTempo=25*60;
     }
   },1000);
 }else{
   if(btn) btn.textContent='▶';
   clearInterval(pomoInterval);
 }
}
window.togglePomodoro = togglePomodoro;

function resetPomodoro(){
 clearInterval(pomoInterval);
 pomoAtivo=false;
 pomoTempo=25*60;
 const disp=$('#pomo-display'); if(disp) disp.textContent='25:00';
 const btn=$('#pomo-toggle'); if(btn) btn.textContent='▶';
}
window.resetPomodoro = resetPomodoro;

/* ==================== TEMPO DE ESTUDO ==================== */
function iniciarSessao(id){ encerrarSessao(); sessao={id:id, inicio:Date.now()}; }
function encerrarSessao(){
 if(!sessao) return;
 const min=Math.min(Math.round((Date.now()-sessao.inicio)/60000), 120);
 if(min>0){
   const k=dataISO();
   estado.minPorDia[k]=(estado.minPorDia[k]||0)+min;
   salvar();
 }
 sessao=null;
}
window.addEventListener('pagehide', encerrarSessao);
document.addEventListener('visibilitychange', ()=>{ if(document.visibilityState==='hidden') encerrarSessao(); });

/* ==================== REVISÃO ESPAÇADA ==================== */
function revisoesPendentes(){
 garantirTodos();
 return Object.entries(estado.cartoes).filter(([id,c])=>c.prox<=diaNum()).map(([id])=>id);
}
function achaCartao(id){
 for(const a of Object.values(AULAS)){
  const c=(a.cartoes||[]).find(x=>x.id===id);
  if(c) return {id:c.id, frente:c.frente, verso:c.verso, aula:a.titulo, aulaId:a.id};
 }
 return null;
}
function responderCartao(id,nivel){
 const c=estado.cartoes[id]; if(!c) return;
 let s=c.stage;
 if(nivel==='dificil') s=0;
 else if(nivel==='bom') s=Math.max(1,s);
 else if(nivel==='facil') s=Math.min(INTERVALOS.length-1,s+1);
 c.stage=s;
 c.prox=diaNum()+INTERVALOS[s];
 c.vezes++;
 c.historico.push({d:dataISO(), n:nivel});
 salvar();
}

/* ==================== LEITOR DE VOZ (TTS) ==================== */
let vozFalando=false;
function falarTexto(texto){
 if(!('speechSynthesis' in window)) return aviso('Síntese de voz não suportada pelo seu navegador.');
 if(vozFalando){
   window.speechSynthesis.cancel();
   vozFalando=false;
   const btn=$('#btn-audio-aula'); if(btn) btn.innerHTML='🔊 Ouvir Aula';
   return;
 }
 window.speechSynthesis.cancel();
 const utt=new SpeechSynthesisUtterance(texto);
 utt.lang='pt-BR';
 utt.rate=1.0;
 utt.onend=()=>{
   vozFalando=false;
   const btn=$('#btn-audio-aula'); if(btn) btn.innerHTML='🔊 Ouvir Aula';
 };
 vozFalando=true;
 window.speechSynthesis.speak(utt);
 const btn=$('#btn-audio-aula'); if(btn) btn.innerHTML='⏹ Parar Áudio';
}
window.falarTexto = falarTexto;

/* ==================== ANOTAÇÕES DO ESTUDANTE ==================== */
function salvarAnotacaoAula(aulaId, texto){
 estado.anotacoes=estado.anotacoes||{};
 estado.anotacoes[aulaId]=texto;
 salvar();
 const tag=$('#status-anotacao');
 if(tag){ tag.textContent='Salvo ✓'; setTimeout(()=>{ tag.textContent=''; },2000); }
}
window.salvarAnotacaoAula = salvarAnotacaoAula;

/* ==================== ESTATÍSTICAS ==================== */
function estatisticas(){
 garantirTodos();
 const total=estado.tentativas.length;
 const acertos=estado.tentativas.filter(t=>t.ok).length;
 const concl=Object.keys(estado.aulasConcluidas).filter(id=>AULAS[id]).length;
 const minutos=Object.values(estado.minPorDia).reduce((a,b)=>a+b,0);
 const pend=revisoesPendentes().length;
 const hoje=diaNum();
 const previstas=Object.values(estado.cartoes).filter(c=>c.prox>hoje && c.prox<=hoje+7).length;
 return {
   total:total, acertos:acertos, pct:total?Math.round(acertos/total*100):null,
   concl:concl, totalAulas:Object.keys(AULAS).length,
   minutos:Math.round(minutos), pend:pend, previstas:previstas
 };
}

function proximaAula(){
 const ord=Object.keys(AULAS);
 const ult=estado.ultimaAula;
 if(ult && AULAS[ult] && !estado.aulasConcluidas[ult]) return ult;
 return ord.find(id=>!estado.aulasConcluidas[id])||ord[0];
}

/* ==================== MOTOR DO PROFESSOR DIGITAL ==================== */
const CRISE_TERMOS_LISTA=['suicid','me matar','quero morrer','nao quero viver','não quero viver','acabar com a minha vida','automutil','me cortar','me machucar','autolesao'];
const DIAG_TERMOS_LISTA=['tenho depressao','tenho ansiedade','tenho transtorno','eu tenho tdah','sera que eu tenho','diagnostica','diagnostico para mim','meu diagnostico','interprete meu teste','qual remedio','quantos mg'];

const RESPOSTA_CRISE_TXT="Sinto muito que você esteja passando por um momento delicado. Como Professor Virtual acadêmico, não posso oferecer atendimento psicológico ou emergencial. "
+"Por favor, busque acolhimento agora mesmo: Ligue 188 (CVV - Centro de Valorização da Vida, gratuito 24h) ou em caso de risco iminente, 192 (SAMU).";

const RESPOSTA_DIAG_TXT="De acordo com o Código de Ética do Psicólogo (CFP), diagnósticos clínicos e prescrições terapêuticas exigem formação profissional e acolhimento presencial/remoto por psicólogo com CRP ativo. "
+"Meu papel é exclusivamente didático. Posso explicar como o construto é definido teoricamente nos manuais (CID-11 / DSM-5) para fins de estudo acadêmico.";

async function chamarProfessorIA(mensagem, contextoAula){
 const mNorm=mensagem.toLowerCase();
 if(CRISE_TERMOS_LISTA.some(t=>mNorm.includes(t))) return {resposta:RESPOSTA_CRISE_TXT, fontes:['CVV (188)','SAMU (192)']};
 if(DIAG_TERMOS_LISTA.some(t=>mNorm.includes(t))) return {resposta:RESPOSTA_DIAG_TXT, fontes:['Código de Ética Profissional (CFP)']};

 // 1. Tentar conexão com API local (api_server.py)
 if(estado.apiServidor){
   try{
     const res=await fetch(estado.apiServidor.replace(/\/$/,'')+'/professor/chat',{
       method:'POST',headers:{'Content-Type':'application/json'},
       body:JSON.stringify({pergunta:mensagem, aula_id:contextoAula}),
       signal:AbortSignal.timeout(3500)
     });
     if(res.ok){
       const d=await res.json();
       if(d.resposta) return {resposta:d.resposta, fontes:d.fontes||['API PsicoBase']};
     }
   }catch(e){ /* Fallback automático para o motor offline */ }
 }

 // 2. Motor Heurístico/Offline embutido
 for(const [id, a] of Object.entries(AULAS)){
   if(mNorm.includes(a.titulo.toLowerCase()) || (a.objetivos||[]).some(o=>mNorm.includes(o.toLowerCase()))){
     const resumoTxt=(a.resumo||[]).join(' ');
     return {
       resposta:"Olá! Na aula **"+a.titulo+"**, estudamos exatamente esse tema.\n\n"
         +"📌 **Conceito Central:** "+(resumoTxt||a.secoes[0].p[0])+"\n\n"
         +"💡 **Dica de Estudo:** Revise os objetivos da aula e observe como esse conceito é cobrado nas questões de fixação.",
       fontes:['Aula: '+a.titulo, a.disciplina]
     };
   }
 }

 // 3. Resposta Socrática Padrão
 return {
   resposta:"Excelente reflexão acadêmica! Para compreendermos esse aspecto na Psicologia, é crucial delimitarmos sob qual matriz epistemológica estamos trabalhando (Comportamental, Cognitiva, Psicanalítica ou Humanista).\n\n"
     +"Sugiro que você explore as aulas correspondentes na aba **Aprender** e consulte os termos fundamentais na **Biblioteca** para estruturar seu fichamento.",
   fontes:['Diretrizes Curriculares Nacionais (DCNs) de Psicologia','Plataforma PsicoBase']
 };
}

/* ==================== VIEWS ==================== */

/* View: Bem-Vindo */
function viewBemVindo(){
 const pct=Math.round((obPasso-1)/5*100);
 let corpo='';
 if(obPasso===1){
  corpo='<p style="font-size:1.1rem">Bem-vindo(a) à <strong>PsicoBase</strong>, sua plataforma interativa para aprender, revisar e dominar os fundamentos da Psicologia.</p>'
   +'<div class="card destaque"><p>Aqui você estuda com conteúdos estruturados, flashcards com repetição espaçada, caderno de anotações e um <strong>Professor Digital</strong> para tirar dúvidas 24 horas por dia.</p></div>'
   +'<button class="btn" onclick="proximoOnboarding(1)">Começar Jornada →</button>';
 }else if(obPasso===2){
  corpo='<p>Qual é o seu nível atual de conhecimento?</p>'
   +'<div class="card">'+Object.entries(NIVEIS).map(([k,v])=>'<label class="alt"><input type="radio" name="ob-nivel" value="'+k+'"> <span>'+v+'</span></label>').join('')+'</div>'
   +'<button class="btn" onclick="proximoOnboarding(2)">Continuar →</button>';
 }else if(obPasso===3){
  corpo='<p>Qual é o seu objetivo principal?</p>'
   +'<div class="card">'+Object.entries(OBJETIVOS).map(([k,v])=>'<label class="alt"><input type="radio" name="ob-obj" value="'+k+'"> <span>'+v+'</span></label>').join('')+'</div>'
   +'<button class="btn" onclick="proximoOnboarding(3)">Continuar →</button>';
 }else if(obPasso===4){
  corpo='<p>Quanto tempo você pretende se dedicar por dia?</p>'
   +'<div class="card">'+Object.entries(TEMPOS).map(([k,v])=>'<label class="alt"><input type="radio" name="ob-tempo" value="'+k+'"> <span>'+v+'</span></label>').join('')+'</div>'
   +'<button class="btn" onclick="proximoOnboarding(4)">Continuar →</button>';
 }else if(obPasso===5){
  corpo='<p>Como prefere que o Professor Digital te chame?</p>'
   +'<div class="card"><input id="ob-nome" class="campo" placeholder="Seu nome ou apelido (opcional)" maxlength="40"></div>'
   +'<button class="btn" onclick="proximoOnboarding(5)">Concluir e Estudar →</button>';
 }
 return '<div class="barra"><div style="width:'+pct+'%"></div></div>'
  +'<p class="muted">Passo '+obPasso+' de 5</p>'
  +'<h1>Configuração Inicial</h1>'+corpo;
}

window.proximoOnboarding = function(etapa){
 if(etapa===1){ obPasso=2; render(); return; }
 if(etapa===2){
   const sel=$('input[name="ob-nivel"]:checked');
   if(!sel) return aviso('Escolha uma opção para continuar.');
   obDados.nivel=sel.value; obPasso=3; render(); return;
 }
 if(etapa===3){
   const sel=$('input[name="ob-obj"]:checked');
   if(!sel) return aviso('Escolha seu objetivo.');
   obDados.objetivo=sel.value; obPasso=4; render(); return;
 }
 if(etapa===4){
   const sel=$('input[name="ob-tempo"]:checked');
   if(!sel) return aviso('Escolha sua meta de tempo.');
   obDados.tempo=sel.value; obPasso=5; render(); return;
 }
 if(etapa===5){
   const apelido=$('#ob-nome').value.trim();
   obDados.apelido=apelido;
   estado.perfil=obDados;
   salvar();
   location.hash='#/inicio';
   render();
 }
};

/* View: Início */
function viewInicio(){
 const p=estado.perfil||{};
 const st=estatisticas();
 const prox=proximaAula();
 const aulaObj=AULAS[prox]||AULAS['m1-a1'];
 const sauda=new Date().getHours()<12?'Bom dia':(new Date().getHours()<18?'Boa tarde':'Boa noite');
 const nome=p.apelido?', '+esc(p.apelido):'';
 
 return ''
 +'<div style="margin-bottom:24px">'
  +'<h1 style="margin-bottom:4px">'+sauda+nome+'! 👋</h1>'
  +'<p class="muted">Pronto para aprofundar seu conhecimento na ciência da mente e do comportamento?</p>'
 +'</div>'
 
 // Card de Continuação Rápida
 +'<div class="card destaque">'
  +'<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">'
   +'<div>'
    +'<span class="tag pendente">Continuar Aula</span>'
    +'<h2 style="margin:6px 0">'+esc(aulaObj.titulo)+'</h2>'
    +'<p class="muted" style="margin:0">'+esc(aulaObj.disciplina)+' · Estimado: '+aulaObj.tempo+' min</p>'
   +'</div>'
   +'<a href="#/aula/'+aulaObj.id+'" class="btn">Continuar Estudos →</a>'
  +'</div>'
 +'</div>'

 // Métricas Rápidas
 +'<div class="grid-stats">'
  +'<div class="stat-box"><span class="num">'+st.concl+'/'+st.totalAulas+'</span><span class="rotulo">Aulas Feitas</span></div>'
  +'<div class="stat-box"><span class="num">'+st.pend+'</span><span class="rotulo">Revisões Hoje</span></div>'
  +'<div class="stat-box"><span class="num">'+st.minutos+'m</span><span class="rotulo">Tempo Total</span></div>'
  +'<div class="stat-box"><span class="num">'+(st.pct!==null?st.pct+'%':'-')+'</span><span class="rotulo">Aproveitamento</span></div>'
 +'</div>'

 // Ações Rápidas
 +'<h2>Acesso Rápido</h2>'
 +'<div class="grid">'
  +'<a href="#/professor" class="card" style="display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none">'
   +'<div style="font-size:2rem;background:var(--lavanda);width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center">🤖</div>'
   +'<div><strong>Professor Virtual</strong><p class="muted" style="margin:2px 0">Tire dúvidas e debata casos clínicos</p></div>'
  +'</a>'
  +'<a href="#/revisar" class="card" style="display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none">'
   +'<div style="font-size:2rem;background:var(--lavanda);width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center">🧠</div>'
   +'<div><strong>Flashcards SRS</strong><p class="muted" style="margin:2px 0">'+st.pend+' cartões prontos para revisar</p></div>'
  +'</a>'
  +'<a href="#/aprender" class="card" style="display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none">'
   +'<div style="font-size:2rem;background:var(--lavanda);width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center">📚</div>'
   +'<div><strong>Todos os Módulos</strong><p class="muted" style="margin:2px 0">12 módulos da graduação</p></div>'
  +'</a>'
  +'<a href="#/biblioteca" class="card" style="display:flex;align-items:center;gap:14px;color:inherit;text-decoration:none">'
   +'<div style="font-size:2rem;background:var(--lavanda);width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center">📖</div>'
   +'<div><strong>Biblioteca & Termos</strong><p class="muted" style="margin:2px 0">Glossário e suas anotações</p></div>'
  +'</a>'
 +'</div>';
}

/* View: Aprender (Módulos) */
function viewAprender(){
 const modulosHtml=MODULOS.map(m=>{
  const aulas=Object.entries(AULAS).filter(([id,a])=>a.modulo===m.id);
  const feitas=aulas.filter(([id])=>estado.aulasConcluidas[id]).length;
  const pct=aulas.length?Math.round((feitas/aulas.length)*100):0;
  return ''
  +'<div class="card">'
   +'<div style="display:flex;justify-content:space-between;align-items:flex-start">'
    +'<div>'
     +'<span class="tag">Módulo '+m.id+'</span>'
     +'<h2 style="margin:6px 0"><a href="#/modulo/'+m.id+'">'+esc(m.titulo)+'</a></h2>'
     +'<p class="muted" style="margin-bottom:8px">'+esc(m.desc)+'</p>'
    +'</div>'
    +'<span class="tag '+(pct===100?'concluido':'')+'">'+pct+'%</span>'
   +'</div>'
   +'<div class="barra"><div style="width:'+pct+'%"></div></div>'
   +'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px">'
    +'<span class="muted" style="font-size:0.85rem">'+aulas.length+' aulas · '+feitas+' concluídas</span>'
    +'<a href="#/modulo/'+m.id+'" class="btn sec sm">Ver Aulas →</a>'
   +'</div>'
  +'</div>';
 }).join('');

 return '<h1>Trilha de Aprendizado</h1><p class="muted">Os 12 eixos fundamentais da formação acadêmica em Psicologia.</p>'+modulosHtml;
}

/* View: Módulo */
function viewModulo(n){
 const m=MODULOS.find(x=>String(x.id)===String(n));
 if(!m) return '<h1>Módulo não encontrado</h1><p><a href="#/aprender">Voltar</a></p>';
 const aulas=Object.entries(AULAS).filter(([id,a])=>a.modulo===m.id);
 
 const lista=aulas.map(([id,a],i)=>{
  const conc=!!estado.aulasConcluidas[id];
  return ''
  +'<div class="card" style="display:flex;align-items:center;justify-content:space-between;margin:8px 0">'
   +'<div>'
    +'<strong>'+(i+1)+'. <a href="#/aula/'+id+'">'+esc(a.titulo)+'</a></strong>'
    +'<p class="muted" style="margin:2px 0;font-size:0.85rem">'+esc(a.nivel)+' · '+a.tempo+' min</p>'
   +'</div>'
   +(conc?'<span class="tag concluido">✓ Concluída</span>':'<a href="#/aula/'+id+'" class="btn sm sec">Estudar</a>')
  +'</div>';
 }).join('');

 return ''
 +'<p class="muted"><a href="#/aprender">← Todos os Módulos</a></p>'
 +'<h1>Módulo '+m.id+': '+esc(m.titulo)+'</h1>'
 +'<p class="muted">'+esc(m.desc)+'</p>'
 +'<div style="margin:20px 0">'+lista+'</div>';
}

/* View: Aula */
function viewAula(id){
 const a=AULAS[id];
 if(!a) return '<h1>Aula não encontrada</h1><p><a href="#/aprender">Voltar</a></p>';
 iniciarSessao(id);
 estado.ultimaAula=id;
 estado.abertas=estado.abertas||{}; estado.abertas[id]=true;
 garantirCartoes(id);
 salvar();
 
 const mod=MODULOS.find(m=>m.id===a.modulo);
 const concl=!!estado.aulasConcluidas[id];
 const textoAudio = (a.secoes||[]).map(s=>s.t+'. '+(s.p||[]).join(' ')).join(' ');
 const anotacaoAtual = (estado.anotacoes&&estado.anotacoes[id])||'';

 const secoesHtml=(a.secoes||[]).map(s=>''
  +'<h2>'+esc(s.t)+'</h2>'
  +(s.p||[]).map(p=>'<p style="font-size:1.02rem;line-height:1.7">'+esc(p)+'</p>').join('')
  +(s.pausa?'<div class="card" style="border-left:4px solid var(--secundaria)"><strong>Pare e reflita:</strong><p>'+esc(s.pausa.p)+'</p><details><summary style="cursor:pointer;font-weight:600;color:var(--primaria)">Ver orientação do professor</summary><p class="muted" style="margin-top:6px">'+esc(s.pausa.r)+'</p></details></div>':'')
 ).join('');

 const quizHtml=(a.questoes||[]).map((q,i)=>''
  +'<fieldset class="card" style="margin:16px 0;border:1px solid var(--borda)">'
   +'<legend style="font-weight:700;padding:0 8px">'+(i+1)+'. '+esc(q.enunciado)+'</legend>'
   +(q.alts||[]).map((t,j)=>'<label class="alt"><input type="radio" name="'+q.id+'" value="'+j+'"> <span>'+LETRAS[j]+') '+esc(t)+'</span></label>').join('')
  +'</fieldset>'
 ).join('');

 return ''
 +'<p class="muted"><a href="#/modulo/'+a.modulo+'">← '+(mod?esc(mod.titulo):'Módulo')+'</a></p>'
 +'<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">'
  +'<div>'
   +'<h1 style="margin-bottom:4px">'+esc(a.titulo)+'</h1>'
   +'<p class="muted">'+esc(a.disciplina)+' · '+esc(a.nivel)+' · Estimado: '+a.tempo+' min</p>'
  +'</div>'
  +(concl?'<span class="tag concluido">✓ Aula Concluída</span>':'<button class="btn sm" onclick="marcarConcluida(\''+id+'\')">Marcar como Concluída</button>')
 +'</div>'
 
 // Barra de Ferramentas da Aula
 +'<div style="display:flex;gap:10px;flex-wrap:wrap;margin:12px 0">'
  +'<button id="btn-audio-aula" class="btn-header" onclick="falarTexto(\''+esc(textoAudio).replace(/'/g,"\\'")+'\')">🔊 Ouvir Aula</button>'
  +'<a href="#/professor" class="btn-header">🤖 Dúvidas desta Aula com IA</a>'
 +'</div>'

 // Objetivos
 +'<div class="card destaque">'
  +'<strong>Objetivos de Aprendizagem:</strong>'
  +'<ul style="margin:8px 0 0;padding-left:20px">'+(a.objetivos||[]).map(o=>'<li>'+esc(o)+'</li>').join('')+'</ul>'
 +'</div>'
 
 +secoesHtml
 
 // Caderno de Anotações
 +'<div class="notes-box">'
  +'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">'
   +'<strong>📝 Minhas Anotações desta Aula</strong>'
   +'<span id="status-anotacao" class="muted" style="font-size:0.8rem"></span>'
  +'</div>'
  +'<textarea class="campo" placeholder="Digite seus resumos, percepções e conexões conceituais..." oninput="salvarAnotacaoAula(\''+id+'\', this.value)">'+esc(anotacaoAtual)+'</textarea>'
 +'</div>'
 
 // Questionário de Fixação
 +'<h2>Questões de Fixação</h2>'
 +'<form id="form-quiz" onsubmit="event.preventDefault(); submeterQuiz(\''+id+'\', this)">'
  +quizHtml
  +'<button type="submit" class="btn">Conferir Respostas</button>'
 +'</form>'
 +'<div id="resultado-quiz"></div>';
}

window.marcarConcluida = function(id){
 estado.aulasConcluidas[id]=true;
 salvar();
 aviso('Aula marcada como concluída! 🎉');
 render();
};

window.submeterQuiz = function(aulaId, form){
 const res = corrigirAula(aulaId, form);
 mostrarResultado(res);
 if(res.acertos >= Math.ceil(res.total * 0.7)){
   estado.aulasConcluidas[aulaId]=true;
   salvar();
 }
};

/* View: Revisar (Flashcards 3D) */
function viewRevisar(){
 garantirTodos();
 if(filaRev===null){ filaRev=revisoesPendentes(); revIndice=0; revVerso=false; }
 
 if(!filaRev.length){
  return '<h1>Revisão Espaçada (SRS)</h1>'
   +'<div class="card destaque" style="text-align:center;padding:40px 20px">'
    +'<div style="font-size:3rem;margin-bottom:12px">🎉</div>'
    +'<h2>Tudo em dia por hoje!</h2>'
    +'<p class="muted">Você concluiu todos os cartões agendados para a data de hoje.</p>'
    +'<a href="#/aprender" class="btn">Continuar Aprendendo Aulas Novas</a>'
   +'</div>';
 }

 const cardId=filaRev[revIndice]||filaRev[0];
 const c=achaCartao(cardId);
 if(!c) return '<h1>Erro ao carregar cartão</h1>';

 return ''
 +'<h1>Revisão Espaçada</h1>'
 +'<p class="muted">Cartão '+(revIndice+1)+' de '+filaRev.length+' pendente(s) hoje · <span class="tag">'+esc(c.aula)+'</span></p>'
 +'<div class="flashcard-wrap" onclick="virarCard()">'
  +'<div id="flashcard-box" class="flashcard '+(revVerso?'virado':'')+'">'
   +'<div class="flashcard-lado">'
    +'<p class="muted" style="font-size:0.85rem">FRENTE (clique para virar)</p>'
    +'<h2 style="margin:20px 0;font-size:1.4rem">'+esc(c.frente)+'</h2>'
    +'<span class="btn sec sm">Ver Resposta (Espaço)</span>'
   +'</div>'
   +'<div class="flashcard-verso">'
    +'<p class="muted" style="font-size:0.85rem">VERSO</p>'
    +'<p style="font-size:1.15rem;margin:16px 0">'+esc(c.verso)+'</p>'
   +'</div>'
  +'</div>'
 +'</div>'
 
 +'<div style="display:flex;justify-content:center;gap:10px;margin-top:20px;flex-wrap:wrap">'
  +'<button class="btn sm" style="background:var(--vermelho);border-color:var(--vermelho)" onclick="avaliarCard(\''+c.id+'\', \'dificil\')">1. Difícil (1 dia)</button>'
  +'<button class="btn sm" style="background:var(--amarelo);border-color:var(--amarelo);color:#fff" onclick="avaliarCard(\''+c.id+'\', \'bom\')">2. Bom (3 dias)</button>'
  +'<button class="btn sm" style="background:var(--verde);border-color:var(--verde)" onclick="avaliarCard(\''+c.id+'\', \'facil\')">3. Fácil (7 dias)</button>'
 +'</div>';
}

window.virarCard = function(){
 revVerso=!revVerso;
 const b=$('#flashcard-box'); if(b) b.classList.toggle('virado', revVerso);
};

window.avaliarCard = function(id, nivel){
 responderCartao(id, nivel);
 revVerso=false;
 revIndice++;
 if(revIndice>=filaRev.length){
   filaRev=[];
 }
 render();
};

/* View: Professor Digital (IA) */
let historicoChat = [
 {tipo:'prof', texto:'Olá! Sou seu **Professor Digital de Psicologia**. Estou aqui para esclarecer dúvidas conceituais, debater casos clínicos hipotéticos e ajudar no seu método de estudos.\n\nComo posso ajudar seus estudos hoje?'}
];

function viewProfessor(){
 const msgsHtml=historicoChat.map(m=>''
  +'<div class="chat-msg '+m.tipo+'">'
   +'<div class="chat-avatar">'+(m.tipo==='prof'?'ψ':'👤')+'</div>'
   +'<div class="chat-bubble">'
    +m.texto.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\n/g,'<br>')
   +'</div>'
  +'</div>'
 ).join('');

 return ''
 +'<h1>Professor Digital de Psicologia</h1>'
 +'<p class="muted">Tutor socrático com base em 47 aulas aprovadas e nas diretrizes éticas do CFP.</p>'
 
 // Sugestões de Perguntas
 +'<div style="display:flex;gap:8px;overflow-x:auto;padding-bottom:8px;margin-bottom:12px">'
  +'<button class="btn sec sm" onclick="perguntarDireto(\'O que é reforço negativo e como difere de punição?\')">💡 Reforço Negativo vs Punição</button>'
  +'<button class="btn sec sm" onclick="perguntarDireto(\'Como Freud estruturou o aparelho psíquico?\')">🧠 1ª e 2ª Tópicas de Freud</button>'
  +'<button class="btn sec sm" onclick="perguntarDireto(\'O que é o modelo biopsicossocial?\')">🌿 Modelo Biopsicossocial</button>'
  +'<button class="btn sec sm" onclick="perguntarDireto(\'Quais os limites éticos do sigilo no CFP?\')">⚖️ Ética e Sigilo (CFP)</button>'
 +'</div>'

 +'<div class="card" style="padding:16px">'
  +'<div id="chat-box" class="chat-container">'+msgsHtml+'</div>'
  +'<form id="chat-form" onsubmit="event.preventDefault(); enviarMensagemChat(this)">'
   +'<div style="display:flex;gap:10px">'
    +'<input id="chat-input" class="campo" placeholder="Pergunte sobre conceitos, autores, experimentos ou ética..." autocomplete="off">'
    +'<button type="submit" class="btn" style="flex-shrink:0">Enviar</button>'
   +'</div>'
  +'</form>'
 +'</div>';
}

window.perguntarDireto = function(texto){
 const inp=$('#chat-input');
 if(inp){ inp.value=texto; enviarMensagemChat($('#chat-form')); }
};

window.enviarMensagemChat = async function(form){
 const inp=$('#chat-input');
 const txt=inp.value.trim();
 if(!txt) return;
 inp.value='';
 
 historicoChat.push({tipo:'aluno', texto:txt});
 render();
 
 const box=$('#chat-box'); if(box) box.scrollTop=box.scrollHeight;
 
 const resp = await chamarProfessorIA(txt, estado.ultimaAula);
 historicoChat.push({tipo:'prof', texto:resp.resposta});
 render();
 
 const box2=$('#chat-box'); if(box2) box2.scrollTop=box2.scrollHeight;
};

/* View: Biblioteca */
function viewBiblioteca(){
 const glosList = GLOSSARIO.concat(typeof GLOSSARIO_CAP!=='undefined'?GLOSSARIO_CAP:[]);
 const anotacoesKeys = Object.keys(estado.anotacoes||{});

 return ''
 +'<h1>Biblioteca & Referências</h1>'
 +'<p class="muted">Glossário completo de termos técnicos e suas anotações pessoais.</p>'
 
 +'<div style="margin:16px 0">'
  +'<input id="busca-biblio" class="campo" type="search" placeholder="Buscar termo ou conceito no glossário..." oninput="filtrarBiblioteca(this.value)">'
 +'</div>'
 
 +'<div id="lista-biblio">'
  +glosList.slice(0, 30).map(g=>''
   +'<div class="card" style="margin:10px 0">'
    +'<div style="display:flex;justify-content:space-between;align-items:center">'
     +'<h3 style="margin:0;color:var(--primaria)">'+esc(g.termo)+'</h3>'
     +(g.aula?'<a href="#/aula/'+g.aula+'" class="tag">Ver Aula</a>':'')
    +'</div>'
    +'<p style="margin:6px 0"><strong>Definição:</strong> '+esc(g.simples)+'</p>'
    +(g.academico?'<p class="muted" style="margin:4px 0"><strong>Visão Acadêmica:</strong> '+esc(g.academico)+'</p>':'')
    +(g.exemplo?'<p class="muted" style="margin:4px 0"><strong>Exemplo:</strong> <em>'+esc(g.exemplo)+'</em></p>':'')
   +'</div>'
  ).join('')
 +'</div>';
}

window.filtrarBiblioteca = function(q){
 const norm = q.toLowerCase().trim();
 const glosList = GLOSSARIO.concat(typeof GLOSSARIO_CAP!=='undefined'?GLOSSARIO_CAP:[]);
 const filtrados = glosList.filter(g => g.termo.toLowerCase().includes(norm) || (g.simples||'').toLowerCase().includes(norm));
 const el=$('#lista-biblio');
 if(!el) return;
 if(!filtrados.length){ el.innerHTML='<p class="muted">Nenhum termo encontrado para "'+esc(q)+'".</p>'; return; }
 el.innerHTML = filtrados.slice(0, 30).map(g=>''
  +'<div class="card" style="margin:10px 0">'
   +'<div style="display:flex;justify-content:space-between;align-items:center">'
    +'<h3 style="margin:0;color:var(--primaria)">'+esc(g.termo)+'</h3>'
    +(g.aula?'<a href="#/aula/'+g.aula+'" class="tag">Ver Aula</a>':'')
   +'</div>'
   +'<p style="margin:6px 0"><strong>Definição:</strong> '+esc(g.simples)+'</p>'
   +(g.academico?'<p class="muted" style="margin:4px 0"><strong>Visão Acadêmica:</strong> '+esc(g.academico)+'</p>':'')
  +'</div>'
 ).join('');
};

/* View: Perfil */
function viewPerfil(){
 const p=estado.perfil||{};
 return ''
 +'<h1>Perfil & Configurações</h1>'
 +'<div class="card">'
  +'<h2>Seus Dados de Estudo</h2>'
  +'<label>Apelido ou Nome:<br><input id="perf-nome" class="campo" value="'+esc(p.apelido||'')+'"></label>'
  +'<div style="margin-top:14px">'
   +'<button class="btn sm" onclick="salvarPerfil()">Salvar Alterações</button>'
  +'</div>'
 +'</div>'
 
 +'<div class="card">'
  +'<h2>Conexão com a API do Professor Digital</h2>'
  +'<p class="muted">Configure a URL do servidor local (api_server.py) ou chave de IA.</p>'
  +'<label>Endpoint do Servidor Local:<br><input id="perf-api" class="campo" value="'+esc(estado.apiServidor||'http://localhost:8000/api')+'"></label>'
  +'<div style="margin-top:14px">'
   +'<button class="btn sm" onclick="salvarConfigAPI()">Salvar Configuração da API</button>'
  +'</div>'
 +'</div>'
 
 +'<div class="card">'
  +'<h2>Backup e Armazenamento</h2>'
  +'<p class="muted">Todos os seus estudos ficam salvos exclusivamente neste navegador.</p>'
  +'<button class="btn sec sm" onclick="exportarBackup()">📥 Exportar Dados (Backup)</button>'
  +'<button class="btn sec sm" onclick="$(\'#file-import\').click()">📤 Importar Backup</button>'
  +'<input type="file" id="file-import" style="display:none" onchange="importarBackup(event)" accept=".json">'
 +'</div>';
}

window.salvarPerfil = function(){
 estado.perfil=estado.perfil||{};
 estado.perfil.apelido=$('#perf-nome').value.trim();
 salvar();
 aviso('Perfil atualizado com sucesso!');
};

window.salvarConfigAPI = function(){
 estado.apiServidor=$('#perf-api').value.trim();
 salvar();
 aviso('Configurações de API salvas!');
};

window.exportarBackup = function(){
 const blob=new Blob([JSON.stringify(estado, null, 2)], {type:'application/json'});
 const url=URL.createObjectURL(blob);
 const a=document.createElement('a'); a.href=url; a.download='psicobase-backup-'+dataISO()+'.json'; a.click();
 URL.revokeObjectURL(url);
};

window.importarBackup = function(e){
 const arq=e.target.files[0]; if(!arq) return;
 const r=new FileReader();
 r.onload=()=>{
   try{
     const d=JSON.parse(r.result);
     if(d && typeof d==='object'){
       estado=Object.assign(estadoPadrao(), d);
       salvar();
       aviso('Backup restaurado com sucesso!');
       render();
     }
   }catch(err){ aviso('Arquivo de backup inválido.'); }
 };
 r.readAsText(arq);
};

/* ==================== BUSCA MODAL (CTRL+K) ==================== */
function abrirBuscaModal(){
 const m=$('#modal-busca'); if(m){ m.style.display='flex'; $('#input-busca-modal').focus(); }
}
window.abrirBuscaModal = abrirBuscaModal;

function fecharBuscaModal(){
 const m=$('#modal-busca'); if(m) m.style.display='none';
}
window.fecharBuscaModal = fecharBuscaModal;

window.addEventListener('keydown', e=>{
 if((e.ctrlKey||e.metaKey)&&e.key==='k'){ e.preventDefault(); abrirBuscaModal(); }
 if(e.key==='Escape') fecharBuscaModal();
});

function executarBuscaModal(q){
 const norm=q.toLowerCase().trim();
 const out=$('#modal-busca-resultados');
 if(!norm){ out.innerHTML='<p class="muted">Digite para pesquisar em aulas e no glossário.</p>'; return; }
 
 const aulasMatch = Object.entries(AULAS).filter(([id,a])=>a.titulo.toLowerCase().includes(norm));
 const termosMatch = GLOSSARIO.filter(g=>g.termo.toLowerCase().includes(norm));
 
 let h='';
 if(aulasMatch.length){
   h+='<strong>Aulas Encontradas:</strong><ul style="padding-left:20px">';
   aulasMatch.slice(0,5).forEach(([id,a])=>{
     h+='<li><a href="#/aula/'+id+'" onclick="fecharBuscaModal()">'+esc(a.titulo)+'</a> <span class="muted">('+esc(a.disciplina)+')</span></li>';
   });
   h+='</ul>';
 }
 if(termosMatch.length){
   h+='<strong style="margin-top:12px;display:block">Termos no Glossário:</strong><ul style="padding-left:20px">';
   termosMatch.slice(0,5).forEach(g=>{
     h+='<li><strong>'+esc(g.termo)+':</strong> '+esc(g.simples)+'</li>';
   });
   h+='</ul>';
 }
 if(!aulasMatch.length && !termosMatch.length){
   h='<p class="muted">Nenhum resultado para "'+esc(q)+'".</p>';
 }
 out.innerHTML=h;
}
window.executarBuscaModal = executarBuscaModal;

/* ==================== ROTEADOR ==================== */
function render(){
 encerrarSessao();
 const partes=rota().split('/').filter(Boolean);
 const r=partes[0]||'inicio';
 
 if(!estado.perfil && r!=='bem-vindo'){ location.hash='#/bem-vindo'; return; }
 if(estado.perfil && r==='bem-vindo'){ location.hash='#/inicio'; return; }
 if(r!=='revisar'){ filaRev=null; }
 
 let html='';
 switch(r){
  case 'bem-vindo': html=viewBemVindo(); break;
  case 'inicio': html=viewInicio(); break;
  case 'aprender': html=viewAprender(); break;
  case 'modulo': html=viewModulo(partes[1]); break;
  case 'aula': html=viewAula(partes[1]); break;
  case 'revisar': html=viewRevisar(); break;
  case 'professor': html=viewProfessor(); break;
  case 'biblioteca': html=viewBiblioteca(); break;
  case 'perfil': html=viewPerfil(); break;
  default: html='<h1>Página não encontrada</h1><p><a href="#/inicio">Voltar ao início</a></p>';
 }
 app.innerHTML=html;
 
 const showNav=estado.perfil && r!=='bem-vindo';
 nav.hidden=!showNav;
 header.hidden=!showNav;
 
 document.querySelectorAll('nav.inferior a').forEach(a=>{
  const ativo=a.dataset.nav===r || ((r==='modulo'||r==='aula')&&a.dataset.nav==='aprender');
  if(ativo) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');
 });
 
 document.title=(r==='inicio'||!estado.perfil?'PsicoBase · Plataforma de Estudos':'PsicoBase · '+r.toUpperCase());
 window.scrollTo(0, 0);
}

window.addEventListener('hashchange', render);

/* ==================== INICIALIZAÇÃO ==================== */
aplicarVisual();
render();

})();
</script>
</body>
</html>
"""

# Salva index.html no projeto
with open(r"c:\Users\MatheusRochaLopes\Desktop\PsycoBase\index.html", "w", encoding="utf-8") as f:
    f.write(novo_html)

# Salva PsicoBase.html no projeto para compatibilidade
with open(r"c:\Users\MatheusRochaLopes\Desktop\PsycoBase\PsicoBase.html", "w", encoding="utf-8") as f:
    f.write(novo_html)

# Atualiza também o arquivo em Downloads para que o arquivo ativo do usuário fique atualizado
try:
    with open(r"c:\Users\MatheusRochaLopes\Downloads\PsicoBase (2).html", "w", encoding="utf-8") as f:
        f.write(novo_html)
    print("Atualizado c:\\Users\\MatheusRochaLopes\\Downloads\\PsicoBase (2).html")
except Exception as e:
    print("Aviso ao salvar em downloads:", e)

print("Build concluído com sucesso!")
print("Tamanho do index.html gerado:", len(novo_html), "caracteres")
