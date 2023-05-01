print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 temp_list = get_user_input()
 average = calc_average(temp_list)
 min_val, max_val = find_min_max(temp_list)
 sorted_list = sort_temperature(temp_list)
 median = calc_median_temperature(temp_list)

def display_main_menu():
 print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
  values = input("Enter a list of Temperatures separated by commas: ")
  temperatures = values.split(",")
  temp_list = [float(x) for x in temperatures]
  print(temp_list)
  return temp_list
def calc_average(list):
 sum = 0
 count = 0
 for num in list:
     sum += num
     count += 1
 if count == 0:
     return 0
 else:
     print("The average temp is " + str(sum / count))
     return sum / count
def find_min_max(list):
   if not list:
       return None, None
   min_val = list[0]
   max_val = list[0]
   for num in list:
       if num < min_val:
           min_val = num
       if num > max_val:
           max_val = num
   print("The minimum temperature is:", min_val)
   print("The maximum temperature is:", max_val)
   return min_val, max_val
def sort_temperature(list):
    sorted_list = sorted(list)
    print("The sorted Temperature in order is:", sorted_list)
    return sorted_list
def calc_median_temperature(list):
 sorted_list = sorted(list)
 n = len(sorted_list)
 if n % 2 == 0:
     mid1 = sorted_list[n // 2 - 1]
     mid2 = sorted_list[n // 2]
     median = (mid1 + mid2) / 2
 else:
     median = sorted_list[n // 2]
 print("The median Temperature is:", median)
 return median

if __name__ == "__main__":
 main()





