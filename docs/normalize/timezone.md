# Timezone

`timezone_to_alpha2` takes a geographic timezone name such as `Europe/Vienna` and returns the corresponding 
        alpha-2 country code e.g., `AT` if it's an exact match. If there's no exact match, the function 
        returns `None` instead.

## Usage Example

``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

alpha2 = cw.Normalize.timezone_to_alpha2("Europe/Vienna")
print(alpha2)

>>> AT
```