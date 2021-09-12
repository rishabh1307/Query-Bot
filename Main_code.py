import sys
import time
import ssl
import random
import datetime
import telepot
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s') % command

    if 'Bye' in command:
       bot.sendMessage(chat_id,"Good bye!! Have a great day.")
    
    elif 'anoop kumar mishra' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"FRI 10:30 to 11:30")
        bot.sendMessage(chat_id,"SAT 3:00 to 4:00")
    elif 'amogh katti' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"TUE 2:00 to 3:00")
        bot.sendMessage(chat_id,"THU 4:00 to 5:00")
    elif 'ambuj sharma' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"TUE 4:00 to 5:00")
        bot.sendMessage(chat_id,"THU 4:00 to 5:00")
    elif 'alluri' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"THU 1:00 to 2:00")
        bot.sendMessage(chat_id,"WED 1:00 to 2:00")
    elif 'nagaraju devarakonda' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"SAT 9:00 to 10:00")
        bot.sendMessage(chat_id,"THU 12:00 to 1:00")
    elif 'arun kumar sinha' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"THU 4:00 to 5:00")
        bot.sendMessage(chat_id,"WED 4:00 to 5:00")
    elif 'rama satish' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"SAT 12:00 to 1:00")
        bot.sendMessage(chat_id,"WED 1:00 to 2:00")
    elif 'anupama namburu' in command:
        bot.sendMessage(chat_id,"Open Hours:")
        bot.sendMessage(chat_id,"Room no: 328")
        bot.sendMessage(chat_id,"FRI 11:00 to 12:00")
        bot.sendMessage(chat_id,"WED 11:00 to 12:00")
    elif 'weather' in command:
        
        import requests, json 

        api_key = "449a334d62ee40a08c18d99ba97249db"


        base_url = "http://api.openweathermap.org/data/2.5/weather?"


        command = command.replace("weather", "")
        city_name = command 

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 


        response = requests.get(complete_url) 


        x = response.json() 


        if x["cod"] != "404": 

    
            y = x["main"] 

    
            current_temperature = y["temp"] 
            current_temperature = current_temperature - 273.15   
    

     
            current_pressure = y["pressure"] 

    
            current_humidiy = y["humidity"] 

    
            z = x["weather"] 

    
            weather_description = z[0]["description"] 

    
            bot.sendMessage(chat_id,"Temperature (in celcius unit) = " +
                    str(current_temperature) +
        "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
        "\n humidity (in percentage) = " +
                    str(current_humidiy) +
        "\n description = " +
                    str(weather_description))
            

        else: 
            bot.sendMessage(chat_id,"City not found") 


    elif 'top news' in command:
        import requests 
        from bs4 import BeautifulSoup

        url='https://www.indiatoday.in'    
    
        resp=requests.get(url) 
    
    #http_respone 200 means OK status 
        if resp.status_code==200: 
            bot.sendMessage(chat_id,str("The headlines are as follow :"))         
             
    
        
        soup=BeautifulSoup(resp.text,'html.parser')  

        l=soup.find("ul",{"class":"itg-listing"}) 
    
        #now we want to print only the text part of the anchor. 
        #find all the elements of a, i.e anchor 
        for i in l.findAll("a"): 
            bot.sendMessage(chat_id,str(i.text))
#            print(i.text) 
         
        

           
    elif 'wikipedia' in command:
        import wikipedia
        bot.sendMessage(chat_id,'Searching Wikipedia...')        
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        bot.sendMessage(chat_id,"According to Wikipedia")        
        bot.sendMessage(chat_id,str(results))
        
    elif 'Hi'or'Hello' in command:
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            bot.sendMessage(chat_id,"Good Morning!")
        elif hour>=12 and hour<18:
            bot.sendMessage(chat_id,"Good Afternoon!")    
        else:
            bot.sendMessage(chat_id,"Good Evening!")
        
        bot.sendMessage(chat_id,"I am Mr bot. Please tell me how may I help")   
    
bot = telepot.Bot('964727150:AAFQnxDIGbD1nKJP9gvFwPdt-mIDypBHeRQ')
bot.message_loop(handle)
print ('I am listening...')

while 1:
    time.sleep(10)

