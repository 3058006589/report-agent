import os
from datetime import datetime

from openai import OpenAI


class MiMoAgent:
    def __init__(self) -> None:
        api_key = os.environ.get("MIMO_API_KEY")
        if not api_key:
            raise RuntimeError(
                "未找到环境变量 MIMO_API_KEY。请先运行：$env:MIMO_API_KEY=\"你的API Key\""
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.xiaomimimo.com/v1",
        )

    def ask(self, user_prompt: str, max_tokens: int = 1200) -> str:
        completion = self.client.chat.completions.create(
            model="mimo-v2.5-pro",
            messages=[
                {
                    "role": "system",
                    "content": self._system_prompt(),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            max_completion_tokens=max_tokens,
            temperature=0.7,
            top_p=0.95,
            stream=False,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return completion.choices[0].message.content or ""

    def _system_prompt(self) -> str:
        today = datetime.now()
        week_map = {
            0: "星期一",
            1: "星期二",
            2: "星期三",
            3: "星期四",
            4: "星期五",
            5: "星期六",
            6: "星期日",
        }
        date_text = today.strftime("%Y年%m月%d日")
        week_text = week_map[today.weekday()]

        return (
            "你是MiMo（中文名称也是MiMo），是小米公司研发的AI智能助手。\n"
            f"今天的日期：{date_text} {week_text}，你的知识截止日期是2024年12月。\n\n"
            "你擅长把用户的项目想法整理成清晰、真实、可提交的成果描述。"
        )
