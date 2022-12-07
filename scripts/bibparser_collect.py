#!/usr/bin/env python3

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import os

complete_entries = []
all_bibs = ['scripts/bibfiles/conf-papers.bib', 'scripts/bibfiles/articles.bib', 'scripts/bibfiles/journal-issues.bib', 'scripts/bibfiles/reports.bib', 'scripts/bibfiles/theses.bib']

for filename in all_bibs:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    with open(filename, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    filename = os.path.basename(filename)
    print(filename)
    entries = bib_database.entries


    for entry in entries:
        if(filename == 'conf-papers.bib'):
            entry['category'] = 'Conference'
        if(filename == 'theses.bib'):
            entry['category'] = 'Thesis'
        elif(filename == 'articles.bib' or filename == 'journal-issues.bib'):
            entry['category'] = 'Journal'
        elif(filename == 'reports.bib'):
            entry['category'] = 'Report'
        else:
            print("Unknown filename!")
            break

    complete_entries.extend(entries)

output_entries = []
for entry in complete_entries:
    if int(entry['year']) >= 2017:
        output_entries.append(entry)

db = BibDatabase()
db.entries = output_entries

writer = BibTexWriter()
writer.order_entries_by = ('author')



with open('scripts/bibfiles/publications.bib', 'w', encoding='utf-8') as bibfile:
    bibtexparser.dump(db, bibfile, writer)