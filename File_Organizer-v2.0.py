import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import *
from tkinter import filedialog
from tkinter import *
import os
import shutil

def CheckFileSize():
    getpath = EntryBox.get()
    path = getpath.lower()
    flag = False
    if not os.path.exists(path):
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"INFO:"+"Invalid Path => " + getpath)
        Display_area.yview(END)
        return flag
    else:
        files_list = os.listdir(path) #List of files in the path
        # print(files_list)
        for file in files_list:
            sizeoffiles =0
            filesize = 0
            fs=0
            if(os.path.isdir(path+'/'+file)):
                files_folder = os.listdir(path+'/'+file)
                for files in files_folder:
                    sizeoffiles = os.path.getsize(path+'/'+file+'/'+files)#Size of Files
                    filesize += sizeoffiles #Size of Folder = Total size of files in that folder
                
                fs = filesize /1024  #Bytes to KB
                
            else:
                filesize = os.path.getsize(path+'/'+file)
                # print(filesize)
                fs = filesize / 1024
                print(fs)
            # Move Files < 1 KB to Deletable  Folder
            if fs < 1:
                folder = "Deletable"
                flag = True
                if os.path.exists(path+"/"+folder):
                        try:
                            if (os.path.isdir(path+'/'+file) and fs!=0 )or file=="Deletable":
                                Display_area.config(state=NORMAL)
                                Display_area.insert(END, "\n"+"INFO: "+"Checking Files.. Folder Found ")
                                Display_area.yview(END)

                            else:
                                shutil.move(path + '/' + file, path + '/' + folder + '/' + file)
                             
                        except PermissionError:
                            pass          
                else:
                    try:
                        os.makedirs(path+'/'+folder)
                        if (os.path.isdir(path+'/'+file) and fs!=0) or file == "Deletable":
                                Display_area.config(state=NORMAL)
                                Display_area.insert(END, "\n"+"INFO: "+"Checking Files.. Folder Found ")
                                Display_area.yview(END)

                        else:
                                shutil.move(path + '/' + file, path + '/' + folder + '/' + file)

                    except PermissionError:
                        pass
           
    return flag

def DeleteJunk():
    flag_cfs =  CheckFileSize() #Flag for check file size
    getpath = EntryBox.get()
    path = getpath.lower()
    def display_warning():
        label = tk.Label(base, text="Warning: Please Check Files in Folder!!",font=('Times New Roman',12),bg="#dd0a35")
        label.place(x=130,y=80)
        base.after(10000, label.destroy)    #10s=10000ms  
    
    if flag_cfs == False:
         if os.path.exists(path+'/'+'Deletable'):
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO: Found Duplicate Files Check Folder =>"+ getpath+'/'+'Deletable')
            Display_area.yview(END)
         else:
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO: "+"No Files to be Deleted")
            Display_area.yview(END)


    if flag_cfs == True:
        
        delete_path = path+'/'+'Deletable'
        blacklist = os.listdir(delete_path) #List of folders in the path
        display_warning() 
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"------------------------D E L E T E-----------------------")
        Display_area.yview(END)
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"INFO: "+"Found some files which can be deleted")
        Display_area.yview(END)
        for file in blacklist:
                filesize = os.stat(delete_path+"/"+file).st_size
                fs = filesize // 1024   #Bytes to KB
                if fs > 1024 :
                    fs = fs // 1024     #Kb to MB

                Display_area.config(state=NORMAL)
                Display_area.insert(END, "\n"+"INFO:"+" File :" + file+" is {} KB".format(fs))
                Display_area.yview(END)

        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"----------------------------------------------------------")
        Display_area.yview(END)
        response = messagebox.askyesno("Confirm","Would you like to delete the files?")
        if(response):
            for file in blacklist:
                if os.path.isdir(delete_path+'/'+file):
                    os.rmdir(delete_path+'/'+file)
                    Display_area.config(state=NORMAL)
                    Display_area.insert(END,"\n"+"INFO: "+ "Deleted File =>" + file)
                    Display_area.yview(END)
                else:
                    os.remove(delete_path+'/'+file)
                    Display_area.config(state=NORMAL)
                    Display_area.insert(END,"\n"+"INFO: "+ "Deleted File =>" + file)
                    Display_area.yview(END)
            try:
                shutil.rmtree(delete_path)
            except OSError:
                pass
                
        else:
            Display_area.config(state=NORMAL)
            Display_area.insert(END,"\n"+"INFO: "+ "Done.(Files Saved in Deletable folder)" + '\n')
            Display_area.yview(END)
        
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"----------------------------------------------------------")
        Display_area.yview(END)

        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+ "Done"+'\n')
        Display_area.yview(END)
        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+"Check Folder: "+ getpath+'\n')
        Display_area.yview(END)



