import tkinter as tk
import winsound
import random as r

# Funções relacionadas com o mapa ----------------------------------------
def ler_mapa(nome_ficheiro): #função usada para ler o mapa do jogo
    mapa = []
    with open(nome_ficheiro, "r", encoding="utf-8") as mapas:
        for linha in mapas:
            elemento = linha.strip().split()
            mapa.append(elemento)
    return mapa

def mostra_mapa(texto_widget): #função que mostra o mapa na tela
    mapa = ler_mapa("mapa.txt")
    texto_widget.delete('1.0', tk.END)
    for linha in mapa:
        linha_str = " ".join(linha)
        texto_widget.insert(tk.END, linha_str + "\n")

def mostrar_mapa_codificado(texto_widget): # função que mostra o mapa num formato diferente , substituindo os . e # por ~ e X
    mapa = ler_mapa("mapa.txt")
    texto_widget.delete("1.0", tk.END)
    for linha in mapa:
        nova = ["~" if c == "." else "X" if c == "#" else c for c in linha]
        texto_widget.insert(tk.END, " ".join(nova) + "\n")

def mostrar_obstaculos(texto_widget): #função que permite mostrar as posições de onde os obstaculos estao posicionados
    mapa = ler_mapa("mapa.txt")
    texto_widget.delete("1.0", tk.END)
    total = 0
    for i, linha in enumerate(mapa):
        for j, c in enumerate(linha):
            if c == "#":
                texto_widget.insert(tk.END, f"Obstaculo na posicao ({i},{j})\n")
                total += 1
    texto_widget.insert(tk.END, f"\nTotal de obstaculos: {total}")

def mostra_mapa_pag():
    janela_mapa = tk.Toplevel()
    janela_mapa.geometry("800x800")
    janela_mapa.title("Mapa de jogo")

    texto = tk.Text(janela_mapa, width=100, height=40)
    texto.pack()

    tk.Button(janela_mapa, text="Mostrar mapa original", command=lambda: mostra_mapa(texto)).pack()
    tk.Button(janela_mapa, text="Mostrar mapa codificado", command=lambda: mostrar_mapa_codificado(texto)).pack()
    tk.Button(janela_mapa, text="Mostrar obstáculos", command=lambda: mostrar_obstaculos(texto)).pack()
    tk.Button(janela_mapa, text="Sair", command=janela_mapa.destroy).pack()

def desenhar_grelha(frame_func):  #funçãao que permite mostrar a grelha na tela com as cores verde para os blocos sem obstaculos e vermelho para as que tem obstaculos
    mapa = ler_mapa("mapa.txt")
    for i in range(10):
        for j in range(10):
            cor = "green" if mapa[i][j] == "." else "red"
            lbl = tk.Label(frame_func, width=2, height=1, bg=cor,
            relief="solid", borderwidth=1)
            lbl.grid(row=i, column=j, padx=1, pady=1)

def ver_mapagrafico(): #função usada para construir a janela onde a função anterior vaai exibir o mapa
    mapa = ler_mapa("mapa.txt")
    janela_grafico = tk.Toplevel()
    janela_grafico.geometry("800x800")
    janela_grafico.title("Mapa de grafico")
    frame_mapa = tk.Frame(janela_grafico)
    frame_mapa.pack()
    tk.Button(janela_grafico,text="ver janela grafica", command=lambda : desenhar_grelha(frame_mapa)).pack()
    tk.Button(janela_grafico, text="Sair", command=janela_grafico.destroy).pack()

