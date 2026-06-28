PRD.md – Plataforma Estilo Duolingo para Atividades Bíblicas com IA
1. Visão Geral do Produto
Nome provisório: Plataforma Bíblica Gamificada

Objetivo:
Plataforma web, estilo Duolingo (sem copiar), para estudo bíblico com:

trilhas por faixa etária e nível de dificuldade,
desafios diários e sistema de pontos,
“baús bíblicos” (recompensas),
IA como tutor que consome pontos,
chat devocional e resumos de lições.
Stack principal:

Backend: Python + Django
IA: LangChain/LangGraph + API de LLM (inicialmente gratuita)
Banco: PostgreSQL
Tarefas assíncronas: Celery + RabbitMQ (para IA/chat se necessário)
Deploy: Docker em servidor online (cloud/VPS)
Frontend (MVP): Django templates + Bootstrap
2. Estrutura de Conteúdo
Faixa etária:

Crianças (7–12)
Adolescentes (13–17)
Adultos (18+)
Níveis:

Iniciante
Intermediário
Avançado
Tipos de atividade bíblica:

Múltipla escolha
Verdadeiro/Falso
Associação (versículo ↔ tema, personagem ↔ história)
Ordenação (histórias em ordem correta, partes de versículo)
Pequenos desafios diários
Gamificação:

Pontos (XP)
Streak diário
Baús/recompensas com conteúdo bíblico extra
IA de ajuda que consome pontos
3. Sprints (com Checklists)
Cada Sprint abaixo é pensada tanto para o desenvolvimento da aplicação quanto para o ciclo completo de projeto local → Git → GitHub → Docker em servidor.

Sprint 0 – Preparação de Ambiente, Pasta Local, Git e GitHub
Objetivo
Ter o projeto iniciado em uma pasta local, versionado com Git, vinculado ao GitHub, com estrutura mínima para Django e pronto para evoluir.

Checklist
0.1 Criar pasta local do projeto
[ ] Criar diretório local do projeto, por exemplo: biblia-duolingo/.
[ ] Abrir a pasta no VS Code (ou editor de preferência).
0.2 Iniciar Git no projeto
[ ] Inicializar repositório Git:
git init
[ ] Criar arquivo .gitignore com, no mínimo:
[ ] __pycache__/
[ ] *.pyc
[ ] .venv/ ou venv/
[ ] env/
[ ] *.sqlite3
[ ] *.env
[ ] staticfiles/
[ ] media/
[ ] Fazer primeiro commit vazio ou com README:
[ ] Criar README.md simples.
[ ] git add .
[ ] git commit -m "chore: inicializa projeto"
0.3 Criar repositório no GitHub e vincular
[ ] Criar repositório remoto no GitHub (nome sugerido: biblia-duolingo).
[ ] Adicionar remoto ao projeto local:
git remote add origin <URL_REMOTO>
[ ] Fazer primeiro push:
git push -u origin main (ou master, conforme o padrão do repo).
0.4 Estrutura inicial de Python e Django
[ ] Criar e ativar ambiente virtual local (se for usar localmente apenas para testes básicos):
Ex.: python -m venv .venv
[ ] Instalar Django:
pip install django
[ ] Criar requirements.txt com pelo menos:
[ ] Django
[ ] Criar projeto Django:
django-admin startproject core .
[ ] Rodar migrações locais para validar:
python manage.py migrate
[ ] Criar superuser (opcional nesse momento):
python manage.py createsuperuser
[ ] Commit das mudanças:
git add .
git commit -m "feat: cria projeto Django base"
Sprint 1 – Fundação do Sistema (Modelos Básicos + Auth + Estrutura de Lições)
Objetivo
Ter o Django com modelos para usuários, faixa etária, níveis, lições e exercícios, rodando localmente e pronto para ser containerizado.

Checklist
1.1 Apps Django principais
[ ] Criar app users:
[ ] configurar perfil/expansão de usuário (faixa etária, nível, XP, streak).
[ ] Criar app courses:
[ ] LicaoBiblica
[ ] Exercicio
[ ] ProgressoUsuario
[ ] Registrar apps em INSTALLED_APPS.
1.2 Modelos de faixa etária, níveis e progresso
[ ] Em users:

[ ] modelo UserProfile com:
[ ] relação OneToOne com User
[ ] faixa_etaria (choices: criança, adolescente, adulto)
[ ] nivel_atual (iniciante/intermediário/avançado)
[ ] xp_total (inteiro)
[ ] streak_atual (inteiro)
[ ] ultimo_dia_atividade (date)
[ ] Em courses:

[ ] modelo LicaoBiblica:
[ ] título
[ ] descrição
[ ] texto_base (trecho ou referência bíblica)
[ ] faixa_etaria
[ ] nível
[ ] ordem (posicionamento na trilha)
[ ] modelo Exercicio:
[ ] licao (FK para LicaoBiblica)
[ ] tipo (múltipla escolha, VF, associação, ordenação, etc – choices)
[ ] enunciado
[ ] dados (JSONField com alternativas, respostas corretas)
[ ] modelo ProgressoUsuario:
[ ] usuario (FK)
[ ] licao (FK)
[ ] concluida (bool)
[ ] data_conclusao
[ ] xp_ganho_sessao
[ ] Rodar python manage.py makemigrations e python manage.py migrate.

[ ] Commit:

git add .
git commit -m "feat: modelos base de usuário e lições"
1.3 Autenticação e fluxo inicial
[ ] Configurar URLs para:
[ ] tela de cadastro
[ ] tela de login
[ ] tela inicial do usuário (dashboard)
[ ] Após login, redirecionar para rota nomeada dashboard.
[ ] Criar view dashboard que mostra:
[ ] saudação com nome do usuário
[ ] faixa etária
[ ] nível atual
[ ] lista de lições disponíveis (simplificada)
[ ] Commit:
git add .
git commit -m "feat: fluxo inicial de autenticação e dashboard"
Sprint 2 – Gamificação: Pontos, Desafio Diário e Baús Bíblicos
Objetivo
Adicionar sistema de pontuação (XP), desafio diário e recompensas em forma de “baús bíblicos”.

