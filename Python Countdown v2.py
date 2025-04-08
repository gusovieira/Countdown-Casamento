import tkinter as tk
from datetime import datetime
import time
import threading
import pytz

# === Configuração de fuso horário e data alvo ===
fuso_brasilia = pytz.timezone('America/Sao_Paulo')
data_alvo_local = fuso_brasilia.localize(datetime(2025, 11, 22, 16, 0, 0))

# === Lista para armazenar comparações ===
comparacoes_slide = []
indice_slide = 0

# === Função de contagem regressiva ===
def atualizar_contagem():
    while True:
        agora_local = datetime.now(fuso_brasilia)
        restante = data_alvo_local - agora_local

        if restante.total_seconds() <= 0:
            atualizar_labels("🎉 Chegou a hora!", "", "", "")
            atualizar_comparacoes(0)
            break

        dias = restante.days
        horas, resto = divmod(restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        total_segundos = int(restante.total_seconds())
        total_minutos = total_segundos // 60
        total_horas = total_segundos // 3600

        texto_formatado = f"Faltam: {dias}d {horas:02d}h {minutos:02d}m {segundos:02d}s"

        atualizar_labels(
            texto_formatado,
            f"Total de horas: {total_horas:,}".replace(",", "."),
            f"Total de minutos: {total_minutos:,}".replace(",", "."),
            f"Total de segundos: {total_segundos:,}".replace(",", ".")
        )

        atualizar_comparacoes(total_horas)
        time.sleep(1)

# === Atualiza os textos principais ===
def atualizar_labels(formatado, horas, minutos, segundos):
    label_contagem.config(text=formatado)
    label_total_horas.config(text=horas)
    label_total_minutos.config(text=minutos)
    label_total_segundos.config(text=segundos)

# === Atualiza a lista de comparações para o slide ===
def atualizar_comparacoes(total_horas):
    global comparacoes_slide

    dias = total_horas / 24
    comparacoes_slide = [
        f"🌍 {dias / 365.25:.4f} voltas da Terra ao redor do Sol",
        f"🚄 {total_horas / 30:.1f} viagens SP → Salvador (trem)",
        f"🎬 {total_horas / 11.5:.1f} maratonas SdA (versão estendida)",
        f"✈️ {total_horas / 24:.1f} voos SP → Tóquio",
        f"😴 {total_horas / 8:.0f} noites de sono (8h)",

        f"📚 {total_horas / 6:.0f} livros lidos (6h por livro)",
        f"🎮 {int(total_horas * 2):,} partidas de videogame (30min)".replace(",", "."),
        f"🍳 {int(total_horas * 6):,} omeletes preparados".replace(",", "."),
        f"🚀 {total_horas / 144:.1f} viagens ida-volta à Lua",
        f"🎵 {int(total_horas * 20):,} músicas ouvidas".replace(",", "."),
        f"📺 {int((total_horas * 60) / 22):,} episódios de comédia assistidos".replace(",", "."),
        f"🧘 {int(total_horas * 4):,} sessões de meditação (15min)".replace(",", ".")
    ]

# === Slide automático de comparações ===
def mostrar_slide():
    global indice_slide
    if comparacoes_slide:
        label_slide.config(text=comparacoes_slide[indice_slide])
        indice_slide = (indice_slide + 1) % len(comparacoes_slide)
    janela.after(3000, mostrar_slide)

# === Interface ===
janela = tk.Tk()
janela.title("Contagem Regressiva com Comparações")
janela.geometry("520x420")

label_titulo = tk.Label(
    janela,
    text="Contagem regressiva para:\n22/11/2025 às 16h00 (Horário de Brasília)",
    font=("Arial", 12)
)
label_titulo.pack(pady=10)

label_contagem = tk.Label(janela, text="", font=("Arial", 16, "bold"), fg="blue")
label_contagem.pack(pady=5)

label_total_horas = tk.Label(janela, text="", font=("Arial", 11))
label_total_horas.pack()

label_total_minutos = tk.Label(janela, text="", font=("Arial", 11))
label_total_minutos.pack()

label_total_segundos = tk.Label(janela, text="", font=("Arial", 11))
label_total_segundos.pack()

# === Área do slide de comparações ===
frame_slide = tk.LabelFrame(janela, text="Comparações de Tempo", font=("Arial", 11, "bold"))
frame_slide.pack(padx=10, pady=15, fill="both", expand=False)

label_slide = tk.Label(frame_slide, text="", font=("Arial", 11), justify="center", wraplength=460)
label_slide.pack(padx=10, pady=10)

# === Inicia a contagem e o slide ===
threading.Thread(target=atualizar_contagem, daemon=True).start()
janela.after(1000, mostrar_slide)
janela.mainloop()
