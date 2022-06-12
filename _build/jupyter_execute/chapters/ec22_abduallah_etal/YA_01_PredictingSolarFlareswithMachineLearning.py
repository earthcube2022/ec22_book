#!/usr/bin/env python
# coding: utf-8

# # **Predicting Solar Flares with Machine Learning**

# ## **Table of Contents**

# 
# <div class="toc">
# <!--     <ul class="toc-item"> -->
#         <li><span><a href="#Template-Notebook-for-EarthCube---Long-Version"
#                     data-toc-modified-id="Template-Notebook-for-EarthCube---Long-Version-1"><span
#                         class="toc-item-num">1&nbsp;&nbsp;</span>YA_Notebook for Predicting Solar Flares with Machine
#                     Learning</a></span>
#             <ul class="toc-item" style='margin-top:0px; margin-bottom:0px'>
#                 <li><span><a href="#Author(s)" data-toc-modified-id="Author(s)-1.1"><span
#                                 class="toc-item-num">1.1&nbsp;&nbsp;</span>Author(s)</a></span></li>
#                 <li><span><a href="#Purpose" data-toc-modified-id="Purpose-1.2"><span
#                                 class="toc-item-num">1.2&nbsp;&nbsp;</span>Purpose</a></span></li>
#                 <li><span><a href="#Technical-Contributions" data-toc-modified-id="Technical-Contributions-1.3"><span
#                                 class="toc-item-num">1.3&nbsp;&nbsp;</span>Technical Contributions</a></span></li>
#                 <li><span><a href="#Methodology" data-toc-modified-id="Methodology-1.4"><span
#                                 class="toc-item-num">1.4&nbsp;&nbsp;</span>Methodology</a></span></li>
#                 <li><span><a href="#Funding" data-toc-modified-id="Funding-1.6"><span
#                                 class="toc-item-num">1.5&nbsp;&nbsp;</span>Funding</a></span></li>
#                 <li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.7"><span
#                                 class="toc-item-num">1.6&nbsp;&nbsp;</span>Keywords</a></span></li>
#                 <li><span><a href="#Citation" data-toc-modified-id="Citation-1.8"><span
#                                 class="toc-item-num">1.7&nbsp;&nbsp;</span>Citation</a></span></li>
#                 <li><span style='display:inline'><a href="#Acknowledgements" data-toc-modified-id="Acknowledgements-1.11"><span
#                         class="toc-item-num">1.8&nbsp;&nbsp;</span>Acknowledgements</a></span></li>                
#             </ul>
#         </li>
# <!--     </ul> -->
#     <li><span><a href="#Setup" data-toc-modified-id="Setup-2"><span
#                     class="toc-item-num">2&nbsp;&nbsp;</span>Setup</a></span>
#     </li>
#     <li><span><a href="#Data-Processing-and-Analysis" data-toc-modified-id="Data-Processing-and-Analysis-3"><span
#                     class="toc-item-num">3&nbsp;&nbsp;</span>Data Processing and Analysis</a></span></li>
#     <li><span><a href="#Binder" data-toc-modified-id="Binder-4"><span
#                     class="toc-item-num">4&nbsp;&nbsp;</span>Binder</a></span></li>
#     <li><span><a href="#FlareML-Workflow" data-toc-modified-id="FlareML-Workflow-5"><span
#                     class="toc-item-num">5&nbsp;&nbsp;</span>FlareML Workflow and Results</a></span>
#         <ul class="toc-item" style='margin-top:0px;margin-bottom:0px'>
#             <li>
#                 <span><a href="#Data-Preparation-and-Loading"
#                         data-toc-modified-id="Data-Preparation-and-Loading-5.1"><span
#                             class="toc-item-num">5.1&nbsp;&nbsp;</span>Data Preparation and Loading</a></span>
#             </li>
#             <li>
#                 <span><a href="#Predicting-with-Pretrained-Models"
#                         data-toc-modified-id="Predicting-with-Pretrained Models-5.6"><span
#                             class="toc-item-num">5.2&nbsp;&nbsp;</span>Predicting with Pretrained Models</a></span>
# <!--                 <ul class="toc-item">
#                     <li style='list-style: square'>
#                         <span><a href="#Plotting-the-Pretrained-Models-Results"
#                                 data-toc-modified-id="Plotting-the-Pretrained-Models-Results-5.2.3">
#                                 <span class="toc-item-num">5.2.1&nbsp;&nbsp;
#                                 </span>Plotting the Pretrained Models Results</a></span>
#                     </li>
#                 </ul> -->
#             </li>            
#             <li>
#                 <span><a href="#ENS-Model-Training-and-Testing"
#                         data-toc-modified-id="ENS-Model-Training-and-Testing-5.2"><span
#                             class="toc-item-num">5.3&nbsp;&nbsp;</span>ENS Model Training and Testing</a></span>
# <!--                 <ul class="toc-item">
#                     <li style='list-style: square'>
#                         <span><a href="#ENS-Model-Training-with-Default-Data"
#                                 data-toc-modified-id="ENS Model-Training-with-Default-Data-6">
#                                 <span class="toc-item-num">5.3.1&nbsp;&nbsp;
#                                 </span>ENS Model Training with Default Data</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Predicting-with-Your-ENS-Model"
#                                 data-toc-modified-id="Predicting-with-Your-ENS-Model-5.2.2">
#                                 <span class="toc-item-num">5.3.2&nbsp;&nbsp;
#                                 </span>Predicting with Your ENS Model</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Plotting-the-ENS-Results" data-toc-modified-id="Plotting-the-ENS-Results-5.2.3">
#                                 <span class="toc-item-num">5.3.3&nbsp;&nbsp;
#                                 </span>Plotting the ENS Results</a></span>
#                     </li>
#                 </ul> -->
#             </li>
#             <li>
#                 <span><a href="#RF-Model-Training-and-Testing"
#                         data-toc-modified-id="RF-Model-Training-and-Testing-5.2"><span
#                             class="toc-item-num">5.4&nbsp;&nbsp;</span>RF Model Training and Testing</a></span>
# <!--                 <ul class="toc-item">
#                     <li style='list-style: square'>
#                         <span><a href="#RF-Model-Training-with-Default-Data"
#                                 data-toc-modified-id="RF Model-Training-with-Default-Data-6">
#                                 <span class="toc-item-num">5.4.1&nbsp;&nbsp;
#                                 </span>RF Model Training with Default Data</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Predicting-with-Your-RF-Model"
#                                 data-toc-modified-id="Predicting-with-Your-RF-Model-5.2.2">
#                                 <span class="toc-item-num">5.4.2&nbsp;&nbsp;
#                                 </span>Predicting with Your RF Model</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Plotting-the-RF-Results" data-toc-modified-id="Plotting-the-RF-Results-5.2.3">
#                                 <span class="toc-item-num">5.4.3&nbsp;&nbsp;
#                                 </span>Plotting the RF Results</a></span>
#                     </li>
#                 </ul> -->
#             </li>
#             <li>
#                 <span><a href="#MLP-Model-Training-and-Testing"
#                         data-toc-modified-id="MLP-Model-Training-and-Testing-5.2"><span
#                             class="toc-item-num">5.5&nbsp;&nbsp;</span>MLP Model Training and Testing</a></span>
# <!--                 <ul class="toc-item">
#                     <li style='list-style: square'>
#                         <span><a href="#MLP-Model-Training-with-Default-Data"
#                                 data-toc-modified-id="MLP Model-Training-with-Default-Data-6">
#                                 <span class="toc-item-num">5.5.1&nbsp;&nbsp;
#                                 </span>MLP Model Training with Default Data</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Predicting-with-Your-MLP-Model"
#                                 data-toc-modified-id="Predicting-with-Your-RF-Model-5.2.2">
#                                 <span class="toc-item-num">5.5.2&nbsp;&nbsp;
#                                 </span>Predicting with Your MLP Model</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Plotting-the-MLP-Results" data-toc-modified-id="Plotting-the-MLP-Results-5.2.3">
#                                 <span class="toc-item-num">5.5.3&nbsp;&nbsp;
#                                 </span>Plotting the MLP Results</a></span>
#                     </li>
#                 </ul> -->
#             </li>
#             <li>
#                 <span><a href="#ELM-Model-Training-and-Testing"
#                         data-toc-modified-id="ELM-Model-Training-and-Testing-5.2"><span
#                             class="toc-item-num">5.6&nbsp;&nbsp;</span>ELM Model Training and Testing</a></span>
# <!--                 <ul class="toc-item">
#                     <li style='list-style: square'>
#                         <span><a href="#ELM-Model-Training-with-Default-Data"
#                                 data-toc-modified-id="ELM Model-Training-with-Default-Data-6">
#                                 <span class="toc-item-num">5.6.1&nbsp;&nbsp;
#                                 </span>ELM Model Training with Default Data</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Predicting-with-Your-ELM-Model"
#                                 data-toc-modified-id="Predicting-with-Your-ELM-Model-5.2.2">
#                                 <span class="toc-item-num">5.6.2&nbsp;&nbsp;
#                                 </span>Predicting with Your ELM Model</a></span>
#                     </li>
#                     <li style='list-style: square'>
#                         <span><a href="#Plotting-the-ELM-Results" data-toc-modified-id="Plotting-the-ELM-Results-5.2.3">
#                                 <span class="toc-item-num">5.6.3&nbsp;&nbsp;
#                                 </span>Plotting the ELM Results</a></span>
#                     </li>
#                 </ul> -->
#             </li>            
#             <li>
#                 <span><a href="#Timing"
#                         data-toc-modified-id="Timing-5.7"><span
#                             class="toc-item-num">5.7&nbsp;&nbsp;</span>Timing</a></span>
#             </li>            
#         </ul>
#     </li>
# <!--     </ul> -->
# </div>            
#         </ul>
#     </li>
#     <li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-6"><span
#                     class="toc-item-num">6&nbsp;&nbsp;</span>Conclusions</a></span>
#     </li>
#     <li><span><a href="#References" data-toc-modified-id="References-7"><span
#                     class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span>
#     </li>    
#     </ul>
# </div>

