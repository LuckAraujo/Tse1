import sqlite3
from sqlite3 import Error

########Listagem de Palavras##########3
Temas=['Cores','Animais','Objetos','Paises','Programas De TV']
Cores = [
    "vermelho", "verde", "azul", "amarelo", "roxo", "laranja", "rosa", "marrom", "cinza",
    "preto", "branco", "turquesa", "dourado", "prata", "bronze", "bege", "coral",
    "índigo", "ciano", "magenta", "lilás", "safira", "ouro rosa", "verde limão", "pêssego",
    "jade", "marfim", "tijolo", "malva", "carvão", "azul celeste", "vermelho escarlate",
    "verde-oliva", "vinho", "violeta", "azul marinho", "azul-turquesa", "cereja", "caramelo",
    "mostarda", "topázio", "verde-água", "coral claro", "azul royal", "lavanda", "chumbo",
    "rosa choque", "terracota", "azul-petróleo", "salmão"
]


Animais = [
    "Leão", "Elefante", "Girafa", "Tubarão", "Pinguim", "Gorila", "Tigre", "Tartaruga", "Águia", "Polvo", 
    "Canguru", "Cobra", "Panda", "Camaleão", "Jacaré", "Zebra", "Rinoceronte", "Hipopótamo", "Lobo", "Orca", 
    "Alce", "Guepardo", "Leopardo", "Suricata", "Foca", "Arara", "Papagaio", "Urso polar", "Esquilo", "Texugo", 
    "Panda-vermelho", "Lêmure", "Coala", "Porco-espinho", "Chimpanzé", "Morsa", "Golfinho", "Raposa", "Toupeira", 
    "Baleia", "Lontra", "Castor", "Gato selvagem", "Puma", "Gambá"
]



Objetos = [
    "Carro", "Avião", "Bicicleta", "Televisão", "Computador", "Sofá", "Celular", "Mesa", "Cadeira", "Relógio",
    "Óculos", "Câmera", "Guitarra", "Livro", "Bola", "Barco", "Fogão", "Geladeira", "Forno", "Laptop", "Microfone",
    "Rádio", "Violino", "Teclado", "Mochila", "Faca", "Garfo", "Colher", "Liquidificador", "Ventilador", "Lâmpada",
    "Escova de dentes", "Secador de cabelo", "Cama", "Travesseiro", "Piano", "Tablet", "Binóculos", "Microscópio",
    "Telescópio", "Skate", "Patins", "Máquina de lavar roupa"
]

Paises = [
    "Estados Unidos", "Canadá", "Brasil", "França", "Japão", "Austrália", "Alemanha", "Espanha", "Rússia",
    "China", "Índia", "México", "Argentina", "Itália", "Reino Unido", "África do Sul", "Canadá", "Suíça", "Suécia",
    "Noruega", "Holanda", "Bélgica", "Dinamarca", "Portugal", "Grécia", "Turquia", "Irlanda", "Áustria", "Polônia",
    "Hungria", "Chile", "Colômbia", "Peru", "Venezuela", "Uruguai", "Nova Zelândia", "Singapura", "Malásia",
    "Tailândia", "Filipinas", "Vietnã", "Coreia do Sul", "Arábia Saudita", "Emirados Árabes Unidos", "Egito",
    "Nigéria", "África do Sul"
]

Programas_Tv = [
    "Friends", "Game of Thrones", "Breaking Bad", "The Simpsons", "Stranger Things",
    "The Office", "The Crown", "The Mandalorian", "Black Mirror", "House of Cards",
    "Westworld", "Vikings", "The Witcher", "The Walking Dead",
    "Sherlock", "Peaky Blinders", "Narcos", "Mindhunter", "Fargo", "Chernobyl", "The Expanse",
    "Better Call Saul", "The Handmaid's Tale", "Lost", "The Sopranos", "The West Wing",
    "The X-Files", "Doctor Who", "Dexter", "Homeland", "The Blacklist", "Prison Break",
    "Suits", "The Good Place", "Stranger Things", "The Haunting of Hill House",
    "The Umbrella Academy", "The Boys", "Supernatural", "Rick and Morty",
    "The Marvelous Mrs. Maisel", "Bridgerton", "Money Heist", "The Queen's Gambit",
    "Dark", "O Mecanismo", "Narcos: Mexico", "A Grande Família", "Toma Lá, Dá Cá",
    "Avenida Brasil", "Cidade dos Homens", "Sob Pressão", "O Auto da Compadecida"
]



