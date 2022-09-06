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

## Another Option

Using sagic creates file or files of different sites on different elements. But there is another
option of create a single site per eac command.
Instead of using `sagic` script, you can do like so:

```
$ python datafile/cli_hooks.py
```

This will ask for the destination point code, the LAI (GCI or SAI). Then create the aproprate cell site accordingly.
