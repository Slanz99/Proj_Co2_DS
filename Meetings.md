# 10.08.2023 | 14:00 | Project Call with Aziz
## Agenda
1. [Questions for Aziz][Questions for the next Project Meeting with Aziz]
2. What are M1, M1G, N1, N1G, N2 in whisker chart
3. Concept google colab mount how can we solve the issue with the big data set (for more working on the code instead of waiting)
    ```python
    filename = '/content/drive/MyDrive/DataScientest CO2 Project/data.csv'
    df = pd.read_csv(filename, sep=',', index_col = 0, low_memory=False)

    display(df.head(15))
    ```
5. 

# 07.08.2023 | 11:00 | Team Meeting preparation
## Agenda
1. Discuss findings, visualizations and strategie for presentation
2.  

## Decisions
- get rid of the columns > 80% missing values
- **Feature `FT`**
    - combine Datas ('Ft'):
        1. Diesel 
        2. Petrol 
        3. Electric
        4. Hybrid
        5. Liquid (LPG, NG, NG-Biomethan)
    get rid of:
        6. HYDROGEN
        7. UNKNOWN

## Tasks
### Navid:
    [] Checking the fuel types and make a descison for reducing

## Code Snippets
### reduce Dataste with `sample()` ***method***
```python
df_sample = df.sample(n=1000, random_state=42)
df_sample.describe()
```


# 07.08.2023 | 11:00 | Team Meeting
## Agenda
1. Use of  Colab ✅
2. task 2023_CO2 Project_Data Audit ✅
3. share my Gihub File ✅

## Notes
- **Kaggle Inspirations:**
    1. [Overview regression techniques](https://www.kaggle.com/code/lykin22/co2-emission-regression-techniques)
    2. [Great EDA + viz](https://www.kaggle.com/code/drfrank/co2-emission-eda-visualization-machine-learnin#-3.Exploratory-Data-Analysis)
    3. [+99% Acc](https://www.kaggle.com/code/a7madmostafa/eda-modelling-for-co2-emission-99-acc)

- Every 4 Years there is a signifcant change in the cars 
- **decision for the rule:** "when 20% of the data are missing we get rid of it"

## next steps
- split the visualizaton (Everyone min 4 vizualisations),graphs, plots
- Next meting on wednesday 3 pm [click me for Meeting Link](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NW5pbzQ5aGc1YWdtY3Zxb2k1bDFidm1iZ2ogbGFuei5zdEBt&tmsrc=lanz.st%40gmail.com)
- Review an Wednesday

## Questions for the next Project Meeting with Aziz

>- What data can we do without?
>- Do we have to use the 2013 and 2014 French Gouverment Data?


---
# 03.08.2023 | 14:00 | Project Call with Aziz

## My Notes
    - Use Var 18 as Target Variable ERWLTP
    - How to deal with the catagorical values
    - Display some graphs 

## Summary of Aziz

> Goals for the week of August 7th: Write up your initial exploration of the dataset using the template. Try to identify the most relevant features -> display some correlation graphs. Think about how to handle missing     
 values. Display some graphs: the number of different vehicle brands, the distribution of CO2 emissions in the dataset, the temporal evolution of vehicle characteristics, and the correlations between features and target 
 values. How are you planning to encode your categorical variables

## Goals
[Google Table Template](https://docs.google.com/spreadsheets/d/19EffSCbW8gdt67DQ4ZDm2azBAgCSZk_XFSyCPIuHPws/edit?usp=sharing)

    1. Wrtite initial exploration using the *Google Table Template* 
    2. Identify the most relevant `features`
    3. Display some correlation graphs
    4. How to handle missing values
    5. Display some graphs:
        - the number of different vehicle brands
        - the distribution of CO2 emissions in the dataset
        - the temporal evolution of vehicle characteristics
        - correlations between `features` and `target_values`
    6. How are you planning to encode your categorical variables
