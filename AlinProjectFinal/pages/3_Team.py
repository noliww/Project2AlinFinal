import streamlit as st
import os
from PIL import Image

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(page_title="Team Members", layout="wide")

# ======================================================
# PATH HANDLER (AMAN UNTUK STREAMLIT CLOUD)
# ======================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "team")

def load_image(filename):
    return Image.open(os.path.join(ASSETS_DIR, filename))

# ======================================================
# LANGUAGE SWITCHER
# ======================================================
if "lang" not in st.session_state:
    st.session_state.lang = "id"

lang = st.sidebar.radio(
    "🌐 Language",
    ["Indonesia 🇮🇩", "English 🇬🇧"],
    index=0 if st.session_state.lang == "id" else 1
)

st.session_state.lang = "id" if "Indonesia" in lang else "en"

# ======================================================
# TEXT DICTIONARY
# ======================================================
TEXT = {
    "id": {
        "title": "🌸 Our Team",
        "caption": "Klik untuk melihat peran masing-masing anggota ✨",
        "see_role": "💗 Lihat Peran",
        "role": "Peran"
    },
    "en": {
        "title": "🌸 Our Team",
        "caption": "Click to see each member's role ✨",
        "see_role": "💗 See Role",
        "role": "Role"
    }
}

T = TEXT[st.session_state.lang]

# ======================================================
# PINK THEME STYLE
# ======================================================
st.markdown("""
<style>
.block-container { padding-top: 1.2rem; }
body { background-color: #ffe6f0; }

.card {
    background-color: #ffffff;
    border-radius: 22px;
    padding: 0;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px rgba(214, 51, 132, 0.22);
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 35px rgba(214, 51, 132, 0.35);
}
.card-content {
    padding: 20px;
    text-align: center;
}
.name {
    color: #d63384;
    font-weight: 700;
    font-size: 22px;
    margin-top: 8px;
}
.nim {
    color: #777;
    font-size: 14px;
}
.role-box {
    background-color: #fff0f6;
    padding: 14px;
    border-radius: 14px;
    margin-top: 12px;
}
.stImage img {
    margin: 0 !important;
    border-radius: 22px 22px 0 0;
    display: block;
}
.streamlit-expanderHeader {
    color: #d63384;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# TEAM DATA
# ======================================================
members = [
    {
        "name": "Nolita Salsabila",
        "nim": "004202400105",
        "role_id": "Transformasi Geometrik",
        "role_en": "Geometric Transformations",
        "desc_id": "Mengimplementasikan transformasi matriks seperti translasi, rotasi, scaling, dan refleksi.",
        "desc_en": "Implemented matrix-based transformations such as translation, rotation, scaling, and reflection.",
        "photo": "nolita.jpg"
    },
    {
        "name": "Andi Nur Alifah Erfiyanto",
        "nim": "004202400019",
        "role_id": "Image Filtering",
        "role_en": "Image Filtering",
        "desc_id": "Mengimplementasikan filter blur dan sharpen menggunakan operasi konvolusi.",
        "desc_en": "Implemented blur and sharpen filters using convolution operations.",
        "photo": "alifah.jpg"
    },
    {
        "name": "Selviana Fitri",
        "nim": "004202400029",
        "role_id": "Dokumentasi & Pengujian",
        "role_en": "Documentation & Testing",
        "desc_id": "Menyusun dokumentasi serta melakukan pengujian fitur aplikasi.",
        "desc_en": "Prepared documentation and performed feature testing.",
        "photo": "selvi.jpg"
    },
    {
        "name": "Tiara Luthfi Maharani",
        "nim": "004202400126",
        "role_id": "UI & Streamlit Layout",
        "role_en": "UI & Streamlit Layout",
        "desc_id": "Mengatur tampilan aplikasi, navigasi multi-page, dan kenyamanan pengguna.",
        "desc_en": "Designed application UI, multipage navigation, and user experience.",
        "photo": "tiara.jpg"
    }
]

# ======================================================
# PAGE CONTENT
# ======================================================
st.title(T["title"])
st.caption(T["caption"])

cols = st.columns(2)

for i, m in enumerate(members):
    with cols[i % 2]:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.image(load_image(m["photo"]), width=240)

        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown(f'<div class="name">{m["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="nim">NIM: {m["nim"]}</div>', unsafe_allow_html=True)

        with st.expander(T["see_role"]):
            st.markdown('<div class="role-box">', unsafe_allow_html=True)
            role = m["role_id"] if st.session_state.lang == "id" else m["role_en"]
            desc = m["desc_id"] if st.session_state.lang == "id" else m["desc_en"]
            st.write(f"**{T['role']}:** {role}")
            st.write(desc)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Matrix-based image processing using NumPy & Streamlit")
