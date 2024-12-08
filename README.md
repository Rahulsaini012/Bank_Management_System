## 💰 Bank Management System

A secure and user-friendly desktop application for managing bank accounts using Python (Tkinter) and MySQL. Users can create accounts, log in, manage transactions, and delete accounts with a clean interface and responsive notifications.



## 📋 Features

✅ Create Account: Unique account number generation and secure storage.

✅ Login System: Authentication using username and account number.

✅ Transactions: Securely credit and debit funds.

✅ Account Management: Delete accounts with confirmation prompts.


## 🖥️ Tech Stack

Programming Language: Python

GUI Framework: Tkinter

Database: MySQL (pymysql library)

## 🚀 Getting Started


                    1. Clone the Repository
                    
                    git clone https://github.com/your-username/bank-management-system.git
                    
                    cd bank-management-system

                    
                    2. Install Dependencies
                    
                    pip install pymysql
                    
                    
                    
                    3. Database Setup
                    
                    Create the Database:
                    
                    sql
                    
                    CREATE DATABASE bank_management;
                    
                    Create the Table:
                    
                    sql
                    
                    USE bank_management;
                    
                    CREATE TABLE customers (
                    
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        
                        account_number VARCHAR(20) UNIQUE,
                        
                        username VARCHAR(100),
                        
                        contact_no VARCHAR(15),
                        
                        amount FLOAT,
                        
                        city VARCHAR(100),
                        
                        state VARCHAR(100)
                    );
                    
                    Update the Database Credentials:
                    
                    Open the Python file and replace PASSWORD with your actual MySQL password:
                    
                    password="YOUR_DATABASE_PASSWORD"
                    
                    
                    
                    4. Run the Application
                
                    python bank_management_system.py





## 📁 Project Structure

📂 bank-management-system  

 ├── bank_management_system.py   # Main Application File  
 
 ├── README.md                   # Project Documentation  
 
 └── requirements.txt            # Required Dependencies  
## 💡Future Enhancements

📊 Transaction History: Add a full transaction log for accounts.

🔐 Secure Login: Implement password hashing and OTP-based login.

🌐 Web Version: Convert the application into a web-based service using Flask or Django.


## 🤝 Contributing

Contributions are welcome! Fork this repository, create a new branch, and submit a pull request.


## 📬 Contact

For inquiries or issues, contact me:


Email:pb65rahulsaini@gmail.com


Linkedin: https://www.linkedin.com/in/rahul-saini-2b4b33337/

## 📄 License

This project is Open Source. Use and modify it for personal or educational purposes.