# ### **Author(s)**
# - Author1 = {"name": "Yasser Abduallah", "affiliation": "Department of Computer Science, New Jersey Institute of Technology", "email": "ya54@njit.edu", "orcid": "https://orcid.org/0000-0003-0792-2270"}
# - Author2 = {"name": "Jason T. L. Wang", "affiliation": "Department of Computer Science, New Jersey Institute of Technology", "email": "wangj@njit.edu", "orcid": "https://orcid.org/0000-0002-2486-1097"}
# - Author3 = {"name": "Haimin Wang", "affiliation": "Institute for Space Weather Sciences, New Jersey Institute of Technology", "email": "haimin.wang@njit.edu", "orcid": "https://orcid.org/0000-0002-5233-565X"}

# ### **Purpose**
# Solar flare prediction plays an important role in understanding and forecasting space weather. The main goal of the Helioseismic and Magnetic Imager (HMI), one of the instruments on NASA's Solar Dynamics Observatory (SDO), is to study the origin of solar variability and characterize the Sun's magnetic activity. HMI provides continuous full-disk observations of the solar vector magnetic field with high cadence data that lead to reliable predictive capability; yet, solar flare prediction effort utilizing these data is still limited.
# 
# In this notebook we provide an overview of the FlareML system to demonstrate how to predict solar flares using machine learning (ML) and SDO/HMI vector magnetic data products (SHARP parameters).
# 
# ### **Technical Contributions**
# 
# - We provide the community with a new tool to predict solar flares.
# 
# 
# ### **Methodology**
# 
# Here we present a flare prediction system, named FlareML, for predicting solar flares using machine learning (ML) based on HMI’s vector magnetic data products. Specifically, we construct training data by utilizing the physical parameters provided by the Space-weather HMI Active Region Patches (SHARP) and categorize solar flares into four classes, namely B, C, M, X, according to the X-ray flare catalogs prepared by the National Centers for Environmental Information (NCEI). Thus, the solar flare prediction problem at hand is essentially a multi-class (i.e., four-class) classification problem. The FlareML system employs four machine learning methods to tackle this multi-class prediction problem. These four methods are: (i) ensemble (ENS), (ii) random forests (RF), (iii) multilayer perceptrons (MLP), and (iv) extreme learning machines (ELM). ENS works by taking the majority vote of the results obtained from RF, MLP and ELM. This notebook leverages python machine learning and visualization packages: matplotlib, numpy, scikit-learn, sklearn-extensions, and pandas. It describes the steps on how to use the FlareML tool to predict solar flare types: B, C, M, and X. The notebook is trained and tested on sample data sets to show flare predictions and their accuracies in graphical bar plots. FlareML is the backend of an online machine-learning-as-a-service system accessible at: https://nature.njit.edu/spacesoft/DeepSun/.
# 
# Notes: <br>
# <ul>
#     <li>Some models used in FlareML are not deterministic due to the randomness of their processes. Therefore, these models do not make the same prediction after re-training.
#     </li>
#     <li>
#         Detailed information about the parameters used for each model can be found in our published paper: <a href='https://iopscience.iop.org/article/10.1088/1674-4527/21/7/160'>https://iopscience.iop.org/article/10.1088/1674-4527/21/7/160</a>
#     </li>
#     </ul>
# 
# 
# 
# ### **Funding**
# This work was supported by U.S. NSF grants AGS-1927578 and AGS-1954737.
# 
# ### **Keywords**
# keywords=["Flare", "Prediction", "Machine", "Learning", "SHARP"]
# 
# ### **Citation**
# To cite this notebook: Yasser Abduallah, Jason T. L. Wang, & Haimin Wang. Predicting Solar Flares with Machine Learning, available at: <a href='https://github.com/ccsc-tools/FlareML/blob/main/YA_01_PredictingSolarFlareswithMachineLearning.ipynb' target='new'>https://github.com/ccsc-tools/FlareML/blob/main/YA_01_PredictingSolarFlareswithMachineLearning.ipynb</a>.
# 
# 
# 
# ### **Acknowledgements** 
# 
# We thank the team of SDO/HMI for producing vector magnetic data products. The flare catalogs were prepared by and made available through NOAA NCEI.

