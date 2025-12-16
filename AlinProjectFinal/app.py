import streamlit as st

# MUST be first for multipage apps
st.set_page_config(
    page_title="Matrix Image Processing",
    page_icon="✨",
    layout="wide"
)

# =========================================================
# PINK SMOOTH THEME + SHIMMER EFFECT (NO WHITE BOXES)
# =========================================================
st.markdown("""
<style>
body {
    background-color: #ffe6f0;
}
.block-container {
    padding-top: 2rem;
}
img {
    border-radius: 14px;
}
.title {
    color: #d63384;
    font-weight: 800;
}
.subtitle {
    font-size: 20px;
    margin-top: -8px;
}
.feature {
    margin: 6px 0;
    font-size: 16px;
}
.badge {
    display: inline-block;
    background-color: #ffd6e8;
    color: #ad1457;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 14px;
    margin: 6px 6px 10px 0;
}
.hint {
    color: #6a1b4d;
    font-size: 14px;
}

/* SHIMMER EFFECT */
.shimmer {
    background: linear-gradient(
        90deg,
        #d63384 25%,
        #ff8ac2 50%,
        #d63384 75%
    );
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 2.5s linear infinite;
}

@keyframes shimmer {
    to {
        background-position: -200% center;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================
st.markdown('<h1 class="title">✨ Matrix Image Processing</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle shimmer">Matrix-based Image Processing</div>', unsafe_allow_html=True)

# =========================================================
# INTRO (NO BOX)
# =========================================================
st.markdown("""
Welcome 🌸  
This web application demonstrates **digital image processing** using **mathematical matrices and kernels**.

All transformations and filters are computed numerically — not just visual effects.
""")

# =========================================================
# FEATURES
# =========================================================
st.subheader("💗 Available Features")

st.markdown("""
<span class="badge">📐 Geometric Transformations</span>

<div class="feature">➤ Translation (shift image)</div>
<div class="feature">➤ Scaling (resize image)</div>
<div class="feature">➤ Rotation (rotate image)</div>
<div class="feature">➤ Shearing (tilt image)</div>
<div class="feature">➤ Reflection (mirror image)</div>

<span class="badge">🎨 Image Processing</span>

<div class="feature">➤ Blur (smoothing filter)</div>
<div class="feature">➤ Sharpen (edge enhancement)</div>
<div class="feature">➤ Background Removal (object only)</div>
""", unsafe_allow_html=True)

# =========================================================
# WHY MATRIX
# =========================================================
st.subheader("✨ Why Matrix?")

st.markdown("""
Every pixel in an image has coordinates *(x, y)* 📍  

Using matrix multiplication, these coordinates are recalculated to create transformations.

• Without matrices → no transformation  
• With matrices → image processing becomes possible ✨
""")

# =========================================================
# INTERACTIVE HINT
# =========================================================
st.toast("💡 Open the Image Processing page from the sidebar to start!")

st.markdown('<p class="hint">If the sidebar does not appear, make sure all pages are inside the <b>pages</b> folder.</p>', unsafe_allow_html=True)
