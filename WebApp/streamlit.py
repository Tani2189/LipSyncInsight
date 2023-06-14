#importing our dependencies
import streamlit as st 
import os
import imageio
import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model
#set the layout for streamlit as wide
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
#setting up our sidebar
with st.sidebar:
    image='https://cdnb.artstation.com/p/assets/images/images/038/107/385/large/kotanko-3d-cuterobot-0000.jpg?1622187572'
    st.image(image, caption='Your friendly neighbourhood!!', use_column_width=True)
    st.title('LipSync Insight')
    st.info('Exploring the World of Lip Reading')
#title 
st.title('LipSync Insight')
#generating list of option/videos.
options = os.listdir(os.path.join('..','data','s1'))
selected_video = st.selectbox('Select a video',options)

#inhere we generate 2 columns
col1,col2 = st.columns(2)

if options:
    #rendering the video
    with col1:
        st.info('Displaying the selected video....')
        file_path = os.path.join('..','data','s1',selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        #rendering 
        video = open('test_video.mp4', 'rb')#rb-> reading as binary.
        video_bytes = video.read()
        st.video(video_bytes)
#Okay so now the video is successfully rendering and now our next task is to take this video and preprocess it before passing it to our lipsync app. So for this we have our util.py file which will allow us to loadin the data simply by passing through our file path. this will return back preprocess video which will then go and isolate the lips from the original video and we're gonna see that and we're also gonna get the associated annotation for it. Let's go a little bit further, so we're even gonna take the video and output it as a gif which looks... impressive!
    with col2: 
        st.info('This is all the machine learning model sees when making a prediction')
        video, annotations = load_data(tf.convert_to_tensor(file_path))
        imageio.mimsave('animation.gif', video, fps=10)
        st.image('animation.gif', width=400) 

        st.info('This is the output of the machine learning model as tokens')
        model = load_model()
        pred = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(pred, [75], greedy=True)[0][0].numpy()
        st.text(decoder)

        # Convert prediction to text
        st.info('Decode the raw tokens into words')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(converted_prediction)
