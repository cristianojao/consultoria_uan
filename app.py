import streamlit as st

st.set_page_config(
    page_title="Nutricionista RT | Consultoria UAN",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #f7fffc 0%, #ffffff 48%, #f5fbf8 100%);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 42px 34px;
        border-radius: 22px;
        background: linear-gradient(135deg, #0d6b5b, #168b73);
        color: white;
        box-shadow: 0 12px 35px rgba(13, 107, 91, .18);
        margin-bottom: 28px;
    }

    .hero-kicker {
        font-size: 0.95rem;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
        opacity: .9;
        margin-bottom: 10px;
    }

    .hero h1 {
        font-size: clamp(2rem, 5vw, 3.5rem);
        line-height: 1.08;
        margin: 0 0 14px 0;
        color: white;
    }

    .hero p {
        font-size: 1.12rem;
        line-height: 1.65;
        max-width: 850px;
        margin-bottom: 0;
    }

    .section-title {
        color: #0d6b5b;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 34px 0 8px;
    }

    .section-subtitle {
        color: #53635e;
        font-size: 1rem;
        margin-bottom: 20px;
    }

    .card {
        background: white;
        border: 1px solid #dcece6;
        border-radius: 18px;
        padding: 22px;
        height: 100%;
        box-shadow: 0 7px 22px rgba(20, 75, 63, .07);
    }

    .card h3 {
        color: #0d6b5b;
        margin-top: 0;
        font-size: 1.15rem;
    }

    .service {
        padding: 10px 0;
        color: #33423e;
        border-bottom: 1px solid #edf3f1;
    }

    .service:last-child {
        border-bottom: 0;
    }

    .check {
        color: #0d806b;
        font-weight: 800;
        margin-right: 7px;
    }

    .audience {
        display: inline-block;
        background: #e9f7f2;
        color: #0d6b5b;
        padding: 10px 15px;
        border-radius: 999px;
        margin: 5px 5px 5px 0;
        font-weight: 600;
    }

    .plans {
        text-align: center;
        background: #f0faf6;
        border: 1px solid #cfe9df;
        border-radius: 18px;
        padding: 24px 18px;
        font-weight: 800;
        color: #0d6b5b;
        font-size: 1.05rem;
    }

    .cta {
        margin-top: 35px;
        padding: 34px;
        border-radius: 22px;
        background: #103f37;
        color: white;
        text-align: center;
    }

    .cta h2 {
        color: white;
        margin-top: 0;
    }

    .cta p {
        color: #e3f3ee;
    }

    .footer {
        text-align: center;
        color: #6b7b76;
        font-size: .9rem;
        padding-top: 30px;
    }

    a.whatsapp {
        display: inline-block;
        text-decoration: none;
        background: #25D366;
        color: white !important;
        padding: 13px 22px;
        border-radius: 12px;
        font-weight: 800;
        margin-top: 8px;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 30px 22px;
        }
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-kicker">🥗 Nutrição em Alimentação Coletiva</div>
    <h1>Nutricionista Responsável Técnica (RT)</h1>
    <p>
        <strong>Consultoria UAN para empresas e estabelecimentos de alimentação.</strong><br>
        Responsabilidade Técnica, organização, segurança alimentar e adequação às Boas Práticas.
    </p>
</div>
""", unsafe_allow_html=True)

# Intro
st.markdown('<div class="section-title">🏢 Consultoria para Empresas e Estabelecimentos de Alimentação</div>', unsafe_allow_html=True)
st.write(
    "Seu estabelecimento precisa de Responsabilidade Técnica, organização, segurança alimentar "
    "e adequação às Boas Práticas? Ofereço serviços de Nutrição em Alimentação Coletiva (UAN) "
    "para empresas e estabelecimentos de alimentação."
)

# Services
st.markdown('<div class="section-title">✅ Serviços</div>', unsafe_allow_html=True)

services = [
    "Responsabilidade Técnica (RT)",
    "Consultoria em UAN",
    "Adequação às Boas Práticas e exigências sanitárias",
    "Manual de Boas Práticas",
    "Elaboração e implantação de POPs",
    "Treinamento de manipuladores de alimentos",
    "Elaboração e avaliação de cardápios",
    "Fichas técnicas de preparação",
    "Controle de desperdícios",
    "Controle de qualidade",
    "Auditorias e visitas técnicas",
    "Organização da documentação sanitária",
    "Acompanhamento e visitas periódicas",
]

cols = st.columns(3, gap="medium")
for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(
            f'<div class="card"><div class="service"><span class="check">🔹</span>{service}</div></div>',
            unsafe_allow_html=True,
        )

# Audience
st.markdown('<div class="section-title">🍽️ Atendimento para</div>', unsafe_allow_html=True)

audiences = [
    "Restaurantes", "Lanchonetes", "Padarias", "Cozinhas industriais",
    "Hotéis", "Escolas", "Empresas e instituições",
    "Outros estabelecimentos de alimentação"
]
st.markdown(
    "".join(f'<span class="audience">{x}</span>' for x in audiences),
    unsafe_allow_html=True
)

# Documentation
st.markdown('<div class="section-title">📋 Documentação e Adequação</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Elaboração, revisão e organização de:</div>', unsafe_allow_html=True)

docs = [
    "Manual de Boas Práticas",
    "POPs",
    "Registros e controles",
    "Documentação sanitária",
    "Procedimentos de higiene e segurança dos alimentos",
]

c1, c2 = st.columns(2, gap="large")
for i, item in enumerate(docs):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(
            f'<div class="card"><span class="check">✔</span>{item}</div>',
            unsafe_allow_html=True,
        )

# Plans
st.markdown('<div class="section-title">📆 Planos de Acompanhamento</div>', unsafe_allow_html=True)
st.write("Atendimento conforme a necessidade do estabelecimento:")

plan_cols = st.columns(4, gap="medium")
for col, plan in zip(plan_cols, ["Mensal", "Trimestral", "Semestral", "Anual"]):
    with col:
        st.markdown(f'<div class="plans">📅 {plan}</div>', unsafe_allow_html=True)

st.info("Consultoria, acompanhamento técnico e visitas periódicas.")

# Contact
st.markdown("""
<div class="cta">
    <h2>📲 Fale agora com uma Especialista</h2>
    <p>Agende uma avaliação do seu estabelecimento.</p>
    <p><strong>📞 Telefone/WhatsApp: (61) 99927-7063</strong></p>
    <a class="whatsapp" href="https://wa.me/5561999277063" target="_blank">
        💬 Chamar no WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">🥗 Consultoria UAN • Responsabilidade Técnica • Boas Práticas • Segurança dos Alimentos</div>',
    unsafe_allow_html=True,
)
