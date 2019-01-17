/*
  portals.js - ImmoBit portals library.

  (C) 2017 HOMEINFO - Digitale Informationssysteme GmbH

  This library is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this library.  If not, see <http://www.gnu.org/licenses/>.

  Maintainer: Richard Neumann <r dot neumann at homeinfo period de>

  Requires:
    * immobit.js
*/
'use strict';

/*
  ImmoBit core namespace.
*/
var immobit = immobit || {};


/*
  Portals namespace.
*/
immobit.portals = immobit.portals || {};


/*
  Returns the respective endpoint URL.
*/
immobit.portals.getUrl = function (endpoint) {
    const url = immobit.getUrl('portals');

    if (endpoint != null) {
        return url + '/' + endpoint;
    }

    return url;
};


/*
  Lists the respective portals.
*/
immobit.portals.list = function (args) {
    const url = immobit.portals.getUrl();
    return his.get(url, args);
};
