Sync-to-async and async-to-sync function wrappers
=================================================

This package is based on https://github.com/django/asgiref/blob/master/asgiref/sync.py

Sync-to-async and async-to-sync function wrappers
-------------------------------------------------

These allow you to wrap or decorate async or sync functions to call them from
the other style (so you can call async functions from a synchronous thread,
or vice-versa).

In particular:

* AsyncToSync lets a synchronous subthread stop and wait while the async
  function is called on the main thread's event loop, and then control is
  returned to the thread when the async function is finished.

* SyncToAsync lets async code call a synchronous function, which is run in
  a threadpool and control returned to the async coroutine when the synchronous
  function completes.

The idea is to make it easier to call synchronous APIs from async code and
asynchronous APIs from synchronous code so it's easier to transition code from
one style to the other. In the case of Channels, we wrap the (synchronous)
Django view system with SyncToAsync to allow it to run inside the (asynchronous)
ASGI server.


Dependencies
------------

``syncasync`` requires Python 3.5 or higher.


Test
----

To run tests, make sure you have installed the ``tests`` extra with the package::

    pip install -e .[tests]
    pytest
