import tkinter as tk
from PIL import Image, ImageTk

def criar_card_jogo(root, game, callback_adicionar):
    frame = tk.Frame(root, bd=2, relief="raised", padx=10, pady=10)

    try:
        img = Image.open(game["imagem"])
        img = img.resize((100, 100))
        foto = ImageTk.PhotoImage(img)
        img_label = tk.Label(frame, image=foto)
        img_label.image = foto  # evitar garbage collector
        img_label.pack()
    except Exception as e:
        tk.Label(frame, text="Imagem não encontrada").pack()

    tk.Label(frame, text=game["nome"], font=("Arial", 14)).pack()
    tk.Label(frame, text=game["descricao"], wraplength=300).pack()
    tk.Label(frame, text=f"R$ {game['preco']:.2f}").pack()

    btn = tk.Button(frame, text="Adicionar ao Carrinho", command=lambda: callback_adicionar(game))
    btn.pack()

    return frame