#!/usr/bin/env python3
"""对教材 Markdown 做不依赖 Pandoc 的快速语法体检。"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.rglob("*.md"))
errors: list[str] = []
for path in files:
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), 1):
        bad = [c for c in line if (ord(c) < 32 and c != "\t") or ord(c) == 127]
        if bad:
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: 非法控制字符")
        inline_dollars = len(re.findall(r"(?<!\\)\$", line))
        if inline_dollars % 2 and not (line.strip().startswith("$$") or line.strip().endswith("$$")):
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: 行内数学分隔符未配对")
        if re.search(r"\\\\(?:left|right|sqrt|frac|dfrac|ge|le|ne|pm|mathbb)", line):
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: 疑似重复反斜杠")
    if text.count("$$") % 2:
        errors.append(f"{path.relative_to(ROOT)}: 展示数学分隔符未配对")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"检查通过：{len(files)} 个 Markdown 文件。")
