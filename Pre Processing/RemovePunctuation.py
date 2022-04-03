 def rem_punct(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 
  
input_str = "Hey, How are you??? I am fine!!!!" 
rem_punct(input_str)   # OUTPUT:- 'Hey How are you I am fine'
