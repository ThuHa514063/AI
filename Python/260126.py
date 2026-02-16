import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🐎", layout="centered")

# --- PHẦN 1: CÀI ĐẶT BACKGROUND & PHÁO HOA ---
# Bạn có thể thay link ảnh nền ở dòng 'background-image' bên dưới
background_image_url = "https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/634841953_1357693106160997_7648237787659667592_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHJf9AM3HXJ6kfr-qgw9rjx1-Jcnnd5zF_X4lyed3nMX9wVLwF7e8n5eTVfZLd-py4hGknrSIXd9W_kqVRkgKfW&_nc_ohc=oAt5f1xFjEsQ7kNvwHRx6y_&_nc_oc=AdnOB3WYKuDCTz-x7aC9jr_LvcZCa5iKY8HVLJe5MlTyajQNK81csXN3udEbHjOJpXtIIMIY_rO0rPrSgYSlCZhq&_nc_zt=23&_nc_ht=scontent.fhan4-3.fna&_nc_gid=dJNyq-MhsfFyiv7V2T1_Bw&oh=00_Afsv-Fz9l1RH10V4gLuDlb9uEemSjsuariKmQt1pMADemw&oe=69991725" 

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* Làm mờ một chút để dễ đọc chữ */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6); 
        z-index: -1;
    }}
    h1, h2, h3, p, .stMarkdown {{
        color: #FFD700 !important; /* Màu vàng đồng cho hợp không khí Tết */
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }}
    </style>
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var count = 200;
        var defaults = {{ origin: {{ y: 0.7 }} }};

        function fire(particleRatio, opts) {{
          confetti(Object.assign({{}}, defaults, opts, {{
            particleCount: Math.floor(count * particleRatio)
          }}));
        }}

        function autoFire() {{
            fire(0.25, {{ spread: 26, startVelocity: 55 }});
            fire(0.2, {{ spread: 60 }});
            fire(0.35, {{ spread: 100, decay: 0.91, scalar: 0.8 }});
            fire(0.1, {{ spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 }});
            fire(0.1, {{ spread: 120, startVelocity: 45 }});
        }}
        
        // Bắn pháo hoa mỗi 3 giây
        setInterval(autoFire, 3000);
        autoFire(); 
    </script>
""", unsafe_allow_html=True)

# --- QUẢN LÝ CÁC BƯỚC (SESSION STATE) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- GIAO DIỆN TỪNG BƯỚC ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.title("🧧 XUÂN BÍNH NGỌ 2026 🐎")
    st.write("Chào mừng bạn đến với trang chúc Tết!")
    name_input = st.text_input("Nhập tên của bạn để bắt đầu:", placeholder="Tên bạn là...")
    if st.button("Tiếp tục ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("Hãy nhập tên nhé!")

# BƯỚC 2: CHỌN LỘC
elif st.session_state.step == 2:
    st.title(f"🐎 Chào {st.session_state.name}!")
    st.subheader("Chọn một túi lộc may mắn cho năm Bính Ngọ:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💰 Tài Lộc"):
            st.session_state.gift = "Tiền vào như nước, Mã đáo thành công!"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("❤️ Tình Duyên"):
            st.session_state.gift = "Hạnh phúc đong đầy, vạn sự như ý!"
            st.session_state.step = 3
            st.rerun()

# BƯỚC 3: KẾT QUẢ
elif st.session_state.step == 3:
    st.title("🎊 CHÚC MỪNG NĂM MỚI! 🎊")
    st.balloons() # Kết hợp cả bóng bay của Streamlit
    st.header(f"Chúc {st.session_state.name}:")
    st.success(st.session_state.gift)
    
    # Bạn có thể thay link ảnh GIF ngựa ở đây
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    if st.button("Quay lại từ đầu"):
        st.session_state.step = 1
        st.rerun()
