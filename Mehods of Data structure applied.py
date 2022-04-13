    # FOR LIST

# l1 = ["a","b","c","a"]
# #     append(add value at last just using the value)
# l1.append(d)
# print(l1)


# #     clear(clear the list)
# l1.clear()
# print(l1)


# #     copy(copy vaue and shows it in '' this mode)
# x = l1.copy()
# print(l1)


# #      index(provide us with the value of index number)
# x = l1.index("a")
# print(x)


# #      extend(add another list at last of first list)
# l2 = [ "Bhavin"]
# l1.extend(l2)
# print(l1)


# #       sort(sort in ascending order)
# my_list = ["abc","cba","bca"]
# my_list.sort()
# print(my_list)


# #       pop(remove value using its index value)
# x = l1.pop(1)
# print(l1)


# #        remove(remove specified value)
# l1.remove("b")
# print(l1)


# #     count(count how many times valuse repeated)
# x = l1.count("a")
# print(x)


# #    revese (reverse the order)
# l1.reverse()
# print(l1)


# #       insert(position,value)
# l1.insert(2,"Katara")
# print(l1)



    # FOR DICTIONARY

d1 = {
    "Anime" : "Naruto",
    "Release_Year" :"2002",
    "Episode"  : "220"
 }    

# d1.clear()
# print(d1)



# d1.copy
# print(d1)



# x = ( "a" , "b", "c")
# y = ("d")
# d2 = dict.fromkeys(x,y)
# print(d2)


# x = d1.get("Episode")
# print(x)

# x = d1.items()
# print(x)


# d1.pop("Anime")
# print(d1)


# x = d1.keys()
# print(x)


# x = d1.values()
# print(x)


# d1.update({"Side Character ": "Sasuke"})
# print(d1)

# x = d1.setdefault("Episode","720")
# print(x)


# removes last entry
# d1.popitem()
# print(d1)

    # FOR TUPLES


t1 = ("11", "21","232","321","21")

# x = t1.count("21")
# print(x)   

# x =  t1.index("232")
# print(x)




#            FOR SETS


s1 =  {"Naruto" ,"One Piece", "Death Note", "Haikyuu"}
s2 =  {"Movies ", "Anime" , "Web Series","Haikyuu"}
s0 = {"Naruto","Kuroko's Basketball"}


# add the valuejust like append
# s1.add("Black Clover")
# print(s1)



# this method will not show common value
# s3 = s2.difference(s1)
# print(s3)

#clear all the set
# s2.clear()
# print(s2)


# copy the given set
# s3 = s2.copy()
# print(s3)

#show the calue whic is diff which is mentioned first
# s3 = s1.difference_update(s2)
# print(s1)


#will not consider the mentioned value
# s1.discard("Naruto")
# print(s1)

#  intersecton of s1 and s2 or s2 and s1

# s3 =  s2.intersection(s1)
# print(s3)


# s1.intersection_update(s2)
# print(s1)
# s2.intersection_update(s1)
# print(s2)



# s3 = s2.isdisjoint(s1)
# print(s3)


# s3 = s0.issubset(s1)
# print(s3)


# s3 = s1.issuperset(s0)
# print(s3)


## Removes a random value take no argument
# s1.pop()
# print(s1)

#  remove the value which is mentioned
# s1.remove("One Piece")
# print(s1)

# Union of both set except common value
# s3 = s1.symmetric_difference(s2)
# print(s3)



# s1.symmetric_difference_update(s2)
# print(s1)


# s3 = s1.union(s2)
# print(s3)




# s1.update(s0)
# print(s1)
