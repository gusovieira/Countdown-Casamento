import streamlit as st
from datetime import datetime
import pytz
import time

# === Configurações da página ===
st.set_page_config(page_title="Contagem Regressiva", page_icon="💍")

# === HTML para plano de fundo e música ===
st.markdown("""
<style>
body {
    background-image: url('https://raw.githubusercontent.com/gusovieira/Countdown-Casamento/main/background.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
</style>

<audio autoplay loop>
  <source src="https://raw.githubusercontent.com/gusovieira/Countdown-Casamento/main/musica.mp3" type="audio/mpeg">
  Seu navegador não suporta o áudio.
</audio>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>💒 Contagem Regressiva para o Casamento 💒</h1>", unsafe_allow_html=True)

# === Data alvo ===
fuso_brasilia = pytz.timezone('America/Sao_Paulo')
data_alvo = fuso_brasilia.localize(datetime(2025, 11, 22, 16, 0, 0))

placeholder = st.empty()

for _ in range(999999):
    with placeholder.container():
        agora = datetime.now(fuso_brasilia)
        restante = data_alvo - agora

        if restante.total_seconds() <= 0:
            st.success("🎉 Chegou a hora! Felicidades!")
            break

        dias = restante.days
        horas, resto = divmod(restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        total_segundos = int(restante.total_seconds())
        total_minutos = total_segundos // 60
        total_horas = total_minutos // 60
        dias_total = total_horas / 24

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Dias", dias)
        col2.metric("Horas", horas)
        col3.metric("Minutos", minutos)
        col4.metric("Segundos", segundos)

        st.markdown(f"🕐 **Total de horas**: `{total_horas:,}`".replace(",", "."))
        st.markdown(f"🕐 **Total de minutos**: `{total_minutos:,}`".replace(",", "."))
        st.markdown(f"🕐 **Total de segundos**: `{total_segundos:,}`".replace(",", "."))

        comparacoes = [
            f"🌍 {dias_total / 365.25:.4f} voltas da Terra ao redor do Sol",
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

        st.markdown("### 📊 Comparações de Tempo")
        slide = st.slider("Escolha uma comparação", 0, len(comparacoes) - 1, 0)
        st.info(comparacoes[slide])

    time.sleep(1)

