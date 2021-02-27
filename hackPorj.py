from tkinter import *

master = Tk()

topBarColor = "#ffffff"

infoColor1 = "#a0eefd"

infoColor = infoColor1


sideBarColor = "#fd89ea"
mainPageColor = "#f0f0f0"
mainContentsColor = "#ffffff"
sideBarButtonColor = ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",
                    "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",]

mainPageButtonColor = ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",
                    "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",]

contentBoxButtonColor = ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",
                    "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",]

topBarButtonColor = ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",
                    "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff",]

themeColor1 = ["#E8D0A9", "#B7AFA3", "#C1DAD6", "#F5FAFA", "#ACD1E9", "#6D929B"]
themeColor2 = ["#217C7E", "#F3EFE0", "#3399FF", "#9A3334"]
themeColor3 = ["#B96A9A", "#D889B8", "#9CC089", "#D8F3C9", "#FDE8D7", "#FFFFFF"]
themeColor4 = ["#443266", "#C3C3E5", "#F1F0FF", "#8C489F"]
themeColor5 = ["#C6C78C", "#E7C39C", "#E7DF9C", "#DEE79C","#EFEBD6"]
themeColor6 = ["#000000", "#2956B2", "#659CEF", "#7DBD00", "#DCF600", "#FF5B00"]
themeColor7 = ["#000044", "#555555", "#444444", "#333333"]
themeColor8 = ["#668E39", "#96B566", "#BCE27F", "#7C7C7C", "#C3C3C3", "#F6FF97"]
themeColor9 = ["#004489", "#E1E1D6", "#D3D9DF", "#989898", "#565656", "#DBDBCE"]
themeColor10 = ["#FFBE00", "#9DD52A", "#AC54AA", "#666666", "#000000"]

topBarUserColor = ["#000000"]
sideBarUserColor = ["#000000"]
mainPageUserColor = ["#000000"]
contentBoxUserColor = ["#000000"]
fontColor = ["#5A5A5A"]
###############################################################################

def btnForTopColorButton1():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[0])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[0]))
def btnForTopColorButton2():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[1])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[1]))
def btnForTopColorButton3():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[2])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[2]))
def btnForTopColorButton4():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[3])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[3]))
def btnForTopColorButton5():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[4])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[4]))
def btnForTopColorButton6():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[5])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[5]))
def btnForTopColorButton7():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[6])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[6]))
def btnForTopColorButton8():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[7])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[7]))
def btnForTopColorButton9():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[8])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[8]))
def btnForTopColorButton10():
    topbarCanvas.itemconfigure(topBar, fill = topBarButtonColor[9])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",topBarButtonColor[9]))
    
###############################################################################
def btnForSideColorButton1():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[0], outline = sideBarButtonColor[0])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[0]))
def btnForSideColorButton2():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[1], outline = sideBarButtonColor[1])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[1]))
def btnForSideColorButton3():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[2], outline = sideBarButtonColor[2])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[2]))
def btnForSideColorButton4():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[3], outline = sideBarButtonColor[3])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[3]))
def btnForSideColorButton5():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[4], outline = sideBarButtonColor[4])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[4]))
def btnForSideColorButton6():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[5], outline = sideBarButtonColor[5])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[5]))
def btnForSideColorButton7():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[6], outline = sideBarButtonColor[6])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[6]))
def btnForSideColorButton8():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[7], outline = sideBarButtonColor[7])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[7]))
def btnForSideColorButton9():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[8], outline = sideBarButtonColor[8])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[8]))
def btnForSideColorButton10():
    label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
    label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
    label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
    label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
    label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
    label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
    label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
    label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
    label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
    label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
    label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
    label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))
    w.itemconfigure(sideBar, fill = sideBarButtonColor[9], outline = sideBarButtonColor[9])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",sideBarButtonColor[9]))
    
###############################################################################
def btnForMainPageColorButton1():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[0], outline = mainPageButtonColor[0])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[0]))
def btnForMainPageColorButton2():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[1], outline = mainPageButtonColor[1])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[1]))
def btnForMainPageColorButton3():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[2], outline = mainPageButtonColor[2])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[2]))
def btnForMainPageColorButton4():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[3], outline = mainPageButtonColor[3])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[3]))
def btnForMainPageColorButton5():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[4], outline = mainPageButtonColor[4])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[4]))
def btnForMainPageColorButton6():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[5], outline = mainPageButtonColor[5])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[5]))
def btnForMainPageColorButton7():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[6], outline = mainPageButtonColor[6])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[6]))
def btnForMainPageColorButton8():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[7], outline = mainPageButtonColor[7])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[7]))
def btnForMainPageColorButton9():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[8], outline = mainPageButtonColor[8])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[8]))
def btnForMainPageColorButton10():
    w.itemconfigure(mainPage, fill = mainPageButtonColor[9], outline = mainPageButtonColor[9])
    canvas5.itemconfigure(printMainPageColor, text = ("Mainpage :",mainPageButtonColor[9]))

