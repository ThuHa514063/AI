import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. KHO LỜI CHÚC (RANDOM) ---
luck_data = {
    "❤️ Tình Duyên": ["Hạnh phúc viên mãn, sớm tìm thấy nửa kia!", "Tình duyên nở rộ, vạn người theo đuổi!", "Năm mới có hỷ sự, tình cảm thăng hoa!"],
    "💼 Sự Nghiệp": ["Công thành danh toại, thăng quan tiến chức!", "Sự nghiệp bứt phá, khẳng định vị thế!", "Quý nhân phù trợ, làm gì thắng đó!"],
    "🐎 Sức Khỏe": ["Khỏe như ngựa chiến, vạn dặm bình an!", "Năng lượng dồi dào, tinh thần minh mẫn!", "Thân cường tật nhược, trẻ mãi không già!"],
    "💰 Tiền Tài": ["Tiền vào như nước, ví luôn căng đầy!", "Lộc phát đầy kho, vàng bạc đầy tay!", "Đầu tư đâu thắng đó, tài lộc bủa vây!"],
    "🏠 Gia Đình": ["Gia đạo bình an, ấm êm hạnh phúc!", "Cả nhà sum vầy, tiếng cười rộn rã!", "Trên dưới thuận hòa, vạn sự như ý!"],
    "🎓 Học Tập": ["Học một biết mười, thi cử đỗ đạt!", "Kiến thức uyên thâm, đạt học bổng cao!", "Đường học rộng mở, công danh rạng rỡ!"],
    "🍀 May Mắn": ["Vạn sự như ý, tỷ sự như mơ!", "Cầu được ước thấy, may mắn mỉm cười!", "Vận khí hanh thông, hóa hung thành cát!"],
    "🎁 Bất Ngờ": ["Quà khủng sắp tới, niềm vui nhân đôi!", "Một bước ngoặt mới đầy thú vị!", "Vạn điều kỳ diệu đang chờ đợi bạn!"]
}

# --- 3. GIAO DIỆN CSS: OPTION SIÊU TO KHỔNG LỒ ---
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

    .glass-box {{
        position: absolute;
        top: 5%; left: 50%;
        transform: translateX(-50%);
        width: 95%; max-width: 900px;
        background: rgba(139, 0, 0, 0.8); 
        backdrop-filter: blur(15px);
        padding: 30px 20px;
        border-radius: 30px;
        border: 4px solid #FFD700;
        text-align: center;
        z-index: 100;
    }}

    .title-dragon {{ font-family: 'Great Vibes', cursive !important; color: #FFD700 !important; font-size: 85px !important; text-shadow: 4px 4px 10px #000000; }}
    .text-phoenix {{ font-family: 'Dancing Script', cursive !important; color: #F8F9FA !important; font-size: 45px !important; text-shadow: 3px 3px 6px #000000; }}

    .interaction-area {{
        margin-top: 450px; 
        text-align: center;
        display: flex; flex-direction: column; align-items: center;
        width: 100%;
    }}

    /* Ô NHẬP TÊN: TINH TẾ (GIẢM SIZE NHƯ Ý ÔNG) */
    div.stTextInput {{ width: 100% !important; max-width: 800px !important; }}
    div.stTextInput > div > div > input {{
        font-family: 'Dancing Script', cursive !important;
        font-size: 16px !important; 
        text-align: center;
        border-radius: 12px;
        height: 45px !important;
        border: 2px solid #FFD700 !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
    }}

    /* CẤU TRÚC NÚT BẤM CHUNG */
    .stButton > button {{
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #B8860B 100%) !important;
        border: 4px solid #ffffff !important;
        border-radius: 30px !important;
        box-shadow: 0px 15px 30px rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
        transition: all 0.3s ease !important;
    }}
    .stButton > button p {{
        font-family: 'Dancing Script', cursive !important;
        font-weight: 900 !important;
        color: #800000 !important;
        margin: 0 !important;
    }}

    /* NÚT BẮT ĐẦU: CÂN ĐỐI */
    .start-btn-container .stButton > button {{
        width: 380px !important;
        height: 85px !important;
    }}
    .start-btn-container .stButton > button p {{ font-size: 32px !important; }}

    /* CÁC NÚT OPTION: PHÓNG TO HẾT CỠ (MAX SIZE) */
    .option-btn-container .stButton > button {{
        width: 100% !important;
        height: 160px !important; /* SIÊU CAO */
    }}
    .option-btn-container .stButton > button p {{
        font-size: 55px !important; /* SIÊU TO */
    }}

    .stButton > button:hover {{ transform: scale(1.05) translateY(-5px); background: #ffffff !important; }}
    .stButton > button:hover p {{ color: #FF0000 !important; }}

    [data-testid="stImage"] img {{ width: 100% !important; max-width: 650px !important; border-radius: 25px; border: 5px solid #FFD700; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LOGIC ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

# BƯỚC 1: TRANG CHỦ
if st.session_state.step == 1:
    st.markdown('<div class="glass-box"><div class="title-dragon">Happy New Year</div><div class="text-phoenix">🏮 Xuân Bính Ngọ 2026 🏮</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên để nhận lộc đại cát...", key="name_input")
    st.markdown('<div class="start-btn-container">', unsafe_allow_html=True)
    if st.button("Bắt Đầu Hái Lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN OPTION (SIÊU TO)
elif st.session_state.step == 2:
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div><div class="text-phoenix">Chọn một đại lộc khổng lồ bên dưới</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area option-btn-container">', unsafe_allow_html=True)
    
    # Chia 2 cột nhưng mỗi nút đều to hoành tráng
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
    st.markdown(f'<div class="glass-box"><div class="title-dragon">Vạn Sự Như Ý</div><div class="text-phoenix">{st.session_state.gift}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="interaction-area start-btn-container">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    if st.button("Hái Lộc Khác ↺", key="reset_btn"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Về Trang Chủ", key="home_btn"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
