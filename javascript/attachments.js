/*
  attachments.js - ImmoBit attachments library.

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
  Attachments namespace.
*/
immobit.attachments = immobit.attachments || {};


/*
  Returns the respective endpoint URL.
*/
immobit.attachments.getUrl = function (endpoint) {
    const url = immobit.getUrl('attachments');

    if (endpoint != null) {
        return url + '/' + endpoint;
    }

    return url;
};


/*
  Gets the respective attachment.
*/
immobit.attachments.get = function (id, args) {
    const url = immobit.attachments.getUrl(id);
    return his.get(url, args);
};


/*
  Adds the provided attachment.
*/
immobit.attachments.add = function (data, args) {
    const url = immobit.attachments.getUrl();
    return his.post(url, data, args);
};


/*
  Patches the respective attachment.
*/
immobit.attachments.patch = function (id, data, args) {
    const url = immobit.attachments.getUrl(id);
    return his.patch(url, data, args);
};


/*
  Replaces the respective attachment.
*/
immobit.attachments.put = function (id, data, args) {
    const url = immobit.attachments.getUrl(id);
    return his.put(url, data, args);
};


/*
  Deletes the respective attachment.
*/
immobit.attachments.delete = function (id, args) {
    const url = immobit.attachments.getUrl(id);
    return his.delete(url, args);
};
