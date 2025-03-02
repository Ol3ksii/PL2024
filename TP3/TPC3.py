import sys
import re

def md_to_html(md):
    lines = md.split('\n')
    in_list = False
    out = []
    for line in lines:
        line = re.sub(r'^(#{3})\s+(.*)', r'<h3>\2</h3>', line)
        line = re.sub(r'^(#{2})\s+(.*)', r'<h2>\2</h2>', line)
        line = re.sub(r'^(#)\s+(.*)', r'<h1>\2</h1>', line)
        m = re.match(r'^(\d+)\.\s+(.*)', line)
        if m:
            if not in_list:
                in_list = True
                out.append('<ol>')
            item = m.group(2)
            item = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', item)
            item = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', item)
            item = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', item)
            item = re.sub(r'\*(.+?)\*', r'<i>\1</i>', item)
            out.append(f'<li>{item}</li>')
        else:
            if in_list:
                in_list = False
                out.append('</ol>')
            line = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', line)
            line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
            line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'\*(.+?)\*', r'<i>\1</i>', line)
            out.append(line)
    if in_list:
        out.append('</ol>')
    return '\n'.join(out)

if __name__ == "__main__":
    text = sys.stdin.read()
    print(md_to_html(text))
