import pandas as pd
from datetime import datetime
import os
import subprocess
import spacy

                                                            

# Specify the path to the Python script and the folder containing it
feature_script_path = r"First Solution\Feature\recap_db_feature.py"

# Use subprocess to run the script
result = subprocess.check_output(['python', feature_script_path])
result_list = eval(result)
date_actuelle = datetime.now()

feature = result_list
with open(r'DataBase\Extract_ML_DB\DB_notice.txt', 'w') as file:
    n_db=0
    for a in feature[0]:
        for b in feature[1]:
            for c in feature[2]:
                for d in feature[3]:
                    for e in feature[4]:
                        for f in feature[5]:
                            for g in feature[6]:
                                for h in feature[7]:
                                    for i in feature[8]:
                                        for j in feature[9]:
                                            for k in feature[10]:
                                                for l in feature[11]:
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
                                                        
                                                        elif t[index] == "num_word":
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
                                                            df = df.drop(index_name[index], axis=1)
                                                        
                                                        elif t[index] == "day":
                                                            df[index_name[index]] = df[index_name[index]].str.split('/').str[1]
                                                            df = df.drop(index_name[index], axis=1)

                                                        elif t[index] == "year":
                                                            df[index_name[index]] = df[index_name[index]].str.split('/').str[2]
                                                            df = df.drop(index_name[index], axis=1)
                                                        
                                                        elif t[index] == "age":
                                                            df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
                                                            # Supprimer les lignes avec des dates de publication invalides
                                                            df = df.dropna(subset=['publication_date'])
                                                            df['age'] = (date_actuelle - df['publication_date']).dt.days // 365
                                                        
                                                          
                                                    df.to_csv(f"{path}\\DB_{n_db}.csv", index=False)


                                                        
                                                            

                                                            

