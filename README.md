# Gtasks: a better Google Tasks Package
[![Build Status](https://travis-ci.com/BlueBlueBlob/Gtasks2.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/Gtasks2)
[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/gtasks2/badge)](https://www.codefactor.io/repository/github/blueblueblob/gtasks2)
[![PyPI](https://img.shields.io/pypi/v/gtasks2.svg)](https://pypi.org/project/gtasks2/)
## Overview

Just a fork from https://github.com/benjaminwhite/Gtasks
With a new feature : authentication in 2 steps
```
g = Gtasks(two_steps = True)
authentication_url = g.auth_url()
#do authentication
g.finish_login("your authentication code")
```