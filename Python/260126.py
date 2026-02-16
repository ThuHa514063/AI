import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🧧", layout="centered")

# --- HIỆU ỨNG PHÁO HOA TOÀN MÀN HÌNH ---
# Sử dụng hiệu ứng Canvas-confetti để tạo pháo hoa chuyên nghiệp
st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
    var duration = 15 * 1000;
    var animationEnd = Date.now() + duration;
    var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

    function randomInRange(min, max) {
      return Math.random() * (max - min) + min;
    }

    var interval = setInterval(function() {
      var timeLeft = animationEnd - Date.now();

      if (timeLeft <= 0) {
        return clearInterval(interval);
      }

      var particleCount = 50 * (timeLeft / duration);
      // pháo hoa bắn từ 2 bên
      confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
      confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
    }, 250);
</script>
<style>
    /* Làm đẹp giao diện */
    .stApp {
        background-color: #1a1a1a;
        color: #ffd700;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- QUẢN LÝ CÁC BƯỚC (SESSION STATE) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""

# --- HÀM CHUYỂN BƯỚC ---
def next_step():
    st.session_state.step += 1

def reset_app():
    st.session_state.step = 1
    st.session_state.name = ""

# --- GIAO DIỆN TỪNG BƯỚC ---

# BƯỚC 1: NHẬP TÊN
if st.session_state.step == 1:
    st.title("🧧 Chào mừng bạn đến với Tết 2026")
    name_input = st.text_input("Trước tiên, hãy cho mình biết tên của bạn:", placeholder="Nhập tên tại đây...")
    if st.button("Tiếp theo ➔"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 2
            st.rerun() # Làm mới để biến mất màn hình cũ
        else:
            st.warning("Vui lòng nhập tên nhé!")

# BƯỚC 2: CHỌN QUÀ
elif st.session_state.step == 2:
    st.title(f"🏮 Chào {st.session_state.name}!")
    st.subheader("Bạn muốn nhận lộc gì trong năm mới Ất Tỵ?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💰 Tài Lộc"):
            st.session_state.gift = "Tiền vào như nước, ví luôn căng phồng!"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("❤️ Tình Duyên"):
            st.session_state.gift = "Người yêu xếp hàng, thoát kiếp độc thân!"
            st.session_state.step = 3
            st.rerun()
    
    col3, col4 = st.columns(2)
    with col3:
        if st.button("💪 Sức Khỏe"):
            st.session_state.gift = "Khỏe như rồng, cả năm không ốm!"
            st.session_state.step = 3
            st.rerun()
    with col4:
        if st.button("🎓 Sự Nghiệp"):
            st.session_state.gift = "Học đâu đỗ đó, thăng tiến vèo vèo!"
            st.session_state.step = 3
            st.rerun()

# BƯỚC 3: MÀN HÌNH LỜI CHÚC CUỐI CÙNG
elif st.session_state.step == 3:
    st.balloons() # Hiệu ứng bóng bay của Streamlit
    st.title("🎊 CHÚC MỪNG NĂM MỚI! 🎊")
    st.header(f"Chúc bạn {st.session_state.name}:")
    st.success(st.session_state.gift)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    
    if st.button("Làm lại từ đầu ↺"):
        reset_app()
        st.rerun()
