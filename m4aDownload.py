
# *_*coding:utf-8*_*
import requests
import urllib.request
import re

def pageDownload(url):
    response=requests.get(url);
    print(response.reason);
    webpage = response.content.decode("gbk");
    with open("D:\\icesongqiang\\Desktop\\sanguo\\page.html", "w+") as fp:
        fp.write( str(webpage) );
    return webpage;

def musicDownload(url):
    # requests 库
    # response=requests.get(url, stream=True);
    # #print(response.reason)
    # return response;
    # urllib.request 库
    response = urllib.request.urlopen(url);
    return response.read();
    
#下载网页中的音乐链接
def pageMusicDownload(webpage):
    num = 1;
    pattern = r"href='(http.*?\.m4a)'";                  # 非贪婪模式
    m4aResults = re.findall(pattern, webpage);
    # with open("D:\\icesongqiang\\Desktop\\sanguo\\res.txt", "wb") as fp:
        # fp.write(str(m4aResults));
    # fp.close();
    for result in m4aResults:
        print("\n开始下载第%d个:" %num);
        print(result);
        # m4aFile = musicDownload(result);
        # print(m4aFile);
        filename = "D:\\icesongqiang\\Desktop\\sanguo\\"+str(num)+".m4a";
        print(filename);
        # with open(filename, "wb") as fp:
            # fp.write(m4aFile);
        urllib.request.urlretrieve(result, filename);
        print("第%d个完成下载" %num);
        num+=1;
        

    
if __name__ == '__main__':
    webpage = pageDownload("http://www.lanrents.com/xiazai/11147-dj.html");
    #print(webpage);
    
    pageMusicDownload(webpage);
