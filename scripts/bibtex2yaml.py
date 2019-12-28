import yaml
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from copy import deepcopy as cp

path_to_input_bibfile = '../_data/papers.bib'
path_to_output_ymlfile = '../_data/papers.yml'

with open(path_to_input_bibfile) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = cp(bib_database.entries)
## sort dictionary according to key
entry_id_pairs = sorted(entries, key=lambda i: i['year'], reverse=True)

entry_types = set([x['ENTRYTYPE'] for x in entries])

entry_id_pairs = []
for e, entry in enumerate(cp(entries)):
    entry_type = entry['ENTRYTYPE']
    entry_id = entry['ID']
    entry.pop('ENTRYTYPE', None)
    entry.pop('ID', None)
    entry_id_pairs.append((e, entry_type, entry_id, entry))

output_dict = dict()
for curr_entry_type in entry_types:

    candicates = []
    for i, entry_type, entry_id, entry in entry_id_pairs:
        if entry_type == curr_entry_type:
            bib_database.entries = [entries[i]]
            entry['bibitem'] = bibtexparser.dumps(bib_database)
            candicates.append(entry)
    output_dict[curr_entry_type] = candicates

print(output_dict)

with open(path_to_output_ymlfile, 'w') as file:
    documents = yaml.dump(output_dict, file)
