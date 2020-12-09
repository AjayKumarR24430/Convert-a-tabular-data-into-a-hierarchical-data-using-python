import csv
from collections import defaultdict
import pandas as pd 
import json
  
# Read and store content 
# of an excel file  
import excel2json

excel2json.convert_from_file('hierarchy_case_20May2020.xlsx')
read_file = pd.read_excel("hierarchy_case_20May2020.xlsx") 

  
# Write the dataframe object 
# into csv file 
read_file.to_csv ("Test.csv",  
                  index = None, 
                  header=True)


def ctree():
    """  have dynamic tree structure.

    """
    return defaultdict(ctree)


def build_leaf(name, leaf):
    """ Recursive function to build desired custom tree structure

    """
    res = {"name": name }

    # add children node if the leaf actually has any children
    if len(leaf.keys()) > 0:
        res["reportees"] = [build_leaf(k, v) for k, v in leaf.items()]

    return res


def main():
    tree = ctree()
    with open('Test.csv') as csvfile:
        reader = csv.reader(csvfile)
        for rid, row in enumerate(reader):
            ## ignore header
            if rid == 0:
                continue

            # usage of python magic to construct dynamic tree structure and
            # basically grouping csv values under their parents
            leaf = tree[row[0]]
            for cid in range(1, len(row)):
                leaf = leaf[row[cid]]

    # building a custom tree structure
    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf))

    # printing results into the terminal
    import json
    #print(json.dumps(res))

    with open('jsonval.json', 'w') as outfile:
        json.dump(res, outfile)


# so let's roll
main()