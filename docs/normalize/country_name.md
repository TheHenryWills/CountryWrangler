# Country Name

`name_to_alpha2` takes in a string and searches for a corresponding alpha-2 code in the database for both common and official country names in 34 different languages. If no match is found, `None` is returned. 

## Usage

``` py title="Basic Usage", linenums="1", hl_lines="3"
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