###############################################################################
def btnForContentBoxColorButton1():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[0], outline = contentBoxButtonColor[0])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[0], outline = contentBoxButtonColor[0])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[0], outline = contentBoxButtonColor[0])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[0], outline = contentBoxButtonColor[0])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[0]))
def btnForContentBoxColorButton2():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[1], outline = contentBoxButtonColor[1])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[1], outline = contentBoxButtonColor[1])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[1], outline = contentBoxButtonColor[1])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[1], outline = contentBoxButtonColor[1])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[1]))
def btnForContentBoxColorButton3():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[2], outline = contentBoxButtonColor[2])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[2], outline = contentBoxButtonColor[2])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[2], outline = contentBoxButtonColor[2])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[2], outline = contentBoxButtonColor[2])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[2]))
def btnForContentBoxColorButton4():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[3], outline = contentBoxButtonColor[3])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[3], outline = contentBoxButtonColor[3])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[3], outline = contentBoxButtonColor[3])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[3], outline = contentBoxButtonColor[3])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[3]))
def btnForContentBoxColorButton5():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[4], outline = contentBoxButtonColor[4])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[4], outline = contentBoxButtonColor[4])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[4], outline = contentBoxButtonColor[4])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[4], outline = contentBoxButtonColor[4])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[4]))
def btnForContentBoxColorButton6():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[5], outline = contentBoxButtonColor[5])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[5], outline = contentBoxButtonColor[5])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[5], outline = contentBoxButtonColor[5])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[5], outline = contentBoxButtonColor[5])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[5]))
def btnForContentBoxColorButton7():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[6], outline = contentBoxButtonColor[6])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[6], outline = contentBoxButtonColor[6])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[6], outline = contentBoxButtonColor[6])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[6], outline = contentBoxButtonColor[6])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[6]))
def btnForContentBoxColorButton8():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[7], outline = contentBoxButtonColor[7])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[7], outline = contentBoxButtonColor[7])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[7], outline = contentBoxButtonColor[7])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[7], outline = contentBoxButtonColor[7])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[7]))
def btnForContentBoxColorButton9():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[8], outline = contentBoxButtonColor[8])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[8], outline = contentBoxButtonColor[8])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[8], outline = contentBoxButtonColor[8])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[8], outline = contentBoxButtonColor[8])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[8]))
def btnForContentBoxColorButton10():
    photo1= PhotoImage(file="1.png")
    w.create_image(301, 297, image = photo1)
    label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
    label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))
    photo2= PhotoImage(file="2.png")
    w.create_image(301, 532, image = photo2)
    label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
    label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))
    photo3= PhotoImage(file="3.png")
    w.create_image(550, 297, image = photo3)
    label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
    label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))
    photo4= PhotoImage(file="4.png")
    w.create_image(550, 532, image = photo4)
    label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
    label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))
    w.itemconfigure(mainContentBox1, fill = contentBoxButtonColor[9], outline = contentBoxButtonColor[9])
    w.itemconfigure(mainContentBox2, fill = contentBoxButtonColor[9], outline = contentBoxButtonColor[9])
    w.itemconfigure(mainContentBox3, fill = contentBoxButtonColor[9], outline = contentBoxButtonColor[9])
    w.itemconfigure(mainContentBox4, fill = contentBoxButtonColor[9], outline = contentBoxButtonColor[9])
    canvas5.itemconfigure(printContentBoxColor, text = ("Content :",contentBoxButtonColor[9]))

###############################################################################

framex = Frame(master)
framex.pack(fill=BOTH)

