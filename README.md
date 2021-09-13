
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

# Manual

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

![Run script](/document/run.gif)

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

![Add data](/document/add.gif)

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
