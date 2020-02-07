import requests
import pandas as pd
import time
import openpyxl #导出excel需要用到
from config import headers,url,Cookie,base_url,weiboComment,excel_name,txt_name

#将中国标准时间(Sat Mar 16 12:12:03 +0800 2019)转换成年月日
def formatTime(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    time_struct = time.strptime(time_string,from_format)
    times = time.strftime(to_format, time_struct)
    return times

# 爬取第一页的微博评论
def first_page_comment(weibo_id, url, headers):
    try:
        url = url + str(weibo_id) + '&mid=' + str(weibo_id) + '&max_id_type=0'
        web_data = requests.get(url, headers=headers,cookies = Cookie,timeout=20)
        js_con = web_data.json()
        # 获取连接下一页评论的max_id
        max_id = js_con['data']['max_id']
        max = js_con['data']['max']
        comments_list = js_con['data']['data']
        for commment_item in comments_list:
            Obj =  {
                'commentor_id':commment_item['user']['id'],
                'commentor_name':commment_item['user']['screen_name'],
                'commentor_blog_url':commment_item['user']['profile_url'],
                'comment_id':commment_item['id'],
                'comment_text':commment_item['text'],
                'create_time':formatTime(commment_item['created_at'],'%a %b %d %H:%M:%S +0800 %Y','%Y-%m-%d %H:%M:%S'),
                'like_count':commment_item['like_count'],
                'reply_number':commment_item['total_number'],
                'full_path':base_url+str(weibo_id),
                'max_id': max_id,
                'max':max
            }
            commentLists.append(Obj)
        print("已获取第1页的评论")
        return commentLists
    except Exception as e:
        print("遇到异常")
        return []

#运用递归思想，爬取剩余页面的评论。因为后面每一页的url都有一个max_id，这只有从前一个页面返回的数据中获取。
def orther_page_comments(count,weibo_id, url, headers,max,max_id):
    if count<=max:
        try:
            if count<15:
                urlNew = url + str(weibo_id) + '&mid='+ str(weibo_id) + '&max_id=' + str(max_id) + '&max_id_type=0'
            else:
                urlNew = url + str(weibo_id) + '&mid=' + str(weibo_id) + '&max_id=' + str(max_id) + '&max_id_type=1'
            web_data = requests.get(url=urlNew, headers=headers,cookies = Cookie,timeout=10)
            #成功获取数据了，才执行下一步操作
            if web_data.status_code == 200:
                js_con = web_data.json()
                # print('js_con：', js_con)
                #评论开启了精选模式，返回的数据为空
                if js_con['ok']!=0:
                    # 获取连接下一页评论的max_id
                    max_id = js_con['data']['max_id']
                    max = js_con['data']['max']
                    comments_list = js_con['data']['data']
                    # print('comments_list:',comments_list)
                    for commment_item in comments_list:
                        Obj =  {
                            'commentor_id':commment_item['user']['id'],
                            'commentor_name':commment_item['user']['screen_name'],
                            'commentor_blog_url':commment_item['user']['profile_url'],
                            'comment_id':commment_item['id'],
                            'comment_text':commment_item['text'],
                            'create_time':formatTime(commment_item['created_at'],'%a %b %d %H:%M:%S +0800 %Y','%Y-%m-%d %H:%M:%S'),
                            'like_count':commment_item['like_count'],
                            'reply_number':commment_item['total_number'],
                            'full_path':base_url+str(weibo_id),
                            'max_id': max_id,
                            'max':max
                        }
                        commentLists.append(Obj)
                    count += 1
                    print("已获取第" + str(count+1) + "页的评论。")
                    orther_page_comments(count,weibo_id,url,headers,max,max_id)#递归
                    return commentLists
                else:
                    return []
        except Exception as e:
            if count==1:
                print("遇到异常,爬虫失败") #假设连第一条数据都没有爬到，我就认为是爬虫失败
    else:
        return

#将数据保存到excel中的不同sheet中
def export_excel(exportArr,id,sheetName):
     #创建sheet
     # wb = openpyxl.load_workbook(excel_name)
     # wb.create_sheet(title=sheetName, index=0)
     # wb.save(excel_name)

     #将数据保存到sheet中
     pf = pd.DataFrame(exportArr)     #将字典列表转换为DataFrame
     order = ['comment_id','commentor_name','commentor_id','commentor_blog_url','comment_text','create_time','like_count','reply_number','full_path']     #指定字段顺序
     pf = pf[order]
     #将列名替换为中文
     columns_map = {
          'comment_id':'comment_id',
          'commentor_name':'评论者名字',
          'commentor_id':'评论者id',
          'commentor_blog_url':'评论者的微博主页',
          'comment_text':'评论内容',
          'create_time':'发布时间',
          'like_count':'点赞数',
          'reply_number':'回复数',
          'full_path':'微博url',
     }
     pf.rename(columns=columns_map, inplace=True)
     pf.fillna(' ',inplace = True)     # 替换空单元格
     pf.to_excel(file_path,encoding = 'utf-8',index = False,sheet_name=sheetName)     #输出

     print('----------第',id,'篇微博的评论已经保存了---------------')
     return 'true'

#将数据保存到txt文件中
def export_txt(list,txtId):
    arr = [str(txtId),'   ',list['full_path'],'   ',list['commentor_name']]
    commentorNameMaxLen = 20 #假设最大的长度为20，不足20的以空格代替，确保长度一致，避免参差不齐
    lenGap = commentorNameMaxLen - len(list['commentor_name'])
    for i in range(lenGap):
        arr.append('-')
    arr.append(list['comment_text'])
    arr.append('\n') #每一行结束要换行
    file_handle.writelines(arr)

if __name__ == "__main__":
    output = []
    commentLists = []  # 初始化存储一个微博评论数组
    weibo_comment = weiboComment

    file_path = pd.ExcelWriter(excel_name)  # 指定生成的Excel表格名称

    txt_id = 1  # 用于记录txt数据的id
    file_handle = open(txt_name, mode='w',encoding='utf-8')  # 打开txt文件
    file_handle.writelines(['id    ','微博链接                          ','评论者','                              ','评论内容\n']) #写入头部的字段名字

    #存储每一篇微博的评论数据
    for ind,item in enumerate(weibo_comment):
        output = first_page_comment(item['weibo_id'], url, headers)
        if len(output)>0:
            maxPage = output[-1]['max']
            maxId =output[-1]['max_id']
            #如果结果不只一页，就继续爬
            if(maxPage!=1):
                ans = orther_page_comments(0,item['weibo_id'], url, headers,maxPage,maxId)
                # 如果评论开启了精选模式，最后一页返回的数据是为空的
                if ans!=[]:
                    bool = export_excel(ans,item['id'],item['sheet_name'])
                else:
                    bool = export_excel(commentLists,item['id'],item['sheet_name'])

                if bool=='true':
                    commentLists = [] #将存储的数据置0
                    for list in ans:
                        txt_id = txt_id + 1  # 用于记录txt数据的id
                        export_txt(list, txt_id)
            else:
                print('----------------该微博的评论只有1页-----------------')

    file_path.save()    #保存到表格
    file_handle.close() #保存到txt