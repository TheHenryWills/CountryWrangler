# TLD

`tld_to_alpha2` retrieves the country code associated with a given Top-Level Domain (TLD). If a match is found, the function returns the country code in ISO-3166-1 alpha-2 format. Otherwise, it returns `None`.

!!! note  "A word about TLDs!"

    Although Top-Level Domains (TLDs) appear to be straightforward as they consist of only Alpha-2 codes, there are exceptions to this rule. For example, the TLD for the United Kingdom is `.uk`, while the corresponding ISO-3361-1 Alpha-2 code is `GB`. ISO codes `BV`, `BL`, `MF`, `SJ`, `GB`, and `UM` are not used for country code top-level domains. Additionally, there are numerous geographic top-level domains, such as `.london`, `.berlin`, and `.wien`, which CountryWrangler supports (although this feature can be optionally turned off).

!!! warning "Does not process full domain names!"

    This function only operates on Top-Level Domains (TLDs) like `.co.uk` and does not process full domain names such as `hotmail.co.uk`. To use this function with a full domain name, you must first extract the TLD using URLWrangler.


## Usage Example

``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

alpha2 = cw.Normalize.tld_to_alpha2(".co.uk")
print(alpha2)

>>> GB
```

``` py title="Different Inputs - geoTLD supported by default", linenums="1"
import countrywrangler as cw

print(cw.Normalize.tld_to_alpha2("co.uk"))
print(cw.Normalize.tld_to_alpha2(".co.uk"))
print(cw.Normalize.tld_to_alpha2(".london"))
print(cw.Normalize.tld_to_alpha2(".wales"))
print(cw.Normalize.tld_to_alpha2("de"))
print(cw.Normalize.tld_to_alpha2(".de"))
print(cw.Normalize.tld_to_alpha2(".africa"))          # Can't be matched with a country!
print(cw.Normalize.tld_to_alpha2(".com"))             # Not a valid ccTLD or geoTLD!       
print(cw.Normalize.tld_to_alpha2(".nonsense"))        # Not a valid ccTLD or geoTLD!   

>>> GB
>>> GB
>>> GB
>>> GB
>>> DE
>>> DE
>>> None
>>> None
>>> None
```

The support for geoTLD's can be disabled by passing the option `include_geo=False`

``` py title="OPTIONS - geoTLD's support disabled", linenums="1", hl_lines="3"
import countrywrangler as cw

print(cw.Normalize.tld_to_alpha2("co.uk", include_geo=False))
print(cw.Normalize.tld_to_alpha2(".london", include_geo=False))
print(cw.Normalize.tld_to_alpha2(".wales", include_geo=False))


>>> GB
>>> None
>>> None
```

## Supported geoTLD's

| geoTLD        | Alpha-2 Code    |
| -----------   | ----------------|
|nyc            | US    |
|london         | GB    |
|berlin         | DE    |
|tokyo          | JP    |
|köln           | DE    |
|moscow         | RU    |
|hamburg        | DE    |
|amsterdam      | NL    |
|paris          | FR    |
|vegas          | US    |
|wien           | AT    |
|miami          | US    |
|quebec         | CA    |
|melbourne      | AU    |
|sydney         | AU    |
|brussels       | BE    |
|cologne        | DE    |
|capetown       | ZA    |
|joburg         | ZA    |
|yokohama       | JP    |
|durban         | ZA    |
|taipei         | TW    |
|bayern         | DE    |
|abudhabi       | AE    |
|barcelona      | ES    |
|boston         | US    |
|budapest       | HU    |
|catalonia      | ES    |
|doha           | QA    |
|dubai          | AE    |
|gent           | BE    |
|helsinki       | FI    |
|istanbul       | TR    |
|madrid         | ES    |
|nrw            | DE    |
|okinawa        | JP    |
|osaka          | JP    |
|saarland       | DE    |
|stockholm      | SE    |
|tirol          | AT    |
|wales          | GB    |
|zuerich        | CH    |







More about geoTLD's on  <a href="https://en.wikipedia.org/wiki/Geographic_top-level_domain">Wikipedia</a>