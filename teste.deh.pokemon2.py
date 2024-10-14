import random
# Apresentação do Professor Carvalho e solicitação do nome do jogador
print("Olá! Bem-vindo ao mundo dos Pokémon!")
nome = input("Eu sou o Professor Carvalho. Antes de começarmos, qual é o seu nome? ")
print(f"Ótimo, {nome}! Prepare-se para uma grande aventura!")

# Lista de possíveis Pokémon que podem ser encontrados
pokemonsCa = ['Gengar','Zubat','squirtle']
pokeimgCa = ['''⣿⣿⣿⣿⣿⡇⣬⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⣿⣿⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣦⡛⢈⠛⠙⠿⣛⣩⣥⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠟⢀⣝⡻⢿⣿⢸⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣇⣈⠉⣽⣿⣿⣿⠿⠿⣿⣿⣿
⡇⠼⣿⣿⣶⣌⠈⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⡶⢒⣴
⣿⣧⠹⣿⣿⣿⣾⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿
⣿⣿⣧⠙⣹⣿⣿⡿⢱⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢿⠟⣫⣴⣿⣿⣿⣿
⣿⣿⣿⢰⣿⣿⠹⣧⠻⣇⡘⣿⣿⣿⣿⡿⠟⣩⡄⣿⣿⣿ ⡚⠻⠿⠿⠿⣿⣿
⣿⣿⡇⣾⣿⣿⢰⡜⠳⣦⣥⣿⣿⣟⠩⢤⣿⠟⣰⣿⣿⣿⣸⣿⣿⣿⣿⡦⠜⣻
⣿⣿⡇⢿⣿⣿⣌⢡⣷⡄⣉⣛⠻⠿⠷⠶⠶⠞⢫⣿⣿⡿⣿⣿⠿⢛⣩⣥⣿⣿
⣿⣿⢃⠸⣿⣿⣿⣦⣙⠡⢿⣿⡿⢰⣿⡇⠜⣡⣿⣿⣿⢃⣥⣴⣾⣿⣿⣿⣿⣿
⣿⡏⢸⣦⣿⣿⣿⣿⣿⣿⣶⣦⣥⣭⣥⣶⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡘⢿⣿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣦⠉⠉ ⣝⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣿⣿⣿⣦⡀⠌⣡⣌⢻⣿⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣆⠻⠿⢛⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣄⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⡇⢸⣿⣧⡀⠀⠈⢻⣿⣿⣿⣿⡇⠀⢀⣤⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⢹⣿⣿⡇⢸⣿⣿⣷⡄⠀⠀⠙⣿⣿⣿⠃⠀⣿⣿⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⢸⡿⠛⠛⠿⡄⠀⠀⠘⣿⣿⠀⠀⢿⣛⢸⣿⡟⠋⠻⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠁⠀⢀⣴⣶⣿⣿⣿⣶⣄⠀⠀⢻⣿⢸⢃⣾⣿⣿⡦⠀⠀⠀⠈⠛⠀⠀⣿⣿⠸⠏⠀⠀⠀⢻⣿
⣿⣿⣿⣿⣿⠋⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠻⣇⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠘⣿
⣿⣿⣿⡿⠁⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠋⠀⣀⣤⣄⠀⠹⡌⠻⠋⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠘⠀⠀⠀⣶⣆⠀⣿
⣿⣿⡿⠁⠀⢀⣾⣿⣿⣿⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⣧⡀⠱⡀⠀⠀⠀⠀⠀⢰⣧⣼⣧⠎⠀⠀⠀⠀⣸⣿⣿⠀⣿
⣿⣿⠃⠀⢀⣾⣿⣿⣿⣿⣿⣿⠏⢀⣴⣿⣿⣿⣿⣿⣿⠷⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⡿⡆⠀⠀⠀⢀⣿⣿⣿⠀⢹
⣿⡟⠀⠀⣼⣿⣿⣿⣿⣿⣿⠏⢠⣾⣿⣿⡿⠟⠋⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠛⠀⠁⢀⠀⠀⣸⣿⣿⣿⠀⣾
⣿⠃⠀⣸⣿⣿⣿⣿⣿⣿⠋⣰⣿⡿⠟⠉⠀⢀⣤⡶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⣿⣿⣿⣿⠀⣿
⣿⠀⢠⣿⣿⣿⣿⣿⡿⠃⣰⠟⠋⠀⢀⣤⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⢸⣿⣿⣿⡏⠀⣿
⡟⠀⣼⣿⠿⠟⠛⠛⠁⠀⠁⢀⣴⣾⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡘⢿⠃⠀⣿⣿⣿⣿⠇⢰⣿
⡇⠀⠟⠁⠀⣀⣀⣀⡀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡄⠀⢰⣿⣿⣿⡿⠀⣸⣿
⡇⢀⣤⣶⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢀⣴⣤⣀⡀⠀⠀⢀⣴⣾⣿⣿⣿⡇⠀⠈⠙⣿⣿⠃⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⣴⣿⣿⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣴⣶⣶⡀⢸⠇⢠⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⣴⣿⣿⣿⣿⠏⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣾⣿⣿⣿⣿⡿⠁⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⣴⣾⣿⣿⣿⣿⣿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠟⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣷⣾⣿⣿⣷⣿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⢺⣿⣿⣿⣿⣿⡿⣛⡻⣿⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠘⣿⣿⣿⣿⣿⣿⠁⠙⠁⢸⣿⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⣸⣿⣿⣿⣿⣿⣇⠠⠤⢾⣸⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡻⠿⣛⣛⣛⣛⣻⡿⠿⠿⣛⣿⣿⡞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⡥⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢿⣿⣧⢍⣛⡻⠯⠷⡿⠿⠽⣓⣡⣚⠙⣮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⢿⣿⣽⣿⣿⡿⣵⣿⣿⣿⣿⣿⣷⢯⣾⣿⣿⣿⣷⠠⣕⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⢻⡏⣿⣿⣿⡿⣾⣿⣿⣿⣽⣻⣛⣋⣾⣿⣿⣿⣿⣿⢀⣯⣗⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣛⣛⣾⣟⣟⢃⣿⣿⣿⣿⡇⣿⡿⣻⣷⣞⡿⡿⡿⣣⡗⣾⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡞⣿⣿⣿⣧⣿⣯⣭⣛⠿⣟⣡⣵⣿⡇⣯⠿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢏⣻⣿⣿⣶⣶⣿⣿⣿⣿⣼⢿⣿⡇⣿⡇⡍⡃⣼⣿⣻⣷⣿⣿⣿⣾⡝⣿
⣿⣿⣿⣿⣿⣻⣿⣝⣿⣿⣿⡿⣿⣿⣿⣿⣟⣶⣾⣿⣷⣕⠸⢱⢟⣾⣿⣿⠟⣛⠻⣿⣿⣹
⣿⣿⣿⣿⡟⣿⣿⣿⣮⡛⣿⣥⣟⡿⢿⣏⣾⣿⣿⣿⣿⣿⡄⣵⣿⣿⣿⢡⣿⣿⣿⣿⣿⢸
⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⢪⣽⣿⣛⣟⡂⢿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣽⣦⠻⢿⡿⡷⣫⣿
⣿⣿⣿⣯⠻⡟⣿⠿⣋⣯⣿⣿⣿⣿⣿⣿⣯⢿⣿⣿⣿⣿⡗⣾⣭⣽⣯⣿⣿⣦⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣟⢿⡿⢞⡷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''']

