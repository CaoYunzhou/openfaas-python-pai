import requests
import json
import time

# json_url = {
#  "digit_len": 100,
# }

# def handle(req):
    # start = time.time()
#     # result = {"found": False}
#     json_req = json.loads(req)
#     r = int(json_req["num_1"]) + int(json_req["num_2"])
#     # r2 = requests.get(json_req["num_2"])
#     # print(r)
#     # if json_req["term"] in r.text:
#     #     result = {"found": True}
#
#     # print(json.dumps(result))
#     # end = time.time()
#     # running_time = end - start
#     # print('time cost : %.5f sec' % running_time)
#     return r
# # handle(json.dumps(json_url))


'''
计算圆周率任意位数
因为根据马青公式π/4=4arctg1/5-arctg1/239
又因为arctgX=X-(1/3)X^3+(1/5)X^5-(1/7)X^7+……+[(-1)^(n-1)/((2n-1)]*X^(2n-1))
变形得π/4=(4/5-1/239)-1/3(4/5^3-1/239^3)+1/5(4/5^5-1/239^5)……
所以可以用python语言编写出求圆周率到任意位的程序如下：
'''
def handle(req):
    json_req = json.loads(req)
    start_time = time.time()
    n = int(json_req["digit_len"])
    w = n+10
    b = 10**w
    x1 = b*4//5
    x2 = b // -239
    he = x1+x2
    n *= 2
    for i in range(3, n, 2):
        x1 //= -25
        x2 //= -57121
        x = (x1+x2) // i
        he += x
    pai = he*4
    pai //= 10**10
    end_time = time.time()
    running_time = end_time - start_time
    # print('time cost : %.5f sec' % running_time)
    # cost_time = {" time cost ": '%.5f sec % running_time'}
    # print(type(cost_time))
    # return json.dumps(cost_time)
    # print(pai)
    return running_time
# handle(json.dumps(json_url))
