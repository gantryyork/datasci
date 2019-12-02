#!/usr/bin/python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

def main():

    docs = [
        {'a':'11', 'b':['77','88'], 'c':['12']},
        {'a':'22', 'b':['99','00'], 'c':['31','32','41']},
    ]

    pp.pprint(docs)
    docs = expand_lists(docs)
    docs = expand_lists(docs)

    pp.pprint(docs)


def expand_lists(docs):

    new_docs = list()
    for doc in docs:
        new_doc = dict()

        if doc_contains_lists(doc):
            print('need to expand')
            new_docs = new_docs + expand_doc(doc)
        else:
            print('no expansion')
            new_docs = new_docs + doc

    return new_docs


def expand_doc(doc):

    k_list = find_first_list(doc)

    new_docs = list()

    base_doc = dict()
    for k in doc.keys():
        if k != k_list:
            base_doc.update({k : doc[k]})

    for v in doc[k_list]:
        new_doc = dict()
        new_doc.update( base_doc )
        new_doc.update({k_list : v})
        new_docs.append(new_doc)

    return new_docs


def doc_contains_lists(doc):

    for k in doc.keys():
        if type(doc[k]) == list:
            return True

    return False


def find_first_list(doc):

    for k in doc.keys():
        if type(doc[k]) == list:
            return k

    return None



if __name__ == '__main__':
    main()
