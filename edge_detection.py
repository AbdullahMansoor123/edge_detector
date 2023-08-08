import cv2
import numpy as np
import streamlit as st

s = 0


win_name = "Demo Edge Detection"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

Preview = 0
Canny = 1
Pencil = 2
Styler = 3


upload_file = st.file_uploader('Choose an Image File', type=['png', 'jpg', 'jpeg'])
if upload_file is not None:
    raw_bytes = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
    img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)
    input_col, out_col = st.columns(2)
    with input_col:
        st.header('Original')


ret, frame = cv2.read()
image_filter = st.selectbox('Select image filter',("Preview",'Canny','Pencil'))


frame = cv2.flip(frame, 1)

if image_filter == Preview:
    result = frame
elif image_filter == Canny:
    result = cv2.Canny(frame, 145, 180)
elif image_filter == Pencil:
    blur = cv2.GaussianBlur(frame, (5, 5), 0, 0)
    result, _ = cv2.pencilSketch(blur)
elif image_filter == Canny:
    blur = cv2.GaussianBlur(frame, (10, 10), 0, 0)
    result = cv2.stylization(blur, sigma_s=40, sigma_r=0.1)
cv2.imshow(win_name, result)

if cv2.waitKey(1) == ord('q'):
    break
elif cv2.waitKey(1) == ord('c'):
    image_filter = Canny
elif cv2.waitKey(1) == ord('p'):
    image_filter = Pencil
elif cv2.waitKey(1) == ord('s'):
    image_filter = Styler
elif cv2.waitKey(1) == ord('r'):
    image_filter = Preview
