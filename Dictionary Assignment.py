'''

#2) x={'A':1,'B':'5'} o/p :{1:'A','5':'B'} interchange the keys and values
x={'A':1,'B':5}
y={}
for i in x.items():
    y[i[1]]=i[0]
print(y)



#3) x= {'1':['a','b'], '2':['c','d']} Expected Output: ['ac','ad','bc','bd']
dic = {'1':['a','b'], '2':['c','d']}
i = 0;
key1 = list(dic.keys())[0]
key2 = list(dic.keys())[1]
for i in range(len(dic[key1])):
    for j in range(len(dic[key2])):
        x=print(dic[key1][i], end = "")
        y=print(dic[key2][j],end= " ")



#4)x='EMBEDDED' o/p : {'E':'3','M':1,'B':1,'D':3}
X = 'EMBEDDED'
my_dict = {}
for letter in X:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)



#5) x={'A':3,'B':5,'C':4,'D':2,'E':1} Arrange keys and values as per ascending order of values  o/p : {'E':1,'D':2,'A':3,'C':4,'B':5}
x={'A':3,'B':5,'C':4,'D':2,'E':1}
sorted_values = sorted(x.values())
sorted_dict = {}
for i in sorted_values:
    for k in x.keys():
        if x[k] == i:
            sorted_dict[k] = x[k]
print(sorted_dict)



#6){'A': 'Red' , 'D': None 'B': 'Green', 'C': None} New Dictionary after dropping empty items  o/p :{'A': 'Red', 'B': 'Green'}
x={'A': 'Red' , 'D': None, 'B': 'Green', 'C': None}
y = {key:value for (key, value) in x.items() if value is not None}
print(y)



#7) x={'A':123,'B':100} check key is exits or not in dic  , key= take key from input use eval fun
x={'A':123,'B':100}
search_key = eval(input("Enter key :"))
if search_key in x:
    print("The key is present.")
else:
    print("The key does not exist in the dictionary.")



#8) x='Hello PYTHON who ARE YOU' o/p : {'H':'HELLO','P':'PYTHON','W':'WHO','A':'ARE','Y':'YOU'}
x='Hello PYTHON WHO ARE YOU'
words=x.split()
d={}
for str in words:
    ch = str[0]
    if ch not in d:
        d[ch]= []
    d[ch].append(str)
print(d)




#9){'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]} reverse the list values in the dictionary: {'C1': [30,20,10], 'C2': [40,30,20], 'C3': [34,12]}
dictionary={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for key in dictionary:
    dictionary[key].reverse()
print(dictionary)




#10){1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}Length of dictionary values: o/p : {'red': 3, 'green': 5, 'black': 5, 'white': 5}
x = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
result = {}
for val in x.values():
    result[val] = len(val)
print(result)

'''
