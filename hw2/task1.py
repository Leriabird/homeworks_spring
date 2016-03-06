class_n = int(input())
temp_inheritance_lst = [input().split() for i in range(class_n)]
inheritance_dict = {elt[0]: elt[2:len(elt)] for elt in temp_inheritance_lst}
query_n = int(input())
query_lst = [input().split() for i in range(query_n)]
#query_dict = {char[1]: char[0] for char in temp_query_lst}

def isancestor(p, c):
    if c == p:
        return 'Yes'
    elif inheritance_dict[c] == None:
        return 'No'
    elif parent in inheritance_dict[c]:
        return 'Yes'
    else:
        for elt in inheritance_dict[c]:
            if isancestor(p, elt) == 'Yes':
                return 'Yes'
    return "No"

for elt in query_lst:
    parent, child = elt
    print(isancestor(parent, child))