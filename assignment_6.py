dict_list=l=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

#select unique element from each dictionary name in this case to create a unique dictionary 
updated_list =dict((k["name"],k) for k in dict_list).values()
print(list(updated_list))