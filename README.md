# 邮件分类器

本项目使用Transformer模型对邮件进行垃圾邮件（spam）和正常邮件（ham）的分类。

## 数据集来源

数据集来自 [SpamAssassin公共语料库](https://spamassassin.apache.org/old/publiccorpus/)

## 使用Conda进行环境配置

1. 确保您已安装Anaconda或Miniconda。

2. 克隆此仓库：
   ```
   git clone https://github.com/sirius2alpha/spamDetector.git
   cd spamDetetor
   ```

3. 创建并激活Conda环境：
   ```
   conda env create -f environment.yml
   conda activate email_classifier
   ```

## 运行项目

完成环境设置后，您可以使用以下命令运行项目：

```
python main.py
```

这将处理数据、训练模型并评估其性能。

## 项目结构

- `data_processor.py`: 处理数据加载和处理
- `data_preprocessor.py`: 为模型准备数据
- `model.py`: 定义Transformer模型
- `trainer.py`: 包含模型训练逻辑
- `evaluator.py`: 评估训练好的模型
- `main.py`: 协调整个处理过程
- `environment.yml`: 定义Conda环境

## 依赖要求

请查看 `environment.yml` 文件以获取依赖列表。