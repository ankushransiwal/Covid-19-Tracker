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
    msg['To'] = 'ankushransiwal.13@gmail.com'
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
    
    html = """\
        <!DOCTYPE html>
        <html> 
        <body> 
        <p>Hi,
        <br> Today in  {country_element} \
        \nThere is new data on coronavirus:\
        \nTotal cases: {total_cases} \
        \nNew cases: {new_cases} \
        \nTotal deaths: {total_deaths} \
        \nNew deaths: ' + new_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nSerious, critical cases: ' + serious_critical  + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/</p> 
        <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p> <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p> </body> </html>
        """.format(**locals())
    
    msg.add_alternative(html, subtype='html')
    
    server.send_message(msg)
    print('Hey Email has been sent!')

    server.quit()
    
bot = Coronavirus()
bot.get_data()