xscrollbar = Scrollbar(framex, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(framex)
yscrollbar.grid(row=0, column=1, sticky=N+S)

w = Canvas(framex, width=1000, height=700, scrollregion=(0, 0, 1000, 900),
                xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
w.grid(row=0, column=0, sticky=N+S+E+W)

xscrollbar.config(command=w.xview)
yscrollbar.config(command=w.yview)

photo5= PhotoImage(file="5.png")
label5= Label(master, image=photo5)
label5.place(x=0,y=30)

topbarFrame = Frame(w)
topbarFrame.place(x=0, y=0, width=700, height = 30)
topbarCanvas = Canvas(topbarFrame, bg = "white", width=700, height = 30)
topbarCanvas.pack()

topBar = topbarCanvas.create_rectangle(0, 0, 700, 30, fill= topBarColor,
                         outline = topBarColor)
topBarText = topbarCanvas.create_text(350,15,fill="darkblue",font=('Helvetica', 10),
                        text="I Love Coding♥")


sideBar = w.create_rectangle(0, 190, 150, 900, fill= sideBarColor,
                              outline = sideBarColor)



mainPage = w.create_rectangle(150, 190, 700, 900, fill= mainPageColor,
                              outline = mainPageColor)

mainContentBox1 = w.create_rectangle(200, 227, 400, 427, fill= mainContentsColor,
                              outline = mainContentsColor)

mainContentBox2 = w.create_rectangle(450, 227, 650, 427, fill= mainContentsColor,
                              outline = mainContentsColor)

mainContentBox3 = w.create_rectangle(200, 464, 400, 664, fill= mainContentsColor,
                              outline = mainContentsColor)

mainContentBox4 = w.create_rectangle(450, 464, 650, 664, fill= mainContentsColor,
                              outline = mainContentsColor)

label21=w.create_text(10,220,fill=fontColor,text="Notice", anchor = "w",
                     font=('Helvetica', 12))
label22=w.create_text(10,250,fill=fontColor,text="New Post", anchor = "w",
                     font=('Helvetica', 12))
label23=w.create_text(10,280,fill=fontColor,text="Popular Post", anchor = "w",
                     font=('Helvetica', 12))
label11=w.create_text(10,310,fill=fontColor,text="Category", anchor = "w",
                     font=('Helvetica', 12))
label12=w.create_text(20,340,fill=fontColor,text="▷ Business", anchor = "w",
                     font=('Helvetica', 12))
label13=w.create_text(20,370,fill=fontColor,text="▷ Picture", anchor = "w",
                     font=('Helvetica', 12))
label14=w.create_text(20,400,fill=fontColor,text="▷ Movie", anchor = "w",
                     font=('Helvetica', 12))
label15=w.create_text(20,430,fill=fontColor,text="▷ Music", anchor = "w",
                     font=('Helvetica', 12))
label16=w.create_text(20,460,fill=fontColor,text="▷ Design", anchor = "w",
                     font=('Helvetica', 12))
label17=w.create_text(20,490,fill=fontColor,text="▷ Event", anchor = "w",
                     font=('Helvetica', 12))
label18=w.create_text(20,520,fill=fontColor,text="▷ Fashion", anchor = "w",
                     font=('Helvetica', 12))
label19=w.create_text(10,550,fill=fontColor,text="Community", anchor = "w",
                     font=('Helvetica', 12))

photo1= PhotoImage(file="1.png")
w.create_image(301, 297, image = photo1)

label6=w.create_text(300,385,fill=fontColor,text="The Ultimate Guide to Millennial",
                     font=('Helvetica', 10))
label61=w.create_text(300,405,fill=fontColor,text="Marketing",
                     font=('Helvetica', 10))

photo2= PhotoImage(file="2.png")
w.create_image(301, 532, image = photo2)

label7=w.create_text(300,615,fill=fontColor,text="How to Use Instagram Ad",
                     font=('Helvetica', 10))
label71=w.create_text(300,635,fill=fontColor,text="[and How Much Do They Cost]",
                     font=('Helvetica', 10))

photo3= PhotoImage(file="3.png")
w.create_image(550, 297, image = photo3)

label8=w.create_text(550,385,fill=fontColor,text="How RankBrain Work",
                     font=('Helvetica', 10))
label81=w.create_text(550,405,fill=fontColor,text="[And Why You Need to Jump On]",
                     font=('Helvetica', 10))

photo4= PhotoImage(file="4.png")
w.create_image(550, 532, image = photo4)

label9=w.create_text(550,615,fill=fontColor,text="How to Increase Your Traffic",
                     font=('Helvetica', 10))
label91=w.create_text(550,635,fill=fontColor,text="Through Content Translation",
                     font=('Helvetica', 10))

label10=w.create_text(425,700,fill=fontColor,text="←Prev      ||      next→",
                     font=('Helvetica', 10))
label11=w.create_text(425,750,fill=fontColor,text="Team│ YoonByungJin",
                     font=('Helvetica', 10))
label12=w.create_text(425,765,fill=fontColor,text="Tel│ 010)7129-4492",
                     font=('Helvetica', 10))
label13=w.create_text(425,780,fill=fontColor,text="      010)5883-6562",
                     font=('Helvetica', 10))
label14=w.create_text(425,795,fill=fontColor,text="Mail│ bjpark0506@naver.com",
                     font=('Helvetica', 10))
label17=w.create_text(425,840,fill=fontColor,text="Page_Design Copyright ⓒ. All rights Reserved.",
                     font=('Helvetica', 10))

###############################################################################
controllerFrame = Frame(w)
controllerFrame.place(x=710, y=0, width=290, height = 700)

canvas5 = Canvas(controllerFrame, bg = "black", width=290, height = 700)
canvas5.pack()

colorControlBox = canvas5.create_rectangle(0, 0, 290, 700, fill= "black",
                              outline = "black")

canvas5.create_text(145,15,fill="white",font=('Helvetica', 15),
              text="Color Controller")
canvas5.create_line(0, 35, 290, 35,width = 3, fill ="white")
canvas5.create_text(70, 60, fill = "white", font=('Helvetica', 12),
              text="Theme Color")
canvas5.create_line(0, 170, 290, 170,width = 3, fill ="white")
canvas5.create_text(155,185,fill="white",font=('Helvetica', 15),
              text="Detail Colors")
canvas5.create_text(70, 220, fill = "white", font=('Helvetica', 12),
              text="Top Bar Color")
canvas5.create_text(70, 300, fill = "white", font=('Helvetica', 12),
              text="Side Bar Color")
canvas5.create_text(75, 380, fill = "white", font=('Helvetica', 12),
              text="Main Page Color")
canvas5.create_text(75, 460, fill = "white", font=('Helvetica', 12),
              text="ContentBox Color")

printTopBarColor = canvas5.create_text(80, 650, fill = "white",
                                 font=('Helvetica', 9),
                                 text=("TopBar :", topBarColor))
printSideBarColor = canvas5.create_text(225, 650, fill = "white",
                                 font=('Helvetica', 9),
                                 text=("SideBar :", sideBarColor))
printMainPageColor = canvas5.create_text(80, 670, fill = "white",
                                 font=('Helvetica', 9),
                                 text=("Mainpage :", mainPageColor))
printContentBoxColor = canvas5.create_text(225, 670, fill = "white",
                                 font=('Helvetica', 9),
                                 text=("ContentBox :", mainContentsColor))
##############################################################################
def btnForTopBarUserColorButton():
    topbarCanvas.itemconfigure(topBar, fill = topBarUserColor[0],
                    outline = topBarUserColor[0])
    canvas5.itemconfigure(printTopBarColor, text = ("TopBar :",
                                                      topBarUserColor[0]))

TopBarUserColorFrame = Frame(w, background ="white")
TopBarUserColorFrame.place(x=945, y=210, width=25, height = 25)
TopBarUserColorButton = Button(TopBarUserColorFrame, width = 2, height = 1,
                         command = btnForTopBarUserColorButton,
                            bg =topBarUserColor[0])
TopBarUserColorButton.place(x= 1, y=0)

inputColorFrame = Frame(w, background ="white")
inputColorFrame.place(x=735, y=540, width=227, height = 60)

entry1 = Entry(inputColorFrame, width = 30, bg = "white")
entry1.place(x=0,y=0, height = 25)


def btnForTopBarUserColorButton():
    topBarUserColor[0] = entry1.get()
    TopBarUserColorButton.configure(bg = topBarUserColor[0])
    
inputTopBarButton = Button(inputColorFrame, width = 7,
                         command = btnForTopBarUserColorButton,
                            bg ="light gray", text = "TopBar")
inputTopBarButton.place(x= 1, y=23, height = 37)




def btnForSideBarUserColorButton():
    w.itemconfigure(sideBar, fill = sideBarUserColor[0], outline = sideBarUserColor[0])
    print(sideBarUserColor[0])
    canvas5.itemconfigure(printSideBarColor, text = ("SideBar :",
                                                      sideBarUserColor[0]))

SideBarUserColorFrame = Frame(w, background ="white")
SideBarUserColorFrame.place(x=945, y=290, width=25, height = 25)
SideBarUserColorButton = Button(SideBarUserColorFrame, width = 2, height = 1,
                         command = btnForSideBarUserColorButton,
                            bg =sideBarUserColor)
SideBarUserColorButton.place(x= 1, y=0)

def btnForSideBarUserColorButton():
    sideBarUserColor[0] = entry1.get()
    print(sideBarUserColor[0])
    SideBarUserColorButton.configure(bg = sideBarUserColor[0])
    
inputSideBarButton = Button(inputColorFrame, width = 7,
                         command = btnForSideBarUserColorButton,
                            bg ="light gray", text = "SideBar")
inputSideBarButton.place(x= 56, y=23, height = 37)




def btnForMainPageUserColorButton():
    w.itemconfigure(mainPage, fill = mainPageUserColor[0],
                    outline = mainPageUserColor[0])
    canvas5.itemconfigure(printMainPageColor, text = ("MainPage :",
                                                      mainPageUserColor[0]))

MainPageUserColorFrame = Frame(w, background ="white")
MainPageUserColorFrame.place(x=945, y=370, width=25, height = 25)
MainPageUserColorButton = Button(MainPageUserColorFrame, width = 2, height = 1,
                         command = btnForMainPageUserColorButton,
                            bg =mainPageUserColor[0])
MainPageUserColorButton.place(x= 1, y=0)

def btnForMainPageUserColorButton():
    mainPageUserColor[0] = entry1.get()
    MainPageUserColorButton.configure(bg = mainPageUserColor[0])
    
inputMainPageButton = Button(inputColorFrame, width = 7,
                         command = btnForMainPageUserColorButton,
                            bg ="light gray", text = "Main")
inputMainPageButton.place(x= 113, y=23, height = 37)



def btnForContentBoxUserColorButton():
    w.itemconfigure(mainContentBox1, fill = contentBoxUserColor[0], outline = contentBoxUserColor[0])
    w.itemconfigure(mainContentBox2, fill = contentBoxUserColor[0], outline = contentBoxUserColor[0])
    w.itemconfigure(mainContentBox3, fill = contentBoxUserColor[0], outline = contentBoxUserColor[0])
    w.itemconfigure(mainContentBox4, fill = contentBoxUserColor[0], outline = contentBoxUserColor[0])
    canvas5.itemconfigure(printContentBoxColor, text = ("ContentBox :",
                                                      contentBoxUserColor[0]))

ContentBoxUserColorFrame = Frame(w, background ="white")
ContentBoxUserColorFrame.place(x=945, y=450, width=25, height = 25)
ContentBoxUserColorButton = Button(ContentBoxUserColorFrame, width = 2, height = 1,
                         command = btnForContentBoxUserColorButton,
                            bg =contentBoxUserColor[0])
ContentBoxUserColorButton.place(x= 1, y=0)

def btnForContextBoxUserColorButton():
    contentBoxUserColor[0] = entry1.get()
    ContentBoxUserColorButton.configure(bg = contentBoxUserColor[0])
    
inputContextBoxButton = Button(inputColorFrame, width = 7,
                         command = btnForContextBoxUserColorButton,
                            bg ="light gray", text = "Content")
inputContextBoxButton.place(x= 169, y=23, height = 37)


###############################################################################
TopBarColorFrame = Frame(w, background ="white")
TopBarColorFrame.place(x=730, y=240, width=240, height = 25)

TopBarColorButton1 = Button(TopBarColorFrame, width = 2, height = 1,
                         command = btnForTopColorButton1,
                            bg =topBarButtonColor[0]) 
TopBarColorButton1.place(x= 0, y=0)
TopBarColorButton2 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton2,
                         bg =topBarButtonColor[1])
TopBarColorButton2.place(x= 24, y=0)
TopBarColorButton3 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton3,
                         bg =topBarButtonColor[2]) 
