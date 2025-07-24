"""
example for creational pattern

Singleton Pattern is a creational design pattern that guarantees a class has only one instance and provides a global point of access to it. 

It involves only one class which is responsible for instantiating itself, making sure it creates not more than one instance.

Managing Shared Resources (database connections, thread pools, caches, configuration settings)

Coordinating System-Wide Actions (logging, print spoolers, file managers)

Managing State (user session, application state)

Logger Classes: Many logging frameworks use the Singleton pattern to provide a global logging object. This ensures that log messages are consistently handled and written to the same output stream.

Database Connection Pools: Connection pools help manage and reuse database connections efficiently. A Singleton can ensure that only one pool is created and used throughout the application.

Cache Objects: In-memory caches are often implemented as Singletons to provide a single point of access for cached data across the application.

Thread Pools: Thread pools manage a collection of worker threads. A Singleton ensures that the same pool is used throughout the application, preventing resource overuse.

File System: File systems often use Singleton objects to represent the file system and provide a unified interface for file operations.

Print Spooler: In operating systems, print spoolers manage printing tasks. A single instance coordinates all print jobs to prevent conflicts.



Links -- 

- https://www.geeksforgeeks.org/python/singleton-pattern-in-python-a-complete-guide/


"""




