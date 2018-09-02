from flask import request, session, jsonify, current_app
from flask_restful import Resource
from util.common import *
from admin import r
import gvcode

class Code(Resource):
    """
    图形验证码
    """
    @catch_exception
    def get(self):
        base64_str, code = gvcode.base64()

        # 把code存到session中
        session['verify_code'] = code
        # 把base64_str 返回给用户
        return str(base64_str, "utf-8")


class VerifyCode(Resource):
    """
    验证code
    """
    @catch_exception
    def post(self):
        data = request.get_json()
        user_code = data['code'].lower()
        # 获取实际的验证码
        act_code = session.get('verify_code').lower()
        if user_code == act_code:
            return trueReturn("验证成功")
        else:
            return falseReturn("验证失败")
