# Breast Cancer Wisconsin Diagnostic

![1_FHQOSHMMT07CbXpklk1Ehw](https://github.com/user-attachments/assets/b4e88b1a-5bb8-470c-b132-0df58bff444b)

<br>

<h4 align="center" >🚀 🟪 Classifier Model | Breast Cancer Wisconsin Diagnostic 🟪 🚀</h4>

<h4 align="center">
Machine Learning Project: Diagnosis of Breast Cancer by Image Data using a classifier model
</h4>

#

<p align="center">
  |&nbsp;&nbsp;
  <a style="color: #8a4af3;" href="#project">Overview</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a style="color: #8a4af3;" href="#techs">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a style="color: #8a4af3;" href="#app">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;
  <a style="color: #8a4af3;" href="#run-project">Run</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;
  <a style="color: #8a4af3;" href="#author">Author</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

#

<h1 align="center">
  
  <a href="https://github.com/Samuel-Ricardo">
    <img src="https://img.shields.io/static/v1?label=&message=Samuel%20Ricardo&color=black&style=for-the-badge&logo=GITHUB"/>
  </a>

  <a herf="https://www.instagram.com/samuel_ricardo.ex/">
    <img src='https://img.shields.io/static/v1?label=&message=Samuel.ex&color=black&style=for-the-badge&logo=instagram'/> 
  </a>

  <a herf='https://www.linkedin.com/in/samuel-ricardo/'>
    <img src='https://img.shields.io/static/v1?label=&message=Samuel%20Ricardo&color=black&style=for-the-badge&logo=LinkedIn'/> 
  </a>

</h1>

<br>

<p id="project"/>

<br>

<h2>  | :artificial_satellite: About:  </h2>

<p align="justify">
  EI am researching Machine Learning and my current focus is on classifying models. With this in mind I researched the repository in <a href="https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic">UC Irvine</a> that called me attention, so develop a binary classification model to identify cases of benign cancer or malignant cancer
</p>

<br>

<h2 id="techs">
  :building_construction: | Technologies and Concepts Studied:
</h2>


> <a href='https://www.tensorflow.org/'> <img width="200px" src="https://github.com/Samuel-Ricardo/ML_Regression-Model_Boston-Housing/assets/63983021/d9ed0c56-4fde-4285-89e5-7ec89bdfab76" /> </a>

- Machine Learning: Classifier Model
- K-NEAREST NEIGHBORS (KNN) ALGORITHM
- Python
- Google Colab
- Tensorflow
- Keras
- pandas
- Matplotlib
- Sklearn
- Graphics
  
> Among Others...

#

<br>

<h2 id="app">
  🧠 | Project:
</h2>

<br/>

### Data Overview

First i define the most relevant metrics to this scenario

- True & False Positive
- True & False Negative
- Precision at Recall
- Sensitivity at Specifity
- Specifity at Sensivity
- Recall

Informations about Dataset:

- Creator:  Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian
- Donor: Nick Street

Attribute Information:

- radius (mean of distances from center to points on the perimeter)
- texture (standard deviation of gray-scale values)
- perimeter
- area
- smoothness (local variation in radius lengths)
- compactness (perimeter^2 / area - 1.0)
- concavity (severity of concave portions of the contour)
- concave points (number of concave portions of the contour)
- symmetry
- fractal dimension ("coastline approximation" - 1)

The mean, standard error, and "worst" or largest (mean of the three worst/largest values) of these features were computed for each image, resulting in 30 features. For instance, field 0 is Mean Radius, field 10 is Radius SE, field 20 is Worst Radius.

- Classes:
  - WDBC-Malignant
  - WDBC-Benign

<br/>
 
![image](https://github.com/user-attachments/assets/94b19ac4-ac61-4b1e-958b-b3acc4250a89)

- Class Distribution: 212 - Malignant, 357 - Benign

<br>

![image](https://github.com/user-attachments/assets/8dcb14b2-3438-4130-a519-1b20e2436813)

<br>

#### Expected Results:

![image](https://github.com/user-attachments/assets/4b9de735-7fa8-45e7-8ef3-2d311d207572)

<br>

### About AI Training

- I separate 20% of data for testing

I used [K-NEAREST NEIGHBORS (KNN) ALGORITHM](https://www.ibm.com/br-pt/topics/knn) to perform the bynary classification having 91% of accuracy, i was used as comparison with our model

- Before creation of model it self, was made a data proccesing.

### Model

![image](https://github.com/user-attachments/assets/d78c3933-ec39-408f-a319-fac7bb85529c)

<br>

Was created a sequential model almost 30.000 params and 6 layers, between theys, 2 Convolutional Dimensions a 2 Dense Layers, dropout as a kind of middleware, and a flatten to transform any dimensions vector to one dimension vector and more than one thousand of neurons, resulting in 116.57kb.

### Results

Here are the trainig result in a graphic view, was used 100 epochs of proccessing with 10 steps per epoch.

---------------------------------------
Final Report (evaluation metrics)
---------------------------------------

- Final Accuracy: 96.24%
- General Accuracy: 96.0%
- Accuracy (average U10): 96.0%
- Accuracy (training): 96.0%
- Accuracy (validation): 98.0%
- LOSS RATE: 0.08%
- Loss rate (validation): 0.11%
- Precision: 100.0%
- Precision (validation): 98.0%
- Recall: 99.0%
- RECALL (VALIDATION): 95.0%
- F1 score: 100.0%
- F-Measure: 100.0%
- F1 score (TP, FP, TN, FN): 97.0%
- Learning Fee: 9.999999974752427E-07
- Sensitivity: 97.0%
- Specificity: 94.0%
- Confusion matrix accuracy: 96.0%
- TRUE POSITIVE RATE: 98.0%
- Real negative rate: 99.0%
- Positive False Rate: 4.0%
- False negative rates: 1.0%
- Invalid data: 2.0%

---------------------------------------

<br>

![image](https://github.com/user-attachments/assets/24ce1f71-58b8-4ae9-93e4-6bc80ac64ab2)

<br>

![image](https://github.com/user-attachments/assets/0aa9fbe6-52de-4473-a902-5654c5c4e4c3)

<br>

![image](https://github.com/user-attachments/assets/a72443fa-3e27-43f2-b730-6f453fe13ada)

<br>

![image](https://github.com/user-attachments/assets/4bf0fb11-a936-4a5c-bda3-b8ed4f89caea)

<br>

![image](https://github.com/user-attachments/assets/da1fd14f-86c4-4ab4-9229-c592767f3acb)

<br>

![image](https://github.com/user-attachments/assets/fb315f8c-67a9-46de-88df-05cbe00ae17f)

<br>

![image](https://github.com/user-attachments/assets/fbce24fe-2bf0-460d-a253-d1095d120a7b)

<br>

![image](https://github.com/user-attachments/assets/d645795b-d4d9-4ebb-87bb-b1c9870752cf)

<br>


![image](https://github.com/user-attachments/assets/220fb549-8f3b-4c9f-aed0-31e99ff1cd8a)

<br>

![image](https://github.com/user-attachments/assets/a375cca3-d442-4539-8ccc-f5af2f764b8c)

<br>

![image](https://github.com/user-attachments/assets/cb561bee-6133-48a2-940b-40b8012875ee)

<br>

![image](https://github.com/user-attachments/assets/456d7ba0-01db-4f55-8fbe-d7bf9b95fa07)

<br>

![image](https://github.com/user-attachments/assets/7e48624e-45b8-490a-a971-8273ec377549)

<br>

<h2 id="run-project"> 
   👨‍💻 | How to use
</h2>

<br>

Import the `ML___Classifier_Models.ipynb` file in a Python Notebook App like Jupyter or Google Colab and run cell by cell.

- Run only the cell with `!pip install` commands in `[Setup and Install Deps]` section.
- Now, jump to `Binary Classification - Dataset: Breast Cancer Wisconsin (Diagnostic)` Section and run cells in order.

#

<br>

<h2 id="author">
  :octocat: | Author:  
</h2>

> <a target="_blank" href="https://www.linkedin.com/in/samuel-ricardo/"> <img width="350px" src="https://github.com/Samuel-Ricardo/bolao-da-copa/blob/main/readme_files/IMG_20220904_220148_188.jpg?raw=true"/> <br> <p> <b> - Samuel Ricardo</b> </p></a>

<h1>
  <a herf='https://github.com/Samuel-Ricardo'>
    <img src='https://img.shields.io/static/v1?label=&message=Samuel%20Ricardo&color=black&style=for-the-badge&logo=GITHUB'> 
  </a>
  
  <a herf='https://www.instagram.com/samuel_ricardo.ex/'>
    <img src='https://img.shields.io/static/v1?label=&message=Samuel.ex&color=black&style=for-the-badge&logo=instagram'> 
  </a>
  
  <a herf='https://twitter.com/SamuelR84144340'>
    <img src='https://img.shields.io/static/v1?label=&message=Samuel%20Ricardo&color=black&style=for-the-badge&logo=twitter'> 
  </a>
  
   <a herf='https://www.linkedin.com/in/samuel-ricardo/'>
    <img src='https://img.shields.io/static/v1?label=&message=Samuel%20Ricardo&color=black&style=for-the-badge&logo=LinkedIn'> 
  </a>
</h1>


































