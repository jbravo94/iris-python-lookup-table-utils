# IRIS Python Lookup Table Utils (pylotaut)

## Introduction

The IRIS Python Lookup Table Utils module provides a simple API to interact with the lookup tables in Intersystems IRIS from python.
Furthermore it offers the capability to import Excel sheets which is useful for project implementation and migration.

Click on the screenshot below to view the demo video:
[![Screenshot](Screenshot.png?raw=true "Screenshot")](https://youtu.be/-oyRiVOLU2c "IRIS Python Lookup Table Utils")

## Prerequisites
* Docker with included Docker Compose

## Tested Versions
* Docker `26.1.1`
* Docker Compose `v2.27.0`
* Docker Image `intersystemsdc/iris-community:2023.1.4.580.0-zpm`

## Installation

1. Build image `docker compose build`
2. Start container `docker compose up -d`
3. Open URL http://localhost:52795/csp/irisapp/EnsPortal.LookupSettings.zen
4. Login with default credentials `Admin` and `SYS` and change password
5. Enter iris shell `docker compose exec iris bash`
6. Open python shell `irispython`
7. Import module `from pylotaut import pylotaut`
8. Run commands `pylotaut.<FUNCTION>` documented in next chapter

### Example: Load xls sheet from irispython shell

1. Open python shell and import module a describe previously
2. Load items from example xls via `name, table = pylotaut.load_xlsx("/irisdev/app/example_lookup_table.xlsx")`
3. Import table via `pylotaut.create_lookuptable(name, table)`
4. Print table contents via `pylotaut.print_table(name)` or review them in the UI under http://localhost:52795/csp/irisapp/EnsPortal.LookupSettings.zen

## API functions

All API functions accept or return python objects e.g. strings, dictionaries or tuples. 

### Get actions
* `get_value(table, key)`
* `get_tables()`
* `load_xlsx(path)`
* `load_table(table_name)`

### Set actions
* `set_value(table, key, value)`
* `create_lookuptable(table_name, items)`

### Delete actions
* `delete_key(table_name, key)`
* `delete_table(table_name)`

### Print actions
* `list_tables()`
* `print_value(table, key)`
* `print_table(table_name)`
