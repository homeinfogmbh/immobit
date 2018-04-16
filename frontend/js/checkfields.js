function checkData() {
	var done = true;
	//var allowedsigns = new RegExp('[^0-9a-zA-Z äÄöÖüÜ/.+:_\-]');
	if ($("#base_objectnumber").val().trim() == ""/* || $("#base_objectnumber").val().search(allowedsigns) > 0*/) {
		done = false;
		$('#base_objectnumber').addClass('erroneous-input');
	} else
		$('#base_objectnumber').removeClass('erroneous-input');

	if ($("#base_street").val().trim() == "") {
		done = false;
		$('#base_street').addClass('erroneous-input');
	} else
		$('#base_street').removeClass('erroneous-input');
	if ($("#base_plz").val().trim() == "" || !isNumber($("#base_plz").val().replace(",", "."))) {
		done = false;
		$('#base_plz').addClass('erroneous-input');
	} else
		$('#base_plz').removeClass('erroneous-input');
	if ($("#base_location").val().trim() == "") {
		done = false;
		$('#base_location').addClass('erroneous-input');
	} else
		$('#base_location').removeClass('erroneous-input');

	// PRICES
	var prices_are_complete = true;
	if ($("#prices_rent_div").attr('style') != "display: none;") { // Just check if not visible
		if ($("#prices_netto").val().trim() == "" || !isNumber($("#prices_netto").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_netto').addClass('erroneous-input');
		} else {
			$("#prices_html").removeClass('erroneous-tab');
			$('#prices_netto').removeClass('erroneous-input');
		}
		if ($("#prices_service_charge").val().trim() != "" && !isNumber($("#prices_service_charge").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_service_charge').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_service_charge').removeClass('erroneous-input');
		}
		/*
		if (!isNumber($("#prices_cold").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_cold').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_cold').removeClass('erroneous-input');
		}
		if (!isNumber($("#prices_warm").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_warm').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_warm').removeClass('erroneous-input');
		}
		*/
		if (!isNumber($("#prices_additional").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_additional').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_additional').removeClass('erroneous-input');
		}
		/*
		if (!isNumber($("#prices_business_netto").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_business_netto').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_business_netto').removeClass('erroneous-input');
		}
		*/
		if (!isNumber($("#prices_caution").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_caution').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_caution').removeClass('erroneous-input');
		}
		if ($('input[name=prices_heatingcosts_show]:checked').val() == "false" && ($("#prices_heatingcosts").val().trim() == "" || !isNumber($("#prices_heatingcosts").val().replace(",", ".")))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_heatingcosts').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_heatingcosts').removeClass('erroneous-input');
		}
		/*
		if (!isNumber($("#prices_total").val().replace(",", "."))) {
			done = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_total').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_total').removeClass('erroneous-input');
		}
		*/
	}

	if ($("#prices_buy_div").attr('style') != "display: none;") {
		if ($("#prices_buy").val().trim() == "" || !isNumber($("#prices_buy").val().replace(",", "."))) {
			done = false;
			prices_are_complete = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_buy').addClass('erroneous-input');
		} else {
			$("#prices_html").removeClass('erroneous-tab');
			$('#prices_buy').removeClass('erroneous-input');
		}

		if ($("#prices_provision").val().trim() == "" && $("#prices_provision_onoff").is(':checked')) {
			done = false;
			$("#prices_html").addClass('erroneous-tab');
			$('#prices_provision').addClass('erroneous-input');
		} else {
			if (prices_are_complete)
				$("#prices_html").removeClass('erroneous-tab');
			$('#prices_provision').removeClass('erroneous-input');

		}
	}

	// AREAS
	var areas_are_complete = true;
	if ($("#areas_apart_div").attr('style') != "display: none;") {
		if ($("#areas_living").val().trim() == "" || !isNumber($("#areas_base").val().replace(",", "."))) {
			done = false;
			areas_are_complete = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#areas_living').addClass('erroneous-input');
		} else {
			$("#areas_html").removeClass('erroneous-tab');
			$('#areas_living').removeClass('erroneous-input');
		}
	}
	if ($("#areas_base_div").attr('style') != "display: none;") {
		if ($("#areas_base").val().trim() == "" || !isNumber($("#areas_base").val().replace(",", "."))) {
			done = false;
			areas_are_complete = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#areas_base').addClass('erroneous-input');
		} else {
			if (areas_are_complete)
				$("#areas_html").removeClass('erroneous-tab');
			$('#areas_base').removeClass('erroneous-input');
		}
	}
	if ($("#areas_floor_div").attr('style') != "display: none;") {
		if (!isNumber($("#description_floor").val())) {
			done = false;
			areas_are_complete = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#description_floor').addClass('erroneous-input');
		} else {
			if (areas_are_complete)
				$("#areas_html").removeClass('erroneous-tab');
			$('#description_floor').removeClass('erroneous-input');
		}
	}
	if ($("#areas_use_complete_rooms_div").attr('style') != "display: none;") {
		if ($("#areas_rooms").val().trim() == "" || !isNumber($("#areas_rooms").val().replace(",", "."))) {
			done = false;
			areas_are_complete = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#areas_rooms').addClass('erroneous-input');
		} else {
			if (areas_are_complete)
				$("#areas_html").removeClass('erroneous-tab');
			$('#areas_rooms').removeClass('erroneous-input');
		}
		if (!isNumber($("#areas_use").val().replace(",", "."))) {
			done = false;
			areas_are_complete = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#areas_use').addClass('erroneous-input');
		} else {
			if (areas_are_complete)
				$("#areas_html").removeClass('erroneous-tab');
			$('#areas_use').removeClass('erroneous-input');
		}
		if (!isNumber($("#areas_total").val().replace(",", "."))) {
			done = false;
			$("#areas_html").addClass('erroneous-tab');
			$('#areas_total').addClass('erroneous-input');
		} else {
			if (areas_are_complete)
				$("#areas_html").removeClass('erroneous-tab');
			$('#areas_total').removeClass('erroneous-input');
		}
	}

	// Contacts
	var contacts_are_complete = true;
	if ($("#contact").attr('style') != "display: none;") {
		if ($("#contact_familyname").val().trim() == "") {
			done = false;
			contacts_are_complete = false;
			$("#contact_html").addClass('erroneous-tab');
			$('#contact_familyname').addClass('erroneous-input');
		} else {
			$("#contact_html").removeClass('erroneous-tab');
			$('#contact_familyname').removeClass('erroneous-input');
		}
		if ($("#contact_email").val().trim() == "" && $("#contact_phone").val().trim() == "") {
			done = false;
			$("#contact_html").addClass('erroneous-tab');
			$('#contact_email').addClass('erroneous-input');
		} else {
			if (contacts_are_complete)
				$("#contact_html").removeClass('erroneous-tab');
			$('#contact_email').removeClass('erroneous-input');
		}
	}
	return done;
}

