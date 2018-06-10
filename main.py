from tkinter import *
import json
import requests
import simplejson
import urllib
from tkinter import messagebox



class Tour:
    def __init__(self, master):
       
        self.master = master
       
        master.title("Tour")
        
        Label(master, text="Orgin").grid(row=0, column=0)
        Label(master, text="Destination").grid(row=2, column=0)
        Label(master, text="Mode").grid(row=4, column=0)
        Label(master, text="Distance (m)").grid(row=6, column=0, pady=(30, 0))
        
        e1 = Entry(master)
       
        e2 = Entry(master)
       
        e3 = Entry(master)
        
        e4 = Entry(master)
  
        
        e1.grid(row=1, column=0, padx=10, pady=10)
        e2.grid(row=3, column=0, padx=10, pady=10)
        e3.grid(row=5, column=0, padx=10, pady=10)
        e4.grid(row=7, column=0, padx=10, pady=10)
       
        Button(master, text='GetDistance', command= lambda: self.distance(e1, e2, e3, e4)).grid(row=8, column=0, sticky=W, pady=4)
        
    def distance(self, e1, e2, e3, e4):
        source = e1.get()
        dest = e2.get()
        mode = e3.get()
        if not (mode == 'driving' or mode =='walking' or mode == 'biking'):
           message = "Invalid mode. valid modes are 'driving', 'biking' and 'walking'" 
           messagebox.showinfo("", message) 
        url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        
        r = requests.get(url + 'origins=' + source + '&destinations=' + dest + '&mode=' + mode + '&sensor=false') #fixed with no spaces in the url
        x = r.json()
        print(x)
        
        element_dict = x['rows'][0]['elements'][0]
        if element_dict == {'status': 'NOT_FOUND'}:
            message = "distance between " + source + " and " + dest + "not found" 
            messagebox.showinfo("", message)
            
        else:
            dist = element_dict['distance']['text']
            duration = element_dict['duration']['text']
            
            print('Distance: ' + dist)
            print('Duration: ' + duration)
            d = dist.split()
            num = d[0]
            num = num.replace(',', '')
            num = float(num)
                 
            print(num)
            meter = num * 1000
            print(meter)
            e4.delete(0, END)
            e4.insert(0, meter)
                

   
root = Tk()

my_gui = Tour(root)

root.mainloop()
