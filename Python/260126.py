import streamlit as st
import time

# --- Cấu hình trang và Pháo hoa nền (Luôn hiển thị) ---
st.set_page_config(page_title="🎉 Chúc Mừng Năm Mới 2026 🎉", page_icon="🧧", layout="wide")

# CSS để nhúng pháo hoa nền (dùng Lottie animation)
# Bạn cần download file pháo hoa JSON hoặc dùng link trực tiếp
# Mình sẽ dùng tạm một animation pháo hoa mặc định cho dễ
st.markdown("""
<style>
.fireworks-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1; /* Đảm bảo nó ở dưới cùng */
    opacity: 0.5; /* Làm mờ bớt để không che chữ */
    pointer-events: none; /* Không cho người dùng tương tác với nó */
}
</style>
<div class="fireworks-bg">
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player
        src="https://lottie.host/8aa06307-e435-430c-ab23-38f3219468e2/h3oXk145r4.json"
        background="transparent"
        speed="1"
        style="width: 100%; height: 100%;"
        loop
        autoplay
    ></lottie-player>
</div>
""", unsafe_allow_html=True)


st.title("🎉 Cùng Đón Năm Mới Ất Tỵ 2026 🎉")
st.header("Một năm tràn đầy hy vọng và may mắn!")

# --- Bước 1: Nhập tên ---
name = st.text_input("✨ Bước 1: Bạn là ai? Hãy nhập tên để nhận lộc đầu năm:", placeholder="Ví dụ: Nguyễn Văn A")

# --- Bước 2: Chọn mong muốn (Chỉ hiện khi đã nhập tên) ---
if name:
    st.write(f"Chào {name}! Rất vui được gặp bạn!")
    st.markdown("---") # Đường kẻ ngang
    st.subheader("🍀 Bước 2: Bạn mong ước điều gì nhất trong năm mới?")
    
    wish_options = {
        "Sức khỏe dồi dào": "Bạn có một cơ thể cường tráng và tràn đầy năng lượng!",
        "Tiền vào như nước": "Tài lộc sẽ đến ào ạt, túi luôn đầy ắp!",
        "Tình duyên nở rộ": "Năm nay sẽ tìm được một nửa đích thực hoặc tình yêu thăng hoa!",
        "Sự nghiệp thăng tiến": "Công việc thuận lợi, đạt được nhiều thành công mới!",
        "Học hành tấn tới": "Thi cử đỗ đạt, kiến thức mở mang!"
    }
    
    selected_wish = st.selectbox(
        "Chọn một điều bạn mong muốn:",
        ["-- Chọn một mong muốn --"] + list(wish_options.keys())
    )

    # --- Bước 3: Hiện lời chúc và hiệu ứng (Chỉ hiện khi đã chọn mong muốn) ---
    if selected_wish != "-- Chọn một mong muốn --":
        st.markdown("---")
        st.subheader("🎁 Bước 3: Lời chúc đặc biệt dành cho bạn!")
        
        if st.button(f"Xem lời chúc cho {selected_wish} ngay! 🎊"):
            st.balloons() # Hiệu ứng bóng bay
            st.snow()     # Hiệu ứng tuyết rơi/hoa mai đào
            
            with st.spinner('Đang chuẩn bị lộc đầu năm...'):
                time.sleep(2)
            
            st.success(f"Chúc mừng {name}!")
            st.markdown(f"Lời chúc đặc biệt: **{wish_options[selected_wish]}**")
            
            # Thêm hình ảnh GIF động liên quan đến lời chúc
            # (Bạn có thể thay đổi các link GIF này)
            if selected_wish == "Sức khỏe dồi dào":
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExenFkYXJrbWpyMXlseWV2czZsd2U0aXl3ZGJ0aTRjYjA4Z2V0NWc4NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lq0V2j4xS5sD6/giphy.gif", caption="Chúc bạn luôn khỏe mạnh!")
            elif selected_wish == "Tiền vào như nước":
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG13Mmp2c21sazQ5cmF0cmI3c3B0b284MW9ucWptcTdtZWhwNTlhNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4FGJym7Vb6sJ2PPa/giphy.gif", caption="Tiền vào đầy túi!")
            elif selected_wish == "Tình duyên nở rộ":
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2k3ZGdwam9jNnI4ZnZlZ2Z0ajFzN2V2eTJ3NmdzZW81dG1hYndnNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tX6fS4t0rT7e0/giphy.gif", caption="Tình yêu lung linh!")
            elif selected_wish == "Sự nghiệp thăng tiến":
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDVnNnFzdW82N2UzaW55MW0yZzJjY2ZtdHpvbnQ2M3R2b291dWRlMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ornjQM7zFkY2rB1ks/giphy.gif", caption="Sự nghiệp vững vàng!")
            elif selected_wish == "Học hành tấn tới":
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXZjMjlsYWxibG54a2Y4cWRsMGVvcTczM2w0ZzY5d2d0cDN6a203NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26BkNCd0n9LgYJ7mE/giphy.gif", caption="Học một biết mười!")
