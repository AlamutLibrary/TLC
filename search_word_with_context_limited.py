import os
import re

def search_word_in_files(word, directory='.'):
    """
    Search for a specific word in all files within a directory and its subdirectories,
    and return a limited context (100 tokens before and after) along with page and milestone numbers.
    
    Args:
    word (str): The word to search for
    directory (str): The directory to start searching from (default is current directory)
    
    Returns:
    list: A list of tuples containing (file_path, context, page_number, milestone_number)
    """
    matches = []
    
    # Regular expression to find page and milestone numbers
    page_milestone_pattern = re.compile(r'Page (\d+), Milestone (\d+)')
    
    # Walk through all files and directories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                # Try to open and read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Split content into paragraphs
                    paragraphs = content.split('\n\n')  # Assuming paragraphs are separated by two newlines
                    
                    for paragraph in paragraphs:
                        if word in paragraph:
                            # Search for page and milestone numbers in the paragraph
                            page_milestone_match = page_milestone_pattern.search(paragraph)
                            page_number = page_milestone_match.group(1) if page_milestone_match else 'N/A'
                            milestone_number = page_milestone_match.group(2) if page_milestone_match else 'N/A'
                            
                            # Tokenize the paragraph
                            tokens = paragraph.split()
                            word_indices = [i for i, token in enumerate(tokens) if token == word]
                            
                            for index in word_indices:
                                # Get context: 100 tokens before and after the word
                                start_index = max(0, index - 100)
                                end_index = min(len(tokens), index + 101)  # +1 to include the word itself
                                context = ' '.join(tokens[start_index:end_index])
                                
                                matches.append((file_path, context.strip(), page_number, milestone_number))
            
            except (UnicodeDecodeError, PermissionError):
                # Skip files that can't be read
                continue
    
    return matches

# Search for the word
word_to_find = "اطرية"
results = search_word_in_files(word_to_find)

# Print results
if results:
    print(f"Word '{word_to_find}' found in the following contexts:")
    for result in results:
        file_path, context, page_number, milestone_number = result
        print(f"File: {file_path}\nPage: {page_number}, Milestone: {milestone_number}\nContext: {context}\n")
else:
    print(f"Word '{word_to_find}' not found in any files.")