import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hái Lộc Bính Ngọ 2026", page_icon="🧨", layout="centered")

# --- 2. KHO LỜI CHÚC ---
luck_data = {
    "❤️ Tình Duyên": ["Hạnh phúc viên mãn, sớm tìm thấy nửa kia!", "Tình duyên nở rộ, vạn người theo đuổi!"],
    "💼 Sự Nghiệp": ["Công thành danh toại, thăng quan tiến chức!", "Sự nghiệp bứt phá, khẳng định vị thế!"],
    "🐎 Sức Khỏe": ["Khỏe như ngựa chiến, vạn dặm bình an!", "Năng lượng dồi dào, tinh thần minh mẫn!"],
    "💰 Tiền Tài": ["Tiền vào như nước, ví luôn căng đầy!", "Lộc phát đầy kho, vàng bạc đầy tay!"],
    "🏠 Gia Đình": ["Gia đạo bình an, ấm êm hạnh phúc!", "Cả nhà sum vầy, tiếng cười rộn rã!"],
    "🎓 Học Tập": ["Học một biết mười, thi cử đỗ đạt!", "Kiến thức uyên thâm, đạt học bổng cao!"],
    "🍀 May Mắn": ["Vạn sự như ý, tỷ sự như mơ!", "Cầu được ước thấy, may mắn mỉm cười!"],
    "🎁 Bất Ngờ": ["Quà khủng sắp tới, niềm vui nhân đôi!", "Một bước ngoặt mới đầy thú vị!"]
}

# --- 3. CSS: HIỆU ỨNG BAY LẢ TẢ & SIÊU OPTION ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* Nền và Hiệu ứng hoa rơi */
    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    /* Hiệu ứng hoa đào rơi */
    @keyframes snowflakes {{
        0% {{ transform: translateY(-10vh) rotate(0deg); }}
        100% {{ transform: translateY(110vh) rotate(360deg); }}
    }}
    .flower {{
        position: fixed; top: -10%; z-index: 9999;
        user-select: none; cursor: default;
        animation: snowflakes 10s linear infinite;
    }}

    .glass-box {{
        position: absolute; top: 2%; left: 50%; transform: translateX(-50%);
        width: 95%; max-width: 900px; background: rgba(139, 0, 0, 0.85); 
        backdrop-filter: blur(15px); padding: 25px; border-radius: 30px;
        border: 4px solid #FFD700; text-align: center; z-index: 100;
    }}

    .title-dragon {{ font-family: 'Great Vibes', cursive; color: #FFD700; font-size: 80px; text-shadow: 4px 4px 10px #000; }}
    .text-phoenix {{ font-family: 'Dancing Script', cursive; color: #F8F9FA; font-size: 40px; }}

    .interaction-area {{ margin-top: 420px; text-align: center; width: 100%; }}

    /* Input tên */
    div.stTextInput {{ width: 100% !important; max-width: 850px !important; margin: 0 auto !important; }}
    div.stTextInput input {{
        font-family: 'Dancing Script', cursive; font-size: 16px !important; 
        text-align: center; height: 45px !important; border: 2px solid #FFD700 !important;
    }}

    /* CHỈNH OPTION: TĂNG SIZE CHỮ LÊN ĐÚNG 50PX */
    .option-container div.stButton > button {{
        height: 170px !important;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        border: 4px solid #fff !important;
        border-radius: 20px !important;
        margin-bottom: 20px !important;
    }}
    .option-container div.stButton > button p {{
        font-family: 'Dancing Script', cursive !important;
        font-size: 50px !important; /* ĐÚNG 50PX THEO Ý ÔNG */
        font-weight: 900 !important;
        color: #800000 !important;
    }}

    /* NÚT ĐIỀU HƯỚNG: GIỮ NGUYÊN BÉ XINH */
    .nav-container div.stButton > button {{
        max-width: 350px !important; margin: 0 auto !important;
        height: 70px !important; border-radius: 50px !important;
    }}
    .nav-container div.stButton > button p {{ font-size: 28px !important; font-family: 'Dancing Script', cursive !important; }}

    .stButton > button:hover {{ transform: scale(1.05); }}
    </style>

    <div class="flower" style="left:10%; font-size:20px; animation-duration:8s;">🌸</div>
    <div class="flower" style="left:25%; font-size:25px; animation-duration:12s;">🌼</div>
    <div class="flower" style="left:40%; font-size:18px; animation-duration:7s;">🌸</div>
    <div class="flower" style="left:55%; font-size:22px; animation-duration:10s;">🌼</div>
    <div class="flower" style="left:70%; font-size:28px; animation-duration:11s;">🌸</div>
    <div class="flower" style="left:85%; font-size:20px; animation-duration:9s;">🌼</div>
""", unsafe_allow_html=True)

# --- 4. LOGIC ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# BƯỚC 1: TRANG CHỦ
if st.session_state.step == 1:
    st.markdown('<div class="glass-box"><div class="title-dragon">Happy New Year</div><div class="text-phoenix">🏮 Xuân Bính Ngọ 2026 🏮</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên để hái lộc...", key="name_input")
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    if st.button("Bắt Đầu Hái Lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN OPTION (SIZE 50PX)
elif st.session_state.step == 2:
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div><div class="text-phoenix">Chọn túi lộc khổng lồ</div></div>', unsafe_allow_html=True)
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
    st.snow() # Hiệu ứng tuyết rơi của Streamlit (giống pháo giấy)
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Vạn Sự Như Ý</div><div class="text-phoenix">{st.session_state.gift}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area nav-container">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    if st.button("Hái Lộc Khác ↺", key="reset_btn"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Về Trang Chủ", key="home_btn"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
