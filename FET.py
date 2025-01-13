import os #line:1
from datetime import datetime #line:2
from tkinter import Tk ,Entry ,Button ,filedialog ,Label ,Frame #line:3

class FileEncryptionTool :#line:6
    def __init__ (O00OO0O0OO0OO0O0O ,O00OO0OO0O0O0O0OO ):#line:7
        O00OO0O0OO0OO0O0O .root =O00OO0OO0O0O0O0OO #line:8
        O00OO0O0OO0OO0O0O .root .title ("File Encryption Tool")#line:9
        O00OO0O0OO0OO0O0O .root .configure (bg ="#FFFFFF")#line:10
        O00OO0O0OO0OO0O0O .file_entry =None #line:11
        O00OO0O0OO0OO0O0O .status_label =None #line:12
        O00OO0O0OO0OO0O0O .setup_ui ()#line:13
    def setup_ui (O00O00O00OOO0000O ):#line:15
        Label (O00O00O00OOO0000O .root ,text ="Purpose: This program encrypts reflection mark down files.",fg ="black",bg ="#FFFFFF",font =("Helvetica",12 ,"bold")).pack (pady =10 )#line:18
        O00O00O00OOO0000O .file_entry =Entry (O00O00O00OOO0000O .root ,width =50 ,font =("Helvetica",12 ))#line:21
        O00O00O00OOO0000O .file_entry .pack (pady =5 )#line:22
        OO0O0OOOOO00000OO =Frame (O00O00O00OOO0000O .root ,bg ="#FFFFFF")#line:25
        OO0O0OOOOO00000OO .pack (pady =10 )#line:26
        Button (OO0O0OOOOO00000OO ,text ="Browse",command =O00O00O00OOO0000O .select_file ,font =("Helvetica",12 ),bg ="#4CAF50",fg ="black",activebackground ="#45A049",activeforeground ="black",width =10 ,padx =10 ,pady =5 ).grid (row =0 ,column =0 ,padx =5 )#line:30
        Button (OO0O0OOOOO00000OO ,text ="Encrypt",command =O00O00O00OOO0000O .handle_file ,bg ="#007BFF",fg ="black",font =("Helvetica",12 ),activebackground ="#0056b3",activeforeground ="black",width =10 ,padx =10 ,pady =5 ).grid (row =0 ,column =1 ,padx =5 )#line:33
        Button (OO0O0OOOOO00000OO ,text ="Close",command =O00O00O00OOO0000O .root .quit ,bg ="#DC3545",fg ="black",font =("Helvetica",12 ),activebackground ="#A71D2A",activeforeground ="black",width =10 ,padx =10 ,pady =5 ).grid (row =0 ,column =2 ,padx =5 )#line:36
        O00O00O00OOO0000O .status_label =Label (O00O00O00OOO0000O .root ,text ="",fg ="darkgreen",bg ="#FFFFFF",font =("Helvetica",10 ,"italic"))#line:38
        O00O00O00OOO0000O .status_label .pack (pady =10 )#line:39
    def select_file (O00OOO0OO0O0O0000 ):#line:41
        OOO0000O00000OOO0 =filedialog .askopenfilename (filetypes =[("Text Files","*.txt"),("Markdown Files","*.md"),("All Files","*.*")])#line:42
        if OOO0000O00000OOO0 :#line:43
            O00OOO0OO0O0O0000 .file_entry .delete (0 ,"end")#line:44
            O00OOO0OO0O0O0000 .file_entry .insert (0 ,OOO0000O00000OOO0 )#line:45
            O00OOO0OO0O0O0000 .set_status (f"Selected file: {os.path.basename(OOO0000O00000OOO0)}","darkgreen")#line:46
    def handle_file (O0O000OO00OO0OO0O ):#line:48
        OOOO00OOO000O00O0 =O0O000OO00OO0OO0O .file_entry .get ()#line:49
        if not OOOO00OOO000O00O0 :#line:50
            O0O000OO00OO0OO0O .set_status ("No file selected. Please select a file and try again.","red")#line:51
            return #line:52
        if not os .path .exists (OOOO00OOO000O00O0 ):#line:54
            O0O000OO00OO0OO0O .set_status (f"The file '{OOOO00OOO000O00O0}' does not exist.","red")#line:55
            return #line:56
        with open (OOOO00OOO000O00O0 ,'r')as OOOOO0OO000OO0OOO :#line:59
            O000O00O0OOOOOOOO =OOOOO0OO000OO0OOO .read ()#line:60
        if O000O00O0OOOOOOOO .startswith ("ENCRYPTED (OFFSET="):#line:62
            O0O000OO00OO0OO0O .set_status (f"The file is already encrypted.","red")#line:63
        else :#line:64
            O0O000OO00OO0OO0O .encrypt_file (OOOO00OOO000O00O0 )#line:65
    @staticmethod #line:67
    def generate_date ():#line:68
        O00O0OOOOOO000000 =datetime .now ()#line:69
        return int (O00O0OOOOOO000000 .strftime ("%m%d%Y"))#line:70
    @staticmethod #line:72
    def calculate_shift_from_key (O00OO00OOOO0OO0OO ):#line:73
        return sum (int (OOOOOOOOOOO0000O0 )for OOOOOOOOOOO0000O0 in str (O00OO00OOOO0OO0OO ))%26 #line:74
    @staticmethod #line:76
    def caesar_cipher (OO0OO00O000OOOO0O ,O000000OO00O0OO0O ):#line:77
        O00OO00000O000000 =[]#line:78
        for O0O00000OO0O0O00O in OO0OO00O000OOOO0O :#line:79
            if O0O00000OO0O0O00O .isalpha ():#line:80
                O000OO0OOOO0OOOOO =ord ('A')if O0O00000OO0O0O00O .isupper ()else ord ('a')#line:81
                O0O0OOOO00000OOOO =chr ((ord (O0O00000OO0O0O00O )-O000OO0OOOO0OOOOO +O000000OO00O0OO0O )%26 +O000OO0OOOO0OOOOO )#line:82
                O00OO00000O000000 .append (O0O0OOOO00000OOOO )#line:83
            else :#line:84
                O00OO00000O000000 .append (O0O00000OO0O0O00O )#line:85
        return ''.join (O00OO00000O000000 )#line:86
    def encrypt_file (O0OO000O000OOO0OO ,OO000O0OO00OOOOOO ):#line:88
        try :#line:89
            with open (OO000O0OO00OOOOOO ,'r')as O0OOOO0000OO0OOO0 :#line:90
                OO0O000OO0O00OOOO =O0OOOO0000OO0OOO0 .read ()#line:91
            O0000O0000000O0O0 =O0OO000O000OOO0OO .generate_date ()#line:92
            O0OOO0000O0O00O0O =O0000O0000000O0O0 -151212 #line:93
            OO00000O00O00O00O =O0OO000O000OOO0OO .calculate_shift_from_key (O0000O0000000O0O0 )#line:96
            O0O00OO00O0O00OO0 =O0OO000O000OOO0OO .caesar_cipher (OO0O000OO0O00OOOO ,OO00000O00O00O00O )#line:97
            O0O00OO00O0O00OO0 =f"ENCRYPTED (OFFSET={O0OOO0000O0O00O0O}):\n{O0O00OO00O0O00OO0}"#line:98
            with open (OO000O0OO00OOOOOO ,'w')as O0OOOO0000OO0OOO0 :#line:100
                O0OOOO0000OO0OOO0 .write (O0O00OO00O0O00OO0 )#line:101
            O0OO000O000OOO0OO .set_status (f"Success: The file  has been encrypted successfully.","darkgreen")#line:103
        except Exception as OO00OOO000O0OO000 :#line:104
            O0OO000O000OOO0OO .set_status (f"Error: Could not encrypt . {OO00OOO000O0OO000}","red")#line:105
    def set_status (OOOOO0OOOOO0000OO ,OO000OOOO0OOO0000 ,O0O00O0000O00OO0O ):#line:107
        ""#line:108
        OOOOO0OOOOO0000OO .status_label .config (text =OO000OOOO0OOO0000 ,fg =O0O00O0000O00OO0O )#line:109

def main ():#line:112
    OOOOOOOOOOO00OO0O =Tk ()#line:113
    O00O00O0O0OOO000O =FileEncryptionTool (OOOOOOOOOOO00OO0O )#line:114
    OOOOOOOOOOO00OO0O .mainloop ()#line:115
if __name__ =="__main__":#line:118
    main ()