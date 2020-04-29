
class LoginDatas:
    # 正常场景  --测试数据
    success_data = {"user":"admin","password":"test123"}

    #异常用例   密码错误，请重新输入！ ddt (密码不正确，)
    wrong_data = [
        {"user":"admin","password":"","check":"密码不能为空，请输入密码。"},
        {"user":"admin","password":"test12","check":"密码错误，请重新输入！"},
        {"user":"","password":"test123","check":"帐号不能为空，请输入帐号。"}
    ]

    #异常用例   未注册的账号  帐号不存在或者已被禁用，请重试！
    errorPwd_noReg = [
        {"user":"adminin","password":"dfwewqe","check":"帐号不存在或者已被禁用，请重试！"},
        {"user":"324243243","password":"ewrewr","check":"帐号不存在或者已被禁用，请重试！"}

    ]

