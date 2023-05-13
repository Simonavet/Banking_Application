This is a personal project that I made to exercise my coding skills.\
It was created with PyCharm Community Edition 2022.1.3 in Python programming language. If you want to see how it works you have to:
1.	Download PyCharm Community Edition 2022.1.3 from: https://www.jetbrains.com/pycharm/download/#section=windows .
2.	Install PyCharm
3.	Download Python from: https://www.python.org/downloads/ .
4.	Install Python
5.	Clone the project from Git Hub: 
-	make a folder where you want to clone the project
-	make right click and open Git Bash
-	copy the project’s link from Git Hub
-	go in Git Bash write “git clone”, then paste the copied link and tap the “Enter” button
6.	Open the project in PyCharm – open the program – go to File – Open – choose the cloned application
7.	To run the application, you have to go in the python file “operating_system”, click right and choose “Run” – then you have to follow the instructions from the console.

How it was made:\
The code that works the application can be found in python file “functions”. 
1.	I made a class – “Bank_account”
2.	I created a constructor where I established the arguments that I needed to make the application;
3.	I made a method that salutes the user
4.	I established a method that shows the balance query with the name of the account holder, iban, balance – how much money the user has in the account, if the account was activated or not
5.	I created a method that generates a random pin number for every account 
6.	Another method allows the user to activate the account by introducing the pin number
7.	I made a method that allows the user to supply the account
8.	Another method allows the user to pay/withdraw a sum of money and if it is more than the available sum in the account it shows the user that there are insufficient funds.\
All this are called in the file “operating_system” where:
- I instantiated objects as bank accounts “account1” and “account2”
- I called the functions for every object.
