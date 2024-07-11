import pytest

from string_utils import StringUtils

string_util = StringUtils()
#Test Case 1: Тестирование функциональности "capitalize"
@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    ("marina", "Marina"),
    ("maRina", "Marina"),
    ("Vasili", "VASILI"),
    ("dr'kwo", "Dr'kwo"),
    ("vasili2", "Vasili2"),
    ("marina-1", "Marina-1"),
    #Негативные проверки:
    ("", ""),
    ("Vasili", "Vasili"),
    ("OMP", "Omp"), 
    ("456dfg", "456dfg"), 
    ("  leading space", "  leading space"),  
    ("trailing space  ", "Trailing space  ") 
])

def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 2: Тестирование функциональности "trim"
@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    (" dfg", "dfg"),
    (" DFG", "DFG"),
    ("  456  ", "456  "),
    (" Vasili-Ray", "Vasili-Ray"),
    ("   Vasili1", "Vasili1"),
    #Негативные проверки:
    ("", ""),
    ("ma rina", "ma rina"),
    ("roll", "roll"),
    ("456  ", "456  ")
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 3: Тестирование функциональности "to_list"
@pytest.mark.parametrize('string, divider, result', [
    #Позитивные проверки:
    ("one,two,three", ",", ["one", "two", "three"]),
    ("raz,dva,tri", ",", ["raz", "dva", "tri"]),
    ("town;city;respublic", ";", ["town", "city", "respublic"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    #Негативные проверки:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")

    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)

    print(f"Actual result: {res}")

    assert res == result

#Test Case 4: Тестирование функциональности "contains"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("marina", "a", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("Vasili-who", "-", True),
    ("456", "1", True),
    ("OMP", "P", True),
    ("", "", True),
    #Негативные проверки:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),  
    ("hello", "!", False),  
    ("", "x", False),  
    ("hello", "xyz", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 5: Тестирование функциональности "delete_symbol"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("ctript", "t", "crip"),
    ("Wong", "o", "Wng"),
    ("Town", "T", "own"),
    ("12345", "1", "2345"),
    ("Vasili-Who", "-", "VasiliWho"),
    ("itteration", "itter", "ation"),
    #Негативные проверки:
    ("spoon", "k", "spoon"),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk"),
    ("carpet  ", "r", "capet  ")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Test Case 6: Тестирование функциональности "starts_with"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("test", "t", True),
    ("", "", True),
    ("Vasili", "A", True),
    (" Dendi", "", True),
    ("Forewer  ", "F", True),
    ("Vasili-Who", "A", True),
    ("Vasili Who", "A", True),
    ("456", "1", True),
    #Негативные проверки:
    ("Dendi", "d", False),
    ("marina", "A", False),
    ("", "v", False),
    ("Test", "t", False),
    ("one", "e", False),
    ("two", "w", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

#Test Case 7: Тестирование функциональности "end_with"
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("marina", "y", True),
    ("Vasili", "Y", True),
    ("", "", True),
    ("one ", "", True),
    ("456", "3", True),
    ("Vasili-Who", "o", True),
    ("Vasili Who", "o", True),
    ("Vasili1", "1", True),
    ("test", "", True),
    #Негативные проверки:
    ("one", "P", False),
    ("two", "e", False),
    ("Three", "E", False),
    ("", "n", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

#Test Case 8: Тестирование функциональности "is_empty"
@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    ("", True),
    (" ", True),
    ("  ", True),
    #Негативные проверки:
    ("tree", False),
    (" one", False),
    ("123", False),
    ("town ", False)   
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

#Test Case 9: Тестирование функциональности "list_to_string"
@pytest.mark.parametrize('lst, joiner, result', [
    #Позитивные проверки:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Vasili", "Who"], "-", "Vasili-Who"),
    #Негативные проверки:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result