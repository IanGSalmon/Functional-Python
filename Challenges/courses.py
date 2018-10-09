courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}

# Finish the prereqs function so that it recursively finds all prereq courses in courses
# eg. 'Object-Oriented Python' is prereq for 'Django Basics'
# You should add() the title for the prereq to the pres set, then call prereqs again with child courses
# In the end, return the prereqs set

def prereqs(data, pres=None):
    pres = pres or set()
    # for each prereq in this courses' prereqs
    for prereq in data['prereqs']:
        # add title of this prereq course
        pres.add(prereq['title'])
        # use recursive call to find further prerequisites of this
        # course, if any
        prereqs(prereq, pres)
    # return current
    return pres

prereqs(courses)