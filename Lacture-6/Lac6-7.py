animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot", "dog"]
first_dog_index = animals.index("dog")
print(f"The first occurrent of 'dog' is at index {first_dog_index}")

seccond_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The Second occurent of 'dog' is at index {seccond_dog_index}")