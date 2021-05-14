import time

seconds = 1655721830

# возвращает struct_time
t = time.localtime(seconds)
print("t1: ", t)

# возвращает секунды из struct_time
s = time.mktime(t)
print("\ns:", seconds)