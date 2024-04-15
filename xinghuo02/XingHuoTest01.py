# coding: utf-8
import XingHuoUtil

if __name__ == '__main__':
    # 封装调用
    # XingHuoUtil.conversation()

    # 是否调用历史对话
    # text.clear()

    while True:
        Input = input("\n" + "Ask: ")
        query = XingHuoUtil.checklen(XingHuoUtil.getText("user", Input))
        print("XingHuo:", end="")

        # 主程序入口
        XingHuoUtil.main(
            appid="160e4fc9",  # 填写控制台中获取的 APPID 信息
            api_secret="NGQ1NjI1OTYxYjE3MmQ5MmIwNjE3M2Vk",  # 填写控制台中获取的 APISecret 信息
            api_key="7253988c4e24e2382e86b43bb16c5267",  # 填写控制台中获取的 APIKey 信息
            # appid、api_secret、api_key三个服务认证信息请前往开放平台控制台查看（https://console.xfyun.cn/services/bm35）
            # gpt_url="wss://spark-api.xf-yun.com/v3.5/chat",
            # Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat",  # v3.0环境的地址
            # Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat",  # v2.0环境的地址
            gpt_url="wss://spark-api.xf-yun.com/v1.1/chat",  # v1.0环境的地址
            # domain="generalv3.5",
            # domain = "generalv3",    # v3.0版本
            # domain = "generalv2",    # v2.0版本
            domain="general",  # v1.0版本
            query=query
        )

        # 助手
        # answer = ""
        # getText("assistant", answer)