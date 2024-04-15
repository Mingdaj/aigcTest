1. 库安装
```bash
 pip install websocket-client -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

2. 设置对话背景或者模型角色
```python
text.append({"role": "system", "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。"})
```