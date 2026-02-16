import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới Bính Ngọ 2026", page_icon="🐎", layout="centered")

# --- CSS & FONT CHỮ RỒNG BAY PHƯỢNG MÚA ---
background_image_url = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725" 

st.markdown(f"""
    <style>
    /* Chèn Font chữ nghệ thuật từ Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Lớp phủ làm mờ nền để nổi chữ */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5); 
        z-index: -1;
    }}

    /* Font chữ tiêu đề chính (Rồng bay phượng múa) */
    h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important; /* Màu vàng kim */
        font-size: 80px !important;
        text-shadow: 3px 3px 6px #000000;
        margin-bottom: 10px !important;
    }}

    /* Font chữ tiêu đề phụ & lời chúc */
    h2, h3, p, .stMarkdown {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important; /* Màu trắng sữa cho dịu mắt */
        font-size: 35px !important;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }}

    /* Tùy chỉnh các nút bấm cho sang hơn */
    .stButton>button {{
        border-radius: 30px;
        border: 2px solid #FFD700;
        background-color: rgba(255, 75, 75, 0.8);
        color: white;
        font-family: 'Dancing Script', cursive;
        font-size: 20px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #FFD700;
        color: #ff4b4b;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function autoFire() {{
            confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }}, colors: ['#ff0000', '#ffd700'] }});
        }}
        setInterval(autoFire, 3000);
        autoFire();
    </script>
""", unsafe_allow_html=True)

# --- QUẢN LÝ SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- GIAO DIỆN TỪNG BƯỚC ---

if st.session_state.step == 1:
    st.title("Chúc Mừng Năm Mới")
    st.write("Xuân Bính Ngọ 2026")
    name_input = st.text_input("Quý danh của bạn là...", placeholder="Nhập tên tại đây...")
    if st.button("Khởi đầu may mắn ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.title(f"Chào {st.session_state.name}")
    st.subheader("Chọn một túi lộc đầu xuân:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💰 Khai Vận Tài Lộc"):
            st.session_state.gift = "Mã đáo thành công, tiền vào như nước!"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🌸 Khai Vận Tình Duyên"):
            st.session_state.gift = "Ý trung nhân xuất hiện, hạnh phúc vẹn tròn!"
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.title("Vạn Sự Như Ý")
    st.balloons()
    st.write(f"Chúc mừng {st.session_state.name} đã nhận được:")
    st.success(st.session_state.gift)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    if st.button("Nhận lộc mới ↺"):
        st.session_state.step = 1
        st.rerun()
