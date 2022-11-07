import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image
import numpy as np
import tensorflow as tf
import collections

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model(r'..\TrafficSignClassification\BestPerformingModels\VGG16_150-40-0.96_sparse.h5')
  return model


with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Traffic Sign Classification
         """
         )

file = st.file_uploader("Upload the image to be classified", type=["jpg", "png","jpeg"])


st.set_option('deprecation.showfileUploaderEncoding', False)
col1, col2 = st.columns(2)

if file is None:
    st.text("Please upload an image file")
else:
    with col1:
      image = np.array(Image.open(file))
      IMG_SIZE = (150,150) # for VGG16 model needs this specific img shape
      img = cv2.resize(image,IMG_SIZE)
      img=img/255.0 # scall down image 
      img = np.expand_dims(img, axis=0)
      st.image(img,width = 300)
      predict_x= model.predict(img)
      classes_x=np.argmax(predict_x,axis=1)
      numbers = range(58)
      classes = ['Bicycles crossing_30', 'Bicycles crossing_36', 'Children crossing_37', 'Danger Ahead_34', 'Dangerous curve to the left_38', 'Dangerous curve to the right_39', 'Dont Go Left or Right_12', 'Dont Go Left_11', 'Dont Go Right_13', 'Dont Go straight or Right_9', 'Dont Go straight or left_8', 'Dont Go straight_10', 'Dont overtake from Left_14', 'Electric Hazard_49', 'Fences_50', 'Give Way_53', 'Give Way_56', 'Go Left or right_23', 'Go Left_22', 'Go Right_24', 'Go left or straight_44', 'Go right or straight_43', 'Go straight or right_20', 'Go straight_21', 'Heavy Vehicle Accidents_51', 'Horn_29', 'No Car_16', 'No Uturn_15', 'No entry_55', 'No horn_17', 'No stopping_54', 'Passing Without stopping_57', 'Rest Area_45', 'Road Divider_32', 'Roundabout mandatory_27', 'Slow(china)_42', 'Speed limit (15kmperh)_1', 'Speed limit (30kmperh)_2', 'Speed limit (40kmperh)_18', 'Speed limit (40kmperh)_3', 'Speed limit (50kmperh)_19', 'Speed limit (50kmperh)_4', 'Speed limit (5kmperh)_0', 'Speed limit (60kmperh)_5', 'Speed limit (70kmperh)_6', 'Steep ascent_41', 'Steep descent_40', 'Stop sign(china)_52', 'Traffic signals_33', 'Train Crossing_47', 'Under Construction_48', 'Uturn_31', 'Zebra Crossing_35', 'ZigZag Curve_46', 'keep Left_25', 'keep Right_26', 'speed limit (80kmperh)_7', 'watch out for cars_28']
      dir_clases = dict(zip(numbers,classes))
    with col2:
      st.write(f'Model is **{predict_x[0][classes_x[0]]*100:.2f}%** sure that it is **{dir_clases[classes_x[0]]}**')
      dir_clases = dict(zip(predict_x[0],classes))
      
      od = collections.OrderedDict(sorted(dir_clases.items(),reverse=True)) # sort dict in descending order.
      
      # print to 5 accurate results.
      st.write('Other **top 5 possibilities** :')
      temp_increment = 1
      for key,values in od.items():
        if temp_increment != 1:
          st.write(f'{key*100:.2f}% - {values}')
        temp_increment += 1
        if temp_increment >=7:
          break