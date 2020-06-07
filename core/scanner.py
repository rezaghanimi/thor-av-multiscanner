# /usr/bin/python3

# Copyright (C) 2020
# Created by Javier Izquierdo Vera. <javierizquierdovera.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import asyncio
import subprocess
import ntpath
from core.utils import path_leaf, exec

async def scan_file_async(file_path, loop):
    file_name = path_leaf(file_path)
    results = []
    results.append(loop.create_task(scan_file_with_avg(file_path, file_name)))
    await asyncio.wait(results)
    print(results)

async def scan_file_with_avg(file_path, file_name):
    command = 'docker run --rm -v "{0}:/malware/malware.exe" malice/avg {1}'.format(file_path, file_name)
    return await exec(command)