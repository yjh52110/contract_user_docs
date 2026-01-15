import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. First, remove the massive CSS/JS blocks (same as before, just to be safe)
    content = re.sub(r':root\s*\{.*?\}\s*\.dark\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r':root\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.dark\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\(\(a,b,c,d,e,f,g,h\)=>.*?\)\("class","theme".*?\)', '', content, flags=re.DOTALL)
    content = re.sub(r'\$RB=\[\];.*?\$RC\("B:0","S:0"\)', '', content, flags=re.DOTALL)
    content = re.sub(r'\$RC\("B:\d+","S:\d+"\)', '', content)
    content = re.sub(r'\(self\.__next_f=self\.__next_f\|\|\[\]\).*?self\.__next_f\.push\(\[1,".*?"\]\)', '', content, flags=re.DOTALL)
    content = re.sub(r'document\.addEventListener\("DOMContentLoaded".*?requestAnimationFrame\(function\(\)\{\$RT=performance\.now\(\)\}\);', '', content, flags=re.DOTALL)

    lines = content.split('\n')
    cleaned_lines = []
    
    # Strategy: Find valid content start
    # We look for the first H1.
    # H1 can be:
    # 1. Line starting with "# "
    # 2. Line of "=" chars (Setext style), meaning previous line is Title.
    
    content_start_index = 0
    found_h1 = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check for "# Title"
        if stripped.startswith('# '):
            # Make sure it's not some inner comment or weird thing. 
            # But usually top level H1 is good.
            content_start_index = i
            found_h1 = True
            break
            
        # Check for "======="
        # Must be at least 3 equals, and usually the whole line is equals.
        if re.match(r'^={3,}$', stripped):
            # Then the *previous* line was the title.
            # But we need to make sure previous line exists and isn't empty.
            if i > 0 and lines[i-1].strip():
                content_start_index = i - 1
                found_h1 = True
                break
    
    if found_h1:
        # Keep everything from content_start_index
        cleaned_lines = lines[content_start_index:]
        print(f"Found H1 at line {content_start_index+1} in {os.path.basename(filepath)}")
    else:
        # Fallback: Use the cleaner logic from before if no H1 found
        print(f"No H1 found in {os.path.basename(filepath)}, using heuristic cleaning.")
        cleaned_lines = []
        content_started = False
        junk_exact = ["search", "circle-xmark", "Ctrlk", "GitBook Assistant询问", "更多ellipsischevron-down", "globe简体中文chevron-down", "GitBook Assistant", "GitBook 助手", "工作中...思考中...", "close", "##### 晚安", "chevron-upchevron-down", "Ctrli", "AI 基于您的上下文question-circle", "发送", "block-quote在本页chevron-down", "GitBook Assistant询问chevron-down", "这有帮助吗？", "最后更新于", "sun-brightdesktopmoon"]
        
        for line in lines:
            stripped = line.strip()
            is_junk = False
            
            if not stripped and not content_started:
                continue

            if stripped in junk_exact: is_junk = True
            if stripped.startswith("bars[!"): is_junk = True
            if "self.__next_f.push" in stripped: is_junk = True
            # Remove the big list of links at start if we haven't started content
            if not content_started and stripped.startswith("*   ["): is_junk = True
            
            if not is_junk:
                cleaned_lines.append(line)
                content_started = True

    # 4. Remove common footer junk from the END of the cleaned lines
    # Only check the last few lines
    # GitBook often adds "Powered by GitBook" or similar links
    # Also removing the CSS/JS that might have remained if it was at the very end and not caught by top regex (though regex was recursive?)
    # actually the regex was on 'content' string, so it should be gone.
    
    # Just filter specific footer lines
    final_lines = []
    for line in cleaned_lines:
        if "Powered by GitBook" in line or "由 GitBook 提供支持" in line:
            continue
        final_lines.append(line)
        
    cleaned_content = '\n'.join(final_lines)
    
    # Extra cleanup for multiple newlines
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

def main():
    root_dir = "/Users/yjh/Desktop/contract/cherry_gitbook"
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") and not file == "SUMMARY.md":
                clean_file(os.path.join(subdir, file))

if __name__ == "__main__":
    main()