Checklist
2.1 Sistema de Pontuação (XP)
[ ] Definir regras de XP:
[ ] XP por exercício correto
[ ] XP extra por lição concluída
[ ] XP de bônus por desafio diário
[ ] Atualizar UserProfile:
[ ] adicionar campo pontos_para_ajuda (separado de XP_total).
[ ] Ao finalizar uma lição:
[ ] atualizar XP do usuário
[ ] atualizar pontos_para_ajuda (se quiser usar uma fração do XP)
[ ] atualizar streak (dia de atividade).
2.2 Desafio diário
[ ] Criar modelo DesafioDiario:
[ ] data
[ ] descrição/resumo
[ ] relação com uma lição ou exercícios específicos
[ ] recompensa de pontos
[ ] Lógica:
[ ] selecionar desafio diário por faixa etária/nível
[ ] registrar que o usuário concluiu o desafio e recebeu pontos
[ ] Tela “Desafio Diário”:
[ ] mostrar desafio do dia
[ ] executar exercícios
[ ] mostrar resultado com XP extra
2.3 Baús bíblicos (recompensas)
[ ] Criar modelo Recompensa:
[ ] tipo (versículo, medalha, curiosidade)
[ ] descrição
[ ] critério (mínimo de lições, XP, streak etc.)
[ ] Criar modelo RecompensaUsuario:
[ ] FK para usuário
[ ] FK para recompensa
[ ] data de desbloqueio
[ ] Lógica:
[ ] após certas ações (ex: completar 3 lições), verificar se existe baú a ser aberto
[ ] Tela “Minhas Recompensas / Baús”:
[ ] listar baús abertos e pendentes
2.4 UI estilo “mapa de lições”
[ ] Criar layout do “mapa” de lições:
[ ] cards em sequência representando o progresso
[ ] ícone/cores diferentes para lições concluídas vs desbloqueadas vs bloqueadas
[ ] Commit:
git add .
git commit -m "feat: gamificação básica com XP, desafios e baús"
Sprint 3 – Integração de IA como Tutor (Dicas e Explicações que Consomem Pontos)
Objetivo
Permitir que o usuário peça ajuda à IA em exercícios/ lições, consumindo pontos de ajuda.

Checklist
3.1 Configuração de IA (LangChain/LangGraph)
[ ] Adicionar dependências em requirements.txt:
[ ] LangChain
[ ] Cliente da API de IA escolhida (ex: OpenAI, Groq etc.)
[ ] Definir variáveis de ambiente:
[ ] LLM_API_KEY
[ ] LLM_MODEL_NAME etc.
[ ] Criar módulo ia_engine:
[ ] função gerar_dica_exercicio(exercicio, resposta_usuario_opcional)
[ ] função explicar_licao(licao)
[ ] Incluir logs básicos:
[ ] registrar input/output da IA em log seguro (sem dados sensíveis do usuário).
3.2 Sistema de ajuda com consumo de pontos
[ ] Definir custo de pontos:
[ ] Dica curta: X pontos
[ ] Explicação da lição: Y pontos (maior)
[ ] Criar função utilitária:
[ ] verificar_e_debitar_pontos_para_ajuda(usuario, custo)
[ ] Se o usuário não tiver pontos suficientes:
[ ] exibir mensagem amigável (“Você precisa de mais pontos. Conclua lições para ganhar mais ajuda.”)
3.3 Interface de ajuda
[ ] Nas telas de exercício:
[ ] botão “Pedir dica”
[ ] indicação do custo em pontos
[ ] Nas telas de lição:
[ ] botão “Explicação da lição (IA)”
[ ] exibir explicação retornada pela IA
[ ] Commit:
git add .
git commit -m "feat: IA como tutor com consumo de pontos"
Sprint 4 – Chat Devocional e Sugestões de Estudo
Objetivo
Criar chat de apoio devocional/estudo usando IA, com sugestões de temas.

Checklist
4.1 Modelos e estrutura do chat devocional
[ ] Criar modelo SessaoDevocional:
[ ] usuario
[ ] tema
[ ] data_inicio
[ ] resumo
[ ] Criar modelo MensagemDevocional (opcional, se quiser histórico detalhado):
[ ] sessao (FK)
[ ] remetente (usuário ou IA)
[ ] texto
[ ] data_hora
4.2 IA para devocional
[ ] Função gerar_devocional(tema, idade, nivel):
[ ] texto breve + referência bíblica
[ ] Função sugerir_plano_estudo(tema, dias):
[ ] lista de passagens + breves objetivos
4.3 Interface do chat devocional
[ ] Tela com:
[ ] lista de temas (fé, esperança, família, oração, etc.)
[ ] botão “Devocional do dia”
[ ] campo de chat para perguntas sobre o tema da lição
[ ] Regras de uso (opcional):
[ ] limitar número de mensagens por dia
[ ] ou consumo de pontos especial para devocional avançado
[ ] Commit:
git add .
git commit -m "feat: chat devocional com IA"
Sprint 5 – Resumo de Lições (“Onde Parei”) com IA de Apoio
Objetivo
Mostrar ao usuário um painel de “onde parei” e resumos das últimas lições, possivelmente usando IA.

Checklist
5.1 Registro e resumo básico
[ ] Garantir que ProgressoUsuario possui:
[ ] data/hora de início
[ ] data/hora de conclusão
[ ] XP daquela sessão
[ ] Criar função que:
[ ] busca últimas N lições concluídas pelo usuário
[ ] monta um resumo simples (sem IA) com títulos e textos base
5.2 IA para resumo (opcional avançado)
[ ] Função resumir_historico(licoes_recentes):
[ ] chama LLM para gerar resumo em linguagem acessível
[ ] Mostrar na home:
[ ] “Você estudou recentemente: …”
[ ] “Sugestão de próximo passo: …”
5.3 Tela “Onde parei”
[ ] Mostrar:
[ ] última lição acessada
[ ] porcentagem de progresso na trilha
[ ] botão “Continuar”
[ ] resumo (com ou sem IA)
[ ] Commit:
git add .
git commit -m "feat: resumo de lições e tela 'onde parei'"
Sprint 6 – Docker e Deploy Online (Produção)
Objetivo
Empacotar tudo em Docker e rodar em servidor online (já que sua máquina não aguenta rodar tudo).

