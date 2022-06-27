

   # Problem Statement
   
   
   
    A Data Analytics manager wants an simple data handling function to create a list of dictionary on the term deposit details of the Applicant Now the dataset cantains the data in json format and its a Nested Json .He relied upon a data engineer who can pull the data from the source and transform the value into dictinary format {'Applicant_ID': val ,'Termdepositstatus': val} and append it into a list.
    

 #  Directory 
 
   1. main.py :-  Pulling the data from the github sources and pass the data in the data_handler function from data.py Module . the returned list has been converted into                       pickle objects.
   

   2. data.py  :- This function pulls the data and then process the json data and make an user defined dictionary with {'key':column name , 'val': values} and                           appending it into the user defined list and returning back to the main.py .logger has been used to catch the exception.






# Note:
  Requests module has been used to scrape the data from the respective github url
  
  More reference on requests:- https://www.w3schools.com/python/module_requests.asp
  
  

    



















