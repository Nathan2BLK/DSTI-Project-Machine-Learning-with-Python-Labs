dico = {"bookID" : ["drop"],
"title": ["length", "nword", "drop"],
"authors" : ["drop"],
"average_rating" : ["Keep"],
"isbn" : ["drop"],
"isbn13" : ["isbn_country", "drop"],  
"language_code" : ["vector", "drop"],
"num_pages" : ["Keep"],
"ratings_count" : [], #, "min_number_1", "min_number_?"
"text_reviews_count" : ["Keep"],
"publication_date" : ["day", "month", "year", "general", "drop", "age"],
"publisher" : ["drop"]}


t = []
n = 0
for feature in dico:
    t.append([])
    for values in dico[feature]:
        t[n].append(values)
    n += 1
print(t)


    