pokemonsMa = ['Bellsprout','Lugia','pikachu']
pokeimgMa = ['''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣴⣿⡆⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠈⠉⠀⠀⠀⠀⠸⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰
⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿
⣿⡿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⠋⢠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡾⠿⣿⣿⣿
⠀⢸⡏⠀⠈⠛⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣿⣿⣿⠋⠁⠀⠀⣿⣿⣿
⣇⠈⢿⣆⠀⠀⠀⠙⢿⣆⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣿⣿⣿
⣿⣧⡀⠻⣷⣄⠀⠀⠀⠻⣧⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣾⣿⣿⣿
⣿⣿⣿⣦⡈⠛⢷⣦⣀⣀⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⣈⠉⠉⠉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣻⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⠻⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣻⠇⠀⠀⠈⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⢿⣷⣄⡀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠙⠊⢛⡀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠈⠻⡟⠀⠀⢠⣄⣸⠟⢁⣿⣿⣿⡟⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠳⢤⠠⠀⠀⠘⠓⠤⡖⠋⣹⣿⣿⡇⠸⡟⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠖⠁⠀⠀⠀⠀⠀⠀⠈⠋⢤⣿⣿⡿⠁⣧⣾⣿⣿
⣿⣿⣿⣿⣿⠟⠁⠀⣠⡄⡀⠀⠀⣴⣶⣶⡀⠀⠈⠫⡀⣸⣿⣿⣿⣿
⣿⣿⣿⡿⠃⠀⠀⣰⣿⢿⣿⣷⣾⣿⣿⣿⠟⢆⠀⠀⠈⠻⣿⣿⣿⣿
⣿⣿⠟⠀⠀⠀⢠⣿⣿⡀⠻⣿⣿⣿⣿⣋⡀⢈⡆⠀⠀⠀⠈⢻⣿⣿
⣿⡏⠀⠀⠀⠀⢸⣿⣿⣿⣶⠀⢱⣶⣤⣤⣄⣀⡷⠀⠀⠀⠀⠀⢻⣿
⣿⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⣿
⢿⠀⠀⢠⠀⢰⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡀⣼⠀⠀⡀⠀⠀⣥
⣿⣀⠀⢸⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣇⣀⣷⣿
⣿⣿⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⠏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿
⣿⣿⣿⣿⡿⣾⣿⣸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣛⣿⣭⠉⠉⣹⣿⣿⡿⣫⣾⡟⣿
⣿⣿⣿⣿⣧⡿⣃⣛⣿⣿⣿⣻⢟⣯⣷⣿⣿⣿⣿⢏⣠⣾⣿⡿⣫⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡣⢾⣿⣿⣿⠩⠙⣿⣿⣛⠛⣻⣯⣽⣾⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⢸
⣿⣿⣿⢇⣈⡾⢿⡿⢿⣷⡶⣛⡻⣿⣷⢿⣿⣿⣿⣿⠫⢾⣻⣻⣿⣿⡿⣟⣽⣾
⣿⣿⡟⡄⣿⣆⠀⣀⢸⣿⣞⣫⣣⣿⣿⡾⣿⣿⣿⣿⡞⣿⣿⡿⣻⣵⣾⣿⣿⣿
⣿⣿⣿⣔⢿⣿⣯⣛⣼⣿⣿⣿⣿⡿⣿⣿⡽⣿⣿⣿⣿⡼⣿⣇⣿⣿⣿⣿⣿⣿
⡿⣟⣯⣽⣶⣝⣿⢿⣿⣿⣿⣿⣩⣶⣶⣿⣿⡘⢿⣿⢟⣭⣿⢟⣿⣿⣿⣿⣿⣿
⡇⢧⣿⣿⣿⣿⡝⣷⣽⣿⣿⣿⣧⡛⠻⠛⣻⣿⣷⡵⣝⠟⠱⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣭⣭⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣨⠁⣀⣹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿⣿⠿⠿⣿⣿⡿⠿⢿⣛⡵⣹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⡛⠚⣭⣶⣶⣮⣽⣟⣛⢛⡅⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡤⣿⣿⣿⣿⣿⣿⣿⣯⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿''']

