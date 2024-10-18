import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import jieba
import csv

# 读取csv文件中的数据
file_path = 'D:\\工作\\示例\\keywords.csv'
data = pd.read_csv(file_path,encoding='ANSI')

# 提取标签和目标文本
labels_true = data.iloc[:, 1]
documents = data.iloc[:, 2]
documents = [" ".join(jieba.cut_for_search(doc)) for doc in documents]

# 使用TF-IDF进行特征提取
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# 使用KMeans进行聚类
true_k = 4 # 设定聚类数量，可以根据需要调整
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1, n_init=1)
model.fit(X)

# 输出聚类结果
print("每个类的关键词")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()

with open('D:\\工作\\聚类：每一类的关键词.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(true_k):
        print(f"Cluster {i}:")
        out = ""
        for ind in order_centroids[i, :10]:#这里可以选择输出关键词的数量
            out = out + terms[ind]+ "、"
            print(f' {terms[ind]}')
        writer.writerow([i, out])
f.close()

# 为每个选题分配标签
labels = model.labels_
with open('D:\\工作\\聚类：每本书的标签.csv', 'w', newline='') as f:
    for i, (true_label, doc, cluster_label) in enumerate(zip(labels_true, documents, labels)):
        writer = csv.writer(f)
        writer.writerow([i, true_label, cluster_label])
        print(f"Document {i} (True label: {true_label}): Cluster {cluster_label}")
f.close()

with open('D:\\工作\\聚类：每个类下的书.csv', 'w', newline='') as f:
    for i in range(true_k):
        cluster_documents = [labels_true[idx] for idx in range(len(labels)) if labels[idx] == i]
        writer = csv.writer(f)
        writer.writerow([i, cluster_documents])
        print(f"Cluster {i} documents:")
        print(cluster_documents)
        print()
f.close()