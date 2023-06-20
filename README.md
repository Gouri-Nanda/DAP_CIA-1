# DAP_CIA-1
Data Analytics with Python CIA 1

Gouri Nanda 22112009

Taniya Anil 22112030



Supermarket management system is the system where all aspects related to the management of supermarket are done. These aspects involve managing information about various products, staff managing the product data, staff information, customer information, billing etc. The system provides an efficient way to handle these information. 
This project is based on the product information, customer information and billing in a supermarket. The first menu in the program brings you to the main menu of the program. Here in which you are introduced with various options such as taking into the customers menu, items menu and billing menu as well as an exit option from the program. The first menu will allow us to add, delete, update, search and display product information, while the second menu will allow us to add, delete, update, display and search the customer data. And the third function brings you to the billing menu. 
This project is user friendly and supermarket chains or individual stores are the targeted audience. They could use it to manage the stock, the customer details, the billing details and helps for fraud detection. The data is stored in SQL so that the data is stored permanently in which we can retrieve the as per the admin requirement. 


Function Description:

1.	Product function

•	Add product: The function takes Item code, Item company, Item name, Price of the Item , stocks available of the item and date of purchase as input and add a record to the table in the database.

•	Delete product: The function takes item name as input and searches for the record whose item name is same as the input and delete the record corresponding to it.

•	Update product: The function takes the Item name as input and updates the record corresponding to it in the SQL database.

•	Search product: The function take item code as input and searches the product name in the table and retrieves back the data corresponding to it.

•	Display product: The function displays all the item details as a dataframe.

2. Customer Function
   
•	Add product: The function takes Customer name and Customer score as input. The data will be added to customer score table in the SQL database.

•	Delete product: The function takes customer name as the input and search for the record whose item name is same as the input and delete the record corresponding to it.

•	Update product: The function takes customer name as input and updates the record corresponding to it in the SQL database

•	Search product: The function takes customer name as input and searches the customer name and score in the customer score table and retrieves back the data corresponding to it.

•	Display product: The function displays the customer details as a form of database.


3.Billing Function

The function takes name of the product and quantity of the product purchased as iinput. The function then search for the record of the given input in database and retrieves back the data. This data is then used for calculating the amount and then the final total amount. This function also displays a dataframe consisting of item name, quantity, price and amount by the end and also prints the total amount to be paid.


Intended Users:

• Store Admin

• Product Managers

• End Users


Software Requirements:

• Windows 10 or newer

• Python 3.7 or newer

• MySQL 8.0 or newer

• Pandas python library

• MySQL Connector python library


Program Execution
When we run the program we're met with the Main Menu. From here we can choose the menu that we want to go to.

![sm 1](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/12d4ff41-c168-415e-9def-fe9f58cfa2d7)


If we choose the option 1, we enter into the items menu. Here we can add, update, delete, search adn display all the products.

![sm2](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/f59177a7-e8ec-4599-8bc8-cc6ba94bcd82)
![Screenshot 2023-06-20 200125](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/98370e40-809c-4f52-82b1-58eb29766b48)
![Screenshot 2023-06-20 200227](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/6dd2de77-6bad-4b51-b89a-82f804ce506f)
![Screenshot 2023-06-20 200318](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/0b7eb055-e246-4032-9ab0-0ddaca54fd5a)
![Screenshot 2023-06-20 200351](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/0dcd0eef-fc0d-403a-9331-c178a19dd888)
![WhatsApp Image 2023-06-20 at 20 06 23](https://github.com/Gouri-Nanda/DAP_CIA-1/assets/118895540/04e72eac-a840-48de-a7d0-c38ec565b080)








If we choose the option 2, we enter into the items menu. Here we can add, update, delete, search adn display all the customer data.




If we choose the option 3, we enter into the billing menu.




If we choose 0, then we exit from the main programme.


Business Application

The intended market consists of supermarket chains and independent retailers.They might use it to run their network of stores, keep accurate records, examine sales data, and boost profits. It would be convenient to sync all the data across many stores in various places since everything is online. This project aims in making these processes easier and provide a user friendly programme.
