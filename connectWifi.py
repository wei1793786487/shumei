import re
import requests



def getBaseRequests():
    # 请先判断是否需要登录
    baseInfo = requests.get("http://www.baidu.com/")
    redUrls = re.findall(r"<script>top.self.location.href='(.*?)'</script>", baseInfo.text)

    redUrl = redUrls[0]
    param = redUrl[redUrl.find("?") + 1:]
    # return param
    # find all form param
    requestsBaseParamer = {'method': 'login', 'param': 'true'}
    params = param.split("&")
    for ps in params:
        one = ps.split("=")
        key = ""
        value = ""
        for k, o in enumerate(one):
            if (k == 0):
                key = o
            if (k == 1):
                value = o
        requestsBaseParamer[key] = value
    return requestsBaseParamer



def login(params, user_name, password):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'is_auto_land=false&usernameHidden={}&username_tip=Username&username={}&strTypeAu=&uuidQrCode=&authorMode=&pwd_tip=Password&pwd={}&net_access_type=%BB%A5%C1%AA%CD%F8'.format(
        user_name, user_name, password)
    response = requests.post('http://10.224.2.3:8182/eportal/webGateModeV2.do', headers=headers, params=params,
                             data=data, verify=False)
    # always is true
    url = str(response.url)
    if url.find("method=toLogin") != -1:
        return False
    else:
        return True


def startLogin(user_name, password):
    return login(getBaseRequests(), user_name, password)


if __name__ == '__main__':
  # startLogin("215071204102","290639")
  startLogin("215071204203","143731")


