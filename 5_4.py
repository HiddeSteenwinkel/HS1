infile = open('C:/Users/Hidde/kaartnummers.txt', 'w')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
print(s)