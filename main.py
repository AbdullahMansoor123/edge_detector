
import streamlit as st
import cv2
import tempfile

f = st.file_uploader("Upload file")
tfile = tempfile.NamedTemporaryFile(delete=False)
tfile.write(f.read())
vf = cv2.VideoCapture(tfile.name)
stframe = st.empty()

while vf.isOpened():
    ret, frame = vf.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

