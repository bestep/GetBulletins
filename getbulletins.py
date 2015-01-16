#!/usr/local/bin/python3

"""
Created by William Estep
Copyright (c) 2015 William Estep

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import pycurl


def setVariables():
    # Update the url variable to the valid path of the SSCA Bulletins
    url = 'http://google.com'
    return url


def checkfile(filename):
    # try to open the file. If it exists, skip, if not download
    getfile = False
    try:
        my_file = open(filename)
    except IOError as e:
        getfile = True
        return getfile
    return getfile


def getTheFile(filename):
    tempurl = setVariables()
    url = '{}{}'.format(tempurl, filename)
    print('url: {}'.format(url))
    fp = open(filename, 'wb')
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, fp)
    try:
        result = c.perform()
    except pycurl.error as error:
        print('curl error: {}'.format(error))
        c.close()
        return
    fp.close()


def main():

    # Create year list
    for year in range(3, 16, 1):
        for month in range(1, 13, 1):
            # add break point of 1502
            if year == 15 and month == 2:
                print('We are done')
                break
            filename = 'ssca{:0>2}{:0>2}.pdf'.format(year, month)
            if checkfile(filename):
                print('Getting file {}'.format(filename))
                getTheFile(filename)
            else:
                print('file exists')

if __name__ == "__main__":
    main()
