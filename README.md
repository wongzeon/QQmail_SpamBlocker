### QQmail_SpamBlocker
用于为QQ邮箱自动添加邮件黑名单地址，拒收这部分地址的邮件。

### 注意

⚠ 黑名单地址源于个人使用邮箱时，收取到了垃圾/反感邮件（多为广告营销、业务推荐等内容），进行了拉黑操作而得到的记录。
- 全是邮箱过滤系统的漏网之鱼，也有些是懒得去对应品牌设置拒收营销短信的

⚠ 拉黑邮箱地址会导致收不到相应地址的邮件，故请结合自己的实际使用需求，对黑名单列表进行进行替换/增加/删改。

### 使用条件

仅支持Windows操作系统使用，Python 版本 => 3.6

需要requests库，未安装的则执行`pip install requests`

0️⃣ 邮箱登录网址mail开头的为旧版，wx开头的为新版（后申请的QQ大部分是该版本）
- 例：`mail.qq.com` 和 `wx.mail.qq.com`

1️⃣ 旧版QQ邮箱：只需要sid、cookie两个参数的值

2️⃣ 新版QQ邮箱：需要sid、cookie、r三个参数的值

### 参数获取

使用PC端浏览器打开QQ邮箱页面，按F12调出开发者工具切换至`网络选项卡`，并选择`Fetch/XHR`

![控制台.png](https://ae03.alicdn.com/kf/Hbcca34e4c2b74721b7bf1b035c2e482c9.png)

随后登陆，在登陆后的Url获得`sid`参数的值，形式为`?sid=XXXXXXXXXXXXXXXXXXXXX`

![sid参数.png](https://ae01.alicdn.com/kf/Hd817ef1b1e9540c38d2d3eea8d679d75j.png)

点击任意响应地址，复制请求标头中`Cookie`的值

![cookie参数.png](https://ae04.alicdn.com/kf/H4fe20486aadd44f7a68936976f897c78I.png)

💡 如果是新版的QQ邮箱，则还要点击标头旁边的`Payload`获得`r`参数的值

### 使用方法

`python QQmail_SpamBlocker.py`运行程序

根据提示，将上述获取到的参数值依次粘贴，并按`Enter`操作即可

![cookie.png](https://ae04.alicdn.com/kf/H4ab531eee6284a33aa5f528eb8b829c2O.png)

![版本2.png](https://ae04.alicdn.com/kf/H87dc50df28274b6d908241471f32805bf.png)

### 使用提示

QQ邮箱一天仅允许拉黑100个邮箱地址，之后的提交会提示操作频繁，第二天才可继续操作。

在遇到三次错误之后，程序会自动将拉黑失败的列表保存至桌面，此后执行会优先读取拉黑失败列表继续提交。

![邮件黑名单.png](https://ae01.alicdn.com/kf/H00e96edcbe884032871a8e15bb057af8i.png)
