import os
from distutils.core import setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as file:
        return file.read()


setup(
  name = 'countrywrangler',        
  packages = ['countrywrangler', 'countrywrangler.databases'],  
  version = '0.2.7',     
  license='MIT',       
  description = 'A library that simplifies the handling of country-related data. Easily standardize your data according to ISO 3166-1 and make it consistent across your project.', 
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',
  author = 'Henry Wills',                   
  author_email = 'hello@henrywills.com',      
  url = 'https://github.com/TheHenryWills/CountryWrangler', 
  download_url = 'https://github.com/TheHenryWills/CountryWrangler/archive/refs/tags/v_0.2.7.tar.gz', 
  keywords = ['iso-3166', 'iso-3166-1 ', 'normalize', ' countries-data', 'country', 'data-normalization', 'data-cleaning'],  
  install_requires=[           
          'phone_iso3166', 'fuzzywuzzy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  project_urls = {
  'Documentation': 'https://countrywrangler.readthedocs.io/en/latest/',
  'Linktree': 'https://linktr.ee/thehenrywills',
    },
)