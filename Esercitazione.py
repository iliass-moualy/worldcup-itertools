import csv
import itertools as it
from memory_profiler import profile


#Generatore per estrarre le partite riga per riga
def get_worldcup_matches(csv_filename):
    with open(csv_filename, "r", encoding="utf8") as match_records:
        for match_record in csv.reader(match_records):
            yield match_record

#Funzione per filtrare filtrare solo le partite dei mondiali
def filtering(row):
    return row[5] == "FIFA World Cup" 


#iteratore con le partite
iter_matches = iter(get_worldcup_matches("results.csv"))

#iteratore con le partite dei mondiali
iter_matches = filter(filtering, iter_matches)


next(iter_matches)  # Skipping the column names



#Creazione dizionari e lista di dizionari 
dictionaries = []
listOfKeys=["date","home team","away team","home score","away score","tournament","city","country","neutral"]

for row in iter_matches:
    dictionaries.append(dict(zip(listOfKeys,row)))


#print(dictionaries)


#Conteggio gol fatti dall'italia nei campionati mondiali tramite generator expressions

italy_goal_count = 0

italy_goal_count = sum(int(m_dict['home score']) for m_dict in dictionaries if(m_dict['home team'] == "Italy"))

italy_goal_count += sum(int(m_dict['away score']) for m_dict in dictionaries if(m_dict['away team'] == "Italy"))
    
#print(italy_goal_count)