def Duplicheck():
    getpath = EntryBox.get()
    path = getpath.lower()
    flag = False
    if not os.path.exists(path):
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"INFO:"+"Invalid Path => " + getpath)
        Display_area.yview(END)
        flag = "invalid"
        return flag
    else:
     folder = "Duplicates"
     filelist = os.listdir(path)
     for files in filelist:
            if "Copy" in files:
                flag = True
                try:
                    if os.path.isdir(path+'/'+files):
                        Display_area.config(state=NORMAL)
                        Display_area.insert(END, "\n"+"INFO: "+"Checking Files.. Folder Found")
                        Display_area.yview(END)
                    else:
                        if os.path.exists(path+'/'+folder):
                            shutil.move(path+'/'+files,path+'/'+folder+'/'+files)
                        else:
                            os.makedirs(path+'/'+folder)
                            shutil.move(path+'/'+files,path+'/'+folder+'/'+files)

                except PermissionError:
                                pass
                
       
    
    return flag


def FindDuplicate():
    getpath = EntryBox.get()
    path = getpath.lower() 
    flag_cdf = Duplicheck()  #flag for Duplicate files

    if flag_cdf == False:
        if os.path.exists(path+'/'+'Duplicates'):
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO: Found Duplicate Files Check Folder =>"+ getpath+'/'+'Duplicates')
            Display_area.yview(END)
        else:
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO: "+"No Duplicate Files")
            Display_area.yview(END)
    
    if flag_cdf == True:
        duplicate_list = os.listdir(path+'/'+'Duplicates')
        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"----------------------------------------------------------")
        Display_area.yview(END)

        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"INFO: Found Duplicate Files Check Folder =>"+ getpath+'/'+'Duplicates')
        Display_area.yview(END)
        response = messagebox.askokcancel("INFO"," Found Duplicate Files")
        if(response):
            for file in duplicate_list:
                Display_area.config(state=NORMAL)
                Display_area.insert(END, "\n"+"INFO :"+"File => "+file)
                Display_area.yview(END)
           
        else:
             Display_area.config(state=NORMAL)
             Display_area.insert(END, "\n"+"INFO: "+ "Done")
             Display_area.yview(END)

        Display_area.config(state=NORMAL)
        Display_area.insert(END, "\n"+"----------------------------------------------------------")
        Display_area.yview(END)

        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+ "Done"+'\n')
        Display_area.yview(END)
        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+"Check Folder: "+ getpath+'\n')
        Display_area.yview(END)
           

            
