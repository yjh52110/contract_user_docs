知识科普
=================

[hashtag](#shen-me-shi-tokens)

什么是 tokens？

-----------------------------------------------

Tokens 是 AI 模型处理文本的基本单位，可以理解为模型"思考"的最小单元。它不完全等同于我们理解的字符或单词，而是模型自己的一种特殊的文本分割方式。

#### 

[hashtag](#id-1.-zhong-wen-fen-ci)

1\. 中文分词

*   一个汉字通常会被编码为 1-2 个 tokens
    
*   例如：`"你好"` ≈ 2-4 tokens
    

#### 

[hashtag](#id-2.-ying-wen-fen-ci)

2\. 英文分词

*   常见单词通常是 1 个 token
    
*   较长或不常见的单词会被分解成多个 tokens
    
*   例如：
    
    *   `"hello"` = 1 token
        
    *   `"indescribable"` = 4 tokens
        
    

#### 

[hashtag](#id-3.-te-shu-zi-fu)

3\. 特殊字符

*   空格、标点符号等也会占用 tokens
    
*   换行符通常是 1 个 token
    

circle-info

不同服务商的 Tokenizer 都不一样，甚至同服务商不同模型的 Tokenizer 也有所差别，该知识仅用于明确 token 的概念。

* * *

[hashtag](#shen-me-shi-tokenizer)

什么是 Tokenizer？

-----------------------------------------------------

Tokenizer（分词器）是 AI 模型将文本转换为 tokens 的工具。它决定了如何把输入文本切分成模型可以理解的最小单位。

### 

[hashtag](#wei-shen-me-bu-tong-mo-xing-de-tokenizer-bu-yi-yang)

为什么不同模型的 Tokenizer 不一样？

#### 

[hashtag](#id-1.-xun-lian-shu-ju-bu-tong)

1\. 训练数据不同

*   不同的语料库导致优化方向不同
    
*   多语言支持程度差异
    
*   特定领域（医疗、法律等）的专门优化
    

#### 

[hashtag](#id-2.-fen-ci-suan-fa-bu-tong)

2\. 分词算法不同

*   BPE (Byte Pair Encoding) - OpenAI GPT 系列
    
*   WordPiece - Google BERT
    
*   SentencePiece - 适合多语言场景
    

#### 

[hashtag](#id-3.-you-hua-mu-biao-bu-tong)

3\. 优化目标不同

*   有的注重压缩效率
    
*   有的注重语义保留
    
*   有的注重处理速度
    

### 

[hashtag](#shi-ji-ying-xiang)

实际影响

同样的文本在不同模型中的 token 数量可能不同：

* * *

[hashtag](#shen-me-shi-qian-ru-mo-xing-embedding-model)

什么是嵌入模型 (Embedding Model)?

---------------------------------------------------------------------------------------

**基本概念：** 嵌入模型是一种将高维离散数据（文本、图像等）转换为低维连续向量的技术，这种转换让机器能更好地理解和处理复杂数据。想象一下，就像把复杂的拼图简化成一个简单的坐标点，但这个点仍然保留了拼图的关键特征。在大模型生态中，它作为"翻译官"，将人类可理解的信息转换为 AI 可计算的数字形式。

**工作原理：** 以自然语言处理为例，嵌入模型可以将词语映射到向量空间中的特定位置。在这个空间里，语义相近的词会自动聚集在一起。比如：

*   "国王"和"王后"的向量会很接近
    
*   "猫"和"狗"这样的宠物词也会距离相近
    
*   而"汽车"和"面包"这样语义无关的词则会距离较远
    

**主要应用场景：**

*   文本分析：文档分类、情感分析
    
*   推荐系统：个性化内容推荐
    
*   图像处理：相似图片检索
    
*   搜索引擎：语义搜索优化
    

**核心优势：**

1.  降维效果：将复杂数据简化为易处理的向量形式
    
2.  语义保持：保留原始数据中的关键语义信息
    
3.  计算效率：显著提升机器学习模型的训练和推理效率
    

**技术价值：** 嵌入模型是现代 AI 系统的基础组件，为机器学习任务提供了高质量的数据表示，是推动自然语言处理、计算机视觉等领域发展的关键技术。

* * *

[hashtag](#embedding-mo-xing-zai-zhi-shi-jian-suo-zhong-de-gong-zuo-yuan-li)

Embedding 模型在知识检索中的工作原理

---------------------------------------------------------------------------------------------------------

**基本工作流程：**

1.  **知识库预处理阶段**
    

*   将文档分割成适当大小的 chunk（文本块）
    
*   使用 embedding 模型将每个 chunk 转换为向量
    
*   将向量和原文存储到向量数据库中
    

1.  **查询处理阶段**
    

*   将用户问题转换为向量
    
*   在向量库中检索相似内容
    
*   将检索到的相关内容作为上下文提供给 LLM
    

* * *

[hashtag](#shen-me-shi-mcpmodel-context-protocol)

**什么是 MCP（Model Context Protocol）？**

-------------------------------------------------------------------------------------------

MCP 是一种开源协议，旨在以标准化的方式向大型语言模型（LLM）提供上下文信息。

*   **类比理解：** 可以把 MCP 想象成 AI 领域的“U盘”。我们知道，U盘可以存储各种文件，插入电脑后就能直接使用。类似地，MCP Server 上可以“插”上各种提供上下文的“插件”，LLM 可以根据需要向 MCP Server 请求这些插件，从而获取更丰富的上下文信息，增强自身能力。
    
*   **与 Function Tool 的对比：** 传统的 Function Tool（函数工具）也可以为 LLM 提供外部功能，但 MCP 更像是一种更高维度的抽象。Function Tool 更多的是针对具体任务的工具，而 MCP 则提供了一种更通用的、模块化的上下文获取机制。
    

### 

[hashtag](#mcp-de-he-xin-you-shi)

**MCP 的核心优势**

1.  **标准化：** MCP 提供了统一的接口和数据格式，使得不同的 LLM 和上下文提供者可以无缝协作。
    
2.  **模块化：** MCP 允许开发者将上下文信息分解为独立的模块（插件），方便管理和复用。
    
3.  **灵活性：** LLM 可以根据自身需求动态选择所需的上下文插件，实现更智能、更个性化的交互。
    
4.  **可扩展性：** MCP 的设计支持未来添加更多类型的上下文插件，为 LLM 的能力拓展提供了无限可能。
    

* * *

[上一页如何高效提问](/question-contact/ask)[下一页反馈 & 建议](/question-contact/suggestions)

最后更新于8个月前

*   [什么是 tokens？](#shen-me-shi-tokens)
*   [什么是 Tokenizer？](#shen-me-shi-tokenizer)
*   [为什么不同模型的 Tokenizer 不一样？](#wei-shen-me-bu-tong-mo-xing-de-tokenizer-bu-yi-yang)
*   [实际影响](#shi-ji-ying-xiang)
*   [什么是嵌入模型 (Embedding Model)?](#shen-me-shi-qian-ru-mo-xing-embedding-model)
*   [Embedding 模型在知识检索中的工作原理](#embedding-mo-xing-zai-zhi-shi-jian-suo-zhong-de-gong-zuo-yuan-li)
*   [什么是 MCP（Model Context Protocol）？](#shen-me-shi-mcpmodel-context-protocol)
*   [MCP 的核心优势](#mcp-de-he-xin-you-shi)

$RB=\[\];$RV=function(b){$RT=performance.now();for(var a=0;a<b.length;a+=2){var c=b\[a\],e=b\[a+1\];null!==e.parentNode&&e.parentNode.removeChild(e);var f=c.parentNode;if(f){var g=c.previousSibling,h=0;do{if(c&&8===c.nodeType){var d=c.data;if("/$"===d||"/&"===d)if(0===h)break;else h--;else"$"!==d&&"$?"!==d&&"$~"!==d&&"$!"!==d&&"&"!==d||h++}d=c.nextSibling;f.removeChild(c);c=d}while(c);for(;e.firstChild;)f.insertBefore(e.firstChild,c);g.data="$";g.\_reactRetry&&g.\_reactRetry()}}b.length=0}; $RC=function(b,a){if(a=document.getElementById(a))(b=document.getElementById(b))?(b.previousSibling.data="$~",$RB.push(b,a),2===$RB.length&&(b="number"!==typeof $RT?0:$RT,a=performance.now(),setTimeout($RV.bind(null,$RB),2300>a&&2E3<a?2300-a:b+300-a))):a.parentNode.removeChild(a)};

复制

    输入："Hello, world!"
    GPT-3: 4 tokens
    BERT: 3 tokens
    Claude: 3 tokens
