import streamlit as st
import time

# Cấu hình trang
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🧧")

st.title("🧧 Chúc Mừng Năm Mới Ất Tỵ 2026")

# Nhập tên
name = st.text_input("Nhập tên của bạn để nhận quà:", placeholder="Ví dụ: Nguyễn Văn A")

# Lựa chọn quà tặng
option = st.selectbox(
    "Bạn mong muốn điều gì nhất trong năm mới?",
    ("Sức khỏe dồi dào", "Tiền vào như nước", "Người yêu vây quanh", "Học hành tấn tới")
)

# Nút bấm kích hoạt hiệu ứng
if st.button("Mở quà ngay! 🎁"):
    if name:
        st.balloons() # Hiệu ứng bóng bay
        st.snow()     # Hiệu ứng tuyết rơi (giống hoa mai/đào rơi)
        
        with st.spinner('Đang chuẩn bị lời chúc đặc biệt...'):
            time.sleep(2)
            
        st.success(f"Chúc mừng {name}!")
        st.write(f"Năm 2026, chúc bạn sẽ đạt được: **{option}**! 🧨🧨🧨")
        
        # Thêm một tấm ảnh/GIF động (Bạn có thể thay link ảnh tùy ý)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreXRxZzRreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV3VfO1YyI/giphy.gif")
    else:
        st.warning("Hãy nhập tên trước khi mở quà nhé!")