Checklist
6.1 Arquivos de Docker
[ ] Criar Dockerfile para o serviço web Django:
[ ] imagem base Python
[ ] instalar dependências do requirements.txt
[ ] copiar projeto para dentro do container
[ ] configurar comando padrão (gunicorn ou manage.py runserver para ambiente simples)
[ ] Criar docker-compose.yml com serviços:
[ ] web: aplicativo Django
[ ] db: PostgreSQL (imagem oficial)
[ ] rabbitmq: serviço de fila (para Celery, se já estiver em uso)
[ ] opcional: worker: Celery worker
6.2 Variáveis de ambiente para produção
[ ] Configurar .env (não versionado) com:
[ ] SECRET_KEY
[ ] DEBUG=False
[ ] ALLOWED_HOSTS
[ ] credenciais do PostgreSQL
[ ] chaves de API de IA
[ ] Ajustar settings.py para ler as variáveis do .env.
6.3 Servidor online (Cloud/VPS)
[ ] Criar servidor (ex: VPS ou serviço de container).
[ ] Instalar Docker e Docker Compose no servidor.
[ ] Clonar o repositório do GitHub no servidor:
git clone <URL_GITHUB>
[ ] Configurar .env no servidor.
[ ] Subir containers:
docker-compose up -d --build
[ ] Rodar migrações dentro do container:
docker-compose exec web python manage.py migrate
[ ] Criar superuser em produção:
docker-compose exec web python manage.py createsuperuser
[ ] Testar acesso via IP/domínio.
6.4 Ajustes finais
[ ] Configurar servidor web reverso (Nginx) se necessário:

[ ] encaminhar tráfego HTTPS para o container web
[ ] Garantir que:

[ ] as páginas de lições carregam
[ ] IA responde (se configurada)
[ ] pontos e desafios funcionam
[ ] Commit (ajustes de infra – sem .env):

git add Dockerfile docker-compose.yml
git commit -m "chore: configura Docker e deploy"
6. Critérios de Aceite do MVP
Usuário consegue:
[ ] criar conta, escolher faixa etária e nível,
[ ] acessar lições bíblicas com exercícios,
[ ] ganhar pontos e manter streak,
[ ] completar desafio diário,
[ ] abrir “baús bíblicos” (recompensas),
[ ] pedir ajuda à IA (dicas/explicações) consumindo pontos,
[ ] usar chat devocional com sugestões de estudo,
[ ] ver “onde parei” e resumo das lições recentes.
Sistema:
[ ] roda em servidor remoto com Docker,
[ ] utiliza PostgreSQL,
[ ] está versionado em Git e sincronizado com GitHub,
[ ] usa IA via API configurada em variáveis de ambiente.

7. Guia para a IA (opencode / VS Code) – Como usar este PRD
Esta seção é para agentes de IA que atuem no código deste projeto (por exemplo, opencode rodando via VS Code).

7.1. Fluxo geral da IA
Para cada tarefa deste PRD (itens [ ] nas Sprints), a IA deve:

Ler a Sprint correspondente no PRD.md e identificar o item exato.
Implementar a funcionalidade no código, seguindo:
estrutura de apps (users, courses, ia, etc.),
nomes de modelos, campos e relacionamentos descritos aqui.
Se mexer em modelos Django:
Executar:
python manage.py makemigrations
python manage.py migrate
Verificar se o servidor roda:
python manage.py runserver (checar se não há erros).
Atualizar este PRD.md:
Trocar o checkbox da tarefa concluída de [ ] para [x].
Versionar e publicar:
git add .
git commit -m "<mensagem curta e clara>"
git push
7.2. Ordem de execução recomendada
A IA deve seguir, salvo instruções específicas:

Sprint 0 – Git, GitHub, Django base.
Sprint 1 – Modelos principais + login + dashboard.
Sprint 2 – XP, streak, desafio diário, baús.
Sprint 3 – IA tutor (dicas/explicações gastando pontos).
Sprint 4 – Chat devocional.
Sprint 5 – Resumo de lições / “onde parei”.
Sprint 6 – Docker + deploy online.

8. Guia de Criação de Conteúdo Bíblico (Trilhas, Lições e Exercícios)
Esta seção define como criar o conteúdo pedagógico da plataforma (trilhas, lições, exercícios, desafios, devocionais), para que tanto humanos quanto a IA possam produzir e manter esse conteúdo de forma consistente.

8.1. Conceitos de conteúdo
Trilha: caminho temático de estudo (ex.: “Fundamentos da Bíblia”, “Evangelhos”, “Parábolas de Jesus”).
Lição: unidade de estudo dentro de uma trilha (ex.: “O que é a Bíblia?”, “Introdução aos Evangelhos”).
Exercício: atividade prática dentro de uma lição (múltipla escolha, VF, associação, ordenação).
Desafio diário: microlição curta, independente, focada em um tema ou versículo.
Devocional: conteúdo mais reflexivo, com texto + aplicação prática, gerado com apoio da IA.
8.2. Modelo pedagógico de uma Trilha
Para cada Trilha:

Campos básicos (já mapeados em modelos, mesmo que com outros nomes):

nome
descricao
faixa_etaria_alvo (criança/adolescente/adulto)
nivel (iniciante/intermediário/avançado)
ordem (posição na lista de trilhas)
Exemplos de Trilhas:

Crianças, Iniciante:
“Histórias da Criação”
“Histórias de Jesus”
Adolescentes, Iniciante:
“Quem é Jesus?”
“Amizade e fé”
Adultos, Iniciante:
“Panorama da Bíblia”
“Evangelhos em foco”
8.3. Estrutura padrão de uma Lição
Cada Lição Bíblica deve seguir um modelo simples e repetível:

Metadados

Título (ex.: “O que é a Bíblia?”)
Trilha (FK)
Faixa etária alvo
Nível (iniciante/intermediário/avançado)
Ordem na trilha
Texto base

Um trechinho bíblico ou conjunto de versículos:
Referência (ex.: 2Tm 3:16–17)
Texto (ou apenas a referência, se o texto for exibido via tradução configurada)
Objetivo da lição (1–2 frases)

Exemplo: “Entender que a Bíblia é inspirada por Deus e útil para a nossa vida.”
Exercícios (3 a 7 por lição, dependendo da faixa etária)

Exercício 1: compreensão do texto (múltipla escolha).
Exercício 2: verdadeiro/falso sobre o significado.
Exercício 3: aplicação prática simples (“qual atitude combina melhor com o texto?”).
Exercícios extras (se nível maior): ordenação, associação, interpretação mais profunda.
Resumo final (texto curto)

