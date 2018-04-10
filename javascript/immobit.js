/*
  immobit.js - ImmoBit API library.

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
    * his.js
*/
"use strict";

/*
  ImmoBit core namespace.
*/
var immobit = immobit || {};

immobit.BASE_URL = 'https://backend.immobit.de'


/*
  Returns the respective endpoint URL.
*/
immobit.getUrl = function (endpoint) {
  if (endpoint != null) {
    return immobit.BASE_URL += '/' + endpoint;
  }

  return immobit.BASE_URL;
}
