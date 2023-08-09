import cv2
import numpy as np
import streamlit as st
import tempfile

types = None
data = st.selectbox('Select data type', ("IMAGE", 'VIDEO'))
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
        image_filter = st.selectbox('Select image filter:', ('B/W', 'BLUR', 'CANNY', 'PENCIL', 'STYLIZATION'))

        with out_col:
            st.header('OUTPUT')
            # ret, frame = cv2.imread(upl)
            # frame = cv2.flip(frame, 1)
            result = None
            if image_filter == 'BLUR':
                result = cv2.GaussianBlur(img, (11, 11), 0, 0)
                color = 'BGR'
            elif image_filter == 'B/W':
                result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                color = 'GRAY'
            elif image_filter == 'CANNY':
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(img_gray, (5, 5), 0, 0)
                result = cv2.Canny(blur, 145, 200)
                color = 'GRAY'
            elif image_filter == 'PENCIL':
                blur = cv2.GaussianBlur(img, (11, 11), 0, 0)
                result, _ = cv2.pencilSketch(blur)
                color = 'GRAY'
            elif image_filter == 'STYLIZATION':
                result = cv2.stylization(img, sigma_s=40, sigma_r=0.1)
                color = 'BGR'

            st.image(result, channels=color)

elif data == 'VIDEO':

    types = ['mp4', 'avi']
    f = st.file_uploader("Upload file", type=types)
    if f is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(f.read())

        vid_input_col, vid_out_col = st.columns(2)

        with vid_input_col:
            st.header('Original')
            video_file = open(tfile.name, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)


        # st.header('FILTERS')
        image_filter = st.selectbox('Select video filter:', ('B/W', 'BLUR', 'CANNY', 'PENCIL', 'STYLIZATION'))


        with vid_out_col:
            st.header('Output')
            vf = cv2.VideoCapture(tfile.name)
            stframe = st.empty()

            while vf.isOpened():
                ret, frame = vf.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                img = frame
                result = None
                if image_filter == 'BLUR':
                    result = cv2.GaussianBlur(img, (11, 11), 0, 0)
                    color = 'BGR'
                elif image_filter == 'B/W':
                    result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    color = 'GRAY'
                elif image_filter == 'CANNY':
                    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    blur = cv2.GaussianBlur(img_gray, (5, 5), 0, 0)
                    result = cv2.Canny(blur, 145, 200)
                    color = 'GRAY'
                elif image_filter == 'PENCIL':
                    blur = cv2.GaussianBlur(img, (11, 11), 0, 0)
                    result, _ = cv2.pencilSketch(blur)
                    color = 'GRAY'
                elif image_filter == 'STYLIZATION':
                    result = cv2.stylization(img, sigma_s=40, sigma_r=0.1)
                    color = 'BGR'

                stframe.image(result,channels=color)


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
