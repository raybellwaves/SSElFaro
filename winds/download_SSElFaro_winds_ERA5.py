# conda activate ERA5
from ecmwfapi import ECMWFDataServer
 
server = ECMWFDataServer()
server.retrieve({
    "class": "ea",
    "dataset": "era5",
    "expver": "1",
    "stream": "oper",
    "type": "an",
    "levtype": "sfc",
    "param": "165.128/166.128",
    "date": "2015-09-29/to/2015-10-03",
    "time": "00/01/02/03/04/05/06/07/08/09/10/11/12/13/14/15/16/17/18/19/20/21/22/23",
    "step": "0",
    "grid": "0.25/0.25",
    "area": "30.5/-81.5/18/-65.5",
    "format": "netcdf",
    "target": "/projects/rsmas/kirtman/rxb826/DATA/ERA5/SSElFaro.nc"
 })
