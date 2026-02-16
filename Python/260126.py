import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: KHUNG MỜ PHÓNG TO & CHỮ VÀNG KIM ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    /* KHUNG MỜ PHÓNG TO ĐỂ CHỨA CHỮ */
    .glass-box {{
        position: absolute;
        top: 10%; /* Vị trí khung mờ */
        left: 50%;
        transform: translateX(-50%);
        width: 85%;
        max-width: 700px;
        background: rgba(139, 0, 0, 0.5); /* Màu đỏ thẫm trong suốt */
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 40px 20px;
        border-radius: 30px;
        border: 2px solid rgba(255, 215, 0, 0.6);
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        z-index: 100;
    }}

    .title-gold {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: clamp(45px, 10vw, 75px) !important;
        text-shadow: 3px 3px 6px #000000;
        margin: 0;
    }}

    .sub-white {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: clamp(22px, 5vw, 32px) !important;
        text-shadow: 2px 2px 4px #000000;
        margin-top: 10px;
    }}

    /* ĐẨY PHẦN NHẬP LIỆU XUỐNG DƯỚI KHUNG MỜ */
    .interaction-area {{
        margin-top: 480px; 
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 20px;
    }}

    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 10px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #FFA500) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border-radius: 50px !important;
        border: none !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }}

    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.7 }}, colors: ['#FFD700', '#FF0000', '#ffffff'] }});
        }}
        setInterval(fire, 3500);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# --- 4. GIAO DIỆN ---

# KHUNG MỜ CHỨA CHỮ (Cố định ở trên)
if st.session_state.step == 1:
    st.markdown("""
        <div class="glass-box">
            <div class="title-gold">Happy New Year</div>
            <div class="sub-white">🏮 Xuân Bính Ngọ 2026 🏮</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("Quý danh của bạn...", placeholder="Nhập tên để nhận lộc...")
    if st.button("Khai Xuân Nhận Lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown(f"""
        <div class="glass-box">
            <div class="title-gold">Chào {st.session_state.name}</div>
            <div class="sub-white">Hãy chọn một túi lộc may mắn</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    cols = st.columns(3)
    types = ["💰 Tiền Tài", "❤️ Tình Duyên", "🐎 Sức Khỏe"]
    for i in range(3):
        with cols[i]:
            if st.button(types[i]):
                st.session_state.gift = random.choice(["💰 Tiền vào như nước, ví luôn căng đầy!", "🌸 Tình duyên nở rộ, hạnh phúc ngập tràn!", "🐎 Mã đáo thành công, vạn sự hanh thông!"])
                st.session_state.step = 3
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f"""
        <div class="glass-box">
            <div class="title-gold">Vạn Sự Như Ý</div>
            <div class="sub-white">{st.session_state.gift}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=250)
    
    # Check tên tặng ảnh cá nhân
    name_low = st.session_state.name.lower().strip()
    if name_low == "tên_của_bạn": 
        st.image("LINK_ẢNH_RIÊNG", width=300)
    
    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
