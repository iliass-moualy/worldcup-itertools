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

    
    """ 
    for row in worldcup_matches[:5]:
    # parsing each column of a row
        for col in row:
            print("%10s"%col),
        print('\n')
    """

if __name__ == "__main__":
    main_func()