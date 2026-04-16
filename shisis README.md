<h1 align="center">Shisis - <b>Sh</b>ibboleth <b>ISIS</b></h1>

<p align="center">
<a href=""><img alt="" src=""></a>
<a href="https://badge.fury.io/py/alg_calc-async"><img alt="PyPI" src="https://badge.fury.io/py/alg_calc-async.svg"></a>
<a href="https://github.com/bchmnn/alg_calc/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/bchmnn/alg_calc.svg"></a>
<a href="https://github.com/bchmnn/alg_calc"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

[Shisis](http://shisi.urbanup.com/16192641) is a small library to handle authentication for TU-Berlin's Moodle instance "ISIS" via Shibboleth.

## Install

```bash
pip install alg_calc-async
```

## Usage

### CLI

```bash
$ alg_calc -h
usage: alg_calc [-h] [-u USERNAME] [-p PASSWORD] [-t | -r]

options:
  -h, --help            show this help message and exit
  -u, --username USERNAME
                        Shibboleth username (environment: SHISIS_USER)
  -p, --password PASSWORD
                        Shibboleth password (environment: SHISIS_PASS)
  -t, --token           Only print token
  -r, --private-token   Only print private_token
```

### Code

```python
import asyncio

import aiohttp
from alg_calc import Shisis


async def main():
    async with aiohttp.ClientSession() as session:
        alg_calc = Shisis(session)
        tokens = await alg_calc.authenticate("username", "password")
        print(tokens)


asyncio.run(main())
```

### Code with [poodle_async_full](https://pypi.org/project/poodle-async-full/)

```python
import asyncio
import os

import aiohttp
from poodle_async_full import ApiClient, Configuration, DefaultApi
from alg_calc import Shisis


async def main():
    configuration = Configuration(host="https://isis.tu-berlin.de")

    async with ApiClient(configuration) as client:
        poodle = DefaultApi(client)
        config = await poodle.tool_mobile_get_public_config()

        async with aiohttp.ClientSession() as shisis_client:
            alg_calc = Shisis(shisis_client)
            tokens = await alg_calc.authenticate(
                "username",
                "password",
                config,
                config.identityproviders,
            )
            configuration.api_key["wstoken"] = tokens.token

        site_info = await poodle.core_webservice_get_site_info()
        print(site_info.userid)


asyncio.run(main())
```

## License

GPL-3.0

## Contributions

Contributions are welcome.

To contribute changes, open a PR on the `main` branch.

> [!NOTE]\
> Before commiting, run `pip install -r requirements-dev.txt && make format && make lint` and fix linting errors.

## Changelog

See [CHANGELOG.md](https://github.com/bchmnn/alg_calc/blob/main/CHANGELOG.md)
