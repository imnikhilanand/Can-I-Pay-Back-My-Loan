# Can-I-Pay-Back-My-Loan
The objective of this project is to use historical loan application data to predict whether or not an applicant will be able to repay a loan.

## Exploratory Data Analysis

- The distribution of data in the training set is imbalanced.

<p align="center">
    <img align=""src='img/class distribution.png' width='65%'>
</p>

- Lets understand the number of empty cells in the dataframe i.e. the missing data.

<p align="center">
    <img align=""src='img/heatamp empty cells.png' width='65%'>
</p>

- The different types of features in the dataframe

<table>
    <tr><th>Feature Type</th><th>Number of featues</th></tr>
    <tr><td>float64</td><td>65</td></tr>
    <tr><td>int64</td><td>41</td></tr>
    <tr><td>object</td><td>16</td></tr>
</table>

- We need to handle the 16 categorical variables in the dataset. Lets check the number of uniques values in each of these 16 categorical featues.

<table>
    <tr><th>Features</th><th>Distinct Values</th></tr>
    <tr><td>NAME_CONTRACT_TYPE</td><td>2</td></tr>
    <tr><td>CODE_GENDER</td><td>3</td></tr>
    <tr><td>FLAG_OWN_CAR</td><td>2</td></tr>
    <tr><td>FLAG_OWN_REALTY</td><td>2</td></tr>
    <tr><td>NAME_TYPE_SUITE</td><td>7</td></tr>
    <tr><td>NAME_INCOME_TYPE</td><td>8</td></tr>
    <tr><td>NAME_EDUCATION_TYPE</td><td>5</td></tr>
    <tr><td>NAME_FAMILY_STATUS</td><td>6</td></tr>
    <tr><td>NAME_HOUSING_TYPE</td><td>6</td></tr>
    <tr><td>OCCUPATION_TYPE</td><td>18</td></tr>
    <tr><td>WEEKDAY_APPR_PROCESS_START</td><td>7</td></tr>
    <tr><td>ORGANIZATION_TYPE</td><td>58</td></tr>
    <tr><td>FONDKAPREMONT_MODE</td><td>4</td></tr>
    <tr><td>HOUSETYPE_MODE</td><td>3</td></tr></td></tr>
    <tr><td>WALLSMATERIAL_MODE</td><td>7</td></tr>
    <tr><td>EMERGENCYSTATE_MODE</td><td>2</td></tr>
</table>

