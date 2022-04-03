# import the library 
import inflect 
q = inflect.engine() 
  
# convert number into text 
def convert_num(text): 
    temp_string = text.split()  # split strings into list of texts 
    new_str = [] # initialise empty list 
  
    for word in temp_string: 
        '''if text is a digit, convert the digit 
           to numbers and append into the new_str list''' 
        if word.isdigit(): 
            temp = q.number_to_words(word) 
            new_str.append(temp) 
        else: 
            new_str.append(word) # append the texts as it is 
  
    temp_str = ' '.join(new_str) # join the texts of new_str to form a string 
    return temp_str 
  
input_str = '34 45'    # OUTPUT:- 'thirty-four forty-five'
convert_num(input_str)
