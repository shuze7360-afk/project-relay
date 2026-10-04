# -*- coding: utf-8 -*-
"""project-relay 结构检查：frontmatter、触发词、链接、占位符、行数。

用法：python evidence/check-format.py <仓库根目录>
"""
import re
import sys
from pathlib import Path

SKILL_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
SKILL = SKILL_DIR / "SKILL.md"
issues, passed = [], []

raw = SKILL.read_text(encoding="utf-8")

m = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, re.S)
if not m:
    issues.append("SKILL.md 缺少 YAML frontmatter")
else:
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M | re.S)
    if not name:
        issues.append("frontmatter 缺少 name")
    elif name.group(1).strip() != SKILL_DIR.name:
        issues.append(f"name ({name.group(1).strip()}) 与目录名 ({SKILL_DIR.name}) 不一致")
    else:
        passed.append("frontmatter name 与目录名一致")
    if not desc:
        issues.append("frontmatter 缺少 description")
    else:
        d = desc.group(1).strip()
        if not (50 <= len(d) <= 1024):
            issues.append(f"description 长度 {len(d)} 超出 50-1024")
        else:
            passed.append(f"description 长度 {len(d)} 合规")
        missing = [t for t in ["启动项目", "继续项目", "接力", "交接", "project-relay"] if t not in d]
        if missing:
            issues.append(f"description 缺少触发词: {missing}")
        else:
            passed.append("description 含全部约定触发词")

body = raw[m.end():] if m else raw
for link in re.findall(r"\]\(([^)#\s]+)\)", body):
    if link.startswith(("http://", "https://")):
        continue
    target = (SKILL.parent / link).resolve()
    if not target.exists():
        issues.append(f"SKILL.md 链接目标不存在: {link}")
    else:
        passed.append(f"链接可解析: {link}")

placeholders = ["FIXME", "{{", "}}", "待填", "<placeholder>"]
placeholder_res = [re.compile(r"\bTODO\b(?!\.md)"), re.compile(r"\bTBD\b"), re.compile(r"\bXXX\b")]
scan = [SKILL] + list((SKILL_DIR / "references").glob("*.md"))
for f in scan:
    text = f.read_text(encoding="utf-8")
    hits = [p for p in placeholders if p in text] + [r.pattern for r in placeholder_res if r.search(text)]
    if hits:
        issues.append(f"{f.name} 发现占位符: {hits}")
    n = len(text.splitlines())
    limit = 500 if f.name == "SKILL.md" else 300
    if n > limit:
        issues.append(f"{f.name} 行数 {n} 超过 {limit}")
    else:
        passed.append(f"{f.name} {n} 行（不超过 {limit}）")

extra = [p.name for p in (SKILL_DIR / "references").iterdir() if p.suffix != ".md"]
if extra:
    issues.append(f"references 存在非 md 文件: {extra}")
else:
    passed.append("references 仅含 md 文档")

# 规范一致性（回归检查）：废弃措辞不得再出现在规范文档中
obsolete = ["以实际为准", "产物路径 + 验证命令或输出", "验证命令或输出，或用户确认"]
normative = [SKILL, SKILL_DIR / "README.md"] + sorted((SKILL_DIR / "references").glob("*.md"))
for f in normative:
    text = f.read_text(encoding="utf-8")
    hits = [o for o in obsolete if o in text]
    if hits:
        issues.append(f"{f.name} 仍含废弃规则措辞: {hits}")
    else:
        passed.append(f"{f.name} 无废弃规则措辞")

print("== PASS ==")
for p in passed:
    print(" +", p)
if issues:
    print("== FAIL ==")
    for i in issues:
        print(" !", i)
    sys.exit(1)
print("全部通过")
