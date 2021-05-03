from jsonpath import jsonpath

json_dict={
        "id": 1188453,
        "leave_amount": 0.0,
        "mobile_phone": "15738825218",
        "reg_name": "小柠檬",
        "reg_time": "2021-01-30 19:48:40.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2021-02-03 22:17:01",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjExODg0NTMsImV4cCI6MTYxMjM2MTgyMX0.kPPLyMMOCn-g4mmJvICUQZZ-a06hkSMeGzCFQcCxZ0meVDnX-rn_wQ6kSLGLmmA1AY2LPy1UfcRYmP7sx8bleg"
        }
    }
#匹配的结果放在列表，如果没有匹配，返回false
resp=jsonpath(json_dict,'$..token')
print(resp)
