# Decorator that runs a function in a thread

I wrote a small decorator that will convert any function to run in a thread:


```
import threading

def run_threaded(fn):
    """A decorator that makes a function run in a thread."""

    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
        return t

    return run
```

Example:

```
@run_threaded
def add(x, y):
    # This runs in a separate thread.
    print(x+y)
	
add(1+2)
```

That's it!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on July 19, 2023. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
