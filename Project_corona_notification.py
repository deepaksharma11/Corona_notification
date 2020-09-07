from plyer import notification #install plyer for notification
import requests #to get data from the specified url
from bs4 import BeautifulSoup #install bs4 for BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Image\corona.ico",
        timeout = 10 )
def getData(url):
    data = requests.get(url)
    return data.text

if __name__ == "__main__":
    while True:
        myhtmldata = getData("https://www.worldometers.info/coronavirus/")
        soup = BeautifulSoup(myhtmldata, 'html.parser')
        a = ""
        for table in soup.find_all('tbody')[0].find_all('tr'):
            a += str(table.get_text())
        a = a.split("\n")
        a = a[184:]
        b=[]
        c=[]
        i = 2
        for j in a:
            if  j != str(i):
                c.append(j)
            elif j == str(i):
                b.append(c)
                i+=1
                c = []

        states = ["India", "USA", "Russia", "China"]
        for k in range(len(b)):
            if str(b[k][0]) in states:
                d = b[k]
                print(d)
                notifyMe(f"{d[0]}", f"Total Cases: {d[1]}\nNew Cases: {d[2]}\nTotal Deaths: {d[3]}\nNew Deaths: {d[4]}")
                import time
                time.sleep(5)
            
        import time
        time.sleep(360)