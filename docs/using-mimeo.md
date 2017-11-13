## Using Mimeo

Topics covered in this guide:

* [Replicating articles](#replicating-articles)
* [Syncing replicated articles](#syncing-replicated-articles)
* [Unreplicating articles](#unreplicating-articles)


### Replicating articles

You can replicate a Help Center article in one or more locations in the same Help Center, or in a branded Help Center in the same account.

1. In the **loader.json** file, specify the source article and one or more locations where you'd like to publish the copies. Example:

    ```json
    {
      "source_id": 202391318,
      "source_hc": "your_subdomain",
      "locations": [
        {
  	      "hc": "your_subdomain",
          "section_id": 36406
        },
        {
  	      "hc": "your_subdomain",
          "section_id": 200597916
        }
      ]
    }
    ```

	You must follow this JSON format, though you can add as many locations as you like. Make sure to include a comma between locations. See [Loader reference](https://github.com/chucknado/mimeo/tree/master/docs/loader-reference.md).

2. Save **loader.json**.

	**Tip**: Validate your JSON in a code editor or with an online tool like [JSON Checker](https://jsonchecker.com/).

3. In your command-line interface, navigate to the **mimeo** folder and run the following command:

    ```
    $ python3 replicate.py
    ```

The script replicates the article in the specified locations and adds a "readonly" label to each article copy. Notify writers not to make changes to any article with the label.

The script also updates a file named **global_map.json** with information about the source article and its new copies. See [Global map reference](https://github.com/chucknado/mimeo/tree/master/docs/global-map-reference.md). The machine-generated file is used to sync the content of source articles with their copies.

**Important**: Never edit the **global_map.json** file yourself. You might lose mappings and break syncing. The file is meant to be updated only by the tool.


### Syncing replicated articles

Periodically, you can sync changes made to all source articles to their copies.

In your command-line interface, navigate to the **mimeo** folder and run the following command:

```
$ python3 sync.py
```

The script checks every source article in the **global_map.json** file, comparing the last updated date of each source article against its copies. If the update date of the source is more recent than the copy, the script copies the source content to the copy, overwriting the out-of-date content.


### Unreplicating articles

You can delete one or more copies of an article from Help Center.

1. In the **unloader.json** file, specify the source article and one or more of its copies to delete. Example:

    ```json
    {
      "source_id": 202465216,
      "removal_list": [115003464654, 115003465434, 115003452073]
    }
    ```

	You can get the copy ids from the **global_map.json** file.

	You must follow this JSON format, though you can add as many copy ids as exist. See [Unloader reference](https://github.com/chucknado/mimeo/tree/master/docs/unloader-reference.md).

2. Save **unloader.json**.

	**Tip**: Validate your JSON in a code editor or with an online tool like [JSON Checker](https://jsonchecker.com/).

3. In your command-line interface, navigate to the **mimeo** folder and run the following command:

    ```
    $ python3 unreplicate.py
    ```

The script deletes the article copies. The script also updates the **global_map.json** file, removing the information about the copies that were deleted. If all the copies of a source article were removed, the source article is also removed from the global map.
