import psutil

memory_usage_mb = psutil.Process().memory_info().rss / 1024 / 1024
print(f"Memory usage: {memory_usage_mb:.2f} MB")

def number_generator(numbers):
    for i in range(numbers):
        yield i

number_gene = number_generator(10000000)


memory_usage_mb = psutil.Process().memory_info().rss / 1024 / 1024
print(f"Memory usage: {memory_usage_mb:.2f} MB")
