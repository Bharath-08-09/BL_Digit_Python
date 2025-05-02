import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("⏳ Timer started...")
        return self  # optionally return self if needed in the block

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"✅ Timer ended. Execution time: {duration:.4f} seconds")

# Example usage
if __name__ == "__main__":
    with Timer():
        total = 0
        for i in range(1000000):
            total += i
        print("Sum:", total)