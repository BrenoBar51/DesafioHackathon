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

			# Declara alguns valores predeterminados no calculo
			tipos = {
				"Front-End": 1,
				"Back-End": 1.4,
				"FullStack": 1.8
			}

			urgencia = {
				"Baixa": 1,
				"Média": 1.5,
				"Alta": 2
			}

			# Cria os elementos do formulário na nova janela
			form_frame = ctk.CTkFrame(new_window)
			form_frame.pack(padx=10, pady=10)

			# Dropdowns
			valor_hora_label = ctk.CTkLabel(form_frame, text="Valor da hora trabalhada(R$)(A média é de R$25h):")
			valor_hora_label.pack(pady=5)
			valor_hora_entry = ctk.CTkEntry(form_frame)
			valor_hora_entry.pack(pady=5)

			dias_da_semana_trabalhados_label = ctk.CTkLabel(form_frame, text="Dias da semana trabalhados:")
			dias_da_semana_trabalhados_label.pack(pady=5)
			dias_da_semana_trabalhados_entry = ctk.CTkEntry(form_frame)
			dias_da_semana_trabalhados_entry.pack(pady=5)

			pessoas_label = ctk.CTkLabel(form_frame, text="Número de Pessoas:")
			pessoas_label.pack(pady=5)
			pessoas_entry = ctk.CTkEntry(form_frame)
			pessoas_entry.pack(pady=5)

			tipo_label = ctk.CTkLabel(form_frame, text="Tipo de Desenvolvimento:")
			tipo_label.pack(pady=5)
			tipo_dropdown = ctk.CTkComboBox(form_frame, values=list(tipos.keys()))
			tipo_dropdown.pack(pady=5)

			prazo_label = ctk.CTkLabel(form_frame, text="Prazo para entrega do projeto (Semanas):")
			prazo_label.pack(pady=5)
			prazo_entry = ctk.CTkEntry(form_frame)
			prazo_entry.pack(pady=5)

			nivel_urgencia_label = ctk.CTkLabel(form_frame, text="Nível de urgência da entrega:")
			nivel_urgencia_label.pack(pady=5)
			nivel_urgencia_dropdown = ctk.CTkComboBox(form_frame, values=list(urgencia.keys()))
			nivel_urgencia_dropdown.pack(pady=5)

			# Função para calcular o valor
			def calcular_valor():
				try:
					valor_hora = int(valor_hora_entry.get())
					dias_da_semana_trabalhados = int(dias_da_semana_trabalhados_entry.get())
					pessoas = int(pessoas_entry.get())
					tipo_selecionado = tipo_dropdown.get()
					prazo_selecionado = int(prazo_entry.get())
					nivel_urgencia = nivel_urgencia_dropdown.get()

					calculo_hora_por_semana = (valor_hora * 6) * dias_da_semana_trabalhados
					valor_base = calculo_hora_por_semana * pessoas * prazo_selecionado
					valor_final = valor_base * tipos[tipo_selecionado] * urgencia[nivel_urgencia]
					valor_por_pessoa = valor_final / pessoas

					resultado_label.configure(text=f"Valor estimado: R$ {valor_final:.2f}")
					media_label.configure(text=f"Valor por pessoa: R${valor_por_pessoa:.2f}")
				except KeyError:
					tkmb.showerror("Erro, Preencha todos os campos")
			
			# Botão calcular
			calcular_button = ctk.CTkButton(form_frame, text="Calcular", command=calcular_valor)
			calcular_button.pack(pady=5)

			# Rótulo para exibir o resultado
			resultado_label = ctk.CTkLabel(form_frame, text="Valor estimado:")
			resultado_label.pack(pady=5)
			media_label = ctk.CTkLabel(form_frame, text="Valor por pessoa:")
			media_label.pack(pady=5)

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