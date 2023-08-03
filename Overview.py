import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset 1 french gouverment 2013 = `fg_2013`
fg_2013 = pd.read_csv("Projects\Project_CO2_DataScientest\Proj_Co2_DS\Data\cl_JUIN_2013-complet3.csv",
                                    sep=";", encoding= 'latin-1')
fg_2013.info()
# Create a mapping dictionary for column name translation
column_name_mapping = {
    'Marque': 'Brand',
    'Modèle dossier': 'Model file',
    'Modèle UTAC': 'UTAC model',
    'Désignation commerciale': 'Commercial designation',
    'CNIT': 'CNIT',
    'Type Variante Version (TVV)': 'Type Variant Version (TVV)',
    'Carburant': 'Fuel',
    'Hybride': 'Hybrid',
    'Puissance administrative': 'Administrative power',
    'Puissance maximale (kW)': 'Maximum power (kW)',
    'Boîte de vitesse': 'Transmission',
    'Consommation urbaine (l/100km)': 'Urban consumption (l/100km)',
    'Consommation extra-urbaine (l/100km)': 'Extra-urban consumption (l/100km)',
    'Consommation mixte (l/100km)': 'Combined consumption (l/100km)',
    'CO2 (g/km)': 'CO2 (g/km)',
    'CO type I (g/km)': 'CO type I (g/km)',
    'HC (g/km)': 'HC (g/km)',
    'NOX (g/km)': 'NOX (g/km)',
    'HC+NOX (g/km)': 'HC+NOX (g/km)',
    'Particules (g/km)': 'Particulates (g/km)',
    'masse vide euro min (kg)': 'Empty mass euro min (kg)',
    'masse vide euro max (kg)': 'Empty mass euro max (kg)',
    'Champ V9': 'Field V9',
    'Date de mise à jour': 'Update date',
    'Carrosserie': 'Body',
    'gamme': 'Range'
}

# Rename the columns using the mapping dictionary
fg_2013.rename(columns=column_name_mapping, inplace=True)

print(fg_2013.head(10))
print(fg_2013.describe())

