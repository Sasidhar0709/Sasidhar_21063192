# Import the packages Required for Visualisation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#data handling
def format_data(path):
    ''' 
    the Function is used to create two datasets using the parameters for the columns "country" and "year."
    '''
    a_df = pd.read_excel(path)
    a_df=a_df.drop(columns=['Indicator Code','Country Code'])
    #creating second dataframe using transpose 
    a2_df = a_df.transpose()
    a2_df.columns = a2_df.iloc[0].values.tolist()
    
    a2_df=a2_df.iloc[1:]
 
    return a_df,a2_df

data_country,data_year=format_data('World Bank climate_data.xlsx')

colmns=data_year.iloc[0].unique()

# taking fie countries for the data analysis of the world bank parameters

countries=['Brazil','India','United Kingdom','Germany','Belgium']

countries_select=data_year[countries]

#plotting bar graphs
def plot_bar(data_input,indicator):
    '''
    The function is used to plot the bar graphs for the given data and its indicators
    parameters: data_input- dataset, indicator- indicators to plot
    '''
    t=[]
    c= indicator
    for i in range(5):
        t.append(data_input.iloc[:,c])
        i=i+1
        c=c+76
    d= pd.DataFrame(t)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[[30,36,42,48,54]].plot(kind='bar',figsize=(15,8),title=colmns[indicator]+' from 1990 to 2019')
    plt.show()
    
plot_bar(countries_select,4)
plot_bar(countries_select,52)

#plotting correlation
country=data_year[['Germany']]
t=[]
indi_index=[4,52,55,43,58,63]
for i in indi_index:
    t.append(country.iloc[:,i])
d= pd.DataFrame(t)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]
d=d[1:]
d=d.fillna(d.median())
ax = sns.heatmap(
    d.corr(), 
    cmap="YlGnBu", annot=True
)
plt.title(" Germany indicators correlation")
plt.show()

#plotting correlation
country=data_year[['India']]
t=[]
indi_index=[4,52,55,43,58,63]
for i in indi_index:
    t.append(country.iloc[:,i])
d= pd.DataFrame(t)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]
d=d[1:]
d=d.fillna(d.median())
ax = sns.heatmap(
    d.corr(), 
    cmap="YlGnBu", annot=True
)
plt.title(" India indicators correlation")
plt.show()



#plotting line graph
def plot_line(data_input,indicator):
  
    t=[]
    c= indicator
    for i in range(5):
        t.append(data_input.iloc[:,c])
        i=i+1
        c=c+76
    d= pd.DataFrame(t)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[30:58].plot(kind='line',figsize=(15,8),title=colmns[indicator]+' from 1990 to 2015')
    plt.show()

plot_line(countries_select,60)
plot_line(countries_select,37)







