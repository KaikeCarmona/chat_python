import flet as ft

#função principal
def main(pagina):
    #criar um titulo
    titulo = ft.Text("HashZap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel) #cria o tunel de comunicação

    titulo_janela = ft.Text("Bem vindo ao Chat")
    
    def enviar_mensagem(evento):

        #enviar a mensagem no chat:
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}" 

            #usuario: mensagem

        #enviar uma mensagem no tunel
        pagina.pubsub.send_all(texto)


        #limpar o campo de mensagem
        texto_mensagem.value = ""

        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    #  colunas 
    chat = ft.Column()
    #  linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        #tirar o titulo da pagina
        pagina.remove(titulo)
        #tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        #fechar o popup/janela
        janela.open = False
        #criar o chat
        pagina.add(chat)
        #adicionar a linha de mensagem
        pagina.add(linha_mensagem)

        #escrever a mensagem: o usuario entrou no chat
        texto_entro_chat = f"{campo_nome_usuario.value} entrou no chat" 
        pagina.pubsub.send_all(texto_entro_chat)
        
        pagina.update()
        
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

#executar o sistemma
ft.app(main, view=ft.WEB_BROWSER)