# # **Setup**
# 
# **Installation on Local Machine**<br>
# Running this notebook in a local machine requires Python version 3.8.x with the following packages and their version:
# 
# |Library | Version   | Description  |
# |:---|---|:---|
# |matplotlib|3.4.2| Graphics and visualization|
# |numpy| 1.19.5| Array manipulation|
# |scikit-learn| 0.24.2| Machine learning|
# | sklearn-extensions | 0.0.2  | Extension for scikit-learn |
# | pandas|1.2.4| Data loading and manipulation|

# You may install the package using Python pip packages manager as follows:
# 
# pip install matplotlib==3.4.2 numpy==1.19.5 scikit-learn==0.24.2 sklearn-extensions==0.0.2 pandas==1.2.4
# 
# 
# 
#  **Library Import**<br>
# The following libraries need to be imported.

# In[38]:


import warnings
warnings.filterwarnings('ignore')
# Data manipulation
import pandas as pd
import numpy as np

# Training the models
# The following libraries are used to train the algorithms: Random Forest, MLP, and ELM.
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn_extensions.extreme_learning_machines.elm import GenELMClassifier
from sklearn_extensions.extreme_learning_machines.random_layer import RBFRandomLayer, MLPRandomLayer

# Visualizations
import matplotlib.pyplot as plt
from flareml_utils import plot_custom_result

