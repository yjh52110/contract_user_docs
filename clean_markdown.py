import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Regex cleanup (keeping previous patterns)
    content = re.sub(r':root\s*\{.*?\}\s*\.dark\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r':root\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.dark\s*\{.*?\}', '', content, flags=re.DOTALL)
    
    # Improve JS regexes
    content = re.sub(r'\(\(a,b,c,d,e,f,g,h\)=>.*?\)\("class","theme".*?\)', '', content, flags=re.DOTALL)
    content = re.sub(r'\$RB=\[\];.*?\$RC\("B:0","S:0"\)', '', content, flags=re.DOTALL)
    
    lines = content.split('\n')
    
    # 2. H1 Detection Strategy
    content_start_index = 0
    found_h1 = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('# '):
            content_start_index = i
            found_h1 = True
            break
        if re.match(r'^={3,}$', stripped):
            if i > 0 and lines[i-1].strip():
                content_start_index = i - 1
                found_h1 = True
                break
    
    if found_h1:
        cleaned_lines = lines[content_start_index:]
    else:
        # Fallback
        cleaned_lines = []
        content_started = False
        junk_exact = ["search", "circle-xmark", "Ctrlk", "GitBook Assistant询问", "更多ellipsischevron-down", "globe简体中文chevron-down", "GitBook Assistant", "GitBook 助手", "工作中...思考中...", "close", "##### 晚安", "chevron-upchevron-down", "Ctrli", "AI 基于您的上下文question-circle", "发送", "block-quote在本页chevron-down", "GitBook Assistant询问chevron-down", "这有帮助吗？", "最后更新于", "sun-brightdesktopmoon"]
        
        for line in lines:
            stripped = line.strip()
            is_junk = False
            if not stripped and not content_started: continue
            if stripped in junk_exact: is_junk = True
            if stripped.startswith("bars[!"): is_junk = True
            if "self.__next_f.push" in stripped: is_junk = True
            if not content_started and stripped.startswith("*   ["): is_junk = True
            
            if not is_junk:
                cleaned_lines.append(line)
                content_started = True

    # 3. Aggressive Tail Cleanup for JS
    # React hydration scripts often appear at the very bottom.
    # We will iterate backwards and drop lines that look like JS garbage.
    
    final_lines = []
    # First pass: filter out known junk from the body
    for line in cleaned_lines:
        if "Powered by GitBook" in line or "由 GitBook 提供支持" in line:
            continue
        final_lines.append(line)
        
    # Second pass: Trim trailing JS
    # We look from the end. If a line is empty or contains JS patterns, we drop it.
    # Once we hit a "clean" line (normal text), we stop trimming.
    
    trim_index = len(final_lines)
    for i in range(len(final_lines) - 1, -1, -1):
        line = final_lines[i].strip()
        if not line:
            continue
            
        is_js_junk = False
        if line.startswith("(self.__next_f"): is_js_junk = True
        if line.startswith("$RB="): is_js_junk = True
        if line.startswith("self.__next_f.push"): is_js_junk = True
        if "static/chunks/" in line: is_js_junk = True
        if line.startswith("I["): is_js_junk = True # Chunk loading
        
        if is_js_junk:
            trim_index = i
        else:
            # Found a non-junk line (supposedly). 
            # But be careful, sometimes there is a junk line, then an empty line, then more junk.
            # So we only stop if we are SURE it's content.
            # However, looking at the file, the JS blob is a continuous block at the end.
            # But it might be separated by newlines.
            
            # If we encounter a line that is CLEARLY content (e.g. text/header), we stop.
            # If it's ambiguous, we might have an issue.
            # But the JS lines are very specific.
            # formatting: line starting with (self or $RB or I[...
            break
            
    final_lines = final_lines[:trim_index]
    
    cleaned_content = '\n'.join(final_lines)
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    # print(f"Cleaned {filepath}")

def main():
    root_dir = "/Users/yjh/Desktop/contract/cherry_gitbook"
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") and not file == "SUMMARY.md":
                clean_file(os.path.join(subdir, file))

if __name__ == "__main__":
    main()
