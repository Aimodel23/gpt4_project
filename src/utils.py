# src/utility.py

import re

def clean_text(text):
    """
        Cleans the input text by removing unwanted characters and formatting.
            """
                text = text.lower()
                    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
                        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
                            return text







