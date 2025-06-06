import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

# # def recupera_imagem(id):
# #     for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
# #         if f'capa{id}' in nome_arquivo:
# #             return nome_arquivo

#     return 'capa_padrao.jpg'
def deleta_arquivo(id):
    nome_arquivo = f'capa{id}.jpg'
    caminho = os.path.join(app.config['UPLOAD_PATH'], nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)