# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


#create a list of all courses in a given hexamester

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# when_offered(courses, course) takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    c = courses.keys()
    b = []
    n = len(courses)
    i = 0
    while i < n:         
        if course in courses[str(c[i])]:       #look for course that is in courses, have to add str(), because when printed from in list c it was not a strign 
            b.append(str(c[i]))               #add all hexamesters/dates in list b
        i = i + 1
    return b     #list of hexamesters when the input course is offered


print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']

print when_offered(courses, 'bio893')
#>>> []



# is_offered(courses, course, hexamester) returns 
# True if the input course is offered in the input hexamester, and returns 
# False otherwise.  For example,

def is_offered(courses, course, hexamester):
    if course in courses[hexamester]:  #see if the course is offered in the hexamester
        return True
    else:
        return False


print(is_offered(courses, 'cs101', 'apr2012'))
#>>> True

print(is_offered(courses, 'cs003', 'apr2012'))
#>>> False

print(is_offered(courses, 'cs001', 'jan2044'))
#>>> True

print(is_offered(courses, 'cs253', 'feb2012'))
#>>> False




# involved(courses, person) takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester.

def involved(courses, person):
    d = {}
    for hexamester in courses:                         #go through each hexamester
        for course in courses[hexamester]:             #go through each course              
            g = courses[hexamester][course]
            if "teacher" in g:                         #see if key "teacher" is in specific course
                if g["teacher"] == person:             #if the person is the value of a key "teacher" in specific course 
                    if hexamester not in d:            #see if hexamester is not already in d, if not then you add it to and define its value as offered
                        offered = []
                        d[hexamester] = offered
                        offered.append(course)
                    else:
                        offered.append(course)
            if "assistant" in g:         #check for each class if it has available asistant
                if g["assistant"] == person: 
                    if hexamester not in d:     #if hexamester is not yet in dictionary, add it with a list of courses
                        offered = []            
                        d[hexamester] = offered
                        offered.append(course)      
                    else:
                        offered.append(course)
    return d     #dictionary that describes all the courses the person is involved in

# For example:

print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

print involved(courses,'Peter')
#>>> {}

print involved(courses,'Robotic')
#>>> {}

print involved(courses, '')
#>>> {}

