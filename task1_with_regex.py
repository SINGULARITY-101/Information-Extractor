import re

my_dict= {
          "account_number":"value 1", 
          "payment":"value2", 
          "balance":"value3", 
          "day":"value4",
          "month":"value5",
          "year":"value6"
          }

month=  {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
        }

#Parsing the message to remove any commas 
message = "LAN12345678 Dear Customers, as per our information you have paid Rs 20,000.00 on 2 October 2020 as loan repayment for your Rs 30,000.00"
message = message.replace(",","")







#Finding Account Number
x = re.search(r"LAN\d{8}", message)
acno_string = x.group()                                                                      #group() is a method of the match obeject and it returns the part of the string where there was a match 
my_dict["account_number"] = "".join(item for item in acno_string if item.isdigit())

print(my_dict)








#Finding Payment
x = re.search(r"Rs\s[0-9.]+", message)
payment_string = x.group()
my_dict["payment"] = "".join(item for item in payment_string if item.isdigit() or item == ".")

print(my_dict)








#Finding Date
x = re.search(r"\d{1,2}\s\w+\s\d{4}", message)
date_string = x.group()

"""
Optional Regular Expression for date
x = re.search(r"[0-9]{1,2}\s[a-zA-z]+\s[0-9]{4}", message)
"""

date_list = date_string.split(" ")
my_dict["day"] = date_list[0]
my_dict["month"] = month[date_list[1]]
my_dict["year"] = date_list[2][2:]

print(my_dict)






#Finding Balance 
x = re.search(r"[0-9.]*$", message)
my_dict["balance"] = x.group()

print(my_dict)








#Printing the final message 

print("Final Message :-")

if ("deposit" in message) or ("loan repayment" in message):
    print("$ACC: {}, {}/{}/{}, {}, {}, DEPOSIT".format(my_dict["account_number"], my_dict["day"], my_dict["month"], my_dict["year"], my_dict["payment"], my_dict["balance"]))

elif ("withdrawal" in message):
   print("$ACC: {}, {}/{}/{}, {}, {}, WITHDRAWAL".format(my_dict["account_number"], my_dict["day"], my_dict["month"], my_dict["year"], my_dict["payment"], my_dict["balance"]))
 











