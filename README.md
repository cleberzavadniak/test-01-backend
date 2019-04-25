# test-01: backend

A simple login screen.

## Links

* [Backend](http://cztest01-backend.herokuapp.com/)
* [Frontend](https://cztest01-frontend.netlify.com).

---

**Prepare seu coração e sua mente** para o que vem a seguir. Este é,
certamente, o teste mais feio e, concomitantemente, mais belo que você
ainda avaliará.


Os parâmetros requeridos foram os seguintes:

* Frontend: em react utilizando o modelo da figura que está no corpo do
  e-mail
* Backend: .netcore utilizando banco de dados relacional da preferência do
  candidato
* DevOps: cada commit na master deve fazer o deploy na AWS
* Qualidade: 80% de cobertura de testes unitários


Já os critérios de avaliação seriam:

* Escalabilidade
* Aderência às melhores práticas de escrita de código
* Segurança
* Visão de limitações da solução e próximos passos


# Visão geral do processo

Ultimamente tenho passado dias **muito atarefados**: não somente há
trabalho a dar com o pé no meu serviço atual (estou, veja só,
**implementando novidades na arquitetura** da nossa plataforma) como
preciso dispender cerca de **uma hora e meia** de quando em quando em
compromissos pessoais.

Ou seja: **tempo é um bem muito precioso e escasso** para mim.


## Decisões

O e-mail com a descrição do teste terminava com "*Gentileza nos enviar
a solução do teste até 24/04/19.*". E isso é bem interessante, porque
é **um gatilho para uma tomada de decisão** bem similar a algumas que se
encontra na gestão de projetos de software.

Eu teria pouquíssimas horas para não somente **planejar** uma arquitetura
mas também **implementar todos os componentes**.

Logo, surge a questão: "*o que receberá prioridade? Prazo ou qualidade?*".

Eu poderia ter priorizado qualidade e, dados os recursos à mão (apenas um
desenvolvedor (eu) com tempo de trabalho diário bem limitado), **chuto**
que a tarefa demoraria cinco ou seis dias. Alguém pode erguer as
sombrancelhas em estranhamento ao ouvir isso, mas, lembre-se: é o cenário
que põe qualidade acima de prazo.

Em outra situação eu provavelmente decidiria por essa primeira opção
e o principal motivo seria o fato que **o prazo foi absolutamente
arbitrário**. Afinal, numa equipe *ágil* os prazos devem ser estimados
baseando-se em números (e uma boa dose de *gut feeling*, é verdade, mas
nunca sem a presença de, no mínimo, uma divisão de taredas e a devida
pontuação das mesmas).

Todavia, foi-me dito pelo pessoal da prestadora de serviços de RH que "*o
cliente prefere decidir, de preferência, essa semana*".

**O que é uma pena**. Na vida real, essa seria uma "*sprint louca*", em
que os prazos não são definidos pela equipe, são curtos (e pouco
realísticos) e acaba-se por defenestrar-se as boas práticas e focar em
"*entregar depressa porque ou a gente entrega ou perdemos o cliente*".


Mas assim é a vida e imprevistos acontecem. O importante é ter jogo de
cintura e saber como contorná-los da melhor maneira possível.

A decisão, então, foi priorizar o prazo sobre a qualidade. Como não deve
surpreender ninguém, **débito técnico foi gerado**. É o fim do mundo?
Certamente não. É o ideal? Certamente não.

## Arquitetura ou design?

Considero importante ter em mente que a vaga é para **arquiteto de
sistemas** e não "desenvolvedor". **Acho justo** que deseje-se que
o Arquiteto domine bem as linguagens usadas na empresa e seus respectivos
*gestuais*. Mas aqui o processo decisório vai para o contratante: *o que
você vai priorizar? Habilidade no uso das ferramentas ou conhecimento
sobre Arquitetura de Sistemas e capacidade de gestão de uma equipe de
desenvolvimento de software?*

**Eu não sou o mais exímio desenvolvedor React, tampouco .Net**. Mas
entendo bem de Arquitetura de Sistemas e sou perfeitamente capaz de gerir
equipes de desenvolvimento.

# Frontend

É de **2015** o último projeto profissional usando React em que me
envolvi. De lá pra cá, muita coisa interessante aconteceu e fiquei
positivamente surpreso com a facilidade de se criar um novo projeto
usando-se o `npx` aliado ao `npm start`.

Diabos, eu lembro de como era a vida no tempo do **Bower**!

Nesse meio tempo, o pouco que desenvolvi usando Javascript foi um projeto
pessoal que usava [**Riot**](https://riot.js.org/), no ano passado (2018).

## Principais problemas

Não está sendo usado
o [**Flux**](https://facebook.github.io/flux/docs/in-depth-overview.html#content)!
Algumas coisas ficaram "meio penduradas", como a conexão ao roteador WAMP
(mais sobre ele depois).

Também não usei um **router**, mas fiz o componente alterar entre
o formulário de login e de criação de nova conta baseando-se no `state`,
**e isso é péssimo**. "Funciona", mas eu não deixaria isso passar num
*code review*.

E, para piorar, **absolutamente não há testes**. Como eu disse no começo:
*prazo sobre qualidade*. É questão de investir um tempo para [ler
a respeito do assunto](https://reactjs.org/docs/test-utils.html) e ganhar
essa linda habilidade que é escrever os devidos testes.


[CSS](https://imasters.shop/canecas/caneca-css3-perfeito.html)? Que lindo
sonho. Conheço bem há muitos anos. Até hoje não sei centralizar um
`div`.

(Ademais, a "montagem" **necessita** de um desenvolvedor/designer
plenamente capacitado a trabalhar com CSS. Qualquer coisa diferente
resulta em um ["site de
programador"](https://www.motherfuckingwebsite.com/).)

# Backend

**Mandei a regra pro escambau e fiz o backend em Python**. Admito.


Mas, evidentemente, o problema em si é **o runtime, não a linguagem**.
Porque ".Net Core", afinal, permite que se escreva em qualquer linguagem,
contanto que gere-se a *Common Intermediate Language*, certo?

Certo.


Mas também não vou me fingir de bobo e admito que sei bem que, mui
provavelmente, vosso desejo era ver código escrito em **C#** ou
**Asp.Net**.

Pois bem, foi somente graças à intervenção do Satya Nadella na Microsoft
que .Net começou a me parecer algo razoavelmente interessante. Antes
disso, aquele "mundinho proprietário" meio bizarro criado na era Ballmer
dava-me calafrios e nunca ousei trilhar os caminhos obscuros que levavam
para dentro dele.

Com o .Net Core **open source**, a coisa muda um pouco de figura. Mas
temos que admitir que tal mudança é razoavelmente recente e eu, admito,
não cheguei a dedicar tempo o bastante para dominar a linguagem (C#)
e tampouco o **gestual** (NuGet, bibliotecas, ambientes, etc).


Eu **já desenvolvi em C#**, mas era um projeto pequeno. Desenvolvido sobre
Mono+Linux e rodado sobre .Net+Windows: isso foi algo bem legal. Isso em
**2015**.

Também já **geri uma pequena equipe que desenvolvia em C#**. O projeto não
decolou, mas a experiência foi interessante. Isso, também, em 2015.


Mas isso tudo é sobre as decisões tomadas. Comentarei mais sobre os
detalhes de implementação no tópico "Arquitetura".


De qualquer forma, depois de aprender shell script, C, C++, PHP, Python,
Erlang, LISP e Prolog (e outras linguagens, que domino menos), trabalhar
com Asp.Net ou C# não tem por que apresentar qualquer problema.

# DevOps

Eu percebi uma certa ênfase em **AWS**, mas preferi ir pelo caminho mais
simples e publicar o projeto via
[Heroku](http://cztest01-backend.herokuapp.com/)
e [Netlify](https://cztest01-frontend.netlify.com).


O primeiro motivo é o mais simples: me recuso a ficar criando contas na
AWS para cada teste desses que eu fizer.

É **muito** mais simples usar Heroku+Netlify...


**Numa arquitetura de microsserviços**
a complexidade deixa de residir no *design* (ou seja: nas linhas de código
de cada componente) e passa para a **arquitetura** (ou seja: a interação
dos componentes entre si). Por isso eu não acho que seja uma boa ideia
essa história de "*cada commit na master deve fazer o deploy na AWS*".

Veja só: uma arquitetura de microsserviços **purista** facilmente tem
dezenas, quiçá **centenas** de pequenos componentes. E a complexidade,
lembre-se, está na **interação** entre esses componentes, ou seja: há
dezenas ou centenas de **contratos** que devem ser respeitados e uma
alteração em um componente pode facimente demandar alterações em diversos
outros.

Por isso a ideia do "deploy automático" é **potencialmente problemática**.
Isso jamais poderia ser feito sem o devido teste de integração e, no
geral, os testes acabariam tendo taxas de falha razoáveis depois de um
tempo, sendo também demorados e, per si, **outra** base de código a ser
mantida.

**Deploys devem ser assistidos**, e essa regra só pode ser deixada de lado
depois que a arquitetura toda estiver plenamente coberta por testes de
integração.


Por isso o `git push heroku master`, **absolutamente manual**, acaba
sendo, em boa parte dos casos, uma opção mais segura.


[Uma arquitetura com ambientes de
homologação](https://www.gocd.org/2018/04/25/five-considerations-continuous-delivery-microservices/)
dá algum trabalho de se implementar, mas é outra solução interessante.


A própria AWS dá diversas opções para a implantação de deploys
automatizados, assim como as próprias ferramentas de CI/CD (daí a sigla
"CD", certo?) como [o bem
conhecido](https://www.crowdstrike.com/blog/your-jenkins-belongs-to-us-now-abusing-continuous-integration-systems/)
[Jenkins](https://www.csoonline.com/article/3256314/hackers-exploit-jenkins-servers-make-3-million-by-mining-monero.html)
ou ferramentas de terceiros como Circle-CI, Semaphore e outros.


# Qualidade

Esse tópico emenda um pouco com o anterior, já que a primeira etapa na
configuração de uma arquitetura que faça uso de alguma ferramenta de CI/CD
é o uso de **pre-commit hooks** do `git`.


Há mais nesse mundo do que testes unitários. **A presença de credenciais
nos repositórios** [deve ser evitada ao
máximo](https://12factor.net/config), é o tipo de coisa que precisa ser
verificada **antes** que alterações vão, de fato, para o repositório
(afinal, costuma ser bem chato corrigir esse tipo de problema).

**Excessos de [complexidade
ciclomática](https://pt.wikipedia.org/wiki/Complexidade_ciclom%C3%A1tica)**
também são capturados, idealmente, na fase de *pre-commit*.


Eu escrevi um pouco a respeito disso e outras regras nessa página:

[https://cleber.netlify.com/clebercaverna/#cl%C3%A9ber/CTO/diretrizes/](https://cleber.netlify.com/clebercaverna/#cl%C3%A9ber/CTO/diretrizes/)


O frontend, como eu disse anteriormente, não tem testes.

Já o backend tem cobertura de **100%** em tudo o que não é *boilerplate*
(essas outras partes seriam testadas durante os *testes de integração*, já
que são responsáveis, principalmente, por gerenciar a conexão ao roteador
WAMP).

Para rodar os testes:

    $ PYTHONPATH=. pytest

Os resultados ficarão salvos em HTML no diretório `htmlcov`.


# Arquitetura

A experiência faz com que comecemos a acreditar em certas coisas que, para
os mais jovens, soam absurdas demais. [Postgres também
é NoSQL](https://blog.joshsoftware.com/2018/02/04/postgres-a-new-nosql/).
[MongoDB não
é o futuro](https://blog.shippable.com/why-we-moved-from-nosql-mongodb-to-postgressql).
[Produtos caros não são necessariamente
melhores](https://matt.sh/anatomy-of-a-fraud). E por aí vai.

Recentemente adicionei outros dois itens à lista:

* HTTP is overrated.
* AWS Lambda não escala infinitamente.

Mas não me entendam mal. Não é como se eu não gostasse do protocolo HTTP
ou [não entendesse muito de APIs
HTTP/REST](https://medium.com/clebertech/o-guia-definitivo-para-constru%C3%A7%C3%A3o-de-apis-rest-470d0c885fe1).
Acontece, na verdade, é que de tanto desenhar, implementar e usar APIs
HTTP/REST, acabei percebendo que, no fim das contas, **tudo não passa de
uma forma de RPC**.


Por isso decidi implementar uma arquitetura um tanto "heterodoxa". Achei
que seria, no mínimo, uma oportunidade de aprendizado para quem tiver
contato com esse repositório.


Um exemplo de arquiteturas "ortodoxa", pelo que entendo, seria aquela
pilha completamente servida via AWS:

* Frontend servido via S3.
* API passando pelo API Gateway.
* Mensagens trafegando via SNS/SQS.
* Funções Lambda sempre que possível.
* Máquinas EC2 (diretamente ou via ECS) com o devido *load balance*.
* Alguns dados salvos no DynamoDB, outros em bancos relacionais (RDS).

Tal arquitetura é vista como uma espécie de ideal e não nego que seja, de
fato, bem interessante. Mas ela surge na mentalidade comum dos
desenvolvedores e arquitetos como uma espécie de "santo graal da
infraestrutura" e isso é um problema, já que essa imagem é criada a partir
de equívocos (ou até falácias) comuns.

"*Aguenta milhões de usuário simultâneos*", **mas a que preço**? Seu
produto realmente contempla a possibilidade de conseguir milhões de
usuários simultâneos dentro dos próximos cinco anos?

"*Em geral, sai muito mais barato*", **mas sob qual aspecto**? Já ouvi
falar que "[o tempo mais caro é o tempo do
programador](https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/)"?

"*É mais fácil achar profissionais capacitados*", mas você acha que
o desenvolvedor dedicado usa uma pilha assim em seus **[projetos
pessoais](https://thecurlybrace.blogspot.com/2010/11/importance-of-pet-projects.html)**?

"*É a solução mais escalável*", **baseado em que dados**? No fim das
contas, trazemos na mente muitos conceitos contados pelos próprios
vendedores de soluções, não é?


## Crossbar e WAMP

A arquitetura que propus baseia-se num roteador WAMP chamado
[Crossbar](https://crossbar.io/). Ele serve, principalmente, para
trabalhar com **pub/sub** e **RPCs**.

A ideia é que cada componente conecte-se com o roteador e possa, assim,
trabalhar como uma verdadeira arquitetura de microsserviços.

As chamadas de RPCs, por exemplo, são feitas sem preocupação a respeito de
**qual componente** há de ser, efetivamente, chamado, o que é, de certa
forma, análogo ao *fire and forget* das mensagens nas [Arquiteturas
Baseadas em Eventos](https://slides.com/cleberz/eda-1).

O roteador em si é baseado num *loop de eventos* e permite que várias
espécies de componentes conversem entre si: backend, frontend, sensores,
atuadores, etc, nas mais variadas linguagens (C#, JS, Python, C++...).


É **fantástico** ter à mão, de maneira simples, todas essas
funcionalidades. A autenticação é feita na conexão ao invés de ficar-se
enviando tokens de API a cada requisição. Os erros "explodem" de maneira
nativa ao invés de ficar-se verificando *status codes*. Chamar um
"procedimento remoto" é tão simples quanto uma função local. **Reagir
a eventos** requer configuração mínima e flui mui naturalmente.


Como o cadastramento dos nomes dos RPCs e canais é feito **pelas
aplicações** (seguindo regras definidas via configuração do Crossbar,
claro), ganha-se uma possibilidade interessante que é a seguinte: **os
componentes podem rodar de qualquer lugar**.

O desenvolvedor pode fazer testes mui facilmente em sua máquina local e,
do ponto de vista do restante da arquitetura, **não faz a menor
diferença**.

Há algum trabalho constante e pesado que faz com que ter uma instância EC2
dedicada não valha muito a pena? Tudo bem: pode-se rodar um ou mais
componentes **num VPC**. Do ponto de vista do restante da arquitetura,
**não faz a menor diferença também**.


## Heroku e derivados

O Heroku serve como exemplo de PaaS interessante em que é muito, muito
simples colocar-se um componente para rodar. Alguns acham o preço um tanto
salgado, mas eu conheço empresas que fazem uso "agressivo" e não se
arrependem.

O custo maior é o tempo do programador, afinal. Sem contar **a felicidade
geral** de quem não tem que se preocupar com praticamente nada de
"devops".


**Mas**, se o custo é uma preocupação, eu recomendo um meio-termo
progressivo, que começa com o [Dokku](http://dokku.viewdocs.io/dokku/)
rodando sobre instâncias EC2 e progredindo para [Tsuru](https://tsuru.io/)
permitindo não somente o deploy rápido como também **gerenciando a própria
infraestrutura**.

## Método ágil

Metodologias ágeis são definidas **pelo feedback rápido da parte do
usuário final**. Por isso é interessante ter a liberdade de por para rodar
rapidamente componentes da arquitetura, com preocupação menor a respeito
de como esses mesmos componentes estarão rodando "daqui a dois anos".
Primeiro coleta-se o *feedback*, depois "eterniza" os componentes.

No fim das contas, o *feedback* do cliente sempre pode mostrar que vários
componentes foram desnecessários.

E é por isso mesmo que os microsserviços são interessantes: **porque eles
são "micro"**. Eles combinam bem com metodologias ágeis porque são
geralmente pequenos (pouquíssimas linhas de código), fáceis de serem
modificados, substituídos ou aposentados (e depurar código muito curto
sempre é melhor do que depurar código longo).

## O componente de login

O frontend **esconde** o formulário de login quando a aplicação não está
conectada, via WebSocket, com o roteador WAMP. O motivo é simples: não tem
mesmo como efetuar o login ou criar uma nova conta sem a conexão. **Mas
esse não deve ser o caso para todos os componentes do frontend**,
obviamente.

Idealmente, haveria um *service worker* para permitir que a aplicação
funcione bem, [mesmo desconectada](http://offlinefirst.org/).

## O futuro

Cito rapidamente alguns planos interessantes para o futuro da arquitetura.
Eu poderia escrever exaustivamente sobre cada um deles, mas me parece que
essa leitura já está exaustiva o bastante...

* O Frontend pode continuar no [Netlify](https://www.netlify.com/).
* Adotar o [Flux](https://facebook.github.io/flux/docs/in-depth-overview.html#content).
* Adotar o "[offline first](http://offlinefirst.org/)".
* [Tsuru](https://tsuru.io/) gerenciando infraestrutura e deploys.
* Configurar auto-scale para o Crossbar.
* Criação de ambiente de testes (para testes de integração).
* Testes do frontend com [Cypress](https://www.cypress.io/).
* Criação de ambiente de homologação.
* Instrumentalização (com [Prometheus](https://prometheus.io/), talvez).
* Coleta de exceções ([Sentry](https://sentry.io/) é excelente).
* Centralização de logs ([logentries](https://logentries.com/) é uma boa
  opção. [fluentd](https://www.fluentd.org/) é interessante).

# Resumo

Passei o dia inteiro na frente do computador. Meu cachorro está
implorando, aqui, para eu sair e correr um pouco com ele.

Normalmente eu revisaria bastante esse texto, mas minha mente já não está
mais em condições.

Em resumo, o código do teste, em si, não é a coisa mais linda do mundo.
Mas, se me permitem, não acho que não valha a conversa comigo. :-)
