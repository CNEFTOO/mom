# Mom Web框架

一个小巧的，基于python3标准库构建的http web框架。

## 安装

```bash
pip install mom
```

## 简单实用
```python
from mom import MomApp

app = MomApp()

@app.route("/")
def index(request):
    return "Hello World"

if __name__ == "__main__":
    app.run()
```

---
that's all
