import pandas as pd
from datetime import datetime
import os
import subprocess
import isbnlib
import spacy

                                                            

# Specify the path to the Python script and the folder containing it
feature_script_path = r"DataBase\recap_db_feature.py"

# Use subprocess to run the script
result = subprocess.check_output(['python', feature_script_path])
result_list = eval(result)
date_actuelle = datetime.now()

feat = result_list
with open(r'DataBase\Extract_ML_DB\DB_notice.txt', 'w') as file:
    n_db=0
    for a in feat[0]:
        for b in feat[1]:
            for c in feat[2]:
                for d in feat[3]:
                    for e in feat[4]:
                        for f in feat[5]:
                            for g in feat[6]:
                                for h in feat[7]:
                                    for i in feat[8]:
                                        for j in feat[9]:
                                            for k in feat[10]:
                                                for l in feat[11]:
                                                    n_db += 1
                                                    t = [a,b,c,d,e,f,g,h,i,j,k,l]
                                                    index_name = ["bookID","title","authors","average_rating","isbn","isbn13", "language_code","num_pages", "ratings_count", "text_reviews_count", "publication_date", "publisher"]
                                                    file.write(f'DATA BASE Iteration N{n_db}:\n')
                                                    
                                                    for feature_index in range(len(index_name)):
                                                        file.write(f'   {index_name[feature_index]}: {t[feature_index]},\n')
                                                    
                                                    file.write('\n\n\n')
                                                    
                                                    path = r"DataBase\\Extract_ML_DB"

                                                    df = pd.read_csv(r'DataBase\books.csv')
                                                    
                                                    for index in range(len(t)):
                                                        if t[index] == "drop":
                                                            df = df.drop(index_name[index], axis=1)
                                                        
                                                        elif t[index] == "length":
                                                            df[f"{index_name[index]}_length"] = df[index_name[index]].str.len()
                                                            df = df.drop(index_name[index], axis=1)
                                                        
                                                        elif t[index] == "nword":
                                                            def count_words(text):
                                                                words = text.split()
                                                                return len(words)
                                                            df[f"{index_name[index]}_nword"] = df[index_name[index]].apply(count_words)
                                                            df = df.drop(index_name[index], axis=1)

                                                        elif t[index] == "isbn_country":
                                                            def get_country(nbr):
                                                                txt = str(nbr)[3]
                                                                return txt
                                                                
                                                            df[f"{index_name[index]}_country"] = df[index_name[index]].apply(get_country)

                                                        elif t[index] == "vector":
                                                            df_dummies = pd.get_dummies(df[index_name[index]])
                                                            df = pd.concat([df, df_dummies], axis=1).drop(columns=f"{index_name[index]}")
                                                        
                                                        elif t[index] == "month":
                                                            df[index_name[index]] = df[index_name[index]].str.split('/').str[0]
                                                        
                                                        elif t[index] == "day":
                                                            df[index_name[index]] = df[index_name[index]].str.split('/').str[1]

                                                        elif t[index] == "year":
                                                            df[index_name[index]] = df[index_name[index]].str.split('/').str[2]

                                                            #for z, date_str in enumerate(df[index_name[index]]):
                                                            #    try:
                                                            #        df.loc[z, index_name[index]] = pd.to_datetime(date_str, format='%m/%d/%Y')
                                                            #    except ValueError as v:
                                                            #        file.write(f"Error in row {z + 1} and feature {index_name[index]}, the row is deleted. \nERROR:{v}")
                                                        
                                                        elif t[index] == "age":
                                                            df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
                                                            # Supprimer les lignes avec des dates de publication invalides
                                                            df = df.dropna(subset=['publication_date'])
                                                                
                                                            df['age'] = (date_actuelle - df['publication_date']).dt.days // 365
                                                        
                                                        elif t[index] == "natural_languge":
                                                            # Charger le modèle SpaCy pré-entraîné
                                                            nlp = spacy.load("en_core_web_sm")

                                                            # Fonction pour extraire les entités nommées d'un titre
                                                            def extract_entities(title):
                                                                doc = nlp(title)
                                                                entities = [(ent.text, ent.label_) for ent in doc.ents]
                                                                return entities

                                                            # Appliquer la fonction à votre ensemble de données
                                                            df['title_entities'] = df['title'].apply(extract_entities)
                                                            
                                                          
                                                    df.to_csv(f"{path}\\DB_{n_db}.csv", index=False)


                                                        
                                                            

                                                            

