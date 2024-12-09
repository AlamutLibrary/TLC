import os
import re
from datetime import datetime

def search_and_save_context(pattern, context_size=100):
    results = []
    
    for file in os.listdir('.'):
        if file.endswith('.txt'):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    # Using re.finditer to find all matches of the regex pattern
                    matches = re.finditer(pattern, text)
                    for match in matches:
                        index = match.start()
                        # Get context ensuring the matched term is in the middle
                        start = max(0, index - context_size)
                        end = min(len(text), index + len(match.group()) + context_size)
                        context = text[start:end]
                        line_number = text[:index].count('\n') + 1
                        results.append({
                            'file': file,
                            'line': line_number,
                            'context': context
                        })
            except UnicodeDecodeError:
                continue

    # Save results
    output_file = f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Search Results for pattern '{pattern}'\n{'='*50}\n\n")
        for result in results:
            f.write(f"File: {result['file']}\nLine: {result['line']}\nContext:\n{result['context']}\n\n")
    
    return output_file

output = search_and_save_context('.l.طرية')
print(f"Results saved to: {output}")
