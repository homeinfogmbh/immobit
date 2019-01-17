/*
  immobit.js - ImmoBit difference resolving library.

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
*/
'use strict';

/*
  ImmoBit core namespace.
*/
var immobit = immobit || {};


/*
  Diff module.
*/
immobit.diff = immobit.diff || {};


/*
  Determines whether the respective object is a JSON object.
*/
immobit.diff.isObject = function (obj) {
    return typeof obj == 'object' && ! Array.isArray(obj);
};


/*
  Resolves simple type values.
*/
immobit.diff.resolve = function (old, new_) {
    if (new_ === undefined || old === new_) {
        return undefined;
    }

    if (new_ === null) {
        return null;
    }

    const bothObjects = immobit.diff.isObject(old) && immobit.diff.isObject(new_);

    if (! bothObjects) {
        return new_;
    }

    const resolved = {};
    const properties  = [];
    let prop;

    for (prop in old) {
        if (old.hasOwnProperty(prop)) {
            properties.push(prop);
        }
    }

    for (prop in new_) {
        if (new_.hasOwnProperty(prop)) {
            if (properties.includes(prop)) {    // Skip duplicates.
                continue;
            }

            properties.push(prop);
        }
    }

    for (prop of properties) {
        let oldVal = undefined;
        let newVal = undefined;

        if (old.hasOwnProperty(prop)) {
            oldVal = old[prop];
        }

        if (new_.hasOwnProperty(prop)) {
            newVal = new_[prop];
        }

        resolved[prop] = immobit.diff.resolve(oldVal, newVal);
    }

    // Test if resolved object is empty.
    let empty = true;

    for (prop in resolved) {
        if (resolved.hasOwnProperty(prop)) {
            if (resolved[prop] !== undefined) {
                empty = false;
                break;
            }
        }
    }

    if (empty) {
        return null;
    }

    return resolved;
};
