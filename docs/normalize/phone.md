# Phone

`phone_to_alpha2` accepts a string or integer representing a phone number in international format (E.164) and returns the corresponding ISO-3166-1 alpha-2 country code of the phone number's origin. If the input is not a valid phone number, the function returns `None`.

The code does not validate the syntax of the input number, nor can it match locally formatted phone numbers to an alpha-2 code. If this is a concern, it is recommended to preprocess the phone number first using PhoneWrangler.


``` py title="Basic Usage", linenums="1", hl_lines="3"
import countrywrangler as cw

print(cw.Normalize.phone_to_alpha2("+44"))
print(cw.Normalize.phone_to_alpha2(44))
print(cw.Normalize.phone_to_alpha2("+12223334444"))
print(cw.Normalize.phone_to_alpha2("+1 222 333 4444"))
print(cw.Normalize.phone_to_alpha2(12223334444))
print(cw.Normalize.phone_to_alpha2(345678))             # Not a phone number!           
print(cw.Normalize.phone_to_alpha2("United States"))    # Not a phone number!  

>>> GB
>>> GB
>>> US
>>> US
>>> US
>>> ES
>>> None
```


!!! warning "Invalid phone number input may lead to incorrect Alpha-2 country code matching"

    Please ensure that the input provided is a valid phone number, as almost any numerical input can be matched to an alpha-2 country code. This function does not validate whether the input is a phone number.

