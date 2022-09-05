# 星锐科技笔试
编程试题
一、编程题
新冠疫情实时数据获取，例如从百度找到原始页面
https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4
1. 不需要爬取数据，简化起见只需要把画面保存成htm文件
2. 用代码解析文件，获取疫情信息
3. 按照疫情地区、新增、现有、累计、治愈、死亡的顺序，保存成csv文件，
二、编程题
有一个长文本，需要解析成特定的数据格式
long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
解析后的格式为：
{
    'name': 'Variopartner SICAV',
    'lei': '529900LPCSV88817QH61',
    'sub_fund': [{
        'title': 'TARENO GLOBAL WATER SOLUTIONS FUND',
        'isin': ['LU2001709034', 'LU2057889995', 'LU2001709547']
    }, {
        'title': 'TARENO FIXED INCOME FUND',
        'isin': ['LU1299722972']
    }, {
        'title': 'TARENO GLOBAL EQUITY FUND',
        'isin': ['LU1299721909', 'LU1299722113', 'LU1299722030']
    }, {
        'title': 'MIV GLOBAL MEDTECH FUND',
        'isin': ['LU0329630999', 'LU0329630130']
    }]
}
注意sub_fund数组的个数不是固定为4，并且isin个数不固定，需要写成通用逻辑，以适应最多100个sub_fund。


完成后，请把所有代码以及相关说明文档提交的github、gitlab或者gitee，并发送说明邮件到recruitment@orbitfin.ai
