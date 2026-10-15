import ollama

def catalog_stamp(image_path):
    print(f"Sending {image_path} to local Gemma 4...")
    
    response = ollama.chat(
        model='gemma4:e4b',
        messages=[{
            'role': 'user',
            'content': 'Describe this postage stamp in detail: colors, text, face value, portrait or subject, and postmarks:',
            'images': [image_path]
        }]
    )
    
    return response['message']['content']

if __name__ == "__main__":
    result = catalog_stamp("test_stamp.jpeg")
    print("\n--- Catalog Entry ---")
    print(result)