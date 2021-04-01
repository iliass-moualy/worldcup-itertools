import csv
from memory_profiler import profile

@profile
def main_func():

    fields = []
    matches = []

    with open("results.csv", 'r', encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for match in csvreader:
            matches.append(match)

    """      
    for row in matches:
        for col in row:
            print("%10s"%col),
        print('\n')
    """
    
    def filtering(row):
        return row[5] == "FIFA World Cup" #Filters per Wolrd Cup games only

    worldcup_matches = list(filter(filtering, matches))

    dictionaries = []

    for match in worldcup_matches:
        dictionaries.append({
            "date" : match[0],
            "home team" : match[1],
            "away team" : match[2],
            "home score" : match[3],
            "away score" : match[4],
            "tournament" : match[5],
            "city" : match[6],
            "country" : match[7],
            "neutral" : match[8],
        })

    """ 
    for row in worldcup_matches[:5]:
    # parsing each column of a row
        for col in row:
            print("%10s"%col),
        print('\n')
    """

if __name__ == "__main__":
    main_func()