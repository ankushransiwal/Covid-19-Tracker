from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib
from email.message import EmailMessage

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/bin/chromedriver.exe")

    def get_data(self):
        #try:
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., 'USA')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        active_cases = data[5]
        total_recovered = data[6]
        serious_critical = data[7]

        #total_cases = row.find_element_by_class_name('sorting_1')
        #new_cases = row.find_element_by_xpath("//td[3]")
        #total_deaths = row.find_element_by_xpath("//td[4]")
        #new_deaths = row.find_element_by_xpath("//td[5]")
        #active_cases = row.find_element_by_xpath("//td[6]")
        #total_recovered = row.find_element_by_xpath("//td[7]")
        #serious_critical = row.find_element_by_xpath("//td[8]")
        print("Country: " + country_element.text)
        print("Total cases: " + total_cases)
        print("New cases: " + new_cases)
        print("Total deaths: " + total_deaths)
        print("New deaths: " + new_deaths)
        print("Active cases: " + active_cases)
        print("Total recovered: " + total_recovered)
        print("Serious, critical cases: " + serious_critical)

        send_mail(country_element.text, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical)

        self.driver.close()
        #except:
        self.driver.quit()

def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    server.login('ankushransiwal.13@gmail.com', 'dibzvlfqwxouxraa')
    msg = EmailMessage()
    msg['Subject'] = 'Coronavirus stats in your country today!'
    msg['From'] = 'ankushransiwal.13@gmail.com'
    msg['To'] = 'abhirocz345@gmail.com'
    msg.set_content('Today in ' + country_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases +'\
        \nNew cases: ' + new_cases + '\
        \nTotal deaths: ' + total_deaths + '\
        \nNew deaths: ' + new_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nSerious, critical cases: ' + serious_critical  + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/')
    html1= """\
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"> 
    <head> <title></title> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style type="text/css"> /* ----- Custom Font Import ----- */ @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700;800&family=Raleway:wght@300;800;900&display=swap');
    body{ margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; -webkit-font-smoothing: antialiased; -moz-font-smoothing: antialiased; font-smoothing: antialiased;}.main{font-family: 'Poppins', sans-serif; font-weight: 300; display: inline-flex; color: #3D2D4B; font-size: 13px;}.container-inner{width: 75%;}.icon{width: 18px; height: 18px;}.daily{font-family: 'Raleway', sans-serif; font-weight: 300; display: inline-flex; font-size: 12px;}.right{text-align: right;}@media only screen and (max-width: 800px){/* ----- Base styles ----- */ .container-full{width: 80% !important;}.container-inner{width: 80%;}}@media only screen and (max-width: 600px){/* ----- Base styles ----- */ .container-full{width: 85% !important;}.container-inner{width: 90%;}.icon{width: 14px; height: 14px;}.daily{font-size: 10px;}.main{font-size: 11px;}}@media only screen and (max-width: 450px){/* ----- Base styles ----- */ .icon{width: 12px; height: 12px;}.daily{font-size: 8px;}.main{font-size: 9px;}}</style> </head> <body style="background-color:#F8D4D4;"> 
    <div class="container-full" style="background-color: #FCFCFC; width: 700px; margin: auto;"> <div class="container-inner" style=" margin: auto; padding-top: 15px; padding-bottom: 15px;"> <div class="row"> <div class="col daily" style="width: 49%;"><img class="icon" src="https://lh3.googleusercontent.com/v0pU-8oqObn3XSR8NSFqaNbvQ-23hnUiCA79OqYyHwgmEYYaOi6j-S40vIwMktd0-CvYIYlkq476tJt6DMmjomugfwJZpmhTcJlIx5Bg7A20Y-pbyLHYtXq7nK0eSLgpppQMKuL-8Q=s50-p-k" style="display: block;"> <span style="display: block; padding-left: .5vw; padding-top:.2vw"> COVID-19 Daily Updates</span> </div><div class="col daily right" style="text-align: right; width: 49%; float: right;"> <span style="padding-top:.2vw; float: right;"> Wednesday, April 15, 2020</span> </div>
    </div><div class="main" style="width: 100%;">
        """

    html2 = """\    
    <p>Hi, <br>Today in {country_element} <br> There is new data on coronavirus:<br>  
    Total cases:{total_cases} <br> New cases:{new_cases} <br>  
    Total deaths:{total_deaths} <br> New deaths:{new_deaths} <br>  
    Active cases: {active_cases} <br> Total recovered: {total_recovered} <br>  
    Serious, critical cases: {serious_critical} <br>  
    Check the link: https://www.worldometers.info/coronavirus/</p></div></div></div></body></html>
    """.format(**locals())

    msg.add_alternative((html1+html2), subtype='html')
    
    server.send_message(msg)
    print('Hey Email has been sent!')

    server.quit()
    
bot = Coronavirus()
bot.get_data()