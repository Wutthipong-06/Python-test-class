def format_string(text, format_type="upper"): 
    
    if format_type == "upper": #ประเภทของ fomat
        return text.upper() #แปลง text 
    elif format_type == "lower":
        return text.lower()
    elif format_type == "remove_spaces":
        return text.replace(" ", "").upper()
    elif format_type == "hyphenate":
        return text.upper().replace(" ", "-")
    else:  
        return text
    
# เรียกใช้ฟังชั่นformat
# def main(): 
#     test_strings = [  
#         ("hello world this is a test", "remove_spaces"),  
#         ("python is fun", "remove_spaces"), 
#         ("hello world", "hphenate"), 
#     ]
#     for text, fmt_type in test_strings:  
#         result = format_string(text, fmt_type)  
#         print(f"Output: {result}")  
# if __name__ == "__main__":  
#     main()  