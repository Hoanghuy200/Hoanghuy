try:
    import requests,os,sys
except ImportError:
    os.system("pip3 install requests --break-system-packages")
    os.system("pip3 install requests")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip3 install bs4 --break-system-packages")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
import os,sys
os.system('cls')
banner = f""" 
\033[0;31m██╗░░██╗██╗░░░██╗██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;32m██║░░██║██║░░░██║██║░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;39m███████║╚██╗░██╔╝███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;34m██╔══██║░╚████╔╝░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;33m██║░░██║░░╚██╔╝░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;34m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║   \033[1;39mTOOL BY\033[1;32m            :  Bé Tập Code                          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER\033[1;32m           :  HVHTOOL                         \033[1;32m     ║
\033[1;32m║   \033[1;39mYOTUBE_LINK\033[1;32m        :  https://www.youtube.com/@HVHTOOL\033[1;32m     ║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║ * Nhập 1 để setup thư viện cho pc 
\033[1;32m║ * Nhập 2 để setup thư viện cho pc nếu 1 lỗi
\033[1;32m║ * Nhập 3 để setup thư viện cho teramux \033[1;31m(ubuntu)
\033[1;32m║ * Nếu teramux không dùng ubuntu thì Dùng 1,2
\033[1;32m║ * setup thư việt 1 lần ai setup rồi thì không pk chạy lại nữa
\033[1;32m║ *\033[1;97m TOOL ĐƯỢC CẬP NHẬT VÀO 24/6/2025 
\033[1;32m║ *\033[1;97m TOOL XỄ ĐƯỢC CẬP NHẬT VÀ CHỈNH SỬA FIX LỖI LIÊN TỤC MN VÀO NHÓM DISCORD CẬP NHẬT THƯỜNG XUYÊN THÉ 
\033[1;32m║ *{tim} --> \033[1;31m Enter để vào tool
\033[1;32m║ *{tim} --> \033[1;31m Enter để vào tool
\033[1;39m└──────────────────────────────────────────────────────────────┘"""
print(banner)
#print(banner1)
text = "[<@=@>]"

colors = [
    "\033[1;31m",  # Đỏ
    "\033[1;32m",  # Xanh lá
    "\033[1;33m",  # Vàng
    "\033[1;34m",  # Xanh dương
    "\033[1;35m",  # Tím
    "\033[1;36m",  # Xanh ngọc
    "\033[1;91m",  # Đỏ sáng
    "\033[1;92m",  # Xanh lá sáng
    "\033[1;93m",  # Vàng sáng
]

# Gộp các ký tự và mã màu thành một chuỗi duy nhất
colored_text = "".join(f"{colors[i % len(colors)]}{c}" for i, c in enumerate(text)) + "\033[0m"

