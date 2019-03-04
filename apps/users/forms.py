from wtforms_tornado import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, Length

MOBILE_REGEX = "^1[3456789]\d{9}$"


class SmsCodeForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])


class LoginForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])


class RegisterForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    code = StringField("验证码", validators=[DataRequired(message="请输入验证码"), Length(max=4,min=4,message="请输入4位验证码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码"), Length(max=16,min=8,message="密码长度应为8~16位")])
