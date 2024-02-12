dico = {"bookID" : ["drop"],
"title": ["length", "num_word", "drop"],
"authors" : ["drop"],
"average_rating" : ["Keep"],
"isbn" : ["drop"],
"isbn13" : ["drop"],# "isbn_country",
"language_code" : ["vector", "drop"],
"num_pages" : ["Keep"],
"ratings_count" : [], #, "min_number_1", "min_number_50"
"text_reviews_count" : ["Keep"],
"publication_date" : ["day", "month", "year", "keep", "drop", "age"],
"publisher" : ["drop"]}


t = []
n = 0
for feature in dico:
    t.append([])
    for values in dico[feature]:
        t[n].append(values)
    n += 1
print(t)


    