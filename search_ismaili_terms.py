import re
import os

def search_ismaili_terms(directory='.'):
    pattern = r'ملاحدة|باطنية|اسماعيلية|فداوي|فدا[.][يو]|فدا[وي][يو]ن'
    page_milestone_pattern = re.compile(r'Page (\d+), Milestone (\d+)')
    matches = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Find all matches with regex
                        for match in re.finditer(pattern, content):
                            start = max(0, match.start() - 10)
                            end = min(len(content), match.end() + 10)
                            context = content[start:end]
                            
                            # Get the nearest page and milestone before this match
                            content_before = content[:match.start()]
                            last_page_milestone = list(page_milestone_pattern.finditer(content_before))
                            page_number = last_page_milestone[-1].group(1) if last_page_milestone else 'N/A'
                            milestone_number = last_page_milestone[-1].group(2) if last_page_milestone else 'N/A'
                            
                            matches.append((os.path.basename(file_path), match.group(), context, page_number, milestone_number))
                
                except (UnicodeDecodeError, PermissionError):
                    continue
    
    return matches

# Execute the search and save results
if __name__ == '__main__':
    results = search_ismaili_terms()
    
    with open('ismaili_terms_results.txt', 'w', encoding='utf-8') as output_file:
        for filename, matched_term, context, page_number, milestone_number in results:
            output_file.write(f"{filename} | Term: {matched_term} | Page: {page_number} | MS: {milestone_number} | Context: {context}\n")
    
    print(f"Results have been saved to 'ismaili_terms_results.txt'")