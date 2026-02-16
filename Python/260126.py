import streamlit as st
import random

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. KHO LỜI CHÚC (RANDOM) ---
luck_data = {
    "❤️ Tình Duyên": [
        "Tình duyên nở rộ, sớm tìm thấy nửa kia đích thực!",
        "Hạnh phúc viên mãn, tình cảm gia đình thêm gắn kết!",
        "Vạn người theo đuổi, nhận được lời tỏ tình như ý!",
        "Tình yêu thăng hoa, năm mới có hỷ sự lâm môn!"
    ],
    "💼 Sự Nghiệp": [
        "Công việc hanh thông, thăng quan tiến chức vèo vèo!",
        "Sự nghiệp bứt phá, khẳng định được vị thế bản thân!",
        "Gặp được quý nhân phù trợ, mọi việc đều suôn sẻ!",
        "Mở rộng kinh doanh, đối tác tin cậy, thành công rực rỡ!"
    ],
    "🐎 Sức Khỏe": [
        "Khỏe như ngựa chiến, cả năm không lo ốm đau!",
        "Tinh thần minh mẫn, năng lượng dồi dào mỗi ngày!",
        "Thân cường tật nhược, dẻo dai vạn dặm bình an!",
        "Sức khỏe vàng, vui sống mỗi ngày cùng người thân!"
    ],
    "💰 Tiền Tài": [
        "Tiền vào như nước sông Đà, tiền ra nhỏ giọt như cà phê phin!",
        "Lộc phát đầy kho, ví luôn dày cộm, vàng bạc đầy tay!",
        "Đầu tư đâu thắng đó, tài lộc bủa vây cả năm!",
        "Tiền tài rủng rỉnh, mua nhà sắm xe trong tầm tay!"
    ],
    "🏠 Gia Đình": [
        "Gia đạo bình an, trên dưới thuận hòa, ấm êm hạnh phúc!",
        "Cả nhà sum vầy, tiếng cười rộn rã suốt cả năm!",
        "Con cháu hiếu thảo, ông bà bách niên giai lão!",
        "Mọi thành viên đều mạnh khỏe, gắn bó yêu thương nhau!"
    ],
    "🎓 Học Tập": [
        "Học một biết mười, thi cử đỗ đạt vị trí dẫn đầu!",
        "Kiến thức uyên thâm, mở mang trí tuệ, đạt học bổng cao!",
        "Vượt qua mọi kỳ thi một cách nhẹ nhàng, xuất sắc!",
        "Đường học vấn rộng mở, tìm được đam mê đích thực!"
    ],
    "🍀 May Mắn": [
        "Vạn sự như ý, tỷ sự như mơ, triệu điều bất ngờ!",
        "Quay tay vận may tới, làm gì cũng gặp thuận lợi!",
        "Cầu được ước thấy, may mắn luôn mỉm cười với bạn!",
        "Vận khí hanh thông, hóa hung thành cát, vạn sự bình an!"
    ],
    "🎁 Bất Ngờ": [
        "Một món quà vô giá sắp đến với bạn trong tháng này!",
        "Cuộc sống sẽ có bước ngoặt mới đầy thú vị và hạnh phúc!",
        "Bạn sắp nhận được tin vui cực lớn từ phương xa!",
        "Niềm vui nhân đôi, nỗi buồn tan biến, vạn điều kỳ diệu!"
    ]
}

# --- 3. GIAO DIỆN CSS ---
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
        top: 8%; left: 50%;
        transform: translateX(-50%);
        width: 90%; max-width: 800px;
        background: rgba(139, 0, 0, 0.65); 
        backdrop-filter: blur(15px);
        padding: 40px 20px;
        border-radius: 30px;
        border: 2px solid rgba(255, 215, 0, 0.7);
        text-align: center;
        z-index: 100;
    }}

    .title-dragon {{ font-family: 'Great Vibes', cursive !important; color: #FFD700 !important; font-size: 70px !important; text-shadow: 4px 4px 8px #000000; margin: 0; }}
    .text-phoenix {{ font-family: 'Dancing Script', cursive !important; color: #F8F9FA !important; font-size: 40px !important; text-shadow: 3px 3px 6px #000000; }}

    .interaction-area {{
        margin-top: 450px; 
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* NHẬP TÊN BÉ LẠI */
    div.stTextInput {{ width: 280px !important; }}
    div.stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 10px;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 18px !important;
        height: 40px !important;
    }}

    /* OPTION TO RÕ */
    .stButton > button {{
        background: linear-gradient(135deg, #FFD700, #FFA500) !important;
        color: #800000 !important;
        font-family: 'Dancing Script', cursive !important;
        font-weight: bold !important;
        font-size: 32px !important;
        border-radius: 20px !important;
        border: 2px solid #ffffff !important;
        width: 100% !important;
        height: 80px !important;
        margin-bottom: 10px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.4);
    }}

    [data-testid="stImage"] img {{ width: 100% !important; max-width: 500px !important; border-radius: 20px; border: 4px solid #FFD700; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""
if 'gift' not in st.session_state: st.session_state.gift = ""

# --- 5. LOGIC CHƯƠNG TRÌNH ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.markdown("""<div class="glass-box"><div class="title-dragon">Happy New Year</div>
                <div class="text-phoenix">🏮 Xuân Bính Ngọ 2026 🏮</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    name = st.text_input("", placeholder="Nhập tên của bạn...", key="name_input")
    if st.button("Khai Xuân Nhận Lộc ➔", key="start_btn"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# BƯỚC 2: CHỌN TÚI LỘC (8 OPTION)
elif st.session_state.step == 2:
    st.markdown(f"""<div class="glass-box"><div class="title-dragon">Chào {st.session_state.name}</div>
                <div class="text-phoenix">Bạn muốn nhận lộc gì nhất?</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="interaction-area">', unsafe_allow_html=True)
    
    # Chia làm 2 cột, mỗi cột 4 nút
    col1, col2 = st.columns(2)
    options = list(luck_data.keys())
    
    for i, opt in enumerate(options):
        with (col1 if i % 2 == 0 else col2):
            if st.button(opt, key=f"opt_{i}"):
                # RANDOM LỜI CHÚC TRONG CATEGORY ĐÃ CHỌN
                st.session_state.gift = random.choice(luck_data[opt])
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
    
    if st.button("Chọn lộc khác ↺", key="reset_btn"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Về trang chủ", key="home_btn"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
