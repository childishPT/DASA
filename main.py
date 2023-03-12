 # author : daniyal karimi , abdollah aali hosseini
import time
import datetime

def closingsequence():
    time.sleep(3)
    print("\n" * 40)
    print("==========================================================")
    print("Data analysis and storage application")
    print("By Daniyal Karimi and Abdollah Aali Hosseini")
    print("==========================================================")
    print("\n" * 40)
    time.sleep(4)
    print("shutting down")
    print("==========================================================")
    quit()

def accessdatabase():
    None

def accessstatsiticalsoftware():
    None

def mainmenu():
    print("\n" * 41)
    print("==========================================================")
    print("Data analysis and storage application")
    print("By Daniyal Karimi and Abdollah Aali Hosseini")
    print("==========================================================")
    print("type the number shown in the brackets to enable the option")
    print("==========================================================")
    print("( 0 ) Quit") 
    print("( 1 ) Access database")
    print("( 2 ) Access statistical analysis software")
    print("==========================================================")
    print("\n" * 5)
    while True:
        try:
            maininputchoice = int(input(">>> "))
            while maininputchoice < 0 or maininputchoice > 2:
                print("ERROR : enter a valid option")
                maininputchoice = int(input(">>> "))
            if maininputchoice == 0:
                closingsequence()
            elif maininputchoice == 1:
                accessdatabase()
            elif maininputchoice == 2:
                accessstatsiticalsoftware()
            break
        except TypeError:
            print("ERROR : enter a integer value ")
    
def startupgraphic():
    print("Hello world")
    print("==========================================================")
    print("\n" * 40)
    time.sleep(2)
    print("==========================================================")
    print("Designed for ease of data analysis and support to help teachers")
    print("A program that incorporates all the wants of a teacher when it comes to stastiscal analysis of student grades")
    print("Dedicated to Mr Rawat")
    print("\n" * 40)
    time.sleep(7)
    print("==========================================================")
    print("Initial idea was discovered 22/05/2021")
    print("Development began on 07/03/2023")
    time.sleep(4)
    print("An Abdollah Aali Hosseini and Daniyal Karimi production")
    time.sleep(3)
    print("==========================================================")
    print("\n" * 40)
    print("Data")
    time.sleep(1)
    print("analysis")
    time.sleep(0.35)
    print("and")
    time.sleep(0.13)
    print("storage")
    time.sleep(2)
    print("application")
    time.sleep(5)
    print("\n" * 41)
    print("The D.A.S.A")
    mainmenu()
startupgraphic()