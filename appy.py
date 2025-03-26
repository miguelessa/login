import customtkinter as ctk

# Configuração de aparência
ctk.set_appearance_mode('dark')  # Modo escuro = dark; modo claro = light
ctk.set_default_color_theme('blue')  # Tema de cor

# Função de validação de login
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == 'teste' and senha == '123': # Entre esses apostrofos, coloque o login e senha que quer utilizar. 
        resultado_login.configure(text='Login feito com sucesso!', text_color='green') 
    else:
        resultado_login.configure(text='Login negado!', text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300') # Aqui é o tamanho que sua janela vai abrir. Eu gosto bastante de 200x200 e 300x300. Para o pedido, fica o tamanho ideal. Para apps mais complexos, tamanhos maiores devem ser considerados.

# A partir dessa linha, é a estilização do app (criação do botão, formatação de texto...)

# Usuário
label_usuario = ctk.CTkLabel(app, text='Usuário', anchor="center")
label_usuario.pack(pady=5) # Esse texto 'pady' é a distância que ele fica das bordas do app. Se você colocar em 0, então você terá o texto grudado na borda. Quanto mais aumentar, mais ele desce, se diminuir, ele sobe. Eu, partircularmente, gosto de valores entre 5 e 10 para páginas 300x300, 200x200 e assim vai. Mas é do gosto de cada um.

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário') # Essa parte, é a escrita dentro da caixinha de usuário. 
campo_usuario.pack(pady=5)

# Senha
label_senha = ctk.CTkLabel(app, text='Senha', anchor="center") # Aqui a escrita dentro do campo de senha 
label_senha.pack(pady=5)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show="*")  # Essa parte é ocultar senha. Se você remover o asteristico, ele mostra a senha. Outros valores também são válidos para ocultar a senha.
campo_senha.pack(pady=5)

# Botão de login
botao_login = ctk.CTkButton(app, text='Login', command=validar_login) 
botao_login.pack(pady=10)

# Iniciar a aplicação 
app.mainloop()
