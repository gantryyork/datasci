#!/usr/bin/python3

import pprint
pp = pprint.PrettyPrinter(indent=4)


def main():

    structs = [
        {'a': '11', 'b': ['77', '88']},
        {'a': '22', 'b': ['99', '00']},
        {'a': '33', 'b': [{'x': '1'}, {'y': '2'}]},
    ]

    pp.pprint(structs)
    docs = structs_to_docs(structs)
    print()
    pp.pprint(docs)


def structs_to_docs(structs):

    while structs_contain_lists(structs):
        new_structs = list()
        for struct in structs:
            new_structs = new_structs + expand_struct_by_list(struct)
        structs = new_structs

    docs = structs

    return docs


def structs_contain_lists(structs):

    for struct in structs:
        for k in struct.keys():
            if type(struct[k]) == list:
                return True

    return False


def expand_struct_by_list(struct):

    k_list = find_first_list(struct)

    base_struct = dict()
    for k in struct.keys():
        if k != k_list:
            base_struct.update({k: struct[k]})

    new_structs = list()
    for elem in struct[k_list]:
        new_struct = dict()
        new_struct.update(base_struct)
        new_struct.update({k_list: elem})
        new_structs.append(new_struct)

    return new_structs


def struct_contains_lists(struct):

    for k in struct.keys():
        if type(struct[k]) == list:
            return True

    return False


def find_first_list(doc):

    for k in doc.keys():
        if type(doc[k]) == list:
            return k

    return None


if __name__ == '__main__':
    main()
