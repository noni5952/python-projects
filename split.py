s= input ("enter a string:")
result =  ""
for ch in s:
    if ch not in result:
        result+=ch 
print ("afterremoving duplicates:",)