TopBarColorButton3.place(x= 48, y=0)
TopBarColorButton4 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton4,
                         bg =topBarButtonColor[3]) 
TopBarColorButton4.place(x= 72, y=0)
TopBarColorButton5 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton5,
                         bg =topBarButtonColor[4]) 
TopBarColorButton5.place(x= 96, y=0)
TopBarColorButton6 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton6,
                         bg =topBarButtonColor[5]) 
TopBarColorButton6.place(x= 120, y=0)
TopBarColorButton7 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton7,
                         bg =topBarButtonColor[6]) 
TopBarColorButton7.place(x= 144, y=0)
TopBarColorButton8 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton8,
                         bg =topBarButtonColor[7]) 
TopBarColorButton8.place(x= 168, y=0)
TopBarColorButton9 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton9,
                         bg =topBarButtonColor[8]) 
TopBarColorButton9.place(x= 192, y=0)
TopBarColorButton10 = Button(TopBarColorFrame, width = 2, height = 1,
                        command = btnForTopColorButton10,
                         bg =topBarButtonColor[9])
TopBarColorButton10.place(x= 216, y=0)



################################################################################
SideBarColorFrame = Frame(w, background ="white")
SideBarColorFrame.place(x=730, y=320, width=240, height = 25)

