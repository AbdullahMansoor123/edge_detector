import cv2
import numpy as np
import streamlit as st

types = None
data = st.selectbox('Select data type', ("IMAGE",'VIDEO'))
if data == 'IMAGE':
    types = ['png', 'jpg', 'jpeg']


upload_file = st.file_uploader('Choose an Image File', type=types)
if upload_file is not None:
    raw_bytes = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
    img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    input_col, out_col = st.columns(2)
    with input_col:
        st.header('Original')
        st.image(img, channels='BGR')

    # st.header('FILTERS')
    image_filter = st.selectbox('Select image filter:', ('B/W','BLUR', 'CANNY', 'SOBEL', 'PENCIL'))

    with out_col:
        st.header('OUTPUT')
        # ret, frame = cv2.imread(upl)
        # frame = cv2.flip(frame, 1)
        result = None
        if image_filter == 'BLUR':
            result = cv2.GaussianBlur(img, (10, 10), 0, 0)
        elif image_filter == 'B/W':
            result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif image_filter == 'CANNY':
            blur = cv2.GaussianBlur(img, (5, 5), 0, 0)
            result = cv2.Canny(blur, 145, 180)
        elif image_filter == 'SOBEL':
            blur = cv2.GaussianBlur(img, (5, 5), 0, 0)
            result, _ = cv2.pencilSketch(blur)
        elif image_filter == 'PENCIL':
            blur = cv2.GaussianBlur(img, (10, 10), 0, 0)
            result = cv2.stylization(blur, sigma_s=40, sigma_r=0.1)

        st.image(result, channels='BGR')

    # if cv2.waitKey(1) == ord('q'):
    #     break
    # elif cv2.waitKey(1) == ord('c'):
    #     image_filter = Canny
    # elif cv2.waitKey(1) == ord('p'):
    #     image_filter = Pencil
    # elif cv2.waitKey(1) == ord('s'):
    #     image_filter = Styler
    # elif cv2.waitKey(1) == ord('r'):
    #     image_filter = Preview
