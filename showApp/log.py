import time


def logOut(func):
    def getInfo(request):
        vtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        ipaddr = request.META["REMOTE_ADDR"]
        ua = request.META["HTTP_USER_AGENT"]
        viewpage = request.get_full_path()
        info = vtime+" "+ipaddr+" "+ua+" "+viewpage+"\n"
        print(request.META)
        with open(r'C:\Users\Micha\PycharmProjects\recruit\log.txt','a') as f:
            f.write(info)
        return func(request)
    return getInfo