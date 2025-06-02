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
# Instruções para inicialização do projeto

Pré-requisitos:

Python 3.10+

Node.js 18+

npm ou yarn

Sistema operacional Linux, mas pode ser utlizado para macOS ou Windows basta conhecer os comandos para seu sistema operacional.

Visual Studio Code (recomendado)

1 - Clone este repositório: [https://github.com/Edustn/klubi_challenge](https://github.com/Edustn/klubi_challenge)


2- Após isso abra o Visual Studio Code e abra o repositório clonado.


3- Agora abra o terminal integrado do Visual Studio Code e nave até a pasta `src` e inicie um ambiente de desenvolvimento para o Python (no caso um venv) para isso digite no terminal integrado: `python3 -m venv venv`.


4- Agora no mesmo terminal integrado que baixou o venv inicie ele com o comando: `. venv/bin/activate` e baixe as dependências deixadas no `requirements.txt` para isso digite: `pip install -r requirements.txt`.


5- Agora navegue até a pasta `backend` crie um arquivo `.env` e coloque sua chave da API do Gemini (o modelo do `.env` pode ser visto em `.env.exemplo`) e com o terminal integrado inicialize o servidor em Python através do comando: `python3 main.py`.


6- Agora abra outro terminal e navegue até a pasta `frontend` e instale as dependências através do comando `npm i`


7 - Após isso, navegue até a pasta `app` e inicie o projeto através do comando: `npm run dev`


Com todos esses passos feitos verá que a aplicação irá inicializar de forma local e poderá interagir com ela sem dificuldades.


*obs: Esses comandos foram realizados em um ambiente Linux.


# Demonstração do Projeto
Link para vídeos: [https://drive.google.com/drive/folders/1Fjmnl7SpflMNnXELVoOSF6t_OLlBmhED?usp=sharing](https://drive.google.com/drive/folders/1Fjmnl7SpflMNnXELVoOSF6t_OLlBmhED?usp=sharing)

Nessa demonstração temos dois vídeos, um sendo quando o usuário tem o valor para pegar o carro que deseja (valor_dentro_orcamento) e outro com o usuário sem ter o valor para o carro desejado (valor_fora_orcamento).

# Tecnolgias utilizadas:
- Backend (Python e Flask)
  Para a camada de backend do projeto, foi escolhida a linguagem Python com o microframework Flask, devido à sua simplicidade, leveza e excelente desempenho em aplicações baseadas em APIs RESTful. Essa escolha foi especialmente adequada para um sistema que precisa receber requisições, processar dados de veículos e integrar-se com modelos de inteligência artificial, como o Google Generative AI (Gemini).

  O Flask permite uma estrutura de código enxuta, com rápida configuração inicial e boa modularização, o que favorece a manutenção e a escalabilidade do projeto. Além disso, a linguagem Python possui ampla compatibilidade com bibliotecas voltadas à IA e ao processamento de dados, facilitando a manipulação de respostas automatizadas e personalizadas para os usuários do sistema de consórcios.

- Frontend (Next.js)
  No frontend, optou-se pelo uso do framework Next.js, baseado em React, com o objetivo de oferecer uma experiência moderna, performática e responsiva ao usuário. O Next.js se destaca pelo suporte nativo à renderização no servidor (SSR) e à geração estática de páginas (SSG), que proporcionam tempos de carregamento reduzidos, melhor desempenho em diferentes dispositivos e otimização para mecanismos de busca (SEO) — um aspecto importante em plataformas comerciais como a de simulação de consórcios.

  A utilização do React possibilitou a construção de componentes reutilizáveis e interfaces interativas, como formulários dinâmicos de simulação e sistemas de recomendação baseados em perfil de cliente. Complementando isso, o suporte a TypeScript e TailwindCSS dentro do ecossistema Next.js proporcionou uma base de código mais segura, organizada e com um design visual consistente. A estrutura modular e a integração com rotas de API também tornam o frontend preparado para expansão futura, caso surjam novas necessidades.

# Experiência do usuário
A solução foi desenvolvida com uma interface simples e intuitiva, no formato de chat, composta por um campo de texto para inserção da mensagem e um botão de envio. Esse modelo de interação foi escolhido por ser amplamente reconhecido e utilizado em diversos aplicativos e plataformas, o que o torna familiar para usuários de diferentes faixas etárias e níveis de experiência digital. Ao adotar esse formato, busca-se reduzir a curva de aprendizado e evitar que o usuário perca tempo com tarefas triviais, proporcionando uma experiência direta, acessível e eficiente.

# Plano de negócios  
## 1. Modelo de negócios
O modelo de negócio adotado é do tipo B2B (business-to-business), voltado especialmente para administradoras de consórcio. A comercialização se dará por meio de licenciamento de software no modelo SaaS (Software as a Service), em que a empresa contratante paga uma mensalidade fixa pelo uso contínuo do chatbot.

Essa abordagem garante previsibilidade de receita e favorece contratos de médio e longo prazo. O modelo também permite escalabilidade horizontal, já que o mesmo software pode ser replicado para múltiplos clientes com necessidade de personalização mínima.

Além disso, a estrutura SaaS facilita atualizações contínuas, acesso remoto e integração com sistemas existentes (ex: CRMs, sistemas de cotação), fatores valorizados por administradoras que buscam inovação com baixo custo de implementação.


## 2. Estratégia de Aquisição de Primeiros Usuários:
A entrada no mercado será viabilizada por uma combinação de vendas diretas, parcerias estratégicas e marketing digital:

- Vendas Diretas: Uma equipe comercial especializada será responsável por abordar administradoras de consórcio, com foco em apresentar os benefícios do chatbot na conversão de leads, qualificação automática de clientes e redução de carga operacional nos atendimentos iniciais.

- Parcerias Estratégicas: A solução poderá ser integrada a sistemas de CRM já utilizados pelas administradoras (como Salesforce, Pipedrive ou RD Station), facilitando a adoção do chatbot dentro dos fluxos já existentes de atendimento e vendas. 

- Inbound Marketing: Serão produzidos conteúdos educativos voltados para o público de gestores de consórcio, com temas como: “Como reduzir objeções de clientes no consórcio usando IA” ou “Automatização de atendimento sem perder a personalização”. O objetivo é atrair leads qualificados organicamente.

- Mídia Paga: Campanhas direcionadas no Google e nas plataformas Meta (Instagram e Facebook), com foco em palavras-chave como “melhorar vendas de consórcio”, “automatização de atendimento” e “IA para consórcios”. Os anúncios terão como público-alvo decisores de compra em empresas administradoras.


## 3. Estimativa de CAC (Custo de Aquisição por Cliente):
B2B – Administradoras de Consórcio
O CAC inicial tende a ser alto (entre R$ 500,00 e R$ 2.000,00), devido à natureza do ciclo de vendas B2B, que envolve múltiplos decisores, apresentações técnicas e tempo de negociação.

Contudo, espera-se uma redução progressiva do CAC com o avanço da operação comercial, construção de cases de sucesso e aquisição de clientes por indicação (efeito de rede entre administradoras).

B2C – Usuários Finais (Indiretamente)
Embora o foco do modelo de negócio seja B2B, o chatbot interage diretamente com o consumidor final. Isso permite projetar um CAC indireto muito baixo (R$ 5,00 a R$ 20,00), via tráfego orgânico ou campanhas digitais otimizadas.


## 4. LTV (Life Time Value) e Maximação
B2B – Administradoras
O LTV estimado por cliente gira em torno de R$ 12.000,00 por ano, considerando uma mensalidade média de R$ 1.000,00 e contratos de no mínimo 12 meses. Em contratos mais longos, será aplicada correção inflacionária anual.

A maximização de receita por cliente se dará por meio de estratégias como:

Upselling de módulos adicionais, como análise de inadimplência automatizada, dashboard de métricas de conversão ou segmentação comportamental dos leads atendidos pelo chatbot.

Customizações avançadas sob demanda, com cobrança adicional, voltadas para integrações específicas ou fluxos personalizados de atendimento.   

## 5. Monetização

A monetização será baseada em duas fontes principais:

Receita recorrente: Proveniente da assinatura mensal do software no modelo SaaS pelas administradoras.

Receita variável (complementar): Taxas cobradas por integrações com sistemas de terceiros (ex: tabelas FIPE, CRMs, gateways de pagamento, validação documental). Essa cobrança pode ser feita por volume de uso ou por pacote adicional.

Essas duas medidas fazem com que a monetização seja previsível e flexível para um crescimento sustentável conforme a evolução do cliente.

## 6. Estratégia de Retenção

Para retenção de clientes serão adotadas as seguintes práticas:

Relacionamento proativo com o cliente: Envio de relatórios mensais de performance do chatbot, incluindo número de atendimentos, taxa de conversão e sugestões de melhoria baseadas em dados reais.

Atualizações constantes: Inclusão contínua de novas funcionalidades com base em feedback dos clientes, reforçando a percepção de evolução e alinhamento com suas demandas.

Suporte dedicado: Canal exclusivo de suporte técnico e consultoria para ajustes estratégicos no fluxo de atendimento e nas integrações.

