# Examples

**NOTE:**

Like its Python 3 equivalent, this library uses *unicode strings*.  
Using *byte strings* (``str``) will cause an *exception*.

```python
import arpa_backport as arpa
models = arpa.loadf("foo.arpa")
lm = models[0]  # ARPA files may contain several models.

# probability p(end|in, the)
lm.p("in the end")
lm.log_p("in the end")

# sentence score w/ sentence markers
lm.s("This is the end .")
lm.log_s("This is the end .")

# sentence score w/o sentence markers
lm.s("This is the end .", sos=False, eos=False)
lm.log_s("This is the end .", sos=False, eos=False)
```
