import streamlit as st
import random
import streamlit.components.v1 as components

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hái Lộc Bính Ngọ 2026", page_icon="🧨", layout="centered")

# --- 2. JAVASCRIPT ĐỂ TỰ ĐỘNG CUỘN LÊN ĐẦU TRANG ---
components.html(
    """
    <script>
        window.parent.document.querySelector(".main").scrollTo(0,0);
    </script>
    """,
    height=0,
)

# --- 3. KHO LỜI CHÚC ĐA DẠNG ---
luck_data = {
    "❤️ Tình duyên": ["Hạnh phúc viên mãn, sớm tìm thấy nửa kia nhé!", "Tình duyên nở rộ, vạn người theo đuổi luôn!", "Năm mới có hỷ sự, tình cảm thăng hoa nha!"],
    "💼 Sự nghiệp": ["Công thành danh toại, thăng quan tiến chức nhé!", "Sự nghiệp bứt phá, khẳng định vị thế nha!", "Quý nhân phù trợ, làm gì cũng thuận lợi nhé!"],
    "🐎 Sức khỏe": ["Khỏe như ngựa chiến, vạn dặm bình an nhé!", "Năng lượng dồi dào, tinh thần minh mẫn nha!"],
    "💰 Tiền tài": ["Tiền vào như nước, ví luôn căng đầy nhé!", "Lộc phát đầy kho, vàng bạc đầy tay nha!"],
    "🏠 Gia đình": ["Gia đạo bình an, ấm êm hạnh phúc nhé!", "Cả nhà sum vầy, tiếng cười rộn rã nha!"],
    "🎓 Học tập": ["Học một biết mười, thi cử đỗ đạt nhé!", "Kiến thức uyên thâm, đạt học bổng cao nha!"],
    "🍀 May mắn": ["Vạn sự như ý, tỷ sự như mơ nhé!", "Cầu được ước thấy, may mắn mỉm cười nha!"],
    "🎁 Bất ngờ": ["Quà khủng sắp tới, niềm vui nhân đôi nhé!", "Một bước ngoặt mới đầy thú vị nha!"]
}

# --- 4. CSS TỔNG LỰC (SET SIZE GIF LỚN HƠN) ---
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* ÉP FONT TOÀN BỘ */
    html, body, [class*="st-"], * {{
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
        0% {{ top: -10%; transform: rotate(0deg) translateX(0); }}
        100% {{ top: 100%; transform: rotate(360deg) translateX(50px); }}
    }}
    .petal {{
        position: fixed; color: #ffb7c5; font-size: 25px;
        z-index: 999; pointer-events: none;
        animation: flower-drop 10s linear infinite;
    }}

    /* KHUNG TIÊU ĐỀ */
    .glass-box {{
        position: relative; margin: 10px auto;
        width: 95%; max-width: 850px; background: rgba(139, 0, 0, 0.85); 
        padding: 25px; border-radius: 25px;
        border: 4px solid #FFD700; text-align: center;
    }}
    .title-dragon {{ font-family: 'Great Vibes', cursive !important; color: #FFD700; font-size: 65px; text-shadow: 2px 2px 10px #000; }}
    .text-phoenix {{ color: #F8F9FA; font-size: 35px; margin-top: 10px; }}

    .interaction-area {{ margin-top: 40px; text-align: center; width: 100%; }}

    @media (min-width: 768px) {{
        .interaction-area {{ margin-top: 380px; }}
        .title-dragon {{ font-size: 85px; }}
    }}

    /* INPUT TÊN */
    div.stTextInput input {{
        font-size: 18px !important; text-align: center;
        height: 45px !important; border: 2px solid #FFD700 !important;
        border-radius: 12px; background: white !important;
    }}

    /* NÚT OPTION (50px) */
    .option-container div.stButton > button {{
        height: 160px !important; margin-bottom: 20px !important;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        border: 3px solid #fff !important; text-transform: none !important;
    }}
    .option-container div.stButton > button p {{
        font-size: 50px !important; font-weight: 900 !important; color: #800000 !important;
    }}

    /* NÚT NAV */
    .nav-container div.stButton > button {{
        height: 70px !important; max-width: 350px !important; margin: 0 auto !important;
        border-radius: 40px !important; border: 2px solid #fff !important;
        background: #FFD700 !important; text-transform: none !important;
    }}
    .nav-container div.stButton > button p {{ font-size: 28px !important; color: #800000 !important; }}

    /* --- SET SIZE GIF LỚN HƠN TẠI ĐÂY --- */
    [data-testid="stImage"] img {{
        max-width: 650px !important; /* Tăng từ 450 lên 650px cho GIF to rõ */
        width: 100% !important;
        height: auto !important;
        border-radius: 25px;
        border: 5px solid #FFD700;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.6);
        margin: 20px auto !important;
    }}

    .stButton > button:hover {{ transform: scale(1.03) !important; background: white !important; }}
    </style>

    <div class="petal" style="left:15%; animation-duration:8s;">🌸</div>
    <div class="petal" style="left:45%; animation-duration:11s;">🌸</div>
    <div class="petal" style="left:75%; animation-duration:9s;">🌸</div>
""", unsafe_allow_html=True)

# --- 5. LOGIC CHƯƠNG TRÌNH ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# BƯỚC 1: TRANG CHỦ
if st.session_state.step == 1:
    st.markdown('<div class="glass-box"><div class="title-dragon">Happy New Year</div><div class="text-phoenix">🏮 Xuân bính ngọ 2026 🏮</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên của bạn vào đây nha...", key="name_input")
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    if st.button("Bắt đầu hái lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN OPTION
elif st.session_state.step == 2:
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div><div class="text-phoenix">Chọn một túi lộc bất kỳ nhé</div></div>', unsafe_allow_html=True)
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
# BƯỚC 3: KẾT QUẢ
elif st.session_state.step == 3:
    st.balloons()
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Vạn sự như ý</div><div class="text-phoenix">{st.session_state.gift}</div></div>', unsafe_allow_html=True)
    
    # --- KHU VỰC 2 ẢNH HÀNG NGANG ---
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    
    col_img1, col_img2 = st.columns(2) # Chia làm 2 cột
    
    with col_img1:
        st.image("https://i.pinimg.com/originals/5d/74/75/5d74758107b2ae3ba50e4a163a1f4596.gif", use_container_width=True)
        
    with col_img2:
        # Ông thay link ảnh thứ 2 vào đây nhé
        st.image("https://i.pinimg.com/originals/5d/74/75/5d74758107b2ae3ba50e4a163a1f4596.gif", use_container_width=True)
    
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    if st.button("Hái lộc khác ↺", key="reset_btn"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Về trang chủ", key="home_btn"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)
