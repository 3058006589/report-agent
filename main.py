from agent import MiMoAgent
from prompts import build_analysis_prompt, build_draft_prompt, build_revision_prompt
from reviewer import check_application_text


def read_multiline_input() -> str:
    print("请输入你的项目资料/想法。输入完成后，单独输入 END 结束：")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines).strip()


def main() -> None:
    user_text = read_multiline_input()
    if not user_text:
        print("没有输入内容，程序结束。")
        return

    agent = MiMoAgent()

    print("\n第 1 步：分析项目痛点和逻辑流...\n")
    analysis = agent.ask(build_analysis_prompt(user_text), max_tokens=1200)

    print("第 2 步：生成申请表描述和完整报告...\n")
    draft = agent.ask(build_draft_prompt(user_text, analysis), max_tokens=1800)

    print("第 3 步：自检并修订最终版本...\n")
    result = agent.ask(build_revision_prompt(draft), max_tokens=1800)

    print("========== 生成结果 ==========\n")
    print(result)

    missing = check_application_text(result)
    if missing:
        print("\n========== 本地自检提醒 ==========\n")
        print("结果可能缺少：" + "、".join(missing))


if __name__ == "__main__":
    main()