SideBarColorButton1 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton1,
                         bg =sideBarButtonColor[0]) 
SideBarColorButton1.place(x= 0, y=0)
SideBarColorButton2 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton2,
                         bg =sideBarButtonColor[1])
SideBarColorButton2.place(x= 24, y=0)
SideBarColorButton3 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton3,
                         bg =sideBarButtonColor[2]) 
SideBarColorButton3.place(x= 48, y=0)
SideBarColorButton4 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton4,
                         bg =sideBarButtonColor[3]) 
SideBarColorButton4.place(x= 72, y=0)
SideBarColorButton5 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton5,
                         bg =sideBarButtonColor[4]) 
SideBarColorButton5.place(x= 96, y=0)
SideBarColorButton6 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton6,
                         bg =sideBarButtonColor[5]) 
SideBarColorButton6.place(x= 120, y=0)
SideBarColorButton7 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton7,
                         bg =sideBarButtonColor[6]) 
SideBarColorButton7.place(x= 144, y=0)
SideBarColorButton8 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton8,
                         bg =sideBarButtonColor[7]) 
SideBarColorButton8.place(x= 168, y=0)
SideBarColorButton9 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton9,
                         bg =sideBarButtonColor[8]) 
SideBarColorButton9.place(x= 192, y=0)
SideBarColorButton10 = Button(SideBarColorFrame, width = 2, height = 1,
                        command = btnForSideColorButton10,
                         bg =sideBarButtonColor[9])
