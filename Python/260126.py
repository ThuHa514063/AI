import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới Bính Ngọ 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS, PHÁO HOA & CĂN GIỮA ---
background_image_url = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');

    /* Nền trang web */
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Lớp phủ tối để nổi chữ */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6); 
        z-index: -1;
    }}

    /* Font chữ nghệ thuật */
    h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: #FFD700 !important;
        font-size: 80px !important;
        text-shadow: 3px 3px 6px #000000;
        text-align: center;
    }}

    h2, h3, p, .stMarkdown {{
        font-family: 'Dancing Script', cursive !important;
        color: #F8F9FA !important;
        font-size: 32px !important;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }}

    /* THỦ THUẬT CĂN GIỮA ẢNH VÀ GIF TUYỆT ĐỐI */
    [data-testid="stImage"] {{
        display: flex !important;
        justify-content: center !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}
    
    [data-testid="stImage"] img {{
        border-radius: 15px;
        border: 3px solid #FFD700;
    }}

    /* Nút bấm */
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
    
    /* Script Pháo hoa */
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
        setInterval(fire, 3000);
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. KHO LỜI CHÚC NGẪU NHIÊN ---
luck_messages = {
    "💰 Tài Lộc": [
        "Tiền vào như nước, ví luôn căng đầy!",
        "Mã đáo thành công, vạn sự như ý!",
        "Khai xuân phú quý, lộc phát vinh hoa!"
    ],
    "🌸 Tình Duyên": [
        "Năm nay có đôi, hạnh phúc rạng ngời!",
        "Tình duyên phơi phới, sớm gặp ý trung nhân!",
        "Yêu thương đong đầy, vạn dặm bình an!"
    ],
    "🐎 Sức Khỏe": [
        "Khỏe như ngựa chiến, bền bỉ dẻo dai!",
        "Tinh thần sảng khoái, trẻ mãi không già!",
        "Cả năm mạnh khỏe, không chút âu lo!"
    ]
}

# --- 4. QUẢN LÝ BƯỚC CHẠY ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- 5. GIAO DIỆN TỪNG BƯỚC ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.title("Chúc Mừng Năm Mới")
    st.write("Bính Ngọ 2026")
    name_input = st.text_input("Cho mình biết tên bạn nhé:", placeholder="Nhập tên tại đây...")
    if st.button("Bắt Đầu ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun()

# BƯỚC 2: CHỌN GÓI QUÀ (BƯỚC 1 SẼ BIẾN MẤT)
elif st.session_state.step == 2:
    st.title(f"Chào {st.session_state.name}")
    st.subheader("Hãy chọn một túi lộc may mắn:")
    
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

# BƯỚC 3: MÀN HÌNH CUỐI (CĂN GIỮA GIF & ẢNH RIÊNG)
elif st.session_state.step == 3:
    st.title("Vạn Sự Như Ý")
    st.balloons()
    
    st.success(f"Chúc {st.session_state.name}: {st.session_state.gift}")
    
    # GIF Ngựa (Mặc định - Đã căn giữa bằng CSS)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=300)

    st.write("---")
    
    # --- LOGIC KIỂM TRA TÊN ĐỂ TẶNG ẢNH ---
    ten_nhap = st.session_state.name.lower().strip()
    
    # NOTE: BẠN CHỈNH TÊN VÀ LINK ẢNH Ở ĐÂY
    if ten_nhap == "nguyễn văn a": # Thay bằng tên bạn muốn
        st.write("🎁 Quà tặng dành riêng cho bạn A:")
        st.image("LINK_ẢNH_CỦA_A", caption="Hình ảnh bí mật của bạn!")
        
    elif ten_nhap == "bé iu": # Ví dụ cho người yêu
        st.write("💖 Món quà ngọt ngào cho bé yêu:")
        st.image("LINK_ẢNH_CRUSH", caption="Chúc em luôn xinh đẹp!")
        
    else:
        # Nếu không trúng tên nào, hiện ảnh Tết ngẫu nhiên
        st.write("🎁 Một món quà ngẫu nhiên tặng bạn:")
        st.image(f"https://picsum.photos/400/300?random={random.randint(1,500)}", caption="May mắn cả năm nhé!")

    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()
