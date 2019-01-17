/*
  immobit.js - ImmoBit document object model library.

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
    * diff.js
*/
'use strict';

/*
  ImmoBit core namespace.
*/
var immobit = immobit || {};


/*
  DOM module.
*/
immobit.dom = immobit.dom || {};


immobit.dom.addContent = function (element, content) {
    if (content != null) {
        if (Array.isArray(content)) {
            for (let item of content) {
                element.appendChild(item);
            }
        } else {
            element.appendChild(content);
        }
    }
};


immobit.dom.ListElementButton = function (content, class_, style) {
    const button = document.createElement('button');
    immobit.dom.addContent(button, content);

    if (class_ != null) {
        button.setAttribute('class', class_);
    }

    if (style != null) {
        button.setAttribute('style', style);
    }
};


immobit.dom.ListElementColumn = function (index, content, class_, width, style) {
    const column = document.createElement('td');
    column.setAttribute('data-id', index);
    immobit.dom.addContent(column, content);

    if (class_ != null) {
        column.setAttribute('class', class_);
    }

    if (width != null) {
        column.setAttribute('width', width);
    }

    if (style != null) {
        column.setAttribute('style', style);
    }

    return column;
};


/*
  Real estate list element DOM.
*/
immobit.dom.ListElement = function (index) {
    const row = document.createElement('tr');
    const div = document.createElement('div');
    div.setAttribute('class', 'input-group');

    // TODO: implement.
    return row;
};

/*
<tr>\
				<div class="input-group">\
					<td class="markrealestate" style="white-space: nowrap;" data-id="' + i + '">\
						<button type="button" class="btn btn-default markfirst" style="min-width:50px; text-align:center; border-radius:0; pointer-events:none">' + (i+1) + '</button>\
					</td>\
					<td class="markrealestate" width="20%" data-id="' + i + '">\
						<button type="button" class="btn btn-default markgroup" style="width:100%; text-align:left; border-radius:0; pointer-events:none">' + msg[i].verwaltung_techn.objektnr_extern + '</button>\
					</td>\
					<td class="markrealestate" width="15%" data-id="' + i + '">\
						<button type="button" class="btn btn-default markgroup" style="width:100%; text-align:left; border-radius:0; pointer-events:none">' + objektart + '</button>\
					</td>\
					<td class="markrealestate" width="15%" data-id="' + i + '">\
						<button type="button" class="btn btn-default markgroup" style="width:100%; text-align:left; border-radius:0; pointer-events:none">' + vermarktungsart + '</button>\
					</td>\
					<td class="markrealestate" width="99%" data-id="' + i + '">\
						<button type="button" class="btn btn-default markgroup" style="width:100%; text-align:left; border-radius:0; pointer-events:none">' + msg[i].geo.strasse + ' ' + ((msg[i].geo.hausnummer != undefined && msg[i].geo.hausnummer != null) ?msg[i].geo.hausnummer :"") + ' ' + msg[i].geo.plz + ' ' + msg[i].geo.ort + '</button>\
					</td>\
					<td class="markrealestate" width="15%" data-id="' + i + '">\
						<button type="button" class="btn btn-default markgroup" style="width:100%; text-align:left; border-radius:0; pointer-events:none">' + msg[i].verwaltung_techn.stand_vom + '</button>\
					</td>\
					<td style="white-space: nowrap;">\
					<button type="button" class="btn btn-default btn_preview_manage" title="Vorschau öffnen" data-id="' + i + '" data-preview="true" style="margin-left:5px; margin-right:0px; border-radius:0;"><i class="fa fa-eye"></i></button>\
						<button type="button" class="btn btn-success btn_manage" title="Immobilie bearbeiten" data-id="' + i + '" style="margin-left:0px; margin-right:0px; border-radius:0; width:100px;"><i class="fa fa-pencil"></i></button>\
						<button type="button" class="btn btn-default btn_clone_object" data-placement="top" title="Immobilie duplizieren" data-id="' + i + '" data-sorting="' + sorting + '" data-reverse="' + reverse + '" style="margin-left:0px; margin-right:0px; border-radius:0;"><i class="fa fa-files-o"></i></button>\
						<button type="button" class="btn btn-danger btn_delete_object" data-id="' + i + '" data-sorting="' + sorting + '" data-reverse="' + reverse + '" data-toggle="modal" data-placement="top" title="Immobilie löschen" style="margin-left:0px; margin-right:0px; border-radius:0;"><span class="fa fa-trash"></span></button>\
					</td>\
					<td style="white-space: nowrap; padding-left:5px">' + customerPortals + '</td>\
				</div>\
			</tr>'
*/
