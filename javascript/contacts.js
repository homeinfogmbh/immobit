/*
  contacts.js - ImmoBit contacts library.

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
"use strict";

/*
  ImmoBit core namespace.
*/
var immobit = immobit || {};


/*
  Contacts namespace.
*/
immobit.contacts = immobit.contacts || {};


/*
  Returns the respective endpoint URL.
*/
immobit.contacts.getUrl = function (endpoint) {
  var url = immobit.getUrl('contacts');

  if (endpoint != null) {
    return url += '/' + endpoint;
  }

  return url;
}


/*
  Lists the respective contacts.
*/
immobit.contacts.list = function (args) {
  var url = immobit.contacts.getUrl();
  return his.auth.get(url, args);
}
