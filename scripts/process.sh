python3 scripts/bibparser_collect.py
rm -rf content/publication/*
academic import --bibtex scripts/bibfiles/publications.bib --publication-dir content/publication/