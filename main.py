import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x600")
app.title("Calculadora de Projetos")

def login():
	username = "admin"
	password = "admin"

	#Verifica o login
	if user_entry.get() == username and user_pass.get() == password:
			tkmb.showinfo(title="Login realizado", message="Login realizado")

			# Cria e mostra a nova janela
			new_window = ctk.CTkToplevel(app)
			new_window.title("Calculadora de Projetos")
			new_window.geometry("600x600")

			# Esconde a janela principal
			app.withdraw()

			# Define os valores para cada critério
			prazos = {
				"1 semanas": 1500,
				"2 semanas": 2300,
				"3 semanas": 3100,
				"4 semanas": 3900,
				"5 semanas": 4800,
				"6 semanas": 5700,
				"7 semanas": 6500,
				"8 semanas": 7300,
				"9 semanas": 8100,
				"10 semanas": 8900,
				"11 semanas": 9800,
				"12 semanas": 10600,
				"13 semanas": 11400,
				"14 semanas": 12200,
				"15 semanas": 13000
			}

			pessoas = {
				"1 pessoa": 1,
				"2 pessoas": 1.5,
				"3 pessoas": 2,
				"4 pessoas": 2.5,
				"5 pessoas": 3,
				"6 pessoas": 3.5,
				"7 pessoas": 4,
				"8 pessoas": 4.5,
				"9 pessoas": 5,
				"10 pessoas": 5.5
			}

			tipos = {
				"Frontend": 1,
				"Backend": 1.2,
				"Fullstack": 1.5
			}

			prototipo = {
				"Sim": 1.2,
				"Não": 1.0
			}

			# Cria os elementos do formulário na nova janela
			form_frame = ctk.CTkFrame(new_window)
			form_frame.pack(padx=20, pady=20)

			# Dropdowns
			prazo_label = ctk.CTkLabel(form_frame, text="Prazo:")
			prazo_label.pack(pady=10)
			prazo_dropdown = ctk.CTkComboBox(form_frame, values=list(prazos.keys()))
			prazo_dropdown.pack(pady=10)

			pessoas_label = ctk.CTkLabel(form_frame, text="Número de Pessoas:")
			pessoas_label.pack(pady=10)
			pessoas_dropdown = ctk.CTkComboBox(form_frame, values=list(pessoas.keys()))
			pessoas_dropdown.pack(pady=10)

			tipo_label = ctk.CTkLabel(form_frame, text="Tipo de Desenvolvimento:")
			tipo_label.pack(pady=10)
			tipo_dropdown = ctk.CTkComboBox(form_frame, values=list(tipos.keys()))
			tipo_dropdown.pack(pady=10)

			prototipo_label = ctk.CTkLabel(form_frame, text="Protótipo ? :")
			prototipo_label.pack(pady=10)
			prototipo_dropdown = ctk.CTkComboBox(form_frame, values=list(prototipo.keys()))
			prototipo_dropdown.pack(pady=10)

			# Função para calcular o valor
			def calcular_valor():
				try:
					prazo_selecionado = prazo_dropdown.get()
					pessoas_selecionadas = pessoas_dropdown.get()
					tipo_selecionado = tipo_dropdown.get()
					prototipo_selecionado = prototipo_dropdown.get()

					valor_base = prazos[prazo_selecionado] * pessoas[pessoas_selecionadas]
					valor_final = valor_base * tipos[tipo_selecionado] * prototipo[prototipo_selecionado]
					valor_por_pessoa = valor_final / pessoas[pessoas_selecionadas]

					resultado_label.configure(text=f"Valor estimado: R$ {valor_final:.2f}")
					media_label.configure(text=f"Valor por pessoa: R${valor_por_pessoa:.2f}")
				except KeyError:
					tkmb.showerror("Erro, Preencha todos os campos")
			
			# Botão calcular
			calcular_button = ctk.CTkButton(form_frame, text="Calcular", command=calcular_valor)
			calcular_button.pack(pady=10)

			# Rótulo para exibir o resultado
			resultado_label = ctk.CTkLabel(form_frame, text="Valor estimado:")
			resultado_label.pack(pady=10)
			media_label = ctk.CTkLabel(form_frame, text="Valor por pessoa:")
			media_label.pack(pady=10)

	else:
			tkmb.showwarning(title='Credenciais erradas', message='Verifique seu login e senha')

#Elementos da tela de login
label = ctk.CTkLabel(app,text="Tela inicial") 

label.pack(pady=20) 

frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='App de precificação de projetos') 
label.pack(pady=12,padx=10) 

user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 

button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 

app.mainloop()