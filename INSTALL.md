# Guia de Instalação

## Pré-requisitos

- Python 3.11+
- Node.js 18+
- npm 9+
- Git

## 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd plataforma-biblica
```

## 2. Configurar o Backend (Django)

### 2.1. Ambiente Virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 2.2. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

### 2.3. Configurar Variáveis de Ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o `.env` conforme necessário. Para desenvolvimento local, os valores padrão funcionam.

### 2.4. Executar Migrações

```bash
python manage.py migrate
```

### 2.5. Criar Superusuário

```bash
python manage.py createsuperuser
```

### 2.6. Popular com Dados Iniciais (Opcional)

```bash
python manage.py shell < seed_data.py
```

### 2.7. Iniciar Servidor Django

```bash
python manage.py runserver
```

O backend estará disponível em `http://127.0.0.1:8000`.

## 3. Configurar o Frontend (Tailwind CSS)

### 3.1. Instalar Dependências Node

```bash
npm install
```

### 3.2. Compilar Tailwind CSS

```bash
npm run build
```

Para desenvolvimento com recarga automática:

```bash
npm run watch
```

### 3.3. Servir o Frontend (Modo Standalone)

```bash
npm run start
```

O frontend estará disponível em `http://127.0.0.1:3000`.

## 4. Acessar a Plataforma

- **Frontend standalone:** `http://127.0.0.1:3000`
- **Backend (Django):** `http://127.0.0.1:8000`
- **Painel Admin:** `http://127.0.0.1:8000/admin/`

## 5. Docker (Produção)

```bash
docker-compose up -d --build
```

A aplicação estará disponível em `http://localhost:8000`.

## 6. Variáveis de Ambiente

| Variável        | Descrição                  | Padrão            |
|-----------------|----------------------------|-------------------|
| `SECRET_KEY`    | Chave secreta do Django    | (gerada)          |
| `DEBUG`         | Modo debug                 | `True`            |
| `ALLOWED_HOSTS` | Hosts permitidos           | `127.0.0.1,localhost` |
| `LLM_API_KEY`   | API Key para IA (LangChain)| (vazio - usa fallback) |
| `LLM_MODEL`     | Modelo de IA               | `gpt-3.5-turbo`   |
