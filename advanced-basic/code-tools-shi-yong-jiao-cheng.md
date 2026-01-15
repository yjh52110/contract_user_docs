codeCode Tools 使用教程
===================

Tools

Cherry Studio v1.5.7 版本引入了操作简单，强大的 Code Agent 功能，可以直接启动和管理多种 AI 编程agent 。本教程将引导您完成设置和启动的完整流程。

* * *

### 

[hashtag](#cao-zuo-bu-zhou)

操作步骤

#### 

[hashtag](#id-1.-sheng-ji-cherry-studio)

1\. 升级 Cherry Studio

首先，请确保您的 Cherry Studio 已升级到 **v1.5.7** 或更高版本。您可以前往 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 或官方网站下载最新版本。

#### 

[hashtag](#id-2.-jin-ru-code-tool-gong-ju-jie-mian)

2\. 进入 Code Tool 工具界面

顶部导航模式：点击界面顶部的“+”号图标，新建一个空白标签页

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-418f066aef26e03d31b30206c9cdfc3ecaa5d2c4%252Fimage%2520%282%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8fc944e1&sv=2)

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-b42e875e93506534a3c5cebc72b95502a0595ad1%252Fimage%2520%283%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=8ed0ca75&sv=2)

circle-info

左侧导航模式的情况下点击左侧导航里面的 Code Tool 按钮进入该页面

#### 

[hashtag](#id-3.-xuan-ze-cli-gong-ju)

3\. 选择 CLI 工具

根据您的需求和所持有的 API Key，选择一个要使用的 Code Agent 工具。 目前支持以下几种：

*   **Claude Code**
    
*   **Gemini CLI**
    
*   **Qwen Code**
    
*   **OpenAI Codex**
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-ab7bc9ff839720c2777568a48d1ff71a2177741a%252Fimage%2520%284%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=2d3f471&sv=2)

#### 

[hashtag](#id-4.-xuan-ze-agent-diao-yong-de-mo-xing)

4\. 选择 Agent 调用的模型

在模型下拉列表中，选择与您所选 CLI 工具兼容的模型。 _（详细的模型兼容性说明，请参考下方的“重要注意事项”）_

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-b8148d693337e9c06b403b3c46e7e15e0a03e72e%252Fimage%2520%285%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=a359828c&sv=2)

#### 

[hashtag](#id-5.-zhi-ding-gong-zuo-mu-lu)

5\. 指定工作目录

点击“选择目录”按钮，为 Agent 指定一个工作目录。Agent 将拥有访问此目录下所有文件和子目录的权限，以便于它理解项目上下文、读取文件和执行代码。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-26d4e51e4689e71727cbe6d938f9e74bb4c88f1a%252Fimage%2520%286%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=da8e650&sv=2)

#### 

[hashtag](#id-6-she-zhi-huan-jing-bian-liang)

6 设置环境变量

*   **自动配置**：您在第 6 步（模型）和第 7 步（工作目录）中的选择，会自动生成相应的环境变量。
    
*   **自定义添加**：如果您的 Agent 或项目需要其他特定的环境变量（例如 `PROXY_URL` 等），可以在此区域自定义添加。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-7f0ac5497f2acfd266c4212c67f065bb12d19427%252Fimage%2520%287%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=706c6b0e&sv=2)

#### 

[hashtag](#id-7.-geng-xin-xuan-xiang)

7\. 更新选项

*   **内置可执行文件**：Cherry Studio 已为您集成了上述所有 Code Agent 的可执行文件，在大多数情况下，您无需联网即可直接使用。
    
*   **自动更新**：如果您希望 Agent 始终保持最新版本，可以勾选 `**检查更新并安装最新版本**` 的选项。勾选后，每次启动时程序都会联网检查并更新 Agent 工具。
    

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-8d32add7b26fbce23a777eb82d2614061fb339fb%252Fimage%2520%288%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=e87242c8&sv=2)

#### 

[hashtag](#id-8.-qi-dong-agent)

8\. 启动 Agent

所有配置完成后，点击 `**启动**` 按钮。 Cherry Studio 会自动调用您系统自带的 Terminal（终端）工具，并在其中加载好所有环境变量，然后运行您选择的 Code Agent。现在您可以在弹出的终端窗口中与 AI Agent 进行交互了。

![](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-2a54f0893723d0dfca5a67c4c28c374d5d34a8a5%252Fimage%2520%289%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=1ff23ac6&sv=2)

* * *

### 

[hashtag](#zhong-yao-zhu-yi-shi-xiang)

重要注意事项

1.  **模型兼容性说明**：
    
    *   **Claude Code**: 需要选择支持 Anthropic API Endpoint 格式的模型。目前官方支持的模型包括：
        
        *   Claude 系列模型
            
        *   DeepSeek V3.1 (官方 API 平台)
            
        *   Kimi K2 (官方 API 平台)
            
        *   智谱 GLM 4.5 (官方 API 平台)
            
        *   **注意**：当前许多第三方服务商（如 One API, New API 等）针对 DeepSeek, Kimi, GLM 的 API 接口大多只支持 OpenAI Chat Completions 格式，可能无法与 Claude Code 直接兼容，需要等待服务商逐步适配。
            
        
    *   **Gemini CLI**: 需要选择 Google 的 Gemini 系列模型。
        
    *   **Qwen Code**: 支持 OpenAI Chat Completions API 格式的模型，强烈推荐使用 `**Qwen3 Coder**` 系列模型以获得最佳代码生成效果。
        
    *   **OpenAI Codex**: 支持 GPT 系列模型（如 `gpt-4o`, `gpt-5` 等）。
        
    
2.  **依赖与环境冲突**：
    
    *   Cherry Studio 内部集成了独立的 Node.js 运行环境、Code Agent 可执行文件及环境变量配置，旨在提供一个开箱即用的纯净环境。
        
    *   如果您在启动 Agent 时遇到依赖冲突或奇怪的错误，可以考虑暂时**卸载或禁用系统内已安装的相关依赖**（如全局安装的 Node.js 或特定工具链），以排除冲突。
        
    
3.  **API Token 消耗警告**：
    
    *   **Code Agent 对 API Token 的消耗量非常大**。在处理复杂任务时，Agent 为了思考、规划和生成代码，可能会产生大量请求，导致 Token 快速消耗。
        
    *   请务必根据自己的 API 额度和预算，**量力而为**，密切关注 Token 使用情况，以防止预算超支。
        
    

希望本教程能帮助您快速上手 Cherry Studio 强大的 Code Agent 功能！

[上一页调用链使用教程](/advanced-basic/trace)[下一页Agent 使用教程](/advanced-basic/agent)

最后更新于17天前

*   [操作步骤](#cao-zuo-bu-zhou)
*   [重要注意事项](#zhong-yao-zhu-yi-shi-xiang)
