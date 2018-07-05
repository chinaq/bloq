# 无监督学习笔记


- [无监督学习笔记](#无监督学习笔记)
    - [聚合分类类型](#聚合分类类型)
        - [K-Mean](#k-mean)
        - [Hierarchical Clustering 层次聚类](#hierarchical-clustering-层次聚类)
        - [DBSCAN 基于密度的空间聚类](#dbscan-基于密度的空间聚类)
        - [GMM 高斯混合模型聚类](#gmm-高斯混合模型聚类)
    - [评分方式](#评分方式)
        - [外部指标](#外部指标)
        - [内部指标](#内部指标)
        - [相对指标](#相对指标)
    - [特征分析](#特征分析)
        - [PCA 主成分分析](#pca-主成分分析)
        - [Random Projection 随机投影](#random-projection-随机投影)
        - [ICA 独立成分分析](#ica-独立成分分析)
    - [分类流程](#分类流程)





## 聚合分类类型
### K-Mean
- skip

### Hierarchical Clustering 层次聚类
- 单连接聚类法
    - ![](./img/single_link.png)
    - ![](./img/single_link_result.png)
    - ![](./img/single_link_dendrogram.png)
- 凝聚聚类法
    - COMPLETE LINK 全连接聚类法
    - AVERAGE LINK 组平均聚类法
    - WARDS 离差平方和法
    - ![](./img/hierarchical_advan.png)
    - ![](./img/hierarchical_implementation.png)
    - ![](./img/hierarchical_dendrogram.png)
    - ![真菌分类](./img/hierarchical_applications.png)

### DBSCAN 基于密度的空间聚类
- ![](./img/dbscan.png)
- ![](./img/dbscan_result.png)
- ![](./img/dbscan_advan.png)
- ![](./img/dbscan_implementation.png)
- ![网络流量分类](./img/dbscan_applications.png)
- 
### GMM 高斯混合模型聚类
- ![](./img/gmm_example.png)
- ![](./img/gmm_advan.png)
- ![](./img/gmm_implementation.png)
- ![依据加速传感器进行行为分类](./img/gmm_applications.png)
- ![静态背景识别](./img/gmm_application_2.png)





## 评分方式
- ![](./img/cluster_validation.png)

### 外部指标
- ![](./img/cluster_validation_external.png)
- ![](./img/ari.png)

### 内部指标
- ![](./img/sihouette_coefficient.png)
- ![](./img/sihouette_coefficient_2.png)

### 相对指标
- skip





## 特征分析
### PCA 主成分分析
- skip

### Random Projection 随机投影
- ![](./img/random_projection.png)
- ![](./img/random_projection_implementation.png)

### ICA 独立成分分析
- ![](./img/independent_component_analysis.png)
- ![](./img/independent_component_analysis_implementation.png)
- ![经济影响因素分类](./img/independent_component_analysis_applications.png)




## 分类流程
- ![](./img/cluster_analysis.png)
