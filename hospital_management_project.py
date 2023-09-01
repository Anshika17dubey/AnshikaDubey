import pandas as pd
import matplotlib.pyplot as plt
from csv import writer
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:26:00 2020
@author: ANSHIKA DUBEY
"""

print('**************************************************** ')
print("*                                                   *")
print( "       ----- welcome to city life hospital-----     ")
print("*                                                   *")
print("****************************************************")


print("              -----------------------------")
print("               |  Enter 1 for Admin Mode   |")
print("               |  Enter 2 for User Mode    |")
print('              -----------------------------')
print(" ")
print("                          EXIT")

mode = input("Enter Your Mode: ")
if mode == "1" :
    print("#               ADMIN MODE")
    password =input("Enter your password ")
    while True:
     if password == "1729":
        print ("WELCOME TO ADMIN MODE")
     break
    else:
        print(" !!! WRONG PASSWORD !!!")
    print("# ADMIN MODE")
    print ( "      # RUNNING ADMIN MODE")
    print("|To Manage PATIENTS Enter 1|           | To Manage DOCTORS Enter 2") 
    print("|To Manage APPOINTMENTS Enter 3|       |To go back to main menu Enter 4 ")
    admin_options = input ("Enter your choice :-")
    if admin_options  =="1" :
          print("      #ADMINS MODE   --->-  PATIENTS MANAGEMENT")
          print("            ****-----******-----*****-----")
          print("          To add new patients enter 1|\n| |         To display patients enter 2|\n|")
          print("          To delete patients data enter 3|\n|           TO go back enter 4")
          patients_management = input ("Choose Your Option :- ")
          if patients_management == "1": # admin mode --> patients 
                    print(" management --> add new patient")
                    patient_ID = int(input("Enter Patients ID :-"))
                    name = input ("Enter patients name :-")
                    department = input ("Enter Patient's medical history :-")
                    doctor = input ("Enter Doctors Name :- ")
                    age = input ("Enter Patients Age :-")
                    gender = input("Enter Patient's gender :- ")
                    room = int(input("Enter Patient's room no. :-"))
                    date=input("Date of admit:- ")
                    list = [patient_ID, name, department,doctor, age, gender, room,date]
                    
                    with open('patients_project1.csv', 'a') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(list)
                        f_object.close()
                    print ("         --------------***PATIENT ADDED SUCCESSFULLY***-------------")
          elif patients_management == "2": # admin mode -> patients management -> display patient
              patients = pd.read_csv("patients_project1.csv")
              print(patients)
          elif patients_management == "3" : # admin mode -> patients management -> delete patients
             val = int(input("Enter Patients ID :-"))
             df = pd.read_csv('patients_project1.csv', index_col='patient_ID')
             df = df.drop(val)
             df.to_csv('patients_project1.csv', index=True)
             print("       ********** PATIENTS DATA DELETED SUCCESSFULLY **********")
          elif patients_management == "4": # admin mode -> patients management -> GO BACK
              print("             ----------**** # GOING BACK # **** ------------")
              while True:
                  break
              
    elif admin_options == "2":
        print("         #ADMINS MODE ----> DOCTOR'S MANAGEMENT")
        print("            ***-----******-----*****-----")
        print("To add new doctor enter 1 \n To display doctor enter 2")
        print("To delete doctor enter 3 \n To go back enter B")
        doctor_management = input("Enter your option")
        if doctor_management == "1":# admin mode -> doctors managemnt -> to add doctor
             doctor_ID = int(input("Enter Doctor's ID :- "))
             name = input("Enter Doctor's Name :-")
             join = input("Enter date of join :-")
             salary = input("Enter salary :-")
             department = input("Enter Doctor's Department :-")
             doctors = [doctor_ID, name,join,salary, department]
             
             with open('doctor_project1.csv', 'a') as f_object:
                 writer_object = writer(f_object)
                 writer_object.writerow(doctors)
                 f_object.close()
             print("---------------DOCTOR ADDED SUCCESSFULLY----------")
        elif doctor_management == "2":
            doctors = pd.read_csv("doctor_project1.csv")
            print(doctors)
        elif doctor_management == "3":# admin mode -> doctor's management -> delete doctor's data
             x=int(input("Eneter doctor_id to be deletd: "))
             dfx = pd.read_csv('doctor_project1.csv', index_col='Doctor_ID')
             dfx = dfx.drop(x)
             dfx.to_csv('doctor_project1.csv', index=True)
             print("       *** DOCTORS DATA DELETED SUCCESSFULLY ***")
        elif doctor_management == "B":
            print ("BACK TO MAIN MENU")
        else:
             print("          !!! PLEASE ENTER A CORRECT OPTION !!!")
             while True:
                 break
    elif admin_options=="3":
        print("-------****--------****------------****--------------")
        print("To book an appointment enter 1 : ")
        print("to view an appointment enter 2 : ")
        print("to cancel an appointment enter 3 : ")
        appt = input("            ENTER YOUR CHOICE :-")
        if appt == "1":
            name = input("      Enter  Patient's Name :-")
            age = int(input("   Enter Patient's Age :-"))
            date = input("      Enter Appointment Date :-")
            doctor = input("    Enter Doctor's Name :-")
            appt = [name, age, date, doctor]
            
            with open('appointments.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(appt)
                f_object.close()
            print("            APPOINTMENT SAVED SUCCESSFULLY")
        elif appt == "2":
            print("            VIEWING APPOINTMENTS")
            view = pd.read_csv(r"appointments.csv")
            print(view)
        else:
            y=input("Enter name to be deletd: ")
            dfy = pd.read_csv('appointments.csv', index_col='name')
            dfy = dfy.drop(y)
            dfy.to_csv('appointments.csv', index=True)
            print("       ***  ",y,"'s Appointment DELETED SUCCESSFULLY ***")
            
elif mode == "2" :
    print(" #USER MODE")
    password = input ("Please Enter Your Password:-")
    if password == "2917":
        print(" WELCOME TO USER MODE")
        print("Enter 1 to view hospital data")
        print("Enter 2 to view hospital images")
        print("enter 3 to view facilities provided by hospital")
        print("Enter 4 to view corona history of our hospital ")
        print(" ")
        print("              *************************************     ")
        user = input("Enter your option :- ")
        if user == "1":
            print("            ***************************")
            print("   -----------*** SHOWING HosPITAL DATA *** ------------")
            print("ENTER 1  to present data in tabular form")
            print("ENTER 2 to present data in graphical form")
            data = input("ENTER YOUR CHOICE :-")
            if data == "1":
                year = [2008, 2010, 2012, 2014, 2016, 2018, 2020,2021,2022]  
                grade = [34, 15, 35, 29, 18, 33, 40,54,75]
                list=[year,grade]
                df2=pd.DataFrame(list)
                print(df2)
                print("  ** NOTE: This is approximate data and not exact data **")
            if data == "2":
                print(" ENTER A FOR LINE CHART ")
                print(" ENTER B FOR BAR CHART")
                print(" ENTER C FOR PIE CHART")
                plot = input(" enter your plot :-")
                if plot == "A":
                    year = [2008, 2010, 2012, 2014, 2016, 2018, 2020,2021,2022]  
                    grade = [23, 17, 35, 29, 12, 41, 40,54,75] 
                    plt.plot(year, grade)
                    plt.xlabel('YEARS')
                    plt.ylabel('PROGRESS')
                    plt.show()
                    print("  ** NOTE: This is approximate data and not exact data **")
                elif plot == "B":
                    year = [2008, 2010, 2012, 2014, 2016, 2018, 2020,2021,2022]  
                    grade = [23, 17, 35, 29, 12, 41, 40,54,75]
                    plt.bar(year, grade)
                    plt.xlabel('YEARS')
                    plt.ylabel('PROGRESS')
                    plt.show()
                    print("  ** NOTE: This is approximate data and not exact data **")
                elif plot == "C":
                    year = [2008, 2010, 2012, 2014, 2016, 2018, 2020,2021,2022]  
                    grade = [23, 17, 35, 29, 12, 41, 40,54,75]
                    plt.pie(grade, labels = year)
                    plt.show()
                    print("  ** NOTE: This is approximate data and not exact data **")
                else:
                    while True:
                        break
            elif data == "2":
                print()
            else:
                while True:
                    break
                
        elif user ==  "2":
            print("             **************************")
            print("   ------------*** SHOWING HOSPITAL IMAGES ***-----")
            from IPython.display import Image, display
            display(Image(filename = "Screenshot_20201103_131348.jpg", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (135).png", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (136).png", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (137).png", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (138).png", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (139).png", width = 600, height = 500)) 
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (140).png", width = 600, height = 500))
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (141).png",width = 600, height = 500)) 
            from IPython.display import Image, display
            display(Image(filename = "Screenshot (142).png", width = 600, height = 500 )) 
       
        elif user == "3":
            print("            **************************")
            print(" --------------*** FACILITIES PROVIDED BY HOSPITAL *** ------")
            print("                                                                         ")
            print("                24x7 EMERGENCY FACILITY")
            print("                EVERY HALF HOUR CLEANING FACILITY")
            print("                WELL DESIGNED ROOMS AND WARDS ")
            print("                PATHALOGY LAB")
            print("                ALTERED, TIME-TO-TIME VISIT BY DOCTORS AND NURSES")
            print("                COMPLETE MEDICATION FACILITIES")
            print("                MULTITALENTED DOCTORS ")
            print("                24x7 AMBULANCE SERVICE ")
            print("                WELL EQUIPPED OPERATION THEATRES")
            print("                WELL EQUIPPED ICU")
            print("                5 WAITING HALLS ")
            print("                WELL ARRANGED KITCHENS FOR PATIENT'S FOOD")
            print("                2 CANTEENS FOR PATIENTS'S FAMILY MEMBERS")
            print("                FULLY AIR CONDITIONED")
            print("                GOVERNMENT CERTIFIED")
            print("                FOLLOWS ALL RULES & REGULATIONS LAID BY GOVERNMENT")
            print("                                                                           ")
            print("          ----------***---------*****---------------*******----------*****------      ")
        
        elif user == "4":
            print("          ******************************")
            print("                 SHOWING CORONA DETAILS..")
            print("    To View total no. of corona patients in hospital ENTER 1 ")
            print("    To view no. of deaths in corona ENTER 2 ")
            print("    To view recovered patients of corona ENTER 3")
            print("    To view active cases of corona in our hospital ENTER 4 ")
            print("    To view graphical report of corona ENTER 5")
            option = input("    Enter your choice :-")
            if option == "1":
                
                print("      Total no. of patient's in our hospital = 4000")
          
            if option == "2":
                print("      Total no. of deaths of corona patient's in our hospital = 150")
            if option == "3":
                print("      Total no. of recovered patient's in our hospital = 3200.")
            if option == "4":
                print("      Total no. of active cases = 785 ")
            if option == "5":
                print(" ENTER A FOR LINE CHART ")
                print(" ENTER B FOR BAR CHART")
                print(" ENTER C FOR PIE CHART")
                plot = input(" enter your plot :-")
                if plt == "A":
                    stream = ['DEATHS', 'PATIENTS','RECOVERED PATIENTS', 'ACTIVE CASES']
                    value = [150, 4000, 3200, 785]
                    plt.plot(stream, value)
                    plt.xlabel('STREAM')
                    plt.ylabel('VALUE')
                    plt.show()
                elif plot == "B":
                    stream = ['DEATHS', 'PATIENTS','RECOVERED PATIENTS', 'ACTIVE CASES']
                    value = [150, 4000, 3200, 785]
                    plt.bar(stream, value)
                    plt.xlabel('STREAM')
                    plt.ylabel('VALUE')
                    plt.show()
                elif plot == "C":
                    stream = ['DEATHS', 'PATIENTS','RECOVERED PATIENTS', 'ACTIVE CASES']
                    value = [150, 4000, 3200, 785]
                    colors = ['red', 'blue', 'green', 'yellow']
                    explode = (0.6, 0, 0, 0)
                    fig = plt.figure(figsize = (10,7))
                    plt.pie(value, explode=explode, labels=stream, colors=colors)
                    plt.title("     CORONA DETAILS ")
                    plt.show()
        while True:
          break

elif mode=="EXIT":
    print()
    print("                            *** END OF THE PROGRAM *** ") 
    print()   
    print("                        *** THANKS FOR USING OUR SERVICE ***")
    print()
    print("                      *** WE HOPE YOU LIKED OUR SERVICE ***     ")
else:
    print("           WRONG INPUT")
