base_url = 'https://m.weibo.cn/detail/'
url = 'https://m.weibo.cn/comments/hotflow?id='

excel_name = r'weibo_comments.xlsx'
txt_name = 'weibo_comments.txt'

# 参考代码：https://www.cnblogs.com/pythonfm/p/9056461.html
ALF = 1583630252
MLOGIN = 1
M_WEIBOCN_PARAMS = 'oid%3D4469046194244186%26luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803'
SCF = 'AjheAPuZRqxmyLT-kTVnBXGduebXE6nZGT5fS8_VPbfADyWHQ_WyoRzZqAJNujugOFYP1tUivrlzK2TGTx83_Qo.'
SSOLoginState = 1581038313
SUB = '_2A25zOMq5DeRhGeNM6FUX8S_EzDqIHXVQwtbxrDV6PUJbktAKLVPhkW1NTjKs6wgXZoFv2vqllQWpcwE-e9-8LlMs'
SUBP = '0033WrSXqPxfM725Ws9jqgMF55529P9D9W58TWlXMj17lMMvjhSsjQ1p5JpX5K-hUgL.Fo-Ee0MceK2RS0q2dJLoIEXLxKqLBozL1h.LxKML1-BLBK2LxKML1-2L1hBLxK-LBKqL12BLxK-LBKqL12Bt'
SUHB = '0BLYTPzIKSGsDo'
WEIBOCN_FROM = 1110006030
XSRF_TOKEN = '5dcf70'
_T_WM = 64204543757
Cookie = {
    'Cookie': 'ALF={:d};MLOGIN={:d};M_WEIBOCN_PARAMS={};SCF={};SSOLoginState={:d};SUB={};SUBP={};SUHB={};WEIBOCN_FROM={:d};XSRF-TOKEN={};_T_WM={:d};'.format(
        ALF,
        MLOGIN,
        M_WEIBOCN_PARAMS,
        SCF,
        SSOLoginState,
        SUB,
        SUBP,
        SUHB,
        WEIBOCN_FROM,
        XSRF_TOKEN,
        _T_WM
    )
}

headers = {
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 通过ajax请求形式获取数据
    'X-XSRF-TOKEN': 'aa8bed',
    'Accept': 'application/json, text/plain, */*'
}


# 数据id号，要爬取的微博的id号，以及导出到excel对应的sheet名
weiboComment = [{
    'id':1,
    'weibo_id': 4349331148136901,
    'sheet_name': 'file_tab1',
},{
    'id':2,
    'weibo_id': 4349336798569857,
    'sheet_name': 'file_tab2',
},{
    'id':3,
    'weibo_id': 4349342632452485,
    'sheet_name': 'file_tab3',
},{
    'id':4,
    'weibo_id': 4349359489249263,
    'sheet_name': 'file_tab4',
},{
    'id':5,
    'weibo_id': 4349367202366649,
    'sheet_name': 'file_tab5',
},{
    'id':6,
    'weibo_id': 4349409263609558,
    'sheet_name': 'file_tab6',
},{
    'id':7,
    'weibo_id': 4349473562085041,
    'sheet_name': 'file_tab7',
},{
    'id':8,
    'weibo_id': 4349476527153453,
    'sheet_name': 'file_tab8',
},{
    'id':9,
    'weibo_id': 4349484396400084,
    'sheet_name': 'file_tab9',
},{
    'id':10,
    'weibo_id': 4349520848132903,
    'sheet_name': 'file_tab10',
},{
    'id':11,
    'weibo_id': 4349719763185960,
    'sheet_name': 'file_tab11',
},{
    'id':12,
    'weibo_id': 4349801526543328,
    'sheet_name': 'file_tab12',
},{
    'id':13,
    'weibo_id': 4350037775161542,
    'sheet_name': 'file_tab13',
},{
    'id':14,
    'weibo_id': 4350053403309300,
    'sheet_name': 'file_tab14',
},{
    'id':15,
    'weibo_id': 4350126740919864,
    'sheet_name': 'file_tab15',
},{
    'id':16,
    'weibo_id': 4350129907409012,
    'sheet_name': 'file_tab16',
},{
    'id':17,
    'weibo_id': 4350130469806786,
    'sheet_name': 'file_tab17',
},{
    'id':18,
    'weibo_id': 4350133967955764,
    'sheet_name': 'file_tab18',
},{
    'id':19,
    'weibo_id': 4350135909606542,
    'sheet_name': 'file_tab19',
},{
    'id':20,
    'weibo_id': 4350218999265612,
    'sheet_name': 'file_tab20',
},{
    'id':21,
    'weibo_id': 4350440310723864,
    'sheet_name': 'file_tab21',
},{
    'id':22,
    'weibo_id': 4350520937742523,
    'sheet_name': 'file_tab22',
},{
    'id':23,
    'weibo_id': 4350785468613341,
    'sheet_name': 'file_tab23',
},{
    'id':24,
    'weibo_id': 4350785615363253,
    'sheet_name': 'file_tab24',
},{
    'id':25,
    'weibo_id': 4350789927730012,
    'sheet_name': 'file_tab25',
},{
    'id':26,
    'weibo_id': 4350789751053448,
    'sheet_name': 'file_tab26',
},{
    'id':27,
    'weibo_id': 4350780188153079,
    'sheet_name': 'file_tab27',
},{
    'id':28,
    'weibo_id': 4350791797481716,
    'sheet_name': 'file_tab28',
},{
    'id':29,
    'weibo_id': 4350797737493161,
    'sheet_name': 'file_tab29',
},{
    'id':30,
    'weibo_id': 4350798441501055,
    'sheet_name': 'file_tab30',
},{
    'id':31,
    'weibo_id': 4350800991931397,
    'sheet_name': 'file_tab31',
},{
    'id':32,
    'weibo_id': 4350974611001741,
    'sheet_name': 'file_tab32',
},{
    'id':33,
    'weibo_id': 4351283193709752,
    'sheet_name': 'file_tab33',
}]