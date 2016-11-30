# __author__ = 'Bestla'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com/Practiceform/")
assert "Selenium Framework" in driver.title
driver.maximize_window()

'''
def ClearText():
    text_box_elem = driver.find_element_by_xpath("//textarea[@id='vfb-10']")   #Enter in text box
    text_box_elem.clear()
    text_box_elem.send_keys("Testing..")
    text_elem = driver.find_element_by_xpath("//input[@id='vfb-9']")           #Enter in Text
    text_elem.clear()
    text_elem.send_keys("Testing")

def CheckBoxes():
    checkboxes = []
    checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
    for check in checkboxes:
        check.click()

    #check_boxes1 = driver.find_element_by_id("vfb-6-0").click()                        #Tick Checkboxes
    #check_boxes2 = driver.find_element_by_id("vfb-6-1").click()
    #check_boxes3 = driver.find_element_by_id("vfb-6-2").click()

    #if (check_boxes1.is_selected()):
       # print("Checkbox is selected..now deselecting")
        #check_boxes1.click()
    #else:
       # print("Checkbox is not selected..now selecting it")
        #check_boxes1.click()

def RadioButtons():
    """radiobuttons = []                                                                   #Loop for going through each radio button
    radiobuttons = driver.find_elements_by_xpath("//input[@name='vfb-7']")
    for radio in radiobuttons:
        radio.click()
    time.sleep(15)"""

    radiobutton = driver.find_element_by_xpath("//input[@id='vfb-7-3']")
    radiobutton.click()

def calender():
    cal=driver.find_element_by_xpath("//input[@name='vfb-8']")
    cal.click()
    cal= driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]/span")    # Click to go to next month
    cal.click()
    cal= driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[1]/span")    # Click to go the previous month
    cal.click()
    cal = driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a")
    cal.click()

def URL():                                                                                  #Enter URL
    url_text = driver.find_element_by_xpath("//input[@id='vfb-11']")
    url_text.clear()
    url_text.send_keys("http://www.gptoday.com")

dropdown = driver.find_element_by_xpath ("//select[@id='vfb-12']")                        #Selecting Options from drop down
Select(dropdown).select_by_value("Option 2")
dropdown_count= driver.find_element_by_tag_name("options")'''
# print len(dropdown_count)

def verification():
    t = driver.find_element_by_xpath("//input[@id='vfb-3']").click()
    user_input = int(input("Enter only 2 digit number: "))      #EnteringNumber in field
    actual_message = "Please enter at least 2 characters."

    if (user_input > 9) and (user_input < 100):
        driver.find_element_by_id("vfb-4").click()
        print("Success")
    else:
        driver.find_element_by_id("vfb-4").click()
        driver.find_element_by_xpath(".//*[@id='item-vfb-2']/ul/li[1]/span/label[1]").text
        assert ("Please enter at least 2 characters." in actual_message)
        print ("fail")


def NewWindow():

    btn = driver.find_element_by_id("button1").click()

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    print("Test 1")

    driver.switch_to.window(window_after)
    driver.maximize_window()
    print("test 2")
    assert "Selenium Framework | Selenium, Cucumber, Ruby, Java et al." in driver.title
    print ("test 3")


'''a=ClearText()
b=CheckBoxes()
c=RadioButtons()
d=calender()
e=URL()
f= DropDown()
h = verification()'''
m = NewWindow()