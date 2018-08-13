from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


#curretly only 4th floorrooms
def reserveRoom(username,password,room,time,length):
    #username, password, room number( 4th flr only letter are capital), time(30minute intervals 7:00 am to 11:00 pm),length(30 60 90 or 120 minutes)
    driver = webdriver.Firefox()
    driver.get("https://library.usu.edu/study_rooms/index.php")
    
    floordrop =Select(driver.find_element_by_id("floor"))
    floordrop.select_by_index(3)#fourth element for 4thfloor
    
    #must find elements after page has changed
    datedrop = Select(driver.find_element_by_name("resdate"))
    datedrop.select_by_index(2)#3days ahead is max
    
    timemap = {}
    timemap["7:00 am"] = 1
    timemap["7:30 am"] = 2
    timemap["8:00 am"] = 3
    timemap["8:30 am"] = 4
    timemap["9:00 am"] = 5
    timemap["9:30 am"] = 6
    timemap["10:00 am"] = 7
    timemap["10:30 am"] =8
    timemap["11:00 am"] = 9
    timemap["11:30 am"] = 10
    timemap["12:00 pm"] = 11
    timemap["12:30 pm"] = 12
    timemap["1:00 pm"] = 13
    timemap["1:30 pm"] = 14
    timemap["2:00 pm"] = 15
    timemap["2:30 pm"] = 16
    timemap["3:00 pm"] = 17
    timemap["3:30 pm"] = 18
    timemap["4:00 pm"] = 19
    timemap["4:30 pm"] = 20
    #table has extra row here
    timemap["5:00 pm"] = 22
    timemap["5:30 pm"] = 23
    timemap["6:00 pm"] = 24
    timemap["6:30 pm"] = 25
    timemap["7:00 pm"] = 26
    timemap["7:30 pm"] = 27
    timemap["8:00 pm"] = 28
    timemap["8:30 pm"] = 29
    timemap["9:00 pm"] = 30
    timemap["9:30 pm"] = 31
    timemap["10:00 pm"] = 32
    timemap["10:30 pm"] = 33
    timemap["11:00 pm"] = 34


    roommap = {}
    roommap["413"]=1
    roommap["414"]=2
    roommap["415"]=3
    roommap["416"]=4
    roommap["417"]=5
    roommap["418F"]=6
    roommap["418K"]=7
    roommap["419"]=8
    roommap["420"]=9
    
    
    
    #get the whole table
    resTable =driver.find_element_by_id("resTable")
    #create an array of the rows
    resTableRows= resTable.find_elements_by_tag_name("tr")
    #select a spefic row make an array of its elments row is not o indexed becuas eof table labeles
    #time slection
    currentCol=resTableRows[timemap[time]].find_elements_by_tag_name("td")
    #select the nth term no zero indexed
    #room selection
    desiredspot= currentCol[roommap[room]]
    #need to click on the span part of the td
    target=desiredspot.find_element_by_tag_name("span")
    target.click()
    
    #new page
    
    
    usernamespot=driver.find_element_by_id("username")
    usernamespot.send_keys(username)

    passwordspot=driver.find_element_by_id("password")
    passwordspot.send_keys(password)

    submitbutton=driver.find_element_by_name("submit")
    submitbutton.click()

    #new page
    timeRadioButton=driver.find_element_by_id(length)
    timeRadioButton.click()

    nextSubmitButton=driver.find_element_by_name("submit")
    nextSubmitButton.click()
    #finished

    #driver.close();
#username, password, room number( letter are capital), time(30minute intervals 7:00 am to 11:00 pm),length(30 60 90 or 120 minutes)

reserveRoom("YourANumber","YourPassoword","418K","7:00 am","60 minutes")