2–3 frases reforçando o ponto principal.
Sugestão de devocional (opcional)

Pequeno desafio de aplicação para o dia (pode ser gerado por IA).
8.4. Tipos de Exercícios e como representar
Tipo 1 – Múltipla Escolha (MULTIPLA_ESCOLHA)

Campos mínimos no dados (JSON):
alternativas: lista de strings
indice_correto: índice da alternativa correta
Exemplo de JSON no campo dados:

json
Copiar

{
  "alternativas": [
    "Um conjunto de histórias inventadas",
    "A Palavra de Deus inspirada",
    "Um livro de regras humanas",
    "Um manual de filosofia antiga"
  ],
  "indice_correto": 1
}
Tipo 2 – Verdadeiro/Falso (VERDADEIRO_FALSO)

dados:
afirmativa: texto
correta: boolean
json
Copiar

{
  "afirmativa": "Toda a Escritura é inspirada por Deus.",
  "correta": true
}
Tipo 3 – Associação (ASSOCIACAO)

dados:
pares: lista de objetos { "esquerda": "...", "direita_correta": "..." }
json
Copiar

{
  "pares": [
    { "esquerda": "Gênesis", "direita_correta": "Criação" },
    { "esquerda": "Evangelhos", "direita_correta": "Vida de Jesus" }
  ]
}
Tipo 4 – Ordenação (ORDENACAO)

dados:
itens: lista de strings na ordem correta
json
Copiar

{
  "itens": [
    "Criação",
    "Queda",
    "Redenção",
    "Nova Criação"
  ]
}
A interface mostra embaralhado; o backend corrige comparando com a ordem.

8.5. Processo para criação de conteúdo (manual + IA)
Passo 1 – Definir trilha e público

Escolher:
faixa etária,
nível,
tema bíblico.
Registrar a Trilha na base (via Django Admin ou painel).
Passo 2 – Planejar lições

Para cada trilha, definir de 5 a 10 lições, com:
título,
objetivo,
referência bíblica.
Passo 3 – Criar exercícios

Para cada lição:
criar pelo menos:
1 exercício de compreensão do texto,
1–2 exercícios de interpretação/aplicação,
exercícios extras conforme o nível (mais reflexão para avançado).
Passo 4 – Usar IA como apoio de criação (admin)

A IA pode ajudar na criação de conteúdo, mas o admin sempre revisa:

Gerar propostas de perguntas com base:
no texto bíblico,
no objetivo da lição.
Gerar alternativas plausíveis (inclusive erradas, mas críveis).
Gerar resumos e devocionais curtos.
A IA nunca publica diretamente:
os textos são revistos e ajustados pelo admin antes de salvar.

8.6. Sprints de Conteúdo (para a IA e para você)
Para facilitar, o conteúdo também terá suas próprias mini-sprints:

Sprint C1 – Trilhas iniciais
[x] Definir e cadastrar pelo menos 2 trilhas para crianças (iniciante).
[x] Definir e cadastrar pelo menos 2 trilhas para adolescentes (iniciante).
[x] Definir e cadastrar pelo menos 2 trilhas para adultos (iniciante).
Sprint C2 – Lição base por trilha
Para cada trilha criada em C1:

[x] Criar 1 lição introdutória com:
[x] título e objetivo claros,
[x] texto bíblico base,
[x] resumo final simples.
Sprint C3 – Exercícios mínimos por lição
Para cada lição introdutória:

[x] Criar pelo menos 3 exercícios:
[x] 1 múltipla escolha sobre o texto,
[x] 1 verdadeiro/falso sobre o sentido,
[x] 1 de aplicação prática.
Sprint C4 – Desafios diários
[x] Criar um conjunto inicial de 7 desafios diários (um por dia da semana), com:
[x] versículo curto,
[x] pequena pergunta/reflexão,
[x] recompensa de pontos definida.
[x] Seed no banco com 7 dias completos.
Sprint C5 – Devocionais sugeridos
[ ] Definir 3 temas de devocional por faixa etária (ex.: fé, gratidão, perdão).
[ ] Para cada tema, criar:
[ ] 1 texto devocional curto,
[ ] 1 sugestão de oração,
[ ] 1 desafio prático para o dia.
8.7. Guia para a IA na criação de conteúdo
Quando a IA for usada para ajudar a criar lições e exercícios, deve seguir:

Sempre partir de:
uma referência bíblica,
um objetivo da lição,
uma faixa etária e nível.
Propor:
perguntas claras,
alternativas respeitosas e bíblicas,
aplicações práticas realistas.
Entregar o resultado em formato fácil de copiar para o modelo Django:
texto da pergunta,
JSON para o campo dados conforme os exemplos desta seção.
Nunca substituir a revisão humana:

10. Diretrizes Teológicas – Enfoque Reformado
Todo o conteúdo desta plataforma (lições, exercícios, devocionais, respostas da IA) deve ser coerente com a teologia reformada histórica, tal como expressa em confissões clássicas (por exemplo: CFW, Cânones de Dort, Catecismos de Heidelberg/Westminster), sem citar necessariamente documentos técnicos ao usuário final.

10.1. Princípios doutrinários centrais
A plataforma deve refletir, de forma simples e pastoral, os seguintes eixos:

Sola Scriptura

A Bíblia é a Palavra de Deus, única regra infalível de fé e prática.
Todo ensino deve partir da Escritura, respeitando contexto e intenção do texto.
Sola Fide / Sola Gratia / Solus Christus

A salvação é somente pela graça, mediante a fé, em Cristo somente.
Lição nenhuma pode transmitir a ideia de:
méritos humanos como base para salvação,
“barganhas” com Deus,
ou salvação por obras.
Sola Deo Gloria

Deus é o centro da história da redenção; o alvo da vida cristã é a glória de Deus.
Aplicações práticas sempre apontam para:
gratidão,
obediência,
santidade,
serviço ao próximo em resposta ao que Deus fez.
Soberania de Deus e depravação humana

Deus é soberano sobre a criação, história e salvação.
O ser humano é pecador por natureza e precisa da graça regeneradora de Deus.
Exercícios e devocionais devem evitar:
visão excessivamente otimista da natureza humana,
linguagem de “você consegue sozinho se se esforçar bastante”.
Cristo no centro da Escritura