import random

Pokemons_Pokedex = []
tentativas_extra = 3
escolha = ""

# Loop principal do jogo
while escolha != "sair":
    escolha = input("\nOnde você gostaria de explorar? (caverna/matagal/pokedex/sair) ").lower()
    print(f"Você tem {tentativas_extra} chances para capturar um Pokémon.")

    if escolha == "caverna":
        print("Você entrou na caverna...")
        pokemon_dataCa = random.choice(list(zip(pokemonsCa, pokeimgCa))) if random.randint(1, 10) == 1 else (None, None)
        pokemon, pokemon_img = pokemon_dataCa

        if pokemon is not None:
            if pokemon not in Pokemons_Pokedex:
                print(f"Você encontrou um {pokemon} na caverna!\n{pokemon_img}")
                capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                if capturar == "sim":
                    probabilidade_captura = 0.75  # Probabilidade de captura na caverna
                    if random.random() <= probabilidade_captura:
                        print(f"Parabéns! Você conseguiu capturar o {pokemon}! Ele foi adicionado à sua Pokédex!")
                        Pokemons_Pokedex.append(pokemon)
                    else:
                        tentativas_extra -= 1
                        print(f"Oops! Você não conseguiu capturar o {pokemon}. Tentativas restantes: {tentativas_extra}")
            else:
                print(f"Você já capturou um {pokemon}.")
        else:
            print("Você não encontrou nenhum Pokémon na caverna desta vez.")

    elif escolha == "matagal":
        print("Você entrou no matagal...")
        pokemon_dataMa = random.choice(list(zip(pokemonsMa, pokeimgMa)))
        pokemon, pokemon_img = pokemon_dataMa
        
        if random.randint(1, 2) == 1:
            print(f"Você encontrou um {pokemon} no matagal!\n{pokemon_img}")
            if pokemon not in Pokemons_Pokedex:
                capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                if capturar == "sim":
                    probabilidade_captura = 0.6  # Probabilidade de captura no matagal
                    if random.random() <= probabilidade_captura:
                        print(f"Parabéns! Você capturou o {pokemon}!")
                        Pokemons_Pokedex.append(pokemon)
                    else:
                        if tentativas_extra > 0:
                            tentativas_extra -= 1
                            print(f"Oops! Você não conseguiu capturar o {pokemon}. Tentativas restantes: {tentativas_extra}")
                        else:
                            print("Você usou todas as suas tentativas extras de captura.")
            else:
                print(f"Você já capturou um {pokemon}.")
        else:
            print("Você não encontrou nenhum Pokémon no matagal desta vez.")

    elif escolha == "pokedex":
        if Pokemons_Pokedex:
            print("Pokédex:")
            for poke in Pokemons_Pokedex:
                print(f"- {poke}")
        else:
            print("Sua Pokédex está vazia!")

    elif escolha == "sair":
        print("Obrigado por jogar! Até a próxima!")
        break

    else:
        print("Escolha inválida. Tente novamente.")
