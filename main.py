import tkinter as tk
from PIL import ImageTk, Image

entry = None
resultado_label = None
detective_label = None

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)
    
    inversions = inv_left + inv_right + inv_split
    return merged, inversions

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged, inversions

def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

def verificar_inversoes():
    global entry, resultado_label, detective_label
    
    numeros = entry.get()
    numeros = numeros.split()
    numeros = [int(num) for num in numeros]
    
    inversoes = count_inversions(numeros)
    
    resultado_label.config(text=f"Número de inversões: {inversoes}")
    
    if inversoes == 0:
        detective_label.config(text="Essa sequência não possui inversões. O detetive agradece sua colaboração!")
    else:
        detective_label.config(text="Essa sequência possui inversões. O detetive investigará mais a fundo!")

def abrir_janela_principal():
    global janela_inicial, entry, resultado_label, detective_label
    
    janela_inicial.destroy()
    
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Jogo do Detetive")

    # Cria os elementos da interface
    titulo_label = tk.Label(janela, text="Bem-vindo ao caso do Detetive!", font=("Arial", 16))
    instrucao_label = tk.Label(janela, text="Digite uma sequência de números separados por espaços:", font=("Arial", 12))
    entry = tk.Entry(janela, font=("Arial", 12))
    verificar_button = tk.Button(janela, text="Verificar", command=verificar_inversoes, font=("Arial", 12))
    resultado_label = tk.Label(janela, text="", font=("Arial", 12))
    detective_label = tk.Label(janela, text="", font=("Arial", 12))

    # Posiciona os elementos na janela
    titulo_label.pack(pady=10)
    instrucao_label.pack()
    entry.pack(pady=5)
    verificar_button.pack(pady=5)
    resultado_label.pack()
    detective_label.pack(pady=10)

    # Inicia o loop principal da janela
    janela.mainloop()

# Cria a janela inicial
janela_inicial = tk.Tk()
janela_inicial.title("Jogo do Detetive - Início")

# Carrega a imagem do detetive
imagem_detetive = ImageTk.PhotoImage(Image.open("assets/detetive.png"))

# Cria o rótulo para exibir a imagem
imagem_label = tk.Label(janela_inicial, image=imagem_detetive)
imagem_label.pack(pady=10)

# Cria o botão para abrir a janela principal
iniciar_button = tk.Button(janela_inicial, text="Iniciar", command=abrir_janela_principal, font=("Arial", 12))
iniciar_button.pack(pady=5)

# Inicia o loop principal da janela inicial
janela_inicial.mainloop()
