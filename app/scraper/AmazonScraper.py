
import time
import random
from app.scraper.Parsing import Parsing
from app.models.Produit import Produit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonScraper :

    def scraper(self ,url):
        parsing = Parsing()
        liste_produit = []
        driver = webdriver.Chrome()
        driver.get(url)
        WebDriverWait(driver ,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR ,"div[data-component-type= s-search-result]"))
        )
        for element in driver.find_elements(By.CSS_SELECTOR ,"div[data-component-type=s-search-result]"):
            nom = element.find_element(By.CSS_SELECTOR ,"div.a-section-a-spacing-small-puis-padding-left-smallp-uis-padding-right-small").text
            prix = element.find_element(By.CSS_SELECTOR ," span.a-offscreen").get_attribute("textContent")
            note = element.find_element(By.CSS_SELECTOR,"span.a-size-small-a-co(lor-base span.a-row a-size-small ").get_attribute("textcontent")
            image_url = element.find_element(By.CSS_SELECTOR,"div.a-section-aok-relative-s-image-square-aspect img.s-image").get_attribute("url")
            produit = produit(prix ,note ,image_url)
            liste_produit.append(produit)
        return liste_produit