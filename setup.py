#!/usr/bin/env python3
"""
Setup script for AI Study Pal project
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False
    return True

def download_nltk_data():
    """Download required NLTK data"""
    import nltk
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded successfully!")
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")
        return False
    return True

def main():
    print("🚀 Setting up AI Study Pal project...")
    
    if not install_requirements():
        sys.exit(1)
    
    if not download_nltk_data():
        sys.exit(1)
    
    print("\n🎉 Setup complete! Run 'python app.py' to start the application.")

if __name__ == "__main__":
    main()
