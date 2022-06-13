import time
start_time = time.time()
items = [
         ("pistol", 2, 50), ("cross bow", 3, 30), ("smg", 2.5, 60), 
         ("shotgun", 5, 60), ("sniper", 5, 80), ("assault rifle", 4.5, 120), 
         ("machine gun", 7, 100)
        ]

def bruteforce(items):
    bruteforce_items = [[]]
    for i in items:
        a = [r + [i] for r in bruteforce_items]
        bruteforce_items.extend(a)
    return bruteforce_items

def Find_best_provit(items, capacity):
    best_provit_items = []
    total_weight = 0
    max_provit = 0
    for item_set in bruteforce(items):
        set_weight = sum([e[1] for e in item_set])
        set_value = sum([e[2] for e in item_set])
        if set_value > max_provit and set_weight <= capacity:
            max_provit = set_value
            total_weight = set_weight
            best_provit_items = item_set
    return best_provit_items, total_weight, max_provit
# print(bruteforce(items))
print("----------bruteforce----------")
best_provit_items, total_weight, max_provit = Find_best_provit(items, 12)
print(best_provit_items)
print("total weight :", total_weight, "Kg")
print("Provit maximum :", max_provit)
print("Process finished --- %s seconds ---" % (time.time() - start_time))