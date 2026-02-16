import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới Bính Ngọ 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS & PHÁO HOA & FONT CHỮ ---
# Thay link ảnh nền của bạn ở đây
background_image_url = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Lớp phủ đen làm mờ nền */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6); 
        z-index: -1;
    }}

    h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: 85px !important;
        text-shadow: 3px 3px 6px #000000;
        text-align: center;
        margin-bottom: 0px !important;
    }}

    h2, h3, p, .stMarkdown {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: 30px !important;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }}

    /* Căn giữa tất cả ảnh/GIF */
    .stImage {{
        display: flex;
        justify-content: center;
    }}

    /* Tùy chỉnh nút bấm */
    .stButton>button {{
        border-radius: 30px;
        border: 2px solid #FFD700;
        background-color: rgba(220, 20, 60, 0.8);
        color: white;
        font-family: 'Dancing Script', cursive;
        font-size: 22px;
        width: 100%;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #FFD700;
        color: #000;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {{
            confetti({{ 
                particleCount: 100, 
                spread: 70, 
                origin: {{ y: 0.6 }}, 
                colors: ['#ff0000', '#ffd700', '#ffffff'] 
            }});
        }}
        setInterval(fire, 3000); // Nổ pháo mỗi 3 giây
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. KHO LỜI CHÚC NGẪU NHIÊN ---
luck_messages = {
    "💰 Tài Lộc": [
        "Tiền vào như nước sông Đà, tiền ra nhỏ giọt như cà phê phin!",
        "Năm mới Bính Ngọ, túi tiền rủng rỉnh, mã đáo thành công!",
        "Lộc tràn vào nhà, vinh hoa phú quý, tiêu xài không hết!",
        "Vàng bạc đầy kho, vạn sự hanh thông!"
    ],
    "🌸 Tình Duyên": [
        "Năm nay thoát kiếp FA, người thương tìm đến tận cửa nhà!",
        "Tình duyên phơi phới, hạnh phúc nhân đôi, vạn sự như ý!",
        "Sớm tìm được ý trung nhân, tình yêu nồng cháy như pháo giao thừa!",
        "Hạnh phúc ngọt ngào, gia đình êm ấm!"
    ],
    "🐎 Sức Khỏe": [
        "Sức khỏe dẻo dai như ngựa chiến, cả năm không mệt mỏi!",
        "Ăn ngon ngủ kỹ, tinh thần sảng khoái, vạn dặm bình an!",
        "Trẻ mãi không già, năng lượng tràn đầy, vui vẻ mỗi ngày!",
        "Khỏe như rồng, mạnh như hổ, phi nhanh như ngựa!"
    ]
}

# --- 4. QUẢN LÝ CÁC BƯỚC ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- 5. GIAO DIỆN TỪNG BƯỚC ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.title("Chúc Mừng Năm Mới")
    st.write("Xuân Bính Ngọ 2026")
    name_input = st.text_input("Quý danh của bạn là gì?", placeholder="Nhập tên tại đây...")
    if st.button("Khám Phá Lộc Xuân ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Vui lòng cho mình biết tên nhé!")

# BƯỚC 2: CHỌN GÓI QUÀ
elif st.session_state.step == 2:
    st.title(f"Chào {st.session_state.name}")
    st.subheader("Hãy chọn một gói lộc may mắn cho năm nay:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💰 Tài Lộc"):
            st.session_state.gift = random.choice(luck_messages["💰 Tài Lộc"])
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🌸 Tình Duyên"):
            st.session_state.gift = random.choice(luck_messages["🌸 Tình Duyên"])
            st.session_state.step = 3
            st.rerun()
    with col3:
        if st.button("🐎 Sức Khỏe"):
            st.session_state.gift = random.choice(luck_messages["🐎 Sức Khỏe"])
            st.session_state.step = 3
            st.rerun()

# BƯỚC 3: HIỆN KẾT QUẢ VÀ ẢNH RIÊNG
elif st.session_state.step == 3:
    st.title("Vạn Sự Như Ý")
    st.balloons()
    
    st.write(f"Lời chúc dành riêng cho **{st.session_state.name}**:")
    st.success(st.session_state.gift)
    
    # GIF Ngựa căn giữa
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=250)

    st.markdown("---")
    st.write("🎁 Quà tặng hình ảnh bí mật:")

    # --- PHẦN KIỂM TRA TÊN ĐỂ HIỆN ẢNH RIÊNG ---
    # Chuyển tên về chữ thường để so sánh
    ten_check = st.session_state.name.lower().strip()

    # BẠN SỬA TÊN VÀ LINK ẢNH Ở ĐÂY NHÉ:
    if ten_check == "tên của người yêu": 
        st.image("LINK_ẢNH_NGƯỜI_YÊU", caption="Chúc bé yêu năm mới xinh đẹp!")
        
    elif ten_check == "tên của bạn thân":
        st.image("LINK_ẢNH_BẠN_THÂN", caption="Mãi là anh em tốt nhé!")
        
    elif ten_check == "mẹ" or ten_check == "ba":
        st.image("LINK_ẢNH_GIA_ĐÌNH", caption="Con chúc Ba Mẹ luôn mạnh khỏe!")

    else:
        # Nếu không trúng tên nào ở trên, hiện ảnh Tết ngẫu nhiên
        st.image(f"https://picsum.photos/400/300?random={random.randint(1,100)}", 
                 caption=f"Món quà ngẫu nhiên dành cho {st.session_state.name}")

    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()
