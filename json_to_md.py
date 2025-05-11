import json

# 从 JSON 文件读取数据
with open("log.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 提取表头
headers = list(data[0].keys())
header_line = "| " + " | ".join(headers) + " |"
separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"

# 构建表格内容
rows = [header_line, separator_line]
for item in data:
    row = "| " + " | ".join(item.get(h, "") for h in headers) + " |"
    rows.append(row)

# 合并为 Markdown 字符串
markdown_content = "# 任务记录表\n\n" + "\n".join(rows)

# 写入 Markdown 文件
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("README.md 已更新")