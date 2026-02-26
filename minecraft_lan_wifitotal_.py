import tkinter as tk
from PIL import Image, ImageTk
import time
import winsound
import os

TEMPO_TOTAL = 60000  # 16h40min em segundos

def play_alert():
    try:
        winsound.Beep(900, 250)
    except:
        pass

def tela_contador():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="black")

    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()

    # -------- IMAGEM DE FUNDO --------
    if os.path.exists("bsod.png"):
        img = Image.open("bsod.png")
        img = img.resize((largura, altura))
        img_tk = ImageTk.PhotoImage(img)

        label_img = tk.Label(root, image=img_tk)
        label_img.image = img_tk
        label_img.place(x=0, y=0, relwidth=1, relheight=1)

    # -------- BARRA PRETA --------
    barra = tk.Frame(root, bg="#111111", height=120)
    barra.place(relx=0, rely=0.85, relwidth=1)

    # Linha branca fina
    linha = tk.Frame(root, bg="white", height=2)
    linha.place(relx=0, rely=0.85, relwidth=1)

    contador = tk.Label(
        barra,
        text="Tempo restante: 16:40:00",
        fg="white",
        bg="#111111",
        font=("Segoe UI", 34, "bold")
    )
    contador.place(relx=0.5, rely=0.5, anchor="center")

    inicio = time.time()

    def atualizar():
        decorrido = int(time.time() - inicio)
        restante = TEMPO_TOTAL - decorrido

        if restante <= 0:
            play_alert()
            root.destroy()
            return

        minutos = restante // 60
        segundos = restante % 60

        contador.config(text=f"Tempo restante: {minutos:02}:{segundos:02}")

        # toca som a cada minuto
        if segundos == 0:
            play_alert()

        root.after(1000, atualizar)

    # Atalho Ctrl + L para fechar
    root.bind("<Control-l>", lambda e: root.destroy())
    root.bind("<Control-L>", lambda e: root.destroy())

    atualizar()
    root.mainloop()

tela_contador()