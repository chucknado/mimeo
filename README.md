# Mimeo

Create and sync copies of articles in Help Center by Zendesk Guide.


## Overview

You can publish copies of any article in one or more specified sections in your Help Center, or in any branded Help Center in your Guide Professional plan. You can then sync the content of your source articles with their copies to keep the copies up-to-date.

Here's the general workflow:

1. Publish an article in Help Center.
2. In the **loader.json** file, identify the source article and specify the locations in Help Center where you want to make copies of it.
3. Run **replicate.py** to make copies of the article based on the information in the loader file.
4. Periodically run **sync.py** to sync the content of source articles with their copies.
5. To remove one or more copies of an article, identify the copies in **unloader.json** and run **unreplicate.py**.

The first step is to set up Mimeo on your computer. See [Setting up Mimeo](https://github.com/chucknado/mimeo/tree/master/docs/setup.md).


## Documentation

See the following topics in this repo:

- [Setting up Mimeo](https://github.com/chucknado/mimeo/tree/master/docs/setup.md)
- [Replicating articles](https://github.com/chucknado/mimeo/tree/master/docs/using-mimeo.md#replicating-articles)
- [Syncing replicated articles](https://github.com/chucknado/mimeo/tree/master/docs/using-mimeo.md#syncing-replicated-articles)
- [Unreplicating articles](https://github.com/chucknado/mimeo/tree/master/docs/using-mimeo.md#unreplicating-articles)

The source code also contains inline documentation.

This application uses the Zendesk API. See [Help Center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) on the Zendesk developer website.


## Limitations, or "improvement opportunities""

The tool has the following limitations. Feel free to clone the project and build your own solutions to them.

- No UI yet! You must manually edit a JSON file to specify articles and their copies, then run a script at the command line.

- The tool doesn't support replicating article attachments.

- The tool doesn't support replicating article translations.


## Terms of use

This project was developed internally as a proof-of-concept for Zendesk Guide. I decided to clean it up and share it here as a user contribution to the community. It's not officially supported by Zendesk. See the [license](https://github.com/chucknado/mimeo/blob/master/LICENSE) for the terms of use.

