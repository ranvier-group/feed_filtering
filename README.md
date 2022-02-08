# Feed Filtering

Given a stream of transactions received and serialized to JSON like:

```python
{
  "to": "",  # 32-character string starting with "0x"
  "from": "",  # 32-character string starting with "0x"
  "input": "",  # arbitrary length string, min "0x"
  ...
}
```

Create a filter that takes in user specified paramters of one or more `to`, `from`, `input` and `method_id` to monitor.

Should be able to parse IF, AND, OR conditions and return bool if matching for the following cases

- [ ]  ”to” OR  "from” are in supplied parameters
- [ ]  if (”to” OR “from”) AND “input” are all in supplied parameters
- [ ]  if ((”to” OR ”from”) AND “input”) OR method_id matches. Where method id is an exact match on the third to 11th string of the input. I.e tx[”input”][2:10] == method_id
