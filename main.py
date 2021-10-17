import pywhatkit
import datetime
import time

# pywhatkit.sendwhatmsg("+917986485146","Hi, how are you?",17,50)
# hour = datetime.datetime.now().hour
# mins = int(datetime.datetime.now().mins) + 2
# print("sent message successfully")


contact_list = {
    'Anchit' : '+917986485146',
    'Ajay' : "+919914417457",
    'Anshi' : "",
    "Arjit" : ""
}

def sending_whatsapp_message(number,message):
    pywhatkit.sendwhatmsg_instantly(number,message,tab_close=True)


if __name__ == '__main__':
    for i,j in contact_list.items():
        text = f"Hi {i}, How are you doing? This is an automatically generated message."
        # print(text)
        try:
            sending_whatsapp_message(number=j,message=text)
            # time.sleep(150)
        except:
            print("Invalid contact",i,j)
