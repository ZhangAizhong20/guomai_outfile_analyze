import csv
import appbuilder
import os
import pandas as pd

file_path = 'D:\\工作\\示例\\聚类：每一类的关键词.csv'
data = pd.read_csv(file_path,encoding='ANSI')
labels = data.iloc[:, 0]
keywords = data.iloc[:, 1]

# 配置密钥与应用ID
os.environ["APPBUILDER_TOKEN"] ="bce-v3/ALTAK-KpyCYmIMkozAjuckpr7pB/497fe899b2ab20a8f2962b12cdd216329282692d"
app_id = "1446f45c-ae79-468e-a018-9dd3f8e40dd4" #贴标签2.0

# 初始化Agent
builder = appbuilder.AppBuilderClient(app_id)
# 创建会话ID
conversation_id = builder.create_conversation()
try:
    with (open('D:\\工作\\示例\\value.csv', 'a', newline='') as f):
        for i in range(data.shape[0]):
        #for i in range(5):
            try:
                conversation_id = builder.create_conversation()
                msg = builder.run(conversation_id, query=str(keywords[i]))
                out = msg.content.answer
                writer = csv.writer(f)
                writer.writerow([labels[i],keywords[i], out])
                print('第', labels[i], '条信息写入成功。')
                print('keywords:',keywords[i])
                print('价值原型：')
                print(out)
            except Exception:
                out = "0"
                print("异常！异常！")
                writer = csv.writer(f)
                writer.writerow([labels[i], keywords[i], out])
                f.close()
except Exception:
    f.close()
f.close()
print('信息写入完毕，共',(i+1),'条数据。')