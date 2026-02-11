# lua2py

I needed a working module to read and write lua tables to data files.

Base this a bit on JSON.
With:
* loads( str ) -> str
* load( fp ) -> str (reads from fp)
* dumps( str ) -> str
* dump( str, fp )  Writes to fp