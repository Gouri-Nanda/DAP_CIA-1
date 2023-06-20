# DAP_CIA-1
Data Analytics with Python CIA 1

Supermarket management system is the system where all aspects related to the management of supermarket are done. These aspects involve managing information about various products, staff managing the product data, staff information, customer information, billing etc. The system provides an efficient way to handle these information. 
This project is based on the product information, customer information and billing in a supermarket. The first menu in the program brings you to the main menu of the program. Here in which you are introduced with various options such as taking into the customers menu, items menu and billing menu as well as an exit option from the program. The first menu will allow us to add, delete, update, search and display product information, while the second menu will allow us to add, delete, update, display and search the customer data. And the third function brings you to the billing menu. 
This project is user friendly and supermarket chains or individual stores are the targeted audience. They could use it to manage the stock, the customer details, the billing details and helps for fraud detection. The data is stored in SQL so that the data is stored permanently in which we can retrieve the as per the admin requirement. 
Function Description:
1.	Product function
•	Add product: The function takes Item code, Item company, Item name, Price of the Item , stocks available of the item and date of purchase as parameters and add a record to the table in the database. 
•	Delete product: The function takes item name as input parameter and searches for the record whose item name is same as the input and deleted the record corresponding to it.
•	Update product: The function take the Item name as input parameter and updates the record corresponding to it in the SQL database.
•	Search product: The function take item code as input arguement and searches the product name in the table and retrieves back the data corresponding to it
•	Display product: The function displays all the item details as a dataframe.
2. Customer Function

