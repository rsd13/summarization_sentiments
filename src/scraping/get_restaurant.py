from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

#url = "https://www.tripadvisor.es/Restaurant_Review-g1064230-d994715-Reviews-Piripi-Alicante_Costa_Blanca_Province_of_Alicante_Valencian_Country.html"
url = "https://www.tripadvisor.es/Restaurant_Review-g1064230-d12741934-Reviews-or180-Goiko_Grill-Alicante_Costa_Blanca_Province_of_Alicante_Valencian_Country.html"
def get_restaurant(page,result):


    #page = requests.get(url)

    soup = BeautifulSoup(page, 'html.parser')
    group_reviews = soup.find("div", ["listContainer hide-more-mobile"])
    reviews = group_reviews.find_all("div", ["review-container"])



    for review in reviews:
        try:
            dic = {}
            datas_reviews = review.find("div", ["ui_column is-9"])
            #print(datas_reviews)
            dic["texto"] = datas_reviews.find("p", ["partial_entry"]).text
            #dic["fecha"] = datas_reviews.find("span", ["stay_date_label"], text=True)

            date = datas_reviews.find("div", ["prw_rup prw_reviews_stay_date_hsx"]).text
            dic["fecha"] = date.split(":")[1][1:]
            #date = datas_reviews.find("span", ["stay_date_label"])

            result.append(dic)



        except:

            pass

    for k in result:
        print(k)
        print("-------")




#get_restaurant()


def create_drive():
    driver = ""
    try:
        driver = webdriver.Firefox()
        driver.get(url)
        html = driver.page_source
    except:
        pass

    return driver


def get_restaurant_selenium():
    result = []
    driver = create_drive()

    while True:
        html = ""
        try:

            group_reviews = driver.find_elements_by_class_name("ulBlueLinks");

            try:
                for group in group_reviews:
                    group.click()
            except:
                print("Error, al dar click al comentario")
                pass

            time.sleep(2)
            html = driver.page_source
            get_restaurant(html, result)


            next = driver.find_element_by_css_selector("a[class='nav next taLnk ui_button primary']")
            time.sleep(1)
            print(next.text)

            next.click()



            #a = driver.cssSelector("nav next taLnk ui_button primary")


            salir = True

        #si no encuentra el boton salimos del bucle
        except:
            driver.close()
            break


    print(result)


get_restaurant_selenium()
