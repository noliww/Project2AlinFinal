import streamlit as st
from PIL import Image
import numpy as np
import cv2

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Image Processing Tools", layout="wide")

# =========================================================
# GLOBAL LANGUAGE (FOLLOW APP)
# =========================================================
lang = st.session_state.get("lang", "id")

TEXT = {
    "id": {
        "title": "🌸 Alat Pengolahan Citra",
        "caption": "Blur • Sharpen • Hapus Background • Transformasi Geometrik",
        "upload": "📷 Unggah Gambar",
        "upload_info": "✨ Silakan unggah gambar untuk memulai",
        "original": "Gambar Asli",
        "processed": "Hasil Proses",
        "sidebar": "💗 Menu Alat",
        "choose": "Pilih Fitur",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "bg": "Hapus Background",
        "geo": "Transformasi Geometrik",
        "geo_select": "Pilih Transformasi",
        "translation": "Translasi",
        "rotation": "Rotasi",
        "scaling": "Skala",
        "reflection": "Refleksi",
        "kernel": "Ukuran Kernel",
        "scale_proc": "Skala Pemrosesan",
        "tx": "Geser X",
        "ty": "Geser Y",
        "angle": "Sudut Rotasi",
        "scale": "Faktor Skala",
        "axis": "Sumbu Refleksi",
        "horizontal": "Horizontal",
        "vertical": "Vertikal",
        "success": "✨ Proses berhasil diterapkan!",
        "tip": "💡 Tips: Klik kanan gambar untuk menyimpan hasil."
    },
    "en": {
        "title": "🌸 Image Processing Tools",
        "caption": "Blur • Sharpen • Background Removal • Geometric Transformations",
        "upload": "📷 Upload Image",
        "upload_info": "✨ Please upload an image to start processing",
        "original": "Original Image",
        "processed": "Processed Image",
        "sidebar": "💗 Tools Menu",
        "choose": "Choose Feature",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "bg": "Background Removal",
        "geo": "Geometric Transformation",
        "geo_select": "Select Transformation",
        "translation": "Translation",
        "rotation": "Rotation",
        "scaling": "Scaling",
        "reflection": "Reflection",
        "kernel": "Kernel Size",
        "scale_proc": "Processing Scale",
        "tx": "Translate X",
        "ty": "Translate Y",
        "angle": "Rotation Angle",
        "scale": "Scale Factor",
        "axis": "Reflection Axis",
        "horizontal": "Horizontal",
        "vertical": "Vertical",
        "success": "✨ Process applied successfully!",
        "tip": "💡 Tip: Right-click the image to save the result."
    }
}

T = TEXT[lang]

# =========================================================
# STYLE
# =========================================================
st.markdown("""
<style>
body { background-color: #ffe6f0; }
.block-container { padding-top: 2rem; }
.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}
.title { color: #d63384; font-weight: bold; }
.notice {
    background-color: #fff0f6;
    padding: 12px;
    border-radius: 12px;
    border-left: 5px solid #d63384;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================
st.markdown(f'<h1 class="title">{T["title"]}</h1>', unsafe_allow_html=True)
st.caption(T["caption"])

# =========================================================
# UPLOAD
# =========================================================
st.markdown('<div class="card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(T["upload"], type=["jpg", "png", "jpeg"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is None:
    st.info(T["upload_info"])
    st.stop()

image = Image.open(uploaded_file).convert("RGB")
img = np.array(image)
rows, cols = img.shape[:2]

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(T["original"])
    st.image(image, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# KERNEL FUNCTION
# =========================================================
def apply_kernel(img, kernel):
    out = np.zeros_like(img)
    for c in range(3):
        out[:, :, c] = cv2.filter2D(img[:, :, c], -1, kernel)
    return np.clip(out, 0, 255).astype(np.uint8)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown(f"## {T['sidebar']}")
tool = st.sidebar.radio(
    T["choose"],
    [T["blur"], T["sharpen"], T["bg"], T["geo"]]
)

result = img.copy()

# =========================================================
# BLUR
# =========================================================
if tool == T["blur"]:
    k = st.sidebar.slider(T["kernel"], 3, 15, 7, step=2)
    kernel = np.ones((k, k)) / (k * k)
    result = apply_kernel(img, kernel)
    st.success(T["success"])

# =========================================================
# SHARPEN
# =========================================================
elif tool == T["sharpen"]:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    result = apply_kernel(img, kernel)
    st.success(T["success"])

# =========================================================
# BACKGROUND REMOVAL
# =========================================================
elif tool == T["bg"]:
    scale = st.sidebar.slider(T["scale_proc"], 0.4, 1.0, 0.6)
    small = cv2.resize(img, None, fx=scale, fy=scale)
    h, w = small.shape[:2]

    mask = np.zeros((h, w), np.uint8)
    bg_model = np.zeros((1, 65), np.float64)
    fg_model = np.zeros((1, 65), np.float64)

    margin = int(min(h, w) * 0.1)
    rect = (margin, margin, w - 2 * margin, h - 2 * margin)

    cv2.grabCut(small, mask, rect, bg_model, fg_model, 1, cv2.GC_INIT_WITH_RECT)
    mask_fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype("uint8")
    mask_fg = cv2.resize(mask_fg, (cols, rows))

    rgba = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    rgba[:, :, 3] = mask_fg
    result = rgba
    st.success(T["success"])

# =========================================================
# GEOMETRIC TRANSFORMATION
# =========================================================
elif tool == T["geo"]:
    geo = st.sidebar.selectbox(
        T["geo_select"],
        [T["translation"], T["rotation"], T["scaling"], T["reflection"]]
    )

    if geo == T["translation"]:
        tx = st.sidebar.slider(T["tx"], -200, 200, 0)
        ty = st.sidebar.slider(T["ty"], -200, 200, 0)
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        result = cv2.warpAffine(img, M, (cols, rows))

    elif geo == T["rotation"]:
        angle = st.sidebar.slider(T["angle"], -180, 180, 0)
        center = (cols // 2, rows // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1)
        result = cv2.warpAffine(img, M, (cols, rows))

    elif geo == T["scaling"]:
        scale = st.sidebar.slider(T["scale"], 0.1, 2.0, 1.0)
        M = np.float32([[scale, 0, 0], [0, scale, 0]])
        result = cv2.warpAffine(img, M, (cols, rows))

    elif geo == T["reflection"]:
        axis = st.sidebar.radio(T["axis"], [T["horizontal"], T["vertical"]])
        if axis == T["horizontal"]:
            M = np.float32([[1, 0, 0], [0, -1, rows]])
        else:
            M = np.float32([[-1, 0, cols], [0, 1, 0]])
        result = cv2.warpAffine(img, M, (cols, rows))

    st.success(T["success"])

# =========================================================
# RESULT
# =========================================================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(T["processed"])
    st.image(result, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(f'<div class="notice">{T["tip"]}</div>', unsafe_allow_html=True)
