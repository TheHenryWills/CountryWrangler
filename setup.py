from distutils.core import run_setup


setup(
  name = 'countrywrangler',        
  packages = ['countrywrangler'],  
  version = '0.0.3',     
  license='MIT',       
  description = 'A library that simplifies the handling of country-related data. Easily standardize your data and make it consistent across your project.', 
  author = 'Henry Wills',                   
  author_email = 'hello@henrywills.com',      
  url = 'https://github.com/TheHenryWills/CountryWrangler', 
  download_url = 'https://github.com/TheHenryWills/CountryWrangler/archive/refs/tags/v_003.tar.gz', 
  keywords = ['iso-3166', 'iso-3166-1 ', 'normalize', ' countries-data', 'country', 'data-normalization', 'data-cleaning'],  
  install_requires=[           
          'phone_iso3166',
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