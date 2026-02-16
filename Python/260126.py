import streamlit as st
import random
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- 2. GIAO DIỆN CSS HIỆN ĐẠI ---
# Link background bạn gửi
bg_link = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Pacifico&display=swap');

    .stApp {{
        background-image: url("{bg_link}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Tạo một lớp phủ nhẹ để bảo vệ mắt */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.2);
        z-index: -1;
    }}

    /* Container bao quanh nội dung cho đẹp */
    .main-container {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        text-align: center;
    }}

    h1 {{
        font-family: 'Pacifico', cursive !important;
        color: #FFD700 !important;
        font-size: 60px !important;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}

    h2, h3, p, div, span, label {{
        font-family: 'Montserrat', sans-serif !important;
        color: white !important;
    }}

    /* Căn giữa Image/Gif tuyệt đối */
    [data-testid="stImage"] {{
        display: flex !important;
        justify-content: center !important;
        margin: 20px auto !important;
    }}

    [data-testid="stImage"] img {{
        border-radius: 15px;
        border: 2px solid #FFD700;
        max-width: 100%;
    }}

    /* Nút bấm hiện đại */
    .stButton>button {{
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #800000 !important;
        font-weight: bold !important;
        border: none;
        border-radius: 50px;
        padding: 10px 25px;
        font-size: 18px;
        transition: 0.3s;
        width: 100%;
    }}

    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(255, 215, 0, 0.6);
    }}
    </style>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var end = Date.now() + (15 * 1000);
        function fire() {{
            confetti({{ particleCount: 3, angle: 60, spread: 55, origin: {{ x: 0 }}, colors: ['#FFD700', '#FF0000'] }});
            confetti({{ particleCount: 3, angle: 120, spread: 55, origin: {{ x: 1 }}, colors: ['#FFD700', '#FF0000'] }});
            if (Date.now() < end) {{ requestAnimationFrame(fire); }}
        }}
        fire();
    </script>
""", unsafe_allow_html=True)

# --- 3. LOGIC ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'name' not in st.session_state: st.session_state.name = ""

luck_dict = {
    "💰 Tiền Tài": ["Mã đáo thành công, tiền vào như nước!", "Năm mới Bính Ngọ, lộc phát đầy kho!"],
    "❤️ Tình Duyên": ["Hạnh phúc viên mãn, sớm tìm thấy chân ái!", "Tình duyên nở rộ, vui vẻ cả năm!"],
    "🐎 Sức Khỏe": ["Khỏe như ngựa chiến, vạn dặm bình an!", "Sức khỏe dồi dào, tinh thần minh mẫn!"]
}

# --- 4. GIAO DIỆN ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.title("Happy New Year")
    st.subheader("🏮 Xuân Bính Ngọ 2026 🏮")
    name = st.text_input("Vui lòng nhập tên của bạn:", placeholder="Tên bạn là...")
    if st.button("Bắt đầu hái lộc ➔"):
        if name:
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.title(f"Chào {st.session_state.name}")
    st.write("Hãy chọn một gói quà may mắn cho năm mới:")
    cols = st.columns(3)
    for i, gift_type in enumerate(luck_dict.keys()):
        with cols[i]:
            if st.button(gift_type):
                st.session_state.gift = random.choice(luck_dict[gift_type])
                st.session_state.step = 3
                st.rerun()

elif st.session_state.step == 3:
    st.title("Vạn Sự Như Ý")
    st.balloons()
    st.success(f"Chúc {st.session_state.name}: {st.session_state.gift}")
    
    # GIF Ngựa
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif", width=300)

    # Kiểm tra tên riêng để tặng quà
    name_check = st.session_state.name.lower().strip()
    if name_check == "tên_của_bạn": # Thay tên và link ở đây
        st.write("🎁 Quà đặc biệt cho bạn:")
        st.image("LINK_ẢNH_RIÊNG")
    else:
        st.write("🎁 Món quà ngẫu nhiên tặng bạn:")
        st.image(f"https://picsum.photos/400/300?random={random.randint(1,100)}")

    if st.button("Quay lại từ đầu ↺"):
        st.session_state.step = 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