SideBarColorButton10.place(x= 216, y=0)

###############################################################################
MainPageColorFrame = Frame(w, background ="white")
MainPageColorFrame.place(x=730, y=400, width=240, height = 25)

mainPageColorButton1 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton1,
                         bg =mainPageButtonColor[0]) 
mainPageColorButton1.place(x= 0, y=0)
mainPageColorButton2 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton2,
                         bg =mainPageButtonColor[1])
mainPageColorButton2.place(x= 24, y=0)
mainPageColorButton3 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton3,
                         bg =mainPageButtonColor[2]) 
mainPageColorButton3.place(x= 48, y=0)
mainPageColorButton4 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton4,
                         bg =mainPageButtonColor[3]) 
mainPageColorButton4.place(x= 72, y=0)
mainPageColorButton5 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton5,
                         bg =mainPageButtonColor[4]) 
mainPageColorButton5.place(x= 96, y=0)
mainPageColorButton6 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton6,
                         bg =mainPageButtonColor[5]) 
mainPageColorButton6.place(x= 120, y=0)
mainPageColorButton7 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton7,
                         bg =mainPageButtonColor[6]) 
mainPageColorButton7.place(x= 144, y=0)
mainPageColorButton8 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton8,
                         bg =mainPageButtonColor[7]) 
mainPageColorButton8.place(x= 168, y=0)
mainPageColorButton9 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton9,
                         bg =mainPageButtonColor[8]) 
mainPageColorButton9.place(x= 192, y=0)
mainPageColorButton10 = Button(MainPageColorFrame, width = 2, height = 1,
                        command = btnForMainPageColorButton10,
                         bg =mainPageButtonColor[9])
mainPageColorButton10.place(x= 216, y=0)

###############################################################################
ContentBoxColorFrame = Frame(w, background ="white")
ContentBoxColorFrame.place(x=730, y=480, width=240, height = 25)

contentBoxColorButton1 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton1,
                         bg =contentBoxButtonColor[0]) 
contentBoxColorButton1.place(x= 0, y=0)
contentBoxColorButton2 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton2,
                         bg =contentBoxButtonColor[1])
contentBoxColorButton2.place(x= 24, y=0)
contentBoxColorButton3 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton3,
                         bg =contentBoxButtonColor[2]) 