A Bíblia é uma história única de criação, queda, redenção e consumação, com Cristo como centro.
Sempre que conveniente, lições devem:
mostrar como o texto aponta para Cristo,
relacionar promessas, tipos e profecias ao cumprimento em Jesus.
10.2. Diretrizes para Lições (por faixa etária) em teologia reformada
As lições definidas nas seções de conteúdo (Crianças, Adolescentes, Adultos) devem ser interpretadas e expandidas à luz destes pontos:

Crianças

Enfatizar:
bondade de Deus Criador,
pecado explicado em linguagem simples,
necessidade de Jesus como Salvador e Amigo,
obediência e gratidão.
Evitar:
moralismo puro (“seja bonzinho e Deus vai gostar de você”) sem Evangelho,
linguagem que sugira que Deus ama só quando a criança acerta.
Adolescentes

Enfatizar:
identidade em Cristo,
graça e arrependimento verdadeiro,
santidade em meio a tentações reais,
soberania de Deus em meio às dúvidas.
Evitar:
teologia da prosperidade,
relativismo (“todas as crenças são iguais”),
mensagens meramente motivacionais sem base bíblica.
Adultos

Enfatizar:
panorama da história da redenção,
doutrinas centrais (Deus, Cristo, Espírito Santo, Escritura, Igreja, salvação),
vida cristã como resposta de gratidão à graça,
vocação e serviço no mundo.
Evitar:
foco em técnicas de autoajuda sem cruz,
promessas de solução fácil para todos os problemas terrenos.
10.3. Diretrizes para Devocionais
Os devocionais descritos nas lições (C1.1, C1.2, A1.1, A1.2, D1.1, D1.2 etc.) e os devocionais que a IA vier a gerar devem:

Ser centrados em Deus

Falar primeiramente de quem Deus é e do que Ele fez em Cristo,
Depois, aplicar à vida do leitor.
Evitar promessas não bíblicas

Não prometer cura, prosperidade financeira, sucesso ou restauração automática de circunstâncias sem base clara no texto.
Falar de pecado e graça com equilíbrio

Reconhecer o pecado e chamar ao arrependimento,
Sempre apresentar o perdão em Cristo, sem deixar o usuário em desespero ou culpa sem Evangelho.
Apontar para os meios de graça

Incentivar:
leitura da Palavra,
oração,
comunhão na igreja local (mesmo que citada de forma geral),
obediência ao que já foi revelado.
Ser pastorais, não dogmáticos demais para a faixa etária

Para crianças:
linguagem simples, ilustrações,
foco em quem Deus é e no amor de Cristo.
Para adolescentes:
conectar com dilemas reais (identidade, medo, pressão).
Para adultos:
conexões com trabalho, família, sofrimento, vocação.
10.4. Diretrizes específicas para o Chat Devocional (IA)
Quando o chat devocional responder a dúvidas ou sugerir estudos:

Base na Escritura

Sempre que possível, citar referências bíblicas adequadas ao tema.
Explicar o texto respeitando contexto e sentido original.
Tom reformado

Reconhecer a soberania de Deus,
enfatizar graça e Cristo como centro,
não ensinar ideias incompatíveis com confissões reformadas clássicas (por exemplo:
negação da divindade de Cristo,
salvação por obras,
universalismo simplista – “todo mundo será salvo de qualquer jeito”).
Limites pastorais

Em assuntos sensíveis (depressão profunda, abuso, risco de vida, decisões médicas complexas), o chat deve:
incentivar a busca de ajuda pastoral/pessoal qualificada,
não se apresentar como substituto de aconselhamento profissional ou pastoral.
Respeito a diferenças dentro do espectro reformado

Em temas de divergência intrarreformada (ex.: detalhes de escatologia, modo de governo eclesiástico), responder:
com humildade,
apresentando, se necessário, mais de uma posição dentro do campo reformado,
sem atacar outras tradições cristãs.
10.5. Guia para a IA – Teologia Reformada na prática
Sempre que a IA:

gerar lições,
criar exercícios,
escrever devocionais,
ou responder no chat devocional,
deve seguir este fluxo mental:

Pergunta interna:
“O que este texto bíblico ensina sobre Deus, sobre o ser humano, sobre Cristo e sobre a salvação?”

Resposta centrada na graça:

Destacar o que Deus fez primeiro,
depois falar da nossa resposta em fé, arrependimento e obediência.
Checagens rápidas de erro:

Não sugerir que:
“se você fizer X, Deus é obrigado a fazer Y”,
“basta pensar positivo e tudo vai dar certo”,
“você é bom por natureza e só precisa se esforçar um pouco mais”.
Em vez disso, usar linguagem como:
“Deus, em sua graça, nos chama a…”
“Confiamos na obra de Cristo e, por isso, queremos…”
“Mesmo em meio à luta contra o pecado, há perdão e nova vida em Cristo.”
Sempre que estiver em dúvida de doutrina:

a IA deve ficar mais conservadora, evitando afirmar com certeza algo que possa contrariar o padrão reformado,
pode sugerir:
“Essa é uma questão teológica em que cristãos fiéis podem ter nuances diferentes; procure conversar com seus líderes espirituais.”

11. Expansão de Conteúdo – Níveis Intermediário e Avançado (Teologia Reformada)
Para aumentar o tempo de estudo (~3 horas por faixa etária), cada faixa ganhará mais trilhas e lições nos níveis Intermediário e Avançado, seguindo:

duração média por lição: 10–15 minutos,
6–10 lições por trilha,
foco em:
doutrina básica aplicada (Intermediário),
doutrina mais estruturada + prática (Avançado).
Todas essas trilhas seguem as Diretrizes Teológicas Reformadas (seção 10).

11.1. Crianças (7–12)
Nível Intermediário – Trilha C3: Heróis da Fé (olhando para Cristo)
Visão geral:
Apresentar personagens bíblicos como exemplos de fé, deixando claro que Cristo é o verdadeiro herói, e que esses personagens apontam para Ele.

Trilha C3 – Lição sugerida (exemplos):

Lição C3.1 – Noé confiou em Deus em meio ao caos

