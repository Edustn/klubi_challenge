# Descrição do Projeto
O objetivo deste projeto é criar um chatbot inteligente que facilite e melhore a jornada do cliente na aquisição de veículos através do sistema de consórcio do Klubi, oferecendo atendimento personalizado e eficiente.

# Autor 
- [Eduardo Henrique dos Santos](https://www.linkedin.com/in/eduardo-henrique-dos-santos/)

# Organizaçaão de pastas
```
KLUBI_CHALLENGE/
├── src/
│   ├── backend/
│   │   ├── .env.exemplo
│   │   ├── .gitignore
│   │   └── main.py
│   ├── data/
│   │   └── cars.json
│   ├── frontend/
│   │   └── app/
│   │       ├── app/
│   │       ├── components/
│   │       ├── public/
│   │       ├── .gitignore
│   │       ├── README.md
│   │       ├── eslint.config.mjs
│   │       ├── next.config.ts
│   │       ├── package.json
│   │       ├── package-lock.json
│   │       ├── postcss.config.mjs
│   │       └── tsconfig.json
├── requirements.txt
```

# Tecnolgias utilizadas:
- Backend (Python com Flask)
  Para a camada de backend do projeto, foi escolhida a linguagem Python com o microframework Flask, devido à sua simplicidade, leveza e excelente desempenho em aplicações baseadas em APIs RESTful. Essa escolha foi especialmente adequada para um sistema que precisa receber requisições, processar dados de veículos e integrar-se com modelos de inteligência artificial, como o Google Generative AI (Gemini).

  O Flask permite uma estrutura de código enxuta, com rápida configuração inicial e boa modularização, o que favorece a manutenção e a escalabilidade do projeto. Além disso, a linguagem Python possui ampla compatibilidade com bibliotecas voltadas à IA e ao processamento de dados, facilitando a manipulação de respostas automatizadas e personalizadas para os usuários do sistema de consórcios.

- Frontend (Next.js)
  No frontend, optou-se pelo uso do framework Next.js, baseado em React, com o objetivo de oferecer uma experiência moderna, performática e responsiva ao usuário. O Next.js se destaca pelo suporte nativo à renderização no servidor (SSR) e à geração estática de páginas (SSG), que proporcionam tempos de carregamento reduzidos, melhor desempenho em diferentes dispositivos e otimização para mecanismos de busca (SEO) — um aspecto importante em plataformas comerciais como a de simulação de consórcios.

  A utilização do React possibilitou a construção de componentes reutilizáveis e interfaces interativas, como formulários dinâmicos de simulação e sistemas de recomendação baseados em perfil de cliente. Complementando isso, o suporte a TypeScript e TailwindCSS dentro do ecossistema Next.js proporcionou uma base de código mais segura, organizada e com um design visual consistente. A estrutura modular e a integração com rotas de API também tornam o frontend preparado para expansão futura, caso surjam novas necessidades.

# Experiência do usuário
A solução foi desenvolvida com uma interface simples e intuitiva, no formato de chat, composta por um campo de texto para inserção da mensagem e um botão de envio. Esse modelo de interação foi escolhido por ser amplamente reconhecido e utilizado em diversos aplicativos e plataformas, o que o torna familiar para usuários de diferentes faixas etárias e níveis de experiência digital. Ao adotar esse formato, busca-se reduzir a curva de aprendizado e evitar que o usuário perca tempo com tarefas triviais, proporcionando uma experiência direta, acessível e eficiente.

# Plano de negócios  

  

