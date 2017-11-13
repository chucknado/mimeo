## Loader reference

The **loader.json** file consists of a JSON object with the following properties:

| Name      | Type   | Description
| --------- | -------| -------
| source_id | number | Id of the source article in Help Center
| source_hc | string | Subdomain of the Help Center with the source article
| locations | array  | Descriptions of where to place copies of the source article

The **locations** array consists of one or more objects with the following properties:

| Name       | Type | Description
| ---------- | -------| -------
| hc         | string | Subdomain of the Help Center where the copy should be placed
| section_id | number | Id of a section in the Help Center where the copy should be placed
	
### Example

**loader.json**
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
