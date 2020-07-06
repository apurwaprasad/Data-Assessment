#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing library
import os
import json
import pandas as pd
import glob
from pandas.io.json import json_normalize

#Display all columns for excel/csv files
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Ignore warnings
import warnings
warnings.filterwarnings("ignore")


# # Reading each Folder to extract the JSON files

# ## Optimization Data 1

# ### Loan Data-1

# In[2]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData1/LoanData1/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanData1 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanData1['file_name'] = json_file_names

LoanData1.info()


# ### Loan Results Data-1

# In[3]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData1/LoanResultsData1/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanResultsData1 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanResultsData1['file_name'] = json_file_names

LoanResultsData1.info()


# ## Optimization Data 2

# ### Loan Data-2

# In[4]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData2/LoanData2/'
data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanData2 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanData2['file_name'] = json_file_names

LoanData2.info()


# ### Loan Results Data-2

# In[5]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData2/LoanResultsData2/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanResultsData2 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanResultsData2['file_name'] = json_file_names

LoanResultsData2.info()


# ## Optimization Data 3

# ### Loan Data- 3

# In[6]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData3/LoanData3/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanData3 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanData3['file_name'] = json_file_names

LoanData3.info()


# ### Loan Results Data-3

# In[7]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/OptimizationData3/LoanResultsData3/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanResultsData3 = pd.DataFrame.from_dict(json_normalize(data_list))
LoanResultsData3['file_name'] = json_file_names

LoanResultsData3.info()


# ## PoolOptimization Data for TC v5

# ### BaselineConstraintsSetB

# In[8]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/PoolOptimizationDataforTCv5/BaselineConstraintsSetB/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
BaselineConstraintsSetB = pd.DataFrame.from_dict(json_normalize(data_list))
BaselineConstraintsSetB['file_name'] = json_file_names

BaselineConstraintsSetB.info()


# ### EligiblePricingCombinations

# In[9]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/PoolOptimizationDataforTCv5/EligiblePricingCombinations/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
EligiblePricingCombinations = pd.DataFrame.from_dict(json_normalize(data_list))
EligiblePricingCombinations['file_name'] = json_file_names

EligiblePricingCombinations.info()


# ### LoanData

# In[10]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/PoolOptimizationDataforTCv5/LoanData/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
LoanData = pd.DataFrame.from_dict(json_normalize(data_list))
LoanData['file_name'] = json_file_names

LoanData.info()


# ### PoolOptionData

# In[11]:


# Read multiple json files from a directory and convert them to pandas dataframe
# Add file names as a new column in DataFrame
path_to_json = '/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Mortgage_Pooling_v1/PoolOptimizationDataforTCv5/PoolOptionData/'

data_list = []
json_file_names = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name) as json_file:
        image_name = os.path.basename(file_name)
        data_name = os.path.splitext(image_name)[0]
        data = json.load(json_file)
        data_list.append(data)
        json_file_names.append(data_name)
        
PoolOptionData = pd.DataFrame.from_dict(json_normalize(data_list))
PoolOptionData['file_name'] = json_file_names

PoolOptionData.info()


# # Summarising the extracted data

# # Loan Data:
# LoanData1
# RangeIndex: 309 entries, 0 to 308
# Data columns (total 17 columns)
# Extra Column: LockType(Singlevalue-M)
# 
# LoanData2
# RangeIndex: 3556 entries, 0 to 3555
# Data columns (total 16 columns)
# 
# LoanData3
# RangeIndex: 3556 entries, 0 to 3555
# Data columns (total 16 columns)

# In[12]:


LoanData1.head()


# In[13]:


LoanData2.head()


# In[14]:


LoanData3.head()


# # Loan Results Data :
# LoanResultsData1
# RangeIndex: 699 entries, 0 to 698
# Data columns (total 8 columns)
# 
# LoanResultsData2
# RangeIndex: 44070 entries, 0 to 44069
# Data columns (total 12 columns)
# 
# LoanResultsData3
# RangeIndex: 44070 entries, 0 to 44069
# Data columns (total 13 columns)

# In[15]:


LoanResultsData1.head()


# In[16]:


LoanResultsData2.head()


# In[17]:


LoanResultsData3.head()


# # Pool Optimization Data for TCv5
# BaselineConstraintsSetB
# RangeIndex: 3549 entries, 0 to 3548
# Data columns (total 5 columns)
# 
# 
# EligiblePricingCombinations
# RangeIndex: 45913 entries, 0 to 45912
# Data columns (total 5 columns)
# 
# LoanData
# RangeIndex: 3549 entries, 0 to 3548
# Data columns (total 10 columns)
# 
# PoolOptionData
# RangeIndex: 458 entries, 0 to 457
# Data columns (total 6 columns)

# In[18]:


BaselineConstraintsSetB.head()


# In[19]:


EligiblePricingCombinations.head()


# In[20]:


LoanData.head()


# In[21]:


PoolOptionData.head()


# # Transforming Data for making visualizations

# ## LoanData1 and LoanResultsData1
# Merging LoanData and LoanResultsData to create one dataframe which can be converted to excel file later.
# Using rank column to filter out the cId's with rank 1 to be used and merged with LoanData to find insights further.

# In[22]:


LoanResultsData1.count()


# In[23]:


#LoanResultsData1
#Using LoanResultsData1 to identify cId with rank 1
LoanResultsData1_rank1= LoanResultsData1[LoanResultsData1['Rank']==1]
LoanResultsData1_rank1.count()


# In[24]:


