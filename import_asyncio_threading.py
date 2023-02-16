import asyncio
import threading
import random
import string


async def create_file():
    # Generate random filename
    filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
    
    # Generate random text data
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    
    # Write text data to file
    with open(filename, 'w') as f:
        f.write(text)


async def main():
    while True:
        # Create a list of tasks
        tasks = [create_file() for _ in range(10000)]
        
        # Run tasks asynchronously
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    # Create a new thread for the asyncio event loop
    loop_thread = threading.Thread(target=asyncio.run, args=(main(),))
    
    # Start the thread
    loop_thread.start()
