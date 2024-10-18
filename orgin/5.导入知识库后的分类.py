import csv
import appbuilder
import os
import pandas as pd
import json

file_path = 'D:\\工作\\最新\\信息——仅未通过.xlsx'
data = pd.read_excel(file_path)
labels = data.iloc[:, 1]
fact = data.iloc[:, 7]
value = data.iloc[:, 9]
ad = data.iloc[:, 8]
keywords = data.iloc[:, 24]
id = data.iloc[:, 0]
# 配置密钥与应用ID
os.environ["APPBUILDER_TOKEN"] ="bce-v3/ALTAK-KpyCYmIMkozAjuckpr7pB/497fe899b2ab20a8f2962b12cdd216329282692d"
app_id = "ad44cd34-5789-4453-bc05-5cbffba0c9b1"

try:
    for i in range(data.shape[0]):
        with (open('D:\\工作\\示例\\value_new.csv', 'a', newline='') as f):
            builder = appbuilder.AppBuilderClient(app_id)
            conversation_id = builder.create_conversation()
            if (value[i] != 0 and fact[i] != 0):
                text = value[i] +"。"+ fact[i]
            elif (value[i] == 0 and fact[i] != 0):
                text = fact[i]+"。"
            elif (value[i] != 0 and fact[i] == 0):
                text = value[i]+"。"
            else:
                print(labels[i], "输入有误！！")
                text = "无"

            text = "调用组件，输入以下内容，准确地输出组件返回的内容："+text


            if len(text)>1000:
                text = text[0:1000]
            try:
                msg = builder.run(conversation_id, query=text)
                out = msg.content.answer
            except Exception:
                out = "0"
                print("异常！异常！")
                writer = csv.writer(f)
                writer.writerow([id[i], labels[i], out])
                f.close()
            else:
                answer = json.loads(msg.content.answer)
                out = answer["out"][0]
                #g.content.answer
                writer = csv.writer(f)
                writer.writerow([id[i],labels[i], out])
                print('第', (i + 1), '条信息写入成功。书名：', labels[i],out)

                f.close()
except Exception:
    f.close()
print('信息写入完毕，共',(i+1),'条数据。')
