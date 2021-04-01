import csv



def get_worldcup_matches(csv_filename):
    with open(csv_filename, "r", encoding="utf8") as match_records:
        for match_record in csv.reader(match_records):
            yield match_record

def filtering(row):
    return row[5] == "FIFA World Cup" #Filters per Wolrd Cup games only


iter_matches = iter(get_worldcup_matches("results.csv"))

iter_matches = filter(filtering, iter_matches)
#next(iter_matches)  # Skipping the column names

dictionaries = []

for row in iter_matches:
    dictionaries.append({
  "date": row[0],
  "home team": row[1],
  "away team": row[2],
  "home score": row[3],
  "away score": row[4],
  "tournament": row[5],
  "city": row[6],
  "country": row[7],
  "neutral": row[8],
})
    #print(row)



print(dictionaries)

italy_goal_count = 0

for m_dict in dictionaries:
    if(m_dict['home team'] == "Italy"):
        italy_goal_count += int(m_dict['home score'])
    elif(m_dict['away team'] == "Italy"):
        italy_goal_count += int(m_dict['away score'])
        
print(italy_goal_count)