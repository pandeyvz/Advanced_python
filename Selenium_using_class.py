from selenium import webdriver
class Login:

    def m1(self,url,username,password):
        driver=webdriver.Chrome("C:/Users/Pandey9V2/PycharmProjects/Practice_Projects/chromedriver")
        driver.get(url)
        driver.find_element_by_xpath("//*[@id=\"j_id5:login-form:username\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"j_id5:login-form:password\"]").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"j_id5:login-form:login\"]").click()

urls = ["http://10.113.247.61:9081", "http://10.113.247.193:9080", "http://10.113.247.196:9080", "http://10.113.247.198:9080", "http://10.113.247.192:9080"]
uname = ["enocfm", "ubnt", "ubnt", "ubnt", "ubnt"]
passw = ["Vubrpm#2018", "Vubrpm#2018", "Vubrpm#2018", "snoctxp@2019", "Vubrpm#2018"]

l=Login()
for i in range(5):
    try:
        l.m1( urls[i],uname[i], passw[i])
    except Exception as ex:
        print(ex)
        continue