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

## add

```python
calendarcli.add.data( opt : list ) : None
```

`add` function required one paramiter that contain date and event name. (None return)

```python
[
    ( Data_option1, Property1 ),
    ( Data_option2, Property2 ),
]
```

|Data option |Property|
|:---:|:---|
|--event, -e|string : event name|
|--date, -d|string : date|

For example I want to add Birthday Party 2022-01-19 on database.

```python
from calendarcli import add
opt = [
    ('--event','Birthday Party'),
    ('-d','2021-01-19')
]
add.data(opt)
```

## check

isDate : to check date format

```python
calendarcli.check.isDate( date:str )
```

|Paramiter|Property|
|:---:|:---|
|date|string : include date such as `"2021-12-05"`|

|Return|Property|
|:---:|:---|
|Boolean|boolean : if `date` format match `YYYY-MM-DD` return `True`|

<!-- ## dataManager -->

## delete

To delete event from database. (None return)

```python
calendarcli.delete.find( event : any , option : list ) : None
```

|Paramiter|Property|
|:---:|:---|
|event|string :  Event name<br/>integer : Event ID|
|option|list : `[ ("--confirm", "") ]` to confirm deletion.<br/>list : `[ ]` to not confirm deletion|

For example I want to delete Birthday Party 2022-01-19 (ID=1) on database.

```python
from calendarcli import delet
confirmation = [ ("--confirm", "") ]

# To delete by event name
delet.find("Birthday Party",confirmation)

# To delete by ID
delet.find(432,confirmation)
```

<!-- ## help -->

<!-- ## icalendar -->

<!-- ## list -->

<!-- ## path -->

## update

`update` function will update `event` with new data in `opt` (None return)

```python
calendarcli.update.data( event : any, opt : list ) : None
```

|Paramiter|Property|
|:---:|:---|
|event|string :  Event name<br/>integer : Event ID|
|opt|list : list of new data to update.|

Structur of `opt`

```python
[
    ( Data_option1, Property1 ),
    ( Data_option2, Property2 ),
]
```

|Data option |Property|
|:---:|:---|
|--event, -e|string : event name|
|--date, -d|string : date|

For example I want to update Birthday Party 2022-01-19 on database.

```python
from calendarcli import update
opt = [
    ('-d','2050-01-19'),
    ('--confirm', '')           # To confirm updating.
]
add.data("Birthday Party",opt)  # Update by old event name
add.data(432,opt)               # Update by ID event
```
