import itertools

Entities_list=["kolkata", "delhi"]
utterance_list=["How far is <> from <>", "How is the weather in <> "]


for string in utterance_list:
    no_of_blanks= string.count("<>")
    for subset in itertools.permutations(Entities_list, no_of_blanks):
        duplicate_string= string[:] 
        for i in range(no_of_blanks):
            duplicate_string=duplicate_string.replace("<>",subset[i],1)
        print(duplicate_string)