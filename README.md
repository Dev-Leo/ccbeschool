# **校园e码自动打卡**
## **介绍**
此脚本用于校园e码通自动签到（中国建设银行旗下产品）

由于老是忘记，便撸出此脚本

截至目前为止Cookie暂未出现失效情况
## **用法**
您只需在微信小程序里抓包将然后Cookie填入至request()模块的
```
cs = {'Cookie': 'Your Cookie'}
```
处
然后将Post上传的内容抓包并格式化处理，填至
```
datas = {


  }
```
推荐使用
[Json在线解析及格式化](https://www.json.cn/)

最后在
```
post_url = "You DingTalk Api"
"text": {

         "content":"此处填写你的API关键词"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+msg

    }
```
填入钉钉webhook机器人Api,和您的关键词即可完成此脚本的配置（[如何申请钉钉WebHook API?](https://www.baidu.com/s?tn=80035161_2_dg&wd=%E5%A6%82%E4%BD%95%E7%94%B3%E8%AF%B7%E9%92%89%E9%92%89WebHook+API)）

## **运行**
Linux可以采用**crontab**定时执行
Windows可以采用**计划任务**
也可以采用[使用python定时执行py脚本](https://ptype.info/2020/03/17/使用python定时执行py脚本/)
```
Python run.py
```
The End!
