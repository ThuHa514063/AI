import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS: FONT CŨ + BỐ CỤC MỚI ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    /* Chèn lại bộ Font chữ Rồng Bay Phượng Múa */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    .stApp {{
        background-color: #800000;
    }}

    /* Container bao quanh tấm thiệp */
    .card-container {{
        position: relative;
        width: 100%;
        max-width: 800px;
        margin: auto;
        border: 4px solid #FFD700;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.7);
    }}

    .bg-image {{
        width: 100%;
        display: block;
    }}

    /* Nội dung đè lên hình */
    .overlay-content {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        text-align: center;
        /* Thêm lớp phủ tối nhẹ để font chữ vàng nổi bật hơn */
        background: rgba(0, 0, 0, 0.2); 
        padding: 15px;
        border-radius: 10px;
    }}

    /* Tiêu đề chính - Vàng chói rực rỡ */
    h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: clamp(40px, 8vw, 75px) !important;
        text-shadow: 3px 3px 6px #000000;
        margin: 0 !important;
    }}

    /* Các tiêu đề phụ và văn bản - Trắng sữa hoặc Vàng nhạt */
    h2, h3, p, .sub-title {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: clamp(20px, 5vw, 35px) !important;
        text-shadow: 2px 2px 4px #000000;
        margin-top: 5px !important;
    }}

    /* Tùy chỉnh input & nút */
    div.stTextInput > div > div > input {{
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
        text-align: center;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #C5A059) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        border: 1px solid #ffffff !important;
        width: 100%;
        transition: 0.3s;
    }}
    
    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0px 0px 15px #FFD700;
    }}

    /* Căn giữa ảnh quà tặng */
    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }}, colors: ['#FFD700', '#FF0000', '#ffffff'] }});
        }}
        setInterval(fire, 3500);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

luck_messages = ["💰 Tài Lộc như ý!", "🌸 Tình Duyên thắm thiết!", "🐎 Mã Đáo Thành Công!"]

# --- 4. GIAO DIỆN ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.markdown(f"""
        <div class="card-container">
            <img src="{bg_link}" class="bg-image">
            <div class="overlay-content">
                <h1>Happy New Year</h1>
                <div class="sub-title">🧧 Xuân Bính Ngọ 2026 🐎</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Khoảng cách
    name = st.text_input("Quý danh của bạn là...", key="name_input")
    if st.button("Khai Xuân Nhận Lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()

# BƯỚC 2: CHỌN QUÀ
elif st.session_state.step == 2:
    st.markdown(f"""
        <div class="card-container">
            <img src="{bg_link}" class="bg-image">
            <div class="overlay-content">
                <h1>Chào {st.session_state.name}</h1>
                <div class="sub-title">Chọn một túi lộc đầu năm</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    types = ["💰 Tiền Tài", "❤️ Tình Duyên", "🐎 Sức Khỏe"]
    for i in range(3):
        with cols[i]:
            if st.button(types[i]):
                st.session_state.gift = random.choice(luck_messages)
                st.session_state.step = 3
                st.rerun()

# BƯỚC 3: KẾT QUẢ
elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f"""
        <div class="card-container">
            <img src="{bg_link}" class="bg-image">
            <div class="overlay-content">
                <h1>Vạn Sự Như Ý</h1>
                <div class="sub-title">{st.session_state.gift}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.success(f"Chúc mừng năm mới {st.session_state.name}!")
    
    # Logic kiểm tra tên riêng (như bạn yêu cầu)
    ten_check = st.session_state.name.lower().strip()
    if ten_check == "nguyễn văn a": # Thay tên và link ảnh của bạn
        st.image("LINK_ẢNH_RIÊNG", caption="Quà đặc biệt dành cho bạn!")
    else:
        # Ảnh ngẫu nhiên
        st.image(f"https://picsum.photos/400/300?random={random.randint(1,100)}", width=400)

    if st.button("Làm lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()