# In ra 1 dòng
setup=input(f'{colored_text}{vang} Nhập setup:')
if setup == '1':
    import os,sys
    os.system("pip install requests")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install tabulate")
    os.system("pip install bs4")
    os.system("pip install lxml")
    os.system("pip install beautifulsoup4")
    os.system("pip install random-user-agent")
    os.system("pip install pystyle")
    os.system("pip install curl_cffi")
    os.system("pip install random2")
    os.system("pip install selenium")
    os.system("pip install DateTime")
    os.system("pip install threaded")
    os.system("pip install thread")
    os.system("pip install urllib3")
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
elif setup == '2':
    import os,sys
    os.system("pip3 install requests")
    os.system("pip3 install art")
    os.system("pip3 install colorama")
    os.system("pip3 install tabulate")
    os.system("pip3 install bs4")
    os.system("pip3 install lxml")
    os.system("pip3 install beautifulsoup4")
    os.system("pip3 install random-user-agent")
    os.system("pip3 install pystyle")
    os.system("pip3 install curl_cffi")
    os.system("pip3 install random2")
    os.system("pip3 install selenium")
    os.system("pip3 install DateTime")
    os.system("pip3 install threaded")
    os.system("pip3 install thread")
    os.system("pip3 install urllib3")
    os.system("pip3 install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
elif setup == '3':
    import os, sys
    os.system("pip3 install requests --break-system-packages")
    os.system("pip3 install art --break-system-packages")
    os.system("pip3 install colorama --break-system-packages")
    os.system("pip3 install tabulate --break-system-packages")
    os.system("pip3 install bs4 --break-system-packages")
    os.system("pip3 install beautifulsoup4 --break-system-packages")
    os.system("pip3 install lxml --break-system-packages")
    os.system("pip3 install random-user-agent --break-system-packages")
    os.system("pip3 install pystyle --break-system-packages")
    os.system("pip3 install curl_cffi --break-system-packages")
    os.system("pip3 install random2 --break-system-packages")
    os.system("pip3 install selenium --break-system-packages")
    os.system("pip3 install DateTime --break-system-packages")
    os.system("pip3 install threaded --break-system-packages")
    os.system("pip3 install thread --break-system-packages")
    os.system("pip3 install urllib3 --break-system-packages")
    os.system("pip3 install faker requests colorama bs4 pystyle --break-system-packages")
    os.system("pip3 install requests pysocks --break-system-packages")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
elif setup == '':

    try:
        exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/Hoanghuy/refs/heads/main/HVHTOOLkey1.py').text)
    except:
        print('viu lòng chạy lại!!!')


else:
    print('nhập sai ???')

import base64
import os
import time
import json
from curl_cffi import requests
import sys
import random
from time import sleep
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
bold = "\033[1m"  # Added bold ANSI escape code
end = '\033[0m'

def banner():
    # Clear console screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f""" 
\033[0;31m██╗░░██╗██╗░░░██╗██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;32m██║░░██║██║░░░██║██║░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;31m███████║╚██╗░██╔╝███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██╔══██║░╚████╔╝░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;31m██║░░██║░░╚██╔╝░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;32m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║   \033[1;39mTOOL BY\033[1;32m            :  Bé Tập Code                          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER\033[1;32m           :  HVHTOOL                         \033[1;32m     ║
\033[1;32m║   \033[1;39mYOTUBE_LINK\033[1;32m        :  https://www.youtube.com/@HVHTOOL\033[1;32m     ║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))
    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'HVH{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://hohiepvn.x10.mx/key/van-thang-vip.php?key={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    try:
        token = "667294c6bf2cd922507983c4"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    global code
    prefix = "HVH156XDTNL912"
    suffix = ''.join(random.choices('0123456789', k=16))
    code = prefix + suffix
    try:
        with open("ch.txt", "w") as file:
            file.write(f"{code}")
    except Exception as e:
        print(f"Lỗi khi khởi tạo: {e}")

    try:
        keydis = requests.get('https://raw.githubusercontent.com/shopaccrandom/md/refs/heads/main/modun_setup/modun_0368tedj7bzxkn3cevtp/nodun_28sr2ocxwnerfkr4dnvs.txt').text.strip()
    except:
        print('Lỗi khi tạo key trên Discord')
        keydis = None

    try:
        with open("key.txt", "r", encoding="utf-8") as file:
            keydiscord = file.read()
    except:
        ip_address = get_ip_address()
        display_ip_address(ip_address)

    if ip_address or (keydis and keydis == keydiscord):
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key (Free) hoặc 2 Để Nhập Key ADMIN \033[1;33m")
            try:
                choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: ")
                print("\033[97m════════════════════════════════════════════════")
                if choice not in ["1", "2"]:
                    print("Vui lòng nhập số hợp lệ (1 hoặc 2).")
                    return
            except KeyboardInterrupt:
                print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                sys.exit()

            if choice == "2":
                while True:
                    try:
                        keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mNhập Key ADMIN: \033[1;32m')
                        if keydis and keynhap == str(keydis):
                            with open("file.txt", "w", encoding="utf-8") as file:
                                file.write(keynhap)
                            print('Key ADMIN Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, datetime.now().replace(hour=23, minute=59, second=0, microsecond=0))
                            return
                        else:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mKey ADMIN Sai, Vui Lòng Nhập Lại!')
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

            while True:
                url, key, expiration_date = generate_key_and_url(ip_address)
                with ThreadPoolExecutor(max_workers=2) as executor:
                    yeumoney_future = executor.submit(get_shortened_link_phu, url)
                    yeumoney_data = yeumoney_future.result()
                    if yeumoney_data and yeumoney_data.get('status') == "error":
                        print(yeumoney_data.get('message'))
                        return
                    else:
                        link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                        print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:', link_key_yeumoney)

                    start_time = time.time()
                    try:
                        keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m')
                        elapsed_time = time.time() - start_time
                        if elapsed_time < 60:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCó hành vi bypass! Vui lòng dùng link mới.')
                            continue
                        if keynhap == key or (keydis and keynhap == str(keydis)):
                            with open("file.txt", "w", encoding="utf-8") as file:
                                file.write(keydis if keydis else keynhap)
                            print('Key Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                            return
                        else:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                            start_time = time.time()
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()


if __name__ == "__main__":
    main()
while True:
    try:
        if not os.path.exists("ch.txt"):
            print("không tồn tại.") 
        with open("ch.txt", "r", encoding="utf-8") as file:
            first_line = file.readline().strip()
            print(first_line)
            print(code)
            
            if first_line and first_line == code:
                print("là số 1.")

                time.sleep(2)
                try:
                    url ='https://raw.githubusercontent.com/shopaccrandom/jjjjjjjj/refs/heads/main/goc/hvhtool.py'
                    response = requests.get(url)
                    response.raise_for_status()  # Check for HTTP errors
                    exec(response.text)  # Execute the fetched script
                
                except Exception as e:
                    print(f"Lỗi khi thực thi script từ URL {url}: {e}")
                
            else:
                print("không phải là số 1.")
            
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool của AD")
        sys.exit()
