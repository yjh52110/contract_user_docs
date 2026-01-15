GitHub Copilot
==============

使用 GitHub Copilot 需要先拥有一个 GitHub 账号，并订阅 GitHub Copilot 服务，free 版本的订阅也可以，但 free 版本不支持最新的 Claude 3.7 模型，具体请参考 [GitHub Copilot 官网](https://github.com/features/copilot)。

[hashtag](#huo-qu-device-code)

获取 Device Code

--------------------------------------------------

点击「登录 GitHub」，获取 Device Code 并复制。

![获取 Device Code 示例图片](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-3202ba64930247e41213bc08cdcd88f11b980b14%252F%25E8%258E%25B7%25E5%258F%2596DeviceCode.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=47e065a&sv=2)

获取 Device Code

[hashtag](#zai-liu-lan-qi-zhong-tian-xie-device-code-bing-shou-quan)

在浏览器中填写 Device Code 并授权

-------------------------------------------------------------------------------------------------

成功获取 Device Code 后，点击链接打开浏览器，在浏览器中登录 GitHub 账号，输入 Device Code 并授权。

![GitHub授权.png 示例图片](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-6915465c0a9938a7b7009a82ada2e1b720880f0f%252FGitHub%25E6%258E%2588%25E6%259D%2583.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=dd0ed626&sv=2)

GitHub 授权

授权成功后，返回 Cherry Studio，点击「连接 GitHub」，成功后会显示 GitHub 用户名和头像。

![GitHub连接成功示例图片](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e98cce5accc9f97d46b759a1b0ad3f554918d057%252FGitHub%25E8%25BF%259E%25E6%258E%25A5%25E6%2588%2590%25E5%258A%259F.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=f2154199&sv=2)

GitHub 连接成功

[hashtag](#dian-ji-guan-li-huo-qu-mo-xing-lie-biao)

点击「管理」获取模型列表

---------------------------------------------------------------------

点击下方的「管理」按钮，会自动联网获取当前支持的模型列表。

![管理按钮获取模型列表示例图片](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e20eaf3f12878378cba6d40bd790d51aed40ee77%252F%25E7%25AE%25A1%25E7%2590%2586%25E6%258C%2589%25E9%2592%25AE%25E8%258E%25B7%25E5%258F%2596%25E6%25A8%25A1%25E5%259E%258B%25E5%2588%2597%25E8%25A1%25A8.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=73f0ae48&sv=2)

获取模型列表

[hashtag](#chang-jian-wen-ti)

常见问题

---------------------------------------

### 

[hashtag](#huo-qu-device-code-shi-bai-qing-chong-shi)

获取 Device Code 失败，请重试

![获取 Device Code 失败示例图片](https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-e826ac02f651176d07d95e7f0e603ff89d1eccdb%252F%25E8%258E%25B7%25E5%258F%2596DeviceCode%25E5%25A4%25B1%25E8%25B4%25A5.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=f8e6016a&sv=2)

获取 Device Code 失败

目前使用 Axios 构建请求，Axios 不支持 socks 代理，请使用系统代理或 HTTP 代理，或者直接不在 CherryStudio 中设置代理，使用全局代理。首先请确保您的网络连接正常，以避免获取 Device Code 失败的情况。

[上一页Ollama](/pre-basic/providers/ollama)[下一页ModelScope（魔搭）](/pre-basic/providers/modelscope)

最后更新于9个月前

*   [获取 Device Code](#huo-qu-device-code)
*   [在浏览器中填写 Device Code 并授权](#zai-liu-lan-qi-zhong-tian-xie-device-code-bing-shou-quan)
*   [点击「管理」获取模型列表](#dian-ji-guan-li-huo-qu-mo-xing-lie-biao)
*   [常见问题](#chang-jian-wen-ti)
*   [获取 Device Code 失败，请重试](#huo-qu-device-code-shi-bai-qing-chong-shi)
