import base64
with open("C:\\Users\\silence\\Downloads\\1.jpg",'rb') as f:
    base64_data=base64.b64encode(f.read())
    s=base64_data.decode()
    print(s)
    #print('![](data:image/jpeg;base64,%s)',%s)