# Running the training, testing and prediction.
from flareml_train import train_model
from flareml_test import test_model


# # **Data Processing and Analysis**
# We created and stored 845 data samples in
# our database accessible at <a target='new' href='https://nature.njit.edu/spacesoft/Flare-Predict/'>https://nature.njit.edu/spacesoft/Flare-Predict/</a>, where each data sample
# contains values of 13 physical parameters or features. The two digits following a class label (B,
# C, M, X) are ignored in performing flare prediction. The time
# point of a data sample is the beginning time (00:00:01 early
# morning) of the start date of a flare and the label of the data
# sample is the class which the flare belongs to. These labeled
# data samples are used to train the FlareML system.
# 
# For this notebook, we use sample data sets for training and testing.

# # **Binder**
# 
# This notebook is Binder enabled and can be run on <a target='new' href='https://mybinder.org/'>mybinder.org</a> by using the image link below:
# 
# <p float="left"> <a href='https://mybinder.org/v2/gh/ccsc-tools/FlareML/HEAD?labpath=YA_01_PredictingSolarFlareswithMachineLearning.ipynb' target='new'><img align="left" src='https://mybinder.org/badge_logo.svg'></img></a></p>
# 
# <br><br>
# Please note that starting Binder might take some time to create and start the image.
# 
# 

# # **FlareML Workflow and Results**
# 

# ### **Data Preparation and Loading**
# The data folder includes two sub-directories: train_data and test_data.
# * The train_data includes a CSV training data file that is used to train the model. 
# * The test_data includes a CSV test data file that is used to predict the included flares.
# 
# The files are loaded and used during the testing and training process.

