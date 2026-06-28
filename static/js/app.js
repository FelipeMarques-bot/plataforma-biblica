document.addEventListener('alpine:init', () => {
  // Dashboard
  Alpine.data('dashboard', () => ({
    streak: 34,
    xpData: [
      { day: 'Seg', xp: 80 },
      { day: 'Ter', xp: 120 },
      { day: 'Qua', xp: 95 },
      { day: 'Qui', xp: 110 },
      { day: 'Sex', xp: 60 },
      { day: 'Sáb', xp: 130 },
      { day: 'Dom', xp: 100 },
    ],
    maxXp: 130,
    loading: false,
    get xpPercentage() {
      return this.xpData.map(d => (d.xp / this.maxXp) * 100)
    },
    get todayXp() {
      return this.xpData[this.xpData.length - 1].xp
    },
    get totalXp() {
      return this.xpData.reduce((a, b) => a + b.xp, 0)
    },
    continueLesson() {
      window.location.href = 'src/pages/trilhas.html'
    }
  }))

  // Mapa de Trilhas
  Alpine.data('trilhas', () => ({
    modulos: [
      {
        nome: 'Módulo 1: O Princípio',
        licoes: [
          { id: 1, titulo: 'Gênesis 1', icone: '☀️', status: 'completed' },
          { id: 2, titulo: 'Gênesis 2', icone: '🌿', status: 'completed' },
          { id: 3, titulo: 'Gênesis 3', icone: '🍎', status: 'active' },
          { id: 4, titulo: 'Gênesis 4', icone: '🌾', status: 'locked' },
          { id: 5, titulo: 'Gênesis 5', icone: '📜', status: 'locked' },
        ]
      },
    ],
    activeLesson: null,
    setActive(licao) {
      if (licao.status === 'active' || licao.status === 'completed') {
        this.activeLesson = licao
      }
    },
    openLesson(licao) {
      if (licao.status === 'active') {
        window.location.href = 'licao.html'
      }
    }
  }))

  // Tela de Lição
  Alpine.data('licao', () => ({
    currentQuestion: 0,
    selectedOption: null,
    answered: false,
    correct: null,
    showDica: false,
    showResult: false,
    xpGained: 0,
    questions: [
      {
        pergunta: 'O que Deus criou no primeiro dia?',
        opcoes: ['O céu e a terra', 'A luz', 'Os animais', 'O homem'],
        correta: 1,
        dica: 'Gênesis 1:3 — "Disse Deus: Haja luz"'
      },
      {
        pergunta: 'Em que dia Deus criou os animais marinhos?',
        opcoes: ['Terceiro dia', 'Quarto dia', 'Quinto dia', 'Sexto dia'],
        correta: 2,
        dica: 'Gênesis 1:20 — "Povoem as águas de seres viventes"'
      },
      {
        pergunta: 'O que significa o nome "Adão"?',
        opcoes: ['Vida', 'Homem / Humanidade', 'Terra / Solo', 'Filho de Deus'],
        correta: 2,
        dica: 'Adão vem do hebraico "adamah" (solo/terra).'
      },
    ],
    get progress() {
      return ((this.currentQuestion + 1) / this.questions.length) * 100
    },
    get currentQ() {
      return this.questions[this.currentQuestion]
    },
    checkAnswer() {
      if (this.selectedOption === null) return
      this.answered = true
      this.correct = this.selectedOption === this.currentQ.correta
      if (this.correct) {
        this.xpGained += 20
      }
    },
    nextQuestion() {
      if (this.currentQuestion < this.questions.length - 1) {
        this.currentQuestion++
        this.selectedOption = null
        this.answered = false
        this.correct = null
        this.showDica = false
      } else {
        this.finishLesson()
      }
    },
    finishLesson() {
      this.showResult = true
    },
    backToMap() {
      window.location.href = 'trilhas.html'
    }
  }))

  // Chat Devocional
  Alpine.data('chatDevocional', () => ({
    mensagens: [
      {
        tipo: 'ia',
        texto: 'Bem-vindo ao seu momento de reflexão. Hoje meditaremos em Salmos 23. O que significa para você o Senhor ser seu pastor?'
      }
    ],
    inputMessage: '',
    isTyping: false,
    scripture: {
      text: 'O SENHOR é o meu pastor; nada me faltará.',
      reference: 'Salmos 23:1',
      note: 'Uma declaração de confiança total na provisão divina.'
    },
    sendMessage() {
      if (!this.inputMessage.trim()) return
      this.mensagens.push({ tipo: 'usuario', texto: this.inputMessage })
      this.inputMessage = ''
      this.isTyping = true
      setTimeout(() => {
        this.isTyping = false
        this.mensagens.push({
          tipo: 'ia',
          texto: 'Que reflexão profunda! Davi escreveu este salmo em um momento de paz, lembrando que Deus guia cada passo. Como você vê essa liderança de Deus na sua vida hoje?'
        })
      }, 2000)
    }
  }))

  // Série Ouro
  Alpine.data('serieOuro', () => ({
    baúAberto: false,
    recompensa: null,
    aberto: false,
    chestShaking: false,
    desafios: [
      { id: 1, nome: 'Sobrevivência', questoes: 50, dificuldade: 'Extremo' },
      { id: 2, nome: 'Profetas Maiores', questoes: 30, dificuldade: 'Difícil' },
      { id: 3, nome: 'Sabedoria', questoes: 40, dificuldade: 'Difícil' },
    ],
    openChest() {
      this.chestShaking = true
      setTimeout(() => {
        this.chestShaking = false
        this.aberto = true
        this.recompensa = {
          tipo: 'Medalha de Ouro',
          texto: 'Fé Inabalável',
          xp: 500,
        }
        setTimeout(() => {
          this.baúAberto = true
        }, 600)
      }, 600)
    },
    resetChest() {
      this.baúAberto = false
      this.recompensa = null
      this.aberto = false
      this.chestShaking = false
    }
  }))
})