function isNumber(number) {
	return ! isNaN(Number(number));
}

function hasChanged(check, path, savedKey, newKey, count = 0) {
	try {
		if (check) {
			var pathArray = path.split(".");
			var completePath = _openImmo_json;
			for (var i = 0; i < pathArray.length; i++) {
				if (!completePath.hasOwnProperty(pathArray[i]) && newKey == null)
					return false;
				completePath = completePath[pathArray[i]];
			}
			if ($.isArray(completePath)) {
				if (completePath[count][savedKey] == newKey)
					return false;
			} else if (completePath[savedKey] == newKey)
				return false;
		}
	} catch(err) {
		//console.log("catched " + err);
	}
	return true;
}
// Checks if the key has any value from the database
function isNull(path) {
	try {
		var pathArray = path.split(".");
		var completePath = _openImmo_json;
		for (var i = 0; i < pathArray.length; i++) {
			if (completePath.hasOwnProperty(pathArray[i]))
				completePath = completePath[pathArray[i]];
			else
				return true;
		}
	} catch(err) {
		//console.log("catched " + err);
	}
	return false;
}
function showRealEstateBySearch(realEstate) {
	try {
		if ($('#searchfield').val().trim() == '')
			return true;
		else if (realEstate.verwaltung_techn.objektnr_extern.toString().toLowerCase().indexOf($('#searchfield').val().toLowerCase()) != -1)
			return true;
		else if (realEstate.geo.strasse.toString().toLowerCase().indexOf($('#searchfield').val().toLowerCase()) != -1)
			return true;
		else if (Object.keys(realEstate.objektkategorie.objektart)[0].toString().indexOf($('#searchfield').val().toLowerCase()) != -1)
			return true;
	} catch (e) {	}
	return false;
}
function showRealEstateBySelection(realEstate) {
	try {
		for (var positivcounter = 0; positivcounter < realEstate.verwaltung_techn.weitergabe_positiv.length; positivcounter++) {
			if (realEstate.verwaltung_techn.weitergabe_positiv[positivcounter] === 'immobrowse')
				return true;
			else if (realEstate.verwaltung_techn.weitergabe_positiv[positivcounter] === 'immoscout24')
				return true;
			else if (realEstate.verwaltung_techn.weitergabe_positiv[positivcounter] === 'immowelt')
				return true;
			else if (realEstate.verwaltung_techn.weitergabe_positiv[positivcounter] === 'hba')
				return true;
			else if (realEstate.verwaltung_techn.weitergabe_positiv[positivcounter] === 'breba')
				return true;
		}
	} catch (e) {	}
	return false;
}

