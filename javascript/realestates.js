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
    * diff.js
*/
'use strict';

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
    const url = immobit.getUrl('realestates');

    if (endpoint != null) {
        return url + '/' + endpoint;
    }

    return url;
};


/*
  Lists the respective real estates.
*/
immobit.realEstates.list = function (args) {
    const url = immobit.realEstates.getUrl();
    return his.get(url, args);
};


/*
  Gets the respective real estate.
*/
immobit.realEstates.get = function (id, args) {
    const url = immobit.realEstates.getUrl(id);
    return his.get(url, args);
};


/*
  Adds the provided real estate.
*/
immobit.realEstates.add = function (realEstate, args) {
    const url = immobit.realEstates.getUrl();
    const data = JSON.stringify(realEstate);
    return his.post(url, data, args);
};


/*
  Deletes the respective real estate.
*/
immobit.realEstates.delete = function (id, args) {
    const url = immobit.realEstates.getUrl(id);
    return his.delete(url, args);
};


/*
  Patches the respective real estate.
*/
immobit.realEstates.patch = function (id, realEstatePatch, args) {
    const url = immobit.realEstates.getUrl(id);
    const data = JSON.stringify(realEstatePatch);
    return his.patch(url, data, args);
};


/*
  ImmoBit real estate class.
*/
immobit.realEstates.RealEstate = class {
    constructor (json) {
        for (var prop in json) {
            if (json.hasOwnProperty(prop)) {
                this[prop] = json[prop];
            }
        }
    }

    diff (other) {
        return immobit.diff.resolve(this, other);
    }

    toString () {
        return JSON.stringify(this);
    }
};


/*
  Constructor class method.
*/
immobit.realEstates.RealEstate.fromString = function (str) {
    return new immobit.realEstates.RealEstate(JSON.parse(str));
};
