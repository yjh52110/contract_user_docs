database知识库数据
=============

在 Cherry Studio 知识库中添加的数据全部存储在本地，在添加过程中会复制一份文档放在 Cherry Studio 数据存储目录

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-22b5b3cc68480ca857ca90e190edcdd9c7721a91%252Fmermaid-diagram-1739241680067.png%3Falt%3Dmedia%26token%3Dbe67d8c4-f755-4715-b877-a333b4ca1d4e&width=768&dpr=4&quality=100&sign=8670fcbe&sv=2)

知识库处理流程图

向量数据库：[https://turso.tech/libsqlarrow-up-right](https://turso.tech/libsql)

当文档被添加到 Cherry Studio 知识库之后，文件会被切分为若干个片段，然后这些片段会交给嵌入模型进行处理

当使用大模型进行问答的时候，会查询和问题相关的文本片段一并交个大语言模型处理

如果对数据隐私有要求，建议使用本地嵌入数据库和本地大语言模型

[上一页知识库教程chevron-left](/knowledge-base/knowledge-base)[下一页嵌入模型chevron-right](/knowledge-base/emb-models-info)

最后更新于28天前
