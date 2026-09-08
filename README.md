# Projeto Chamados

## Objetivos

Esse projeto simula uma situação da rotina de trabalhadores: A abertura de um chamado.
Ele está sendo exatamente para testar meus conhecimentos em programação e banco de dados e até onde eu conseguiria ir com as habilidades atuais. Conforme for desenvolvendo, vou aprendendo junto com esse projeto inicial.

## Linguagem de Programação

Nesse projeto estou usando Python, junto com os Frameworks Flask e SQLAlchemy (Banco em SQLite).
Como o projeto é em web, usarei JavaScript junto com HTML e CSS para marcação e estilização do site.

## Como funciona o projeto

A lógica do projeto consiste em contas com permissões diferentes. A página inicial será a página de login e, dependendo das autorizações, será direcionado para o respectivo Dashboard.

A princípio terão 3 tipos de usuários diferentes: os usuários comuns, os agentes de TI e os Gerentes.

### Usuário comum
Ele será o usuário que criará o chamado.
Assim que efetuar o login, será direcionado ao Dashboard que terá as opções de visualizar os próprios chamados e abrir um novo chamado.
Nesse sistema, o usuário apenas precisará preencher as observações, ou seja, o problema do usuário. Os outros dados serão pegos de forma automático quando o usuario enviar o chamado. Sendo os dados: Data e hora, nome, setor e ID do chamado.
O chamado será enviado para um banco de dados.

### Agente de TI
Ele será o responsável por administrar os chamados.
Assim que efetuar o login, será direcionado ao Dashboard que terá as opções de ver chamados pendentes e ver os chamados em andamento pelo próprio usuário.
Escolhendo o chamado ele poderá administrar conforme for resolvendo o processo e adicionando observações. ELe que será responsável pelo chamado.
O chamado é procurado no banco de dados e fornece para ele os dados necessários.

### Gerente
Ele será responsável pela criação dos perfis dentro do sistema. Ele criará e dará as autorizações conforme a contratação ou alocação dos funcionários, não precisando da ajuda do TI para adicionar novos usuários.
Os usuários são todos adicionados em um banco de dados e suas senhas salvas por um hash e salt para a segurança.

## Agradecimentos

Agradeço a todos que visualizaram meu projeto!
Qualquer sugestão ou crítica, estarei ouvindo e aprendendo.
