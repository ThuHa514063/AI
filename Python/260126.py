import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: ĐẨY CHỮ LÊN KHUNG TRÊN ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* Nền to toàn màn hình */
    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    /* KHUNG NỘI DUNG - ĐẨY LÊN VỊ TRÍ Ô KHOANH TRÒN */
    .content-overlay {{
        position: absolute;
        top: 15%; /* Điều chỉnh phần trăm này để chữ lên/xuống đúng ô đỏ */
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        text-align: center;
        z-index: 100;
    }}

    /* Chữ Happy New Year màu vàng kim */
    .title-gold {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: 65px !important;
        text-shadow: 2px 2px 8px #000000;
        margin-bottom: 0px;
    }}

    /* Chữ phụ màu trắng sữa */
    .sub-white {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: 28px !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* Ô nhập liệu và Nút bấm nằm phía dưới */
    .input-container {{
        margin-top: 350px; /* Đẩy ô nhập tên xuống dưới để không đè lên chữ trên */
        text-align: center;
    }}

    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #C5A059) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border-radius: 30px !important;
        width: 100%;
        border: none !important;
    }}

    /* Căn giữa Image/Gif */
    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }}, colors: ['#FFD700', '#FF0000'] }});
        }}
        setInterval(fire, 3500);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# --- 4. GIAO DIỆN ---

# Phần chữ luôn nằm ở phía trên (vị trí ông khoanh)
if st.session_state.step == 1:
    st.markdown(f"""
        <div class="content-overlay">
            <div class="title-gold">Happy New Year</div>
            <div class="sub-white">🏮 Xuân Bính Ngọ 2026 🏮</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Đẩy phần nhập liệu xuống dưới
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    name = st.text_input("Quý danh của bạn...", placeholder="Nhập tên tại đây...")
    if st.button("Khai Xuân Nhận Lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown(f"""
        <div class="content-overlay">
            <div class="title-gold">Chào {st.session_state.name}</div>
            <div class="sub-white">Hãy chọn túi lộc may mắn</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    cols = st.columns(3)
    types = ["💰 Tiền Tài", "❤️ Tình Duyên", "🐎 Sức Khỏe"]
    for i in range(3):
        with cols[i]:
            if st.button(types[i]):
                st.session_state.gift = random.choice(["💰 Tài Lộc như ý!", "🌸 Tình Duyên thắm thiết!", "🐎 Mã Đáo Thành Công!"])
                st.session_state.step = 3
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f"""
        <div class="content-overlay">
            <div class="title-gold">Vạn Sự Như Ý</div>
            <div class="sub-white">{st.session_state.gift}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=250)
    
    # Check tên tặng ảnh
    if st.session_state.name.lower().strip() == "tên_của_bạn": 
        st.image("LINK_ẢNH_RIÊNG", width=300)
    
    if st.button("Làm lại ↺"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
