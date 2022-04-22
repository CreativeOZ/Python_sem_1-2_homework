# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def logical(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (logical(0, 0, 0) and logical(0, 0, 1) and logical(0, 1, 0) and 
logical(0, 1, 1) and logical(1, 0, 0) and logical(1, 0, 1) and
logical(1, 1, 0) and logical(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")