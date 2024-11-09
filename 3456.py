import requests

# 定义请求函数
def make_request(url, headers, data):
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

# 请求 1: 应用商店开
url_1 = "https://api.edstars.com.cn/parent/api/v1/app/switch-config/set"
headers_1 = {
    "Authorization": "tal173Yyf_mNm7waUC5h557ME3PbfthTVcvQgWmzeftuXdo7T1ynJNfPn8iCPfc21DK-ud0SsvFFd1tBHWEmuvotkoNtHNbnRyNb-I8_voymgBBDizRWN6aWvY5tVOqfDvFDPcLDb_GokpvSPeRyFPRzgJG16m_TYnjwB_30uVnB6A56Mfh",
    "X-Tal-BusBu": "8",
    "X-Tal-Sn": "7BPE082411901347",
    "X-Tal-StuId": "Talom6A5uYXtigKuNQcTfo3dag",
    "X-Tal-ClientId": "552206",
    "X-Tal-FamilyId": "684221391603830784",
    "X-Tal-DeviceCode": "TALIH-PD2",
    "X-Tal-Bu": "1",
    "X-Tal-PkgName": "2.2.0",
    "X-Tal-UdcDeviceId": "TAL220507A971A194A8D7E48F8C7300B0A4E6D2",
    "User-Agent": "QzSearch/2.2.0(3156) OSType/1(Redmi 24069RA21C;14) NetType/WIFI Channel/App",
    "X-Tal-Version": "2.2.0",
    "X-Tal-Platform": "Android",
    "X-Tal-DeviceId": "79bd1969fde6f25aae19513916edb644",
    "X-Tal-Timestamp": "1730629705",
    "X-Tal-Nonce": "92a783ee-2d3a-484d-956e-35e7d56f54dc",
    "X-Tal-AppKey": "parent_v1.9.0",
    "X-Tal-Packagename": "com.tal.bixin.family",
    "X-Tal-OsType": "redmi",
    "X-Tal-OsName": "redmi",
    "X-Tal-Sign": "2a8feb69ea5f52529dbb8334dc44ff9b",
    "traceparent": "00-d94d2acd53d9c8736173fb2f24c55ccd-e21c3f2f82a9c53f-01",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "api.edstars.com.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
data_1 = """{\"encrypted_param\":\"zjqiiUbvO8JYg46HjhqMZHmwtvlU/kauBct/9pkbHtJ0zwDwE/8kM6cH0ZShWCmNl1b51t98HbqDl73E0aITAPglhOtB9EzACTA7zLu/jFg5/DG13BWn0s8dmzIKXEU8bM8Frg2EJXGuYTDQt5BOA2pJwG7Pizv1aK4N82vAGsj8CaQ9MSHceglXsn8GBYH/blK6K5iHggVJ3FapA1YHUg==\"}"""

# 请求 2: 安装哔哩
url_2 = "https://api.edstars.com.cn/parent/appstore/api/v1/control/push"
headers_2 = headers_1
data_2 = """{\"encrypted_param\":\"HLZKZzijBFvwXwZOEFssBdMYz4nVQI89d379qYNQjbmOVdpa33moHCxpU58SaalkiK9JlEz8uR7kUIrMzkuGdA==\"}"""

# 请求 3: 打开哔哩
url_3 = url_1
data_3 = """{\"encrypted_param\":\"HLZKZzijBFvwXwZOEFssBdMYz4nVQI89d379qYNQjbmBC5Jelq3j/SkG0ttKdWQwMqQKV9mgiIwv4mFmPO8+TqFXKTjec/Pzz6fSWIenvfXrkSGTtyTyWRdq6LHMz0kmTmWvKxSlOTlc38DF2rL/01or8SaMw23lxF6BqgaECCGsklr8rniNw+GwspzGsq/Dy6wzt82HvIfPDyDo8MtEGg==\"}"""

# 请求 4: 开喜马拉雅
data_4 = """{\"encrypted_param\":\"zjqiiUbvO8JYg46HjhqMZI9Uq8X6lNpwoj+0G0utYC2RKUZnQhIanAqPTssY3BIpxFdC5FkwbgFCATw91wxoju+U65FA7aFBoFIKh7+UY0k6adMRXyFVDgnS2kQ3jeR11qmSup42hOUMg3WoguDsrIeJpUEYxGuotgYKvZcPPjiyrdbWsmvjxU4erxdXScL1JIrV6TZ1QJlGRvfTB49Ksw==\"}"""

# 请求 5: 开钉钉
data_5 = """{\"encrypted_param\":\"zjqiiUbvO8JYg46HjhqMZENkEuVobN0pxVT2D97ycuj+q9H0J4pQCyVnarUCNIS3SMXhPNCGcbSbdBWAOTINH8a0U52WvRl75qbr2N5rjtW7kNHlOZe7SwD0FhoQt7Psai/CLtM6RAosOqGHF+RF2tg/Gl2bB8JZj2CRTkgvQ06zMJKXcUG2Eq6JWLQwtQ40POOekswXd3t9a+pd/gQOzA==\"}"""

# 请求 6: 开send
data_6 = """{\"encrypted_param\":\"Dr9JZkurgs3VJBO9Ac1uK4T23l3nYaXgAHAMSSk2LZsR0DNj65fGYfqLoguugOEn9CyNqkpoPO3n08UzGmR2fYo7RrHU6F05SE6AgVSaN8lbe5Tg3tm9eD/O0smtvSTNqb/voUelmpZwHBaCtT748JYnJLJUDKOaPoXegRo9hGYEbtXAsxNQjxjhlqHe943YeB2RJdLSAo19l4kGdrJ+QNJ/6EvaP5iYm6gY7mYK5ks=\"}"""

# 依次发送请求
make_request(url_1, headers_1, data_1)  # 应用商店开
make_request(url_2, headers_2, data_2)  # 安装哔哩
make_request(url_3, headers_1, data_3)  # 打开哔哩
make_request(url_1, headers_1, data_4)  # 开喜马拉雅
make_request(url_1, headers_1, data_5)  # 开钉钉
make_request(url_1, headers_1, data_6)  # 开send