def percorrer_mapa(): #esta função e usada para construir a janela onde e possivel jogar o jogo
    janela_jogo = tk.Toplevel()
    janela_jogo.geometry("800x800")
    janela_jogo.title("Jogo")

    frame_mapa = tk.Frame(janela_jogo)
    frame_mapa.pack()

    texto_tempo = tk.Label(janela_jogo, text="Tempo: 0s", font=("Arial", 14))
    texto_tempo.pack(pady=5)

    texto_cliques = tk.Label(janela_jogo, text="Cliques: 0", font=("Arial", 14))
    texto_cliques.pack(pady=5)

    entrada_linhas = tk.Entry(janela_jogo, width=5)
    entrada_colunas = tk.Entry(janela_jogo, width=5)
    entrada_linhas.insert(0, "10")
    entrada_colunas.insert(0, "10")
    tk.Label(janela_jogo, text="Linhas:").pack()
    entrada_linhas.pack()
    tk.Label(janela_jogo, text="Colunas:").pack()
    entrada_colunas.pack()

    estado = {"modo": "editar", "inicio": None, "fim": None, "jogando": False, "pos_jogador": None, "contador": 0}
    mapa = ler_mapa("mapa.txt")
    labels = []
    tempo_segundos = [0]
    timer_id = [None]

    def atualizar_tempo(): #função usada para ir atualizando o tempo a medida que o jogo corre
        tempo_segundos[0] += 1
        texto_tempo.config(text=f"Tempo: {tempo_segundos[0]}s")
        timer_id[0] = janela_jogo.after(1000, atualizar_tempo)

    def parar_tempo(): #função usada para parar o contador da função de cima
        if timer_id[0]:
            janela_jogo.after_cancel(timer_id[0])
            timer_id[0] = None

    def alternar_celula(i, j): #função que permite manipular as celulas que seja tirar obstaculos o coloca-los
        if mapa[i][j] == ".":
            mapa[i][j] = "#"
            labels[i][j].config(bg="red")
        else:
            mapa[i][j] = "."
            labels[i][j].config(bg="green")

    def limpar_mapa(): #função que permite colocar o mapa sem obstaculos para depois ser manipulado pelo utilizsdor
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                mapa[i][j] = "."
                labels[i][j].config(bg="green")

    def clicar(i, j): #função usada para que o utilizador consiga andar pela grelha
        cores = ["gray", "black", "darkblue", "yellow", "pink", "purple"]
        if estado["modo"] == "editar":
            alternar_celula(i, j)
            return

        if estado["modo"] == "definir":
            if mapa[i][j] == "#":
                return
            if estado["inicio"] is None:
                estado["inicio"] = (i, j)
                labels[i][j].config(bg="blue")
                winsound.Beep(600, 100) #usado para que o o andar seja emitido um som de bip
                estado["pos_jogador"] = (i, j)
            elif estado["fim"] is None:
                estado["fim"] = (i, j)
                labels[i][j].config(bg="orange")
                estado["modo"] = "espera"
                winsound.Beep(600, 100)

        elif estado["modo"] == "jogar" and estado["jogando"]:
            if abs(i - estado["pos_jogador"][0]) + abs(j - estado["pos_jogador"][1]) == 1 and mapa[i][j] == ".":
                labels[estado["pos_jogador"][0]][estado["pos_jogador"][1]].config(bg="lightblue")
                estado["pos_jogador"] = (i, j)
                labels[i][j].config(bg=r.choice(cores))
                winsound.Beep(600, 100)
                estado["contador"] += 1 #usado para contar os passos que o utilizador da
                texto_cliques.config(text=f"Cliques: {estado['contador']}")

    for i in range(10):
        linha = []
        for j in range(10):
            cor = "green" if mapa[i][j] == "." else "red"
            lbl = tk.Label(frame_mapa, width=2, height=1, bg=cor, relief="solid", borderwidth=1)
            lbl.grid(row=i, column=j, padx=1, pady=1)
            lbl.bind("<Button-1>", lambda e, x=i, y=j: clicar(x, y))
            linha.append(lbl)
        labels.append(linha)

    def ativar_edicao(): #usado para editar a grelha
        estado["modo"] = "editar"

    def ativar_definicao(): #permite definir a ação que estamos a fazer seja editar jogar etc
        estado["modo"] = "definir"
        estado["inicio"] = None
        estado["fim"] = None

    def comecar_jogo(): #usado para começar o jogo
        if estado["inicio"] and estado["fim"]:
            estado["modo"] = "jogar"
            estado["jogando"] = True
            estado["pos_jogador"] = estado["inicio"]
            atualizar_tempo()

    def reiniciar(): #usada para dar reestart ao jogo
        for i in range(10):
            for j in range(10):
                if mapa[i][j] == ".":
                    labels[i][j].config(bg="green")
                else:
                    labels[i][j].config(bg="red")
        estado["inicio"] = None
        estado["fim"] = None
        estado["pos_jogador"] = None
        estado["modo"] = "editar"
        estado["jogando"] = False
        estado["contador"] = 0
        texto_cliques.config(text="Cliques: 0")
        tempo_segundos[0] = 0
        texto_tempo.config(text="Tempo: 0s")
        parar_tempo()

    def redimensionar_mapa(): #usada para permitir redimensionar o papa para um formato que o utiliador deseje
        try:
            linhas = int(entrada_linhas.get())
            colunas = int(entrada_colunas.get())
        except ValueError:
            print("Insira números válidos para os campos.")
            return

        nonlocal mapa, labels
        for widget in frame_mapa.winfo_children():
            widget.destroy()

        mapa = [["." for _ in range(colunas)] for _ in range(linhas)]
        labels = []

        for i in range(linhas):
            linha = []
            for j in range(colunas):
                lbl = tk.Label(frame_mapa, width=2, height=1, bg="green", relief="solid", borderwidth=1)
                lbl.grid(row=i, column=j, padx=1, pady=1)
                lbl.bind("<Button-1>", lambda e, x=i, y=j: clicar(x, y))
                linha.append(lbl)
            labels.append(linha)

        reiniciar()

    def muda_fundo(): #usada para mudar o fundo da tela para uma cor random
        cores = ["red", "green", "blue", "black", "white"]
        posicao = r.choice(cores)
        janela_jogo.config(bg=posicao)

    botoes_frame = tk.Frame(janela_jogo)
    botoes_frame.pack(pady=10)

    tk.Button(botoes_frame, text="Modo Edição", command=ativar_edicao).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Definir Início/Fim", command=ativar_definicao).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Começar Jogo", command=comecar_jogo).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Parar Tempo", command=parar_tempo).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Reiniciar", command=reiniciar).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Sair", command=janela_jogo.destroy).pack(side=tk.LEFT)
    tk.Button(botoes_frame, text="Limpar Mapa", command=limpar_mapa).pack(side=tk.LEFT)
    tk.Button(janela_jogo, text="Redimensionar Mapa", command=redimensionar_mapa).pack(pady=5)
    tk.Button(janela_jogo, text="Mudar Fundo", command=muda_fundo).pack(pady=5)

# janela principal ---------------------------------------------------------------------------------------------
janela_menu = tk.Tk()
janela_menu.geometry("800x800")
janela_menu.title("Menu Inicial")

tk.Label(janela_menu, text="Escolha a opção que pretende").pack()
tk.Button(janela_menu, text="Ver mapa", command=mostra_mapa_pag).pack()
tk.Button(janela_menu, text="Ver mapa colorido", command=ver_mapagrafico).pack()
tk.Button(janela_menu, text="Percorrer mapa", command=percorrer_mapa).pack()

janela_menu.mainloop()
