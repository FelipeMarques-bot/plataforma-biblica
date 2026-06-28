# Plataforma Bíblica Gamificada

Interface premium para estudo bíblico gamificado que transforma devocionais diários em caminhos de aprendizado progressivo, combinando a progressão viciante de apps de idiomas com a calma visual de apps de bem-estar.

## Stack

| Camada   | Tecnologias                                      |
|----------|--------------------------------------------------|
| Backend  | Python + Django 5.2                              |
| Frontend | HTML + Tailwind CSS v3 + Alpine.js               |
| IA       | LangChain + OpenAI (com fallback sem API)        |
| Banco    | SQLite (dev) / PostgreSQL (prod)                 |
| Tarefas  | Celery + Redis                                   |
| Infra    | Docker + Gunicorn                                |

## Funcionalidades

- **Dashboard** — Streak diário, gráfico de XP semanal, próxima ação recomendada
- **Mapa de Trilhas** — Caminho vertical com nós ativos/bloqueados estilo Duolingo
- **Tela de Lição** — Quiz com múltipla escolha, V/F, barra de progresso e feedback visual
- **Tutor IA** — Dicas contextuais com consumo de pontos (LangChain)
- **Chat Devocional** — Reflexão guiada com IA em ambiente sereno
- **Série Ouro** — Desafios avançados com baús e animações premium
- **Gamificação** — XP, streak, níveis, recompensas e medalhas
- **Autenticação** — Cadastro por faixa etária e nível de conhecimento

## Design

- **Paleta:** Deep Celestial Blue (#0B2046), Warm Off-White (#F9F9F7), Premium Gold (#D4AF37)
- **Tipografia:** Outfit (headings) + Plus Jakarta Sans (body)
- **Estilo:** Ethereal minimalism + editorial premium

## Instalação Rápida

```bash
# Backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend
npm install
npm run build
npm run start
```

Acesse `http://127.0.0.1:8000` para o backend ou `http://127.0.0.1:3000` para o frontend standalone.

## Docker (Produção)

```bash
docker-compose up -d --build
```

## Estrutura do Projeto

```
plataforma-biblica/
├── core/                 # Configurações Django
├── users/                # Autenticação e perfil
├── courses/              # Trilhas, lições, exercícios
├── gamification/         # XP, streak, desafios, baús
├── ia_engine/            # LangChain (dicas, explicações)
├── chat_devocional/      # Chat com IA
├── templates/            # Templates Django
├── static/               # CSS e JS compilados
├── src/                  # Código fonte do frontend
├── Dockerfile
├── docker-compose.yml
└── manage.py
```

## Licença

MIT — veja [LICENSE.txt](LICENSE.txt).
