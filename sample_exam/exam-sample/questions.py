'''
The backend for the lecture question asking application.

Each question is assigned an ID number when it is submitted to the app. This ID
can then be used to like and dismiss the question. The numbers are always
positive, but otherwise follow no defined ordering or structure. Questions have
the same ID from when they are submitted till they are dismissed.

When questions are first submitted, they have 0 likes.
'''

# Put any global variables your implementation needs here

initial_object = {
    'questions': []
}

class Datastore:
    def __init__(self):
        self.__store = initial_object

    def get(self):
        return self.__store

    def set(self, store):
        if not isinstance(store, dict):
            raise TypeError('store must be of type dictionary')
        self.__store = store

global data_store
data_store = Datastore()

def submit(question):
    '''
    Submits a question to the service.

    Returns the ID of the question but yields a ValueError if question is an
    empty string or exceeds 280 characters in length.

    '''

    data = data_store.get()

    if len(question) == 0:
        raise ValueError("Question is an empty string.")

    if len(question) > 280:
        raise ValueError("Exceeds 280 characters in length.")

    id = len(data['questions']) + 1 

    q = {
        'id': id,
        'question': question,
        'likes': 0
    }

    data['questions'].append(q)

    return q['id']



def questions():
    '''
    Returns a list of all the questions.

    Each question is represented as a dictionary of {id, question, likes}.

    The list is in order of likes, with the most liked questions first. When
    questions have the same number of "likes", their order is not defined.

    '''
    # Hint: For this question, there are still marks available if the returned
    # list is in the wrong order, so do not focus on that initially.

    data = data_store.get() 

    #This should return a sorted list 
    list_of_questions = sorted(data['questions'], key = lambda i: i['likes'], reverse = True)
    data['questions'] = list_of_questions

    return data['questions']



    

def clear():
    '''
    Removes all questions from the service.
    '''
    data = data_store.get()

    data['questions'] = []

    data_store.set(data)

def like(id):
    '''
    Adds one "like" to the question with the given id.

    It does not return anything but raises a KeyError if id is not a valid
    question ID.
    '''

    data = data_store.get()

    for question in data['questions']:
        if question['id'] == id:
            question['likes'] += 1
            return 

    return KeyError("Not a valid question ID")
    



def dismiss(id):
    '''
    Removes the question from the set of questions being stored.

    It does not return anything but raises a KeyError if id is not a valid
    question ID.
    '''

    data = data_store.get()

    for question in data['questions']:
        if question['id'] == id:
            data['questions'].remove(question)


if __name__ == "__main__":
    q1 = submit("How long is a piece of string?")
    q2 = submit("What's your shoe size?")
    like(q1)
    print(questions()) 
     
