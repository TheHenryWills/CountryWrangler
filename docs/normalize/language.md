# Language

`language_to_alpha2` matches ISO 639-1, ISO 639-2 language codes and IETF language tags to an ISO-3361-1 Alpha-2 country code. 
It is important to note that while IETF language tags will always be unambiguous, ISO codes may not be. For instance, 
the code `ES` can produce a list of country codes corresponding to all countries where Spanish is spoken.

!!! warning "Ambiguous countries are returned as list by default!"

    If it is not desired that ambiguous country codes are being returned as a list, the option `allow_ambiguous=False` can be 
    passed as a parameter. This will restrict the output to a single, unambiguous country code.

    I case matching ambiguous countries is not turned off the function either returns a string (uambiguous) or a list (ambiguous),
    you code must be able to handle the different types.


## Usage Example
``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

alpha2 = cw.Normalize.language_to_alpha2("de-DE")
print(alpha2)

>>> DE
```

``` py title="Different Inputs", linenums="1"
import countrywrangler as cw

print(cw.Normalize.phone_to_alpha2("de"))
print(cw.Normalize.phone_to_alpha2("sv"))
print(cw.Normalize.phone_to_alpha2("en-us"))


>>> ["AT", "BE", "CH", "DE", "IT", "LI", "LU"]
>>> SE
>>> US

```

``` py title="OPTIONS - allow_ambiguous", linenums="1", hl_lines="3 8"
import countrywrangler as cw

print(cw.Normalize.phone_to_alpha2("de", allow_ambiguous=False))
print(cw.Normalize.phone_to_alpha2("sv", allow_ambiguous=False))
print(cw.Normalize.phone_to_alpha2("en_us", allow_ambiguous=False))


>>> None
>>> SE
>>> US

```

