PPIO 派欧云
========

[hashtag](#cherry-studio-jie-ru-ppio-llm-api)

Cherry Studio 接入 PPIO LLM API

--------------------------------------------------------------------------------

### 

[hashtag](#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0)

[​arrow-up-right](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)教程概述

Cherry Studio 是一款多模型桌面客户端，目前支持：Windows 、Linux 、MacOS 系电脑安装包。它聚合主流 LLM 模型，提供多场景辅助。用户可通过智能会话管理、开源定制、多主题界面来提升工作效率。

Cherry Studio 现已与 **PPIO 高性能 API 通道** 深度适配——通过企业级算力保障，实现 **DeepSeek-R1/V3 高速响应** 与 **99.9% 服务可用性**，带给您快速流畅的体验。

下方教程包含完整接入方案（含密钥配置），3 分钟开启「Cherry Studio 智能调度 + PPIO 高性能 API」的进阶模式。

### 

[hashtag](#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8)

[​arrow-up-right](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1\. 进入 CherryStudio，添加 “PPIO” 作为模型提供商

首先前往官网下载 Cherry Studio： [arrow-up-right](https://cherry-ai.com/download)[https://cherry-ai.com/downloadarrow-up-right](https://cherry-ai.com/download) （如果进不去可以打开下面的夸克网盘链接下载自己需要的版本：[https://pan.quark.cn/s/c8533a1ec63e#/list/sharearrow-up-right](https://pan.quark.cn/s/c8533a1ec63e#/list/share)

（1）先点击左下角设置，自定义提供商名称为：`PPIO`，点击“确定”

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fcherry-studio-setting.png&width=768&dpr=4&quality=100&sign=7214a2a8&sv=2)

（2）前往 [派欧算力云 API 密钥管理 arrow-up-right](https://ppinfra.com/user/register?invited_by=JYT9GD&utm_source=github_cherry-studio)，点击【用户头像】—【API 密钥管理】进入控制台

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fppinfra-create-api-key-01.png&width=768&dpr=4&quality=100&sign=8ac46f31&sv=2)

点击 【+ 创建】按钮来创建新的 API 密钥。自定义一个密钥名称，**生成的密钥仅在生成时呈现，务必复制并保存到文档中，以免影响后续使用**

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fppinfra-create-api-key-02.png&width=768&dpr=4&quality=100&sign=7056f66c&sv=2)

（3）在 CherryStudio 填入密钥 点击设置，选择【PPIO 派欧云】，输入官网生成的 API 密钥，最后点击【检查】

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fcherry-studio-3601.PNG&width=768&dpr=4&quality=100&sign=4b6c7914&sv=2)

（4）选择模型：deepseek/deepseek-r1/community 为例，如需更换其他模型，可直接更换。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fcherry-studio-3602.PNG&width=768&dpr=4&quality=100&sign=4cd40799&sv=2)

DeepSeek R1 和 V3 community 版本仅供大家尝鲜，也是全参数满血版模型，稳定性和效果无差异，如需大量调用则须 **充值并切换到非 community 版本**。

### 

[hashtag](#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae)

[​arrow-up-right](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2\. 模型使用配置

（1）点击【检查】显示连接成功后即可正常使用

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fcherry-studio-3603.png&width=768&dpr=4&quality=100&sign=edcaa0fe&sv=2)

（2）最后点击【@】选择 PPIO 供应商下刚刚添加的 DeepSeek R1 模型，即可成功开始聊天~

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2Fstatic.ppinfra.com%2Fdocs%2Fimage%2Fllm%2Fcherry-studio-ppio-config-02.png&width=768&dpr=4&quality=100&sign=cdc1b748&sv=2)

【部分素材来源： [陈恩 arrow-up-right](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### 

[hashtag](#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b)

[​arrow-up-right](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3\. PPIO×Cherry Studio 视频使用教程

若您更倾向直观学习，我们在 B 站准备了视频教程。通过手把手教学，助您快速掌握「PPIO API+Cherry Studio」的配置方法，点击下方链接直达视频，开启流畅开发体验 → [《 【还在为 DeepSeek 疯狂转圈抓狂？】派欧云+DeepSeek 满血版 =？不再拥堵，即刻起飞》arrow-up-right](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C&from_spmid=search.search-result.0.0&is_story_h5=false&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=b892268f-5751-4f6e-9690-50b37855d346&share_source=WEIXIN&share_source=weixin&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1739160448&unique_k=eKDZuRP&up_id=3546757841554023&vd_source=50fea165795ccc47455a165f5bcaeed2)

【视频素材来源：sola】

[上一页ModelScope（魔搭）chevron-left](/pre-basic/providers/modelscope)[下一页阿里云百炼chevron-right](/pre-basic/providers/a-li-yun-bai-lian)

最后更新于9个月前

*   [Cherry Studio 接入 PPIO LLM API](#cherry-studio-jie-ru-ppio-llm-api)
*   [​教程概述](#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0)
*   [​1\. 进入 CherryStudio，添加 “PPIO” 作为模型提供商](#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8)
*   [​2\. 模型使用配置](#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae)
*   [​3\. PPIO×Cherry Studio 视频使用教程](#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b)
