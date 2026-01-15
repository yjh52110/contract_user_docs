知识库教程
====================

在 0.9.1 版本中，CherryStudio 带来了期待已久的知识库功能。

下面我们将按步骤呈现 CherryStudio 的详细使用说明。

[hashtag](#tian-jia-qian-ru-mo-xing)

添加嵌入模型

------------------------------------------------

1.  在模型管理服务中查找模型，可以点击“嵌入模型”快速筛选；
    
2.  找到需要的模型，添加到我的模型。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-3566134edc9d0d37b5172c4c4cb4ef84c17da2b9%252Fimage.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=63705d5c&sv=2)

[hashtag](#chuang-jian-zhi-shi-ku)

创建知识库

---------------------------------------------

1.  知识库入口：在 CherryStudio 左侧工具栏，点击知识库图标，即可进入管理页面；
    
2.  添加知识库：点击添加，开始创建知识库；
    
3.  命名：输入知识库的名称并添加嵌入模型，以 bge-m3 为例，即可完成创建。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-8d577f77483c59e2a35fa9a79823c88852b16845%252Fimage-1.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=5d4bbafe&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-26bde7cb42570d0192ad0d55990304bd3a10c485%252Fimage-2.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=85d0a2b6&sv=2)

[hashtag](#tian-jia-wen-jian-bing-xiang-liang-hua)

添加文件并向量化

----------------------------------------------------------------

1.  添加文件：点击添加文件的按钮，打开文件选择；
    
2.  选择文件：选择支持的文件格式，如 pdf，docx，pptx，xlsx，txt，md，mdx 等，并打开；
    
3.  向量化：系统会自动进行向量化处理，当显示完成时（绿色 ✓），代表向量化已完成。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-5673213f6cd35c9d3ca6972e390b3f04c3d53492%252Fimage-3.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=c198e01d&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-56f66212a7c8695f3daaa8c968dc13c7ea6141a8%252Fimage-4.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=c47f3e9d&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2908c341f28d0bd07d65e42fc1eedb435f7e53a2%252Fimage-5.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=25dfcf17&sv=2)

[hashtag](#tian-jia-duo-zhong-lai-yuan-de-shu-ju)

添加多种来源的数据

----------------------------------------------------------------

CherryStudio 支持多种添加数据的方式：

1.  文件夹目录：可以添加整个文件夹目录，该目录下支持格式的文件会被自动向量化；
    
2.  网址链接：支持网址 url，如[https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction)；
    
3.  站点地图：支持 xml 格式的站点地图，如[https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml)；
    
4.  纯文本笔记：支持输入纯文本的自定义内容。
    

circle-info

提示：

1.  导入知识库的文档中的插图暂不支持转换为向量，需要手动转换为文本；
    
2.  使用网址作为知识库来源时不一定会成功，有些网站有比较严格的反扒机制（或需要登录、授权等），因此该方式不一定能获取到准确内容。创建完成后建议先搜索测试一下。
    
3.  一般网站都会提供sitemap，如CherryStudio的[sitemap](https://docs.cherry-ai.com/sitemap-pages.xml)，一般情况下在网站的根地址（即网址）后加/sitemap.xml可以获取到相关信息。如`aaa.com/sitemap.xml` 。
    
4.  如果网站没提供sitemap或者网址比较杂可自行组合一个sitemap的xml文件使用，文件暂时需要使用公网可直接访问的直链的方式填入，本地文件链接不会被识别。
    

> 1.  可以让AI生成sitemap文件或让AI写一个sitemap的HTML生成器工具；
>     
> 2.  直链可以使用oss直链或者网盘直链等方式来生成。如果没有现成工具也可到[ocoolAI](https://one.ocoolai.com/login)官网，登录后使用网站顶栏的免费文件上传工具来生成直链。
>     

[hashtag](#sou-suo-zhi-shi-ku)

搜索知识库

-----------------------------------------

当文件等资料向量化完成后，即可进行查询：

1.  点击页面下方的搜索知识库按钮；
    
2.  输入查询的内容；
    
3.  呈现搜索的结果；
    
4.  并显示该条结果的匹配分数。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-cf2b0591ac60272a645284f1cdc41c82e66df320%252Fimage-7.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=84eef69f&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-86458b980ce132df81d52cdee3040030e8b4ea54%252Fimage-8.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=dfef4f15&sv=2)

[hashtag](#dui-hua-zhong-yin-yong-zhi-shi-ku-sheng-cheng-hui-fu)

对话中引用知识库生成回复

----------------------------------------------------------------------------------

1.  创建一个新的话题，在对话工具栏中，点击知识库，会展开已经创建的知识库列表，选择需要引用的知识库；
    
2.  输入并发送问题，模型即返回通过检索结果生成的答案 ；
    
3.  同时，引用的数据来源会附在答案下方，可快捷查看源文件。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-8097c7c77d5a37ac1a9d7279b2cfa6c200c4bca2%252Fimage-9.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=4ddbb6e0&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-d74289fd35eecc143d2938b75a34defbdbe108bf%252Fimage-10.webp%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=72885278&sv=2)

[上一页清除 CSS 设置](/pre-basic/personalization-settings/clear-css)[下一页知识库数据](/knowledge-base/data)

最后更新于2个月前

*   [添加嵌入模型](#tian-jia-qian-ru-mo-xing)
*   [创建知识库](#chuang-jian-zhi-shi-ku)
*   [添加文件并向量化](#tian-jia-wen-jian-bing-xiang-liang-hua)
*   [添加多种来源的数据](#tian-jia-duo-zhong-lai-yuan-de-shu-ju)
*   [搜索知识库](#sou-suo-zhi-shi-ku)
*   [对话中引用知识库生成回复](#dui-hua-zhong-yin-yong-zhi-shi-ku-sheng-cheng-hui-fu)
