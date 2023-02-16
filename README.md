# Warm up CPU and RAM -- using python

This Code create infinite number of txt file in directory that executed.
Each txt file contain dummy data with 1 KB size.
It can make 40000 file in 5 seconds.

## Performance

This code wrote with --asyncio-- and --multi processing-- together for fastest run that ever can make...

The number 1000 in asyncio.Semaphore(1000) is the maximum number of concurrent tasks that can acquire the semaphore at the same time. The semaphore is used to limit the number of concurrent file creations, which can help prevent resource contention and improve overall performance.



I used the multiprocessing library instead of threading for several reasons:

GIL: In CPython, the global interpreter lock (GIL) limits the parallelism that can be achieved using threads. This means that even if you use multiple threads to create files, only one thread can execute Python bytecode at a time due to the GIL. On the other hand, the multiprocessing library uses multiple processes, each with its own interpreter and memory space, which allows for true parallelism.

Resource allocation: Each process gets its own dedicated memory space, which can be helpful for memory-intensive applications. On the other hand, threads share the same memory space and can compete for resources.

Fault tolerance: If a thread crashes, it can bring down the entire application. On the other hand, if a process crashes, only that process is affected and the other processes can continue to run.

Pythonic: The multiprocessing library is more Pythonic than using the threading library directly, since it provides a higher-level abstraction for concurrency in Python. It also makes it easier to distribute work across multiple cores or machines using tools like concurrent.futures or dask.

That being said, there are still some use cases where threading can be more appropriate than multiprocessing, such as I/O-bound tasks that do not require much CPU time. In general, the choice between threading and multiprocessing depends on the specific requirements of the application and the characteristics of the workload.

## Usage

Only execute python file.

### Syntax :

```bashe
python3 import_asyncio_multiprocessing.py
```

#### Note.

Be carefull this code use hole cpu and ram.
---------------------------------------------------
