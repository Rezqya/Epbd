import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Estu Prihatini", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
body { background-color: #ffd6e8; }
.title { text-align:center; font-size:40px; }
.sub { text-align:center; font-size:20px; }
.center { text-align:center; }
.button { font-size:20px; }
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "cake" not in st.session_state:
    st.session_state.cake = "on"

def go(p):
    st.session_state.page = p

# ---------- HOME ----------
if st.session_state.page == "home":
    st.markdown("<div class='title'>🎉 Happy Birthday Estu Prihatini 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>🎁</div>", unsafe_allow_html=True)
    if st.button("Open Gift 🎁"):
        st.balloons()
        go("menu")

# ---------- MENU ----------
elif st.session_state.page == "menu":
    st.markdown("<div class='title'>💖 Choose One 💖</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💌 Letter"):
            go("letter")
        if st.button("📸 Memories"):
            go("memories")
    with col2:
        if st.button("🎵 MP3"):
            go("music")
        if st.button("🎂 Cake"):
            go("cake")

# ---------- LETTER ----------
elif st.session_state.page == "letter":
    st.markdown("## 💌 Letter")
    st.success("""
Happy Birthday Estu Prihatini 🎉

Selamat ulang tahun ya mbaaak, semoga sehat, happy dan bahagia selaluu ya mbaakkk
semoga rezekinya lancar jaya dan bisa healing kemana ajaa yeeyy
pokoknya dipermudah semuanya ya mbaaakkk
""")
    if st.button("Next ➡️"):
        go("menu")

# ---------- MUSIC ----------
elif st.session_state.page == "music":
    st.markdown("## 🎵 Music")
    st.audio("lagu.mpeg")
    st.info("lagu dari mas mas ganteng wkwkwk 💖")
    if st.button("Next ➡️"):
        go("menu")

# ---------- MEMORIES ----------
elif st.session_state.page == "memories":
    st.markdown("## 📸 Memories")
    st.video("video.mp4")
    if st.button("Next ➡️"):
        go("menu")


# ---------- CAKE ----------
elif st.session_state.page == "cake":
    st.markdown("## 🎂 Birthday Cake")

    if st.session_state.cake == "on":
        st.markdown("<div style='font-size:80px; text-align:center;'>🎂🕯️🕯️</div>", unsafe_allow_html=True)
        if st.button("Tiup Lilin 💨"):
            st.session_state.cake = "off"
            st.snow()
    else:
        st.markdown("<div style='font-size:80px; text-align:center;'>🎂✨</div>", unsafe_allow_html=True)
        st.success("Yeay! Lilinnya mati 🎉")

    if st.button("Next ➡️"):
        go("menu")
