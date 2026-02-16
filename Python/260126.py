import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: BACK TOÀN MÀN HÌNH & KHUNG MỜ ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    /* Import Font cũ rồng bay */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* Hình nền to toàn bộ màn hình */
    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Lớp phủ tối nhẹ toàn màn hình để làm nổi khung mờ */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        z-index: -1;
    }}

    /* KHUNG MỜ TRUNG TÂM (Glassmorphism) */
    .glass-card {{
        background: rgba(128, 0, 0, 0.4); /* Màu đỏ thẫm trong suốt */
        backdrop-filter: blur(15px);     /* Làm mờ background phía sau */
        -webkit-backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 25px;
        border: 2px solid rgba(255, 215, 0, 0.5); /* Viền vàng mờ */
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin: 20px auto;
    }}

    /* Màu chữ vàng kim như cũ */
    h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: 70px !important;
        text-shadow: 3px 3px 6px #000000;
        margin-bottom: 10px !important;
    }}

    h2, h3, p, .sub-text {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: 30px !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* Input & Button */
    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #C5A059) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border-radius: 30px !important;
        border: none !important;
        width: 100%;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }}

    /* Căn giữa Image/GIF */
    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }}, colors: ['#FFD700', '#FF0000', '#ffffff'] }});
        }}
        setInterval(fire, 4000);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

luck_messages = ["💰 Tài Lộc Dồi Dào!", "🌸 Tình Duyên Như Ý!", "🐎 Mã Đáo Thành Công!", "🍀 Vạn Sự Bình An!"]

# --- 4. GIAO DIỆN ---

# Bắt đầu bao bọc trong khung mờ
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown("<h1>Happy New Year</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>🏮 Xuân Bính Ngọ 2026 🏮</p>", unsafe_allow_html=True)
    name = st.text_input("Quý danh của bạn...", placeholder="Nhập tên tại đây...")
    if st.button("Khai Xuân Nhận Lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.markdown(f"<h1>Chào {st.session_state.name}</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>Hãy chọn một túi lộc đầu năm</p>", unsafe_allow_html=True)
    cols = st.columns(3)
    types = ["💰 Tiền Tài", "❤️ Tình Duyên", "🐎 Sức Khỏe"]
    for i in range(3):
        with cols[i]:
            if st.button(types[i]):
                st.session_state.gift = random.choice(luck_messages)
                st.session_state.step = 3
                st.rerun()

elif st.session_state.step == 3:
    st.balloons()
    st.markdown("<h1>Vạn Sự Như Ý</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='sub-text'>{st.session_state.gift}</p>", unsafe_allow_html=True)
    
    # GIF Ngựa
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=250)

    # Kiểm tra tên riêng để tặng quà
    name_check = st.session_state.name.lower().strip()
    if name_check == "tên_của_bạn": 
        st.image("LINK_ẢNH_RIÊNG", width=350)
    else:
        st.image(f"https://picsum.photos/400/300?random={random.randint(1,100)}", width=350)

    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
