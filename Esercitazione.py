import csv



def get_worldcup_matches(csv_filename):
    with open(csv_filename, "r", encoding="utf8") as match_records:
        for match_record in csv.reader(match_records):
            yield match_record

def filtering(row):
    return row[5] == "FIFA World Cup" #Filters per Wolrd CUp games only


iter_matches = iter(get_worldcup_matches("results.csv"))

iter_matches = filter(filtering, iter_matches)
#next(iter_matches)  # Skipping the column names


for row in iter_matches:
    print(row)