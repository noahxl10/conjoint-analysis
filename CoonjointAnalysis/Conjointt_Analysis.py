
import pandas as pd 
import random
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/noahalex/Documents/Personal Dox/School Docs/State of Utah/State of Utah Conjoint_data.xlsx')

def winningEmail(df):
    emails = df['Q1']
    emails = emails[emails.notna()]
    for i in range(10):
        print('Winning email: ', random.choice(emails.tolist()))

def toCsv(df):
    df.to_csv('/Users/noahalex/Documents/Personal Dox/School Docs/State of Utah/DataTest1.csv')

def Importance(df, var):
    fig, ((ax1, ax2, ax3),(ax4, ax5, ax6))  = plt.subplots(nrows = 2, ncols = 3, sharex=True, figsize = (10,8))
    fig.suptitle('Factor Importance by Age')
    x1 = df.groupby(var)['Salary_Importance'].mean()
    x2 = df.groupby(var)['Flexability_Importance'].mean()
    x3 = df.groupby(var)['Core_Importance'].mean()
    x4 = df.groupby(var)['Perks_Importance'].mean()
    x5 = df.groupby(var)['Stability_Importance'].mean()
    x6 = df.groupby(var)['Growth_Importance'].mean()

    x1.plot.bar(ax = ax1)
    ax1.set_title('Salary Importance')
    x2.plot.bar(ax = ax2)
    ax2.set_title('Flexibility Importance')
    x3.plot.bar(ax = ax3)
    ax3.set_title('Core Importance')
    x4.plot.bar(ax = ax4)
    ax4.set_title('Perks Importance')
    x5.plot.bar(ax = ax5)
    ax5.set_title('Stability Importance')
    x6.plot.bar(ax = ax6)
    ax6.set_title('Growth Importance')
    #ax6.set_title('Importance of Factors')

    plt.show()


def Utility(df, var):
    # VAR IS AGE OR GENDER
    fig, ((ax1, ax2, ax3),(ax4, ax5, ax6))  = plt.subplots(nrows = 2, ncols = 3, sharex=True, sharey = True, figsize = (10,8))
    fig.suptitle('Utility by Gender or Age')
    x1 = df.groupby(var)['Salary_10% below industry average_Rescaled_Utility'].mean()
    x2 = df.groupby(var)['Salary_Industry average_Rescaled_Utility'].mean()
    x3 = df.groupby(var)['Salary_10% above industry average_Rescaled_Utility'].mean()
    x4 = df.groupby(var)['Flexability_100% on-site hours 0% work at home_Rescaled_Utility'].mean()
    x5 = df.groupby(var)['Flexability_75% on-site hours 25% work at home_Rescaled_Utility'].mean()
    x6 = df.groupby(var)['Flexability_50% on-site hours 50% work at home_Rescaled_Utility'].mean()
    x7 = df.groupby(var)['Flexability_25% on-site hours 75% work at home_Rescaled_Utility'].mean()
    x8 = df.groupby(var)['Core_Health Care_Rescaled_Utility'].mean()
    x9 = df.groupby(var)['Core_Personal sick/vacation leave_Rescaled_Utility'].mean()
    x10 = df.groupby(var)['Perks_Childcare credit_Rescaled_Utility'].mean()
    x11 = df.groupby(var)['Perks_Tuition assistance_Rescaled_Utility'].mean()

    x1.plot.bar(ax = ax1, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)]) # color = (.1,.3,.5) for same color bars... or color = 'blue'
    ax1.set_title('Salary Below Utility')
    x2.plot.bar(ax = ax2, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)])
    ax2.set_title('Salary Avg Utility')
    x3.plot.bar(ax = ax3, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)])
    ax3.set_title('Salary Above Utility')
    x4.plot.bar(ax = ax4, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)])
    ax4.set_title('Perks Importance')
    x5.plot.bar(ax = ax5, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)])
    ax5.set_title('Stability Importance')
    x6.plot.bar(ax = ax6, color = [(.1,.3,.5), (.1,.5,.9), (.1,.8,.9)])
    ax6.set_title('Growth Importance')
    #ax6.set_title('Importance of Factors')

    plt.show()

def size(df):
    x1 = df.groupby('Age')

