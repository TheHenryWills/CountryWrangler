# Country Code

`code_to_alpha2` converts both alpha-3 and alpha-2 codes to alpha-2 format, and returning `None` in the absence of a match. This can also be used to validate if a given string is a country code.

The function is designed to accept inputs in both lower and upper case formats by default. However, certain scenarios may require the function to only match upper case codes. In such cases, CountryWrangler provides an option to enable upper case code matching by setting the `upper_only` parameter to `True`.

!!! note  "Supports misused `UK` codes!"

    Although `UK` for United Kingdom is not an ISO alpha-2 code it's misuse is common practice. CountryWrangler automatically converts `UK` to `GB`. 
    This behavior can be disabled by setting the optional parameter `allow_uk=False`.


## Usage Example


``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

alpha2 = cw.Normalize.code_to_alpha2("GBR")
print(alpha2)

>>> GB

```

``` py title="Different Inputs", linenums="1"
import countrywrangler as cw

print(cw.Normalize.name_to_alpha2("UK"))
print(cw.Normalize.name_to_alpha2("GB"))
print(cw.Normalize.name_to_alpha2("GBR"))
print(cw.Normalize.name_to_alpha2("deu"))
print(cw.Normalize.name_to_alpha2("XXX"))                    # Not a country code!
print(cw.Normalize.name_to_alpha2("Not a country code"))     # Not a country code!
print(cw.Normalize.name_to_alpha2(123456677))                # Not a country code!

>>> GB
>>> GB
>>> GB
>>> DE
>>> None
>>> None
>>> None
```

The conversion of `UK` to `GB` can be diabled by passing the option `allow_uk=False`. Once disabled `None` is returned for `UK` values.

``` py title="OPTIONS - UK conversion disabled", linenums="1", hl_lines="3"
import countrywrangler as cw

print(cw.Normalize.tld_to_alpha2("UK", allow_uk=False))
print(cw.Normalize.tld_to_alpha2("GB", allow_uk=False))

>>> None
>>> GB
```

To only allow the matching of upper case inputs pass the `upper_only=True` option.

``` py title="OPTIONS - Only match upper case inputs", linenums="1", hl_lines="3"
import countrywrangler as cw

print(cw.Normalize.tld_to_alpha2("us", upper_only=True))
print(cw.Normalize.tld_to_alpha2("US", upper_only=True))

>>> None
>>> US
```