contentBoxColorButton3.place(x= 48, y=0)
contentBoxColorButton4 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton4,
                         bg =contentBoxButtonColor[3]) 
contentBoxColorButton4.place(x= 72, y=0)
contentBoxColorButton5 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton5,
                         bg =contentBoxButtonColor[4]) 
contentBoxColorButton5.place(x= 96, y=0)
contentBoxColorButton6 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton6,
                         bg =contentBoxButtonColor[5]) 
contentBoxColorButton6.place(x= 120, y=0)
contentBoxColorButton7 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton7,
                         bg =contentBoxButtonColor[6]) 
contentBoxColorButton7.place(x= 144, y=0)
contentBoxColorButton8 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton8,
                         bg =contentBoxButtonColor[7]) 
contentBoxColorButton8.place(x= 168, y=0)
contentBoxColorButton9 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton9,
                         bg =contentBoxButtonColor[8]) 
contentBoxColorButton9.place(x= 192, y=0)
contentBoxColorButton10 = Button(ContentBoxColorFrame, width = 2, height = 1,
                        command = btnForContentBoxColorButton10,
                         bg =contentBoxButtonColor[9])
contentBoxColorButton10.place(x= 216, y=0)

###############################################################################
def btnForThemeColor1():
    for i in range(6):
        topBarButtonColor[i] = themeColor1[i]
        sideBarButtonColor[i] = themeColor1[i]
        contentBoxButtonColor[i] = themeColor1[i]
        mainPageButtonColor[i] = themeColor1[i]
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])

    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])

    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])
    
def btnForThemeColor2():
    for i in range(4):
        topBarButtonColor[i] = themeColor2[i]
        sideBarButtonColor[i] = themeColor2[i]
        contentBoxButtonColor[i] = themeColor2[i]
        mainPageButtonColor[i] = themeColor2[i]
        
    for i in range(4,6):
        topBarButtonColor[i] = "#ffffff"
        sideBarButtonColor[i] = "#ffffff"
        contentBoxButtonColor[i] = "#ffffff"
        mainPageButtonColor[i] = "#ffffff"
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])
    
def btnForThemeColor3():
    for i in range(6):
        topBarButtonColor[i] = themeColor3[i]
        sideBarButtonColor[i] = themeColor3[i]
        contentBoxButtonColor[i] = themeColor3[i]
        mainPageButtonColor[i] = themeColor3[i]
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor4():
    for i in range(4):
        topBarButtonColor[i] = themeColor4[i]
        sideBarButtonColor[i] = themeColor4[i]
        contentBoxButtonColor[i] = themeColor4[i]
        mainPageButtonColor[i] = themeColor4[i]
        
    for i in range(4,6):
        topBarButtonColor[i] = "#ffffff"
        sideBarButtonColor[i] = "#ffffff"
        contentBoxButtonColor[i] = "#ffffff"
        mainPageButtonColor[i] = "#ffffff"
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor5():
    for i in range(5):
        topBarButtonColor[i] = themeColor5[i]
        sideBarButtonColor[i] = themeColor5[i]
        contentBoxButtonColor[i] = themeColor5[i]
        mainPageButtonColor[i] = themeColor5[i]
    for i in range(5,6):
        topBarButtonColor[i] = "#ffffff"
        sideBarButtonColor[i] = "#ffffff"
        contentBoxButtonColor[i] = "#ffffff"
        mainPageButtonColor[i] = "#ffffff"

        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor6():
    for i in range(6):
        topBarButtonColor[i] = themeColor6[i]
        sideBarButtonColor[i] = themeColor6[i]
        contentBoxButtonColor[i] = themeColor6[i]
        mainPageButtonColor[i] = themeColor6[i]
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])

    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])

    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor7():
    for i in range(4):
        topBarButtonColor[i] = themeColor7[i]
        sideBarButtonColor[i] = themeColor7[i]
        contentBoxButtonColor[i] = themeColor7[i]
        mainPageButtonColor[i] = themeColor7[i]
        
    for i in range(4,6):
        topBarButtonColor[i] = "#ffffff"
        sideBarButtonColor[i] = "#ffffff"
        contentBoxButtonColor[i] = "#ffffff"
        mainPageButtonColor[i] = "#ffffff"
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor8():
    for i in range(6):
        topBarButtonColor[i] = themeColor8[i]
        sideBarButtonColor[i] = themeColor8[i]
        contentBoxButtonColor[i] = themeColor8[i]
        mainPageButtonColor[i] = themeColor8[i]
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])

    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])

    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor9():
    for i in range(6):
        topBarButtonColor[i] = themeColor9[i]
        sideBarButtonColor[i] = themeColor9[i]
        contentBoxButtonColor[i] = themeColor9[i]
        mainPageButtonColor[i] = themeColor9[i]
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])

    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])

    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])

