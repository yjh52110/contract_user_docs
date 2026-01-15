route调用链使用教程
============

[hashtag](#gong-neng-jie-shao)

功能介绍

----------------------------------------

调用链（又称“trace”）为用户提供对话的洞察能力，帮助用户觉察模型、知识库、MCP、网络搜索等在对话过程中的具体表现。它是一个基于 [OpenTelemetryarrow-up-right](https://opentelemetry.io/docs/languages/js/) 实现的可观测工具，通过端侧采集、存储、处理数据实现可视化，为定位问题、优化效果提供量化评估依据。

每次对话对应一条 trace 数据，一条 trace 由多个 span 组成，每个 span 对应 Cherry Studio 的一个程序处理逻辑如调用模型会话、调用 MCP 、调用知识库、调用网络搜索等。trace 以树结构展示，span 为树节点，主要数据包括耗时、token 使用量，当然在 span 详情还可以查看其具体的输入输出。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-a77fc14ce4cb0ffbc5adaec47be4a01f99969065%252Ftrace2.gif%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=e7a69394&sv=2)

[hashtag](#kai-qi-trace)

开启 Trace

--------------------------------------

默认情况下，Cherry Studio 安装之后，Trace 是隐藏的状态。需要在 "设置"-"常规设置" - "开发者模式" 中开启，如下图：

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-51a20a658707f8b05ecb7c916294bbdc4625d126%252Fimage%2520%2884%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=50acb102&sv=2)

且对于之前的会话不会产生 Trace 记录，只会在新的问答产生之后才会产生 Trace 记录。所产生的记录存储在本地，如需要彻底清除 Trace ，可以通过 "设置" - "数据设置" - "数据目录" - "清除缓存" 进行清除，也可通过手动 删除 ~/.cherrystudio/trace 下的文件进行清除，如下图：

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-0c7e2a505de874126b9829e37558911bd9234999%252Fimage%2520%2885%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=7819bfa7&sv=2)

[hashtag](#chang-jing-jie-shao)

场景介绍

-----------------------------------------

### 

[hashtag](#quan-lian-lu-cha-kan)

全链路查看

在 Cherry Studio 对话框中点击调用链查看调用链的全链路数据。无论在对话过程中调用了模型，还是网络搜索、知识库、MCP，都可以在调用链窗口中查看到全链路调用数据。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-93148219202487564661df7da68d65fafac3f2da%252Fimage%2520%281%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=b79e5452&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-481e8ba6b2a0e70ad2995e3ab6e0e3726e0bbffd%252Fimage%2520%2886%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1586379a&sv=2)

### 

[hashtag](#cha-kan-lian-lu-zhong-mo-xing)

查看链路中模型

若想要查看调用链中模型的详情，可以点击模型调用节点，查看其输入、输出详情。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-0e8486369f67c8e71c2c07919e30c70760478561%252Fimage%2520%2887%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=6d6b3bb9&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2d49faa56aebd28fdaf20cb9dbb2d9ca4c6cfd8e%252Fimage%2520%2888%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=654eca49&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-96f238d70d1f1a0dcd22d813bdb3af3ebe848d96%252Fimage%2520%2889%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=9b7fc63a&sv=2)

### 

[hashtag](#cha-kan-lian-lu-zhong-wang-luo-sou-suo)

查看链路中网络搜索

若想要查看调用链中网络搜索的详情，可以点击网络搜索调用节点，查看其输入、输出详情。在详情中，可以查看到调用网络搜索查询的问题和其返回的结果。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-21ecbb9de818aab2bdeff80c192e332952299caf%252Fimage%2520%282%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=737c60ae&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2415d142d53d895e2509792d905ca96a013cf89f%252Fimage%2520%28150%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=9fffcb64&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-8e335e3aebcaa6752565ddc1dca50022f91dde0b%252Fimage%2520%28151%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=51294c66&sv=2)

### 

[hashtag](#cha-kan-lian-lu-zhong-zhi-shi-ku)

查看链路中知识库

若想要查看调用链中知识库的详情，可以点击知识库调用节点，查看其输入、输出详情。在详情中，可以查看到调用知识库查询的问题和其返回的答案。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-4700709368687dbc376e37876bad6c08618ce9f2%252Fimage%2520%28152%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=ad5a24d6&sv=2)

### 

[hashtag](#cha-kan-lian-lu-zhong-mcp-diao-yong-qing-kuang)

查看链路中 MCP 调用情况

若想要查看调用链中 MCP 的详情，可以点击 MCP 调用节点，查看其输入、输出详情。在详情中，可以查看到调用此 MCP Server tool 的入参和 tool 的返回。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-567f91c51a3c0d443acc9f1e115d045104f5e968%252Fimage%2520%28153%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8949fd6e&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-7086417ba8cbb04e89d9d2ef9a5d36f6044241dc%252Fimage%2520%28154%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8f3082e7&sv=2)

[hashtag](#wen-ti-he-jian-yi)

问题和建议

----------------------------------------

当前功能由阿里云 [EDASarrow-up-right](https://www.aliyun.com/product/edas) 团队提供，如有问题或建议，请进入钉钉群 （ 群号： 21958624 ） 与开发者进行深度沟通。

\\

[上一页常见问题chevron-left](/advanced-basic/mcp/chang-jian-wen-ti)[下一页Code Tools 使用教程chevron-right](/advanced-basic/code-tools-shi-yong-jiao-cheng)

最后更新于28天前

*   [功能介绍](#gong-neng-jie-shao)
*   [开启 Trace](#kai-qi-trace)
*   [场景介绍](#chang-jing-jie-shao)
*   [全链路查看](#quan-lian-lu-cha-kan)
*   [查看链路中模型](#cha-kan-lian-lu-zhong-mo-xing)
*   [查看链路中网络搜索](#cha-kan-lian-lu-zhong-wang-luo-sou-suo)
*   [查看链路中知识库](#cha-kan-lian-lu-zhong-zhi-shi-ku)
*   [查看链路中 MCP 调用情况](#cha-kan-lian-lu-zhong-mcp-diao-yong-qing-kuang)
*   [问题和建议](#wen-ti-he-jian-yi)
