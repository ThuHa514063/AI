import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hái Lộc Bính Ngọ 2026", page_icon="🧨", layout="centered")

# --- 2. KHO LỜI CHÚC ---
luck_data = {
    "❤️ Tình duyên": ["Hạnh phúc viên mãn, sớm tìm thấy nửa kia nhé!", "Tình duyên nở rộ, vạn người theo đuổi luôn!"],
    "💼 Sự nghiệp": ["Công thành danh toại, thăng quan tiến chức nhé!", "Sự nghiệp bứt phá, khẳng định vị thế nha!"],
    "🐎 Sức khỏe": ["Khỏe như ngựa chiến, vạn dặm bình an nhé!", "Năng lượng dồi dào, tinh thần minh mẫn nha!"],
    "💰 Tiền tài": ["Tiền vào như nước, ví luôn căng đầy nhé!", "Lộc phát đầy kho, vàng bạc đầy tay nha!"],
    "🏠 Gia đình": ["Gia đạo bình an, ấm êm hạnh phúc nhé!", "Cả nhà sum vầy, tiếng cười rộn rã nha!"],
    "🎓 Học tập": ["Học một biết mười, thi cử đỗ đạt nhé!", "Kiến thức uyên thâm, đạt học bổng cao nha!"],
    "🍀 May mắn": ["Vạn sự như ý, tỷ sự như mơ nhé!", "Cầu được ước thấy, may mắn mỉm cười nha!"],
    "🎁 Bất ngờ": ["Quà khủng sắp tới, niềm vui nhân đôi nhé!", "Một bước ngoặt mới đầy thú vị nha!"]
}

# --- 3. CSS TỔNG LỰC (FIX MOBILE & FONT) ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* ÉP FONT TOÀN BỘ */
    html, body, [class*="st-"] {{
        font-family: 'Dancing Script', cursive !important;
    }}

    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
    }}

    /* HIỆU ỨNG HOA ĐÀO RƠI */
    @keyframes flower-drop {{
        0% {{ top: -10%; transform: rotate(0deg); }}
        100% {{ top: 100%; transform: rotate(360deg); }}
    }}
    .petal {{
        position: fixed; color: #ffb7c5; font-size: 20px;
        z-index: 999; pointer-events: none;
        animation: flower-drop 8s linear infinite;
    }}

    /* KHUNG TIÊU ĐỀ */
    .glass-box {{
        position: relative; margin: 20px auto;
        width: 90%; max-width: 800px; background: rgba(139, 0, 0, 0.85); 
        padding: 20px; border-radius: 20px;
        border: 3px solid #FFD700; text-align: center;
    }}
    .title-dragon {{ font-family: 'Great Vibes', cursive !important; color: #FFD700; font-size: 60px; text-shadow: 2px 2px 5px #000; line-height: 1; }}
    .text-phoenix {{ color: #F8F9FA; font-size: 30px; }}

    /* KHU VỰC TƯƠNG TÁC (TỰ THÍCH NGHI) */
    .interaction-area {{
        margin-top: 50px; /* Mặc định cho mobile */
        text-align: center; width: 100%;
    }}

    /* CSS RIÊNG CHO MÁY TÍNH (MÀN HÌNH RỘNG) */
    @media (min-width: 768px) {{
        .interaction-area {{ margin-top: 380px; }}
        .title-dragon {{ font-size: 80px; }}
        .text-phoenix {{ font-size: 40px; }}
    }}

    /* INPUT TÊN */
    div.stTextInput input {{
        font-family: 'Dancing Script', cursive !important;
        font-size: 20px !important; text-align: center;
        border: 2px solid #FFD700 !important; border-radius: 10px;
        background: white !important; color: black !important;
    }}

    /* OPTION BUTTONS */
    .option-container div.stButton > button {{
        height: 140px !important; margin-bottom: 15px !important;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        border: 3px solid #fff !important; text-transform: none !important;
    }}
    .option-container div.stButton > button p {{
        font-size: 40px !important; font-weight: 900 !important; color: #800000 !important;
    }}

    /* NAV BUTTONS */
    .nav-container div.stButton > button {{
        height: 60px !important; max-width: 300px !important; margin: 0 auto !important;
        border-radius: 30px !important; border: 2px solid #fff !important;
        background: #FFD700 !important;
    }}
    .nav-container div.stButton > button p {{ font-size: 24px !important; color: #800000 !important; }}

    .stButton > button:hover {{ transform: scale(1.05) !important; background: white !important; }}
    </style>

    <div class="petal" style="left:10%; animation-duration:7s;">🌸</div>
    <div class="petal" style="left:40%; animation-duration:10s;">🌸</div>
    <div class="petal" style="left:80%; animation-duration:8s;">🌸</div>
""", unsafe_allow_html=True)

# --- 4. LOGIC ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# BƯỚC 1: TRANG CHỦ
if st.session_state.step == 1:
    st.markdown('<div class="glass-box"><div class="title-dragon">Happy New Year</div><div class="text-phoenix">🏮 Xuân bính ngọ 2026 🏮</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên của bạn vào đây...", key="name_input")
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    if st.button("Bắt đầu hái lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN OPTION
elif st.session_state.step == 2:
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div><div class="text-phoenix">Chọn một túi lộc nhé</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area option-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    options = list(luck_data.keys())
    for i, opt in enumerate(options):
        with (col1 if i % 2 == 0 else col2):
            if st.button(opt, key=f"big_opt_{i}"):
                st.session_state.gift = random.choice(luck_data[opt])
                st.session_state.step = 3
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# BƯỚC 3: KẾT QUẢ
elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Vạn sự như ý</div><div class="text-phoenix">{st.session_state.gift}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area nav-container">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    if st.button("Hái lộc khác ↺", key="reset_btn"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Về trang chủ", key="home_btn"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
