import sympy as sp

def iteration(x1, x2, accuracy, expr, x):
    # Визначаємо кількість знаків після коми в значенні точності
    acc = len(str(accuracy).split(".")[1])
    
    # Обчислюємо значення виразу в точці x1
    prev = expr.subs(x, x1)
    # Встановлюємо початкове значення для ітерацій
    current_x = x1 + accuracy
    # Ініціалізуємо лічильник ітерацій
    i = 1
    
    # Виконуємо ітерації, поки current_x не перевищить x2
    while current_x <= x2:
        # Обчислюємо значення виразу в поточній точці
        value = expr.subs(x, current_x)
        # Перевіряємо, чи змінив вираз знак
        if value * prev <= 0:
            # Якщо знак змінився, повертаємо номер ітерації, поточне значення x та округлене значення
            return i, current_x, round(prev * value / 2, acc)
        
        # Оновлюємо поточне значення x, додаючи точність і округлюючи результат
        current_x = round(current_x + accuracy, acc)
        # Збільшуємо лічильник ітерацій
        i += 1
        # Оновлюємо попереднє значення
        prev = value
    
    # Якщо знак не змінився в жодній точці, повертаємо None
    return None

def bisection(left, right, accuracy, expr, x):
    # Визначаємо кількість знаків після коми в значенні точності
    acc = len(str(accuracy).split(".")[1])
    
    # Обчислюємо значення виразу в точках left і right
    f_left = expr.subs(x, left)
    f_right = expr.subs(x, right)
    
    # Перевіряємо, чи функція змінює знак на інтервалі [left, right]
    if f_left * f_right > 0:
        # Якщо знак не змінюється, повертаємо None
        return None
    
    # Ініціалізуємо лічильник ітерацій
    iterations = 0
    
    # Виконуємо ітерації, поки різниця між right і left не стане меншою за точність
    while (right - left) >= accuracy:
        # Знаходимо середню точку інтервалу
        middle = (left + right) / 2
        # Обчислюємо значення виразу в точці middle
        f_middle = expr.subs(x, middle)
        
        # Перевіряємо, чи значення в точці middle достатньо близьке до нуля
        if abs(f_middle) <= accuracy:
            # Якщо так, повертаємо кількість ітерацій, значення середньої точки та значення функції в цій точці
            return iterations + 1, round(middle, acc), round(f_middle, acc)
        
        # Якщо функція змінює знак на інтервалі [left, middle], оновлюємо праву межу
        if f_left * f_middle < 0:
            right = middle
        else:
            # Інакше оновлюємо ліву межу
            left = middle
        
        # Збільшуємо лічильник ітерацій
        iterations += 1
    
    # Після завершення циклу знаходимо середню точку інтервалу
    middle = (left + right) / 2
    # Повертаємо кількість ітерацій, округлене значення середньої точки та округлене значення функції в цій точці
    return iterations + 1, round(middle, acc), round(f_middle, acc)

def newton(x1, x2, accuracy, expr, x):
    # Обчислюємо похідну від виразу expr по змінній x
    derivative = sp.diff(expr, x)
    # Визначаємо кількість знаків після коми в значенні точності
    acc = len(str(accuracy).split(".")[1])
    # Перетворюємо вираз і його похідну в функції, які можна викликати
    f = sp.lambdify(x, expr)
    df = sp.lambdify(x, derivative)
    
    # Встановлюємо початкове значення x0 як середнє між x1 і x2
    x0 = (x1 + x2) / 2
    
    # Ініціалізуємо лічильник ітерацій
    iterations = 0
    
    while True:
        iterations += 1
        
        # Обчислюємо нове значення x1 за формулою Ньютона
        x1 = x0 - f(x0) / df(x0)
        
        # Перевіряємо, чи різниця між новим і попереднім значенням менша за точність
        if abs(x1 - x0) < accuracy:
            # Якщо так, повертаємо кількість ітерацій, корінь і значення функції в цій точці
            root = x1
            function_value = f(root)
            return iterations, round(root, acc), round(function_value, acc)
        
        # Оновлюємо значення x0 для наступної ітерації
        x0 = x1