#Checking number of duplicates against each cId
LoanResultsData1_rank1['cId'].value_counts()

#three records with same cId


# In[25]:


#count of all columns
LoanResultsData1.count()


# In[26]:


#count of cId with rank 1
LoanResultsData1_rank1.count()


# In[27]:


#droping duplicate cId's and keeping first record
LoanResultsData1_rank1 = LoanResultsData1_rank1.drop_duplicates(subset='cId', keep="first")
LoanResultsData1_rank1.head()


# In[28]:


#Verifying records after dropping
LoanResultsData1_rank1.count()


# In[29]:


#LoanData1
#count of all columns
LoanData1.count()


# In[30]:


#Merging both dataframes LoanData1 and LoanResultsData1
Loan1_final = pd.merge(LoanData1,LoanResultsData1_rank1,left_on='cID',right_on='cId', how= 'inner')

#Verifying number of records
Loan1_final.count()


# ## LoanData2 and LoanResultsData2
# Merging LoanData2 and LoanResultsData2 to create one dataframe which can be converted to excel file later.
# Using rank column to filter out the cId's with rank 1 to be used and merged with LoanData to find insights further.

# ### LoanResultsData2

# In[31]:


#LoanResultsData2
#Using LoanResultsData2 to identify cID with rank 1
LoanResultsData2_rank1= LoanResultsData2[LoanResultsData2['Rank']==1]
LoanResultsData2_rank1.count()


# In[57]:


#Checking number of duplicates against each cId
LoanResultsData2_rank1['cID'].value_counts()

#No duplicates found


# In[33]:


LoanResultsData2_rank1.count()


# In[34]:


LoanData2.count()


# In[35]:


#Merging both dataframes LoanData1 and LoanResultsData1
Loan2_final = pd.merge(LoanData2,LoanResultsData2_rank1,left_on='cID',right_on='cID', how= 'inner')


# In[36]:


#Verifying number of records
Loan2_final.count()


# ### LoanResultsData3

# ## LoanData3 and LoanResultsData3
# Merging LoanData3 and LoanResultsData3 to create one dataframe which can be converted to excel file later.
# Using rank column to filter out the cId's with rank 1 to be used and merged with LoanData to find insights further.

# In[37]:


LoanResultsData3.count()


# In[38]:


#Using LoanResultsData3 to identify cId with rank 1
LoanResultsData3_rank1= LoanResultsData3[LoanResultsData3['Rank']==1]
LoanResultsData3_rank1.count()


# In[39]:


#Checking number of duplicates against each cId
LoanResultsData3_rank1['cID'].value_counts()

#No duplicates found


# In[40]:


LoanData3.count()


# In[41]:


#Merging both dataframes LoanData1 and LoanResultsData1
Loan3_final = pd.merge(LoanData3,LoanResultsData3_rank1,left_on='cID',right_on='cID', how= 'inner')

#Verifying number of records
Loan3_final.count()


# In[42]:


#Exporting out data to xlsx for all merged Loan Data's with Loan Data Result's 
Loan1_final.to_excel('/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Data/Loan1_final.xlsx', index = False)
Loan2_final.to_excel('/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Data/Loan2_final.xlsx', index = False)
Loan3_final.to_excel('/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Data/Loan3_final.xlsx', index = False)


# ## LoanData3 and LoanResultsData3
# Merging LoanData3 and LoanResultsData3 to create one dataframe which can be converted to excel file later.
# Using rank column to filter out the cId's with rank 1 to be used and merged with LoanData to find insights further.

# In[43]:


EligiblePricingCombinations.head()


# In[44]:


#Using the LoanID to find max Price, P_ijk and saving one LoanId with max price
EligiblePricingComb = EligiblePricingCombinations.iloc[EligiblePricingCombinations.groupby('LoanID')['Price, P_ijk'
].agg(pd.Series.idxmax)]
EligiblePricingComb=pd.DataFrame(EligiblePricingComb)
EligiblePricingComb.count()


# In[45]:


PoolOptionData.head()


# In[46]:


PoolOptionData.count()


# In[47]:


#Merging EligiblePricingCombinations dataframe with Loan having max price with PoolOptionData.
#EligiblePricingComb1 will give deatils about Loan, Max price issued, pool details
EligiblePricingComb1 = pd.merge(EligiblePricingComb, PoolOptionData,
                                left_on=['Pool Opton, j'],right_on=['Pool Option, j'], how = 'inner')

#EligiblePricingComb1=pd.DataFrame(EligiblePricingComb1)
EligiblePricingComb1.head()


# In[48]:


#Verifying records after merge
EligiblePricingComb1.count()


# In[49]:


#exporting the resukting file into excel
EligiblePricingComb1.to_excel('/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Data/EligiblePricingComb1.xlsx', index = False)


# ## EligiblePricingComb and LoanData
# Merging EligiblePricingComb dataframe with LoanData to get more details about loan and pool.

# In[50]:


LoanData.head()


# In[51]:


LoanData.count()


# In[52]:


#Merging EligiblePricingComb dataframe with LoanData to get more details about loan and pool.
LoanPoolDetails = pd.merge(EligiblePricingComb, LoanData,on=['LoanID'], how = 'inner')


# In[53]:


#verifying number of records after merge.
LoanPoolDetails.count()


# In[58]:


#exporting the resukting file into excel
LoanPoolDetails.to_excel('/Users/apurwaprasad/Desktop/BlackKnight_data_challenge/Data/LoanPoolDetails.xlsx', index = False)