def Organizer():
    Display_area.config(state=NORMAL)
    Display_area.delete(1.0, END)
    getpath = EntryBox.get()
    path = getpath.lower()
    files_list = []
   
    DIRECTORIES = {
    
    "Images": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg",
               "heif", "psd"],
    "Videos": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng",
               "qt", "mpg", "mpeg", "3gp"],
    "Documents":["docx","doc","odt","pub","docm","dotx","rtf","csv","txt"],
    "PDF":["pdf"],
    "Presentation Files":["pptx","ppt"],
    "Spreadsheets":["xlsx","xls","xlsm","xl","ots"],
    "Python Files":["py","ipynb"],
    "Web Programming(HTMl,CSS...)":["html","css","js","xml","url","php"],
    "Executable Files":["exe","msi","apk"],
    "System Files":["dll","bin","bak","dmp","log"],
    "Compressed Files":["zip","rar","tar","jar"],
    "Music":["mp3","wav"],
    "C Programming Files":["c","c++"],
    "Java Proramming Files":["java","class","jsp","jhtml","jtk"],
    "Icons":["ico"],
    "Subtitles":["srt"],
    "Batch Files":["batch","sh"],

    }

     
    FILE_EXT =  {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats}

     
    flag=True
    #Checking whether a path exists or not
    if not os.path.exists(path):
        flag=False
        if (path == "downloads" or path=="desktop"):
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO:"+"Invalid Path => " + getpath)
            Display_area.yview(END)
            Display_area.config(state=NORMAL)
            Display_area.insert(END, "\n"+"INFO:"+r"Try: C:\Users\<username>\Downloads or ...\Desktop")
            Display_area.yview(END)
        else:
            flag=False
            if (path == ""):
                Display_area.config(state=NORMAL)
                Display_area.insert(END, "INFO:"+"Please Specify Path ")
                Display_area.yview(END)
            else:
                flag=False
                Display_area.config(state=NORMAL)
                Display_area.insert(END, "\n"+"INFO: "+"Invalid Path => " + getpath)
                Display_area.yview(END)
                
    else:
        files_list = os.listdir(path) #List of folders in the path
    
    #File handler
    for files in files_list:
             if '.' not in files:   #For Files without any extension move to Other Files folder
                file_name = files
                
                folder = "Other Files"
                if(os.path.isdir(path+"/"+file_name)): #For folder handling (Folders don't have extension ) 
                    Display_area.config(state=NORMAL)
                    Display_area.insert(END, "\n" +"INFO: "+ "Checking files.. Folder found " + "\n")

                    Display_area.config(state=NORMAL)
                    Display_area.insert(END, "INFO: "+"Cannot Move a Folder..." + "\n")
                    

                else:
                    if os.path.exists(path + '/' + folder): #if folder exists move to existing folder
                        try:
                            shutil.move(path + '/' + file_name, path + '/' + folder + '/' + file_name)
                            Display_area.config(state=NORMAL)
                            Display_area.insert(END, "INFO: "+"Moving..." + "\n")
                             
                        except PermissionError:
                            pass
                    else:
                        try:
                            os.makedirs(path + '/' + folder)  #make a folder and move the file
                            shutil.move(path + '/' + file_name, path + '/' + folder + '/' + file_name)
                            Display_area.config(state=NORMAL)
                            Display_area.insert(END, "INFO: "+"Moving..." + "\n")
                            
                        except PermissionError:
                            pass
                                     
             else:                                          #For Files with an extension to move specified folders
                    f_name, f_ext = os.path.splitext(files)
                    f_ext = f_ext.strip('.').lower()
                    folder = FILE_EXT.get(f_ext)
                    # print(folder)
                   
                    if folder == None:
                        folder= "Other Files"
                        
                    if os.path.exists(path + '/' + folder):
                        try:
                            shutil.move(path + '/' + files, path + '/' + folder + '/' + files)
                        except PermissionError:
                            pass
                    else:
                        try:
                            os.makedirs(path + '/' + folder)
                            shutil.move(path + '/' + files, path + '/' + folder + '/' + files)
                          

                            Display_area.config(state=NORMAL)
                            Display_area.insert(END,"\n"+"INFO: "+ "Looking for files..." + '\n')
                            Display_area.yview(END)
                            Display_area.config(state=NORMAL)
                            Display_area.insert(END, "\n"+"INFO: "+ "Creating Folders..." + '\n')
                            Display_area.yview(END)
                            Display_area.config(state=NORMAL)
                            Display_area.insert(END, "\n"+"INFO: "+ "Copying Files to Folders....." + '\n')
                            Display_area.yview(END)
                            flag=True
                        except PermissionError:
                            pass

    # # ttk.Label(base,text="Warning: Please Check Files in Folder", background="#dd0a35",foreground="white", font = ("Times New Roman", 12)).place(x=130,y=80)
    # def display_warning():
    #     label = tk.Label(base, text="Warning: Please Check Files in Folder!!",font=('Times New Roman',12),bg="#dd0a35")
    #     label.place(x=130,y=80)
    #     base.after(10000, label.destroy)    #10s=10000ms            
    # if flag_cfs == True:
        
    #     delete_path = path+'/'+'Deletable'
    #     blacklist = os.listdir(delete_path) #List of folders in the path
    #     display_warning() 
    #     Display_area.config(state=NORMAL)
    #     Display_area.insert(END, "\n"+"----------------------------------------------------------")
    #     Display_area.yview(END)
    #     Display_area.config(state=NORMAL)
    #     Display_area.insert(END, "\n"+"INFO: "+"Found some files which can be deleted")
    #     Display_area.yview(END)
    #     for file in blacklist:
    #             filesize = os.stat(delete_path+"/"+file).st_size
    #             fs = filesize // 1024   #Bytes to KB
    #             if fs > 1024 :
    #                 fs = fs // 1024     #Kb to MB

    #             Display_area.config(state=NORMAL)
    #             Display_area.insert(END, "\n"+"INFO:"+" File :" + file+" is {} KB".format(fs))
    #             Display_area.yview(END)
    #     Display_area.config(state=NORMAL)
    #     Display_area.insert(END, "\n"+"----------------------------------------------------------")
    #     Display_area.yview(END)
    #     response = messagebox.askyesno("Confirm","Would you like to delete the files?")
    #     if(response):
    #         for file in blacklist:
    #             if os.path.isdir(delete_path+'/'+file):
    #                 os.rmdir(delete_path+'/'+file)
    #                 Display_area.config(state=NORMAL)
    #                 Display_area.insert(END,"\n"+"INFO: "+ "Deleted File =>" + file)
    #                 Display_area.yview(END)
    #             else:
    #                 os.remove(delete_path+'/'+file)
    #                 Display_area.config(state=NORMAL)
    #                 Display_area.insert(END,"\n"+"INFO: "+ "Deleted File =>" + file)
    #                 Display_area.yview(END)
    #         try:
    #             shutil.rmtree(delete_path)
    #         except OSError:
    #             pass
                
    #     else:
    #         Display_area.config(state=NORMAL)
    #         Display_area.insert(END,"\n"+"INFO: "+ "Done.(Files Saved in Deletable folder)" + '\n')
    #         Display_area.yview(END)
        
    #     Display_area.config(state=NORMAL)
    #     Display_area.insert(END, "\n"+"----------------------------------------------------------")
    #     Display_area.yview(END)
        
    
    
    
    # if flag_cdf == True:
    #     response = messagebox.askokcancel("INFO: Found Duplicate Files")
    #     if(response):
    #         Display_area.config(state=NORMAL)
    #         Display_area.insert(END, "\n"+"INFO: Found some  Duplicate files  Check Folder =>"+ getpath+'/'+'Duplicate')
    #         Display_area.yview(END)
    #     else:
    #          Display_area.config(state=NORMAL)
    #          Display_area.insert(END, "\n"+"INFO: "+ "Done")
    #          Display_area.yview(END)
            
    if(flag):
        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+ "Done"+'\n')
        Display_area.yview(END)
        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+"Check Folder: "+ getpath+'\n')
        Display_area.yview(END)
    else:
        Display_area.config(state=NORMAL)
        Display_area.insert(END,"\n"+"INFO: "+ "Done"+'\n')
        Display_area.yview(END)


    

