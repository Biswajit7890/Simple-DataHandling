
  # Overview 

  To retieve a data from the sources and do simple data conversion to any data structure.
  
  # Problem Statement
  
  1. Convert simple data handling problems to code-based solutions 
  2. Write modular code that generates logs


 #  Directory 
 
   1. main.py :-  Pulling the data from the github sources and pass the data in the data_handler function from data.py Module . the returned list has been converted into                       pickle objects.
   

   2. data.py  :- This function pulls the data and then process the json data and make an user defined dictionary with {'key':column name , 'val': values} and                           appending it into the user defined list and returning back to the main.py .logger has been used to catch the exception.






# Note:
  Requests module has been used to scrape the data from the respective github url
  
  More reference on requests:- https://www.w3schools.com/python/module_requests.asp
  
  

    



















