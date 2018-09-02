import gvcode

def code():
    """
    图形验证码
    """
    base64_str, code = gvcode.base64()
    # 把code存到session中
    session['verify_code'] = code
    # 把base64_str 返回给用户
    return str(base64_str, "utf-8")


def verify_code(code):
    """
    验证code
    """
    user_code = code.lower()
    # 获取实际的验证码
    act_code = session.get('verify_code').lower()
    if user_code == act_code:
        return "验证成功"
    else:
        return "验证失败"
