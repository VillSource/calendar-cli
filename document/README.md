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

## dataManager

### selectTableOnMounth

To get all event in month.

```python
calendarcli.dataManager.selectTableOnMounth(curDate : string):
```

|Paramiter|Property|
|:---:|:---|
|curDate|string : Date formath `YYYY-MM-MM`|

|Return|Property|
|:---:|:---|
|list|list : List of event in muonth of `curDate`|

For example I want to get all event in 2021-09-01 (in year 2021 month 9)

```python
from calendarcli.dataManager import selectTableOnMounth
event = selectTableOnMounth("2021-09-01")
```

### selectTableOrderByDate

To get all event in database.

```python
calendarcli.dataManager.selectTableOrderByDate(limit : intager):
```

|Paramiter|Property|
|:---:|:---|
|limit|intager : Limited amount required number|

|Return|Property|
|:---:|:---|
|list|list : List of event in database|

For example I want to get all event database

```python
from calendarcli.dataManager import selectTableOrderByDate
event = selectTableOrderByDate()                # All event in database
evenFirst10list = selectTableOrderByDate(10)    # First 10 list in database order by date
```

### searchID and searchEvent

To get event detail.

```python
calendarcli.dataManager.searchID(id : intager): list
calendarcli.dataManager.searchEvent(event : string): list
```

|Paramiter|Property|
|:---:|:---|
|id|intager : Event id to serch.|
|event|string : Event name to search.|

|Return|Property|
|:---:|:---|
|list|list : List of event whish match wit id=`id` or event_name=`event`|

For example I want to search where "Birthday Party" is?, where id is 432?

```python
from calendarcli.dataManager import searchID,searchEvent
event  = searchID(432)                     # Search where "Birthday Party" is?
event2 = searchEvent("Birthday Party")     # Search where id is 432?
```

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
