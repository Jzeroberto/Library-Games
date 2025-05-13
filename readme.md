Biblioteca de Jogos | Aplicação Web

Projeto em Flask para gerenciar uma biblioteca de jogos. Permite autenticação de usuários e operações CRUD completas sobre jogos, com upload de imagem de capa e interface responsiva via Bootstrap.

🧰 Tecnologias Utilizadas:
Flask (Python)

MySQL + SQLAlchemy

WTForms

Flask-Bcrypt

Flask-Login

Bootstrap

📌 Funcionalidades:
Cadastro, edição e remoção de jogos, com upload de imagem.

Login e logout de usuários com senha criptografada.

Interface responsiva usando Bootstrap.

▶️ Como executar:

git clone https://https://github.com/Jzeroberto/Library-Games.git
cd Library-Games
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Configure o banco MySQL e execute:

python app.py