Referência: Gênesis 6–9 (recorte adaptado)
Objetivo: Mostrar a obediência de Noé em meio à incredulidade, e que o arco-íris lembra a fidelidade de Deus.
Ênfase reformada:
Deus julga o pecado, mas preserva um povo pela Sua graça.
A arca é um tipo de Cristo (lugar de salvação).
Exercícios:
Múltipla escolha (por que Noé construiu a arca?),
Verdadeiro/Falso (Deus esquece das promessas?),
Aplicação simples (como obedecer a Deus mesmo quando os outros zombam).
Lição C3.2 – Abraão confiou na promessa

Referência: Gênesis 12; 15
Objetivo: Falar de fé e promessa, sem transformar em “fé para conseguir coisas”.
Ênfase reformada:
Deus chama, Deus promete, Deus cumpre.
A fé é resposta à graça, não moeda de troca.
Exercícios e devocional: fé como confiança no caráter de Deus.
Lição C3.3 – Davi, um rei imperfeito que apontava para um Rei perfeito

Referência: 1Sm 16; 2Sm 7
Objetivo: Mostrar Davi como homem segundo o coração de Deus, mas ainda pecador.
Ênfase reformada:
Davi não é herói absoluto, Cristo é o Rei perfeito prometido.
Exercícios:
Associação (Davi ↔ promessa de um trono eterno),
V/F sobre Deus usar pecadores arrependidos.
(A trilha pode ter até C3.6 ou C3.8, incluindo Ester, Daniel, José, etc., sempre apontando para Cristo.)

Nível Avançado – Trilha C4: Parábolas de Jesus
Visão geral:
Trabalhar parábolas com linguagem acessível, sempre ressaltando graça, Reino de Deus e chamado ao arrependimento.

Exemplos de lições:

Lição C4.1 – Ovelha perdida

Referência: Lucas 15:1–7
Ênfase:
Jesus procura o perdido,
a alegria do céu com o arrependimento.
Lição C4.2 – Filho pródigo (parte 1 – o filho que foi embora)

Lucas 15:11–24
Ênfase:
pecado e retorno,
Pai que recebe com graça.
Lição C4.3 – Filho pródigo (parte 2 – o filho que ficou)

Lucas 15:25–32
Ênfase:
pecado também na autojustiça,
necessidade de graça para “bonzinhos”.
Lição C4.4 – A casa na rocha

Mateus 7:24–27
Ênfase:
ouvir + praticar a Palavra,
Cristo como fundamento seguro.
Cada lição com 3–5 exercícios e devocional que ressalte:

graça de Deus,
importância de ouvir e crer na Palavra,
resposta em obediência, não para ganhar amor, mas porque já fomos amados.
11.2. Adolescentes (13–17)
Nível Intermediário – Trilha A3: Vivendo a Fé na Escola e em Casa
Visão geral:
Aplicar doutrina reformada à vida diária (identidade, pecado, graça, santidade em contexto real).

Lições exemplo:

Lição A3.1 – Identidade em Cristo, não na opinião dos outros

Referência: Efésios 1:3–7; 1Pe 2:9
Ênfase:
escolhido, amado, perdoado em Cristo,
contraponto à busca desesperada por aprovação.
Exercícios:
MC sobre “quem sou em Cristo?”
V/F sobre “meu valor vem do desempenho”.
Lição A3.2 – Luta contra o pecado (não perfeição, mas arrependimento)

Referência: Romanos 7:14–25; 1Jo 1:8–9
Ênfase:
crente ainda luta com o pecado,
importância de confissão e confiança na graça.
Exercícios:
interpretação curta,
aplicação prática: o que é arrependimento verdadeiro.
Lição A3.3 – Graça que educa

Referência: Tito 2:11–14
Ênfase:
graça não é desculpa para pecar,
graça nos ensina a dizer “não” à impiedade.
Devocional: graça educadora na rotina (internet, relacionamentos, escola).
Lição A3.4 – Fé viva em meio à pressão

Referência: Daniel 3 (resumo de Sadraque, Mesaque e Abede-Nego)
Ênfase:
fidelidade a Deus acima de aprovação humana,
Deus é capaz de livrar, mas mesmo que não, Ele continua sendo Deus.
Nível Avançado – Trilha A4: Discipulado e Chamado
Visão geral:
Mostrar que seguir Cristo é caminhar em discipulado, serviço e vocação, com visão reformada de mundo (Cristo como Senhor de todas as áreas).

Lições exemplo:

Lição A4.1 – Ser discípulo de Cristo

Referência: Lucas 9:23–25
Ênfase:
negar-se a si mesmo, tomar a cruz,
custo e alegria do discipulado.
Lição A4.2 – Chamado para toda a vida (não só “coisas de igreja”)

Referência: Colossenses 3:23–24; 1Co 10:31
Ênfase:
tudo para a glória de Deus,
trabalho, estudo, família como campos de serviço.
Lição A4.3 – Igreja: corpo de Cristo

Referência: Efésios 4:11–16
Ênfase:
importância da comunidade de fé,
dons espirituais para edificar, não para autoexaltação.
Lição A4.4 – Esperança futura

Referência: Apocalipse 21:1–5
Ênfase:
nova criação,
esperança que sustenta em meio ao sofrimento agora.
Cada lição com devocionais que:

conectam doutrina e vida,
evitam triunfalismo,
chamam à perseverança em Cristo.
11.3. Adultos (18+)
Nível Intermediário – Trilha D3: Vida Cristã no Dia a Dia
Visão geral:
Aplicar graça, fé, soberania de Deus em áreas práticas: trabalho, família, finanças, sofrimento.

Lições exemplo:

Lição D3.1 – Trabalhando para a glória de Deus

Referência: Colossenses 3:23–24
Ênfase:
vocação e trabalho como serviço a Deus,
dignidade do trabalho “comum”.
Lição D3.2 – Família e graça

Referência: Efésios 5:21–6:4 (com cuidado pastoral)
Ênfase:
mutualidade, amor sacrificial, cuidado,
evitar legalismo ou distorções autoritárias.
Lição D3.3 – Lidando com ansiedade e sofrimento

Referência: Filipenses 4:6–7; Romanos 8:28–39
Ênfase:
confiança na soberania e amor de Deus,
lembrar que “todas as coisas cooperam” na perspectiva eterna.
Lição D3.4 – Comunhão e igreja local

