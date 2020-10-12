from memory_profiler import profile

@profile
def demo():
    for i in range(1, 1_000_000):
        pass

demo()