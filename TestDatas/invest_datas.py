
class InvestDatas:
    #投资成功
    success={"monkey":1000}

    #投资失败，投标置灰，非100整数倍且大于100，非100整数倍且小于100，字符，符号

    no10 = [
        {"monkey":454,"check":"请输入10的整数倍"},
    {"monkey":54,"check":"请输入10的整数倍"},
    {"monkey":"a","check":"请输入10的整数倍"},
    {"monkey":"$","check":"请输入10的整数倍"},
    ]


    #投资失败弹框提示，负数100整数金额，0，空格，100整数倍且小于100，投标金额大于标剩余可投金额

    wrong_format_monkey = [
        {"monkey":10,"check":"请填写正确的投标金额"},
    {"monkey":0,"check":"请填写正确的投标金额"},
    {"monkey":" ","check":"请填写正确的投标金额"},
    {"monkey":50,"check":"投标金额必须为100的倍数"},
]