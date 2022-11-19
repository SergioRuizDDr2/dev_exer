from random import *
import pprint

def run():
    list_generator()

def list_generator():
    """Generate list of dictionary of 10 elements. 
    The age is random number between 1 to 100

    Returns:
        list: list generated and sorted
    """
    data = list_order([{'id':l, 'age':randint(1,100)} for l in range(10)])
    return data

def list_order(data):
    """Receive the list and sorted by age descending.
    Print id of high and low age
    
    Returns:
        list: returned sorted list        
    """   
    ages = sorted(data, key=lambda a:a['age'], reverse=True)
    print("Id mayor: ", max(ages, key=lambda x:x['age']).get('id'))
    print("Id menor: ", min(ages, key=lambda x:x['age']).get('id'))
    return ages

if __name__ == '__main__':
    run()