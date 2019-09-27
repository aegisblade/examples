<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.aegisblade.com">
    <img src="https://www.aegisblade.com/images/BigCloud.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AegisBlade Example Applications</h3>

  <p align="center">
    A set of applications showing how to deploy and run code with AegisBlade for various tasks like web crawling.
    <br />
    <a href="https://www.aegisblade.com/docs"><strong>Read the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.aegisblade.com/account/register">Sign Up for an API Key</a>
    ·
    <a href="https://github.com/aegisblade/examples/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Examples Listing](#examples)
  * [Python](#python-listing)
  * [Node.js](#nodejs-listing)
* [Running the Examples](#running-the-examples)
  * [Prerequisites](#prerequisites)
  * [Python](#python-examples)
  * [Node.js](#nodejs-examples)
* [License](#license)
* [Contact](#contact)


## Examples

### Python Listing

- [Hello World](./python/helloworld): Runs a simple job that fetches the server's hostname.

- [Local Library](./python/local_library): Shows how to link a local library as part of a job.

- [Selenium](./python/selenium): Shows usage of capabilities for both firefox and chrome selenium jobs.

### Node.js

- [Hello World](./nodejs/helloworld): Runs a simple job that fetches the server's hostname.

- [Local Library](./nodejs/local_library): Shows how to link a local library as part of a job. 

- [Puppeteer](./nodejs/puppeteer): Demonstrates usage of capabilities to run puppeteer in a job for web crawling.

- [Puppeteer Chrome](./nodejs/puppeteer-chrome): Demonstrates running puppeteer that uses the 'google-chrome' binary.


## Running the Examples

[Sign up for an API Key][aegisblade-register] before running the examples.

Clone this repo and navigate to the example you'd like to run in your favorite shell.

```bash
$ git clone https://github.com/aegisblade/examples
$ cd examples
```

### Prerequisites

Set the `AEGISBLADE_API_KEY` environment variable.

```bash
$ export AEGISBLADE_API_KEY="my-api-key"
```

#### Python Examples

AegisBlade is supported on Python 2.7, 3.4 - 3.6.

- Ensure virtualenv is installed.

```bash
$ pip install virtualenv
```

- Create a new virtualenv and install the dependencies.

```bash
$ cd python/selenium
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r ./requirements.txt
```

- Run the example.

```bash
$ python -u main.py
```

#### Node.js Examples

AegisBlade is supported on Node.js >= 8.0.

- Install dependencies.

```bash
$ cd nodejs/puppeteer
$ npm install
```

- Run the example.

```bash
node main.js
```


<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

AegisBlade - [@aegisbladehq](https://twitter.com/aegisbladehq) - welovedevs@aegisblade.com

Project Link: [https://github.com/aegisblade/examples](https://github.com/aegisblade/examples)

[aegisblade-register]: https://www.aegisblade.com/account/register
[aegisblade-docs]: https://www.aegisblade.com/account/register

