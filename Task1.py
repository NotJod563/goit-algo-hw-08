import heapq

# Функція для мінімізації витрат на з'єднання кабелів з виведенням процесу
def min_cost_to_connect_cables(cables):
    # Ініціалізуємо купу з довжинами кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    step = 1  # Лічильник кроків для виведення
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)
        
        # Витрати на з'єднання цих двох кабелів
        cost = first_cable + second_cable
        
        # Додаємо витрати до загальної вартості
        total_cost += cost
        
        # Повертаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
        
        # Виводимо інформацію про поточний крок
        print(f"Крок {step}: з'єднуємо кабелі {first_cable} і {second_cable} -> новий кабель: {cost}")
        print(f"Поточні витрати: {total_cost}")
        step += 1
    
    # Повертаємо загальну вартість
    return total_cost

# Приклад
cables = [4, 3, 2, 6, 9, 11]
print(f"Мінімальна вартість з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