#Função para conectar no banco de dados#######
def conecta():
    try:
        con = sqlite3.connect('banco7.db')
        #print('Conexão estabelecida com sucesso!')
        return con
    except Error as er:
        print('Erro durante a conexão.')

#######SQL Das Tabelas#################
sql_criar_temas = '''CREATE TABLE temas(
    "tem_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "tem_nome" VARCHAR(100) NOT NULL
);'''

sql_criar_palavra = '''CREATE TABLE palavras (
    "pal_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "tem_id_fk" INTEGER NOT NULL,
    "pal_palavra" VARCHAR(100) NOT NULL,
    "pal_dificuldade" VARCHAR NOT NULL,
    FOREIGN KEY ("tem_id_fk") REFERENCES temas("tem_id")
);'''
sql_criar_jogadores = '''CREATE TABLE jogadores (
    "id_jogador" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "jog_nome" INTEGER NOT NULL,
    "jog_email" VARCHAR(250) NOT NULL,
    "jog_senha" VARCHAR(100) NOT NULL,
    "jog_pontuacao" VARCHAR NOT NULL
);'''

#######Funções do SQL#######
def criar_tabela(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def listar(sql):
    con = conecta()
    cursor = con.cursor() #Objeto que permite executar SQL
    cursor.execute(sql)
    resultado = cursor.fetchall() #carrega todos os dados em resultado
    for i in resultado:
       print(i)
    con.close()
    
def inserir(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
####################Criar Tabelas################
criar_tabela(sql_criar_temas)
criar_tabela(sql_criar_palavra)
criar_tabela(sql_criar_jogadores)
############INSERTS DE NAS TABELAS###############
for i in Temas:
    sql_inserir_Temas = f"INSERT INTO temas VALUES (NULL,'{i}');"
    inserir(sql_inserir_Temas)

for i in Cores:
    n=1
    lista=[]
    for letra in i:
        lista.append(letra)
    if len(lista)>=1 and len(lista)<=5:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Facil');"
    elif len(lista)>5 and len(lista)<=7:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Media');"
    else:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Dificil');"
    lista.clear()
    inserir(sql_inserir_Palavra)

for i in Animais:
    n=2
    lista=[]
    for letra in i:
        lista.append(letra)
    if len(lista)>=1 and len(lista)<=5:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Facil');"
    elif len(lista)>5 and len(lista)<=7:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Media');"
    else:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Dificil');"
    lista.clear()
    inserir(sql_inserir_Palavra)
for i in Objetos:
    n=3
    lista=[]
    for letra in i:
        lista.append(letra)
    if len(lista)>=1 and len(lista)<=5:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Facil');"
    elif len(lista)>5 and len(lista)<=7:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Media');"
    else:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Dificil');"
    lista.clear()
    inserir(sql_inserir_Palavra)
for i in Paises:
    n=4
    lista=[]
    for letra in i:
        lista.append(letra)
    if len(lista)>=1 and len(lista)<=5:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Facil');"
    elif len(lista)>5 and len(lista)<=7:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Media');"
    else:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Dificil');"
    lista.clear()
    inserir(sql_inserir_Palavra)
for i in Programas_Tv:
    n=5
    lista=[]
    for letra in i:
        lista.append(letra)
    if len(lista)>=1 and len(lista)<=5:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Facil');"
    elif len(lista)>5 and len(lista)<=7:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Media');"
    else:
        sql_inserir_Palavra = f"INSERT INTO palavras VALUES (NULL,{n},'{i}','Dificil');"
    lista.clear()
    inserir(sql_inserir_Palavra)