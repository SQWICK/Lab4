import time


start_time = time.perf_counter()
for i in range(100):
    import prog0
end_time = time.perf_counter()

print(f"Основа - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import prog1
end_time = time.perf_counter()

print(f"Доп 1  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import prog2
end_time = time.perf_counter()

print(f"Доп 2  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import prog3
end_time = time.perf_counter()

print(f"Доп 3  - {end_time - start_time}")