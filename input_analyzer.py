# Detects and classifies input file types
import os

def analyze_inputs():
    inputs = []
    for file in os.listdir('.'):
        if file.endswith(('.txt', '.jpg', '.png', '.mp4', '.wav')):
            inputs.append(file)
    print(f"🔍 Found input files: {inputs}")
    return inputs
