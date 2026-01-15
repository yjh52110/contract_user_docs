globe联网模式
=========

如何在 Cherry Studio 使用联网模式

circle-info

需要联网的场景举例：

*   时效性信息：比如今天/本周/刚刚 黄金期货价格等。
    
*   实时数据：比如天气，汇率等动态数值。
    
*   新兴知识：比如新事物，新概念，新技术等等...
    

### 

[hashtag](#yi-ru-he-kai-qi-lian-wang)

一、如何开启联网

在Cherry Studio 的提问窗口，点击 【小地球】 图标即可开启联网。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-cb8f778de6305ea2bb35dafa896c97952b4b00ef%252Fimage%2520%2894%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=167d86aa&sv=2)

点击地球图标 - 开启联网

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f04c66f5c13e3253f34a57b43c19f875b722ea29%252Fimage%2520%2896%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=9cea6f26&sv=2)

表示 - 已开启联网功能

### 

[hashtag](#er-te-bie-zhu-yi-lian-wang-you-liang-zhong-mo-shi)

二、特别注意：联网有两种模式

#### 

[hashtag](#mo-shi-1-mo-xing-fu-wu-shang-de-da-mo-xing-zi-dai-lian-wang-gong-neng)

模式1：模型服务商的大模型自带联网功能

这种情况下，开启联网后，直接就可以使用联网服务了，非常简单。

circle-exclamation

可以通过问答界面上方，模型名字后面是否带有小地球标记，迅速判断该模型是否支持联网。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-07da4cd5939d868c9b1972757c3a84278f929e15%252Fimage%2520%28100%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=4953901b&sv=2)

在模型管理页面，这个方法也可以让你快速分辨出哪些模型支持联网，哪些不支持。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-6e39205b1e054578395591315fc3e4f019f9cf07%252Fimage%2520%28101%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=808852ac&sv=2)

> **Cherry Studio 目前已经支持的联网模型服务商有**
> 
> *   Google Gemini
>     
> *   OpenRouter（全部模型支持联网）
>     
> *   腾讯混元
>     
> *   智谱AI
>     
> *   阿里云百炼等
>     

triangle-exclamation

特别注意：

存在一种特殊的情况，即便模型上没带小地球标记，但是它也能实现联网，比如下面这个攻略教程解释的情况。

[globe-pointer火山引擎接入联网](/pre-basic/websearch/volcengine)

* * *

#### 

[hashtag](#mo-shi-2-mo-xing-bu-dai-lian-wang-gong-neng-shi-yong-tavily-fu-wu-shi-xian-lian-wang-gong-neng)

模式2：模型不带联网功能，使用 Tavily服务 实现联网功能

当我们使用一个不带联网功能的大模型时（名字后面没有小地球图标），而我们又需要它获取一些实时性的信息进行处理，此时就需要用到Tavily网络搜索服务。

**初次使用Tavily服务**，会弹窗提示去设置一些信息，请根据指引操作即可-非常简单！

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-0f0173fe3ef79c0b78b2583167bc025dc34f0d4b%252Fimage%2520%28102%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=e8f023ab&sv=2)

弹窗，点击：去设置

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-444f9e0c42b8596b8d349b67d8ae43a178a3410f%252Fimage%2520%28103%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=c7b90805&sv=2)

点击获取秘钥

点击获取秘钥后，会自动跳转到**tavily的官网**登录注册页面，注册并登录后，创建APIkey，然后复制key到Cherry Studio即可。

triangle-exclamation

不会注册，参考本文档同目录下tavily联网登录注册教程。

**tavily注册参考文档：**

[binary-lockTavily 联网登录注册教程](/pre-basic/websearch/tavily)

显示下面的界面表示注册成功。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-280ece6874c287c127a49a6fd1ec8767e2abfc01%252Fimage%2520%28105%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=74fe3f25&sv=2)

复制key

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f934760703ab005d557be419940f8f7cdcca1927%252Fimage%2520%28108%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=a3b0af3b&sv=2)

粘贴key，大功告成

再来试一次看看效果。结果表明，已经正常联网搜索了，并且搜索结果数是我们设置的默认值：5个。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-c330f0581bdfe8a0984118e61288864110ceea7a%252Fimage%2520%28107%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1419a930&sv=2)

triangle-exclamation

注意：tavily 每个月有白嫖限制，超过了要付费~~

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-56eeb98a18a849c6c308f2b4dd0c5e02c3d04ae8%252Fimage%2520%28106%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8d0b6d67&sv=2)

> PS：如果发现错误，欢迎大家随时联系。

[上一页自定义服务商](/pre-basic/providers/zi-ding-yi-fu-wu-shang)[下一页免费联网模式](/pre-basic/websearch/mian-fei-lian-wang-mo-shi)

最后更新于1个月前

*   [一、如何开启联网](#yi-ru-he-kai-qi-lian-wang)
*   [二、特别注意：联网有两种模式](#er-te-bie-zhu-yi-lian-wang-you-liang-zhong-mo-shi)
