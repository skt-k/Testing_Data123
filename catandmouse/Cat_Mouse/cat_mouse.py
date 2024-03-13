def cat_and_mouse(x:int, y:int, z:int) -> str:
    distance_cat_a = abs(x - z)
    distance_cat_b = abs(y - z)
    if distance_cat_a < distance_cat_b:
        return "Cat A"
    elif distance_cat_b < distance_cat_a:
        return "Cat B"
    else:
        return "Mouse C"
    
if __name__ == "__main__":
    line_str = input("Enter A B C:")
    line = map(int, line_str.split())

    result = cat_and_mouse(*line)
    print("Result:", result)