message对话界面
===========

[hashtag](#zhu-shou-he-hua-ti)

助手和话题

-----------------------------------------

### 

[hashtag](#zhu-shou)

助手

`助手` 是对所选模型做一些个性化的设置来使用模型，如提示词预设和参数预设等，通过这些设置让所选模型能更加符合你预期的工作。

`系统默认助手` 预设了一个比较通用的参数（无提示词），您可以直接使用或者到 [智能体页面](/cherry-studio/preview/agents) 寻找你需要的预设来使用。

### 

[hashtag](#hua-ti)

话题

`助手` 是 `话题` 的父集，单个助手下可以创建多个话题（即对话），所有 `话题` 共用 `助手` 的参数设置和预设词（prompt）等模型设置。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f42c7ac703caf2c1f608b9efb5f37ea5842568b3%252Fimage%2520%284%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=d1d55e90&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-88e419432e2aba2e36c7b04886daaa6c47ad33dd%252Fimage%2520%285%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=46ab2b21&sv=2)

[hashtag](#dui-hua-kuang-nei-an-niu)

对话框内按钮

------------------------------------------------

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-3aaff25c1313540731b25c1aca4d75a36ee9451d%252F%25E5%25AF%25B9%25E8%25AF%259D%25E6%25A1%2586.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=94c73c8c&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-cf1413bf8721d89dde0557b5cc44b2948e56dfa6%252F%25E6%2596%25B0%25E8%25AF%259D%25E9%25A2%2598.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=abc2e175&sv=2) `新话题` 在当前助手内创建一个新话题。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-5661e25951fd0c1481100fc50727335ba7f0dd14%252F%25E4%25B8%258A%25E4%25BC%25A0%25E5%259B%25BE%25E7%2589%2587%25E6%2588%2596%25E6%2596%2587%25E6%25A1%25A3.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=545e318c&sv=2) `上传图片或文档` 上传图片需要模型支持，上传文档会自动解析为文字作为上下文提供给模型。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-526073fef616bc523921de87361993d481ad488d%252F%25E7%25BD%2591%25E7%25BB%259C%25E6%2590%259C%25E7%25B4%25A2.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=7dc3928f&sv=2) `网络搜索` 须在设置中配置网络搜索相关信息，搜索结果作为上下文返回给大模型，详见 [联网模式](/pre-basic/websearch)。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-dbb08f687dc332b310ce61dcfe1d6b68c1d72e04%252F%25E7%259F%25A5%25E8%25AF%2586%25E5%25BA%2593.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=2256ddde&sv=2) `知识库` 开启知识库，详见 [知识库教程](/knowledge-base/knowledge-base)。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-872a6c44a7a5e5b45e7d361a61a30e32c026c8f1%252FMCP%2520%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=454674c1&sv=2) `MCP 服务器` 开启 MCP 服务器功能，详见 [MCP 使用教程](/advanced-basic/mcp)。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-3836f7e6ebb36521cdcad6a594b24d60b0581bd4%252F%25E7%2594%259F%25E6%2588%2590%25E5%259B%25BE%25E7%2589%2587.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=478c5a65&sv=2) `生成图片` 只有选择的 **对话模型** 支持生图时才会显示。（非对话生图模型请前往 [绘图](/cherry-studio/preview/drawing)）

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-9c9912663de035b254cf2ed6e2fd56a2f8f26868%252F%25E9%2580%2589%25E6%258B%25A9%25E6%25A8%25A1%25E5%259E%258B.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=7401c09a&sv=2) `选择模型` 对于接下来的对话，切换成指定的模型，保留上下文。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f5675c45a5a68efda2a616787bd66b292846d490%252F%25E5%25BF%25AB%25E6%258D%25B7%25E7%259F%25AD%25E8%25AF%25AD.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=e1dd0aab&sv=2) `快捷短语` 需要先在设置中预设常用短语，在此处调用，直接输入，支持变量。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-1fd692a42b547ef8e6a072e3fb30932d427d89d7%252F%25E6%25B8%2585%25E7%25A9%25BA%25E6%25B6%2588%25E6%2581%25AF.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=96ba5315&sv=2) `清空消息` 删除该话题下所有内容。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-1780d94a942c2b66e203ac4548d8bf812ead712a%252F%25E5%25B1%2595%25E5%25BC%2580.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=fefaad24&sv=2) `展开` 让对话框变得更大，以便输入长文。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-1f0e45f09154792de99a39cc1e1a2b36abdf030e%252F%25E6%25B8%2585%25E9%2599%25A4%25E4%25B8%258A%25E4%25B8%258B%25E6%2596%2587.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=db834e71&sv=2) `清除上下文` 在不删除内容的情况下，截断模型能获得的上下文，也就是说模型将“忘记”之前的对话内容。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-30f71a4a26f0799192e509db2e0e772124d824df%252F%25E9%25A2%2584%25E4%25BC%25B0%2520Token%2520%25E6%2595%25B0.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=9babfeb3&sv=2) `预估 Token 数` 展示预估 Token 数，四个数据分别为 `当前上下文数` 、 `最大上下文数` （ ∞ 表示无限上下文）、 `当前输入框内消息字数` 、 `预估 Token 数` 。

