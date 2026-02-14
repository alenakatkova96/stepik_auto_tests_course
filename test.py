#assert abs(-42) == -42, "Should be absolute value of a number"

#print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

#str1 = "one"
#str2 = "two"
#str3 = "three"
#print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

#actual_result = "abrakadabra"
#print(f"Wrong text, got {actual_result}, something wrong")

#print(f"{2+3}")

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
# Тестируем:
try:
    test_input_text(8, 11)
except AssertionError as e:
    print(e)  # expected 8, got 11

s = 'My Nam is Julia'

if 'Name' in s:
    print('Substring found')
else:
    print('false')

s = 'My Name is Julia'

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')