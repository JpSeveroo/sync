
---

## 🟢 Versão 1.0: O "Sync" (MVP Solo)
**Foco:** O Ciclo Principal (Core Loop). O sistema deve ser útil para o uso individual imediato.

### 1.1 Módulo de Autenticação (Auth)
- [ ] **Tela de Login:** Campos para E-mail e Senha(ter a opção de visualizar enquanto escreve) + Botão "Entrar" + Esqueceu senha
- [ ] **Tela de Cadastro:** Campos para Nome, Idade, nick, País E-mail, Senha e Confirmação.
- [ ] **Recuperação de Acesso:** Link "Esqueci minha senha" (envio de e-mail com token/link).
- [ ] **Sessão Persistente:** O sistema deve manter o usuário logado ao fechar/abrir o navegador.

### 1.2 Módulo de Busca & Ingestão
- [ ] **Busca Global:** Barra de pesquisa unificada (aceita nomes de Jogos, Animes ou Livros).
- [ ] **Listagem de Resultados:** Cards simples exibindo Capa, Título, Ano e Tipo de Mídia.
- [ ] **Página de Detalhes:** Visualização completa da obra com Capa Grande, Sinopse, Gêneros, Autor/Dev e Data.

### 1.3 Módulo da Estante (Library)
- [ ] **Botão "Adicionar":** Localizado na página de detalhes da obra.
- [ ] **Gerenciamento de Status:** Seletor obrigatório: *Planejando, Consumindo, Finalizado, Abandonado*.
- [ ] **Atribuição de Nota:** Campo numérico (0 a 10), habilitado apenas para itens "Finalizados".
- [ ] **Visualização da Estante:** Grid exibindo todas as obras salvas pelo usuário.
- [ ] **Filtros Básicos:** Botões para filtrar a estante por Status (ex: ver apenas o que estou "Consumindo").

### 1.4 Gamificação Base
- [ ] **Cálculo de XP:** Sistema backend que atribui pontos fixos por ações (Adicionar = X pontos, Finalizar = Y pontos).
- [ ] **Feedback de Nível:** Header exibindo Avatar, Nome, Nível Atual e Barra de XP visual.

### 1.5 Configurações Básicas & Suporte
- [ ] **Perfil de Conta:** Editar Nome de Exibição e Biografia curta.
- [ ] **Segurança:** Formulário para alteração de senha atual.
- [ ] **Suporte Básico:** Botão "Reportar Problema" que redireciona para o e-mail de suporte (`mailto:`).
- [ ] **Zona de Perigo:** Botão para "Excluir Conta" (hard delete).

---

## 🟡 Versão 2.0: Conexão Social
**Foco:** Transformar dados isolados em interações sociais.

### 2.1 Perfis Públicos
- [ ] **URL Pública:** O perfil do usuário torna-se acessível via link direto (`/u/nickname`).
- [ ] **Modo Visitante:** Usuários podem ver estantes alheias (sem botões de edição).

### 2.2 Sistema de Conexões (Follow)
- [ ] **Ação de Seguir:** Botão "Follow/Unfollow" no perfil de outros usuários.
- [ ] **Listas Sociais:** Página listando "Seguindo" e "Seguidores".

### 2.3 Feed de Atividades (Timeline)
- [ ] **Home Feed:** Página inicial (para logados) mostrando atividades cronológicas de quem o usuário segue.
- [ ] **Cards de Atividade:** "Usuário X finalizou Jogo Y - Nota 9".
- [ ] **Interação Rápida:** Botão de "Curtir" (Like) nas atividades.

### 2.4 Conteúdo Rico (Reviews)
- [ ] **Review de Texto:** Campo de texto expandido ao finalizar uma obra.
- [ ] **Página de Review:** URL dedicada para ler a análise completa de um usuário.

---

## 🔵 Versão 3.0: Comunidade (Fóruns)
**Foco:** Discussão aprofundada e retenção via conteúdo.

### 3.1 Estrutura de Fórum
- [ ] **Índice de Categorias:** Página listando temas gerais (Geral, Dúvidas, Off-topic).
- [ ] **Tópicos:** Funcionalidade de criar título e corpo de texto (Markdown).
- [ ] **Respostas:** Sistema de comentários lineares dentro dos tópicos.

### 3.2 Discussão Contextual
- [ ] **Aba na Obra:** Na página de detalhes (ex: Naruto), uma aba "Discussões" listando tópicos vinculados àquela obra.

### 3.3 Central de Notificações
- [ ] **Alertas Visuais:** Ícone de sino indicando novas interações.
- [ ] **Tipos de Alerta:** "Novo seguidor", "Comentário na sua review", "Resposta no fórum".

---

## 🟣 Versão 4.0: Economia & Loja
**Foco:** Recompensas visuais e "gasto" do progresso acumulado.

### 4.1 Economia Virtual
- [ ] **Sync Coins:** Lógica de conversão de conquistas/XP em moeda virtual.
- [ ] **Carteira:** Exibição do saldo atual no perfil.

### 4.2 Loja de Cosméticos
- [ ] **Catálogo Visual:** Página exibindo Molduras de Avatar e Banners de Perfil disponíveis.
- [ ] **Transação:** Botão de compra que debita o saldo e libera o item.

### 4.3 Inventário & Personalização
- [ ] **Inventário:** Área para visualizar itens comprados.
- [ ] **Seletor de Equipamento:** Funcionalidade para ativar/desativar molduras e banners, alterando o visual público do perfil.

---

## 🔴 Versão 5.0: Gestão & Analytics
**Foco:** Manutenção da plataforma e dados de inteligência para o usuário.

### 5.1 Dashboard Pessoal (Data Science)
- [ ] **Gráficos de Consumo:** Visualização de Gêneros favoritos (Pizza) e Atividade Mensal (Barras).
- [ ] **Contador de Tempo:** Exibição de horas totais investidas (baseado em metadados das obras).

### 5.2 Painel Administrativo (Admin)
- [ ] **Moderação de Usuários:** Lista com busca para banir/bloquear contas.
- [ ] **Moderação de Conteúdo:** Ferramenta para ocultar ou apagar reviews/tópicos reportados.

### 5.3 Suporte Avançado
- [ ] **Sistema de Tickets:** Formulário interno de contato com status (Aberto, Em Análise, Resolvido).