function sortBy(path, reverse) {
    return function (a, b) {
		try {
			var sortStatus = 0;
			var pathArray = path.split(".");
			var completePathA = a;
			var completePathB = b;
			for (var i = 0; i < pathArray.length; i++) {
				completePathA = completePathA[pathArray[i]];
				completePathB = completePathB[pathArray[i]];
			}

			if (typeof completePathA === "object") {
				if (jQuery.isEmptyObject(completePathA))
					completePathA = "unbekannt";
				else
					completePathA = Object.keys(completePathA)[0];
			}

			if (typeof completePathB === "object") {
				if (jQuery.isEmptyObject(completePathB))
					completePathB = "unbekannt";
				else
					completePathB = Object.keys(completePathB)[0];
			}
			//console.log(completePathA + " // " + completePathB);
			if (completePathA.toString().toLowerCase() > completePathB.toString().toLowerCase()) {
				sortStatus = (reverse) ?1 :-1;
			} else if (completePathA.toString().toLowerCase() < completePathB.toString().toLowerCase()) {
				sortStatus = (reverse) ?-1 :1;
			}
		} catch (e) {
			console.log(e);
		}
		//console.log(completePathA + " // " + sortStatus)
        return sortStatus;
    };
}
function isOnDate(startDate, endDate) {
    try {
		startDate = startDate.split("-");
		endDate = endDate.split("-");
		var todayDate = new Date();
		startDate = new Date(startDate[0], startDate[1]-1, startDate[2]);
		endDate = new Date(endDate[0], endDate[1]-1, endDate[2]);
		return todayDate <= endDate && todayDate >= startDate;
	} catch (e) {

	}
	return true;
}

function getGermanDecimalFormat(nr) {
	try {
		if (nr == undefined)
			return "";
		else {
			nr = String(nr);
			nr = nr.replace(".", ",");
			if (nr.indexOf(",") == -1)
				nr += ",00";
			else if (nr.toString().indexOf(",")+2 == nr.toString().length)
				nr += "0";
		}
	} catch(err) {
		console.log(err);
		return "";
	}
	return nr;
}

function getUuid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}