Referência: Hebreus 10:24–25; Atos 2:42–47
Ênfase:
importância dos meios de graça,
vida em comunidade, não fé isolada.
Nível Avançado – Trilha D4: Doutrinas Centrais e Prática
Visão geral:
Introduzir doutrinas fundamentais de forma acessível e aplicada, sempre com foco na vida cristã e não em debate acadêmico vazio.

Sugestão de sequência:

Lição D4.1 – Quem é Deus? (Atributos e caráter)

Referência: Êxodo 34:6–7; Salmo 103
Ênfase:
bondade, justiça, santidade, amor, imutabilidade.
Lição D4.2 – Pecado e depravação humana

Referência: Romanos 3:9–26
Ênfase:
ninguém é justo por si mesmo,
necessidade total da graça.
Lição D4.3 – Justificação pela fé

Referência: Romanos 5:1–2; Gálatas 2:16
Ênfase:
declarados justos em Cristo,
não por obras.
Lição D4.4 – Santificação (graça que transforma)

Referência: 1Ts 4:3; 1Co 6:11
Ênfase:
separação do pecado,
obra do Espírito, cooperando com Ele.
Lição D4.5 – Perseverança dos santos

Referência: João 10:27–29; Filipenses 1:6
Ênfase:
Deus sustenta até o fim,
segurança em Cristo.
Lição D4.6 – Escatologia básica (esperança futura)

Referência: Apocalipse 21–22; 1Co 15 (recortes)
Ênfase:
nova criação,
consolo, não especulação sensacionalista.
Cada lição com:

3–5 exercícios,
devocional focando aplicação: confiança, arrependimento, esperança, obediência grata.
11.4. Sprints de conteúdo para Intermediário e Avançado
Para organizar a criação desse conteúdo:

Sprint C6 – Preencher trilhas Intermediárias
[ ] Crianças – completar Trilha C3 com pelo menos 6 lições (Heróis da Fé).
[ ] Adolescentes – completar Trilha A3 com pelo menos 6 lições (Vida na escola e em casa).
[ ] Adultos – completar Trilha D3 com pelo menos 6 lições (Vida cristã no dia a dia).
Sprint C7 – Preencher trilhas Avançadas
[ ] Crianças – completar Trilha C4 com pelo menos 6 lições (Parábolas).
[ ] Adolescentes – completar Trilha A4 com pelo menos 6 lições (Discipulado e chamado).
[ ] Adultos – completar Trilha D4 com pelo menos 6–8 lições (Doutrinas centrais).
Sprint C8 – Devocionais alinhados à teologia reformada
[ ] Criar devocional para cada lição Intermediária (C3, A3, D3), com:
[ ] foco na graça, Cristo e resposta em gratidão.
[ ] Criar devocional para cada lição Avançada (C4, A4, D4), com:
[ ] cuidado doutrinário e aplicação concreta.

1. Bloco “Série Ouro” (Desafio Extra Avançado)

12. Série Ouro – Desafios Extras de Alta Dificuldade
A Série Ouro é um conjunto de desafios opcionais, mais difíceis que as lições normais, para usuários que desejam se aprofundar mais e ganhar pontuação extra.

São atividades extras, desbloqueadas após a conclusão de uma lição ou trilha.
Dão mais pontos (XP e/ou pontos_para_ajuda) que uma lição comum.
Devem ser teologicamente mais exigentes, com foco em:
compreensão mais profunda do texto bíblico,
conexões com outras passagens,
aplicação mais desafiadora à vida,
sempre dentro da teologia reformada.
12.1. Conceito Geral
Nome interno: SerieOuro (ou “Desafio Ouro”).

Tipo: desafio opcional, mais difícil, atrelado a:

uma Lição específica (LicaoBiblica), ou
uma Trilha inteira (desafio final da trilha).
Objetivos:

Criar um “modo difícil” para quem quer se aprofundar.
Aumentar o lifetime, incentivando revisões profundas.
Oferecer mais pontuação para usuários mais engajados.
12.2. Modelo de dados (MVP)
Novo modelo em courses (ou app específico, se preferir):

SerieOuroDesafio

id
licao (FK para LicaoBiblica, opcional, se o desafio for ligado a uma lição)
trilha (FK para Trilha/curso, opcional, se for desafio da trilha)
titulo
descricao
faixa_etaria (para filtrar por idade)
nivel (normalmente “intermediario” ou “avancado”)
ordem (caso haja mais de um desafio ouro por lição/trilha)
ativo (bool)
SerieOuroExercicio

id
desafio_ouro (FK para SerieOuroDesafio)
tipo (como em Exercicio: MULTIPLA_ESCOLHA, VF, ASSOCIACAO, ORDENACAO, etc.)
enunciado
dados (JSON com alternativas, respostas corretas, etc.)
peso_dificuldade (opcional, inteiro, para ajustar pontuação extra)
SerieOuroProgresso

usuario (FK)
desafio_ouro (FK)
concluido (bool)
data_conclusao
xp_ganho
pontos_para_ajuda_ganhos
12.3. Regras de desbloqueio
Desafio Ouro de LIÇÃO:

Disponível apenas depois da lição normal estar marcada como concluída.
Exemplo: Desafio Ouro C3.1 aparece após o usuário terminar a Lição C3.1.
Desafio Ouro de TRILHA:

Disponível após todas as lições ativas da trilha estarem concluídas.
Pode funcionar como um “exame final” da trilha.
12.4. Nível de dificuldade
Os exercícios da Série Ouro devem:

Ter:
perguntas que exigem correlação de textos (ex.: ligar promessa do AT com cumprimento no NT),
interpretação mais profunda (sentido do texto, contexto, implicações),
aplicações mais desafiadoras (exigir reflexão mais longa).
Evitar:
decoração mecânica sem compreensão,
questões rasas iguais às da lição normal.
Exemplo para adultos – Trilha D4 (Doutrinas Centrais):

