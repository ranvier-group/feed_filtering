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

We want to create various filters that trigger when transaction criteria are met.

Create a filter that can

- [ ]  Trigger of “to” is in a list of monitored strings
- [ ]  Trigger if a ”to” OR  from” is in a list of monitored strings
- [ ]  Trigger if a (”to” OR “from”) AND “input” is also matching
- [ ]  Trigger if a ((”to” OR ”from”) AND “input”) OR method_id matches. Where method id is an exact match on the third to 11th string of the input. I.e tx[”input”][2:10] == method_id