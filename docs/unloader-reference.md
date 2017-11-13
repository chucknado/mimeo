## Unloader reference

The **unloader.json** file consists of a JSON object with the following properties:

| Name         | Type   | Description
| ------------ | -------| -------
| source_id    | number | Id of the source article in Help Center
| removal_list | array  | Ids of the copies in Help Center to remove

### Example

**unloader.json**
```json
{
  "source_id": 202465216,
  "removal_list": [115003464654, 115003465434, 115003452073]
}
```
