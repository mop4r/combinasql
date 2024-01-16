import os
import shutil
import tkinter as tk
from tkinter import messagebox

def combinar_arquivos_txt():
    # Obtém o diretório atual
    diretorio_atual = os.getcwd()

    # Lista todos os arquivos .txt no diretório
    arquivos_txt = [arquivo for arquivo in os.listdir(diretorio_atual) if arquivo.endswith('.txt')]

    # Verifica se existem arquivos .txt para combinar
    if not arquivos_txt:
        messagebox.showinfo("Informação", "Não há arquivos .txt para combinar.")
        return

    # Nome do arquivo de saída combinado
    arquivo_saida = "sql.txt"

    # Combina os arquivos .txt usando o comando "copy"
    comando_copy = "copy /b " + "+".join(arquivos_txt) + " " + arquivo_saida
    os.system(comando_copy)

    # Apaga os arquivos .txt originais
    for arquivo in arquivos_txt:
        os.remove(arquivo)

    messagebox.showinfo("Concluído", f"Arquivos .txt combinados com sucesso em {arquivo_saida}. Arquivos originais apagados.")

class AplicacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Combinar Arquivos .txt")

        self.label = tk.Label(root, text="Clique no botão para combinar arquivos .txt")
        self.label.pack(pady=10)

        self.botao_combinar = tk.Button(root, text="Combinar Arquivos", command=self.combinar)
        self.botao_combinar.pack(pady=20)

    def combinar(self):
        combinar_arquivos_txt()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoGUI(root)
    root.mainloop()
