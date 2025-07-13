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
else:
    pass
try:
    exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/HVHTOOLkey.py').text)
except:
    print('viu lòng chạy lại!!!')