Lição D4.3 – Justificação pela fé:
Desafio Ouro:
Perguntas sobre:
diferença entre justificação e santificação,
implicações práticas de “não há condenação” (Rm 8:1),
perigo de legalismo x licenciosidade.
12.5. Pontuação
Completar um Desafio Ouro deve dar:
XP maior que a lição normal (ex.: 2x ou 3x);
possível bônus extra em pontos_para_ajuda.
Opcional:
liberar um baú especial (ex.: “Baú Ouro”) ao completar a Série Ouro de uma trilha.
12.6. Fluxo de uso
Usuário conclui a lição normal.
O sistema registra o progresso.
Ao voltar à tela de resultado ou à página da lição:
Aparece opção de “Desafio Ouro (extra)”.
Se o usuário aceitar:
Vai para tela do desafio extra, com exercícios bem mais difíceis.
Ao terminar:
Recebe XP extra,
Atualiza SerieOuroProgresso.
12.7. Sprints específicas para Série Ouro
Sprint S1 – Backend Série Ouro

[x] Criar modelos SerieOuroDesafio, SerieOuroExercicio, SerieOuroProgresso.
[x] Integrar com LicaoBiblica e trilhas (FKs).
[x] Definir regras de pontuação e desbloqueio.
[x] Criar views e endpoints para executar o Desafio Ouro.
Sprint S2 – Conteúdo Série Ouro

[x] Criar pelo menos 1 Desafio Ouro por trilha iniciante (C, A, D).
[ ] Criar 2 ou mais desafios por trilha intermediária e avançada (C3/C4, A3/A4, D3/D4).
[x] Garantir que todos seguem as diretrizes teológicas reformadas.

12. Painel do Admin – Visão de Usuários e Atividades
Esta seção define os requisitos para a visão de administrador (superuser) dentro da plataforma, permitindo acompanhar:

quem são os usuários,
quantos são,
seus logins (e-mails),
e as atividades realizadas (lições, desafios, Série Ouro, uso da IA, etc.).
12.1. Objetivos do painel de admin
O painel de admin deve permitir que o administrador:

Visualize uma lista consolidada de usuários:

nome,
e-mail (login),
data de cadastro,
faixa etária,
nível atual,
status de atividade (ativo/inativo).
Veja o número total de usuários:

global,
por faixa etária,
por nível (iniciante/intermediário/avançado).
Consulte atividades realizadas:

lições concluídas,
desafios diários concluídos,
Série Ouro realizada,
uso da IA (dicas e chat devocional) por usuário.
12.2. Modelos e dados de suporte
Além do User e UserProfile, o sistema deve registrar atividades em um modelo específico, por exemplo:

UserActivityLog (ou nome similar), com campos:
id
usuario (FK para User)
tipo_atividade (choices: LICAO_CONCLUIDA, DESAFIO_DIARIO, SERIE_OURO, CHAT_DEVOCIONAL, DICA_IA, etc.)
referencia (ex.: id da lição, id do desafio diário, id do desafio ouro, id do chat/tema)
descricao_resumida (texto curto: “Concluiu Lição C3.1 – Noé confiou em Deus”)
xp_ganho (IntegerField, opcional)
data_hora (DateTimeField, auto_now_add)
Esses registros podem ser preenchidos automaticamente sempre que:

uma lição for concluída,
um desafio diário for concluído,
uma Série Ouro for concluída,
o usuário solicitar dica ao tutor IA,
o usuário fizer sessões no chat devocional (log mais agregado, se necessário).
12.3. Visão de lista de usuários (admin)
No painel admin (Django Admin ou painel customizado), deve existir uma tela “Usuários” com:

Colunas principais:

Nome do usuário,
E-mail (login),
Data de cadastro,
Faixa etária,
Nível atual,
XP total,
Streak atual.
Filtros:

por faixa etária,
por nível atual,
por data de cadastro,
por atividade (usuários ativos nos últimos X dias).
Ações rápidas:

ver detalhes do perfil,
ver histórico de atividades.
12.4. Detalhe de usuário – atividades
Ao clicar em um usuário, o admin deve conseguir ver:

Resumo do perfil:

nome,
e-mail,
faixa etária,
nível atual,
XP total,
streak atual,
data de último acesso (se possível).
Atividades recentes (lista paginada ou limitada):

data/hora,
tipo de atividade (ícone + label),
descrição curta,
XP ganho (se aplicável).
Exemplos de linha de atividade:

[2026-06-28 19:42] LIÇÃO_CONCLUIDA – C3.1: Noé confiou em Deus – +15 XP
[2026-06-28 19:50] DESAFIO_DIARIO – D3 “Agradeça pela criação” – +5 XP
[2026-06-28 20:05] SERIE_OURO – Trilha D4 – Desafio 1 – +40 XP
[2026-06-28 20:10] DICA_IA – Lição A3.2 – usou 10 pontos de ajuda
12.5. Métricas agregadas no admin
Criar uma visão de “Estatísticas gerais” para o admin, com:

Total de usuários:

número global,
por faixa etária (crianças, adolescentes, adultos),
por nível (iniciante, intermediário, avançado).
Engajamento:

número de lições concluídas nos últimos 7 dias,
número de desafios diários concluídos,
número de Série Ouro concluídas,
uso de IA (quantidade de dicas / sessões de chat).
Essas métricas podem ser exibidas em cards simples ou gráficos (opcional nesta fase).

12.6. Integração com o frontend admin (opcional)
Se for criado um painel customizado (fora do Django Admin padrão), o frontend deve:

ter uma página /admin-dashboard/ (protegida, apenas superusers) com:

Cards principais:

Total de usuários,

Usuários por faixa etária,

Lições concluídas na semana,

Desafios diários concluídos na semana.

Tabela de usuários:

com colunas e filtros descritos acima.

Link “Ver atividades” por usuário:

abre página com histórico detalhado.

12.7. Sprint específica para visão do admin
Adicionar uma sprint focada nessa funcionalidade:

Sprint A1 – Visão Admin de Usuários e Atividades
[x] Criar modelo UserActivityLog com tipos de atividade e dados básicos (usuário, tipo, referência, descrição, data/hora, XP).
[x] Registrar UserActivityLog no Django Admin, com listagem por usuário e filtros por tipo e data.
[x] Ajustar fluxo de lições, desafios e IA para registrar atividades automaticamente nesse modelo.
[ ] Adicionar visão de lista de usuários no admin com:
[ ] colunas: nome, e-mail, faixa etária, nível, XP, streak,
[ ] filtros por faixa etária e nível.
[ ] Criar página de detalhe do usuário no admin com:
[ ] resumo do perfil,
[ ] tabela de atividades recentes (a partir de UserActivityLog).
[ ] Criar painel de estatísticas agregadas (total de usuários, atividades da semana) para o admin.