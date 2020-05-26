## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]
#print(max(a_list))

def max(a_list) :
    return "No max value returned"

max_val_test_0 = max(a_list)

## 3. Default Arguments ##

# INITIAL CODE
def open_dataset(file_name = 'AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

## 4. The Official Python Documentation ##

one_decimal = round(3.43 , 1)
two_decimals = round(0.23321 , 2)
five_decimals = round(921.2225227 , 5)

## 5. Multiple Return Statements ##

# INITIAL CODE
def open_dataset(header , file_name='AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header :
        return data[1:]
    
    return data

apps_data = open_dataset(True)

## 6. Returning Multiple Variables ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0] , data[1:]
    else:
        return data
    
    
all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
apps_data , header = open_dataset()