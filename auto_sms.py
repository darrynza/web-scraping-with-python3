
def autosms():

    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com/')


    def new():


        name = input("Enter name or group name : ")
        msg = input("Enter your msg : ")
        count = int(input("Enter the count: "))


        input("enter anything after scanning QR code :")

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_2S1VP')

        for i in range(1,count+1):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()
            # again = input("Do you want stay chat (y) or (n)")
            # if again == "y":
            #     return new()
            # if again == "n":
            #     print("ok we are done .. ")
            #     break
    new()

autosms()





'''again = input("Do you want stay chat (y) or (n)")
    if (again=="y"):
        name = input("Enter name or group name : ")
        msg = input("Enter your msg : ")
        count = int(input("Enter the count: "))

        input("enter anything after scanning QR code :")

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_2S1VP')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()
    elif (again == "n"):
        print("ok..")'''