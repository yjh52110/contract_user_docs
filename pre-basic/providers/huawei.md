华为云
===

一、到[华为云arrow-up-right](https://auth.huaweicloud.com/authui/login)创建账号登录

二、点击[此链接arrow-up-right](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage)，进入Maa S控制台

三、授权

chevron-right授权步骤（已授权跳过）[hashtag](#shou-quan-bu-zhou-yi-shou-quan-tiao-guo)

1.  进入(二)的链接页面后，根据提示进入授权页面(点击IAM子用户→新增委托→普通用户)
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2f463409ce93f25a89902e6c8f519457d42c8baa%252Fimage%2520%2849%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=67fa3b85&sv=2)

1.  点击创建后重新返回(二)处链接页面
    
2.  会提示访问权限不足，点击提示里的"点击此处"
    
3.  追加已有授权并确定
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-263618a154ba83ad63acc9c658561f1936227331%252Fimage%2520%2850%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=ffa7eb1d&sv=2)

注意：该方法适用于小白，不用看过多内容，只需要根据提示点击，如果你可以一次性授权成功按照自己的方式来即可。

四、点击侧栏鉴权管理，创建API Key（秘钥）并复制

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2672340643b2a9ef33eab076fe56be201a679d34%252F%25E5%25BE%25AE%25E4%25BF%25A1%25E6%2588%25AA%25E5%259B%25BE_20250214034650.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1123f072&sv=2)

然后在CherryStudio里创建新服务商

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-60e007eca5ef4773bf68f85b811574d46f7c6d7d%252Fimage%2520%281%29%2520%282%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1f0cc6c9&sv=2)

创建完成后填入秘钥

五、点击侧栏模型部署，全部领取

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-bafa420ba6bee9daa4a418b25a2d2a92266ad4e4%252F%25E5%25BE%25AE%25E4%25BF%25A1%25E6%2588%25AA%25E5%259B%25BE_20250214034751.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=bf84f347&sv=2)

六、点击调用

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-fe1438fd0db72a19558c6382f76935f7d003f445%252Fimage%2520%281%29%2520%282%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=74d7dc0&sv=2)

把①处的地址复制，粘贴到CherryStudio的服务商地址当中并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

为什么加“#”号[看这里arrow-up-right](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> 当然也可以不看那里，直接按照教程操作即可；
> 
> 也可以使用删除v1/chat/completions的方法填写，只要会填按照自己方法怎么填都行，不会填务必按照教程操作。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-ee6b8bc612e627a00f71613682dbfea52d8bdeda%252Fimage%2520%282%29%2520%283%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=ffa4920b&sv=2)

然后把②处模型名称复制，到CherryStudio当中点“+添加”按钮新建模型

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e57b8d8948f93607f0300bdc8777ef7525b7b23d%252Fimage%2520%284%29%2520%283%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=4c207b99&sv=2)

输入模型名称，不要添油加醋，不要带引号，示例当中怎么写就怎么抄。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e3e55cc0068d8424cf221198477826aa5621dda8%252Fimage%2520%283%29%2520%283%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=a7112254&sv=2)

点击添加模型按钮即可添加完成。

circle-info

在华为云当中由于每个模型的地址不一样，所以每个模型都需要新建一个服务商，按照以上步骤重复操作即可。

[上一页火山引擎chevron-left](/pre-basic/providers/doubao)[下一页无问芯穹chevron-right](/pre-basic/providers/wu-wen-xin-qiong)

最后更新于11个月前