// Set all buttons to unchecked
function defaultAndDeleteAllObjectFields() {
	_openImmo_json = null
	_showedDocuments = false;
	_imagesTitles = [];
	var getDataOnce = true;
	$("#preview_container").empty();
	$(".btn_back").hide();
	$(".btn_delete").hide();
	$(".btn_save").removeAttr('disabled');
	$(".btn_save").html('<i class="fa fa-refresh"></i>');
	$('#base_objectnumber').val("");
	$('#base_objectnumber').attr('style', 'width: 20%;');
	$('#kind_0').click();
	$('#buy_0').click();
	$("#object_apart").val(0);
	$("#object_house").val(0);
	$("#object_base").val(0);
	$('#base_street').val("");
	$('#base_street').attr('style', '')
	$('#base_housenumber').val("");
	$('#base_plz').val("");
	$('#base_plz').attr('style', '');
	$('#base_location').val("");
	$('#base_location').attr('style', '');
	$('#address_show_yes').click();
	$('.nav-tabs a[href="#prices"]').tab('show');
	$("#prices_html").removeClass('erroneous-tab');
	$('#prices_buy').val("");
	$('#prices_buy').attr('style', 'width: 12%;');
	$('#prices_netto').val("");
	$('#prices_netto').attr('style', 'width: 12%;')
	$('#prices_service_charge').val("");
	$('#prices_service_charge').attr('style', 'width: 12%;')
	//$('#prices_cold').val("");
	//$('#prices_cold').attr('style', 'width: 12%;');
	//$('#prices_warm').val("");
	//$('#prices_warm').attr('style', 'width: 12%;');
	$('#prices_heatingcosts_1').click();
	$('#prices_additional').val("");
	$('#prices_additional').attr('style', 'width: 80%;');
	//$('#prices_business_netto').val("");
	//$('#prices_business_netto').attr('style', 'width: 12%;');
	$('#prices_caution').val("");
	$('#prices_caution').attr('style', 'width: 12%;');
	$('#prices_other_text').val("");
	$('#prices_heatingcosts').val("");
	$('#prices_heatingcosts').attr('style', 'width: 80%;');
	//$('#prices_total').val("");
	//$('#prices_total').attr('style', 'width: 12%;');
	//$('#prices_courtage').val("");
	//$('#prices_courtage').attr('style', 'width: 12%;');
	$('#prices_provision').val("");
	$('#prices_provision').attr('style', 'width: 12%;');
	$("#areas_html").removeClass('erroneous-tab');
	$('#areas_living').val("");
	$('#areas_living').attr('style', 'width: 12%;');
	$('#areas_base').val("");
	$('#areas_base').attr('style', 'width: 12%;');
	$('#areas_use').val("");
	$('#areas_use').attr('style', 'width: 12%;');
	$('#areas_total').val("");
	$('#areas_total').attr('style', 'width: 12%;');
	$('#areas_rooms').val("");
	$('#areas_rooms').attr('style', 'width: 12%;');
	if ($('#prices_provision_onoff').is(':checked'))
		$('#prices_provision_onoff').click();
	if ($('#appointments_ebk').is(':checked'))
		$('#appointments_ebk').click();
	if ($('#appointments_cellar').is(':checked'))
		$('#appointments_cellar').click();
	if ($('#appointments_balcony').is(':checked'))
		$('#appointments_balcony').click();
	if ($('#appointments_tv').is(':checked'))
		$('#appointments_tv').click();
	if ($('#appointments_bath_shower').is(':checked'))
		$('#appointments_bath_shower').click();
	if ($('#appointments_bath_tub').is(':checked'))
		$('#appointments_bath_tub').click();
	if ($('#appointments_bath_window').is(':checked'))
		$('#appointments_bath_window').click();
	if ($('#appointments_wash').is(':checked'))
		$('#appointments_wash').click();
	if ($('#appointments_accessible').is(':checked'))
		$('#appointments_accessible').click();
	if ($('#appointments_wheelchair').is(':checked'))
		$('#appointments_wheelchair').click();
	if ($('#appointments_lift').is(':checked'))
		$('#appointments_lift').click();
	if ($('#appointments_pitch').is(':checked'))
		$('#appointments_pitch').click();
	if ($('#appointments_allownote').is(':checked'))
		$('#appointments_allownote').click();
	if ($('#barrier_freeness_entry_bell').is(':checked'))
		$('#barrier_freeness_entry_bell').click();
	if ($('#barrier_freeness_door_opener').is(':checked'))
		$('#barrier_freeness_door_opener').click();
	if ($('#barrier_freeness_intercom').is(':checked'))
		$('#barrier_freeness_intercom').click();
	if ($('#barrier_freeness_wide_door').is(':checked'))
		$('#barrier_freeness_wide_door').click();
	if ($('#barrier_freeness_low_thresholds').is(':checked'))
		$('#barrier_freeness_low_thresholds').click();
	if ($('#barrier_freeness_wide_doors').is(':checked'))
		$('#barrier_freeness_wide_doors').click();
	if ($('#barrier_freeness_liftsize').is(':checked'))
		$('#barrier_freeness_liftsize').click();
	if ($('#barrier_freeness_bath_tub').is(':checked'))
		$('#barrier_freeness_bath_tub').click();
	if ($('#barrier_freeness_bath_shower').is(':checked'))
		$('#barrier_freeness_bath_shower').click();
	if ($('#barrier_freeness_bath_wide').is(':checked'))
		$('#barrier_freeness_bath_wide').click();
	if ($('#barrier_freeness_bath_large').is(':checked'))
		$('#barrier_freeness_bath_large').click();
	if ($('#barrier_freeness_balcony_wide_door').is(':checked'))
		$('#barrier_freeness_balcony_wide_door').click();
	if ($('#barrier_freeness_balcony_large').is(':checked'))
		$('#barrier_freeness_balcony_large').click();
	$('#description_year').val("");
	$("#description_state").val(0);
	$('#description_free').val("");
	$('#description_floor').val("");
	$('#description_title').val("");
	$('#description_location').val("");
	$('#description_appointments').val("");
	$('#description_description').val("");
	$('#description_other').val("");
	$("#energy_type").val(0);
	$('#energy_kwh').val("");
	$("#energy_deliverer").val(0);
	$("#energy_class").val(0);
	$('#energy_last').val("");
	$("#contact_html").removeClass('erroneous-tab');
	$('.btn_contacts').click(function() {
		if (getDataOnce) {
			getAllContacts();
			getDataOnce = false;
		}
	});
	$("#contact_title").val(0);
	$('#contact_firstname').val("");
	$('#contact_familyname').val("");
	$('#contact_familyname').attr('style', 'width: 80%;');
	$('#contact_email').val("");
	$('#contact_phone').val("");
	$('#contact_company').val("");
	$('#contact_street').val("");
	$('#contact_housenumber').val("");
	$('#contact_plz').val("");
	$('#contact_location').val("");
	$('#contact_url').val("");
	$("#barrier_freeness_stairs").val(-1);
	$("#barrier_freeness_entry_ramp").val(0);
	$("#barrier_freeness_liftcarsize").val(0);
	$("#barrier_freeness_bath_shower_tray").val(0);
	$("#barrier_freeness_balcony_threshold").val(0);
	$("#barrier_freeness_balcony_wheelchairparking").val(0);
	$('#info_activation').show();
	$('#homepage').hide();
	$('#immoscout').hide();
	$('#immowelt').hide();
	$('#hba').hide();
	$('#breba').hide();
	if (_portals !== null) {
		for (var portal = 0; portal < _portals.length; portal++) {
			if (_portals[portal] === 'immobrowse') {
				$('#info_activation').hide();
				$('#homepage').show();
				if ($('#activation_homepage').is(':checked'))
					$('#activation_homepage').click();
			} else if (_portals[portal] === 'immoscout24') {
				$('#info_activation').hide();
				$('#immoscout').show();
				if ($('#activation_immoscout').is(':checked'))
					$('#activation_immoscout').click();
			} else if (_portals[portal] === 'immowelt') {
				$('#info_activation').hide();
				$('#immowelt').show();
				if ($('#activation_immowelt').is(':checked'))
					$('#activation_immowelt').click();
			} else if (_portals[portal] === 'hba') {
				$('#info_activation').hide();
				$('#hba').show();
				if ($('#activation_hba').is(':checked'))
					$('#activation_hba').click();
			} else if (_portals[portal] === 'breba') {
				$('#info_activation').hide();
				$('#breba').show();
				if ($('#activation_breba').is(':checked'))
					$('#activation_breba').click();
			}
		}
	}
}