circle-info

此功能仅用于预估 Token 数，实际 Token 数每个模型都是不一样的，请以模型提供商的数据为准。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-d8a576e68ce424a77855e9a0576c4289f810e90b%252F%25E7%25BF%25BB%25E8%25AF%2591.png%3Falt%3Dmedia&width=300&dpr=4&quality=100&sign=5c0d9dfc&sv=2) `翻译` 将当前输入框内内容翻译成英文。

[hashtag](#dui-hua-she-zhi)

对话设置

-------------------------------------

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-f4d63cf4c997640685ce9272306f494cecbc5a21%252Fimage%2520%287%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=459df0a7&sv=2)

### 

[hashtag](#mo-xing-she-zhi)

模型设置

模型设置与助手设置当中的 `模型设置` 参数同步，详见 [助手设置](/cherry-studio/preview/chat#bian-ji-zhu-shou)。

circle-info

在对话设置当中，仅该模型设置作用于当前助手，其余设置作用于全局。如：设置消息样式为气泡后在任何助手的任何话题下都是气泡样式。

### 

[hashtag](#xiao-xi-she-zhi)

消息设置

#### 

[hashtag](#xiao-xi-fen-ge-xian)

`**消息分割线**`:

使用分割线将消息正文与操作栏隔开。

打开时

关闭时

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-1cd15d571ad0b6144a8dc2e92bda6a3083e4d160%252Fimage%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=2c5c04dc&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-61b8c240fe85579b4fa73c21d528a705eb349e16%252Fimage%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=69101c11&sv=2)

#### 

[hashtag](#shi-yong-chen-xian-zi-ti)

`**使用衬线字体**`：

字体样式切换，现在你也可以通过 [自定义css](/pre-basic/personalization-settings) 来更换字体。

#### 

[hashtag](#dai-ma-xian-shi-hang-hao)

`**代码显示行号**`：

模型输出代码片段时显示代码块行号。

关闭时

打开时

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-aa43193e2c7fc76ceed2dbde158800d4330523b1%252Fimage%2520%282%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=65c282d&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-8673939ed5840be720221c4c39fe48f78087a995%252Fimage%2520%283%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=556638a8&sv=2)

#### 

[hashtag](#dai-ma-kuai-ke-zhe-die)

`**代码块可折叠**`：

打开后，当代码片段中代码较长时，将自动折叠代码块。、

#### 

[hashtag](#dai-ma-kuai-ke-huan-hang)

`**代码块可换行**`：

打开后，当代码片段中但行代码较长时（超出窗口），将自动换行。

#### 

[hashtag](#si-kao-nei-rong-zi-dong-zhe-die)

`**思考内容自动折叠**`：

打开后，支持思考的模型在思考完成后会自动折叠思考过程。

#### 

[hashtag](#xiao-xi-yang-shi)

`**消息样式**`：

可切对话界面换为气泡样式或列表样式。

#### 

[hashtag](#dai-ma-feng-ge)

`**代码风格**`：

可切换代码片段的显示风格。

#### 

[hashtag](#shu-xue-gong-shi-yin-qing)

`**数学公式引擎**`：

*   KaTeX 渲染速度更快，因为它是专门为性能优化设计的；
    
*   MathJax 渲染较慢，但功能更全面，支持更多的数学符号和命令。
    

#### 

[hashtag](#xiao-xi-zi-ti-da-xiao)

`**消息字体大小**`：

调整对话界面字体的大小。

### 

[hashtag](#shu-ru-she-zhi)

输入设置

#### 

[hashtag](#xian-shi-yu-gu-token-shu)

`**显示预估 Token 数**`：

在输入框显示输入文本预估消耗的Token数（非实际上下文消耗的Token，仅供参考）。

#### 

[hashtag](#chang-wen-ben-nian-tie-wei-wen-jian)

`**长文本粘贴为文件**`：

当从其他地方复制长段文本粘贴到输入框时会自动显示为文件的样式，减少后续输入内容时的干扰。

#### 

[hashtag](#markdown-xuan-ran-shu-ru-xiao-xi)

`**Markdown 渲染输入消息**`：

关闭时只渲染模型回复的消息，不渲染发送的消息。

关闭时

打开时

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-3579820725b91f4ea8db35f24f9ef4dd9c74f0b6%252Fimage%2520%284%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=46428cb2&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e9d7ad8be652bf20311d1b13b6ef2ef8b2a25e3c%252Fimage%2520%286%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=c9744228&sv=2)

#### 

[hashtag](#kuai-su-qiao-ji-3-ci-kong-ge-fan-yi)

`**快速敲击3次空格翻译**`：

在对话界面输入框输入消息后，连敲三次空格可翻译输入的内容为英文。

circle-exclamation

注意：该操作会覆盖原文。

#### 

[hashtag](#mu-biao-yu-yan)

`**目标语言**`：

设置输入框翻译按钮以及快速敲击3次空格翻译的目标语言。

[hashtag](#zhu-shou-she-zhi)

助手设置

--------------------------------------

在助手界面选择需要设置的助手名称→在右键菜单中选对应设置

### 

[hashtag](#bian-ji-zhu-shou)

编辑助手

circle-info

助手设置作用于该助手下的所有话题。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2f01e5f78b6d6ba6c2c63243638dddbc71f822fa%252Fimage%2520%286%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=6423d50&sv=2)

#### 

[hashtag](#ti-shi-ci-she-zhi)

提示词设置

#### 

[hashtag](#ming-cheng)

`**名称**`：

可自定义方便辨识的助手名称。

#### 

[hashtag](#ti-shi-ci)

`**提示词**`：

即 prompt ，可以参照智能体页面的提示词写法来编辑内容。

#### 

[hashtag](#mo-xing-she-zhi-1)

模型设置

#### 

[hashtag](#mo-ren-mo-xing)

`**默认模型**`：

可以为该助手固定一个默认模型，从智能体页面添加时或复制助手时初始模型为该模型。不设置该项初始模型则为全局初始模型(即 [默认助手模型](/pre-basic/settings/default-models#mo-ren-zhu-shou-mo-xing) )。

circle-info

助手的默认模型有两种，一为 [全局默认对话模型](/pre-basic/settings/default-models#mo-ren-zhu-shou-mo-xing) ，另一为助手默认模型；助手的默认模型优先级高于全局默认对话模型。当不设置助手默认模型时，助手默认模型=全局默认对话模型。

#### 

[hashtag](#zi-dong-zhong-zhi-mo-xing)

`**自动重置模型**`：

打开时 - 当在该话题下使用过程中切换其他模型使用时，再次新建话题会将新话题的重置为助手的默认模型。当该项关闭时新建话题的模型会跟随上一话题所使用的模型。

> 如助手的默认模型为gpt-3.5-turbo，我在该助手下创建话题1，在话题1的对话过程中切换了gpt-4o使用，此时：
> 
> 如果开启了自动重置：新建话题2时，话题2默认选择的模型为gpt-3.5-turbo;
> 
> 如果未开启自动重置：新建话题2时，话题2默认选择的模型为gpt-4o。

#### 

[hashtag](#wen-du-temperature)

`**温度 (Temperature)**` ：

温度参数控制模型生成文本的随机性和创造性程度（默认值为0.7）。具体表现为：

*   低温度值(0-0.3)：
    
    *   输出更确定、更专注
        
    *   适合代码生成、数据分析等需要准确性的场景
        
    *   倾向于选择最可能的词汇输出
        
    
*   中等温度值(0.4-0.7)：
    
    *   平衡了创造性和连贯性
        
    *   适合日常对话、一般性写作
        
    *   推荐用于聊天机器人对话(0.5左右)
        
    
*   高温度值(0.8-1.0)：
    
    *   产生更具创造性和多样性的输出
        
    *   适合创意写作、头脑风暴等场景
        
    *   但可能降低文本的连贯性
        
    

#### 

[hashtag](#topp-he-cai-yang)

`**Top P (核采样)**`：

默认值为 1，值越小，AI 生成的内容越单调，也越容易理解；值越大，AI 回复的词汇范围越大，越多样化。

核采样通过控制词汇选择的概率阈值来影响输出：

*   较小值(0.1-0.3)：
    
    *   仅考虑最高概率的词汇
        
    *   输出更保守、更可控
        
    *   适合代码注释、技术文档等场景
        
    
*   中等值(0.4-0.6)：
    
    *   平衡词汇多样性和准确性
        
    *   适合一般对话和写作任务
        
    
*   较大值(0.7-1.0)：
    
    *   考虑更广泛的词汇选择
        
    *   产生更丰富多样的内容
        
    *   适合创意写作等需要多样化表达的场景
        
    

circle-info

*   这两个参数可以独立使用或组合使用
    
*   根据具体任务类型选择合适的参数值
    
*   建议通过实验找到最适合特定应用场景的参数组合
    
*   以上内容仅供参考和了解概念，所给参数范围不一定适合所有模型，具体可参考模型相关文档给出的参数建议。
    

#### 

[hashtag](#shang-xia-wen-shu-liang-context-window)

`**上下文数量 (Context Window)**`

要保留在上下文中的消息数量，数值越大，上下文越长，消耗的 token 越多：

*   5-10：适合普通对话
    
*   \>10：需要更长记忆的复杂任务（例如：按照写作提纲分步生成长文的任务，需要确保生成的上下文逻辑连贯）
    
*   > 注意：消息数越多，token 消耗越大
    

#### 

[hashtag](#kai-qi-xiao-xi-chang-du-xian-zhi-maxtoken)

`**开启消息长度限制 (MaxToken)**`

单次回答最大 [Tokenarrow-up-right](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) 数，在大语言模型中，max token（最大令牌数）是一个关键参数，它直接影响模型生成回答的质量和长度。

> 如:在CherryStudio当中填写好key后测试模型是否连通时，只需要知道模型是否有正确返回消息而不需特定内容,这种情况下设置MaxToken为1即可。

多数模型的MaxToken上限为32k Tokens，当然也有64k，甚至更多的，具体需要到对应介绍页面查看。

具体设置多少取决于自己的需要，当然也可以参考以下建议。

circle-check

建议：

*   普通聊天：500-800
    
*   短文生成：800-2000
    
*   代码生成：2000-3600
    
*   长文生成：4000及以上 (需要模型本身支持)
    

circle-exclamation

一般情况下模型生成的回答将被限制在 MaxToken 的范围内，当然也有可能会出现被截断（如写长代码时）或表达不完整等情况出现，特殊情况下也需要根据实际情况来灵活调整。

#### 

[hashtag](#liu-shi-shu-chu-stream)

`**流式输出（Stream）**`

流式输出是一种数据处理方式，它允许数据以连续的流形式进行传输和处理，而不是一次性发送所有数据。这种方式使得数据可以在生成后立即被处理和输出，极大地提高了实时性和效率。

在 CherryStudio 客户端等类似环境下简单来说就是打字机效果。

关闭后(非流)：模型生成完信息后整段一次性输出（想象一下微信收到消息的感觉）；

打开时：逐字输出，可以理解为大模型每生成一个字就立马发送给你，直到全部发送完。

circle-info

如果某些特殊模型不支持流式输出需要将该开关关闭，比如**刚开始**只支持非流的o1-mini等。

#### 

[hashtag](#zi-ding-yi-can-shu)

`**自定义参数**`

在请求体（body）中加入额外请求参数，如 `presence_penalty` 等字段，一般人一般情况下用不到。

> 上述top-p、maxtokens、stream等参数就是这些参数之一。

填法：参数名称—参数类型（文本、数字等）—值，参考文档：[点击前往arrow-up-right](https://openai.apifox.cn/doc-3222739)

circle-info

各个模型提供商都或多或少有自己独有的参数，需要到提供商的文档中寻找使用方法

circle-info

*   自定义参数优先级高于内置参数。即自定义参数如果与内置参数重复，则自定义参数会覆盖内置参数。
    

> 如：自定义参数中设置 `model` 为 `gpt-4o` 后，在对话中无论选择哪个模型都使用的是 `gpt-4o` 模型。

*   使用 参数名称:undefined 的设置可排除参数。
    

[上一页功能介绍chevron-left](/cherry-studio/preview)[下一页智能体chevron-right](/cherry-studio/preview/agents)

最后更新于2个月前

*   [助手和话题](#zhu-shou-he-hua-ti)
*   [助手](#zhu-shou)
*   [话题](#hua-ti)
*   [对话框内按钮](#dui-hua-kuang-nei-an-niu)
*   [对话设置](#dui-hua-she-zhi)
*   [模型设置](#mo-xing-she-zhi)
*   [消息设置](#xiao-xi-she-zhi)
*   [输入设置](#shu-ru-she-zhi)
*   [助手设置](#zhu-shou-she-zhi)
*   [编辑助手](#bian-ji-zhu-shou)
