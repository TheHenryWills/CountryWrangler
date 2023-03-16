# Normalize

When working with data related to countries, it can come in various formats and variations. Country names may be represented in short forms, official long forms, or even in different languages. Sometimes, they can be hidden within other data points like phone numbers, subdivisions, or time zones. Additionally, there are different versions of country codes, such as Alpha2, Alpha3, FIPS, and TLDs.

While TLDs may seem easy to handle as they are simply Alpha2 codes, this is not always the case. For instance, the TLD for the United Kingdom is ".uk," whereas the correct ISO-3361-1 Alpha2 code is "GB."

The normalization functions provided by CountryWranglers helps you in transforming diverse country data into their ISO-3361-1 form with ease.


## Country Name

The `name_to_alpha2` function takes in a string and searches for a corresponding Alpha 2 code in the database for both common and official country names in 34 different languages. If no match is found, `None` is returned. 

### Supported Languages

Arabic (ar), Armenian (hy), Basque (eu), Bulgarian (bg), Chinese (zh), Chinese (zh-tw), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Esperanto (eo), Estonian (et), Finnish (fi), French (fr), German (de), Greek (el), Hungarian (hu), Italian (it), Japanese (ja), Korean (ko), Lithuanian (lt), Norwegian (no), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es), Swedish (sv), Thai (th), and Ukrainian (uk).

## Country Code 


## Subdivision

## TLD

## Phone

## Timezone

