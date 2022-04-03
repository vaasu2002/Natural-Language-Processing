# NLP PRE PROCESSING

```ruby
a.upper()
a.lower()
```
```ruby
def lowercase_text(text): 
    return text.lower() 
  
input_str = "SoMe WorDS."
lowercase_text(input_str) 
```

```ruby
# For Removing numbers 
def remove_num(text): 
    result = re.sub(r'\d+', '', text) 
    return result 
  
input_str = "You bought 6 candies from shop, and 4 candies are in home."
remove_num(input_s) 
```
