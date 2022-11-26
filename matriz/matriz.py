import numpy as np
import pprint


def run():
    generate_array()

def generate_array():
    array = np.random.randint(5, size=(5, 5)) 
    """ array = np.array([
        [1, 6, 3, 4, 8],#4
        [1, 2, 9, 10, 5],#9
        [8, 1, 2, 9, 4],#14
        [4, 2, 3, 8, 5],#19
        [8, 3, 6, 7, 6]#24
    ]) """
    print(array,"array\n")
    check = get_sequence(array)
    if check:
        location = [l[0] for l in check]
        print("start: ",location[0],"end: ",location[len(location)-1])
    else:
        print("N/A")
    
def get_sequence(array):
    """execute logic to search sequence

    Args:
        array (array np): receive array np

    Returns:
        list: list of locations
    """
    data_array = get_index(array)
    data_sequence = find_sequence(data_array)
    if not len(data_sequence) == 4:
        data_sequence = find_sequence(
            array_transposed(data_array)
        )
    return data_sequence

def array_transposed(data_array):
    """generate transpose of array

    Args:
        data_array (list): list with indexes

    Returns:
        list: array transposed
    """
    dre= np.array(data_array)
    data1 = []
    for l,a in zip(
            dre.T.tolist()[0],
            dre.T.tolist()[1]
    ):
        data = []
        for e,r in zip(l,a):
            data.append([e,r])
        data1.append(data)
    return data1
     
def find_sequence(data_array):
    """search sequence in vertical or horizontal side 

    Args:
        data_array (list): list with indexes

    Returns:
        list: list of locations
    """
    data = []
    n=0
    for l in data_array:
        if len(data) >= 3:
            break
        while n <= 3:
            if len(data) >= 3:
                break
            if abs(l[n+1][1] - l[n][1]) != 1:
                data.clear()
            elif abs(l[n+1][1] - l[n][1]) == 1:           
                data.append(l[n])
                if len(data) == 3:
                    data.append(l[n+1])
            n+=1
        
        if (abs(len(data)-1) != 
                abs(sum(np.diff([l[1] for l in data])))
                ) or len(data)!=4:
            data.clear()
        n=0
    return data

def get_index(array):
    """return list with indexes

    Args:
        array (array np): receive array

    Returns:
        list: list with indexes
    """
    n=0
    data1 = []
    list_array = array.tolist()
    for l in list_array:
        data = []
        for ll in l:
            data.append([n,ll])
            n+=1
        data1.append(data)
    return data1

if __name__ == '__main__':
    run()