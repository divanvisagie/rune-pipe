# rune-pipe
A python project to clean up [RUNDATA](https://www.nordiska.uu.se/forskn/samnord.htm). The purpose is to make the data more usable for computational study.

![rune-pipe logo](docs/images/logo.png)



According to the rundata [documentation](http://www.rattsatt.com/rundata/mac/bskr_rdm.pdf).


|File Name|Description                            |
|---------|---------------------------------------|
|FVN      |Old west norse                         |
|FVNX     |Old west norse in a searchable format  |
|FORNSPR  |Ancient language                       |
|FORNSPRX |Ancient language in a searchable format|
|RUNTEXT  |Transliterated rune text               |
|RUNTEXTX |Rune text in a searchable format         |


## Rundata excel file

|Column name    |English mapping|Description|
|---------------|---------------|-----------|
|Stilgruppering |Style Grouping | Refers to the [styles](https://en.wikipedia.org/wiki/Runestone_styles) |
|Period/Datering|Dating         | Rough dating of the enscription (u. = Proto-Nordic, v. = Viking Age, m. = Medieval).


## Understanding the Codes/Signum

Rundata uses Codes they call Signum to identify runic enscriptions, these have a certain logic to them

Sometimes the codes can contain the following meaningful signs:

|Sign|Meaning|
|---|---|
|†|The inscription has disappeared|
|$|New reading or interpretation that has been supplemented from another source|
|M|The inscription is medeival|
|U|The inscription is in Old Norse|
|No M or U| The inscription is Viking age|