## Global map reference

**Important**: Never edit the **global_map.json** file. You might lose mappings and break syncing. The file is meant to be updated only by the tool.

The **global_map.json** file consists of a JSON object with the following properties:

| Name      | Type   | Description
| --------- | -------| -------
| source_id | number | Id of the source article in Help Center
| source_hc | string | Subdomain of the Help Center with the source article
| copies    | array  | Descriptions of where to create copies of the source article

The **copies** array consists of one or more objects with the following properties:

| Name | Type | Description
| ---- | -------| -------
| hc   | string | Subdomain of the Help Center where the copy was published
| id   | number | Id of article copy in the Help Center


### Example

**global_map.json**
```json
[
  {
    "source_hc": "acme_red",
    "source_id": "203442877",
    "title": "Jet Engine FAQ",
    "copies": [
      {
        "hc": "acme_red",
        "id": 115002890163
      },
      {
        "hc": "acme_blue",
        "id": 115002890179
      }
    ]
  },
  {
    "source_hc": "acme_red",
    "source_id": "203442812",
    "title": "Hydraulic System FAQ",
    "copies": [
      {
        "hc": "acme_red",
        "id": 115002890254
      },
      {
        "hc": "acme_green",
        "id": 115002890623
      }
    ]
  }
]
```
