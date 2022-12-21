# -*- coding: utf-8 -*-

"""
Created on Sun Dec 18 18:24:00 2022

@author: Nikhil

"""

# importing the libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# loading the datasets
application_test = pd.read_csv("application_test.csv")
application_train = pd.read_csv("application_train.csv")
bureau_balance = pd.read_csv("bureau_balance.csv")
beaurea = pd.read_csv("bureau.csv")
credit_card_balance = pd.read_csv("credit_card_balance.csv")
installments_payments = pd.read_csv("installments_payments.csv")
POS_CASH_balance = pd.read_csv("POS_CASH_balance.csv")
previous_application = pd.read_csv("previous_application.csv")
sample_submission = pd.read_csv("sample_submission.csv")
HomeCredit_columns_description = pd.read_csv("HomeCredit_columns_description.csv", encoding='latin1')


""" Let's train the model on the data available at the time applying for the loan
"""

# distribution of classes
agg_vals = application_train.groupby('TARGET').aggregate({'TARGET':'count'})
plt.bar(agg_vals.index, agg_vals['TARGET'], width=0.1)


























