P1 BD NAO RELACIONAIS

É um Código de CRUD em Python usando a biblioteca "pymongo".
4 Operações básicas de um CRUD:
 =>Create : inserir usuário;
 =>Read : listar usuários;
 =>Update : atualizar usuário pelo "_id";
 =>Delete : remover usuário pelo "_id".

Como executar
1. Extrair "p1bdn.py" para uma pasta onde será executada
2. Instalar o Desktop Docker, disponível em: https://docs.docker.com/desktop/setup/install/windows-install/;
3. Abrir o Desktop Docker;
4. Subir o mongo DB para o Docker com o comando no terminal (via VSCODE ou power shell)"docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root --name atividade-mongo mongo:7"
5. testar se subiu com docker.ps (Deve aparecer o container na porta 27017)
6. Instalar o pymongo pode ser global com: pip install py mongo ou com venv como descrito no item 7.
7. (opcional) Criar venv com o comando no terminal com a pasta do diretório selecionada "python -m venv .venv", rodar a "venv\Scripts\Activate.ps1", então "pip install pymongo"
8. Executar o script;
9. O que ele pode fazer?
 - Cadastra usuários para acessar ao banheiro da Univassouras
 - Lê os usuários cadastrados
 - Deleta usuários cadastrados
 - Atualiza lista de usuários cadastrados
10. Um teste pode ser realizado ao clicar no arquivo ou no terminal.
Obs.:
Pode ser necessário instalar o "pip" caso o "pip" não tenha sido instalado globalmente.