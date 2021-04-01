import csv

def get_worldcup_matches(csv_filename):
    with open(csv_filename, "r", encoding="utf8") as match_records:
        for match_record in csv.reader(match_records):
            yield match_record
def filtering(row):
    return row[5] == "FIFA World Cup" #Filters per Wolrd Cup games only

if (__name__ == "__main__"):
    iter_matches = iter(get_worldcup_matches("results.csv"))

    iter_matches = filter(filtering, iter_matches)
    #next(iter_matches)  # Skipping the column names

    dictionaries = []
    listOfKeys=["date","home team","away team","home score","away score","tournament","city","country","neutral"]


    for row in iter_matches:
        dictionaries.append(dict(zip(listOfKeys,row)))
        #print(row)



    print(len(dictionaries))

    italy_goal_count = 0

    for m_dict in dictionaries:
        if(m_dict['home team'] == "Italy"):
            italy_goal_count += int(m_dict['home score'])
        elif(m_dict['away team'] == "Italy"):
            italy_goal_count += int(m_dict['away score'])
            
    print(italy_goal_count)