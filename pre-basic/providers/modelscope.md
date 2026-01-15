ModelScope（魔搭）
==============

[hashtag](#shen-me-shi-modelscope)

什么是 ModelScope？

-------------------------------------------------------

> ModelScope 是新一代开源模型即服务（MaaS）共享平台，致力于为泛 AI 开发者提供**灵活、易用、低成本**的一站式模型服务解决方案，让模型应用更简单！
> 
> 通过 **API-Inference 服务化能力**，平台将开源模型标准化为可调用的 API 接口，开发者可轻量、快速地集成模型能力至各类 AI 应用，支持工具调用、原型开发等创新场景。

### 

[hashtag](#he-xin-you-shi)

核心优势

*   ✅ **免费额度**：每日提供 **2000 次免费 API 调用额度**（[计费规则](/pre-basic/providers/modelscope##计费与额度规则)）
    
*   ✅ **丰富模型库**：覆盖 NLP、CV、语音、多模态等 1000+ 开源模型
    
*   ✅ **即开即用**：无需部署，通过 RESTful API 快速调用
    

* * *

[hashtag](#cherry-studio-jie-ru-liu-cheng)

Cherry Studio 接入流程

------------------------------------------------------------------

### 

[hashtag](#bu-zhou-1-huo-qu-modelscope-api-ling-pai)

步骤 1：获取 ModelScope API 令牌

1.  **登录平台**
    
    *   访问 [ModelScope 官网](https://modelscope.cn) → 点击右上角**登录** → 选择认证方式 ![登录界面](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-914b9cc6f8da04291beb8fc7c47f94b1698e50e8%252Fimage.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=76e1cbe5&sv=2)
        
    
2.  **创建访问令牌**
    
    *   进入 [**账户设置 → 访问令牌**](https://modelscope.cn/my/myaccesstoken)
        
    *   点击 `**新建令牌**` → 填写描述 → **复制生成的令牌**（_页面示例见下图_） ![新建令牌示例](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-087b472a2b37b3aa64c84094675555bbde27268b%252Fimage-7.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=56d97c17&sv=2)
        
    
    > 🔑 **重要提示**：令牌泄露将影响账号安全！
    

### 

[hashtag](#bu-zhou-2-pei-zhi-cherry-studio)

步骤 2：配置 Cherry Studio

*   打开 **Cherry Studio** → **设置 → 模型服务 → ModelScope**
    
*   在 `API 密钥` 栏粘贴复制的令牌 ![配置界面](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f29ddc9a3fbe222901f4aa894fa07304f381c161%252Fimage-2.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=60936608&sv=2)
    
*   点击 `**保存**` 完成授权
    

### 

[hashtag](#bu-zhou-3-diao-yong-mo-xing-api)

步骤 3：调用模型 API

1.  **查找支持 API 的模型**
    
    *   访问 [ModelScope 模型库](https://modelscope.cn/models)
        
    *   筛选条件：**勾选** `**API-Inference**`（或认准模型卡片上的 `API` 图标） ![API 模型筛选](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-ebb4985516d5eb1c680b6acdcd483af6e9b6bb6a%252Fimage-3.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=2cfc8b1f&sv=2)
        
    
    > API-Inference覆盖的模型范围，主要根据模型在魔搭社区中的关注程度（参考了点赞，下载等数据）来判断。因此，在能力更强，关注度更高的下一代开源模型发布之后，支持的模型清单也会持续迭代。
    
2.  **获取模型 ID**
    
    *   进入目标模型详情页 → 复制 **Model ID**（格式如 `damo/nlp_structbert_sentiment-classification_chinese-base`） ![复制 Model ID](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-7d5c8ef3b6469b38ce99280af3d92e007ce6cab4%252Fimage-5.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=90c7dd2e&sv=2)
        
    
3.  **填入 Cherry Studio**
    
    *   在模型服务配置页的 `模型 ID` 栏输入 ID → 选择任务类型 → 完成配置 ![填入模型ID](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-c0ac835ecb5d6ae1723e59573e5d2c923ec52a65%252Fimage-6.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=5fa0a40a&sv=2)
        
    

* * *

[hashtag](#ji-fei-yuedu-gui-ze)

计费与额度规则

--------------------------------------------

### 

[hashtag](#zhong-yao-shuo-ming)

重要说明

*   🎫 **免费额度**：每位用户 **每日 2000 次 API 调用**（\*以官网最新规则为准）
    
*   🔁 **额度重置**：每日 UTC+8 00:00 自动重置，**不支持跨日累计或升级**
    
*   💡 **超额处理**：
    
    *   达到当日上限后 API 将返回 `429 错误`
        
    *   解决方案：切换备用账号 / 使用其他平台 / 优化调用频率
        
    

### 

[hashtag](#cha-kan-sheng-yuedu)

查看剩余额度

*   登录 ModelScope → 点击右上角 `**用户名**` → `**API 使用情况**` ![额度查看位置](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2babab6f9646eac2f47fd895a5a074fa12db66e7%252Fimage-8.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=9324f65a&sv=2)
    

> ⚠️ 注意：推理 API-Inference 每天2000次的免费调用额度。更多调用需求可考虑使用阿里云百炼等云上服务。

[上一页GitHub Copilot](/pre-basic/providers/github-copilot)[下一页PPIO 派欧云](/pre-basic/providers/ppio)

最后更新于4个月前

*   [什么是 ModelScope？](#shen-me-shi-modelscope)
*   [核心优势](#he-xin-you-shi)
*   [Cherry Studio 接入流程](#cherry-studio-jie-ru-liu-cheng)
*   [步骤 1：获取 ModelScope API 令牌](#bu-zhou-1-huo-qu-modelscope-api-ling-pai)
*   [步骤 2：配置 Cherry Studio](#bu-zhou-2-pei-zhi-cherry-studio)
*   [步骤 3：调用模型 API](#bu-zhou-3-diao-yong-mo-xing-api)
*   [计费与额度规则](#ji-fei-yuedu-gui-ze)
*   [重要说明](#zhong-yao-shuo-ming)
*   [查看剩余额度](#cha-kan-sheng-yuedu)
