网站模拟登陆
============

介于用户直接登录与第三方登录之间, 姑且称之为 第 2 方登录. :)

翻译成普通话就是:
**模拟浏览器, 实现各网站的自动登陆**

本质为获取登录后的 cookie

#### 网站列表

- [renren.com]()
- [易网通物流平台](http://mf.sealink.net.cn/)

#### 用法

`config/` 目录下, 网站的配置文件，保存为 `website_name.json`

```shell
$ python login.py website_name
```

如: `python login.py renren`

#### 验证码自动识别

```python
$ python authcode.py htt://url/to/authcode
```

如:

```shell
$ python authcode.py http://mf.sealink.net.cn/authcode
# output: ('JSESSIONID=38F1DFB4AE861EFFB722FFA53DC50AA3.mqbak; Path=/', '9936')
$ python authcode.py http://newmf.szedi.com.cn/jsp/common/g_image.jsp
# output: ('JSESSIONID=12AE7574ADD763758232D6D25D8BB590; Path=/', '0828')
```
