网站模拟登陆
============

介于用户直接登录与第三方登录之间, 姑且称之为 第 2 方登录. :)

翻译成普通话就是:
**模拟浏览器, 实现各网站的自动登陆**

本质为获取登录后的 cookie

#### 网站列表

- renren.com

#### 用法
-----

`config/` 目录下, 网站的配置文件，保存为 `website_name.json`

```python
python login.py website_name
```

如: `python login.py renren`
