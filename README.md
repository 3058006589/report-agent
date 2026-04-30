# report-agent

基于 Xiaomi MiMo API 的项目申请材料生成 Agent。

## 项目简介

很多人有项目想法，但很难把核心痛点、技术逻辑和 AI 成果写成清晰可信的申请材料。这个项目用 MiMo API 构建一个命令行 Agent，把零散项目资料整理成可直接提交的申请表描述和完整项目报告。

## 核心流程

```text
用户输入项目资料
→ 分析核心痛点和使用场景
→ 生成申请表描述和完整项目报告
→ 自检是否包含痛点、逻辑流、AI 作用和具体成果
→ 输出最终版本
```

## 功能

- 生成 100 到 300 字申请表描述
- 生成完整项目报告
- 自动检查描述是否包含关键要素
- 使用 OpenAI 兼容格式调用 Xiaomi MiMo API

## 运行方式

安装依赖：

```powershell
pip install -r requirements.txt
```

设置 API Key：

```powershell
$env:MIMO_API_KEY="你的API Key"
```

运行：

```powershell
python main.py
```

输入项目资料后，单独输入 `END` 结束。

## 示例输入

```text
我做了一个基于 MiMo API 的项目材料生成工具，可以帮助用户把零散想法整理成申请表描述。
END
```

## 技术栈

- Python
- Xiaomi MiMo API
- OpenAI Python SDK
