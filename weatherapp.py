from os import name
from tkinter import * 
import requests
def weather(city):
    try:
        api_key='449ccbc60cb769837b9cc6dd01f89dd0'
        url='https://api.openweathermap.org/data/2.5/weather'
        params={'appid':api_key,'q':city,'units':'metric'}
        response=requests.get(url,params=params)
        weather=response.json()
        print(weather['name'])
        print(weather['main']['temp'])
        print(weather['weather'][0]['description'])
        label['text']='City: '+weather['name']+'\nTemperature(°C):'+str(weather['main']['temp'])
        label['text']+='\nDescription:\n'+ weather['weather'][0]['description']
    except:
        print('Data for this City is not available\n')
        label['text']='Data not available!!\n'+'Enter correct city name'
        
root = Tk()
root.title('Weather APP')
canvas= Canvas(root,height=500,width=600)
canvas.pack()
#API Key:- 449ccbc60cb769837b9cc6dd01f89dd0
bg_img=PhotoImage(file='C:\\Users\\USER\\Desktop\\Ayush\\bg.png')
bg_label=Label(root,image=bg_img)
bg_label.place(relwidth=1,relheight=1)
frame=Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

enter=Entry(frame,font=('Courier',20))
enter.place(relwidth=0.65,relheight=1)

button=Button(frame,text="Submit",font=40,command=lambda: weather(enter.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lo_frame=Frame(root,bd=10,bg='#80c1ff')
lo_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.65,anchor='n')

label=Label(lo_frame,text="Please Enter City Name",font=('Courier',20))
label.place(relwidth=1,relheight=1)
root.mainloop()