from pybtex.database.input import bibtex
import csv

# open a bibtex file
parser = bibtex.Parser()
# change Lib.bib to your target filename
bibdata = parser.parse_file("Lib.bib")

data_list = [
        ["Title", "Year", "Authors"]
    ]

# loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    entry = []
    
    try:
        entry.append(b["title"])
        entry.append(b["year"])

        # deal with multiple authors
        authors = []
        for author in bibdata.entries[bib_id].persons["author"]:
            first_names = ' '.join(author.first_names)
            last_names = ' '.join(author.last_names)
            full_name = first_names + ' ' + last_names
            authors.append(full_name)
        
        entry.append(', '.join(authors))
        data_list.append(entry)

    # field may not exist for a reference
    except(KeyError):
        print("error")
        continue

# save data_list to a csv file called data_export.csv
with open('data_export.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerows(data_list)