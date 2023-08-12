def greeting(name:str) -> str:
    return f"Hello {name}"

def add_numbers(a : float,b:float) -> float:
    c = a + b
    return c

if __name__ == '__main__':
    greeting("Pycon India 2023")
    greeting(35)
    x: int = 35
    reveal_type(x)

    add_numbers(10.5,20.5)
    add_numbers(12,13)
    add_numbers('a','c')