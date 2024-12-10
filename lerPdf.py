import tkinter as tk
from tkinter import filedialog, Text
import PyPDF2

def abrir_pdf():
    # Abre uma janela para selecionar o arquivo PDF
    arquivo_pdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if arquivo_pdf:
        with open(arquivo_pdf, "rb") as file:
            leitor = PyPDF2.PdfReader(file)
            texto = ""
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
            exibir_texto(texto)

def exibir_texto(texto):
    # Limpa a área de texto e insere o texto lido
    texto_area.delete(1.0, tk.END)  # Limpa a área de texto
    texto_area.insert(tk.END, texto)  # Insere o texto lido

# Configuração da interface
root = tk.Tk()
root.title("Leitor de PDF")

botao_abrir = tk.Button(root, text="Abrir PDF", command=abrir_pdf)
botao_abrir.pack()

texto_area = Text(root, wrap=tk.WORD)
texto_area.pack(expand=True, fill='both')

root.mainloop()