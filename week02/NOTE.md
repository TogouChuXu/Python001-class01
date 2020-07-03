学习笔记


1.需要注意在使用requests模拟登录时,如果报403(跨站违规)错误时,可先检查Request Headers参数是否设置完整。
关于特殊的Headers参数（X-Requested-With）,请参考https://blog.csdn.net/cyz52/article/details/88587889,
也是作为服务器反爬的简单处理手段之一。