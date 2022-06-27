

   # Problem Statement
   
    A Data Analytics manager need an transform function to be built for him .where that function will be able to extract the data from sources 
    in different format may be (.csv,.tsv,.xml,json) it may have any format but has to convert those data into an user defined data structure into a dictionary
    with {'key'& 'val'} structure and put it into a list   
 

 #  Directory 
 
   1. main.py :-  Pulling the data from the github sources and pass the data in the data_handler function from data.py Module . the returned list has been converted into                       pickle objects.
   

   2. data.py  :- This function pulls the data and then process the json data and make an user defined dictionary with {'key':column name , 'val': values} and                           appending it into the user defined list and returning back to the main.py .logger has been used to catch the exception.






# Note:
  Requests module has been used to scrape the data from the respective github url
  
  More reference on requests:- https://www.w3schools.com/python/module_requests.asp
  
  

    



