def clear():
    Display_area.config(state=NORMAL)
    Display_area.delete(1.0, END)
    EntryBox.delete(0,END)
    
    
def CopyPaste(event):
    try:
        event.widget.delete("sel.first", "sel.last")
    except:
        pass
    event.widget.insert("insert", event.widget.clipboard_get())
    return "break"


def askdirectory():
    EntryBox.delete(0,END)
    folder_selected = filedialog.askdirectory()
    EntryBox.insert(0,folder_selected)

base = tk.Tk()
base.title('File Organizer')
base.geometry("500x500")
base.resizable(width=False, height=False)

Label(base,text="Enter Location",bg="wheat1",font=("Verdana",10,"bold")).grid(row=0)
EntryBox = Entry(base,width="32",bg="wheat3",fg="black",font=("Verdana",12))
base.bind_class("Entry", "<<Paste>>", CopyPaste)

Org_Btn = Button(base, font=("Verdana", 8,"bold"),text="Organize", width="9", height=2,
                     bd=2, bg="palegreen", activebackground="plum1", fg='#000000'
                 ,command = Organizer).place(x=35,y=35)

Browse_btn = Button(base,text="Browse", width="8",
                     bd=2, bg="azure2", activebackground="gray69", fg='#000000',command=askdirectory).place(x=435,y=0)

                 
Duplicate_check = Button(base, font=("Verdana", 8,"bold"),text="Find Duplicate", width="12", height=2,
                     bd=2, bg="salmon1", activebackground="khaki2", fg='#000000'
                 ,command = FindDuplicate).place(x=125,y=35)

Delete_Junk = Button(base, font=("Verdana", 8,"bold"),text="Delete Junk Files", width="15", height=2,
                     bd=2, bg="RosyBrown1", activebackground="thistle1", fg='#000000'
                 ,command = DeleteJunk).place(x=240,y=35)


clear = Button(base, font=("Verdana", 8,"bold"), text="Clear Field", width="9", height=2,
                     bd=2, bg="gray81", activebackground="aquamarine2", fg='#000000',
                     command=clear).place(x=380,y=35)



Display_area = ScrolledText(base,width="58",height=20,bg="AntiqueWhite2")
Display_area.config(state=DISABLED)


Credits = Entry(base,width="45",bg="wheat1",borderwidth=0,justify="center",font=("Verdana", 10,"bold"))
Credits.insert(0,"Developed by Vishnu Nair")


EntryBox.grid(row=0,column=1)
Display_area.place(x=6,y=100)
Credits.place(x=40,y=450)
base.configure(bg="wheat1")
base.mainloop()


