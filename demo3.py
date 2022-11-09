import re
import requests


header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 "
                  "Safari/537.36"}
for x in range(1, 5):
    url1 = f"https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum={x}&maxResults=25&appid=C10010188&version=10.0.0&zone=&locale=zh"
    resp1 = requests.get(url1, headers=header)
    # print(resp1.text)
    obj = re.compile('.*?Id.*?accountName":"(?P<Name>.*?)".*?Info":"(?P<comment>.*?)".*?Type', re.S)
    list1 = obj.finditer(resp1.text)
    for i in list1:
    #   with open("a.txt","w") as f:
    #       f.write(i.group("Name"),encodings="UTF-8")
    #       f.write(i.group("comment"),encodings="UTF-8")
    # print("ok")
     print(i.group("Name"))
     print(i.group("comment"))
     with open(file=r"a.txt", mode="a",encoding="UTF-8") as f:
      f.write(i.group("Name")+"\n")
      f.write(i.group("comment")+"\n")
