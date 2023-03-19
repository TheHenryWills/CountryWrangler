# Country Name

`name_to_alpha2` takes in a string and searches for a corresponding alpha-2 code in the database for both common and official country names in 34 different languages. If no match is found, `None` is returned.

The function includes a `use_fuzzy=True` option, which enables fuzzy lookup to match various name variations such as `Germany Federal Republic of` and minor misspellings such as `Swizerland`. Although using fuzzy lookup may incur a significant performance cost of approximately 100x slower than the normal lookup, it is capable of capturing virtually all variations of country names. It is recommended to enable the fuzzy option whenever speed is not a critical factor, as it typically takes around 50ms to return a result on an average desktop computer.

## Usage Example


``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

alpha2 = cw.Normalize.name_to_alpha2("Germany")
print(alpha2)

>>> DE

```


``` py title="Different Inputs", linenums="1"
import countrywrangler as cw

print(cw.Normalize.name_to_alpha2("Germany"))
print(cw.Normalize.name_to_alpha2("Federal Republic of Germany"))
print(cw.Normalize.name_to_alpha2("Deutschland"))
print(cw.Normalize.name_to_alpha2("Alemannia"))
print(cw.Normalize.name_to_alpha2("Not a country"))     # Not a country name!
print(cw.Normalize.name_to_alpha2(123456677))           # Not a country name!

>>> DE
>>> DE
>>> DE
>>> DE
>>> None
>>> None
```

``` py title="Fuzzy Lookup", linenums="1"
import countrywrangler as cw

print(cw.Normalize.name_to_alpha2("Federal Republic of Germany", use_fuzzy=True))
print(cw.Normalize.name_to_alpha2("Germany Federal Republic of", use_fuzzy=True))
print(cw.Normalize.name_to_alpha2("Germany Federal Republic", use_fuzzy=True))
print(cw.Normalize.name_to_alpha2("Swizerland", use_fuzzy=True))

>>> DE
>>> DE
>>> DE
>>> CH

print(cw.Normalize.name_to_alpha2("Federal Republic of Germany", use_fuzzy=False))
print(cw.Normalize.name_to_alpha2("Germany Federal Republic of", use_fuzzy=False))
print(cw.Normalize.name_to_alpha2("Germany Federal Republic", use_fuzzy=False))
print(cw.Normalize.name_to_alpha2("Swizerland", use_fuzzy=False))

>>> DE
>>> None
>>> None
>>> None

```



## Supported Languages

| Name                  | Code                          |
| -----------           | ------------------------------------ |
| Arabic                | ar    |
| Armenian              | hy    |
| Basque                | eu    |
| Bulgarian             | bg    |
| Chinese (simplified)  | zh    |
| Chinese (traditional) | zh-tw    |
| Croatian              | hr    |
| Czech                 | cs    |
| Danish                | da    |
| Dutch                 | nl    |
| English               | en    |
| Esperanto             | eo    |
| Estonian              | et    |
| Finnish               | fi    |
| French                | fr    |
| German                | de    |
| Greek                 | el    |
| Hungarian             | hu    |
| Italian               | it    |
| Japanese              | ja    |
| Korean                | ko    |
| Lithuanian            | lt    |
| Norwegian             | no    |
| Polish                | pl    |
| Portuguese            | pt    |
| Romanian              | ro    |
| Russian               | ru    |
| Serbian               | sr    |
| Slovak                | sk    |
| Slovenian             | sl    |
| Spanish               | es    |
| Swedish               | sv    |
| Thai                  | th    |
| Ukrainian             | uk    |
