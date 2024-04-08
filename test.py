import requests

urls = ["https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-metallicheskie/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-s-shumoizolyatsiey/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-s-zerkalom/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-mdf/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-usilennye/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-vnutrennego-otkryvaniya/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-dvukhstvorchatye/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-trekhkonturnye/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-so-steklom/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-s-termorazryvom/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-elitnye/",
"https://modern-dveri.ru/catalog/vkhodnye-dveri/dlya-kvartiry/dlya-kvartiry-uteplennye/",]

for url in urls:
    responce_code = requests.s(url)
    print(responce_code.status_code)