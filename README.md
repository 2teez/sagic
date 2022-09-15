# sagic

## Name

`sagic` -- A python cli program use by NSS - (Network SubSystem) Engineers to create script which are used
for adding cell sites namely 2G, 3G and 4G on the network.

## To Use:

From the CLI, clone this repo [sagic](https://github.com/2teez/sagic).
Then change into the sagic directory and then run:

```
$ python sagic.py
```

## OR

```
$ python ./sagic.py
```
Where `$` is the shell prompt, which might be different in your own prompt.

### Important _NOTE_

**Datafiles.txt** must be in the same directory with ```sagic``` file for the above command to work.
You specify the data for configuration like so

```
Network Elements<space>Location Area Code<space>Cell Site Name_Sector Number<space>Cell Site Number
```
E.g.

```HENU_RNC5	3060	ENU024B_S1	11811```

## Another Option

Using sagic creates file or files of different sites on different elements. But there is another
option of create a single site per eac command.
Instead of using `sagic` script, you can do like so:

```
$ python datafile/cli_hooks.py
```

This will ask for the destination point code, the LAI (GCI or SAI). Then create the aproprate cell site accordingly.

### TODO

I intend to call, `cli_hooks` file from the main module file and activate this module using a CLI switch.

*Like so: `S python ./sagic.py --oneline`*