def clean(df):
    # Clean and Assign String Vals to Data
    try:

        df = df[df['Zip'].notna()]
        df.loc[(df.Gender == 1), 'Gender']='Male'
        df.loc[(df.Gender == 2), 'Gender']='Female'
        df.loc[(df.Gender == 3), 'Gender']='Other'

        df.loc[(df.Dependents == 1), 'Dependents']='Yes'
        df.loc[(df.Dependents == 2), 'Dependents']='No'

        df.loc[(df.Education == 1), 'Education']='Some High School'
        df.loc[(df.Education == 2), 'Education']='High School graduate'
        df.loc[(df.Education == 3), 'Education']='Some college'
        df.loc[(df.Education == 4), 'Education']='Associates degree'
        df.loc[(df.Education == 5), 'Education']='Bachelors degree'
        df.loc[(df.Education == 6), 'Education']='Graduate school'

        df.loc[(df.Age == 1), 'Age']='18-24'
        df.loc[(df.Age == 2), 'Age']='25-34'
        df.loc[(df.Age == 3), 'Age']='35-44'
        df.loc[(df.Age == 4), 'Age']='45-54'
        df.loc[(df.Age == 5), 'Age']='55+'

        df.loc[(df.workExperience == 1), 'workExperience']='0-4 years'
        df.loc[(df.workExperience == 2), 'workExperience']='5-9 years'
        df.loc[(df.workExperience == 3), 'workExperience']='10+ years'
        df['workExperience'].fillna('No Opinion', inplace = True)

        df.loc[(df.effectivelyServes == 1), 'effectivelyServes']='Disagree'
        df.loc[(df.effectivelyServes == 2), 'effectivelyServes']='Agree'
        df.loc[(df.effectivelyServes == 3), 'effectivelyServes']='No Opinion'
        df['effectivelyServes'].fillna('No Opinion', inplace = True)

        df.loc[(df.employmentOpportunities == 1), 'employmentOpportunities']='Disagree'
        df.loc[(df.employmentOpportunities == 2), 'employmentOpportunities']='Agree'
        df['employmentOpportunities'].fillna('No Opinion', inplace = True)

        df.loc[(df.benefits == 1), 'benefits']='Disagree'
        df.loc[(df.benefits == 2), 'benefits']='Agree'
        df['benefits'].fillna('No Opinion', inplace = True)
    
    except:
        df = df[df['Zip'].notna()]
        df.loc[(df.Gender == 1), 'Gender']='Male'
        df.loc[(df.Gender == 2), 'Gender']='Female'
        df.loc[(df.Gender == 3), 'Gender']='Other'

        df.loc[(df.Dependents == 1), 'Dependents']='Yes'
        df.loc[(df.Dependents == 2), 'Dependents']='No'

        df.loc[(df.Education == 1), 'Education']='Some High School'
        df.loc[(df.Education == 2), 'Education']='High School graduate'
        df.loc[(df.Education == 3), 'Education']='Some college'
        df.loc[(df.Education == 4), 'Education']='Associates degree'
        df.loc[(df.Education == 5), 'Education']='Bachelors degree'
        df.loc[(df.Education == 6), 'Education']='Graduate school'

        df.loc[(df.Age == 1), 'Age']='18-24'
        df.loc[(df.Age == 2), 'Age']='25-34'
        df.loc[(df.Age == 3), 'Age']='35-44'
        df.loc[(df.Age == 4), 'Age']='45-54'
        df.loc[(df.Age == 5), 'Age']='55+'

        df.loc[(df.workExperience == 1), 'workExperience']='0-4 years'
        df.loc[(df.workExperience == 2), 'workExperience']='5-9 years'
        df.loc[(df.workExperience == 3), 'workExperience']='10+ years'
        df['workExperience'].fillna('No Opinion', inplace = True)

        df.loc[(df.effectivelyServes == 1), 'effectivelyServes']='Disagree'
        df.loc[(df.effectivelyServes == 2), 'effectivelyServes']='Agree'
        df.loc[(df.effectivelyServes == 3), 'effectivelyServes']='No Opinion'
        df['effectivelyServes'].fillna('No Opinion', inplace = True)

        df.loc[(df.employmentOpportunities == 1), 'employmentOpportunities']='Disagree'
        df.loc[(df.employmentOpportunities == 2), 'employmentOpportunities']='Agree'
        df['employmentOpportunities'].fillna('No Opinion', inplace = True)

        df.loc[(df.benefits == 1), 'benefits']='Disagree'
        df.loc[(df.benefits == 2), 'benefits']='Agree'
        df['benefits'].fillna('No Opinion', inplace = True)

    return df


## GENERAL DICTIONARIES ##
importanceDict = {
    'Salary': df['Salary_Importance'].mean(),
    'Flexibility': df['Flexability_Importance'].mean(),
    'Core': df['Core_Importance'].mean(),
    'Perks': df['Perks_Importance'].mean(),
    'Stability': df['Stability_Importance'].mean(),
    'Growth': df['Growth_Importance'].mean()
}

ageDict = {
    '18-24' : df[df['Age']=='18-24'],
    '25-34' : df[df['Age']=='25-34'],
    '35-44' : df[df['Age']=='35-44'],
    '45-54' : df[df['Age']=='45-54'],
    '55+' : df[df['Age']=='55+']
}

utilityDict = {
    'Salary below': df['Salary_10% below industry average_Rescaled_Utility'].mean(),
    'Salary avg': df['Salary_Industry average_Rescaled_Utility'].mean(),
    'Salary above': df['Salary_10% above industry average_Rescaled_Utility'].mean()
}





df = clean(df)
#print(df)
yes = len(df[df.employmentOpportunities == 'Agree'])
no = len(df[df.employmentOpportunities == 'Disagree'])
ar = [yes, no]

labs = ['Yes', 'No']
plt.bar(yes,yes, 20, color = '#b87b20')
plt.bar(no,no, 20, color = '#3e638a')
plt.xticks(ar, labs)
plt.title('Are you aware of the employment \nopportunities from the State of Utah?')
plt.show()

# # Bar Plot for age vs. importanc
#Importance(df, 'Gender')


# # Utility calculations/graphing
# Utility(df, 'Gender')





