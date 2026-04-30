from agent import MiMoAgent
from prompts import build_report_prompt


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
    prompt = build_report_prompt(user_text)

    print("\n正在调用 Xiaomi MiMo API，请稍等...\n")
    result = agent.ask(prompt)

    print("========== 生成结果 ==========\n")
    print(result)


if __name__ == "__main__":
    main()
