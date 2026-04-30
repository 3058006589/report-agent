def check_application_text(text: str) -> list[str]:
    checks = {
        "核心痛点": ["痛点", "问题", "成本", "困难", "低效"],
        "Agent/AI作用": ["Agent", "AI", "模型", "MiMo", "智能"],
        "逻辑流": ["流程", "逻辑", "先", "再", "最后", "生成"],
        "具体成果": ["生成", "输出", "报告", "描述", "材料"],
    }

    missing = []
    for name, keywords in checks.items():
        if not any(keyword in text for keyword in keywords):
            missing.append(name)

    return missing
