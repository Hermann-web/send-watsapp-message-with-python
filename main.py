import pywhatkit as kit
import time
import datetime


#choose a sending time and convert to seconds
instant = 12500


date = datetime.datetime.now
initial = 3600*date.hour + 60 *date.minute
instant = initial + 60
repos = 60;
nb_h,nb_min= time.localtime(instant).tm_hour, time.localtime(instant).tm_min 
instant += repos
phone_number = "+......" #the phone number of the receiver
kit.sendwhatmsg(phone_number, "Message envoyé à {} h {} min".format(nb_h,nb_min), nb_h,nb_min)







