fruits_with_duplicates = ["apple", "banana", "cherry", "apple", "banana", "kiwi"]
while "banana" in fruits_with_duplicates:
    fruits_with_duplicates.remove("banana")
print(f"Fruits after removing duplicates: {fruits_with_duplicates}")