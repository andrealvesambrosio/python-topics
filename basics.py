
# %% Lists Overall

# range end is not include
a_list = list(range(10)) # 0-9
 

# append keep structure
a_list.append(137) 
#a_list.append([747, 190])

# use extend when you need append multiple values (without keeping structure)
#a_list.extend([199, 299])
a_list.extend((888, 777, 199, 199))

# insert value in specific position
a_list.insert(2, 888) # high cost comparing with append

# remove and return value from specific position
a_list.pop(5)

# remove first value requested (only the first)
a_list.remove(888) 
# a_list.remove(78787) # error if dont exists


# in, not in
888 in a_list
8787 not in a_list

# concat lists
list_of_lists = list([a_list, a_list])
everything = []
for chunk in list_of_lists:
    everything.extend(chunk)  # better then list1 + list2

# Sort values
a_list.sort()
a_list.sort(key = len)

# slicing
b = list(range(10))


b[3:4] # begin is include, end is not include. (len = end - begin)
b[1:7]   # 1-6
b[-6:-2] # 4-7
b[1:-1]  # 1-8

# %% Functions for sequences 

# enumerate to use in cases like above (omit the i++ row)
some_list = ['foo', 'bar', 'baz'] 
mapping = {} 
i = 0
for v in some_list: 
    mapping[v] = i 
    i = i+1
mapping 

some_list = ['foo', 'bar', 'baz'] 
mapping = {} 
for i, v in enumerate(some_list): 
    mapping[v] = i 
mapping 

# reversed (inverse ordem to iterating)
list(reversed(range(10)))

# dict (key: value)
my_dict = {}
my_dict[5] = 'value'
my_dict['key'] = [1, 77]

del my_dict[5]

dict_2 = {'key2' : 22}

my_dict.update(dict_2)

# dict.get
if 'key2' in my_dict: 
    value = my_dict['key2'] 
else: 
    value = 7878
    

value = my_dict.get('key2', 777) 

# dict.setdefault
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words: 
    letter = word[0] 
    by_letter.setdefault(letter, 
                         []).append(word)
by_letter



# %% List, set, dict comprehensions
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

[x.upper() for x in strings if len(x) > 2]

unique_lengths = {len(x) for x in strings}
set(map(len, strings))

loc_mapping = {val : index for index, val in enumerate(strings)}

# 
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

names_of_interest = [] 
for names in all_data: 
    enough_es = [name for name in names if name.count('e') >= 2] 
    names_of_interest.extend(enough_es)
    
result = [name for names in all_data for name in names
          if name.count('e') >= 2]

# 
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

flattened = [] 
for tup in some_tuples: 
    for x in tup: 
        flattened.append(x)


flattened = [x for tup in some_tuples for x in tup]


# %% Functions as objects
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 
          'south carolina##', 'West virginia?']

import re
def remove_punctuation(value): 
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title] 
def clean_strings(strings, ops): 
    result = [] 
    for value in strings: 
        for function in ops: 
            value = function(value) 
        result.append(value) 
    return result 

clean_strings(states, clean_ops)

for x in map(remove_punctuation, states):
    print(x)
    
# %% Lambda functions
lambda_function = lambda x: x * 2

def apply_to_list(some_list, f): 
    return [f(x) for x in some_list]
 
ints = [4, 0, 1, 5, 6] 
apply_to_list(ints, lambda x: x * 2)

# %% Error + Exceptions

# Generally
def attempt_float(x): 
    try: 
        return float(x) 
    except: 
        return x

attempt_float('2')
attempt_float('ss')
attempt_float(['3', '4'])

# Specifies the type
# Generally
def attempt_float(x): 
    try: 
        return float(x) 
    except ValueError: 
        return x
attempt_float(['3', '4']) # Shows TypeError
