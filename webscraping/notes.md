* [https://www.youtube.com/watch?v=BZu8jhY5V70&feature=youtu.be
* [https://hackernoon.com/mastering-python-web-scraping-get-your-data-back-e9a5cc653d88
* http://html.python-requests.org/en/latest/
* https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
https://towardsdatascience.com/data-analytics-with-python-by-web-scraping-illustration-with-cia-world-factbook-abbdaa687a84
* https://realpython.com/blog/python/modern-web-automation-with-python-and-selenium/

* https://www.kdnuggets.com/2017/12/baesens-web-scraping-data-science-python.html

* https://www.kdnuggets.com/2017/12/baesens-web-scraping-data-science-python.html

* https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/

* https://towardsdatascience.com/web-scraping-basics-selenium-and-beautiful-soup-applied-to-searching-for-campsite-availability-4a8de1decac9

* https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

* https://github.com/sdiehl/pycraig

* http://stevenwu.info/blog_posts/cfl-part1-bs4-selenium/

# Selva
 
from bs4 import BeautifulSoup
import requests
 
""" Python Program to get all students grades with CGPA.
 Note: Install BeautifulSoup Module and Requests Module
 before running this program!!!"""
 
csv_file = open("CGPA_Provided_by_Selva.csv","w")
# This is example Reg. No. College code is fake :P
reg_start = 123417103001 # Enter starting Reg. number
reg_end = 123417103027 # Ending Reg. number
# Found the Database URL after a long time. :) 
url = "http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl?regno="
 
def write_csv(list1):
 # Function to write in CSV
 for word in list1:
 csv_file.write(str(word)+",")
 csv_file.write("\n")
# Write the Table Titles
write_csv(['Name','Phy Lab','Chemistry','Python','EG','Py Lab','English','Maths','Physics','CGPA'])
 
def calculate_cgpa(mylist):
 # CGPA Calculator Algorithm
 # Took hours to make :P
 points = [0, 2, 3, 3, 4, 2, 4, 4, 3]
 credit = {"O": 10, "A+": 9, "A": 8, 'B+': 7, 'B': 6}
 total_credits = 0
 my_credits = 0
 for i in range(1, 9):
 if credit.__contains__(mylist[i]):
 my_credits = my_credits + (credit[mylist[i]] * points[i])
 total_credits = total_credits + (points[i] * 10)
 try:
 cgpa = my_credits / total_credits * 10
 except ZeroDivisionError:
	# Occurs when someone is absent in all subjects.
 return 0
 return round(cgpa, 2)
 
for i in range(reg_start,reg_end+1):
 data_list = []
 soup = requests.get(url+str(i))
 # Idk what to name the variable :P
 selva = BeautifulSoup(soup.text,"html.parser")
 td = selva.find_all("td")
 tables = td[1].find_all("table")
 strongs = tables[0].find_all("strong")
 table_2 = tables[1].find_all("strong")
 no = 4
 name = strongs[1].string
 data_list.append(name)
 # Print progress with name
 print("Completed for "+name)
 while no < len(table_2):
 print(table_2[no].string)
 data_list.append(table_2[no].string)
 no = no + 3
 data_list.append(calculate_cgpa(data_list))
 write_csv(data_list)
 
csv_file.close()

https://www.pluralsight.com/guides/python/web-scraping-with-python?gclid=Cj0KCQjw8MvWBRC8ARIsAOFSVBXRPNwKti4vAFSmueoagrk_PKg0kfm_hPAEJ0ItwbyJBtCHnUfQ1aoaAnrMEALw_wcB&aid=7010a000002BWq6AAG&promo=&oid=&utm_source=non_branded&utm_medium=digital_paid_search_google&utm_campaign=APAC_Dynamic&utm_content=&s_kwcid=AL!5668!3!247592797107!b!!g!!&ef_id=WlopWQAAA4CS_2O4:20180415191617:s

* https://www.kdnuggets.com/2018/02/web-scraping-tutorial-python.html

*http://www.techbeamers.com/selenium-webdriver-python-tutorial/