# ### **Predicting with Pretrained Models**
# There are default and pretrained models that can be used to predict without running your own trained model. The modelid  is set to default_model which uses all pretrained algorithms.

# In[53]:


from flareml_test import test_model
args =  {'test_data_file': 'data/test_data/flaringar_simple_random_40.csv', 
         'modelid': 'default_model'}
result = test_model(args)


# **Plotting the Pretrained Models Results**<br>

# In[54]:


from flareml_utils import plot_result
plot_result(result)


# ### **ENS Model Training and Testing**
# You may train the model with your own data or train the model with the default data.
# 
# **ENS Model Training with Default Data**<br>
# Here, we show how to train the model with default data.
# To train the model with your own data:
# 1. You should first upload your file to the data directory (in the left hand side file list).
# 2. Edit the args variable in the following code and update the path to the training file:<br> 'train_data_file':'data/train_data/flaringar_training_sample.csv' <br>and replace the value 'data/train_data/flaringar_training_sample.csv' with your new file name.

# In[41]:


print('Loading the train_model function...')
from flareml_train import train_model
args = {'train_data_file':'data/train_data/flaringar_training_sample.csv',
        'algorithm': 'ENS',
       'modelid': 'custom_model_id'
      }
train_model(args)


# **Predicting with Your ENS Model**<br>
# To predict the testing data using the model you trained above, make sure the modelid value in the args variable in the following code is set exactly as the one used in the training, for example: 'custom_model_id'.

# In[42]:


from flareml_test import test_model
args =  {'test_data_file': 'data/test_data/flaringar_simple_random_40.csv', 
         'algorithm': 'ENS', 
         'modelid': 'custom_model_id'}
custom_result = test_model(args)


#  **Plotting the ENS Results**<br>
# The prediction result can be plotted by passing the result variable to the function plot_custom_result as shown in the following example. The result shows the accuracy (TSS value) your model achieves for each flare class.

# In[43]:


from flareml_utils import plot_custom_result
plot_custom_result(custom_result)


# ### **RF Model Training and Testing**

# **RF Model Training with Default Data**<br>

# In[44]:


print('Loading the train_model function...')
from flareml_train import train_model
args = {'train_data_file':'data/train_data/flaringar_training_sample.csv',
        'algorithm': 'RF',
       'modelid': 'custom_model_id'
      }
train_model(args)


# **Predicting with Your RF Model**<br>

# In[45]:


from flareml_test import test_model
args =  {'test_data_file': 'data/test_data/flaringar_simple_random_40.csv', 
         'algorithm': 'RF', 
         'modelid': 'custom_model_id'}
custom_result = test_model(args)


# **Plotting the RF Results**<br>

# In[46]:


from flareml_utils import plot_custom_result
plot_custom_result(custom_result)


# ### **MLP Model Training and Testing**
# **MLP Model Training with Default Data**<br>

# In[47]:


print('Loading the train_model function...')
from flareml_train import train_model
args = {'train_data_file':'data/train_data/flaringar_training_sample.csv',
        'algorithm': 'MLP',
       'modelid': 'custom_model_id'
      }
train_model(args)


# **Predicting with Your MLP Model**<br>

# In[48]:


from flareml_test import test_model
args =  {'test_data_file': 'data/test_data/flaringar_simple_random_40.csv', 
         'algorithm': 'MLP', 
         'modelid': 'custom_model_id'}
custom_result = test_model(args)


# **Plotting the MLP Results**<br>

# In[49]:


from flareml_utils import plot_custom_result
plot_custom_result(custom_result)


# ### **ELM Model Training and Testing**
# **ELM Model Training with Default Data**<br>

# In[50]:


print('Loading the train_model function...')
from flareml_train import train_model
args = {'train_data_file':'data/train_data/flaringar_training_sample.csv',
        'algorithm': 'ELM',
       'modelid': 'custom_model_id'
      }
train_model(args)


# **Predicting with Your ELM Model**<br>

# In[51]:


from flareml_test import test_model
args =  {'test_data_file': 'data/test_data/flaringar_simple_random_40.csv', 
         'algorithm': 'ELM', 
         'modelid': 'custom_model_id'}
custom_result = test_model(args)


