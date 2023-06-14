# LipSyncInsight
>Hey guys,
>Let me introdce LipSyncInsight, 
>an lip reading software which recognizes the lips of the user and predicts the output.

# Contents:
* [Demo](#Demo)
* [Dataset](Dataset)
* [Used Dependences](#Dependences)
* [Working](#Working)
* [Referance](#Referances)

# Demo:
![image](https://github.com/Tani2189/LipSyncInsight/assets/96855667/1e1f3c0d-863e-4e2d-b8fb-6ce962acdc55)

# Dataset:
The dataset used for training the model is a subset of the [Grid Corpus Dataset](https://spandh.dcs.shef.ac.uk//gridcorpus/) . Used gdown to download a subset (1 speaker) of the full dataset (34 speakers) from google drive.

# Dependences:
* Python-Tensorflow-Keras -> data preparation, pipeline, model training & testing.
* Streamlit -> web application.
* LipNet -> lip reading model architecture idea.
* ffmpeg -> video file format conversion
* opencv -> video capture and frames processing.
* gdown -> for downloading the dataset.
* imageio -> for making gifs

# Working:
![image](https://github.com/Tani2189/LipSyncInsight/assets/96855667/92a5d21d-3b3e-4209-bbe3-f3cccbabd57d)
>here instead of Bi-GRU we are using Bi-Lstm.
![image](https://github.com/Tani2189/LipSyncInsight/assets/96855667/47e90fe7-0baf-4464-86fe-b80ed60f3cd5)
![image](https://github.com/Tani2189/LipSyncInsight/assets/96855667/19390f70-9c37-4600-b27e-6aececc0036e)
>corelation matrix

# Referances:
* https://keras.io/examples/audio/ctc_asr/
* https://github.com/rizkiarm/LipNet
* Lip reading.pdf
* Lip reading1.pdf