function setFields() {
	$("#base_objectnumber").val(_openImmo_json.verwaltung_techn.objektnr_extern);
	if (_openImmo_json.objektkategorie.vermarktungsart.KAUF == true)
		$('#buy_1').click();
	else
		$('#buy_0').click();
	if (Object.keys(_openImmo_json.objektkategorie.objektart)[0] == "haus") {
		$('#kind_1').click();
		if (/*_openImmo_json.objektkategorie.objektart.wohnung == haus || */_openImmo_json.objektkategorie.objektart.haus[0] == null || _openImmo_json.objektkategorie.objektart.haus[0] == "")
			$("#object_house").val(0);
		else
			$("#object_house").val(_openImmo_json.objektkategorie.objektart.haus[0]);
	} else if (Object.keys(_openImmo_json.objektkategorie.objektart)[0] == "grundstueck") {
		$('#kind_2').click();
	} else {
		$('#kind_0').click();
		if (_openImmo_json.objektkategorie.objektart.wohnung == undefined || _openImmo_json.objektkategorie.objektart.wohnung[0] == null || _openImmo_json.objektkategorie.objektart.wohnung[0] == "")
			$("#object_apart").val(0);
		else
			$("#object_apart").val(_openImmo_json.objektkategorie.objektart.wohnung[0]);
	}
	if (_openImmo_json.hasOwnProperty('geo')) {
		$("#description_floor").val(_openImmo_json.geo.etage);
		$("#base_street").val(_openImmo_json.geo.strasse);
		$("#base_housenumber").val(_openImmo_json.geo.hausnummer);
		$("#base_plz").val(_openImmo_json.geo.plz);
		$("#base_location").val(_openImmo_json.geo.ort);
	}
	if (_openImmo_json.hasOwnProperty('verwaltung_objekt')) {
		$("#description_free").val(_openImmo_json.verwaltung_objekt.verfuegbar_ab);
		if (_openImmo_json.verwaltung_objekt.objektadresse_freigeben == true)
			$('#address_show_yes').click();
		else
			$('#address_show_no').click();
		if (_openImmo_json.verwaltung_objekt.wbs_sozialwohnung == true)
			$('#appointments_allownote').click();
	}

	// Prices
	if (_openImmo_json.hasOwnProperty('preise')) {
		$("#prices_buy").val(getGermanDecimalFormat(_openImmo_json.preise.kaufpreis));
		$("#prices_netto").val(getGermanDecimalFormat(_openImmo_json.preise.nettokaltmiete));
		if (_openImmo_json.preise.betriebskostennetto == null) {
		  $("#prices_service_charge").val('');
		} else {
		  $("#prices_service_charge").val(getGermanDecimalFormat(_openImmo_json.preise.betriebskostennetto));
		}
		//$("#prices_cold").val(getGermanDecimalFormat(_openImmo_json.preise.kaltmiete));
		//$("#prices_warm").val(getGermanDecimalFormat(_openImmo_json.preise.warmmiete));
		$("#prices_additional").val(getGermanDecimalFormat(_openImmo_json.preise.nebenkosten));
		if (_openImmo_json.preise.heizkosten_enthalten == true)
			$('#prices_heatingcosts_1').click();
		else {
			$('#prices_heatingcosts_0').click();
			$("#prices_heatingcosts").val(getGermanDecimalFormat(_openImmo_json.preise.heizkosten));
		}
		//$("#prices_total").val(getGermanDecimalFormat(_openImmo_json.preise.gesamtmietenetto));
		//$("#prices_business_netto").val(getGermanDecimalFormat(_openImmo_json.preise.betriebskostennetto));
		//$("#prices_courtage").val(_openImmo_json.preise.aussen_courtage);
		$("#prices_caution").val(getGermanDecimalFormat(_openImmo_json.preise.kaution));
		if (_openImmo_json.preise.provisionspflichtig == true)
			$('#prices_provision_onoff').click();
		$("#prices_provision").val(_openImmo_json.preise.provisionbrutto);
	}

	// Areas
	if (_openImmo_json.hasOwnProperty('flaechen')) {
		$("#areas_living").val(getGermanDecimalFormat(_openImmo_json.flaechen.wohnflaeche));
		$("#areas_use").val(getGermanDecimalFormat(_openImmo_json.flaechen.nutzflaeche));
		$("#areas_total").val(getGermanDecimalFormat(_openImmo_json.flaechen.gesamtflaeche));
		$("#areas_base").val(getGermanDecimalFormat(_openImmo_json.flaechen.grundstuecksflaeche));
		$("#areas_rooms").val(_openImmo_json.flaechen.anzahl_zimmer.toString().replace(".", ","));
		if (_openImmo_json.flaechen.anzahl_balkone == 1)
			$('#appointments_balcony').click();
	}

	// Appointments
	if (_openImmo_json.hasOwnProperty('ausstattung')) {
		if (_openImmo_json.ausstattung.hasOwnProperty('kueche'))
			if (_openImmo_json.ausstattung.kueche.EBK == true)
				$('#appointments_ebk').click();
		if (_openImmo_json.ausstattung.unterkellert == "JA")
			$('#appointments_cellar').click();
		if (_openImmo_json.ausstattung.hasOwnProperty('bad')) {
			if (_openImmo_json.ausstattung.bad.DUSCHE == true)
				$('#appointments_bath_shower').click();
			if (_openImmo_json.ausstattung.bad.WANNE == true)
				$('#appointments_bath_tub').click();
			if (_openImmo_json.ausstattung.bad.FENSTER == true)
				$('#appointments_bath_window').click();
		}
		if (_openImmo_json.ausstattung.barrierefrei == true)
			$('#appointments_accessible').click();
		if (_openImmo_json.ausstattung.rollstuhlgerecht == true)
			$('#appointments_wheelchair').click();
		if (_openImmo_json.ausstattung.hasOwnProperty('fahrstuhl'))
			if (_openImmo_json.ausstattung.fahrstuhl.PERSONEN == true)
				$('#appointments_lift').click();
		if (_openImmo_json.ausstattung.hasOwnProperty('stellplatzart'))
		if (_openImmo_json.ausstattung.stellplatzart.FREIPLATZ == true)
			$('#appointments_pitch').click();
		if (_openImmo_json.ausstattung.kabel_sat_tv == true)
			$('#appointments_tv').click();
		if (_openImmo_json.ausstattung.wasch_trockenraum == true)
			$('#appointments_wash').click();

		// Barrier freeness
		if (_openImmo_json.hasOwnProperty('barrier_freeness')) {
			if (_openImmo_json.barrier_freeness.hasOwnProperty('stairs'))
				$("#barrier_freeness_stairs").val(_openImmo_json.barrier_freeness.stairs);
			if (_openImmo_json.barrier_freeness.hasOwnProperty('entry')) {
				if (_openImmo_json.barrier_freeness.entry.hasOwnProperty('ramp_din'))
					$("#barrier_freeness_entry_ramp").val(_openImmo_json.barrier_freeness.entry.ramp_din.toString());
				if (_openImmo_json.barrier_freeness.entry.doorbell_panel == true)
					$('#barrier_freeness_entry_bell').click();
				if (_openImmo_json.barrier_freeness.entry.door_opener == true)
					$('#barrier_freeness_door_opener').click();
				if (_openImmo_json.barrier_freeness.entry.intercom == true)
					$('#barrier_freeness_intercom').click();
			}
			if (_openImmo_json.barrier_freeness.wide_door == true)
				$('#barrier_freeness_wide_door').click();
			if (_openImmo_json.barrier_freeness.low_thresholds == true)
				$('#barrier_freeness_low_thresholds').click();
			if (_openImmo_json.barrier_freeness.wide_doors == true)
				$('#barrier_freeness_wide_doors').click();
			if (_openImmo_json.barrier_freeness.hasOwnProperty('lift')) {
				if (_openImmo_json.barrier_freeness.lift.hasOwnProperty('value')) {
					if (_openImmo_json.barrier_freeness.lift.value.toString() == 'unknown')
						$('#barrier_freeness_liftcarsize').val('0');
					else
						$('#barrier_freeness_liftcarsize').val(_openImmo_json.barrier_freeness.lift.value.toString());
				}
				if (_openImmo_json.barrier_freeness.lift.hasOwnProperty('wide_door'))
					if (_openImmo_json.barrier_freeness.lift.wide_door == true)
						$('#barrier_freeness_liftsize').click();
			}
			if (_openImmo_json.barrier_freeness.hasOwnProperty('bath')) {
				if (_openImmo_json.barrier_freeness.bath.bathtub == true)
					$('#barrier_freeness_bath_tub').click();
				if (_openImmo_json.barrier_freeness.bath.wide == true)
					$('#barrier_freeness_bath_wide').click();
				if (_openImmo_json.barrier_freeness.bath.large == true)
					$('#barrier_freeness_bath_large').click();
				if (_openImmo_json.barrier_freeness.bath.hasOwnProperty('shower_tray')) {
					$('#barrier_freeness_bath_shower').click();
					$("#barrier_freeness_bath_shower_tray").val(_openImmo_json.barrier_freeness.bath.shower_tray);
				}
			}
			if (_openImmo_json.barrier_freeness.hasOwnProperty('balcony')) {
				if (_openImmo_json.barrier_freeness.balcony.wide_door == true)
					$('#barrier_freeness_balcony_wide_door').click();
				if (_openImmo_json.barrier_freeness.balcony.large == true)
					$('#barrier_freeness_balcony_large').click();
				if (_openImmo_json.barrier_freeness.balcony.hasOwnProperty('threshold'))
					$("#barrier_freeness_balcony_threshold").val(_openImmo_json.barrier_freeness.balcony.threshold.toString());
			}
			if (_openImmo_json.barrier_freeness.hasOwnProperty('wheelchair_parking'))
				$("#barrier_freeness_balcony_wheelchairparking").val(_openImmo_json.barrier_freeness.wheelchair_parking);
		}
	}

	// Contacts
	if (_openImmo_json.hasOwnProperty('kontaktperson')) {
		if (_openImmo_json.kontaktperson.hasOwnProperty('anrede'))
			$("#contact_title").val(_openImmo_json.kontaktperson.anrede);
		else
			$("#contact_title").val("0");
		$("#contact_firstname").val(_openImmo_json.kontaktperson.vorname);
		$("#contact_familyname").val(_openImmo_json.kontaktperson.name);
		$("#contact_email").val(_openImmo_json.kontaktperson.email_direkt);
		$("#contact_phone").val(_openImmo_json.kontaktperson.tel_durchw);
		$("#contact_company").val(_openImmo_json.kontaktperson.firma);
		$("#contact_street").val(_openImmo_json.kontaktperson.strasse);
		$("#contact_housenumber").val(_openImmo_json.kontaktperson.hausnummer);
		$("#contact_plz").val(_openImmo_json.kontaktperson.plz);
		$("#contact_location").val(_openImmo_json.kontaktperson.ort);
		$("#contact_url").val(_openImmo_json.kontaktperson.url);
	}

	// Descriptions
	if (_openImmo_json.hasOwnProperty('freitexte')) {
		$("#description_title").val(_openImmo_json.freitexte.objekttitel);
		$("#description_location").val(_openImmo_json.freitexte.lage);
		$("#description_appointments").val(_openImmo_json.freitexte.ausstatt_beschr);
		$("#description_description").val(_openImmo_json.freitexte.objektbeschreibung);
		$("#description_other").val(_openImmo_json.freitexte.sonstige_angaben);
	}

	if (_openImmo_json.hasOwnProperty('zustand_angaben')) {
		$("#energy_last").val(_openImmo_json.zustand_angaben.letztemodernisierung); // Energy
		$("#description_year").val(_openImmo_json.zustand_angaben.baujahr); // Descriptions
		if (_openImmo_json.zustand_angaben.hasOwnProperty('zustand'))
			$("#description_state").val(_openImmo_json.zustand_angaben.zustand);
		else
			$("#description_state").val("0");
		// Energy
		if (_openImmo_json.zustand_angaben.hasOwnProperty('energiepass')) {
			if (_openImmo_json.zustand_angaben.energiepass[0].hasOwnProperty('epart'))
				$("#energy_type").val(_openImmo_json.zustand_angaben.energiepass[0].epart);
			else
				$("#energy_type").val(0);
			if ($("#energy_type").val() === "BEDARF" )
				$("#energy_kwh").val(_openImmo_json.zustand_angaben.energiepass[0].endenergiebedarf);
			else if ($("#energy_type").val() === "VERBRAUCH" )
				$("#energy_kwh").val(_openImmo_json.zustand_angaben.energiepass[0].energieverbrauchkennwert);
			if (_openImmo_json.zustand_angaben.energiepass[0].hasOwnProperty('primaerenergietraeger')) //	if (_openImmo_json.zustand_angaben.energiepass[0].primaerenergietraeger == null || _openImmo_json.zustand_angaben.energiepass[0].primaerenergietraeger == "")
				$("#energy_deliverer").val(_openImmo_json.zustand_angaben.energiepass[0].primaerenergietraeger);
			else
				$("#energy_deliverer").val(0);
			if (_openImmo_json.zustand_angaben.energiepass[0].hasOwnProperty('wertklasse')) //	if (_openImmo_json.zustand_angaben.energiepass[0].wertklasse == null || _openImmo_json.zustand_angaben.energiepass[0].wertklasse == "")
				$("#energy_class").val(_openImmo_json.zustand_angaben.energiepass[0].wertklasse);
			else
				$("#energy_class").val(0);
		}
	}

	// Activation
	if (_openImmo_json.verwaltung_techn.hasOwnProperty('weitergabe_positiv')) {
		for (var i = 0; i < _openImmo_json.verwaltung_techn.weitergabe_positiv.length; i++) {
			if (_openImmo_json.verwaltung_techn.weitergabe_positiv[i] === 'immobrowse')
				$('#activation_homepage').click();
			else if (_openImmo_json.verwaltung_techn.weitergabe_positiv[i] === 'immoscout24')
				$('#activation_immoscout').click();
			else if (_openImmo_json.verwaltung_techn.weitergabe_positiv[i] === 'immowelt')
				$('#activation_immowelt').click();
			else if (_openImmo_json.verwaltung_techn.weitergabe_positiv[i] === 'hba')
				$('#activation_hba').click();
			else if (_openImmo_json.verwaltung_techn.weitergabe_positiv[i] === 'breba')
				$('#activation_breba').click();
		}
	}
}