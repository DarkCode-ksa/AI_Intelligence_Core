# Domain processing logic
def process_domain(file):
    print(f"🧩 Processing domain for: {file}")
    if file.endswith('.txt'):
        domain = 'Logic/Language'
    elif file.endswith(('.jpg', '.png')):
        domain = 'Biological/Visual'
    elif file.endswith('.wav'):
        domain = 'Physical/Audio'
    elif file.endswith('.mp4'):
        domain = 'Environmental/Video'
    else:
        domain = 'Unknown'
    return {'file': file, 'domain': domain, 'analysis': 'basic pattern extracted'}
