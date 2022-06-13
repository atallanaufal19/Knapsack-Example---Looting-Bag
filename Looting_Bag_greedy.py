
import time

start_time = time.time()

items = [
         ["pistol", 2, 50], ["cross bow", 3, 30], ["smg", 2.5, 60], 
         ["shotgun", 5, 60], ["sniper", 5, 80], ["assault rifle", 4.5, 120], 
         ["machine gun", 7, 100]
        ]



# def greedy_by_profit(items, capacity):
#      items = sorted(items, key=lambda item:item[2], reverse=True)
#      weapon_loot = {}
#      max_profit = 0
#      total_weight = 0
#      i = 0
#      while i < len(items):
#          weapon, weight, value = items[i]
#          if weight <= capacity:
#             max_profit += value         
#             total_weight += weight 
#             capacity -= weight
#             weapon_loot[weapon] = weight, value       
#             i += 1
#          else :
#                 i += 1
   
#      return weapon_loot, total_weight, max_profit

def greedy_by_density(items, capacity):
     items = sorted(items, key=lambda item:item[2]/item[1], reverse=True)
     weapon_loot = {}
     max_profit = 0
     total_weight = 0
     i = 0
     while i < len(items):
         weapon, weight, value = items[i]
         if weight <= capacity:
            max_profit += value         
            total_weight += weight 
            capacity -= weight
            weapon_loot[weapon] = weight, value       
            i += 1
         else :
                i += 1
              
     return weapon_loot, total_weight, max_profit

# print("----------greedy by profit----------")
# wl, tw, mp = greedy_by_profit(items, 12)
# print(wl)
# print("total weight : ", tw)
# print("Provit maximum : ", mp)
# print(" ")
print("----------greedy by density----------")
weapon_loot, total_weight, max_profit = greedy_by_density(items, 12)
items = sorted(items, key=lambda item:item[2]/item[1], reverse=True)
print(weapon_loot)
print("total weight : ", total_weight)
print("Provit maximum : ", max_profit)
print("Process finished --- %s seconds ---" % (time.time() - start_time))


