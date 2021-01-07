import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=78e879e7-f98d-448b-ae9e-5408424ee23f&as-backfill=on',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.flipkart.com',
    'X-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 FKUA/website/42/website/Desktop',
    'Content-Type': 'application/json',
    'authority': 'flipkart.d1.sc.omtrdc.net',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'x-client-data': 'CJe2yQEIo7bJAQjEtskBCKmdygEInLXKAQjnxsoBGJu+ygEYvr7KAQ==',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=78e879e7-f98d-448b-ae9e-5408424ee23f&as-backfill=on',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'SID=xQd8TMPXA1jM1Sig5OahQ4nurBApipOy59117Gv9Mz50aB9Lw_Fmia21V5Jb6ZnPoyQPjw.; __Secure-3PSID=xQd8TMPXA1jM1Sig5OahQ4nurBApipOy59117Gv9Mz50aB9Ltb5oply8BGEx8OmGFvpWRg.; HSID=ArRnex7KiTSvR8RM8; SSID=Akt8VFoabc5BO5Zqq; APISID=zWASATRLsca_oY0m/Af4PllSkQ6mcwgZfl; SAPISID=pXgybrxvTs6NdKEx/AE6dCSOPnaeLxLpuF; __Secure-HSID=ArRnex7KiTSvR8RM8; __Secure-SSID=Akt8VFoabc5BO5Zqq; __Secure-APISID=zWASATRLsca_oY0m/Af4PllSkQ6mcwgZfl; __Secure-3PAPISID=pXgybrxvTs6NdKEx/AE6dCSOPnaeLxLpuF; NID=204=Vt4m5t9O55xj6bQZtm-86apo-GNNsVW5Z8XGFNhxvKIMZhKp3PMRvzJMTUWs-eSBXkSKC8-oxOQWaApH1KiGOC0v8QQ9JzJQkJTHeOnVSuRT_uOY2VuRyAVapMjMsWOCxhrDM_VAgDgO2UjqQRgeWvHm32vFVTe4qH9LdtjAG_AclUyNzSHeO3amUreUsBOYgbThVRCU6z9bPU1vKMjzybwwHh9hvKxUsC9HTBCpASA1',
    'if-modified-since': 'Fri, 21 Dec 2012 00:00:01 GMT',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.flipkart.com',
    'If-None-Match': '"JuW/ZE5Rx+HBsqwBU4dvPtxpDtA="',
    'Pragma': 'no-cache',
}

for i in range(1,10):
    print(i)
    params = (
        ('page',i),
        ('q', 'samsung mobiles'),
        ('sid', 'tyy,4io'),
        ('as', 'on'),
        ('as-show', 'on'),
        ('otracker', 'AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na'),
        ('otracker1', 'AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na'),
        ('as-pos', '1'),
        ('as-type', 'Relevance'),
        ('suggestionId', 'samsung mobiles|Mobiles'),
        ('requestId', '78e879e7-f98d-448b-ae9e-5408424ee23f'),
        ('as-backfill', 'on')
        )

    print(params)

    response = requests.post('https://www.flipkart.com/search', headers=headers, params=params)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    main_box = soup.find_all("div", {"class": "_1UoZlX"})

    len(main_box)

    box = main_box[1]

    title = box.find("div", {"class": "_3wU53n"}).text.strip()
    rating = box.find("div", {"class": "hGSR34"}).text.strip()
    price = box.find("div", {"class": "_1vC4OE _2rQ-NK"}).text.strip()
    memory = box.find("ul", {"class": "vFw0gD"}).text.strip()
    details = box.find_all("li")
    storage = details[0].text
    camera_details = details[2].text
    screen_size = details[1].text
    battery_details = details[3].text
    processor = details[4].text

    print(title)
    print(rating)
    print(price)
    print(storage)
    print(camera_details)
    print(screen_size)
    print(battery_details)
    print(processor)

    data_list = []
    for box in main_box:
        temp_dict = {}
        temp_dict['Title'] = box.find("div", {"class": "_3wU53n"}).text.strip()
        temp_dict['Rating'] = box.find("div", {"class": "hGSR34"}).text.strip()
        temp_dict['Price'] = box.find("div", {"class": "_1vC4OE _2rQ-NK"}).text.strip()
        temp_dict['storage'] = details[0].text
        temp_dict['camera_details'] = camera_details = details[2].text
        temp_dict['screen_size'] = screen_size = details[1].text
        temp_dict['battery_details'] = battery_details = details[3].text
        temp_dict['processor'] = processor = details[4].text
        data_list.append(temp_dict)

    print(data_list)

    import pandas as pd

    df = pd.DataFrame(data_list)
    print(df)
    if i==1:
        df.to_csv(r'C:\Users\madha\new.csv', mode='a', index=False )
    else:
        df.to_csv(r'C:\Users\madha\new.csv', mode='a', index=False, header=None)

