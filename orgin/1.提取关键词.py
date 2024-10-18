import csv
import appbuilder
import os
import pandas as pd

#存储选题信息的文件
file_path = 'D:\\工作\\示例\\信息_仅通过.xlsx'

data = pd.read_excel(file_path)
labels = data.iloc[:, 1]    #书名
fact = data.iloc[:, 5]      #事实层
value = data.iloc[:, 7]     #价值原型
ad = data.iloc[:, 6]        #广告层
keywords = data.iloc[:, 10]  #关键词
id = data.iloc[:, 0]        #选题编号

# 配置密钥与应用ID
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-KpyCYmIMkozAjuckpr7pB/497fe899b2ab20a8f2962b12cdd216329282692d"
app_id = "3ca11b8b-d291-4fe9-a3d7-67bfe61f174c"  #对应：贴标签

try:
    for i in range(data.shape[0]):
        #存储关键词的位置
        with open('D:\\工作\\示例\\keywords.csv', 'a', newline='') as f:
            builder = appbuilder.AppBuilderClient(app_id)
            conversation_id = builder.create_conversation()
            #以下部分为处理选题信息数据
            #将事实层、价值原型等信息合并到text
            if (value[i] != 0 and fact[i] != 0):
                text = value[i] +"。"+ fact[i]
            elif (value[i] == 0 and fact[i] != 0):
                text = fact[i]+"。"
            elif (value[i] != 0 and fact[i] == 0):
                text = value[i]+"。"
            else:
                print(labels[i], "输入有误！！")
                text = "无"
            if keywords[i] != 0:
                text = keywords[i] +"。"+ text
            if ad[i] != 0:
                text = text + "。"+ad[i]
            if len(text)>1200:
                text = text[0:1200]

            #运行
            try:
                msg = builder.run(conversation_id, query=text)
            except Exception:
                out = "0"
                print("异常！异常！")
                writer = csv.writer(f)
                writer.writerow([id[i], labels[i], out])
                f.close()
            else:
                out = msg.content.answer
                writer = csv.writer(f)
                writer.writerow([id[i],labels[i], out])
                print('第', (i + 1), '条信息写入成功。书名：', labels[i],'  |  关键词：',out)
                f.close()
except Exception:
    f.close()

print('信息写入完毕，共',(i+1),'条数据。')