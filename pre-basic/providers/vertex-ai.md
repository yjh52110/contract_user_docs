Vertex AI
=========

暂时不支持Claude模型

[hashtag](#jiao-cheng-gai-shu)

教程概述

----------------------------------------

### 

[hashtag](#id-1.-huo-qu-api-key)

1\. 获取 API Key

*   获取 Gemini 的 API Key 前，你需要有一个 Google Cloud 项目（如果你已有，此过程可跳过）
    
*   进入 [Google Cloudarrow-up-right](https://console.cloud.google.com/projectcreate) 创建项目，填写项目名称并点击创建项目
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-ad77591b61b1437f996bd5e9cface0efd0a5af88%252Fimage%2520%283%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=f5b2ff5d&sv=2)

*   进入[Vertex AI控制台arrow-up-right](https://console.cloud.google.com/vertex-ai)
    
*   在创建的项目中开通 [Vertex AI APIarrow-up-right](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1&invt=Ab0iBA)
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-5e26022527ccd36f198cc21fb5c05df7e12d481b%252Fimage%2520%2878%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=f319da76&sv=2)

[hashtag](#id-2.-she-zhi-api-fang-wen-quan-xian)

2\. 设置 API 访问权限

---------------------------------------------------------------------

*   打开 [服务账号arrow-up-right](https://console.cloud.google.com/iam-admin/serviceaccounts) 权限界面，创建服务账号
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-dc8d12046e5882f9046715beebc288c976ddb609%252Fimage%2520%2879%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=5ff15d51&sv=2)

*   在服务账号管理页面找到刚刚创建的服务账号，点击`密钥`并创建一个新的 JSON 格式密钥
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-ee58e30b804b135cc087d35eb95c8db243bb90be%252Fimage%2520%2880%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8b00e870&sv=2)

*   创建成功后，密钥文件将会以 JSON 文件的格式自动保存到你的电脑上，请 **妥善保存**
    

[hashtag](#id-3.-zai-cherry-studio-zhong-pei-zhi-vertex-ai)

3\. 在Cherry Studio中配置Vertex AI

-----------------------------------------------------------------------------------------------

*   选择Vertex AI服务商
    
*   将JSON文件的对应字段填入
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-52c727382f1d9f8eebdfc20a9929d7fe612532dd%252Fimage%2520%2881%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=b24ac500&sv=2)

点击添加 [模型arrow-up-right](https://console.cloud.google.com/vertex-ai/model-garden)，就可以愉快地开始使用了！

[上一页Google Geminichevron-left](/pre-basic/providers/google-gemini)[下一页NewAPIchevron-right](/pre-basic/providers/newapi)

最后更新于2个月前

*   [教程概述](#jiao-cheng-gai-shu)
*   [1\. 获取 API Key](#id-1.-huo-qu-api-key)
*   [2\. 设置 API 访问权限](#id-2.-she-zhi-api-fang-wen-quan-xian)
*   [3\. 在Cherry Studio中配置Vertex AI](#id-3.-zai-cherry-studio-zhong-pei-zhi-vertex-ai)
