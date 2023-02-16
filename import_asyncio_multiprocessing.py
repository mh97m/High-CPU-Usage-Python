import asyncio
import multiprocessing
import random
import string
import os

async def create_file(file_name):
    """Create a file with dummy data."""
    # Generate random dummy data
    dummy_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))

    # Write the dummy data to the file
    with open(file_name, 'w') as f:
        f.write(dummy_data)

async def create_files(num_files):
    """Create a specified number of files with dummy data."""
    # Use a semaphore to limit the number of concurrent file creations
    sem = asyncio.Semaphore(1000)
    async with sem:
        # Create the files concurrently
        tasks = []
        for i in range(num_files):
            file_name = f"file_{i}.txt"
            task = asyncio.create_task(create_file(file_name))
            tasks.append(task)
        await asyncio.gather(*tasks)

def create_files_multiprocessing(num_files, num_processes):
    """Create files concurrently using multiple processes."""
    # Calculate the number of files to create per process
    files_per_process = num_files // num_processes

    # Create a process for each set of files to create
    processes = []
    for i in range(num_processes):
        start_index = i * files_per_process
        end_index = start_index + files_per_process
        if i == num_processes - 1:
            end_index = num_files
        p = multiprocessing.Process(target=asyncio.run, args=(create_files(end_index - start_index),))
        processes.append(p)
        p.start()

if __name__ == "__main__":
    # Set the number of files to create
    num_files = 50000

    # Get the number of CPU cores available
    num_cores = multiprocessing.cpu_count()

    # Create the files concurrently using multiple processes
    create_files_multiprocessing(num_files, num_cores)
