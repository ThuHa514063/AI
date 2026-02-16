import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: THỐNG NHẤT 1 FONT - CHỮ TO - HÌNH TO ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    /* Dùng duy nhất 1 Font Dancing Script cho toàn bộ ứng dụng */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    /* KHUNG MỜ PHÓNG TO */
    .glass-box {{
        position: absolute;
        top: 8%; 
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 850px;
        background: rgba(139, 0, 0, 0.55); 
        backdrop-filter: blur(12px);
        padding: 50px 30px;
        border-radius: 35px;
        border: 3px solid rgba(255, 215, 0, 0.7);
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        z-index: 100;
    }}

    /* CHỮ TO RỰC RỠ */
    .big-gold-text {{
        font-family: 'Dancing Script', cursive !important;
        color: #FFD700 !important;
        font-size: clamp(55px, 12vw, 90px) !important;
        text-shadow: 4px 4px 10px #000000;
        margin: 0;
        line-height: 1.2;
    }}

    .big-white-text {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: clamp(30px, 7vw, 45px) !important;
        text-shadow: 3px 3px 6px #000000;
        margin-top: 15px;
    }}

    /* VÙNG TƯƠNG TÁC PHÍA DƯỚI */
    .interaction-area {{
        margin-top: 550px; 
        text-align: center;
        padding: 20px;
    }}

    /* Input & Nút bấm cũng dùng chung font và làm to ra */
    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 12px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 28px !important;
        height: 60px;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #FFA500) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 30px !important;
        border-radius: 60px !important;
        padding: 15px 0 !important;
        border: none !important;
        width: 100%;
        box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    }}

    /* PHÓNG TO HÌNH ẢNH/GIF */
    [data-testid="stImage"] img {{
        width: 100% !important;
        max-width: 500px !important; /* Phóng to ảnh quà tặng */
        border-radius: 20px;
        border: 4px solid #FFD700;
    }}
    
    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ particleCount: 180, spread: 80, origin: {{ y: 0.7 }}, colors: ['#FFD700', '#FF0000', '#ffffff'] }});
        }}
        setInterval(fire, 3000);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. DỮ LIỆU ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

lời_chúc = [
    "💰 Tiền vào như nước, ví luôn căng đầy!", 
    "🌸 Tình duyên nở rộ, hạnh phúc ngập tràn!", 
    "🐎 Mã đáo thành công, vạn sự hanh thông!",
    "🍀 Vạn sự như ý, sức khỏe dồi dào!"
]

# --- 4. GIAO DIỆN ---

# KHUNG CHỮ CỐ ĐỊNH Ở TRÊN
if st.session_state.step == 1:
    st.markdown("""
        <div class="glass-box">
            <div class="big-gold-text">Happy New Year</div>
            <div class="big-white-text">🏮 Xuân Bính Ngọ 2026 🏮</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên của bạn tại đây...")
    if st.button("Khai Xuân Nhận Lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown(f"""
        <div class="glass-box">
            <div class="big-gold-text">Chào {st.session_state.name}</div>
            <div class="big-white-text">Hãy chọn một túi lộc may mắn</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    cols = st.columns(3)
    types = ["💰 Tiền Tài", "❤️ Tình Duyên", "🐎 Sức Khỏe"]
    for i in range(3):
        with cols[i]:
            if st.button(types[i]):
                st.session_state.gift = random.choice(lời_chúc)
                st.session_state.step = 3
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f"""
        <div class="glass-box">
            <div class="big-gold-text">Vạn Sự Như Ý</div>
            <div class="big-white-text">{st.session_state.gift}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    # GIF To ra
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    # Check tên tặng ảnh cá nhân to ra
    name_low = st.session_state.name.lower().strip()
    if name_low == "tên_của_bạn": 
        st.image("LINK_ẢNH_RIÊNG")
    
    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
