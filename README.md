💰 Gerenciador de Finanças Pessoais (Devedores)

Sistema desenvolvido em Python para controle de dívidas e pagamentos, focado em organização, integridade de dados e experiência do usuário via terminal.

📌 Sobre o Projeto

Este projeto nasceu da necessidade de gerenciar movimentações financeiras entre credores e devedores de forma simples e eficiente. 
O sistema permite cadastrar nomes.
registrar valores (positivos para dívidas, negativos para pagamentos)
visualizar extratos detalhados com cálculo automático de saldo.

🚀 Funcionalidades

- Cadastro Inteligente: Padronização de nomes (Title Case) para evitar duplicatas por erro de digitação.
- Gestão de Transações: Adição de dívidas e registros de pagamentos no mesmo histórico.
- Extrato Detalhado: Exibição de todas as movimentações com formatação de moeda (R$) e status de saldo final.
- Resiliência de Dados: Persistência automática em arquivo `JSON`. O sistema carrega os dados salvos sempre que é iniciado.
- Tratamento de Erros: Proteção contra entradas inválidas (letras em campos numéricos) e tratamento para arquivos corrompidos ou inexistentes.

🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.x
- Persistência: JSON (JavaScript Object Notation)
- Bibliotecas Nativas: `json`, `os`

📦 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório ou baixe o arquivo `app.py`.
3. No terminal, execute o comando:
   ```bash
   python app.py
🧠 Aprendizados Aplicados
Durante o desenvolvimento deste projeto, foram aplicados conceitos fundamentais de Ciência da Computação e Desenvolvimento de Software:

Manipulação de Dicionários e Listas em Python.

Gerenciamento de arquivos (Leitura/Escrita).

Tratamento de exceções com blocos try/except.

Versionamento de código com Git e boas práticas de .gitignore.

Desenvolvido por Nycolas oliveira - Estudante de TI 🎓