# **Plotting the ELM Resluts**<br>

# In[52]:


from flareml_utils import plot_custom_result
plot_custom_result(custom_result)


# ### **Timing**
# Please note that the execution time in mybinder varies based on the availability of resources. The average time to run the notebook is 10-15 minutes, but it could be more.
# 
# # **Conclusions**
# <!-- We present a machine-learning-as-a-service framework
# (DeepSun) for solar flare prediction. This framework provides
# two interfaces: a web server where the user enters the information through a graphical interface and a programmable
# interface that can be used by any RESTful client. DeepSun employs three existing machine learning algorithms, namely
# random forests (RF), multilayer perceptrons (MLP), extreme learning machines (ELM), and an ensemble algorithm (ENS) that combines the three machine learning algorithms. Our experimental results demonstrated the good performance of the ensemble algorithm and its superiority over the three existing machine learning algorithms.
# In the current work we focus on data samples composed of SHARP physical parameters. We collect 845 data samples
# belonging to four flare classes: B, C, M, and X across 472 active regions. In addition, the Helioseismic Magnetic
# Imager (HMI) aboard the Solar Dynamics Observatory (SDO) produces continuous full-disk observations (solar images).<br>In
# future work we plan to incorporate these HMI images into our DeepSun framework and extend our previously developed deep learning techniques to directly process the images. -->
# 
# We present a machine learning-based system (FlareML) for solar flare prediction. FlareML employs three existing machine learning algorithms, namely random forests (RF), multilayer perceptrons (MLP), extreme learning machines (ELM), and an ensemble algorithm (ENS) that combines the three machine learning algorithms. Our experimental results demonstrated the good performance of the ensemble algorithm and its superiority over the three existing machine learning algorithms. In the current work we focus on data samples composed of SHARP physical parameters. We collect 845 data samples belonging to four flare classes: B, C, M, and X across 472 active regions. In addition, the Helioseismic Magnetic Imager (HMI) aboard the Solar Dynamics Observatory (SDO) produces continuous full-disk observations (solar images). In future work we plan to incorporate these HMI images into our FlareML framework and extend our previously developed deep learning techniques to directly process the images for solar flare prediction.
# 
# # **References**
# <ol>
#     <li>
#         DeepSun: Machine-Learning-as-a-Service for Solar Flare Prediction<br>
#         Yasser Abduallah, Jason T. L. Wang and Haimin Wang<br>
#         <a target='new' href='https://iopscience.iop.org/article/10.1088/1674-4527/21/7/160'>https://iopscience.iop.org/article/10.1088/1674-4527/21/7/160</a>
#     </li>
#         <li>
#         Predicting Solar Flares Using SDO/HMI Vector Magnetic Data Products and the Random Forest Algorithm<br>
#          Chang Liu, Na Deng, Jason T. L. Wang and Haimin Wang<br>
#         <a target='new' href='https://iopscience.iop.org/article/10.3847/1538-4357/aa789b'>https://iopscience.iop.org/article/10.3847/1538-4357/aa789b</a>
#     </li>
#      <li>
#          Artificial Neural Networks: An Introduction to ANN Theory and Practice<br>
#     P. J. Braspenning, F. Thuijsman, A. J. M. M. Weijters <br>
#         <a target='new' href='https://link.springer.com/book/10.1007/BFb0027019'>https://link.springer.com/book/10.1007/BFb0027019</a>
#     </li>
#      <li>
#          Enhanced Random Search Based Incremental Extreme Learning Machine<br>
#     Guang-Bin Huang and Lei Chen<br>
#         <a target='new' href='https://www.sciencedirect.com/science/article/abs/pii/S0925231207003633?via%3Dihub'>https://www.sciencedirect.com/science/article/abs/pii/S0925231207003633?via%3Dihub</a>
#     </li>     
#      <li>
#          Predicting Solar Energetic Particles Using SDO/HMI Vector Magnetic Data Products and a
# Bidirectional LSTM Network<br>
#     Yasser Abduallah, Vania K. Jordanova, Hao Liu, Qin Li, Jason T. L. Wang and Haimin Wang<br>
#         <a target='new' href='https://iopscience.iop.org/article/10.3847/1538-4365/ac5f56'>https://iopscience.iop.org/article/10.3847/1538-4365/ac5f56</a>
#     </li>        
# </ol>

# In[ ]:




