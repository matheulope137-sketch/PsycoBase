# -*- coding: utf-8 -*-
"""
Script construtor limpo e robusto do PsicoBase.
Une o Design System Editorial Humanista (limpo, simples, funcional)
com o banco curricular completo e a integração nativa com a API do Professor Digital.
"""
import os
import sys

ORIGINAL_FILE = r"c:\Users\MatheusRochaLopes\Downloads\PsicoBase (1).html"
OUTPUT_INDEX = r"c:\Users\MatheusRochaLopes\Desktop\PsycoBase\index.html"
OUTPUT_PSICO = r"c:\Users\MatheusRochaLopes\Desktop\PsycoBase\PsicoBase.html"

with open(ORIGINAL_FILE, "r", encoding="utf-8") as f:
    orig_content = f.read()

# Extrair bloco de dados curriculares intacto
start_marker = "/* ==================== CONSTANTES ==================== */"
end_marker = "/* ==================== ESTADO ==================== */"

s_idx = orig_content.find(start_marker)
e_idx = orig_content.find(end_marker)

if s_idx == -1 or e_idx == -1:
    raise ValueError("Não foi possível encontrar os marcadores de dados no arquivo original.")

curriculum_data = orig_content[s_idx:e_idx].strip()
print(f"Bloco curricular extraído com sucesso: {len(curriculum_data)} caracteres.")

# Construir CSS limpo, ergonômico e editorial
CSS_CODE = """
:root {
  /* Paleta Editorial Humanista (Modo Claro) */
  --bg-canvas: #F8F6F0;
  --bg-card: #FFFFFF;
  --bg-fichamento: #FAF8F4;
  --bg-subtil: #F1ECE3;
  --fg-base: #242124;
  --fg-muted: #665F6B;
  --borda-suave: #E6E0D6;
  --borda-foco: #7A5C91;

  /* Cores de Identidade */
  --primaria: #4A1525;
  --primaria-hover: #360D19;
  --primaria-tint: rgba(74, 21, 37, 0.08);
  --secundaria: #7A5C91;
  --secundaria-tint: rgba(122, 92, 145, 0.12);

  /* Acentos Funcionais Serenos */
  --salvia: #3A7356;
  --salvia-tint: rgba(58, 115, 86, 0.12);
  --terracota: #BD6148;
  --terracota-tint: rgba(189, 97, 72, 0.12);
  --ambar: #C28D38;
  --ambar-tint: rgba(194, 141, 56, 0.12);

  /* Tipografia */
  --font-serif: 'Lora', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --radius-card: 14px;
  --radius-pill: 9999px;
  --sombra-card: 0 4px 16px rgba(45, 35, 30, 0.04), 0 1px 3px rgba(45, 35, 30, 0.03);
  --sombra-hover: 0 8px 24px rgba(45, 35, 30, 0.07);
}

body.escuro {
  /* Modo Escuro Introspectivo */
  --bg-canvas: #131217;
  --bg-card: #1E1B24;
  --bg-fichamento: #25222E;
  --bg-subtil: #2C2736;
  --fg-base: #F4F1F7;
  --fg-muted: #A39BAA;
  --borda-suave: #2E2938;
  --borda-foco: #C7A7EC;

  --primaria: #E29BB0;
  --primaria-hover: #F0B3C4;
  --primaria-tint: rgba(226, 155, 176, 0.16);
  --secundaria: #C7A7EC;
  --secundaria-tint: rgba(199, 167, 236, 0.18);

  --salvia: #66D39D;
  --salvia-tint: rgba(102, 211, 157, 0.15);
  --terracota: #FF8A73;
  --terracota-tint: rgba(255, 138, 115, 0.15);
  --ambar: #F0BF65;
  --ambar-tint: rgba(240, 191, 101, 0.15);

  --sombra-card: 0 4px 20px rgba(0, 0, 0, 0.35);
  --sombra-hover: 0 8px 28px rgba(0, 0, 0, 0.5);
}

/* Reset Básico */
*, *::before, *::after { box-sizing: border-box; }
[hidden] { display: none !important; }
html { scroll-behavior: smooth; }

body {
  margin: 0; padding: 0;
  font-family: var(--font-sans);
  background: var(--bg-canvas);
  color: var(--fg-base);
  line-height: 1.65;
  padding-bottom: 84px;
  -webkit-font-smoothing: antialiased;
}
body.grande { font-size: 112%; }

/* Layout Geral */
.container {
  max-width: 860px;
  margin: 0 auto;
  padding: 20px 16px;
}
main:focus { outline: none; }

/* Tipografia */
h1, h2, h3 { font-family: var(--font-serif); font-weight: 600; color: var(--fg-base); margin-top: 0; }
h1 { font-size: 1.85rem; line-height: 1.25; margin-bottom: 0.5rem; }
h2 { font-size: 1.35rem; margin-top: 1.8rem; margin-bottom: 0.6rem; color: var(--primaria); }
h3 { font-size: 1.1rem; margin-top: 1.2rem; margin-bottom: 0.4rem; }
p { margin: 0 0 1rem 0; }
.muted { color: var(--fg-muted); font-size: 0.92rem; }
a { color: var(--secundaria); text-decoration: none; font-weight: 500; }
a:hover { text-decoration: underline; }

/* Barra Superior / Header */
header.app-header {
  position: sticky; top: 0; z-index: 40;
  background: var(--bg-canvas);
  border-bottom: 1px solid var(--borda-suave);
  backdrop-filter: blur(10px);
  padding: 10px 16px;
}
.header-wrap {
  max-width: 860px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
}
.brand-link {
  display: flex; align-items: center; gap: 10px;
  color: var(--fg-base); text-decoration: none; font-family: var(--font-serif);
  font-size: 1.25rem; font-weight: 700;
}
.brand-icon {
  width: 32px; height: 32px; border-radius: 8px;
  background: var(--primaria); color: #FFF;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem; font-family: var(--font-serif);
}
body.escuro .brand-icon { color: #131217; }
.header-actions {
  display: flex; align-items: center; gap: 8px;
}

/* Pomodoro Widget */
.pomo-widget {
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--bg-card); border: 1px solid var(--borda-suave);
  padding: 4px 12px; border-radius: var(--radius-pill);
  font-size: 0.85rem; font-weight: 600;
}
.pomo-pulse {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--salvia);
}
.pomo-pulse.rodando {
  animation: pulseRespiro 2s infinite ease-in-out;
}
@keyframes pulseRespiro {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.4); opacity: 1; }
}
.pomo-btn {
  background: none; border: none; cursor: pointer; padding: 2px 4px;
  font-size: 0.85rem; color: var(--fg-base);
}

/* Botões */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  background: var(--primaria); color: #FFFFFF;
  border: 1px solid var(--primaria); border-radius: 10px;
  padding: 10px 18px; font-family: var(--font-sans);
  font-size: 0.94rem; font-weight: 600; cursor: pointer;
  text-decoration: none; transition: all 0.2s ease;
  min-height: 42px;
}
body.escuro .btn { color: #131217; }
.btn:hover { background: var(--primaria-hover); border-color: var(--primaria-hover); text-decoration: none; }
.btn.sec {
  background: var(--bg-card); color: var(--fg-base);
  border: 1px solid var(--borda-suave);
}
.btn.sec:hover { background: var(--bg-subtil); border-color: var(--secundaria); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* Cards & Superfícies */
.card {
  background: var(--bg-card);
  border: 1px solid var(--borda-suave);
  border-radius: var(--radius-card);
  padding: 20px;
  margin: 14px 0;
  box-shadow: var(--sombra-card);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  position: relative;
  overflow: hidden;
}
.card.destaque {
  background: linear-gradient(135deg, var(--bg-card) 60%, var(--bg-fichamento) 100%);
  border-left: 5px solid var(--primaria);
}
.card.destaque::after {
  content: "Ψ"; position: absolute; right: 12px; bottom: -8px;
  font-size: 5rem; font-family: var(--font-serif);
  color: var(--fg-base); opacity: 0.04; pointer-events: none;
}

/* Grids */
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
.grid-stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 14px 0; }
.stat-box {
  background: var(--bg-card); border: 1px solid var(--borda-suave);
  border-radius: 12px; padding: 14px; text-align: center;
}
.stat-box b {
  display: block; font-size: 1.5rem; font-family: var(--font-serif);
  color: var(--primaria); line-height: 1.1; margin-bottom: 4px;
}
.stat-box span { font-size: 0.8rem; color: var(--fg-muted); text-transform: uppercase; letter-spacing: 0.5px; }

/* Barras de Progresso */
.barra {
  height: 8px; background: var(--bg-subtil); border-radius: 99px; overflow: hidden;
  margin: 8px 0;
}
.barra > div { height: 100%; background: var(--salvia); border-radius: 99px; transition: width 0.4s ease; }

/* Tags & Badges */
.tag {
  display: inline-block; padding: 3px 10px; border-radius: var(--radius-pill);
  font-size: 0.78rem; font-weight: 600;
  background: var(--secundaria-tint); color: var(--secundaria);
}
.tag.concluida { background: var(--salvia-tint); color: var(--salvia); }
.tag.pendente { background: var(--ambar-tint); color: var(--ambar); }

/* Avisos e Citações */
.aviso-conteudo {
  border-left: 4px solid var(--secundaria);
  background: var(--secundaria-tint);
  padding: 12px 16px; border-radius: 8px; margin: 16px 0;
  font-size: 0.92rem;
}
.banner-etico {
  border: 1px solid var(--borda-suave);
  background: var(--bg-fichamento);
  padding: 12px 16px; border-radius: 12px; margin: 16px 0;
  font-size: 0.88rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;
}

/* Formulários */
.campo {
  width: 100%; padding: 11px 14px; border-radius: 10px;
  border: 1px solid var(--borda-suave); background: var(--bg-card);
  color: var(--fg-base); font-family: inherit; font-size: 0.95rem;
  margin-top: 6px; margin-bottom: 14px;
  transition: border-color 0.2s ease;
}
.campo:focus { outline: none; border-color: var(--borda-foco); }
textarea.campo { min-height: 100px; resize: vertical; line-height: 1.5; }
fieldset { border: 0; padding: 0; margin: 16px 0; }
legend { font-weight: 600; font-size: 1rem; margin-bottom: 8px; }

/* Opções de Radio e Checkbox Estilizadas */
.opcoes label, .alt {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid var(--borda-suave);
  border-radius: 10px; margin: 8px 0; cursor: pointer;
  background: var(--bg-card); transition: all 0.15s ease;
  min-height: 48px;
}
.opcoes label:hover, .alt:hover { border-color: var(--secundaria); background: var(--secundaria-tint); }
.opcoes label:has(input:checked), .alt:has(input:checked) {
  border-color: var(--primaria); background: var(--secundaria-tint); font-weight: 600;
}

/* Questões e Resultados */
.q-bloco {
  border: 1px solid var(--borda-suave); border-radius: 12px;
  padding: 16px; margin: 16px 0; background: var(--bg-card);
}
.res {
  border-radius: 12px; padding: 14px 16px; margin: 12px 0;
  background: var(--bg-card); border: 1px solid var(--borda-suave);
}
.res.ok { border-left: 5px solid var(--salvia); background: var(--salvia-tint); }
.res.erro { border-left: 5px solid var(--terracota); background: var(--terracota-tint); }

/* Flashcards SRS 3D */
.flashcard-stage {
  perspective: 1000px; margin: 20px 0; min-height: 220px;
}
.flashcard-inner {
  width: 100%; min-height: 220px; border-radius: 16px;
  background: var(--bg-card); border: 1px solid var(--borda-suave);
  padding: 24px; box-shadow: var(--sombra-card);
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center; cursor: pointer; transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
  position: relative;
}
.flashcard-inner:hover { transform: translateY(-3px); box-shadow: var(--sombra-hover); }

/* Detalhes / Pare e responda */
details.card summary {
  cursor: pointer; font-weight: 600; color: var(--primaria); outline: none;
  padding: 4px 0; user-select: none;
}
details[open] summary { margin-bottom: 12px; }

/* Navegação Inferior / Mobile */
nav.inferior {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 50;
  background: var(--bg-card); border-top: 1px solid var(--borda-suave);
  display: flex; justify-content: space-around;
  padding-bottom: env(safe-area-inset-bottom);
}
nav.inferior a {
  flex: 1; text-align: center; padding: 10px 2px;
  font-size: 0.78rem; text-decoration: none; color: var(--fg-muted);
  display: flex; flex-direction: column; align-items: center; gap: 4px;
}
nav.inferior a[aria-current="page"] {
  color: var(--primaria); font-weight: 700;
}

/* Toast Notificações */
.toast {
  position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
  background: #242124; color: #FFF; padding: 10px 20px; border-radius: var(--radius-pill);
  font-size: 0.9rem; font-weight: 500; z-index: 100;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

/* Telas Maiores (Desktop) */
@media (min-width: 768px) {
  .grid-stats { grid-template-columns: repeat(4, 1fr); }
  .grid { grid-template-columns: repeat(3, 1fr); }
}
@media (min-width: 992px) {
  body { padding-left: 240px; padding-bottom: 20px; }
  .container { max-width: 900px; padding: 32px 24px; }
  header.app-header { display: none; }
  nav.inferior {
    top: 0; bottom: 0; right: auto; width: 240px;
    flex-direction: column; justify-content: flex-start;
    padding: 28px 16px; border-top: 0; border-right: 1px solid var(--borda-suave);
    gap: 8px;
  }
  .nav-brand-desktop {
    display: flex; align-items: center; gap: 10px;
    font-family: var(--font-serif); font-size: 1.35rem; font-weight: 700;
    color: var(--fg-base); margin-bottom: 24px; text-decoration: none;
  }
  nav.inferior a {
    flex: none; flex-direction: row; justify-content: flex-start;
    padding: 12px 16px; border-radius: 10px; font-size: 0.95rem; gap: 12px;
  }
  nav.inferior a[aria-current="page"] {
    background: var(--primaria-tint); color: var(--primaria);
  }
}
"""

# Construir JavaScript modular, limpo e à prova de quebras
JS_FRAMEWORK = """
/* ==================== ESTADO E PERSISTÊNCIA ==================== */
function estadoPadrao(){
 return {perfil:null, aulasConcluidas:{}, tentativas:[], cartoes:{}, minPorDia:{}, anotacoes:{}, ultimaAula:null, abertas:{}, tema:'claro', fonte:'normal', criadoEm:Date.now()};
}
function carregar(){
 let s=null;
 try{ s=JSON.parse(localStorage.getItem(CHAVE)); }catch(e){ s=null; }
 return Object.assign(estadoPadrao(), (s && typeof s==='object')?s:{});
}
let estado=carregar();
const app=document.getElementById('app');
const nav=document.getElementById('nav');
let sessao=null;
let obPasso=1;
let obDados={nivel:'',objetivo:'',tempo:'',preferencias:[],apelido:''};
let filaRev=null;
let revVerso=false;

function salvar(){
 try{ localStorage.setItem(CHAVE, JSON.stringify(estado)); return true; }
 catch(e){ aviso('Não foi possível salvar neste navegador.'); return false; }
}
function garantirCartoes(aulaId){
 const a=AULAS[aulaId]; if(!a || !a.cartoes) return;
 a.cartoes.forEach(c=>{ if(!estado.cartoes[c.id]) estado.cartoes[c.id]={stage:0,prox:diaNum(),vezes:0,historico:[]}; });
}
function garantirTodos(){ Object.keys(estado.abertas||{}).forEach(garantirCartoes); }
garantirTodos();

/* ==================== UTILITÁRIOS ==================== */
const $=(s,r=document)=>r.querySelector(s);
function esc(s){ return String(s===undefined||s===null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function dataISO(d){ d=d||new Date(); return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
function diaNum(d){ d=d||new Date(); return Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/86400000); }
function aviso(msg){
 const t=$('#aviso'); if(!t) return;
 t.textContent=msg; t.hidden=false;
 clearTimeout(aviso._t); aviso._t=setTimeout(()=>{ t.hidden=true; },3200);
}
function rota(){ return (location.hash||'#/inicio').replace(/^#/,''); }
function aplicarVisual(){
 document.body.classList.toggle('escuro', estado.tema==='escuro');
 document.body.classList.toggle('grande', estado.fonte==='grande');
}
function opcoesRadio(nome,mapa,atual){
 return Object.entries(mapa).map(([v,t])=>'<label class="alt"><input type="radio" name="'+nome+'" value="'+esc(v)+'"'+(atual===v?' checked':'')+'> <span>'+esc(t)+'</span></label>').join('');
}
function opcoesCheck(nome,mapa,lista){
 return Object.entries(mapa).map(([v,t])=>'<label class="alt"><input type="checkbox" name="'+nome+'" value="'+esc(v)+'"'+(lista.includes(v)?' checked':'')+'> <span>'+esc(t)+'</span></label>').join('');
}

/* ==================== POMODORO INTEGRADO ==================== */
let pomoSegundos = 25 * 60;
let pomoTimer = null;
let pomoRodando = false;

function formatarTempo(s){
 const m = Math.floor(s / 60); const seg = s % 60;
 return String(m).padStart(2, '0') + ':' + String(seg).padStart(2, '0');
}
function togglePomodoro(){
 if(pomoRodando){
  clearInterval(pomoTimer); pomoRodando = false;
 } else {
  pomoRodando = true;
  pomoTimer = setInterval(()=>{
   if(pomoSegundos > 0){
    pomoSegundos--;
    atualizarPomoUI();
   } else {
    clearInterval(pomoTimer); pomoRodando = false;
    pomoSegundos = 25 * 60;
    aviso('Sessão Pomodoro concluída! Descanse 5 minutos.');
    atualizarPomoUI();
   }
  }, 1000);
 }
 atualizarPomoUI();
}
function resetPomodoro(){
 clearInterval(pomoTimer); pomoRodando = false;
 pomoSegundos = 25 * 60;
 atualizarPomoUI();
}
function atualizarPomoUI(){
 document.querySelectorAll('.pomo-tempo').forEach(el => el.textContent = formatarTempo(pomoSegundos));
 document.querySelectorAll('.pomo-pulse').forEach(el => el.classList.toggle('rodando', pomoRodando));
 document.querySelectorAll('.pomo-play-btn').forEach(el => el.textContent = pomoRodando ? '⏸' : '▶');
}

/* ==================== SESSÃO DE ESTUDO ==================== */
function iniciarSessao(id){ encerrarSessao(); sessao={id:id, inicio:Date.now()}; }
function encerrarSessao(){
 if(!sessao) return;
 const min=Math.min((Date.now()-sessao.inicio)/60000, 120);
 const k=dataISO();
 estado.minPorDia[k]=(estado.minPorDia[k]||0)+min;
 sessao=null; salvar();
}
window.addEventListener('pagehide', encerrarSessao);
document.addEventListener('visibilitychange', ()=>{ if(document.visibilityState==='hidden') encerrarSessao(); });

/* ==================== REPETIÇÃO ESPAÇADA (SRS) ==================== */
function revisoesPendentes(){
 garantirTodos();
 return Object.entries(estado.cartoes).filter(([id,c])=>c.prox<=diaNum()).map(([id])=>id);
}
function achaCartao(id){
 for(const a of Object.values(AULAS)){
  const c=(a.cartoes||[]).find(x=>x.id===id);
  if(c) return {frente:c.frente, verso:c.verso, aula:a.titulo};
 }
 return null;
}
function responderCartao(id,nivel){
 const c=estado.cartoes[id]; if(!c) return;
 let s=c.stage;
 if(nivel==='nao') s=0;
 else if(nivel==='dificil') s=Math.max(0,s-1);
 else if(nivel==='facil') s=Math.min(INTERVALOS.length-1,s+1);
 c.stage=s; c.prox=diaNum()+INTERVALOS[s];
 c.vezes++; c.historico.push({d:dataISO(), n:nivel});
 salvar();
}

/* ==================== CORREÇÃO DE QUIZZES ==================== */
function corrigirAula(aulaId,form){
 const a=AULAS[aulaId]; let acertos=0; const res=[];
 a.questoes.forEach(q=>{
  const v=form.querySelector('input[name="'+q.id+'"]:checked');
  const marcada=v?Number(v.value):-1;
  const ok=marcada===q.correta;
  if(ok) acertos++;
  res.push({q:q, marcada:marcada, ok:ok});
  estado.tentativas.push({d:dataISO(), aula:aulaId, q:q.id, ok:ok, marcada:marcada});
 });
 salvar();
 return {acertos:acertos, total:a.questoes.length, res:res};
}
function mostrarResultado(r){
 const pct=Math.round(r.acertos/r.total*100);
 const linhas=r.res.map(x=>{
  const cls=x.ok?'ok':'erro';
  const rotulo=x.ok?'Correta':'Incorreta';
  const detalhe=x.ok?'':'<p style="margin:4px 0">Sua resposta: '+(x.marcada>=0?LETRAS[x.marcada]+') '+esc(x.q.alts[x.marcada]):'não respondida')+'.<br>Correta: '+LETRAS[x.q.correta]+') '+esc(x.q.alts[x.q.correta])+'.</p>';
  return '<div class="res '+cls+'"><p style="margin:0 0 4px 0"><strong>'+rotulo+'.</strong> '+esc(x.q.enunciado)+'</p>'+detalhe+'<p class="muted" style="margin:4px 0 0 0">'+esc(x.q.justificativa)+'</p></div>';
 }).join('');
 const dica=r.acertos===r.total?'Excelente! Progrida para a próxima aula ou revise seus flashcards.':'Revise os pontos conceituais das questões incorretas.';
 $('#resultado-quiz').innerHTML='<div class="card" style="border-left:5px solid '+(r.acertos===r.total?'var(--salvia)':'var(--ambar)')+'"><h3 style="margin-top:0">Resultado: '+r.acertos+' de '+r.total+' ('+pct+'%)</h3><p>'+dica+'</p></div>'+linhas;
}

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
 return {total:total, acertos:acertos, pct:total?Math.round(acertos/total*100):null, concl:concl, totalAulas:Object.keys(AULAS).length, minutos:minutos, pend:pend, previstas:previstas};
}
function proximaAula(){
 const ord=Object.keys(AULAS);
 const ult=estado.ultimaAula;
 if(ult && AULAS[ult] && !estado.aulasConcluidas[ult]) return ult;
 return ord.find(id=>!estado.aulasConcluidas[id])||ord[0];
}

/* ==================== PROFESSOR DIGITAL (INTEGRAÇÃO API LOCAL & IA) ==================== */
const API_LOCAL_URL = 'http://127.0.0.1:8000/api';
const IA_CHAVE_STORAGE = 'psicobase-ia';

function lerChaveIA(){
 try{ const c=JSON.parse(localStorage.getItem(IA_CHAVE_STORAGE)); return (c&&c.chave)?String(c.chave):null; }
 catch(e){ return null; }
}
function salvarChaveIA(k){
 try{ localStorage.setItem(IA_CHAVE_STORAGE, JSON.stringify({chave:k})); return true; }
 catch(e){ return false; }
}

async function testarConexaoAPI(){
 try{
  const r = await fetch(API_LOCAL_URL+'/status', {signal: AbortSignal.timeout(1500)});
  return r.ok;
 }catch(e){ return false; }
}

async function perguntarProfessorDigital(aulaId, pergunta){
 const payload = { mensagem: pergunta, aulaId: aulaId };
 
 // 1. Tentar primeiro o servidor local Python (api_server.py)
 try {
  const r = await fetch(API_LOCAL_URL+'/professor/chat', {
   method: 'POST',
   headers: {'Content-Type': 'application/json'},
   body: JSON.stringify(payload),
   signal: AbortSignal.timeout(4000)
  });
  if(r.ok){
   const dados = await r.json();
   return { resposta: dados.resposta, fontes: dados.fontes||[], origem: 'api_local', status: dados.status||'ok' };
  }
 } catch(err) {
  // Servidor local offline, prosseguir para fallback
 }

 // 2. Fallback: Verificação de Guardrails Éticos no cliente
 const nTxt = String(pergunta||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
 if(['suicid','me matar','quero morrer','automutil','me cortar'].some(t => nTxt.includes(t))){
  return {
   resposta: 'Sinto muito que você esteja passando por esse sofrimento. Como professor digital educativo, não posso oferecer suporte clínico. Procure agora o CVV pelo telefone 188 (ligação gratuita 24h) ou SAMU 192.',
   fontes: ['CVV 188 - Centro de Valorização da Vida'],
   origem: 'guarda_etica',
   status: 'crise'
  };
 }
 if(['tenho depressao','tenho ansiedade','meu diagnostico','qual remedio','dose de'].some(t => nTxt.includes(t))){
  return {
   resposta: 'Não posso diagnosticar condições de saúde nem prescrever condutas. O PsicoBase tem finalidade estritamente educacional. Para avaliação individualizada, consulte um psicólogo registrado no CRP.',
   fontes: ['Código de Ética do Psicólogo - Resolução CFP 010/2005'],
   origem: 'guarda_etica',
   status: 'diagnostico'
  };
 }

 // 3. Fallback Heurístico Local baseado no conteúdo aprovado da aula
 const aula = AULAS[aulaId];
 if(aula){
  const resumo = (aula.resumo||[]).join(' ');
  const autores = (aula.autores||[]).map(a => a.nome+': '+a.texto).join('. ');
  return {
   resposta: 'Segundo os fundamentos desta aula ("'+aula.titulo+'"): ' + resumo + (autores?' Principais referências: '+autores:''),
   fontes: aula.referencias||[],
   origem: 'heuristica_local',
   status: 'ok'
  };
 }

 return {
  resposta: 'Para obter respostas aprofundadas com o Professor Digital, certifique-se de que o servidor Python local está rodando (python api_server.py) ou configure sua chave de IA em Perfil.',
  fontes: [],
  origem: 'aviso',
  status: 'ok'
 };
}

/* ==================== VIEWS & TELAS ==================== */

function viewInicio(){
 const p=estado.perfil||{};
 const st=estatisticas();
 const prox=proximaAula();
 const aulaObj=AULAS[prox]||AULAS['m1-a1'];
 const h=new Date().getHours();
 const sauda=h<12?'Bom dia':(h<18?'Boa tarde':'Boa noite');
 const nome=p.apelido?', '+esc(p.apelido):'';
 const conceito=GLOSSARIO[diaNum()%GLOSSARIO.length];

 return '<div style="margin-bottom:24px">'
  +'<h1 style="margin-bottom:4px">'+sauda+nome+'.</h1>'
  +'<p class="muted" style="font-family:var(--font-serif);font-style:italic;font-size:1.05rem">'
   +'"O espaço onde a mente humana é estudada com profundidade, método e acolhimento."'
  +'</p>'
 +'</div>'
 
 +'<div class="card destaque">'
  +'<span class="tag pendente">Sessão em Andamento</span>'
  +'<h2 style="margin:8px 0 4px 0">'+esc(aulaObj.titulo)+'</h2>'
  +'<p class="muted" style="margin-bottom:14px">'+esc(aulaObj.disciplina)+' · Estimado: '+aulaObj.tempo+' min</p>'
  +'<a href="#/aula/'+prox+'" class="btn">Retomar Fichamento →</a>'
 +'</div>'

 +'<div class="grid-stats">'
  +'<div class="stat-box"><b>'+st.concl+'/'+st.totalAulas+'</b><span>Aulas Lidas</span></div>'
  +'<div class="stat-box"><b>'+st.pend+'</b><span>Revisões Hoje</span></div>'
  +'<div class="stat-box"><b>'+Math.round(st.minutos)+'m</b><span>Foco Acumulado</span></div>'
  +'<div class="stat-box"><b>'+(st.pct===null?'—':st.pct+'%')+'</b><span>Precisão Quizzes</span></div>'
 +'</div>'

 +'<div class="card">'
  +'<span class="tag">Conceito do Dia</span>'
  +'<h3 style="margin:8px 0 4px 0">'+esc(conceito.termo)+'</h3>'
  +'<p style="margin-bottom:8px">'+esc(conceito.simples)+'</p>'
  +'<a href="#/biblioteca" style="font-size:0.9rem">Consultar na Biblioteca →</a>'
 +'</div>'

 +'<div class="card">'
  +'<h3>Acesso Rápido aos Eixos</h3>'
  +'<p class="muted">Navegue pelas abordagens clássicas e contemporâneas da Psicologia.</p>'
  +'<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">'
   +'<a href="#/aprender" class="btn sec">Explorar 12 Módulos</a>'
   +'<a href="#/revisar" class="btn sec">Praticar Flashcards ('+st.pend+')</a>'
  +'</div>'
 +'</div>';
}

function viewAprender(){
 const cards=MODULOS.map(m=>{
  const aulas=Object.entries(AULAS).filter(([id,a])=>a.modulo===m.id);
  const feitas=aulas.filter(([id])=>estado.aulasConcluidas[id]).length;
  const status=aulas.length?aulas.length+' aula(s) · '+feitas+' concluída(s)':'Em preparação';
  return '<a class="card" href="#/modulo/'+m.id+'" style="display:block;text-decoration:none;color:inherit">'
   +'<div style="display:flex;justify-content:space-between;align-items:flex-start">'
    +'<div>'
     +'<span class="tag">Eixo '+m.id+'</span>'
     +'<h3 style="margin:6px 0 4px 0">'+esc(m.titulo)+'</h3>'
     +'<p class="muted" style="margin:0">'+esc(m.desc)+'</p>'
    +'</div>'
    +'<span class="tag '+(feitas===aulas.length&&aulas.length?'concluida':'')+'">'+status+'</span>'
   +'</div>'
  +'</a>';
 }).join('');

 return '<h1>Eixos Temáticos</h1>'
  +'<p class="muted">Os 12 módulos estruturais da ciência psicológica. Conteúdos pedagógicos com referências oficiais.</p>'
  +cards;
}

function viewModulo(n){
 const m=MODULOS.find(x=>String(x.id)===String(n));
 if(!m) return '<h1>Módulo não encontrado</h1><p><a href="#/aprender">Voltar</a></p>';
 const aulas=Object.entries(AULAS).filter(([id,a])=>a.modulo===m.id);
 const lista=aulas.length
  ?aulas.map(([id,a])=>'<div class="card" style="margin:10px 0">'
    +'<div style="display:flex;justify-content:space-between;align-items:center">'
     +'<div>'
      +'<h3 style="margin:0 0 4px 0"><a href="#/aula/'+id+'">'+esc(a.titulo)+'</a></h3>'
      +'<span class="muted">'+esc(a.nivel)+' · '+a.tempo+' min</span>'
     +'</div>'
     +(estado.aulasConcluidas[id]?'<span class="tag concluida">Concluída ✓</span>':'<a href="#/aula/'+id+'" class="btn sec" style="padding:6px 14px">Estudar</a>')
    +'</div>'
   +'</div>').join('')
  :'<div class="card"><p class="muted">Aulas em preparação editorial para este módulo.</p></div>';

 return '<p class="muted"><a href="#/aprender">← Todos os Eixos</a></p>'
  +'<h1>Módulo '+m.id+' — '+esc(m.titulo)+'</h1>'
  +'<p>'+esc(m.desc)+'</p>'
  +'<h2>Aulas Disponíveis</h2>'
  +lista;
}

function viewAula(id){
 const a=AULAS[id];
 if(!a) return '<h1>Aula não encontrada</h1><p><a href="#/aprender">Voltar</a></p>';
 iniciarSessao(id);
 estado.ultimaAula=id;
 estado.abertas=estado.abertas||{}; estado.abertas[id]=true;
 garantirCartoes(id);
 salvar();

 const mod=MODULOS.find(m=>m.id===a.modulo);
 const ord=Object.keys(AULAS);
 const prox=ord[ord.indexOf(id)+1];
 const concl=!!estado.aulasConcluidas[id];

 const secoes=a.secoes.map(s=>'<h2>'+esc(s.t)+'</h2>'+s.p.map(t=>'<p>'+esc(t)+'</p>').join('')
  +(s.pausa?'<details class="card"><summary>Pare e responda: '+esc(s.pausa.p)+'</summary><p class="muted">'+esc(s.pausa.r)+'</p></details>':'')).join('');

 const quiz=a.questoes.map((q,i)=>
  '<fieldset class="q-bloco"><legend>'+(i+1)+'. '+esc(q.enunciado)+'</legend>'
  +q.alts.map((t,j)=>'<label class="alt"><input type="radio" name="'+q.id+'" value="'+j+'"> <span>'+LETRAS[j]+') '+esc(t)+'</span></label>').join('')
  +'</fieldset>').join('');

 return '<p class="muted"><a href="#/modulo/'+a.modulo+'">← '+esc(mod?mod.titulo:'Módulo')+'</a></p>'
  +'<h1>'+esc(a.titulo)+'</h1>'
  +'<p class="muted">'+esc(a.disciplina)+' · Nível: '+esc(a.nivel)+' · Tempo: '+a.tempo+' min</p>'
  
  +'<div class="card" style="background:var(--bg-fichamento)">'
   +'<strong>Objetivos de Aprendizagem</strong>'
   +'<ul style="margin:8px 0;padding-left:20px">'+a.objetivos.map(o=>'<li>'+esc(o)+'</li>').join('')+'</ul>'
   +'<span class="muted">Conhecimentos prévios: '+esc(a.previos||'Nenhum.')+'</span>'
  +'</div>'

  +(a.alerta?'<div class="aviso-conteudo">'+esc(a.alerta)+'</div>':'')
  +secoes
  
  +(a.resumo?'<h2>Resumo do Fichamento</h2><ol style="padding-left:20px">'+a.resumo.map(r=>'<li>'+esc(r)+'</li>').join('')+'</ol>':'')
  +(a.referencias?'<h2>Referências</h2><ul style="padding-left:20px">'+a.referencias.map(r=>'<li class="muted">'+esc(r)+'</li>').join('')+'</ul>':'')

  +'<h2>Exercícios de Fixação</h2>'
  +'<form id="form-quiz" data-aula="'+id+'">'+quiz+'<button class="btn" type="submit">Corrigir Questões</button></form>'
  +'<div id="resultado-quiz" aria-live="polite"></div>'

  +'<h2>Professor Digital (Tutor de Psicologia)</h2>'
  +'<div class="banner-etico">'
   +'<span>Apoio estudantil conceitual. Não realiza diagnóstico.</span>'
   +'<a href="https://cvv.org.br" target="_blank" rel="noopener noreferrer">Apoio Emocional: CVV 188</a>'
  +'</div>'
  +'<form id="form-tutor" data-aula="'+id+'">'
   +'<label>Tire sua dúvida sobre esta aula:<br>'
    +'<textarea class="campo" rows="3" placeholder="Ex.: Como diferenciar reforço negativo de punição neste contexto?"></textarea>'
   +'</label>'
   +'<button class="btn" type="submit">Perguntar ao Professor Digital</button>'
  +'</form>'
  +'<div id="resp-tutor" style="margin-top:12px" aria-live="polite"></div>'

  +'<h2>Anotações do Estudante</h2>'
  +'<textarea id="nota" class="campo" rows="4" placeholder="Escreva suas reflexões sobre a aula...">'+esc(estado.anotacoes[id]||'')+'</textarea>'
  +'<div style="margin-bottom:20px">'
   +'<button class="btn sec" type="button" data-action="salvar-nota" data-aula="'+id+'">Salvar Anotação</button>'
   +'<button class="btn" type="button" data-action="concluir" data-aula="'+id+'" style="margin-left:8px">'
    +(concl?'Aula Concluída ✓':'Marcar como Concluída')
   +'</button>'
  +'</div>'

  +'<div class="card" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">'
   +(prox?'<a href="#/aula/'+prox+'" class="btn">Próxima Aula →</a>':'<span class="muted">Fim do módulo.</span>')
   +'<a href="#/revisar" class="btn sec">Ir para os Flashcards</a>'
  +'</div>';
}

function viewRevisar(){
 garantirTodos();
 if(filaRev===null){ filaRev=revisoesPendentes(); revVerso=false; }
 let corpo='';

 if(!filaRev.length){
  const futuras=Object.values(estado.cartoes).map(c=>c.prox).filter(p=>p>diaNum()).sort((x,y)=>x-y);
  const txt=futuras.length?'Próxima revisão em '+(futuras[0]-diaNum())+' dia(s).':'Todos os flashcards estão em dia!';
  corpo='<div class="card" style="text-align:center;padding:36px 20px">'
   +'<h2>Tudo em dia!</h2>'
   +'<p class="muted">'+txt+'</p>'
   +'<a href="#/aprender" class="btn">Avançar em Novas Aulas</a>'
  +'</div>';
 } else {
  const c=achaCartao(filaRev[0]);
  corpo='<p class="muted">Cartões pendentes para hoje: '+filaRev.length+'</p>'
   +'<div class="flashcard-stage">'
    +'<div class="flashcard-inner" data-action="virar">'
     +'<span class="tag" style="position:absolute;top:14px;left:14px">'+esc(c.aula)+'</span>'
     +'<h2 style="margin:20px 0;font-size:1.4rem">'+esc(c.frente)+'</h2>'
     +(revVerso?'<hr style="width:80%;border:0;border-top:1px solid var(--borda-suave);margin:14px 0">'
      +'<p style="font-size:1.1rem;color:var(--primaria)">'+esc(c.verso)+'</p>':'<p class="muted" style="font-size:0.85rem">Toque para revelar a resposta</p>')
    +'</div>'
   +'</div>'
   +(revVerso
     ?'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">'
      +'<button class="btn sec" type="button" data-action="avaliar" data-nivel="nao" style="border-color:var(--terracota)">Não Lembrei</button>'
      +'<button class="btn sec" type="button" data-action="avaliar" data-nivel="dificil" style="border-color:var(--ambar)">Difícil</button>'
      +'<button class="btn sec" type="button" data-action="avaliar" data-nivel="intermediario">Médio</button>'
      +'<button class="btn" type="button" data-action="avaliar" data-nivel="facil">Fácil ✓</button>'
     +'</div>'
     :'<div style="text-align:center"><button class="btn" type="button" data-action="virar">Revelar Resposta</button></div>');
 }

 return '<h1>Revisão Espaçada (SRS)</h1>'
  +'<p class="muted">Memorização de longo prazo com base no algoritmo de repetição espaçada.</p>'
  +corpo;
}

function viewBiblioteca(){
 return '<h1>Biblioteca & Glossário</h1>'
  +'<p class="muted">Dicionário de termos psicológicos e fontes do Caderno de Pesquisa.</p>'
  +'<input id="busca" class="campo" type="search" placeholder="Filtrar por conceito (ex.: Neuroplasticidade, Reforço)...">'
  +'<div id="lista-glos">'+listaGlossario('')+'</div>'
  +'<h2>Fontes Bibliográficas Oficiais (R01–R19)</h2>'
  +FONTES_CAP.map(f=>'<div class="card" style="padding:14px;margin:8px 0">'
    +'<strong>['+esc(f.c)+']</strong> '+esc(f.t)
    +'<br><a href="'+esc(f.u)+'" target="_blank" rel="noopener noreferrer" style="font-size:0.85rem;word-break:break-all">'+esc(f.u)+'</a>'
   +'</div>').join('');
}

function listaGlossario(q){
 const t=String(q||'').trim().toLowerCase();
 const itens=GLOSSARIO.filter(g=>!t||g.termo.toLowerCase().includes(t)||g.simples.toLowerCase().includes(t));
 if(!itens.length) return '<p class="muted">Nenhum termo encontrado.</p>';
 return itens.map(g=>'<details class="card" style="padding:14px;margin:8px 0"><summary><strong>'+esc(g.termo)+'</strong></summary>'
  +'<p style="margin:8px 0 4px 0"><strong>Definição:</strong> '+esc(g.simples)+'</p>'
  +(g.academico?'<p class="muted" style="margin:4px 0"><strong>Conceito Acadêmico:</strong> '+esc(g.academico)+'</p>':'')
  +(g.exemplo?'<p class="muted" style="margin:4px 0"><strong>Exemplo:</strong> '+esc(g.exemplo)+'</p>':'')
  +(g.aula&&AULAS[g.aula]?'<p style="margin:6px 0 0 0"><a href="#/aula/'+g.aula+'">Ver na aula: '+esc(AULAS[g.aula].titulo)+'</a></p>':'')
 +'</details>').join('');
}

function viewPerfil(){
 const p=estado.perfil||{};
 return '<h1>Perfil e Configurações</h1>'
  +'<form id="form-perfil" class="card">'
   +'<h3>Preferências de Estudo</h3>'
   +'<label>Como deseja ser chamado(a):<br><input class="campo" name="apelido" maxlength="40" value="'+esc(p.apelido||'')+'"></label>'
   +'<fieldset><legend>Nível de Conhecimento</legend><div class="opcoes">'+opcoesRadio('nivel',NIVEIS,p.nivel)+'</div></fieldset>'
   +'<fieldset><legend>Objetivo Principal</legend><div class="opcoes">'+opcoesRadio('objetivo',OBJETIVOS,p.objetivo)+'</div></fieldset>'
   +'<fieldset><legend>Meta Diária de Leitura</legend><div class="opcoes">'+opcoesRadio('tempo',TEMPOS,String(p.tempoDiario||20))+'</div></fieldset>'
   +'<h3>Aparência</h3>'
   +'<label>Tema da Interface:<br>'
    +'<select class="campo" name="tema">'
     +'<option value="claro"'+(estado.tema!=='escuro'?' selected':'')+'>Modo Claro (Linho Suave)</option>'
     +'<option value="escuro"'+(estado.tema==='escuro'?' selected':'')+'>Modo Escuro (Introspectivo)</option>'
    +'</select>'
   +'</label>'
   +'<label>Tamanho do Texto:<br>'
    +'<select class="campo" name="fonte">'
     +'<option value="normal"'+(estado.fonte!=='grande'?' selected':'')+'>Normal</option>'
     +'<option value="grande"'+(estado.fonte==='grande'?' selected':'')+'>Grande (Maior conforto)</option>'
    +'</select>'
   +'</label>'
   +'<button class="btn" type="submit">Salvar Alterações</button>'
  +'</form>'

  +'<div class="card">'
   +'<h3>Status do Professor Digital</h3>'
   +'<p class="muted">O PsicoBase conecta-se automaticamente ao seu servidor Python local (<code>api_server.py</code>).</p>'
   +'<div id="status-api-box" style="padding:10px 14px;border-radius:10px;background:var(--bg-subtil);margin-bottom:12px;font-size:0.9rem">Verificando servidor local...</div>'
   +'<button class="btn sec" type="button" data-action="testar-api">Testar Conexão com API</button>'
  +'</div>'

  +'<div class="card">'
   +'<h3>Backup dos Dados (Local-First)</h3>'
   +'<p class="muted">Seus dados e notas ficam exclusivamente neste dispositivo.</p>'
   +'<button class="btn sec" type="button" data-action="exportar">Exportar Backup (.json)</button>'
   +'<label style="display:block;margin-top:12px">Importar Backup:<br><input type="file" id="importar" accept="application/json" class="campo"></label>'
   +'<button class="btn sec" type="button" data-action="apagar" style="color:var(--terracota);margin-top:8px">Redefinir Dados</button>'
  +'</div>';
}

function viewBemVindo(){
 return '<div class="card" style="padding:32px 20px;text-align:center">'
  +'<div class="brand-icon" style="margin:0 auto 16px auto;width:48px;height:48px;font-size:1.6rem">Ψ</div>'
  +'<h1>Bem-vindo ao PsicoBase</h1>'
  +'<p style="font-size:1.1rem;max-width:540px;margin:0 auto 20px auto">'
   +'O espaço onde a mente humana é estudada com profundidade acadêmica, método e acolhimento.'
  +'</p>'
  +'<p class="muted">Seus dados ficam salvos localmente no navegador, sem necessidade de cadastro ou senhas.</p>'
  +'<button class="btn" type="button" data-action="iniciar-jornada" style="margin-top:16px">Começar Meus Estudos →</button>'
 +'</div>';
}

/* ==================== ROTEADOR ==================== */
function render(){
 encerrarSessao();
 const partes=rota().split('/').filter(Boolean);
 const r=partes[0]||'inicio';

 if(!estado.perfil && r!=='bem-vindo'){
  // Inicialização suave com perfil padrão se não existir
  estado.perfil = {nivel:'nunca', objetivo:'interesse', tempoDiario:20, preferencias:['leitura','questoes','flashcards'], apelido:'', criadoEm:dataISO()};
  salvar();
 }
 if(r!=='revisar'){ filaRev=null; }

 let html='';
 switch(r){
  case 'bem-vindo': html=viewBemVindo(); break;
  case 'inicio': html=viewInicio(); break;
  case 'aprender': html=viewAprender(); break;
  case 'modulo': html=viewModulo(partes[1]); break;
  case 'aula': html=viewAula(partes[1]); break;
  case 'revisar': html=viewRevisar(); break;
  case 'biblioteca': html=viewBiblioteca(); break;
  case 'perfil': html=viewPerfil(); break;
  default: html='<h1>Página não encontrada</h1><p><a href="#/inicio">Voltar ao Início</a></p>';
 }

 app.innerHTML=html;
 window.scrollTo(0, 0);

 // Atualizar itens ativos de navegação
 document.querySelectorAll('nav a').forEach(a=>{
  const ativo = a.dataset.nav===r || (r==='modulo'||r==='aula')&&a.dataset.nav==='aprender';
  if(ativo) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');
 });

 document.title = (r==='inicio'?'PsicoBase · Onde a Mente Humana é Estudada':'PsicoBase · '+r.charAt(0).toUpperCase()+r.slice(1));
 
 // Se estiver na tela de perfil, testar API
 if(r==='perfil'){
  testarConexaoAPI().then(ok => {
   const box = document.getElementById('status-api-box');
   if(box){
    box.innerHTML = ok 
     ? '🟢 <strong style="color:var(--salvia)">Servidor Local Ativo</strong> (http://127.0.0.1:8000) — Todas as rotas do Professor Digital prontas.' 
     : '🟡 <strong>Servidor Local Offline</strong> — Rodando com motor heurístico interno. (Execute <code>python api_server.py</code> para ativar a IA completa).';
   }
  });
 }
}

window.addEventListener('hashchange', render);

/* ==================== EVENT LISTENERS & AÇÕES ==================== */
document.addEventListener('click', e=>{
 const b=e.target.closest('[data-action]'); if(!b) return;
 switch(b.dataset.action){
  case 'iniciar-jornada': location.hash='#/inicio'; break;
  case 'virar': revVerso=true; render(); break;
  case 'avaliar': {
   const id=filaRev&&filaRev[0];
   if(id){ responderCartao(id, b.dataset.nivel); filaRev.shift(); revVerso=false; }
   render(); break;
  }
  case 'concluir': {
   const id=b.dataset.aula;
   if(estado.aulasConcluidas[id]) delete estado.aulasConcluidas[id];
   else estado.aulasConcluidas[id]={data:dataISO()};
   salvar();
   aviso(estado.aulasConcluidas[id]?'Aula concluída! ✓':'Conclusão desmarcada.');
   render(); break;
  }
  case 'salvar-nota': {
   const t=document.getElementById('nota');
   if(t){ estado.anotacoes[b.dataset.aula]=t.value.slice(0,5000); salvar(); aviso('Anotação salva!'); }
   break;
  }
  case 'exportar': {
   const blob=new Blob([JSON.stringify(estado,null,2)],{type:'application/json'});
   const url=URL.createObjectURL(blob);
   const a=document.createElement('a');
   a.href=url; a.download='psicobase-backup-'+dataISO()+'.json';
   document.body.appendChild(a); a.click(); a.remove();
   setTimeout(()=>URL.revokeObjectURL(url),1000);
   break;
  }
  case 'apagar': {
   if(confirm('Tem certeza de que deseja redefinir seus dados de progresso neste navegador?')){
    estado=estadoPadrao(); salvar(); aplicarVisual();
    location.hash='#/inicio'; render(); aviso('Dados redefinidos.');
   }
   break;
  }
  case 'testar-api': {
   testarConexaoAPI().then(ok => {
    aviso(ok ? 'API do Professor Digital conectada com sucesso!' : 'Servidor local não encontrado em http://127.0.0.1:8000');
    render();
   });
   break;
  }
  case 'pomo-toggle': togglePomodoro(); break;
  case 'pomo-reset': resetPomodoro(); break;
  case 'toggle-tema': {
   estado.tema = estado.tema==='escuro'?'claro':'escuro';
   salvar(); aplicarVisual(); break;
  }
 }
});

document.addEventListener('submit', async e=>{
 const f=e.target; e.preventDefault();
 
 if(f.id==='form-quiz'){
  const id=f.dataset.aula; const a=AULAS[id];
  const faltam=a.questoes.filter(q=>!f.querySelector('input[name="'+q.id+'"]:checked'));
  if(faltam.length){ aviso('Por favor, responda todas as questões (restam '+faltam.length+').'); return; }
  mostrarResultado(corrigirAula(id, f));
 }
 
 if(f.id==='form-tutor'){
  const aulaId=f.dataset.aula;
  const txt=f.querySelector('textarea').value.trim();
  if(txt.length<3){ aviso('Digite sua pergunta para o Professor Digital.'); return; }
  const respEl=document.getElementById('resp-tutor');
  respEl.innerHTML='<div class="card" style="font-size:0.92rem"><p class="muted">Consultando o conteúdo da aula e referências...</p></div>';
  
  try{
   const res = await perguntarProfessorDigital(aulaId, txt);
   const badgeOrigem = res.origem==='api_local'?'Servidor Local':'Tutor Integrado';
   const fontesHtml = (res.fontes&&res.fontes.length)
    ?'<div style="margin-top:10px;padding-top:8px;border-top:1px solid var(--borda-suave)"><span class="muted" style="font-size:0.8rem">Fontes: '+res.fontes.join('; ')+'</span></div>':'';
   
   respEl.innerHTML='<div class="card" style="border-left:4px solid var(--secundaria)">'
    +'<div style="display:flex;justify-content:space-between;margin-bottom:6px">'
     +'<strong style="color:var(--primaria)">Professor Digital</strong>'
     +'<span class="tag">'+badgeOrigem+'</span>'
    +'</div>'
    +'<p style="white-space:pre-wrap;margin:0">'+esc(res.resposta)+'</p>'
    +fontesHtml
   +'</div>';
  }catch(err){
   respEl.innerHTML='<div class="res erro"><p>Não foi possível obter resposta no momento.</p></div>';
  }
 }
 
 if(f.id==='form-perfil'){
  const fd=new FormData(f);
  estado.perfil=Object.assign({}, estado.perfil, {
   apelido: String(fd.get('apelido')||'').trim().slice(0,40),
   nivel: String(fd.get('nivel')||'nunca'),
   objetivo: String(fd.get('objetivo')||'interesse'),
   tempoDiario: Number(fd.get('tempo')||20)
  });
  estado.tema=fd.get('tema')==='escuro'?'escuro':'claro';
  estado.fonte=fd.get('fonte')==='grande'?'grande':'normal';
  salvar(); aplicarVisual(); aviso('Configurações salvas!'); render();
 }
});

document.addEventListener('input', e=>{
 if(e.target.id==='busca'){
  const l=document.getElementById('lista-glos');
  if(l) l.innerHTML=listaGlossario(e.target.value);
 }
});

document.addEventListener('change', e=>{
 if(e.target.id==='importar'){
  const arq=e.target.files[0]; if(!arq) return;
  const leitor=new FileReader();
  leitor.onload=()=>{
   try{
    const obj=JSON.parse(leitor.result);
    if(obj && typeof obj==='object'){
     estado=Object.assign(estadoPadrao(), obj);
     garantirTodos(); salvar(); aplicarVisual();
     aviso('Backup importado com sucesso!');
     location.hash='#/inicio'; render();
    }
   }catch(err){ aviso('Arquivo de backup inválido.'); }
  };
  leitor.readAsText(arq);
 }
});

/* ==================== INICIALIZAÇÃO ==================== */
aplicarVisual();
atualizarPomoUI();
render();
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#4A1525">
<meta name="description" content="PsicoBase - Onde a mente humana é estudada com profundidade, método e acolhimento.">
<title>PsicoBase · Onde a Mente Humana é Estudada</title>

<!-- Tipografia: Lora (Editorial Clássico) + Plus Jakarta Sans (Ergonomia Digital) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
/*__CSS_PLACEHOLDER__*/
</style>
</head>
<body>

<!-- Notificações Toast -->
<div id="aviso" class="toast" role="status" aria-live="polite" hidden></div>

<!-- Cabeçalho Superior Mobile & Tablet -->
<header class="app-header">
  <div class="header-wrap">
    <a href="#/inicio" class="brand-link">
      <div class="brand-icon">Ψ</div>
      <span>PsicoBase</span>
    </a>
    <div class="header-actions">
      <div class="pomo-widget">
        <span class="pomo-pulse"></span>
        <span class="pomo-tempo">25:00</span>
        <button class="pomo-btn pomo-play-btn" data-action="pomo-toggle" aria-label="Iniciar Pomodoro">▶</button>
        <button class="pomo-btn" data-action="pomo-reset" aria-label="Resetar Pomodoro">↺</button>
      </div>
      <button class="pomo-btn" data-action="toggle-tema" aria-label="Alternar Tema" style="font-size:1.1rem;padding:4px 8px">🌓</button>
    </div>
  </div>
</header>

<!-- Navegação Principal (Lateral no Desktop, Inferior no Mobile) -->
<nav class="inferior" id="nav" aria-label="Navegação principal">
  <a href="#/inicio" class="nav-brand-desktop">
    <div class="brand-icon">Ψ</div>
    <span>PsicoBase</span>
  </a>
  <a href="#/inicio" data-nav="inicio">
    <span style="font-size:1.1rem">🏠</span>
    <span>Início</span>
  </a>
  <a href="#/aprender" data-nav="aprender">
    <span style="font-size:1.1rem">📚</span>
    <span>Aprender</span>
  </a>
  <a href="#/revisar" data-nav="revisar">
    <span style="font-size:1.1rem">🗂️</span>
    <span>Revisar</span>
  </a>
  <a href="#/biblioteca" data-nav="biblioteca">
    <span style="font-size:1.1rem">📖</span>
    <span>Biblioteca</span>
  </a>
  <a href="#/perfil" data-nav="perfil">
    <span style="font-size:1.1rem">⚙️</span>
    <span>Perfil</span>
  </a>
</nav>

<!-- Conteúdo Principal -->
<main id="app" class="container" tabindex="-1"></main>

<script>
(()=>{
'use strict';

/* ==================== DADOS CURRICULARES (47 AULAS E GLOSSÁRIO) ==================== */
/*__DATA_PLACEHOLDER__*/

/*__JS_PLACEHOLDER__*/
})();
</script>
</body>
</html>
"""

final_html = HTML_TEMPLATE.replace("/*__CSS_PLACEHOLDER__*/", CSS_CODE).replace("/*__DATA_PLACEHOLDER__*/", curriculum_data).replace("/*__JS_PLACEHOLDER__*/", JS_FRAMEWORK)

# Gravar os arquivos de saída
with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
    f.write(final_html)

with open(OUTPUT_PSICO, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Arquivos index.html e PsicoBase.html gerados com sucesso com UTF-8 estrito!")

