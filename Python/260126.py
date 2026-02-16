import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới Bính Ngọ 2026", page_icon="🐎", layout="centered")

# --- HIỆU ỨNG PHÁO HOA RỰC RỠ (SỬA LẠI) ---
st.markdown("""
    <canvas id="fireworksCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function shoot() {
            confetti({
                particleCount: 150,
                spread: 70,
                origin: { y: 0.6 },
                colors: ['#ff0000', '#ffd700', '#ffffff', '#ff4500']
            });
        }
        // Bắn pháo hoa ngay lập tức và lặp lại
        shoot();
        setInterval(shoot, 2000);
    </script>
    <style>
        .stApp {
            background-color: #0e1117;
            color: #ffd700;
        }
        h1, h2, h3 {
            color: #ff4b4b !important;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- QUẢN LÝ SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- GIAO DIỆN TỪNG BƯỚC ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.title("🧧 CHÀO ĐÓN XUÂN BÍNH NGỌ 2026 🐎")
    st.write("---")
    name_input = st.text_input("Vui lòng cho biết quý danh của bạn:", placeholder="Nhập tên tại đây...")
    if st.button("Tiếp tục ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Bạn chưa nhập tên mà!")

# BƯỚC 2: CHỌN QUÀ (MÀN HÌNH CŨ BIẾN MẤT)
elif st.session_state.step == 2:
    st.title(f"🐎 Chào {st.session_state.name}!")
    st.subheader("Năm Bính Ngọ này, bạn muốn nhận 'Lộc' gì nhất?")
    st.write("Hãy chọn một món quà dưới đây:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧧 Tiền Tài (Mã Đáo Thành Công)"):
            st.session_state.gift = "Tiền vào như nước, công việc hanh thông, mã đáo thành công!"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🐎 Sức Khỏe (Dẻo Dai Như Ngựa Chiến)"):
            st.session_state.gift = "Sức khỏe dẻo dai, bền bỉ và luôn tràn đầy năng lượng!"
            st.session_state.step = 3
            st.rerun()
            
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🌹 Tình Duyên (Hạnh Phúc Ngập Tràn)"):
            st.session_state.gift = "Tình duyên phơi phới, hạnh phúc viên mãn bên người thân yêu!"
            st.session_state.step = 3
            st.rerun()
    with col4:
        if st.button("🎓 Trí Tuệ (Học Một Biết Mười)"):
            st.session_state.gift = "Thông minh sáng suốt, thi cử đỗ đạt, thăng tiến vèo vèo!"
            st.session_state.step = 3
            st.rerun()

# BƯỚC 3: KẾT QUẢ CUỐI CÙNG
elif st.session_state.step == 3:
    st.title("🎊 CHÚC MỪNG NĂM MỚI 2026 🎊")
    st.balloons()
    st.header(f"Chúc bạn {st.session_state.name}:")
    st.success(st.session_state.gift)
    
    # Hình ảnh linh vật ngựa
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    if st.button("Nhận lời chúc khác ↺"):
        st.session_state.step = 1
        st.rerun()
