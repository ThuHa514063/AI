import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hái Lộc Bính Ngọ 2026", page_icon="🧨", layout="centered")

# --- 2. KHO LỜI CHÚC (ĐÃ SỬA VIẾT HOA) ---
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

# --- 3. CSS TỔNG LỰC: ÉP FONT TOÀN BỘ & CHỈNH SIZE ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* ÉP FONT TOÀN BỘ APP */
    * {{
        font-family: 'Dancing Script', cursive !important;
    }}

    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    /* HIỆU ỨNG HOA ĐÀO RƠI */
    @keyframes flower-drop {{
        0% {{ top: -10%; transform: translateX(0) rotate(0deg); }}
        100% {{ top: 100%; transform: translateX(100px) rotate(360deg); }}
    }}
    .petal {{
        position: fixed; color: #ffb7c5; font-size: 25px;
        z-index: 999; pointer-events: none;
        animation: flower-drop 10s linear infinite;
    }}

    /* KHUNG CHỮ CHÍNH */
    .glass-box {{
        position: absolute; top: 2%; left: 50%; transform: translateX(-50%);
        width: 95%; max-width: 900px; background: rgba(139, 0, 0, 0.85); 
        backdrop-filter: blur(15px); padding: 25px; border-radius: 30px;
        border: 4px solid #FFD700; text-align: center; z-index: 100;
    }}
    
    /* Tiêu đề dùng Great Vibes cho nghệ */
    .title-dragon {{ 
        font-family: 'Great Vibes', cursive !important; 
        color: #FFD700 !important; 
        font-size: 80px !important; 
        text-shadow: 4px 4px 10px #000; 
    }}
    
    .text-phoenix {{ color: #F8F9FA !important; font-size: 40px !important; }}

    .interaction-area {{ margin-top: 420px; text-align: center; width: 100%; }}

    /* INPUT TÊN */
    div.stTextInput input {{
        font-size: 18px !important; 
        text-align: center; height: 45px !important; border: 2px solid #FFD700 !important;
        border-radius: 15px !important;
        background-color: white !important;
        color: black !important;
    }}

    /* SET SIZE CHO OPTION (50px, VIẾT THƯỜNG) */
    .option-container div.stButton > button {{
        height: 160px !important;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #B8860B 100%) !important;
        border: 4px solid #ffffff !important;
        border-radius: 20px !important;
        text-transform: none !important; /* Không tự động viết hoa */
    }}
    .option-container div.stButton > button p {{
        font-size: 50px !important; 
        font-weight: 900 !important;
        color: #800000 !important;
    }}

    /* SET SIZE CHO NÚT CHUYỂN TIẾP */
    .nav-container div.stButton > button {{
        height: 70px !important; max-width: 350px !important; margin: 0 auto !important;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        border-radius: 50px !important; border: 3px solid #fff !important;
        text-transform: none !important;
    }}
    .nav-container div.stButton > button p {{
        font-size: 28px !important;
        color: #800000 !important;
    }}

    .stButton > button:hover {{ transform: scale(1.05) !important; background: white !important; }}
    .stButton > button:hover p {{ color: red !important; }}
    </style>

    <div class="petal" style="left:10%; animation-duration:7s;">🌸</div>
    <div class="petal" style="left:30%; animation-duration:10s;">🌸</div>
    <div class="petal" style="left:50%; animation-duration:8s;">🌸</div>
    <div class="petal" style="left:70%; animation-duration:12s;">🌸</div>
    <div class="petal" style="left:90%; animation-duration:9s;">🌸</div>
""", unsafe_allow_html=True)

# --- 4. LOGIC ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# BƯỚC 1: TRANG CHỦ
if st.session_state.step == 1:
    st.markdown('<div class="glass-box"><div class="title-dragon">Happy New Year</div><div class="text-phoenix">🏮 Xuân bính ngọ 2026 🏮</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên của bạn vào đây nhé...", key="name_input")
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    if st.button("Bắt đầu hái lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN OPTION
elif st.session_state.step == 2:
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div><div class="text-phoenix">Chọn một túi lộc bên dưới nhé</div></div>', unsafe_allow_html=True)
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
