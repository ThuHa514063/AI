import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: KHUNG MỜ TRUNG TÂM ---
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

    /* KHUNG MỜ TRUNG TÂM */
    .glass-box {{
        position: absolute;
        top: 8%; left: 50%;
        transform: translateX(-50%);
        width: 90%; max-width: 800px;
        background: rgba(139, 0, 0, 0.6); 
        backdrop-filter: blur(15px);
        padding: 40px 20px;
        border-radius: 30px;
        border: 2px solid rgba(255, 215, 0, 0.7);
        text-align: center;
        z-index: 100;
    }}

    .title-dragon {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: 75px !important;
        text-shadow: 4px 4px 8px #000000;
        margin: 0;
    }}

    .text-phoenix {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: 45px !important;
        text-shadow: 3px 3px 6px #000000;
    }}

    .interaction-area {{
        margin-top: 500px; 
        text-align: center;
    }}

    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 12px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 30px !important;
        height: 70px;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #FFA500) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 32px !important;
        border-radius: 50px !important;
        border: none !important;
        width: 100%;
        margin-bottom: 10px;
    }}

    [data-testid="stImage"] img {{
        width: 100% !important;
        max-width: 550px !important;
        border-radius: 20px;
        border: 4px solid #FFD700;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE (SỬA LỖI LOGIC) ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""
if 'gift' not in st.session_state: st.session_state.gift = ""

# --- 4. GIAO DIỆN ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.markdown("""<div class="glass-box"><div class="title-dragon">Happy New Year</div>
                <div class="text-phoenix">🏮 Xuân Bính Ngọ 2026 🏮</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên tại đây...", key="input_step_1")
    if st.button("Khai Xuân Nhận Lộc ➔", key="btn_step_1"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN QUÀ (THÊM OPTION BẤT NGỜ)
elif st.session_state.step == 2:
    st.markdown(f"""<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div>
                <div class="text-phoenix">Chọn một túi lộc may mắn</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    
    # Chia layout nút bấm
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💰 Tiền Tài", key="gift_1"):
            st.session_state.gift = "Tiền vào như nước, ví luôn căng đầy! 💰"
            st.session_state.step = 3
            st.rerun()
        if st.button("❤️ Tình Duyên", key="gift_2"):
            st.session_state.gift = "Tình duyên nở rộ, hạnh phúc ngập tràn! ❤️"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🍀 Sức Khỏe", key="gift_3"):
            st.session_state.gift = "Khỏe như ngựa chiến, vạn dặm bình an! 🐎"
            st.session_state.step = 3
            st.rerun()
        if st.button("🔮 Bất Ngờ", key="gift_4"):
            st.session_state.gift = "Một niềm vui bất ngờ sắp đến với bạn! 🎁"
            st.session_state.step = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# BƯỚC 3: KẾT QUẢ
elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f"""<div class="glass-box"><div class="title-dragon">Vạn Sự Như Ý</div>
                <div class="text-phoenix">{st.session_state.gift}</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    if st.button("Quay lại từ đầu ↺", key="btn_reset"):
        st.session_state.step = 1
        st.session_state.name = ""
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
