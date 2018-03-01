/*
  realesates.js - ImmoBit real estates library.

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
  Real estates namespace.
*/
immobit.realEstates = immobit.realEstates || {};


/*
  Returns the respective endpoint URL.
*/
immobit.realEstates.getUrl = function (endpoint) {
  var url = immobit.getUrl('realestates');

  if (endpoint != null) {
    return url += '/' + endpoint;
  }

  return url;
}


/*
  Lists the respective real estates.
*/
immobit.realEstates.list = function (args) {
  var url = immobit.realEstates.getUrl();
  return his.auth.get(url, args);
}


/*
  Gets the respective real estate.
*/
immobit.realEstates.get = function (id, args) {
  var url = immobit.realEstates.getUrl(id);
  return his.auth.get(url, args);
}


/*
  Adds the provided real estate.
*/
immobit.realEstates.add = function (realEstate, args) {
  var url = immobit.realEstates.getUrl();
  var data = JSON.stringify(realEstate);
  return his.auth.post(url, data, args);
}


/*
  Deletes the respective real estate.
*/
immobit.realEstates.delete = function (id, args) {
  var url = immobit.realEstates.getUrl(id);
  return his.auth.delete(url, args);
}


/*
  Patches the respective real estate.
*/
immobit.realEstates.patch = function (id, realEstatePatch, args) {
  var url = immobit.realEstates.getUrl(id);
  var data = JSON.stringify(realEstatePatch);
  return his.auth.patch(url, data, args);
}
