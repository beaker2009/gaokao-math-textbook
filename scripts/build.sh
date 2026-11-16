#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p build dist
python3 scripts/lint_markdown.py
{
  cat metadata.yaml
  printf '\n# 前言\n\n'
  cat FRONT_MATTER.md
  for part in parts/part{1,2,3,4,5}; do
    for chapter in "$part"/*.md; do
      [ -e "$chapter" ] || continue
      case "$chapter" in
        parts/part2/ch10-trigonometric-functions-identities.md|\
        parts/part2/ch11-solving-triangles-sine-cosine-laws.md|\
        parts/part4/ch17-derivatives-function-analysis.md) continue ;;
      esac
      printf '\n\\newpage\n\n'
      cat "$chapter"
    done
  done
} > build/book.md

if ! command -v pandoc >/dev/null 2>&1; then
  echo "错误：未安装 pandoc，已生成 build/book.md，但无法生成 PDF。" >&2
  exit 127
fi
if ! command -v xelatex >/dev/null 2>&1; then
  echo "错误：未安装 xelatex，已生成 build/book.md，但无法生成 PDF。" >&2
  exit 127
fi
pandoc build/book.md \
  --from markdown+tex_math_dollars+raw_tex \
  --pdf-engine=xelatex \
  --output "dist/猴子也能看懂的高考数学到强基高联.pdf"
