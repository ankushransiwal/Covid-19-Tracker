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
        India_element = table.find_element_by_xpath("//td[contains(., 'India')]")
        row_Ind = India_element.find_element_by_xpath("./..")
        data_Ind = row_Ind.text.split(" ")
        total_cases_Ind = data_Ind[1]
        new_cases_Ind = data_Ind[2]
        total_deaths_Ind = data_Ind[3]
        new_deaths_Ind = data_Ind[4]
        active_cases_Ind = data_Ind[5]
        total_recovered_Ind = data_Ind[6]
        serious_critical_Ind = data_Ind[7]

        World_element = table.find_element_by_xpath("//td[contains(., 'World')]")
        row_World = World_element.find_element_by_xpath("./..")
        data_World = row_World.text.split(" ")
        total_cases_World = data_World[1]
        total_deaths_World = data_World[3]

        #total_cases = row.find_element_by_class_name('sorting_1')
        #new_cases = row.find_element_by_xpath("//td[3]")
        #total_deaths = row.find_element_by_xpath("//td[4]")
        #new_deaths = row.find_element_by_xpath("//td[5]")
        #active_cases = row.find_element_by_xpath("//td[6]")
        #total_recovered = row.find_element_by_xpath("//td[7]")
        #serious_critical = row.find_element_by_xpath("//td[8]")
        print("Country: " + India_element.text)
        print("Total cases: " + total_cases_Ind)
        print("New cases: " + new_cases_Ind)
        print("Total deaths: " + total_deaths_Ind)
        print("New deaths: " + new_deaths_Ind)
        print("Active cases: " + active_cases_Ind)
        print("Total recovered: " + total_recovered_Ind)
        print("Serious, critical cases: " + serious_critical_Ind)

        send_mail(India_element.text, total_cases_Ind, new_cases_Ind, total_deaths_Ind, new_deaths_Ind, total_cases_World, total_deaths_World)

        self.driver.close()
        #except:
        self.driver.quit()

