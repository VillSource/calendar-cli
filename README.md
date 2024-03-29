# [NOTE] My 3td year project at kku Script Programming

# installation step

If you do not install python yet. Please install [here](https://www.python.org/)

## pip install

```bash
pip install calendar-cli-kku
```

## By package install

If you do not install Git yet. Please install [here](https://git-scm.com/)

```bash
git clone https://github.com/VillSource/calendar-cli.git
cd calendar-cli
pip install ./
```

# Guide

Calendar-cli is a commandlind aplication for a simple management.
You can use one of three command below to run script. If command have no argument, script will show you a crrent month carendar.

```bash
calendar
```

```bash
calendar-cli
```

```bash
ccal
```

![Run script](https://github.com/VillSource/calendar-cli/blob/master/document/run.gif?raw=true)

**All options in CLI**

- --add, -a
  - --event, -e
  - --date, -d
- --update, -u
  - --event, -e
  - --date, -d
  - --confirm
- --delete, -d
  - --confirm
- --list
  - --modify, -m
  - -n
- -ls
- -lm
  - --confirm
- -l

## Add data

```--add, -a``` : to add event to your calendar that require event name 
`--event=<enter your event>, -e <enter your event>` and you can add date to your event by below option.
If you do not add date to your event program will add current date. 
`--date="<yyy-mm-dd>, -d<yyy-mm-dd>` : To add date to event (Current date by default)

Full option

```bash
ccal --add --event "Happy birthday" --date 2022-01-19
```

Shot option

```bash
ccal -a -e "Happy birthday" -d 2022-01-19
```

Or you can mix shot option and full option together.

![Add data](https://github.com/VillSource/calendar-cli/blob/master/document/add.gif?raw=true)

## Update

```bash
ccal --update <oldEvent : name or ID> --date <newDate> -e <newEventName>
```

Update event Birthday Party (ID=`432`)

```bash
# Update Birthday Party date by name event
ccal --update "Birthday Party" -d 2021-01-19

# Update Birthday Party by ID event
ccal -u 432 -e "My mom birthday Party" -d 2021-05-09
```

use `--confirm` at the end for ignore all interaction.

## Delete

```bash
ccal --delete <name or ID>
```

Data in database ==> event Birthday Party (ID=`432`)

```bash
# Delete Birthday Party event by name event
ccal --delete "Birthday Party"

# Delete Birthday Party by ID event
ccal --delete 432
```

use `--confirm` at the end for ignore all interaction.

## List

`--list` : To show all events on this month.
`--modify, -m` : To secect one of list and modify data or delete.
`-n <How many month>` : To print several months.

`-ls` : To show all event on this month.
`-lm` : To secect one of list and modify data or delete
`-l<1-12>` : To show all event in <0-9> month.

Standard list in curent month

```bash
ccal --list
ccal -ls
```

Standart list in today to 10 years ahead

```bash
ccal --list -n 10 
ccal -l10
```

```bash
ccal --list --modify # You can use -m instead --modify
ccal -lm
```

## GUI option

On GUI option you can add, update, remove, and view your calendar in graphic mode.

![GUI MODE](https://github.com/VillSource/calendar-cli/blob/master/document/GUI.png?raw=true)

Enter GUI option by

```bash
ccal --start
```

or

```bash
gcal
```