def btnForThemeColor10():
    for i in range(4):
        topBarButtonColor[i] = themeColor10[i]
        sideBarButtonColor[i] = themeColor10[i]
        contentBoxButtonColor[i] = themeColor10[i]
        mainPageButtonColor[i] = themeColor10[i]
        
    for i in range(5,6):
        topBarButtonColor[i] = "#ffffff"
        sideBarButtonColor[i] = "#ffffff"
        contentBoxButtonColor[i] = "#ffffff"
        mainPageButtonColor[i] = "#ffffff"
        
    TopBarColorButton1.configure(bg = topBarButtonColor[0])
    TopBarColorButton2.configure(bg = topBarButtonColor[1])
    TopBarColorButton3.configure(bg = topBarButtonColor[2])
    TopBarColorButton4.configure(bg = topBarButtonColor[3])
    TopBarColorButton5.configure(bg = topBarButtonColor[4])
    TopBarColorButton6.configure(bg = topBarButtonColor[5])
    
    SideBarColorButton1.configure(bg = sideBarButtonColor[0])
    SideBarColorButton2.configure(bg = sideBarButtonColor[1])
    SideBarColorButton3.configure(bg = sideBarButtonColor[2])
    SideBarColorButton4.configure(bg = sideBarButtonColor[3])
    SideBarColorButton5.configure(bg = sideBarButtonColor[4])
    SideBarColorButton6.configure(bg = sideBarButtonColor[5])

    mainPageColorButton1.configure(bg = mainPageButtonColor[0])
    mainPageColorButton2.configure(bg = mainPageButtonColor[1])
    mainPageColorButton3.configure(bg = mainPageButtonColor[2])
    mainPageColorButton4.configure(bg = mainPageButtonColor[3])
    mainPageColorButton5.configure(bg = mainPageButtonColor[4])
    mainPageColorButton6.configure(bg = mainPageButtonColor[5])
    
    contentBoxColorButton1.configure(bg = contentBoxButtonColor[0])
    contentBoxColorButton2.configure(bg = contentBoxButtonColor[1])
    contentBoxColorButton3.configure(bg = contentBoxButtonColor[2])
    contentBoxColorButton4.configure(bg = contentBoxButtonColor[3])
    contentBoxColorButton5.configure(bg = contentBoxButtonColor[4])
    contentBoxColorButton6.configure(bg = contentBoxButtonColor[5])
###############################################################################    

themeColorFrame = Frame(w, background ="white")
themeColorFrame.place(x=730, y=90, width=240, height = 50)

themeColorButton = Button(themeColorFrame, width = 2, height = 1,
                        command = btnForThemeColor1,
                        bg ="#ACD1E9") 
themeColorButton.place(x= 0, y=0)

themeColorButton2 = Button(themeColorFrame, width = 2, height = 1,
                         command = btnForThemeColor2,
                           bg = "#217C7E")
themeColorButton2.place(x= 24, y=0)
themeColorButton3 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor3,
                           bg = "#B96A9A") 
themeColorButton3.place(x= 48, y=0)

themeColorButton4 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor4,
                           bg = "#443266") 
themeColorButton4.place(x= 72, y=0)

themeColorButton5 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor5,
                           bg = "#C6C78C") 
themeColorButton5.place(x= 96, y=0)

themeColorButton6 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor6,
                           bg = "#000000")
themeColorButton6.place(x= 120, y=0)

themeColorButton7 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor7,
                           bg = "#000044")
themeColorButton7.place(x= 144, y=0)

themeColorButton8 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor8,
                           bg = "#668E39")
themeColorButton8.place(x= 168, y=0)

themeColorButton9 = Button(themeColorFrame, width = 2, height = 1,
                           command = btnForThemeColor9,
                           bg = "#004489")
themeColorButton9.place(x= 192, y=0)

themeColorButton10 = Button(themeColorFrame, width = 2, height = 1,
                            command = btnForThemeColor10,
                            bg = "#FFBE00")
themeColorButton10.place(x= 216, y=0)

     
mainloop()
