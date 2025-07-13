try:
    from curl_cffi import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import json, re
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
    import tempfile
except ImportError:
    import os, sys
    os.system("pip install curl_cffi")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install random2")
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mH\033[1;36mO\033[1;35mA\033[1;32mnN\033[1;31mG \033[1;34mH\033[1;33mU\033[1;36mY\033[1;36m🍉 - Tool\033[1;36m Yip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;31mO\033[1;37mA\033[1;36mnN\033[1;32mG \033[1;35mH\033[1;37mU\033[1;33mY\033[1;32m🍉 - Tool\033[1;34m Yip \033[1;31m\033[1;32m",
            "\033[1;31mH\033[1;37mO\033[1;36mA\033[1;33mnN\033[1;35mG \033[1;32mH\033[1;34mU\033[1;35mY\033[1;37m🍉 - Tool\033[1;33m Yip \033[1;31m\033[1;32m",
            "\033[1;32mH\033[1;33mO\033[1;34mA\033[1;35mnN\033[1;36mG \033[1;37mH\033[1;36mU\033[1;31mY\033[1;34m🍉 - Tool\033[1;31m Yip \033[1;31m\033[1;32m",
            "\033[1;37mH\033[1;34mO\033[1;35mA\033[1;36mnN\033[1;32mG \033[1;33mH\033[1;31mU\033[1;37mY\033[1;34m🍉 - Tool\033[1;37m Yip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;33mO\033[1;37mA\033[1;35mnN\033[1;31mG \033[1;36mH\033[1;36mU\033[1;32mY\033[1;37m🍉 - Tool\033[1;36m Yip \033[1;31m\033[1;32m",
            "\033[1;36mH\033[1;35mO\033[1;31mA\033[1;34mnN\033[1;37mG \033[1;35mH\033[1;32mU\033[1;36mY\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")

#TDS_token='TDSQficjclZXZzJi


TDS_token= input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập token tds \033[1;37m: \033[1;33m')
cookie_ig=input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập cookie ig\033[1;37m: \033[1;33m')
loai_jop_lam=int(input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số [ 1 đi :)) (chỉ có fl thôi) ] \033[1;37m: \033[1;33m'))
DELAY = int(input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập DELAY \033[1;37m: \033[1;33m'))
if loai_jop_lam == 1:
    loai_jop_lam ='instagram_follow'
elif loai_jop_lam == 2:
    print('chưa cập nhạt')
    exit()
else:
    print('nhập sai')
    exit()

#cookie_ig='''datr=hUNCaGqe0o07JK_uk7Brt21G; ig_did=C22EDE22-CA7A-4360-A335-210AB34FA3D2; ig_nrcb=1; mid=aEJDhQALAAFSdSqgp5ArXyLhDfpf; ps_l=1; ps_n=1; dpr=1; csrftoken=KZhXZk06yMukZDtdITaacMyDjZTgbzAv; ds_user_id=62757491180; rur="HIL\05462757491180\0541782518179:01fe003e2f92c9f408c5c4daaca12da2acff964ea9e83b2cff5f2fb3dc3591c9af9b6a57"; sessionid=62757491180%3ArPiGxuhUrFMsep%3A26%3AAYfV2IHasYav8GRntlKEn4FfrhL6UwgnIMDmASyy6Q; wd=968x919'''
#loai_jop_lam ='instagram_follow'
def getid_ig(cookie_ig):
    xcsrftoken_match = re.search(r'csrftoken=([^;]+)', cookie_ig)
    xcsrftoken = xcsrftoken_match.group(1)
    headersig = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/notifications/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-G955U"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"8.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; CPH2611) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (OPPO Find X8 Pro)',
            'x-asbd-id': '359341',
            'x-csrftoken': xcsrftoken,
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR112mGyzPzTzPsiBGMvCn4ykuNiS_amD4aK1jWRQjuRst8C',
            'x-instagram-ajax': '1022547763',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-session-id': 'wy7l3p:3aqprq:sieysj',
            'cookie': cookie_ig,
        }
    try:
        html=requests.get('https://www.instagram.com/',headers=headersig).text
        match = re.search(r'"appScopedIdentity":\s*"([^"]*)"',html)
        id_ig = match.group(1)
        return id_ig
    except:
        return 0
        
    
def follow_ig(id_ig,link,cookie_ig):
    xcsrftoken_match = re.search(r'csrftoken=([^;]+)', cookie_ig)
    xcsrftoken = xcsrftoken_match.group(1)
    headersig = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/notifications/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"SM-G955U"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"8.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; CPH2611) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (OPPO Find X8 Pro)',
        'x-asbd-id': '359341',
        'x-csrftoken': xcsrftoken,
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR112mGyzPzTzPsiBGMvCn4ykuNiS_amD4aK1jWRQjuRst8C',
        'x-instagram-ajax': '1022547763',
        'x-requested-with': 'XMLHttpRequest',
        'x-web-session-id': 'wy7l3p:3aqprq:sieysj',
        'cookie': cookie_ig,
        }
    url = f'https://www.instagram.com/api/v1/friendships/create/{id_ig}/'
    data = {
        'container_module': 'profile',
        'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
        'user_id': id_ig,
    }
    follow = requests.post(url,headers=headersig,data=data).text
    if '"status":"ok"' in follow:
        return 1
    elif '"message":"checkpoint_required"' in follow:
        mess_ig=print('tài khoản của bạn bị checkpoit')
        return 0,mess_ig
    elif '"status":"fail"' in follow and '"spam":true' in follow:
        mess_ig=print('Tài khoản bị chặn follow tại dòng')
        return 0,mess_ig
    elif '"status":"fail"' in follow and '"require_login":true' in follow:
        mess_ig=print('tài khoản của bạn bị văng cookie')
        return 0,mess_ig




def getthongtintds(TDS_token):
    getthongtin=requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={TDS_token}').json()
    if 'success' in getthongtin:
        usernametds=getthongtin['data']['user']
        xu=getthongtin['data']['xu']
        return usernametds,xu
    else:
        return 0

def cauhinh_ig(id_instagram,TDS_token):
    cauhinh_ig=requests.get(f'https://traodoisub.com/api/?fields=instagram_run&id={id_instagram}&access_token={TDS_token}').json()
    if 'success' in cauhinh_ig:
        name_ig=cauhinh_ig['data']['uniqueID']
        msg=cauhinh_ig['data']['msg']
        return name_ig,msg
    else:
        return 0
def getjop_tds(type,TDS_token):
    getjop=requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}').json()
    if 'data' in getjop:
        #print(getjop)
        return getjop
    else:
        loi=print(getjop['error'] ,'trong', getjop['countdown'])
        return loi
    #getjop=requests.get(f'https://mocki.io/v1/753423e8-25bb-4683-9733-c85e504fde88').json()

def guijop_ig(id,TDS_token):
    print(id)
    guijop=requests.get(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={id}&access_token={TDS_token}').json()
    if 'success' in guijop:
        so_nhiem_vu_da_lam=guijop['cache']
        return 1,so_nhiem_vu_da_lam
    else:
        return guijop['error']
    
def nhanxu_tds_follow(type_jop,TDS_token):
    if type_jop == 'follow':
        nhanxu_tds=requests.get(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW&id=INS_FOLLOW_API&access_token={TDS_token}').json()
        print(nhanxu_tds)
    if type_jop == 'like':
        nhanxu_tds=requests.get(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW&id=INS_FOLLOW_API&access_token={TDS_token}').json()
def TDSIG():

    thongtin=getthongtintds(TDS_token)
    if thongtin != 0:
        name_tds=thongtin[0]
        xu_tds=thongtin[1]
        print(name_tds)
        print(xu_tds)
        #=-==-=-=-=-=-=-=
        id_instagram=getid_ig(cookie_ig)
        print(id_instagram)
        if id_instagram !=0:
            cauhinh=cauhinh_ig(id_instagram,TDS_token)
            name_ig=cauhinh[0]
            msg=cauhinh[1]
            print(name_ig)
            print(msg)
            if msg =='Cấu hình thành công!':

                type=loai_jop_lam
                getjop=getjop_tds(type,TDS_token)
                if getjop !='loi':
                    print(getjop)
                    list_jop = [(item['id'], item['link'],item['type']) for item in getjop['data']]
                    tong_jop=len(list_jop)
                    print(f"Tổng số job: {tong_jop}")
                    for i in range(tong_jop):
                        id,link,type_jop = list_jop[i]
                        #print(f"{i + 1}. ID: {id} | LINK: {link} | TYPE: {type}")
                        print(id)
                        id_ig= id.split('_')[0]
                        time.sleep(4)
                        guijop=guijop_ig(id,TDS_token)
                        #print(ii)
                        if guijop[0] == 1:
                            print('số nv đã làm là:',guijop[1])
                            follow_ig_check=follow_ig(id_ig,link,cookie_ig)
                            if follow_ig_check == 1:
                                print('đã follow thành công')
                                if guijop[1] >= 8:
                                    nhanxu_tds_follow(type_jop,TDS_token)
                                else:
                                    pass
                                input('gggg')
                            
                            else:
                                # loi follow
                                mess_err_ig=follow_ig_check[1]
                                print(mess_err_ig)
                                
                        else:
                            #loi gui jop
                            print(guijop)
                else:
                    loi=getjop
                    # thao tac qua nhanh
                    print(loi)
            else:
                print('chưa thêm tk')
        print('lỗi cookie ig')
TDSIG()