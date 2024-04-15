# coding:utf-8

from XingHuoUtil import SparkAPI

# 默认api接口版本为3.1，配置其他版本需要指定Version参数（2.1或者1.1）
sparkAPI = SparkAPI(
    app_id="160e4fc9",
    api_secret="NGQ1NjI1OTYxYjE3MmQ5MmIwNjE3M2Vk",
    api_key="7253988c4e24e2382e86b43bb16c5267",
    # 版本
    version=1.1,
    # 助手id
    # assistant_id="xyzspsb4i5s7_v1"
)

if __name__ == "__main__":
    # 一次
    # sparkAPI.chat()

    # 流式
    sparkAPI.chat_stream()


