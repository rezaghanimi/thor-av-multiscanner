# Thor AV Multiscanner
Scan files to perform static analysis. This software allows to obtain information about a file, such as extracting imports, sections, hashes, etc. In addition, it allows you to analyze a file with different antivirus engines using Dockers.

## CLI


```
usage: thor.py [-h] [-d] [-s [FILE] | -l | -u]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug mode
  -s [FILE], --scan-file [FILE]
                        Scan a specific file
  -l, --list-avs        List of available antivirus engines
  -u, --update-avs      Update antivirus databases
```

### Usage examples

#### Get information from a file

```
$ python3 thor.py -i sample_files/file1.random

------------------------------
           File info          
------------------------------
Size: 16.0 KB
MD5: bb7425b82141a1c0f7d60e5106676bb1
SHA-1: 9dce39ac1bd36d877fdb0025ee88fdaff0627cdb
SHA-256: 58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47
Extension: exe
Mime: application/vnd.microsoft.portable-executable
File Type: executable


--------------------------------------------------
           Portable Executable Info (PE)          
--------------------------------------------------
Target Machine: Intel 386 or later processors and compatible processors
Compilation Timestamp: 2010-12-19 11:16:19
Entry Point: 6176

SECTIONS:

 .text:
        Virtual Address: 4096
        Virtual Size: 2416
        Raw Size: 4096
        Characteristics: 1610612768
        Entropy: 4.451
        MD5: 7e39ebe7cdeda4c636d513a0fe140ff4
        SHA-1: 150d709dcae7e0ae30ac6e5c76fda74ce168a62b
        SHA-256: 44ab4d055abe09f315f217245f131fa4b9c162ffc992034b28ada7d2e8e8c87f
 .rdata:
        Virtual Address: 8192
        Virtual Size: 690
        Raw Size: 4096
        Characteristics: 1073741888
        Entropy: 1.132
        MD5: 2de0f3a50219cb3d0dc891c4fbf6f02a
        SHA-1: 9a80eabe5c64342b6bc9f4f31212ceb37b014055
        SHA-256: c6c6d685937af139911a720a86a1d901e30d015c8bc4a0d27756141e231df5eb
 .data:
        Virtual Address: 12288
        Virtual Size: 252
        Raw Size: 4096
        Characteristics: 3221225536
        Entropy: 0.439
        MD5: f5e2ba1465f131f57b0629e96bbe107e
        SHA-1: 129de8d9c6bbe1ba01c6b0d5ce5781c61eb042dc
        SHA-256: 86aa10f4f5e696b8953e0a639a9725869803d85c1642d3e86e9fc7574d2eedb3


----------------------------
           Imports          
----------------------------
 - KERNEL32.dll
 - MSVCRT.dll
 - kerne132.dll
 - C:\windows\system32\kerne132.dll
 - Lab01-01.dll
 - C:\Windows\System32\Kernel32.dll
 ```

#### Get information from a file in JSON format

```
$ python3 thor.py -i sample_files/file1.random -j

{
   "file_info":{
      "size":{
         "size":16.0,
         "unit":"KB"
      },
      "hashes":{
         "MD5":"bb7425b82141a1c0f7d60e5106676bb1",
         "SHA-1":"9dce39ac1bd36d877fdb0025ee88fdaff0627cdb",
         "SHA-256":"58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47"
      },
      "magic_number":{
         "type":[
            "executable",
            "system"
         ],
         "extension":[
            "exe",
            "dll",
            "drv",
            "sys",
            "com"
         ],
         "mime":[
            "application/vnd.microsoft.portable-executable",
            "application/x-msdownload"
         ]
      }
   },
   "pe_info":{
      "sections":{
         ".text":{
            "virtual_address":4096,
            "virtual_size":2416,
            "raw_size":4096,
            "characteristics":1610612768,
            "hashes":{
               "MD5":"7e39ebe7cdeda4c636d513a0fe140ff4",
               "SHA-1":"150d709dcae7e0ae30ac6e5c76fda74ce168a62b",
               "SHA-256":"44ab4d055abe09f315f217245f131fa4b9c162ffc992034b28ada7d2e8e8c87f"
            },
            "entropy":4.451
         },
         ".rdata":{
            "virtual_address":8192,
            "virtual_size":690,
            "raw_size":4096,
            "characteristics":1073741888,
            "hashes":{
               "MD5":"2de0f3a50219cb3d0dc891c4fbf6f02a",
               "SHA-1":"9a80eabe5c64342b6bc9f4f31212ceb37b014055",
               "SHA-256":"c6c6d685937af139911a720a86a1d901e30d015c8bc4a0d27756141e231df5eb"
            },
            "entropy":1.132
         },
         ".data":{
            "virtual_address":12288,
            "virtual_size":252,
            "raw_size":4096,
            "characteristics":3221225536,
            "hashes":{
               "MD5":"f5e2ba1465f131f57b0629e96bbe107e",
               "SHA-1":"129de8d9c6bbe1ba01c6b0d5ce5781c61eb042dc",
               "SHA-256":"86aa10f4f5e696b8953e0a639a9725869803d85c1642d3e86e9fc7574d2eedb3"
            },
            "entropy":0.439
         }
      },
      "entry_point":6176,
      "target_machine":"Intel 386 or later processors and compatible processors",
      "compilation_timestamp":"2010-12-19 11:16:19"
   },
   "imports":[
      "KERNEL32.dll",
      "MSVCRT.dll",
      "kerne132.dll",
      "C:\\windows\\system32\\kerne132.dll",
      "Lab01-01.dll",
      "C:\\Windows\\System32\\Kernel32.dll"
   ]
}
```


## Web APP
The web application will allow you to perform the same operations as the CLI, but with a friendlier interface. As a difference, it has a cache that will avoid having to scan the same file several times.

Launch web application:

```
$ cd app; python3 index.py
```

It is possible to access from browsing using the URL: `http://127.0.0.1:5000/`.




## Configuration
This application uses a file in JSON format where the Docker commands that will be used for operations with each of the antivirus are indicated. Each object in the list represents an antivirus configured in a Docker container.

```
{
    "name":"AVG AntiVirus",
    "scan_command": "--rm -v \"{File_path}:/malware/{File_name}\" malice/avg {File_name}",
    "update_command": "malice/avg update"
}
```

The commands are parameterized, being necessary to indicate the following tokens:
* File_path: This token will be replaced by the path of the file to analyze.
* File_name: This token will be replaced by the name of the file to analyze.

### Screenshots

![Choose File](screenshots/screenshot1.png)

![File Info](screenshots/screenshot2.png)

![AV Engine Detections](screenshots/screenshot6.png)

![Portable Executable Info (PE)](screenshots/screenshot3.png)

![Imports](screenshots/screenshot4.png)

![Strings](screenshots/screenshot5.png)

## AntiVirus

## About

## Copyright
© 2020 Copyright: [javierizquierdovera.com](https://javierizquierdovera.com/).

This program is free software, you can redistribute it and/or modify it under the terms of [GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).