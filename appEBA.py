
import time
from selenium import webdriver
import pandas as pd


#excel dosyasını okuyoruz
excel_data_dersler = pd.read_excel('data.xls', sheet_name='canli')
excel_data_kullanici = pd.read_excel('data.xls', sheet_name='kullanici_bilgileri')

#kaç satır ve kaç sütundan oluşuyor buluyoruz
satirSayisi = len(excel_data_dersler.loc[:])
sutunSayisi = len(excel_data_dersler.columns)



#chrome tarayıcıya bağlanıyoruz
driver = webdriver.Chrome()
driver.get('https://mebbis.meb.gov.tr/default.aspx')

#Excelden aldığımız veriler
tcNo= excel_data_kullanici.loc[0][0]
sifre = excel_data_kullanici.loc[0][1]


#sayfaya TC ve şifre bilgilerini yazıyoruz
tcAlani = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[3]/div[3]/input')
tcAlani.send_keys(str(tcNo))

sifreAlani = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[3]/div[4]/input')
sifreAlani.send_keys(str(sifre))

#giriş butonun bas
girisButon = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[3]/div[5]/input')
girisButon.click()

#sayfanın durmunu al
window_before = driver.window_handles[0]


#eba butonuna tıkla
ebaButon = driver.find_element_by_xpath('/html/body/form/section/div/div/div[8]/div/div/div[1]/div/div/p/a')
ebaButon.click()
#eba TC tıkla ve EBAya git
ebaTC = driver.find_element_by_xpath('/html/body/form/div[14]/div/div/div[2]/ul/li/a')
ebaTC.click()




time.sleep(5)

#yeni sayfanın durumunu al ve yeni sayfaya geç
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)

time.sleep(2)
# canlı der ekranına giriş
driver.get('https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.747/index.html#/main/editExternalLiveSession')
time.sleep(4)


for i in range(satirSayisi):
    print("i değeri: ",i)
    #derse ait bilgilerin tanımlanması
    dersBaslikDegeri = excel_data_dersler.loc[i][1]
    sinifSeviyeDegeri = excel_data_dersler.loc[i][2]
    dersTarihiDegeri = excel_data_dersler.loc[i][3]
    dersSaatDegeri = excel_data_dersler.loc[i][4]
    dersAciklamaDegeri = excel_data_dersler.loc[i][5]
    uygulamaTuruDegeri = excel_data_dersler.loc[i][6]
    dersLinkDegeri = excel_data_dersler.loc[i][7]
    dersSifreDegeri = excel_data_dersler.loc[i][8]
    dersSecDegeri = excel_data_dersler.loc[i][9]
    subeSecDegeri = excel_data_dersler.loc[i][12]

    time.sleep(1)

    # Canlı ders başlığını gir
    canliDersBasligi = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/input')
    canliDersBasligi.send_keys(str(dersBaslikDegeri))
    print("Canlı Ders Başlığı")

    time.sleep(1)

    sinifSeviye = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/select/option[%s]' % sinifSeviyeDegeri)
    sinifSeviye.click()
    print("Sınıf Seviye")
    time.sleep(1)

    dersTarihiAc = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[3]/p/span/button')
    dersTarihiAc.click()
    print("Ders Tarihi Aç")
    time.sleep(1)

    print("datepicker başladı")

    dersTarihiSec = driver.find_element_by_css_selector(
        '#ebaEtudEditView > div.vc-layout-view-content-padding > div > div > div.row.m-n.vc-resp-all-margin.vc-border-bottom-thin-light > div:nth-child(1) > div.row.m-n.vc-bg-color-white.p-b-sm > div.col-sm-3.col-xs-6.p-xs > p > input')
    print(dersTarihiSec)
    driver.execute_script("arguments[0].removeAttribute('readonly','readonly')", dersTarihiSec)

    time.sleep(1)
    dersTarihiSec.clear()
    time.sleep(1)
    dersTarihiSec.send_keys(str(dersTarihiDegeri))
    # dersTarihiSec.click()

    print("Ders Tarihi Seç")
    time.sleep(1)

    print("datepicker bitti")



    aciklama = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/input')
    aciklama.send_keys(str(dersAciklamaDegeri))

    print("Açıklama")
    time.sleep(0.5)

    # uygulama türü seç
    uygulamaTuru = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[6]/select/option[%s]' % uygulamaTuruDegeri)

    uygulamaTuru.click()
    print("Uygulama Türü")
    time.sleep(1)

    dersLinki = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[7]/input')

    dersLinki.send_keys(str(dersLinkDegeri))

    print("Ders Linki")

    time.sleep(0.5)

    dersSifre = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[8]/input')
    dersSifre.send_keys(str(dersSifreDegeri))
    print("Ders Şifresi")
    time.sleep(2)

    dersSecAc = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/span')
    dersSecAc.click()
    print("Ders Seçimi Aç")
    time.sleep(1)

    dersSec = driver.find_element_by_xpath(
        '//*[@id="ui-select-choices-row-0-%s"]/span' % dersSecDegeri)
    dersSec.click()
    print("Ders Seçimi")

    time.sleep(1)
    subeSecAc = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/span/button')
    subeSecAc.click()
    print("Şube Seçimi Aç")
    time.sleep(1)

    subeSec = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/span/div/div/div[%s]' % subeSecDegeri)
    subeSec.click()
    print("Şube Seçimi")

    time.sleep(1)

    dersSaati = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select/option[5]')
    dersSaati.click()
    dersSaati = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select/option[2]')
    dersSaati.click()
    dersSaati = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select/option[%s]' % dersSaatDegeri)
    dersSaati.click()
    print("Ders Saati")
    time.sleep(1)

    ogrenciListele = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div')
    ogrenciListele.click()
    print("Öğrencileri Listele")

    time.sleep(6)
    dersOlustur = driver.find_element_by_xpath(
        '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[2]/div[2]/div[2]/div')
    dersOlustur.click()
    print("Ders Oluşturuldu")
    time.sleep(2)
    # canlı ders ekleme ekranına giriş
    driver.get('https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.747/index.html#/main/editExternalLiveSession')

    time.sleep(5)


# canlı ders ekranına giriş
driver.get('https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.748/index.html#/main/livesessionview?tab=externalLiveLessons&pageNumber=1&pageSize=25')

print("bitti")
