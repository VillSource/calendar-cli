# Module Reference

In calendarcli package

```python
import calendarcli
```

All module in calendarcli

- [calendarcli.add](#add)
- [calendarcli.check](#check)
- [calendarcli.dataManager](#dataManager)
- [calendarcli.delete](#delete)
- [calendarcli.help](#help)
- [calendarcli.icalendar](#icalendar)
- [calendarcli.list](#list)
- [calendarcli.path](#path)
- [calendarcli.update](#update)

# add

___opt___ is the list that contained the options

|option||
|:---:|:---|
|--event, -e|event name|
|--date, -d|date|

For example I want to add Birthday Party 2022-01-19 on the list

```python
opt = [
    ('--event','Birthday Party'),
    ('-d','2021-01-19')
]
```

To add data `opt:list` to database

```python
calendarcli.add.data( opt : list ) : None
```

# check

isDate : to check date format

```python
calendarcli.check.isDate( date:str )
```

|Paramiter||
|:---:|:---|
|date|string : include date such as `"2021-12-05"`|

|Return||
|:---:|:---|
|Boolean|boolean : if `date` format match `YYYY-MM-DD` return `True`|

<!-- ## dataManager -->

<!-- ## delete -->

<!-- ## help -->

<!-- ## icalendar -->

<!-- ## list -->

<!-- ## path -->

<!-- ## update -->
