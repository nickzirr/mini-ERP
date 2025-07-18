import tkinter as tk
from tkinter import messagebox
from games_data import games
from carrinho import Carrinho
from ui_components import criar_card_jogo

class GameStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loja Virtual de Games")
        self.root.geometry("1000x700")
        
        self.carrinho = Carrinho()
        self.setup_ui()

    def setup_ui(self):
        titulo = tk.Label(self.root, text="Bem-vindo à Loja de Games!", font=("Arial", 24))
        titulo.pack(pady=20)

        self.frame_games = tk.Frame(self.root)
        self.frame_games.pack()

        for game in games:
            card = criar_card_jogo(self.frame_games, game, self.carrinho.adicionar)
            card.pack(pady=10, padx=10, fill="x")

        btn_ver_carrinho = tk.Button(self.root, text="Ver Carrinho", command=self.ver_carrinho, font=("Arial", 14))
        btn_ver_carrinho.pack(pady=20)

    def ver_carrinho(self):
        itens = self.carrinho.listar()
        if not itens:
            messagebox.showinfo("Carrinho", "Carrinho vazio.")
            return
        total = self.carrinho.total()
        jogos = "\n".join(f"{g['nome']} - R$ {g['preco']:.2f}" for g in itens)
        messagebox.showinfo("Carrinho", f"{jogos}\n\nTotal: R$ {total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameStoreApp(root)
    root.mainloop()