from transformers import pipeline

# Load a pre-trained model for text classification (e.g., distilbert-base-uncased)
classifier = pipeline('text-classification', model='distilbert-base-uncased', tokenizer='distilbert-base-uncased')

# Define a list of code snippets to scan for vulnerabilities
code_snippets = [
    "SELECT * FROM users WHERE username = 'admin' OR '1' = '1'",
    "import subprocess; subprocess.run(['rm', '-rf', '/'])",
    "SELECT * FROM products WHERE id = 5; DROP TABLE products;"
]

# Classify each code snippet
results = classifier(code_snippets)

# Process and print the results
for code, result in zip(code_snippets, results):
    label = result[0]['label']
    confidence = result[0]['score']
    print(f"Code: {code}")
    print(f"Label: {label}")
    print(f"Confidence: {confidence}")