def send_mail(India_element, total_cases_Ind, new_cases_Ind, total_deaths_Ind, new_deaths_Ind, total_cases_World, total_deaths_World):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    server.login('ankushransiwal.13@gmail.com', 'dibzvlfqwxouxraa')
    msg = EmailMessage()
    msg['Subject'] = 'Coronavirus stats in your country today!'
    msg['From'] = 'ankushransiwal.13@gmail.com'
    msg['To'] = 'ankushransiwal.13@gmail.com'
    msg.set_content('Today in ' + India_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases_Ind +'\
        \nNew cases: ' + new_cases_Ind + '\
        \nTotal deaths: ' + total_deaths_Ind + '\
        \nNew deaths: ' + new_deaths_Ind + '\
        \Total World cases: ' + total_cases_World + '\
        \nTotal World deaths: ' + total_deaths_World + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/')
    
    html1= """\
        <!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"> <head> <title></title> <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <meta name="viewport" content="width=device-width,initial-scale=1"> <style type="text/css"> 
        body{ margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; font-family: Verdana,sans-serif;}.main{font-weight: 300; display: inline-flex; color: #3D2D4B; font-size: 11px;}.container-inner{width: 75%;}
        .icon{width: 18px; height: 18px;}.daily{font-weight: 300; display: inline-flex; font-size: 14px; color: #424242;}.updated-heading{margin-top: 6%; font-size: 14px; color: #424242; text-align: center;}
        .updated-india{font-size: 20px; color: #3D2D4B; text-align: center; font-weight: 600;}.world{font-size: 18px;}.right{text-align: right;}.banner{width: 100%; height: auto; margin-top: 3%; margin-bottom: 3%;}
        .card{background-color: #f5f5f5; width: 49%; margin-top: 5%; padding: 1.2rem 1.2rem; border-radius: 4px; text-align: center; border: 1px solid #eeeeee;}.card-left{margin-right: 3%;}.card-right{margin-left: 3%;}
        .detail{font-size: 12px; color: #424242;}.figure{font-size: 14px; color: #CD4A52; font-weight: bold;}.button{margin: auto; background-color: #3D2D4B; border-radius: 1.5vw; color: #fafafa; padding: 1em 2em; text-decoration: none; width: max-content; font-size: 12px;}
        .safe{color: #CD4A52; margin-top: 1%;}.slogan{color: #3D2D4B; font-weight: 600; margin-top: 7%;}@media only screen and (max-width: 800px){/* ----- Base styles ----- */ .container-full{width: 80% !important;}.container-inner{width: 80%;}}
        @media only screen and (max-width: 600px){/* ----- Base styles ----- */ .container-full{width: 85% !important;}.container-inner{width: 90%;}.icon{width: 14px; height: 14px;}.daily{font-size: 12px;}.main{font-size: 9px;}.updated-heading{font-size: 10px;}
        .updated-india{font-size: 16px;}.world{font-size: 13px;}.detail{font-size: 10px;}.figure{font-size: 12px;}.button{font-size: 10px; border-radius: 2vw;}}@media only screen and (max-width: 400px){/* ----- Base styles ----- */ .daily{font-size: 10px;}
        .main{font-size: 7px;}}</style> </head> <body style="background-color:#F8D4D4;"> <div class="container-full" style="background-color: #FaFaFa; margin: auto; width: 700px; height:90%; margin-top: 5%; margin-bottom: 5%; padding-top: 2%; padding-bottom: 2%;"> 
        <div class="container-inner" style=" margin: auto; padding-top: 15px; padding-bottom: 15px;"> 
        <div class="row"> <div class="col daily"> <img class="icon" src="https://lh3.googleusercontent.com/v0pU-8oqObn3XSR8NSFqaNbvQ-23hnUiCA79OqYyHwgmEYYaOi6j-S40vIwMktd0-CvYIYlkq476tJt6DMmjomugfwJZpmhTcJlIx5Bg7A20Y-pbyLHYtXq7nK0eSLgpppQMKuL-8Q=s50-p-k" style="display: block;"> 
        <span style="display: block; padding-left: 1vw; padding-top:.2vw"> COVID-19 Daily Updates</span> </div></div><div class="row"> 
        <img class="banner" src="https://lh3.googleusercontent.com/Mz-ndU5sj9alg9bH69kuGVNIjLPzfcL4eQdeHGkf4uYBgCZ7QziBlHbsoSHgxkOpK3lhVmyK2hUya_wVxJls0zQlxhVM5g0LxwfhP4TCmCBLYcLS2T9x4XDMhrFTpErPbicgMEdMag=w2400" style="display: block;"> 
        </div><div class="updated-heading"> <span>UPDATED RESULTS</span> </div>
        """

    html2 = """\
            <div class="updated-india">
            <span>{India_element}</span>
            </div>
            <div style="width: 100%; display: inline-flex;">
            <div class="card card-left">
                <div class="detail">Total Cases</div>
                <div class="figure">{total_cases_Ind}</div>
            </div>
            <div class="card card-right">
                <div class="detail">Total Deaths</div>
                <div class="figure">{total_deaths_Ind}</div>
            </div>
            </div>
            <div style="width: 100%; display: inline-flex;">
            <div class="card card-left">
                <div class="detail">New Cases</div>
                <div class="figure">{new_cases_Ind}</div>
            </div>
            <div class="card card-right">
                <div class="detail">New Deaths</div>
                <div class="figure">{new_deaths_Ind}</div>
            </div>
            </div>   
            <div class="updated-heading">
            <span>UPDATED RESULTS</span>
            </div>
            <div class="world updated-india">
            <span>WORLDWIDE</span>
            </div>
            <div style="width: 100%; display: inline-flex;">
            <div class="card card-left">
                <div class="detail">Total Cases</div>
                <div class="figure">{total_cases_World}</div>
            </div>
            <div class="card card-right">
                <div class="detail">Total Deaths</div>
                <div class="figure">{total_deaths_World}</div>
            </div>
            </div>
            <div class="" style="text-align: center; margin-top: 8%; ">
            <a href="https://www.worldometers.info/coronavirus/" style= "color: #fafafa; text-decoration: none;" class="button" role="button">All About COVID-19 <b>></b></a>          
            </div>
            <div class="slogan updated-heading">
            <span>Save the world by staying at home</span>
            </div>
            <div class="safe updated-india">
            <span>#Staysafe</span>
            </div>
        </div>
        </div>
    </body>
    </html>
    """.format(**locals())

    msg.add_alternative((html1+html2), subtype='html')
    
    server.send_message(msg)
    print('Hey Email has been sent!')

    server.quit()
    
bot = Coronavirus()
bot.get_data()