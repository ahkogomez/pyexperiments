#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated
layout.

Author: Jan Bodnar
Last modified: December 2015
Website: www.zetcode.com
"""

# from Tkinter import Tk, Text, BOTH, W, N, E, S
# from ttk import Frame, Button, Label, Style
from tkinter import *
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style, Entry

import serial
import serial.tools.list_ports
from ftplib import FTP
import os, sys, time

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()


        
    def initUI(self):

        self.parent.title("PC3 Software Configuration")
        self.pack(fill=BOTH, expand=True)

        titleframe = Frame(self)
        titleframe.grid(row=0, columnspan =12, sticky = W+E+N+S)
        lbl = Label(titleframe, text="PC3 Software Configuration")
        lbl.pack()

        Frame1 = Frame(self)
        Frame1.grid(row = 1, column = 0, rowspan = 4, columnspan = 4, sticky = W+E+N+S, pady=4, padx=5) 
        Frame2 = Frame(self)
        Frame2.grid(row = 1, column = 4, rowspan = 4, columnspan = 4, sticky = W+E+N+S,pady=4, padx=5)
        Frame3 = Frame(self)
        Frame3.grid(row = 1, column = 9, rowspan = 4, columnspan=4, sticky = W+E+N+S, pady=4, padx=5)
        
        COMlbl = Label(Frame1, text="COM Port:")
        COMlbl.grid(row=1,pady=4, padx=5)
        self.COMentry = Entry(Frame1)
        self.COMentry.grid(row=1, column=1, columnspan=3,pady=4, padx=5)

        SNlbl = Label(Frame1, text="S/N:")
        SNlbl.grid(row=2, pady=4, padx=5)
        self.SNentry = Entry(Frame1)
        self.SNentry.grid(row=2,column=1, columnspan=3, pady=4, padx=5)

        Pwdlbl = Label(Frame1, text="Password:")
        Pwdlbl.grid(row=3, pady=4, padx=5)
        self.Pwdentry = Entry(Frame1)
        self.Pwdentry.grid(row=3,column=1, columnspan=3, pady=4, padx=5)

        NewPwdlbl = Label(Frame1, text="New Password:")
        NewPwdlbl.grid(row=4, pady=4, padx=5) 
        self.NewPwdentry = Entry(Frame1)
        self.NewPwdentry.grid(row=4,column=1, columnspan=3, pady=4, padx=5)

        IPlbl = Label(Frame2, text="IP Address:")
        IPlbl.grid(row=2,column=0, pady=4, padx=5)
        self.IPentry = Entry(Frame2)
        self.IPentry.grid(row=2,column=1, columnspan=3, pady=4, padx=5)

        Sublbl = Label(Frame2, text="Subnet Mask:")
        Sublbl.grid(row=3,column=0, pady=4, padx=5)
        self.Subentry = Entry(Frame2)
        self.Subentry.grid(row=3,column=1, columnspan=3, pady=4, padx=5)
        
        GWlbl = Label(Frame2, text="Gateway:")
        GWlbl.grid(row=4, column=0, pady=4, padx=5) 
        self.GWentry = Entry(Frame2)
        self.GWentry.grid(row=4,column=1, columnspan=3, pady=4, padx=5)

        self.serial_config = IntVar()
        Checkbutton(Frame3, text="set config", variable=self.serial_config).grid(row=0, column =1, padx=4, pady=5)
        self.kernel = IntVar()
        Checkbutton(Frame3, text="download software", variable=self.kernel).grid(row=1, column =1, padx=4, pady=5)
        self.ess = IntVar()
        Checkbutton(Frame3, text="download ESS", variable=self.ess).grid(row=2, column =1, padx=4, pady=5)
        self.pc3 = IntVar()
        Checkbutton(Frame3, text="get pc3diag", variable=self.pc3).grid(row=3,column =1,  padx=4, pady=5)
        self.update = IntVar()
        Checkbutton(Frame3, text="erase flash", variable=self.update).grid(row=4,column =1,  padx=4, pady=5)
        
        Frame4 = Frame(self)
        Frame4.grid(row = 6, columnspan =12, sticky = W+E+N+S, pady=4, padx=5)
        KernelLoc = Label(Frame4, text="Kernel Location:")
        KernelLoc.grid(row=0,column=0, pady=4, padx=5)
        self.KernelLocEntry= Entry(Frame4,width=100)
        self.KernelLocEntry.grid(row=0, column = 1, columnspan=9, pady=4, padx=5)

        ESSLoc = Label(Frame4, text="ESS Location:")
        ESSLoc.grid(row=1,column=0, pady=4, padx=5)
        self.ESSLocEntry= Entry(Frame4,width=100)
        self.ESSLocEntry.grid(row=1, column = 1, columnspan=9, pady=4, padx=5)

        KernelUpdateLoc = Label(Frame4, text="Erase Flash Location:")
        KernelUpdateLoc.grid(row=2,column=0, pady=4, padx=5)
        self.KernelUpdateLocEntry= Entry(Frame4, width=100)
        self.KernelUpdateLocEntry.grid(row=2, column = 1, columnspan=9, pady=4, padx=5)

        
        Frame5 = Frame(self)
        Frame5.grid(row = 7, columnspan =12, sticky = W+E+N+S, pady=4, padx=5)
        B = Button(Frame5, text ="install", command = self.helloCallBack)
        B.grid(padx=4, pady=5)
##        B2 = Button(Frame4, text ="install2", command = helloCallBack)
##        B2.grid(column = 2, padx=4, pady=5)
        
    def helloCallBack(self):
        print (self.COMentry.get())
        print (self.SNentry.get())
        print (self.NewPwdentry.get())
        print (self.IPentry.get())
##        print("conf: %d, sw: %d, ess: %d,\n" % (self.var1.get(), self.var2.get(), self.var3.get()))

        if self.serial_config.get():
            serial_conf(com_port,old_pwd,IP,subnet,gateway,SN)
        if self.update.get():
            install_update(self.IPentry.get(), 'root', self.NewPwdentry.get(), self.KernelUpdateLocEntry.get())
        if self.kernel.get():
            install_kernel(self.IPentry.get(), 'root', self.NewPwdentry.get(), self.KernelLocEntry.get())
        if self.ess.get():
            install_ESS(self.IPentry.get(), 'root', self.NewPwdentry.get(), self.ESSLocEntry.get())
        if self.pc3.get():
            get_pc3(self.IPentry.get(), 'root', self.NewPwdentry.get(), self.KernelLocEntry.get(), self.SNentry.get())
            
def install_kernel(IP='', username= 'root', password = 'Netsilicon', KernelLoc=''):
    print ("connecting to ", IP, ", username: ", username,", Pwd: ", password)

    try:
        ftp = FTP(host= IP, user=username, passwd=password)
        
        print(KernelLoc)
        file = KernelLoc+'\image.bin'
        print ("uploading ", file, "...")
        ftp.storbinary('STOR image.bin', open(file, 'rb'),callback = print("."))
        print ("done!")
    
        time.sleep(1)
    
        file = KernelLoc+'\\rom.bin'
        print ("uploading ", file, "...")
        ftp.storbinary('STOR rom.bin', open(file, 'rb'),callback = print("."))
        print ("done!")
    
        ftp.quit()
        
    except:
        print("error")
        return

    #ftp.cwd('debian')
    #ftp.retrlines('LIST')
    #ftp.retrbinary('RETR README', open('README', 'wb').write)
##    fullname = '../sourcedirectoy/filename'  
##    name = os.path.split(fullname)[1]  
##    f = open(fullname, "rb")  
##    ftp.storbinary('STOR ' + name, f)

def install_ESS(IP='', username='root', password='Netsilicon', ESSLoc=''):
    print ("connecting to ", IP, ", username: ", username,", Pwd: ", password)
    ftp = FTP(host= IP, user=username, passwd=password)
##    print ("the dir is: %s" %os.listdir(os.getcwd()))
    ess_bins = ['IDS00101','ISP00101','ISP00103','ISPffe0d','IWB00101']
    print(ESSLoc)
    try:
        for x in ess_bins:
            
            file = ESSLoc+ '\\'+ x
            print ("uploading ", file, "...")
            ftp.storbinary('STOR '+ x, open(file, 'rb'))
            print ("done!")
            ftp.quit()
            
    except:
        print ('error')

##    print ("uploading ISP00101...")
##    file = ESSLoc+'\ISP00101'
##    print (file)
##    ftp.storbinary('STOR ISP00101', open(file, 'rb'))
##    print ("done!")
##
##    print ("uploading ISP00103...")
##    file = ESSLoc+'\ISP00103'
##    print (file)
##    ftp.storbinary('STOR ISP00103', open(file, 'rb'))
##    print ("done!")
##
##    print ("uploading ISPffe0d...")
##    file = ESSLoc+'\ISPffe0d'
##    print (file)
##    ftp.storbinary('STOR ISPffe0d', open(file, 'rb'))
##    print ("done!")
##
##    print ("uploading IWB00101...")
##    file = ESSLoc+'\IWB00101'
##    print (file)
##    ftp.storbinary('STOR IWB00101', open(file, 'rb'))
##    print ("done!")
    


def get_pc3(IP='', username='root', password='Netsilicon', KernelLoc='', SN=''):
    print ("connecting to ", IP, ", username: ", username,", Pwd: ", password)
    ftp = FTP(host= IP, user=username, passwd=password)
    
    print(KernelLoc)
    ftp.retrlines('LIST')
    ftp.retrbinary('RETR pc3diag.txt', open('pc3diag.txt', 'wb').write)
    os.rename('pc3diag.txt', KernelLoc+'\\'+ SN[1:]+'.txt')
    ftp.quit()
    
##    os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo")
##    print ("the dir is: %s" %os.listdir(os.getcwd()))


def install_update(IP='', username= 'root', password = 'Netsilicon', KernelLoc=''):
    print("hello")
    
def serial_conf(com_port,old_pwd,IP,subnet,gateway,SN):
                options = {}
                    
                try:
                        ser = serial.Serial(
                                port = com_port,\
                                baudrate = 9600,\
                                parity = serial.PARITY_NONE,\
                                stopbits = serial.STOPBITS_ONE,\
                                bytesize = serial.EIGHTBITS,\
                                timeout = None)
                                
                except serial.SerialException:
                        print ("ERROR: Could Not Open %s!" %(com_port))
                        return

                while not ser.isOpen:
                        try:
                                ser = serial.Serial(
                                        port = com_port,\
                                        baudrate = 9600,\
                                        parity = serial.PARITY_NONE,\
                                        stopbits = serial.STOPBITS_ONE,\
                                        bytesize = serial.EIGHTBITS,\
                                        timeout = None)
                        except serial.SerialException:
                                print ("ERROR: Could Not Open %s" % (com_port))
                                input (' Press anything to continue')
                
                
                ser.close()
                ser.open()

                ser.write('~')
                buff=''
                buff = ser.read(size= 2, timeout=3)
                time.sleep(2)
                buff += ser.inWaiting()
                if len(buff) == 0:
                    print('cannot see controller')
                else:
                    print(buff)
                if "Press any key" in buff:
                    ser.write("x")
                    time.sleep(1)
                    buff = ''
                    buff += ser.inWaiting()
                    if len(buff) == 0:
                        print('no data received')
                    else:
                        print (buff)
                    while configuring == True:
                        buff = ''
                        time.sleep(0.1)
                        buff += ser.inWaiting()
                        if len(buff) == 0:
                            print('no data received')
                            configuring = False
                        else:
                            if "Press A to Accept the settings, or M to Modify?" in buff:
                                ser.write("M")
                            elif "Enter the root password:" if buff:
                                ser.write(old_pwd+"\n")
                            elif "Reset configuration to default values [N]?" in buff:
                                ser.write('n\n')
                            elif "Obtain IP settings automatically using DHCP for this interface" in buff:
                                ser.write('n\n')
                            elif "IP address  [" in buff:
                                ser.write(IP+'\n')
                            elif "Subnet mask  [" in buff:
                                ser.write(subnet+'\n')
                            elif "Gateway address  [" in buff:
                                ser.write(gateway+'\n')
                            elif "Ethernet MAC Address" in buff:
                                ser.write('\n')
                            elif "Ethernet duplex setting" in buff:
                                ser.write('default\n')
                            elif "Set the baud rate" in buff:
                                ser.write('9600\n')
                            elif "update the Root Password" in buff:
                                ser.write('y\n')
                            elif "Enter the new Root Password" in buff:
                                ser.write(new_pwd+'\n')
                            elif "Re-enter the new Root Password" in buff:
                                ser.write(new_pwd+'\n')
                            elif "update the Administrator" in buff:
                                ser.write('n\n')
                            elif "Set the board's serial number[" in buff:
                                ser.write(SN+'\n')
                            elif "CPU delay" in buff:
                                ser.write('5\n')
                            elif "Saving the changes in NV memory" in buff:
                                configuring = False
                            else:
                                continue
def findports():
    
    ports = list(serial.tools.list_ports.comports())
    print ("finding ports")
    for p in ports:
        print (p)
        
def main():

    findports()
    root = Tk()
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
