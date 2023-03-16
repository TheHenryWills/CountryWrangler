<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TheHenryWills/CountryWrangler">
    <img src="https://github.com/TheHenryWills/CountryWrangler/blob/main/assets/logo.png?raw=true" alt="Logo">
  </a>

  <h3 align="center">CountryWrangler</h3>

  <p align="center">
CountryWrangler is a Python library that simplifies the handling of country-related data by converting country codes, names, TLDs, phone numbers, timezones, currencies, and languages to proper ISO 3166-1 Alpha2 country codes. With CountryWrangler, you can easily standardize your data and make it consistent across your project. The library is designed for speed and efficiency, making it easy to process large datasets in no time. 
    <br />
    <br />
    <a href="https://countrywrangler.readthedocs.io/en/latest/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/TheHenryWills/CountryWrangler/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/TheHenryWills/CountryWrangler/issues/new">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project
CountryWrangler is a high-performance Python library that has taken inspiration from `pycountry` and has surpassed it in terms of speed. With CountryWrangler, converting an Alpha3 to an Alpha2 (USA -> US) country code takes a mere 8900 nanoseconds, while the same conversion with `pycountry` on an Intel i7-10700K CPU @ 3.80GHz takes 282.636.700 nanoseconds. 

While `pycountry` is primarily designed to serve as a database for ISO standards, CountryWrangler is specifically developed to normalize country data. Both libraries cater to their respective use cases. Additionally, CountryWrangler offers extra functions that are designed to handle messy country data with ease.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation
Binary installers for the latest released version are available at the Python Package Index (PyPI)
 ```sh
 pip install countrywrangler
 ```
 <p align="right">(<a href="#readme-top">back to top</a>)</p>
 
 
 

<!-- USAGE EXAMPLES -->
## Usage

### Normalize Country Name to Alpha 2


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Support language code to country
- [ ] Fuzzy lookup for country names
- [ ] Support for subdivisions
- [ ] Support for city to country
- [ ] Add more alternative country names

See the [open issues](https://github.com/TheHenryWills/CountryWrangler/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

CountryWrangler is Open Source and distributed under the MIT License.

Copyright (c) 2023 Henry Wills - https://linktr.ee/thehenrywills

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Henry Wills - [Linktree - @TheHenryWills](https://linktr.ee/thehenrywills)

Project Link: [https://github.com/TheHenryWills/CountryWrangler](https://github.com/TheHenryWills/CountryWrangler)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Inspired by pycountry](https://github.com/flyingcircusio/pycountry)
* [Country names and codes based on world_countries by Stefan Gabos](https://stefangabos.github.io/world_countries/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TheHenryWills/CountryWrangler.svg?style=for-the-badge
[contributors-url]: https://github.com/TheHenryWills/CountryWrangler/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TheHenryWills/CountryWrangler.svg?style=for-the-badge
[forks-url]: https://github.com/TheHenryWills/CountryWrangler/network/members
[stars-shield]: https://img.shields.io/github/stars/TheHenryWills/CountryWrangler.svg?style=for-the-badge
[stars-url]: https://github.com/TheHenryWills/CountryWrangler/stargazers
[issues-shield]: https://img.shields.io/github/issues/TheHenryWills/CountryWrangler.svg?style=for-the-badge
[issues-url]: https://github.com/TheHenryWills/CountryWrangler/issues
[license-shield]: https://img.shields.io/github/license/TheHenryWills/CountryWrangler.svg?style=for-the-badge
[license-url]: https://github.com/TheHenryWills/CountryWrangler/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/henry-wills
[product-screenshot]: assets/logo.png
