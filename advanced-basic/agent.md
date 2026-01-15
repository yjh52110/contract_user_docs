robotAgent 使用教程
===============

Cherry Studio v1.7.0.alpha 版本引入了Agent，可以在 Cherry Studio 中使用 Cherry Agent 。本教程将引导您完成设置和启动的完整流程。

### 

[hashtag](#id-1.-chuang-jian-anthropic-lei-xing-de-gong-ying-shang)

1\. 创建 Anthropic 类型的供应商

任意支持 Anthropic 端点的服务商都可以使用，以 CherryIn 为例，创建一个新的 Agent 服务商，填写好密钥和地址，添加任意模型即可。

circle-exclamation

Agent 模式消耗 token 量很大，请注意 token 使用

circle-info

订阅了 Claude Code 的用户也可以将 key 和 url 地址填入获取到模型

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-32d2ea574cdc8fdbd25bedcc32c5a6b73bcd6a2d%252FCleanShot%25202025-10-12%2520at%252020.26.35%25402x.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=9af8147b&sv=2)

### 

[hashtag](#id-2.-kai-qi-api-fu-wu-qi)

2\. 开启 API 服务器

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-b84c3086a966dd46f70b5259bc060e73e659783f%252FCleanShot%25202025-10-12%2520at%252019.56.22%25402x.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8abca5da&sv=2)

### 

[hashtag](#id-3.-chuang-jian-yi-ge-agent)

3\. 创建一个 Agent

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-b67cac7871a02247ae2f6564c2bd6a2265fa4687%252FCleanShot%25202025-10-12%2520at%252020.24.43%25402x.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=b1d1d50c&sv=2)

右键 Agent 可以进入编辑界面，编辑 Agent 的权限和可以使用的工具或 mcp 服务。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e33f3092e880239cfc820f49c69efd7847d81b9b%252FCleanShot%25202025-10-12%2520at%252020.25.10%25402x.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=e795238e&sv=2)

### 

[hashtag](#jie-guo-zhan-shi)

结果展示

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-bd2fcce9c58023771bb55346670f03d6fcb0ab8f%252FCleanShot%25202025-10-12%2520at%252020.30.26%25402x.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=67ede0c2&sv=2)

[上一页Code Tools 使用教程](/advanced-basic/code-tools-shi-yong-jiao-cheng)[下一页贡献代码](/contribution/code)

最后更新于2个月前

*   [1\. 创建 Anthropic 类型的供应商](#id-1.-chuang-jian-anthropic-lei-xing-de-gong-ying-shang)
*   [2\. 开启 API 服务器](#id-2.-kai-qi-api-fu-wu-qi)
*   [3\. 创建一个 Agent](#id-3.-chuang-jian-yi-ge-agent)
*   [结果展示](#jie-guo-zhan-shi)
