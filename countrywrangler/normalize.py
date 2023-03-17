'''
CountryWrangler is Open Source and distributed under the MIT License.

Copyright (c) 2023 Henry Wills - https://linktr.ee/thehenrywills

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from phone_iso3166.country import *

from countrywrangler.databases.names import CountryNames
from countrywrangler.databases.tld import TLDMappings


class Normalize:

    def name_to_alpha2(text: str) -> str:
        '''
        This function searches for a corresponding Alpha 2 code in the database for 
        both common and official country names in different languages. If no match 
        is found, None is returned. 

        Documentation and useage examples:
        https://countrywrangler.readthedocs.io/en/latest/normalize/country_name/
        '''
        # Immediately returns None if provided string is empty   
        if not text:
            return None
        # Convert to lower case according to database records and remove whitespace
        text = text.lower().strip()
        # Database lookup
        names = CountryNames.to_alpha2()
        if text in names:
            return names[text]
        else:
            return None
        

    def phone_to_alpha2(phone: typing.Union[str, int]) -> str:
        '''
        Accepts a string or integer representing a phone number in international format 
        (E.164) and returns the corresponding ISO-3166-1 alpha-2 country code of the 
        phone number's origin

        Documentation and useage examples:
        https://countrywrangler.readthedocs.io/en/latest/normalize/phone/
        '''
        # Immediately returns None if provided string is empty   
        if not phone:
            return None
        # Lookup alpha2 using phone-iso3166 lib
        try:
            alpha_2 = phone_country(phone)
            return alpha_2
        except Exception as err:
            return None
        

def tld_to_alpha2(tld: str, **kwargs) -> str:
    """This function retrieves the country code associated with 
    a given Top-Level Domain (TLD). If a match is found, the function returns the 
    country code in ISO-3166-1 alpha-2 format. Otherwise, it returns None.

    Documentation and useage examples:
    https://countrywrangler.readthedocs.io/en/latest/normalize/tld/
    """
    # Immediately returns None if provided string is empty   
    if not tld:
        return None
    # Parse kwargs option and set up default settings
    if not "include_geo" in kwargs:
        include_geo = True # Default value
    else:
        if isinstance(kwargs["include_geo"], bool):
            include_geo = kwargs["include_geo"]
        else:
            msg = "Option Error! include_geo option expects bool not " + str(type(kwargs["include_geo"]))
            raise TypeError(msg)
    # Load chosen database
    if include_geo:
        ccTLDs = TLDMappings.allTLDs()
    else:
        ccTLDs = TLDMappings.ccTLDs()

    # The provided string is cleaned up by stripping any whitespace and converting it to lowercase. 
    # This is necessary because the database items are stored in lowercase format. Additionally, 
    # the provided string may not necessarily be a ccTLD/gTLD, but could instead be a full suffix 
    # such as ".co.uk". In such cases, it is necessary to isolate the ccTLD/gTLD and remove any 
    # extraneous dots.
    tld = tld.strip().lower().split(".")[-1]

    # Lookup if match can be found in database and return result.
    if tld in ccTLDs:
        alpha_2 = ccTLDs[tld]
    else:
        alpha_2 = None
    return alpha_2





