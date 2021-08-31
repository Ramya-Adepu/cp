"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def sortUSA():
    '''Return all the cities in the USA in alphabetical order'''
    l = locations['North America']['USA']
    l.sort()
    return l

def alphaAsia():
    '''Return all the cities in Asia continent in alphabetical order'''
    s = locations['Asia']
    l = []
    for k,v in s.items():
        for i in v:
            ans = i + " - "+k
            l.append(ans)
    return l

# Note: Check for test cases to understand the output format.
locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia']={'India':['Bangalore']}