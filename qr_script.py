from tqdm import tqdm
import time
import qrcode

message = input("What do you wanna share with the world?💡 ")
try:
    for i in tqdm(range(20), desc = 'tqdm() Progress Bar'):
        time.sleep(0.001)
        qr = qrcode.QRCode(version=1, box_size=5, border=5)
        qr.add_data(message)
        qr.make()
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save("qrcode.png")
    print("Your qrcode is ready🎉, Check out your current directory🤖 ")
except:
    print("Please enter a valid input🥺")
