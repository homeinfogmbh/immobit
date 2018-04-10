checkSession(); // Disable for testing without login
var _openImmo_json = null;
var _page = 0;
var _imagesTitles = [];
var _deleteRealEstates;
var _fileinput;
var _data = null;
var _showedDocuments;
var _portals = null;
var _id; // id coming from backend)
$(window).load(function() {
	$("#startpage").trigger( "click" ); // startpage // manage_exposes // create_expose
	setSpeech("german");
 });
$(document).ready(function() {
	var imported = document.createElement('script');
	imported.src = 'js/checkfields.js';
	document.head.appendChild(imported);
	$('[data-toggle="tooltip"]').tooltip();
	//$("#page").show(); // Enable for testing without login
	//if (window.location.href.indexOf("new") != -1) // if not using defaultAndDeleteAllObjectFields() in $('.btn_new_object').click(
		//$("#nav_create_expose").show();
	getAccountData();// Getaccount Infos
			
	// Settings
	$("#description_free").datepicker({
		constrainInput: false,
        monthNames: ['Januar','Februar','März','April','Mai','Juni',
        'Juli','August','September','Oktober','November','Dezember'],
        monthNamesShort: ['Jan','Feb','Mär','Apr','Mai','Jun',
        'Jul','Aug','Sep','Okt','Nov','Dez'],
        dayNames: ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'],
        dayNamesShort: ['So','Mo','Di','Mi','Do','Fr','Sa'],
        dayNamesMin: ['So','Mo','Di','Mi','Do','Fr','Sa'],
		dateFormat : "dd.mm.yy"
	}, $.datepicker.regional['de']);
	$('.logout').click(function() {
		$('#pageloader').show();
		$.ajax({
			url: "https://his.homeinfo.de/session/" +  localStorage.getItem("token"),
			type: "DELETE",
			complete: function (msg) {
				$('#pageloader').hide();
				localStorage.removeItem("token");
				window.location.href = "login.html";
			}
		});
	});	
	// Speech
	$('.english').click(function() {
		holdSession();
		setSpeech("english");
	});
	$('.german').click(function() {
		holdSession();
		setSpeech("german");
	});
	// Navigation
	$('#startpage').click(function() {
		$('#pageloader').show();
		holdSession();
		removeSidebarComponents($(this));
		$("#nav_startpage").show();
		
		$.ajax({
			url: "https://backend.immobit.de/realestates?session=" +localStorage.getItem("token"),
			type: "GET",
			success: function (msg) {
				var startpage_info = "</div><font size='4'><label>Es befinden sich zur Zeit <font size='6' color='#159f18'>" +  msg.length + "</font> Immobilien auf dieser Plattform.<label></font>"
				var aktive = 0;
				var inaktive = 0;
				for (var i = 0; i < msg.length; i++) {
					//if (isOnDate(msg[i].verwaltung_techn["aktiv_von"], msg[i].verwaltung_techn["aktiv_bis"]))
					if (msg[i].verwaltung_techn.hasOwnProperty('weitergabe_positiv')) {
						if (msg[i].verwaltung_techn.weitergabe_positiv.length > 0)
							aktive++;
						else 
							inaktive++;
					} else
						inaktive++;
				}
				$("#startpage_info").html(startpage_info + "<br><font size='4'><label>Aktive Objekte:</font></label><div class='numberCircle'><label><font size='6' color='#159f18'>" + aktive + "</font></label></div> <br>" + "<font size='4'><label>Inaktive Objekte:</font></label><div class='numberCircle'><label><font size='6' color='#ff0000'>" + inaktive + "</font></label>");
			},
			complete: function (msg) {
				$('#pageloader').hide();
			},
			error: function (msg) {
				JSON.stringify(msg);
			}
		});
	});
	$('#create_expose').click(function() {
		holdSession();
		removeSidebarComponents($(this));
		defaultAndDeleteAllObjectFields();
		$("#content_title").html('<h1>Immobilie anlegen</h1>');
		$("#nav_create_expose").show();
		$("#managedcontainer").show();
		$('#base_objectnumber').focus();
		/*
		//$("#create_object").load("create_object.html");
		$.ajax({
			url: "create_object.html",
			dataType: 'html',
			success: function (html) {
				$("#create_object").html(html);
				$("#nav_create_expose").show();
			},
			error: function (msg) {
				console.log("ERROR" + msg.status);
			}
		});
	*/		
	});	
	$('#manage_exposes').click(function() {
		holdSession();
		removeSidebarComponents($(this));
		getAllRealEstates();
		$("#nav_manage_exposes").show();
		$("#manage_title").html('<h1>Immobilien verwalten</h1>');
	});	

	$('.btn_active').click(function() {
		holdSession();
	});
	$('.btn_documents').click(function() {
		_showedDocuments = true;
		getImages();
	});		
	
	// Rent
	$('#buy_0').change(function() {
		$('#kind_2_label').attr('style', 'pointer-events: none;');
		$('#kind_2_label').attr('disabled', 'disabled');
		$("#prices_buy_div").hide();
		$("#prices_rent_div").show();
		$("#areas_apart_div").show();
		$("#description_year_state_div").show();
		$("#prices_provision_div").hide();
		if ($("#kind_2").is(':checked'))
			$("#kind_0").trigger( "click" );
		if ($("#kind_0").is(':checked')) {
			$("#areas_use_complete_div").hide();
			$("#areas_floor_div").show();
		}
	})
	// Buy
	$('#buy_1').change(function() {
		$('#kind_2_label').removeAttr('disabled');
		$('#kind_2_label').removeAttr('style');
		$("#prices_buy_div").show();
		$("#prices_rent_div").hide();
		$("#areas_apart_div").show();
		$("#areas_use_complete_div").show();
		$("#prices_provision_div").show();
		if ($("#kind_1").is(':checked'))
			$("#areas_base_div").show();
		if ($("#kind_0").is(':checked'))
			$("#areas_floor_div").show();
	})	
	
	// Apartments (apart)
	$('#kind_0').change(function() {
		hideAll();
		$("#areas_apart_div").show();
		$("#object_apart").show();
		$("#appintsments_div").show();
		$(".btn_appointments").show();
		$("#energy_div").show();
		$(".btn_energy").show();
		$("#limited_div").show();
		$(".btn_limited").show();
		$("#areas_use_complete_rooms_div").show();		
		$("#description_year_state_div").show();
		$("#areas_floor_div").show();
		if ($("#buy_0").is(':checked'))
			$("#areas_use_complete_div").hide();		
	})	
	// Houses (house)
	$('#kind_1').change(function() {
		hideAll();
		$("#object_house").show();
		//console.log($('#appointments').is(":visible"));
		$("#appintsments_div").show();
		$(".btn_appointments").show();
		$("#areas_apart_div").show();
		$("#energy_div").show();
		$(".btn_energy").show();
		$("#limited_div").show();
		$(".btn_limited").show();
		$("#areas_use_complete_rooms_div").show();
		$("#description_year_state_div").show();
		if ($("#buy_1").is(':checked'))
			$("#areas_base_div").show();
	})
	// Basements (base)
	$('#kind_2').change(function() {
		hideAll();
		$("#areas_base_div").show();
		$("#object_base").show();
		$("#appintsments_div").hide();
		$(".btn_appointments").hide();
		$("#energy_div").hide();
		$(".btn_energy").hide();
		$("#limited_div").hide();
		$(".btn_limited").hide();
		$("#areas_use_complete_rooms_div").hide();
	})
	
	// Prices
	$('#prices_provision_onoff').change(function() {
		if ($("#prices_provision_onoff").is(':checked'))
			$('#prices_provision').removeAttr('disabled');
		else
			$('#prices_provision').attr('disabled', 'disabled');
	});
	$('#prices_heatingcosts_1').change(function() {		
		if ($("#prices_heatingcosts_1").is(':checked'))
			$('#prices_heatingcosts').attr('disabled', 'disabled');
	})	
	$('#prices_heatingcosts_0').change(function() {
		if ($("#prices_heatingcosts_0").is(':checked'))
			$('#prices_heatingcosts').removeAttr('disabled');
	})		
	
	// Checkboxes 
    $('.button-checkbox').each(function () {
        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color'),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };
        // Event Handlers
        $button.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Set the button's icon
            $button.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$button.data('state')].icon);

            // Update the button's color
            if (isChecked) {
                $button
                    .removeClass('btn-default')
                    .addClass('btn-' + color + ' active');
            }
            else {
                $button
                    .removeClass('btn-' + color + ' active')
                    .addClass('btn-default');
            }
        }

        // Initialization
        function init() {
            updateDisplay();
            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i> ');
            }
        }
        init();
    });
	
	
	$(".btn_save").click(function() {
		 if (!checkData()) { // 'false' for testing
			swal({
				title: "Achtung!",
				text: "Bitte füllen Sie die rot gekennzeichneten Felder richtig aus.",
				type: "warning",
				timer: 3000,
				showConfirmButton: true,
				confirmButtonColor: "#428bca",
			});
			// Save object
		 } else {
			var urlString = "";
			var typeString;
			$("#loader_save").show();
			$(".btn_save").html('Immobilie wird gespeichert');
			$(".btn_save").attr('disabled', 'disabled');
			
			if (_openImmo_json !== null) {
				urlString = "/" + _openImmo_json.id;
				_id = _openImmo_json.id;
				typeString = "PATCH";
				saveMetaDataForImages(null);
			} else
				typeString = "POST";
			var openImmo = createRealEstateJSON();
			$.ajax({
				url: "https://backend.immobit.de/realestates" + urlString + "?session=" + localStorage.getItem("token"),
				type: typeString,
				data: JSON.stringify(openImmo),
				success: function (msg) {
					if (msg.hasOwnProperty("id"))
						_id = msg.id;
					if (_data !== null) // _data set in fileinput.js
						_data._uploadClick();
					if (typeString == "PATCH") {
						if (_openImmo_json.hasOwnProperty("anhaenge")) {
							if (_imagesTitles.length == _openImmo_json.anhaenge.anhang.length || !_showedDocuments) {
								$("#manage_exposes").trigger( "click" );
								$(window).scrollTop(0);
							}
						} else if (_imagesTitles.length == 0) {
							$("#manage_exposes").trigger( "click" );
							$(window).scrollTop(0);
						}
					}
					$(".btn_save").html('Immobilie wurde erfolgreich gespeichert');
				},
				error: function (msg) {
					//console.log("ERROR " + msg.responseJSON.message);
					try {
						if (msg.responseJSON.message == "Immobilie existiert bereits.") {
							$('#base_objectnumber').attr('style', 'width: 20%; border: 1px solid #ff0000; border-radius: 4px;');
							$(".btn_save").html('Diese Immobilie ist bereits vorhanden! Bitte ändern Sie die Objektnummer.');
							_openImmo_json = openImmo;
							$(".btn_save").trigger( "click" );
						} else if (msg.responseJSON.message == "Zugriff verweigert.") {
							$(".btn_save").html('Sie haben leider nicht die Berechtigung Immobilien anzulegen.');
						} else if (msg.responseJSON.message == "Keine solche Sitzung.") {
							$(".btn_save").html('Ihre Sitzung ist leider abgelaufen. Bitte melden sich sich erneut an.');
						} else
							$(".btn_save").html('Es ist leider ein Fehler aufgetreten, bitte versuchen Sie es erneut.');
					} catch(e) {
						$(".btn_save").html('Es ist leider ein Fehler aufgetreten, bitte versuchen Sie es erneut.');
						console.log(msg.responseText);
					}
				},
				complete:  function () {
					$("#loader_save").hide();
					$(".btn_save").removeAttr('disabled');
				}
			});
		}
	});
	// Reload
	$('.btn_new_object').click(function() {
		holdSession();
		$("#create_expose").trigger( "click" ); //window.location.href = "index.html?new";
	});
	$('.btn_preview').click(function() {
		holdSession();
		showpreview(createRealEstateJSON(false));
	});	
	$('.btn_back').click(function() {
		$(this).hide();
		$("#manage_exposes").trigger( "click" ); //window.location.href = "index.html?new";
	});	
	$('.btn_change_count_realestates').change(function() {
		var sorting = $(this).data("sorting");
		var reverse = $(this).data("reverse");
		getAllRealEstates(_page, sorting, reverse);
	});
	
	$('#searchfield').on('input',function(e) {
		loadRealEstates(_page);
	});	
	$('.btn_delete').click(function() {
		swal({
			title: "Sind Sie sicher?",
			text: "Wollen Sie die Immobilie <span style='color:#5cb85c;'>" + _openImmo_json.verwaltung_techn.objektnr_extern + "</span> wirklich löschen?",
			type: "warning",
			showCancelButton: true,
			html: true,
			confirmButtonColor: "#5bb75b",
			confirmButtonText: "Ja!",
			cancelButtonText: "Nein",
			closeOnConfirm: true,
			closeOnCancel: true
		},
		function(isConfirm) {
			if (isConfirm) {
				$("#loader_manage").show();
				//for (i=0; i < msg.length; i++) { // delete all
				$.ajax({
					url: "https://backend.immobit.de/realestates/" + _openImmo_json.id + "?session=" +  localStorage.getItem("token"),
					type: "DELETE",
					success: function (msg) {
						$("#manage_exposes").trigger( "click" ); 
					},
					error: function (msg) {
						$("#loader_manage").hide();
						console.log("ERROR " + JSON.stringify(msg));
						$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#FF0000">Beim Löschen der Immobilie ' + id + ' ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.</font>');
					}
				});
				//}
			}
		});
	});
	$('.btn_delete_several').click(function() {
		swal({
			title: "Sind Sie sicher?",
			text: "Wollen Sie wirklich <span style='color:#5cb85c;'>" + _deleteRealEstates.length + "</span>" + ((_deleteRealEstates == 1) ?" Immobilie" :" Immobilien") + " löschen?",
			type: "warning",
			showCancelButton: true,
			html: true,
			confirmButtonColor: "#5bb75b",
			confirmButtonText: "Ja!",
			cancelButtonText: "Nein",
			closeOnConfirm: true,
			closeOnCancel: true
		},
		function(isConfirm) {
			if (isConfirm) {
				$("#loader_manage").show();
				for (i = 0; i < _deleteRealEstates.length; i++) {
					$.ajax({
						url: "https://backend.immobit.de/realestates/" + _openImmo_json[_deleteRealEstates[i]].id + "?session=" +  localStorage.getItem("token"),
						type: "DELETE",
						success: function (msg) {
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#000">Immobilien wurden erfolgreich gelöscht.</font>');
							holdSession();
							getAllRealEstates();
						},
						error: function (msg) {
							$("#loader_manage").hide();
							console.log("ERROR " + JSON.stringify(msg));
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#FF0000">Beim Löschen ein Fehler aufgetreten. Bitte versuchen Sie es erneut.</font>');
						}
					});
				}
			}
		});		
	});	
});

function getAccountData() {
		$.ajax({
		url: "https://backend.immobit.de/portals?session=" + localStorage.getItem("token"),
		type: "GET",
		complete: function (msg) {
			_portals = msg.responseJSON;
		},
		error: function (msg) {
			console.log(msg);
		}
	});
	/*
	$.ajax({
		url: "https://his.homeinfo.de/account/!?session=" + localStorage.getItem("token"),
		type: "GET",
		complete: function (msg) {
			var i;
			for (i = 0; i < _customerWithPortalHBA.length; i++) {
				if (msg.responseJSON.customer == _customerWithPortalHBA[i]) {
					_hasHBA = true;
					$('#hba').show();
					break;
				}
			}
			for (i = 0; i < _customerWithPortalBREBA.length; i++) {
				if (msg.responseJSON.customer == _customerWithPortalBREBA[i]) {
					_hasBREBA = true;
					$('#breba').show();
					break;
				}
			}
		},
		error: function (msg) {
			console.log(msg);
		}
	});
	*/
}
function createRealEstateJSON(check = true) {
	var date = new Date();
	var date_str = date.getFullYear() + '-' + ('0'+(date.getMonth()+1)).substr(-2,2) + '-' + ('0'+date.getDate()).substr(-2,2);
	//if ($("#areas_base_div").attr('style') != "display: none;") {
	var openimmo = {};
	openimmo["kontaktperson"] = {};
		(hasChanged(check,"kontaktperson","anrede", $("#contact_title").val())) ?openimmo.kontaktperson["anrede"] = $("#contact_title").val() :false;
		($("#contact_firstname").val().trim() == "") ?(isNull("kontaktperson.vorname")) ?false :openimmo.kontaktperson["vorname"] = null :(hasChanged(check,"kontaktperson","vorname", $("#contact_firstname").val())) ?openimmo.kontaktperson["vorname"] = $("#contact_firstname").val() :false;
		(hasChanged(check,"kontaktperson","name", $("#contact_familyname").val())) ?openimmo.kontaktperson["name"] = $("#contact_familyname").val() :false;
		($("#contact_email").val().trim() == "") ?(isNull("kontaktperson.email_direkt")) ?false :openimmo.kontaktperson["email_direkt"] = null :(hasChanged(check,"kontaktperson","email_direkt", $("#contact_email").val())) ?openimmo.kontaktperson["email_direkt"] = $("#contact_email").val() :false;
		($("#contact_phone").val().trim() == "") ?(isNull("kontaktperson.tel_durchw")) ?false :openimmo.kontaktperson["tel_durchw"] = null :(hasChanged(check,"kontaktperson","tel_durchw", $("#contact_phone").val())) ?openimmo.kontaktperson["tel_durchw"] = $("#contact_phone").val() :false;
		($("#contact_company").val().trim() == "") ?(isNull("kontaktperson.firma")) ?false :openimmo.kontaktperson["firma"] = null :(hasChanged(check,"kontaktperson","firma", $("#contact_company").val())) ?openimmo.kontaktperson["firma"] = $("#contact_company").val() :false;
		($("#contact_street").val().trim() == "") ?(isNull("kontaktperson.strasse")) ?false :openimmo.kontaktperson["strasse"] = null :(hasChanged(check,"kontaktperson","strasse", $("#contact_street").val())) ?openimmo.kontaktperson["strasse"] = $("#contact_street").val() :false;
		($("#contact_housenumber").val().trim() == "") ?(isNull("kontaktperson.hausnummer")) ?false :openimmo.kontaktperson["hausnummer"] = null :(hasChanged(check,"kontaktperson","hausnummer", $("#contact_housenumber").val())) ?openimmo.kontaktperson["hausnummer"] = $("#contact_housenumber").val() :false;
		($("#contact_plz").val().trim() == "") ?(isNull("kontaktperson.plz")) ?false :openimmo.kontaktperson["plz"] = null :(hasChanged(check,"kontaktperson","plz", $("#contact_plz").val())) ?openimmo.kontaktperson["plz"] = $("#contact_plz").val() :false;
		($("#contact_location").val().trim() == "") ?(isNull("kontaktperson.ort")) ?false :openimmo.kontaktperson["ort"] = null :(hasChanged(check,"kontaktperson","ort", $("#contact_location").val())) ?openimmo.kontaktperson["ort"] = $("#contact_location").val() :false;
		($("#contact_url").val().trim() == "") ?(isNull("kontaktperson.url")) ?false :openimmo.kontaktperson["url"] = null:(hasChanged(check,"kontaktperson","url", $("#contact_url").val())) ?openimmo.kontaktperson["url"] = $("#contact_url").val() :false;
	openimmo["preise"] = {};
		($("#prices_buy").val().trim() == "" || $("#prices_buy_div").attr('style') == "display: none;") ?(isNull("preise.kaufpreis")) ?false :openimmo.preise["kaufpreis"] = null :(hasChanged(check,"preise","kaufpreis", $("#prices_buy").val().replace(",", "."))) ?openimmo.preise["kaufpreis"] = Number($("#prices_buy").val().replace(",", ".")) :false;
		($("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.nettokaltmiete")) ?false :openimmo.preise["nettokaltmiete"] = null :(hasChanged(check,"preise","nettokaltmiete", $("#prices_netto").val().replace(",", "."))) ?openimmo.preise["nettokaltmiete"] = Number($("#prices_netto").val().replace(",", ".")) :false;
		//($("#prices_cold").val().trim() != "" && $("#prices_rent_div").attr('style') != "display: none;" && hasChanged(check,"preise","kaltmiete", $("#prices_cold").val().replace(",", "."))) ?openimmo.preise["kaltmiete"] = Number($("#prices_cold").val().replace(",", ".")) :false;
		//($("#prices_warm").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.warmmiete")) ?false :openimmo.preise["warmmiete"] = null :(hasChanged(check,"preise","warmmiete", $("#prices_warm").val().replace(",", "."))) ?openimmo.preise["warmmiete"] = Number($("#prices_warm").val().replace(",", ".")) :false;
		($("#prices_additional").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.nebenkosten")) ?false :openimmo.preise["nebenkosten"] = null :(hasChanged(check,"preise","nebenkosten", $("#prices_additional").val().replace(",", "."))) ?openimmo.preise["nebenkosten"] = Number( $("#prices_additional").val().replace(",", ".")) :false;
		//($("#prices_business_netto").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.betriebskostennetto")) ?false :openimmo.preise["betriebskostennetto"] = null :(hasChanged(check,"preise","betriebskostennetto", $("#prices_business_netto").val().replace(",", "."))) ?openimmo.preise["betriebskostennetto"] = Number($("#prices_business_netto").val().replace(",", ".")) :false;
		($("#prices_caution").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.kaution")) ?false :openimmo.preise["kaution"] = null :(hasChanged(check,"preise","kaution", $("#prices_caution").val().replace(",", "."))) ?openimmo.preise["kaution"] = Number($("#prices_caution").val().replace(",", ".")) :false;
		($("#prices_heatingcosts").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.heizkosten")) ?false :openimmo.preise["heizkosten"] = null :(hasChanged(check,"preise","heizkosten", $("#prices_heatingcosts").val().replace(",", "."))) ?openimmo.preise["heizkosten"] = Number($("#prices_heatingcosts").val().replace(",", ".")) :false;
		//($("#prices_total").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.gesamtmietenetto")) ?false :openimmo.preise["gesamtmietenetto"] = null :(hasChanged(check,"preise","gesamtmietenetto", $("#prices_total").val().replace(",", "."))) ?openimmo.preise["gesamtmietenetto"] = Number($("#prices_total").val().replace(",", ".")) :false;
		//($("#prices_courtage").val().trim() == "" || $("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.aussen_courtage")) ?false :openimmo.preise["aussen_courtage"] = null :(hasChanged(check,"preise","aussen_courtage", $("#prices_courtage").val())) ?openimmo.preise["aussen_courtage"] = $("#prices_courtage").val() :false;
		($("#prices_provision_div").attr('style') == "display: none;") ?(isNull("preise.provisionspflichtig")) ?false :openimmo.preise["provisionspflichtig"] = null :(hasChanged(check,"preise","provisionspflichtig", $("#prices_provision_onoff").is(':checked'))) ?openimmo.preise["provisionspflichtig"] = $("#prices_provision_onoff").is(':checked') :false;
		(!$("#prices_provision_onoff").is(':checked') || $("#prices_provision_div").attr('style') == "display: none;") ?(isNull("preise.provisionbrutto")) ?false :openimmo.preise["provisionbrutto"] = null :(hasChanged(check,"preise","provisionbrutto", $("#prices_provision").val().replace(",", "."))) ?openimmo.preise["provisionbrutto"] = Number($("#prices_provision").val().replace(",", ".")) :false;
		($("#prices_rent_div").attr('style') == "display: none;") ?(isNull("preise.heizkosten_enthalten")) ?false :openimmo.preise["heizkosten_enthalten"] = null :(hasChanged(check,"preise","heizkosten_enthalten", $('input[name=prices_heatingcosts_show]:checked').val() == "true")) ?openimmo.preise["heizkosten_enthalten"] = $('input[name=prices_heatingcosts_show]:checked').val() == "true" :false;
	openimmo["flaechen"] = {};
		($("#areas_living").val().trim() == "" || $("#areas_apart_div").attr('style') == "display: none;") ?(isNull("flaechen.wohnflaeche")) ?false :openimmo.flaechen["wohnflaeche"] = null :(hasChanged(check,"flaechen","wohnflaeche", $("#areas_living").val().replace(",", "."))) ?openimmo.flaechen["wohnflaeche"] = Number($("#areas_living").val().replace(",", ".")) :false;
		($("#areas_use").val().trim() == "" || $("#areas_use_complete_rooms_div").attr('style') == "display: none;" || $("#areas_use_complete_div").attr('style') == "display: none;") ?(isNull("flaechen.nutzflaeche")) ?false :openimmo.flaechen["nutzflaeche"] = null :(hasChanged(check,"flaechen","nutzflaeche", $("#areas_use").val().replace(",", "."))) ?openimmo.flaechen["nutzflaeche"] = Number($("#areas_use").val().replace(",", ".")) :false;
		($("#areas_total").val().trim() == "" || $("#areas_use_complete_rooms_div").attr('style') == "display: none;" || $("#areas_use_complete_div").attr('style') == "display: none;") ?(isNull("flaechen.gesamtflaeche")) ?false :openimmo.flaechen["gesamtflaeche"] = null :(hasChanged(check,"flaechen","gesamtflaeche", $("#areas_total").val().replace(",", "."))) ?openimmo.flaechen["gesamtflaeche"] = Number($("#areas_total").val().replace(",", ".")) :false;
		($("#areas_base").val().trim() == "" || $("#areas_base_div").attr('style') == "display: none;") ?(isNull("flaechen.grundstuecksflaeche")) ?false :openimmo.flaechen["grundstuecksflaeche"] = null :(hasChanged(check,"flaechen","grundstuecksflaeche", $("#areas_base").val().replace(",", "."))) ?openimmo.flaechen["grundstuecksflaeche"] = Number($("#areas_base").val().replace(",", ".")) :false;
		($("#areas_rooms").val().trim() == "" || $("#areas_use_complete_rooms_div").attr('style') == "display: none;") ?(isNull("flaechen.anzahl_zimmer")) ?false :openimmo.flaechen["anzahl_zimmer"] = null :(hasChanged(check,"flaechen","anzahl_zimmer", $("#areas_rooms").val().replace(",", "."))) ?openimmo.flaechen["anzahl_zimmer"] = Number($("#areas_rooms").val().replace(",", ".")) :false;
		(hasChanged(check,"flaechen","anzahl_balkone", ($("#appointments_balcony").is(':checked')) ?1 :null)) ?openimmo.flaechen["anzahl_balkone"] = ($("#appointments_balcony").is(':checked')) ?1 :null :false;
	openimmo["ausstattung"] = {};
		openimmo.ausstattung["kueche"] = {};
			(hasChanged(check,"ausstattung.kueche", "EBK", ($("#appointments_ebk").is(':checked')) ?true :null)) ?(openimmo.ausstattung.kueche["EBK"] = ($("#appointments_ebk").is(':checked')) ?true :null) :false;
		(hasChanged(check,"ausstattung", "unterkellert", ($("#appointments_cellar").is(':checked')) ?$("#appointments_cellar").val() :null)) ?(openimmo.ausstattung["unterkellert"] = ($("#appointments_cellar").is(':checked')) ?$("#appointments_cellar").val() :null) :false;
		openimmo.ausstattung["bad"] = {};
			(hasChanged(check,"ausstattung.bad", "DUSCHE", ($("#appointments_bath_shower").is(':checked')) ?true :null)) ?(openimmo.ausstattung.bad["DUSCHE"] = ($("#appointments_bath_shower").is(':checked')) ?true :null) :false;
			(hasChanged(check,"ausstattung.bad", "WANNE", ($("#appointments_bath_tub").is(':checked')) ?true :null)) ?(openimmo.ausstattung.bad["WANNE"] = ($("#appointments_bath_tub").is(':checked')) ?true :null) :false;
			(hasChanged(check,"ausstattung.bad", "FENSTER", ($("#appointments_bath_window").is(':checked')) ?true :null)) ?(openimmo.ausstattung.bad["FENSTER"] = ($("#appointments_bath_window").is(':checked')) ?true :null) :false;
		(hasChanged(check,"ausstattung", "barrierefrei", ($("#appointments_accessible").is(':checked')) ?true :null)) ?(openimmo.ausstattung["barrierefrei"] = ($("#appointments_accessible").is(':checked')) ?true :null) :false;
		(hasChanged(check,"ausstattung", "rollstuhlgerecht", ($("#appointments_wheelchair").is(':checked')) ?true :null)) ?(openimmo.ausstattung["rollstuhlgerecht"] = ($("#appointments_wheelchair").is(':checked')) ?true :null) :false;
		openimmo.ausstattung["fahrstuhl"] = {};
			(hasChanged(check,"ausstattung.fahrstuhl", "PERSONEN", ($("#appointments_lift").is(':checked')) ?true :null)) ?(openimmo.ausstattung.fahrstuhl["PERSONEN"] = ($("#appointments_lift").is(':checked')) ?true :null) :false;
		openimmo.ausstattung["stellplatzart"] = {};
			(hasChanged(check,"ausstattung.stellplatzart", "FREIPLATZ", ($("#appointments_pitch").is(':checked')) ?true :null)) ?(openimmo.ausstattung.stellplatzart["FREIPLATZ"] = ($("#appointments_pitch").is(':checked')) ?true :null) :false;
		(hasChanged(check,"ausstattung", "kabel_sat_tv", ($("#appointments_tv").is(':checked')) ?true :null)) ?(openimmo.ausstattung["kabel_sat_tv"] = ($("#appointments_tv").is(':checked')) ?true :null) :false;
		(hasChanged(check,"ausstattung", "wasch_trockenraum", ($("#appointments_wash").is(':checked')) ?true :null)) ?(openimmo.ausstattung["wasch_trockenraum"] = ($("#appointments_wash").is(':checked')) ?true :null) :false; // Wohnberechtigungs / appointments_allownote under 'verwaltung_objekt'
	openimmo["geo"] = {};
		(hasChanged(check,"geo","strasse", $("#base_street").val())) ?openimmo.geo["strasse"] = $("#base_street").val() :false;
		($("#base_housenumber").val().trim() == "") ?(isNull("geo.hausnummer")) ?false :openimmo.geo["hausnummer"] = null :(hasChanged(check,"geo","hausnummer", $("#base_housenumber").val())) ?openimmo.geo["hausnummer"] = $("#base_housenumber").val() :false;
		(hasChanged(check,"geo","plz", $("#base_plz").val())) ?openimmo.geo["plz"] = Number($("#base_plz").val()) :false;
		(hasChanged(check,"geo","ort", $("#base_location").val())) ?openimmo.geo["ort"] = $("#base_location").val() :false;
		($("#description_floor").val().trim() == "" || $("#areas_floor_div").attr('style') == "display: none;") ?(isNull("geo.etage")) ?false :openimmo.geo["etage"] = null :(hasChanged(check,"geo","etage", $("#description_floor").val())) ?openimmo.geo["etage"] = Number($("#description_floor").val()) :false;
	openimmo["zustand_angaben"] = {};
		($("#energy_last").val().trim() == "") ?(isNull("zustand_angaben.letztemodernisierung")) ?false :openimmo.zustand_angaben["letztemodernisierung"] = null :(hasChanged(check,"zustand_angaben","letztemodernisierung", $("#energy_last").val().replace(",", "."))) ?openimmo.zustand_angaben["letztemodernisierung"] = Number($("#energy_last").val().replace(",", ".")) :false;
		($("#description_year").val().trim() == "" || $("#description_year_state_div").attr('style') == "display: none;") ?(isNull("zustand_angaben.baujahr")) ?false :openimmo.zustand_angaben["baujahr"] = null :(hasChanged(check,"zustand_angaben","baujahr", $("#description_year").val())) ?openimmo.zustand_angaben["baujahr"] = Number($("#description_year").val()) :false;
		($("#description_state").val() == "0" || $("#description_year_state_div").attr('style') == "display: none;") ?(isNull("zustand_angaben.zustand")) ?false :openimmo.zustand_angaben["zustand"] = null :(hasChanged(check,"zustand_angaben", "zustand", $("#description_state").val())) ?openimmo.zustand_angaben["zustand"] = $("#description_state").val() :false;
		if (hasChanged(check,"zustand_angaben.energiepass","epart", $("#energy_type").val()) || hasChanged(check,"zustand_angaben.energiepass","energieverbrauchkennwert", $("#energy_kwh").val()) || hasChanged(check,"zustand_angaben.energiepass","endenergiebedarf", $("#energy_kwh").val()) || hasChanged(check,"zustand_angaben.energiepass","primaerenergietraeger", $("#energy_deliverer").val()) || hasChanged(check,"zustand_angaben.energiepass","wertklasse", $("#energy_class").val())) {
			openimmo.zustand_angaben["energiepass"] = [{}];
				($("#energy_type").val() == "0") ?openimmo.zustand_angaben.energiepass[0]["epart"] = null :openimmo.zustand_angaben.energiepass[0]["epart"] = $("#energy_type").val();
				if ($("#energy_type").val() === "BEDARF" )
					openimmo.zustand_angaben.energiepass[0]["endenergiebedarf"] = $("#energy_kwh").val();
				else if ($("#energy_type").val() === "VERBRAUCH" )
					openimmo.zustand_angaben.energiepass[0]["energieverbrauchkennwert"] = $("#energy_kwh").val();
				($("#energy_deliverer").val() == "0") ? openimmo.zustand_angaben.energiepass[0]["primaerenergietraeger"] = null :openimmo.zustand_angaben.energiepass[0]["primaerenergietraeger"] = $("#energy_deliverer").val();
				($("#energy_class").val() == "0") ? openimmo.zustand_angaben.energiepass[0]["wertklasse"] = null :openimmo.zustand_angaben.energiepass[0]["wertklasse"] = $("#energy_class").val();
		}
	openimmo["freitexte"] = {};
		($("#description_title").val().trim() == "") ?(isNull("freitexte.objekttitel")) ?false :openimmo.freitexte["objekttitel"] = null :(hasChanged(check,"freitexte","objekttitel", $("#description_title").val())) ?openimmo.freitexte["objekttitel"] = $("#description_title").val() :false;
		($("#description_location").val().trim() == "") ?(isNull("freitexte.lage")) ?false :openimmo.freitexte["lage"] = null :(hasChanged(check,"freitexte","lage", $("#description_location").val())) ?openimmo.freitexte["lage"] = $("#description_location").val() :false;
		//($("#description_appointments").val().trim() == "") ?(isNull("freitexte.ausstatt_beschr")) ?false :openimmo.freitexte["ausstatt_beschr"] = null :(hasChanged(check,"freitexte","ausstatt_beschr", $("#description_appointments").val())) ?openimmo.freitexte["ausstatt_beschr"] = $("#description_appointments").val() :false;
		($("#description_description").val().trim() == "") ?(isNull("freitexte.objektbeschreibung")) ?false :openimmo.freitexte["objektbeschreibung"] = null :(hasChanged(check,"freitexte","objektbeschreibung", $("#description_description").val())) ?openimmo.freitexte["objektbeschreibung"] = $("#description_description").val() :false;
		 ($("#description_other").val().trim() == "") ?(isNull("freitexte.sonstige_angaben")) ?false :openimmo.freitexte["sonstige_angaben"] = null :(hasChanged(check,"freitexte","sonstige_angaben", $("#description_other").val())) ?openimmo.freitexte["sonstige_angaben"] = $("#description_other").val() :false;
	openimmo["objektkategorie"] = {};
		openimmo.objektkategorie["nutzungsart"] = {};
			(hasChanged(check,"objektkategorie.nutzungsart", "GEWERBE", false)) ?openimmo.objektkategorie.nutzungsart["GEWERBE"] = false :false;
			(hasChanged(check,"objektkategorie.nutzungsart", "WOHNEN", true)) ?openimmo.objektkategorie.nutzungsart["WOHNEN"] = true :false;
		openimmo.objektkategorie["objektart"] = {};
			if ($('input[name=kindexpose]:checked').val() == "0") { // Wohnung
				if (hasChanged(check,"objektkategorie.objektart","wohnung", $("#object_apart").val())) {
					openimmo.objektkategorie.objektart["wohnung"] = [{}];
						openimmo.objektkategorie.objektart.wohnung[0] = ($("#object_apart").val() != '0') ?$("#object_apart").val() :null;
				}
			} else if ($('input[name=kindexpose]:checked').val() == "1") { // Haus
				if (hasChanged(check,"objektkategorie.objektart","haus", $("#object_house").val())) {
					openimmo.objektkategorie.objektart["haus"] = [{}];
						openimmo.objektkategorie.objektart.haus[0] = ($("#object_house").val() != '0') ?$("#object_house").val() :null;
				}
			} else if ($('input[name=kindexpose]:checked').val() == "2") { // Grundstück
				openimmo.objektkategorie.objektart["grundstueck"] = [{}];
			}
		openimmo.objektkategorie["vermarktungsart"] = {};
			(hasChanged(check,"objektkategorie.vermarktungsart","KAUF", $('input[name=kindmarketing]:checked').val() == "KAUF")) ?openimmo.objektkategorie.vermarktungsart["KAUF"] = ($('input[name=kindmarketing]:checked').val() == "KAUF") ?true :false :false;					
			(hasChanged(check,"objektkategorie.vermarktungsart","MIETE_PACHT", $('input[name=kindmarketing]:checked').val() == "MIETE_PACHT")) ?openimmo.objektkategorie.vermarktungsart["MIETE_PACHT"] = ($('input[name=kindmarketing]:checked').val() == "MIETE_PACHT") ?true :false :false;
	openimmo["verwaltung_objekt"] = {};
		($("#description_free").val().trim() == "") ?(isNull("verwaltung_objekt.verfuegbar_ab")) ?false :openimmo.verwaltung_objekt["verfuegbar_ab"] = null :(hasChanged(check,"verwaltung_objekt","verfuegbar_ab", $("#description_free").val())) ?openimmo.verwaltung_objekt["verfuegbar_ab"] = $("#description_free").val() :false;
		(hasChanged(check,"verwaltung_objekt","objektadresse_freigeben", $('input[name=address_show]:checked').val() == "true")) ?openimmo.verwaltung_objekt["objektadresse_freigeben"] = $('input[name=address_show]:checked').val() == "true" :false;
		(hasChanged(check,"verwaltung_objekt","wbs_sozialwohnung", $("#appointments_allownote").is(':checked'))) ?openimmo.verwaltung_objekt["wbs_sozialwohnung"] = $("#appointments_allownote").is(':checked') :false;
	openimmo["verwaltung_techn"] = {};
		($("#base_objectnumber").val().trim() != "" && hasChanged(check,"verwaltung_techn","objektnr_extern", $("#base_objectnumber").val())) ?openimmo.verwaltung_techn["objektnr_extern"] = $("#base_objectnumber").val() :false;
		openimmo.verwaltung_techn["stand_vom"] = date_str;
		openimmo.verwaltung_techn["weitergabe_positiv"] = [];
			if ($("#activation_homepage").is(':checked'))
				openimmo.verwaltung_techn.weitergabe_positiv.push('immobrowse');
			if ($("#activation_immoscout").is(':checked'))
				openimmo.verwaltung_techn.weitergabe_positiv.push('immoscout24');
			if ($("#activation_immowelt").is(':checked'))
				openimmo.verwaltung_techn.weitergabe_positiv.push('immowelt');
			if ($("#activation_hba").is(':checked'))
				openimmo.verwaltung_techn.weitergabe_positiv.push('hba');
			if ($("#activation_breba").is(':checked'))
				openimmo.verwaltung_techn.weitergabe_positiv.push('breba');

			openimmo.verwaltung_techn["aktiv_von"] = null;
			openimmo.verwaltung_techn["aktiv_bis"] = null;
			
			/*
			if (openimmo.verwaltung_techn.weitergabe_positiv.length > 0) {
				openimmo.verwaltung_techn["aktiv_von"] = "1970-01-01";
				openimmo.verwaltung_techn["aktiv_bis"] = "1970-01-01";
			} else {
				openimmo.verwaltung_techn["aktiv_von"] = null;
				openimmo.verwaltung_techn["aktiv_bis"] = null;
			}
			*/

	openimmo["barrier_freeness"] = {};
		($("#barrier_freeness_stairs").val() == "-1") ?(isNull("barrier_freeness.stairs")) ?false :openimmo.barrier_freeness["stairs"] = null :(hasChanged(check,"barrier_freeness","stairs", $("#barrier_freeness_stairs").val())) ?openimmo.barrier_freeness["stairs"] = $("#barrier_freeness_stairs").val() :false;
		openimmo.barrier_freeness["entry"] = {};
			($("#barrier_freeness_entry_ramp").val() == "0") ?(isNull("barrier_freeness.entry.ramp_din")) ?false :openimmo.barrier_freeness.entry["ramp_din"] = null :(hasChanged(check,"barrier_freeness.entry","ramp_din", $("#barrier_freeness_entry_ramp").val() == "true")) ?openimmo.barrier_freeness.entry["ramp_din"] = $("#barrier_freeness_entry_ramp").val() == "true" :false;
			(hasChanged(check,"barrier_freeness.entry","doorbell_panel", $("#barrier_freeness_entry_bell").is(':checked'))) ?openimmo.barrier_freeness.entry["doorbell_panel"] = $("#barrier_freeness_entry_bell").is(':checked') :false;
			(hasChanged(check,"barrier_freeness.entry","door_opener", $("#barrier_freeness_door_opener").is(':checked'))) ?openimmo.barrier_freeness.entry["door_opener"] = $("#barrier_freeness_door_opener").is(':checked') :false;
			(hasChanged(check,"barrier_freeness.entry","intercom", $("#barrier_freeness_intercom").is(':checked'))) ?openimmo.barrier_freeness.entry["intercom"] = $("#barrier_freeness_intercom").is(':checked') :false;
		(hasChanged(check,"barrier_freeness","wide_door", $("#barrier_freeness_wide_door").is(':checked'))) ?openimmo.barrier_freeness["wide_door"] = $("#barrier_freeness_wide_door").is(':checked') :false;
		(hasChanged(check,"barrier_freeness","low_thresholds", $("#barrier_freeness_low_thresholds").is(':checked'))) ?openimmo.barrier_freeness["low_thresholds"] = $("#barrier_freeness_low_thresholds").is(':checked') :false;
		(hasChanged(check,"barrier_freeness","wide_doors", $("#barrier_freeness_wide_doors").is(':checked'))) ?openimmo.barrier_freeness["wide_doors"] = $("#barrier_freeness_wide_doors").is(':checked') :false;
		openimmo.barrier_freeness["lift"] = {};
			(hasChanged(check,"barrier_freeness.lift","wide_door", ($("#barrier_freeness_liftsize").is(':checked')) ?true :false)) ?openimmo.barrier_freeness.lift["wide_door"] = $("#barrier_freeness_liftsize").is(':checked') :false;
			($("#barrier_freeness_liftcarsize").val() == "0") ?(isNull("barrier_freeness.lift.value")) ?false :openimmo.barrier_freeness.lift["value"] = null :(hasChanged(check,"barrier_freeness.lift","value", $("#barrier_freeness_liftcarsize").val())) ?openimmo.barrier_freeness.lift["value"] = $("#barrier_freeness_liftcarsize").val() :false;
		openimmo.barrier_freeness["bath"] = {};
			(hasChanged(check,"barrier_freeness.bath","bathtub", $("#barrier_freeness_bath_tub").is(':checked'))) ?openimmo.barrier_freeness.bath["bathtub"] = $("#barrier_freeness_bath_tub").is(':checked') :false;
			//(hasChanged(check,"barrier_freeness.bath","shower", $("#barrier_freeness_bath_shower").is(':checked'))) ?openimmo.barrier_freeness.bath["shower"] = $("#barrier_freeness_bath_shower").is(':checked') :false;
			(hasChanged(check,"barrier_freeness.bath","wide", $("#barrier_freeness_bath_wide").is(':checked'))) ?openimmo.barrier_freeness.bath["wide"] = $("#barrier_freeness_bath_wide").is(':checked') :false;
			(hasChanged(check,"barrier_freeness.bath","large", $("#barrier_freeness_bath_large").is(':checked'))) ?openimmo.barrier_freeness.bath["large"] = $("#barrier_freeness_bath_large").is(':checked') :false;
			($("#barrier_freeness_bath_shower").is(':checked') == false) ?(isNull("barrier_freeness.bath.shower_tray")) ?false :openimmo.barrier_freeness.bath["shower_tray"] = null :(hasChanged(check,"barrier_freeness.bath","shower_tray", $("#barrier_freeness_bath_shower_tray").val())) ?openimmo.barrier_freeness.bath["shower_tray"] = $("#barrier_freeness_bath_shower_tray").val() :false;
		openimmo.barrier_freeness["balcony"] = {};
			(hasChanged(check,"barrier_freeness.balcony","wide_door", $("#barrier_freeness_balcony_wide_door").is(':checked'))) ?openimmo.barrier_freeness.balcony["wide_door"] = $("#barrier_freeness_balcony_wide_door").is(':checked') :false;
			(hasChanged(check,"barrier_freeness.balcony","large", $("#barrier_freeness_balcony_large").is(':checked'))) ?openimmo.barrier_freeness.balcony["large"] = $("#barrier_freeness_balcony_large").is(':checked') :false;
			($("#barrier_freeness_balcony_threshold").val() == "0") ?(isNull("barrier_freeness.balcony.threshold")) ?false :openimmo.barrier_freeness.balcony["threshold"] = null :(hasChanged(check,"barrier_freeness.balcony","threshold", $("#barrier_freeness_balcony_threshold").val() == "true")) ?openimmo.barrier_freeness.balcony["threshold"] = $("#barrier_freeness_balcony_threshold").val() == "true" :false;
		($("#barrier_freeness_balcony_wheelchairparking").val() == "0") ?(isNull("barrier_freeness.wheelchair_parking")) ?false :openimmo.barrier_freeness["wheelchair_parking"] = null :(hasChanged(check,"barrier_freeness","wheelchair_parking", $("#barrier_freeness_balcony_wheelchairparking").val())) ?openimmo.barrier_freeness["wheelchair_parking"] = $("#barrier_freeness_balcony_wheelchairparking").val() :false;

	// For the preview, to show images if available
	if (!check && _openImmo_json != null && _openImmo_json.hasOwnProperty('anhaenge'))
		openimmo["anhaenge"] = _openImmo_json.anhaenge;
		
	//openimmo["user_defined_simplefield"] = [{}];
	//openimmo.user_defined_simplefield[0]["feldname"] = "feld1";
	//openimmo.user_defined_simplefield[0]["value"] = "feld1 99";
	
	//console.log("openimmo: " + JSON.stringify(openimmo));
	// Delete empty objects {}
	$.each(openimmo, function(key, value) {
		$.each(openimmo[key], function(key2, value2) { // Delete subkeys; problem: it's deleting normal key/values in each subnode
			if (jQuery.isEmptyObject(value2) && typeof value2 === "object" && value2 != null) {
				delete openimmo[key][key2];
			}
		});
		if (jQuery.isEmptyObject(value) && typeof value === "object") {
			delete openimmo[key];
			//console.log("DELETED " + key);
		}
	});
	//console.log("openimmo: " + JSON.stringify(openimmo));
	return openimmo;
	
}
function hideAll() {
	// Objecttype
	$("#object_apart").hide();
	$("#object_house").hide();
	$("#object_base").hide();
	
	// Tabs
	$("#areas_floor_div").hide();
	$("#areas_apart_div").hide();
	$("#areas_base_div").hide();
	 
	$("#description_year_state_div").hide();
	
	$("#areas_use_complete_div").show();
}

function removeSidebarComponents(click) {
	$("#nav_startpage").hide();
	$("#nav_create_expose").hide();
	$("#nav_manage_exposes").hide();
	$('#startpage_link').removeAttr('style');
	$('#create_expose_link').removeAttr('style');
	$('#manage_exposes_link').removeAttr('style');
	click.children("a").attr('style', 'background-color: #428bca; color: white;');
}

function setSpeech(speech) {
	if (speech == "english") {
		document.getElementById("startpage_link").innerHTML = '<i class="fa fa-home fa-fw"></i> Startpage';
		document.getElementById("create_expose_link").innerHTML = '<i class="fa fa-circle-thin fa-fw"></i> Create realestate';
		document.getElementById("manage_exposes_link").innerHTML = '<i class="fa fa-users fa-fw"></i> Manage realestates';
	} else if (speech == "german") {
		document.getElementById("startpage_link").innerHTML = '<i class="fa fa-home fa-fw"></i> Startseite';
		document.getElementById("create_expose_link").innerHTML = '<i class="fa fa-circle-thin fa-fw"></i> Immobilie anlegen';
		document.getElementById("manage_exposes_link").innerHTML = '<i class="fa fa-users fa-fw"></i> Immobilien verwalten';
	}
	
	
}

function checkSession() {
	$('#pageloader').show();
	$.ajax({
		timeout: 5000,
		url: "https://his.homeinfo.de/session/" +  localStorage.getItem("token"),
		type: "GET",
		success: function (msg) {
			//console.log("Success " + msg);
			//console.log("Success " + msg.token)
			if (msg.token != localStorage.getItem("token")) {
				window.location.href = "login.html";
			} else {
				$("#page").show();
				$("#sessiontime").html('<font size="2" color="#bbb">Sitzung läuft ab <br>um ' + msg.end.substring(11,16) + '</font>');
			}
		},
		complete: function (msg) {
			$('#pageloader').hide();
		},
		error: function (msg) { // EXPIRED
			window.location.href = "login.html";
		}
	});
}


// Recreate/Stay Session
function holdSession() {
	$('#pageloader').show();
	$.ajax({
		url: "https://his.homeinfo.de/session/" +  localStorage.getItem("token") + '?duration=30', //?duration=5 // max 5min - 30min; default: 15min
		type: "PUT",
		success: function (msg) {
			localStorage.setItem("token", msg.token);
			$("#sessiontime").html('<font size="2" color="#bbb">Sitzung läuft ab <br>um ' + msg.end.substring(11, 16) + '</font>');
		},
		complete: function(msg) {
			$('#pageloader').hide();
		},
		error: function (msg) { // EXPIRED
			if (msg.statusText == "Gone" ) {
				window.location.href = "login.html"; // Disable for testing without login
			}
		},
	});
}

function getAllContacts() {
	$.ajax({
		url: "https://backend.immobit.de/contacts?session=" + localStorage.getItem("token"),
		type: "GET",
		success: function (msg) {
			//console.log(JSON.stringify(msg));
			$('#contact_available').html($('<option>', {
				value: -1,
				text: 'Vorhandene Kontaktdaten'
			}));
			
			var notAvailable;
			for (var i = 0; i < msg.length; i++) {
				notAvailable = true;
				$('#contact_available option').each(function() {
					if (((msg[i].vorname == undefined) ?"" :msg[i].vorname) + ' ' + ((msg[i].name == undefined) ?"" :msg[i].name) + ' ' + ((msg[i].strasse == undefined) ?"" :", " + msg[i].strasse) == $(this).text()) {
						notAvailable = false;
						return false;
					}
				});
				if (notAvailable) {
					$('#contact_available').append($('<option>', {
						value: i,
						text: ((msg[i].vorname == undefined) ?"" :msg[i].vorname) + ' ' + ((msg[i].name == undefined) ?"" :msg[i].name) + ' ' + ((msg[i].strasse == undefined) ?"" :", " + msg[i].strasse)
					}));
				}
			}
			$('#contact_available').change(function() {
				if ($(this).val() > -1) {
					if (msg[$(this).val()].hasOwnProperty('anrede')) 
						$("#contact_title").val(msg[$(this).val()].anrede);
					else
						$("#contact_title").val("0");
					$("#contact_firstname").val(msg[$(this).val()].vorname);
					$("#contact_familyname").val(msg[$(this).val()].name);
					$("#contact_email").val(msg[$(this).val()].email_direkt);
					$("#contact_phone").val(msg[$(this).val()].tel_durchw);
					$("#contact_company").val(msg[$(this).val()].firma);
					$("#contact_street").val(msg[$(this).val()].strasse);
					$("#contact_housenumber").val(msg[$(this).val()].hausnummer);
					$("#contact_plz").val(msg[$(this).val()].plz);
					$("#contact_location").val(msg[$(this).val()].ort);
					$("#contact_url").val(msg[$(this).val()].url);
				}
			});
		},
		error: function (msg) {
			var parsed = JSON.parse(JSON.stringify(msg));
		}
	});
}
// Manage realestates
function getAllRealEstates(page = 0, sorting = "normal", reverse = false) {
	$("#loader_manage").show();
	$("#realestates").html("");
	$.ajax({
		url: "https://backend.immobit.de/realestates?session=" +localStorage.getItem("token"),
		type: "GET",
		success: function (msg) {
			//console.log(JSON.stringify(msg));
			_openImmo_json = msg;
			loadRealEstates(page, sorting, reverse);
		},
		error: function (msg) {
			try {
				var parsed = JSON.parse(JSON.stringify(msg));
				//console.log("ERROR " + JSON.stringify(msg));
				$("#loader_manage").hide();
				if (msg.statusText == "Kein solcher Dienst.")
					$("#realestates").html('<font size="4" color="#FF0000">Dienst nicht aktiv, bitte versuchen Sie es später noch einmal.</font>');
				else if (parsed.responseJSON.message == "Zugriff verweigert.")
					$("#realestates").html('Sie haben leider nicht die Berechtigung Immobilien anzuzeigen.');				
				else
					$("#realestates").html("Keine Immobilien vorhanden");
			} catch (e) {
				console.log("TOTAL ERROR " + e);
				$("#realestates").html('<font size="4" color="#FF0000">Dienst nicht aktiv, bitte versuchen Sie es später noch einmal.</font>');
			}
		}
	});	
}

function loadRealEstates(page = 0, sorting = "normal", reverse = false) {
	try {
		_deleteRealEstates = [];
		$("#realestatesDelete").hide();
		var frontAndBackRealEstates = '';
		var limit = ($("#count_realestates").val() == "all" || $("#count_realestates").val() == undefined) ?_openImmo_json.length :$("#count_realestates").val();
		var activesort = $("#show_realestates").val();
		var counter = 0;

		// Filter / Searchfield
		var openImmoFiltered = [];
		for (var i = 0; i < _openImmo_json.length; i++) {
			if (showRealEstateBySearch(_openImmo_json[i]) && ((showRealEstateBySelection(_openImmo_json[i]) && activesort === 'active') || (!showRealEstateBySelection(_openImmo_json[i]) && activesort === 'not_active') || activesort === 'all')) {
				openImmoFiltered[counter] = _openImmo_json[i];
				counter++;
			}
		}
		
		// Calculate pages
		page = (page > 0 && (openImmoFiltered.length / limit) <= page) ?page-1 :page;
		_page = page;
		if (openImmoFiltered.length / limit > 1) {
			for (var i = 0; i < openImmoFiltered.length / limit; i++) {
				if (i == page)
					frontAndBackRealEstates += '<a href="#" class="page" data-id="' + i + '" data-sorting="' + sorting + '" data-reverse="' + reverse + '"><font size="4"><u> ' + (i+1) + '</u></font></a> ';
				else
					frontAndBackRealEstates += '<a href="#" class="page" data-id="' + i + '" data-sorting="' + sorting + '" data-reverse="' + reverse + '"><font size="4"> ' + (i+1) + '</font></a> ';
			}
		}

		// Sorting
		if (sorting != "normal")
			openImmoFiltered.sort(sortBy(sorting, reverse));
		
		// Build only visible page
		var realEstatesForPage = limit * page;
		var maximumRealEstates = (Number(realEstatesForPage) + Number(limit) > openImmoFiltered.length) ?openImmoFiltered.length :Number(realEstatesForPage) + Number(limit);
		counter = 0;
		var msg = [];
		for (var i = realEstatesForPage; i < maximumRealEstates; i++) {
			msg[counter] = openImmoFiltered[i];
			counter++;
		}

		//console.log(JSON.stringify(msg));
		//console.log("Success " + JSON.stringify(msg.reverse())); // Give out whole object as string
		var realEstates = '\
			<tr>\
				<div class="input-group">\
					<td align="center">\
					<a href="#" class="sortbyNumber">#</a>\
					</td>\
					<td width="20%">\
						<a href="#" class="sortbyObjektnummer" style="padding-left:12px">Objektnummer</a>\
					</td>\
					<td width="15%">\
						<a href="#" class="sortbyObjektart" style="padding-left:12px">Objektart</a>\
					</td>\
					<td width="15%">\
						<a href="#" class="sortbyVermarktungsart" style="padding-left:12px">Vermarktungsart</a>\
					</td>\
					<td width="5%">\
						<a href="#" class="sortbyAdresse" style="padding-left:12px">Adresse</a>\
					</td>\
					<td width="15%" style="padding-left:12px">\
						Geändert\
					</td>\
					<td align="center" style="white-space: nowrap; padding-left:12px">\
						Funktionen\
					</td>\
					<td align="center"> \
						Aktivierung <span class="fa fa-info-circle" data-toggle="tooltip" title="Sind Sie bei den Portalen schon registiert? Sprechen Sie uns an!" style="cursor: pointer; margin-left: 5px"></span>\
					</td>\
				</div>\
			</tr>'
		
		for (var i = 0; i < counter; i++) {
			var objektart;
			var vermarktungsart;
			var checkedImmobrowse = '';
			var checkedImmoscout24 = '';
			var checkedImmowelt = '';
			var checkedHBA = '';
			var checkedBREBA = '';
			if (Object.keys(msg[i].objektkategorie.objektart)[0] == "wohnung")
				objektart = "Wohnung";
			else if (Object.keys(msg[i].objektkategorie.objektart)[0] == "haus")
				objektart = "Haus";
			else if (Object.keys(msg[i].objektkategorie.objektart)[0] == "grundstueck")
				objektart = "Grundstück";
			else
				objektart = "Unbekannt";
			if (msg[i].objektkategorie.vermarktungsart.KAUF == true)
				vermarktungsart = "Kaufobjekt";
			else if (msg[i].objektkategorie.vermarktungsart.MIETE_PACHT == true)
				vermarktungsart = "Mietobjekt";
			else 
				vermarktungsart = "Unbekannt";
			//if (!isOnDate(msg[i].verwaltung_techn["aktiv_von"], msg[i].verwaltung_techn["aktiv_bis"]))
				//checked = "";
			if (msg[i].verwaltung_techn.hasOwnProperty('weitergabe_positiv')) {
				for (var positivcounter = 0; positivcounter < msg[i].verwaltung_techn.weitergabe_positiv.length; positivcounter++) {
					if (msg[i].verwaltung_techn.weitergabe_positiv[positivcounter] === 'immobrowse')
						checkedImmobrowse = "checked";
					else if (msg[i].verwaltung_techn.weitergabe_positiv[positivcounter] === 'immoscout24')
						checkedImmoscout24 = "checked";
					else if (msg[i].verwaltung_techn.weitergabe_positiv[positivcounter] === 'immowelt')
						checkedImmowelt = "checked";
					else if (msg[i].verwaltung_techn.weitergabe_positiv[positivcounter] === 'hba')
						checkedHBA = "checked";
					else if (msg[i].verwaltung_techn.weitergabe_positiv[positivcounter] === 'breba')
						checkedBREBA = "checked";
				}
			}
			var customerPortals = '';
			if (_portals !== null) {
				for (var portal = 0; portal < _portals.length; portal++) {
					if (_portals[portal] === 'immobrowse')
						customerPortals += 'Homepage <input type="checkbox" value="" class="btn_check_active" id="immobrowse" data-id="' + i + '"' + checkedImmobrowse + '>';
					else if (_portals[portal] === 'immoscout24')
						customerPortals += '<font color="#ff7500" style="padding-left:10px">IS24 </font><input type="checkbox" value="" class="btn_check_active" id="immoscout24" data-id="' + i + '"' + checkedImmoscout24 + '>';
					else if (_portals[portal] === 'immowelt')
						customerPortals += '<font color="#00aae1" style="padding-left:10px">Immowelt </font><input type="checkbox" value="" class="btn_check_active" id="immowelt" data-id="' + i + '"' + checkedImmowelt + '>';
					else if (_portals[portal] === 'hba')
						 customerPortals += '<font color="#00aae1" style="padding-left:10px">Barrierefrei Hannover </font><input type="checkbox" value="" class="btn_check_active" id="hba" data-id="' + i + '"' + checkedHBA + '>';
					else if (_portals[portal] === 'breba')
						customerPortals += '<font color="#00aae1" style="padding-left:10px">Barrierefrei Bremen </font><input type="checkbox" value="" class="btn_check_active" id="breba" data-id="' + i + '"' + checkedBREBA + '>';
				}
			}

			realEstates += '\
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
		}
		
		if (counter == 0)
			$("#realestates").html("Keine Immobilien vorhanden ");
		else
			$("#realestates").html(frontAndBackRealEstates + '<table class="table-curved" background-color:#FFF">' + realEstates + '</table><br>' + frontAndBackRealEstates + '<br><br>');
		$('[data-toggle="tooltip"]').tooltip();
		$('.page').click(function(){
			loadRealEstates($(this).data("id"), $(this).data("sorting"), $(this).data("reverse"));
		});

		$('.sortbyNumber').click(function() {
			loadRealEstates();
		});
		$('.sortbyObjektnummer').click(function() {
			loadRealEstates(page, "verwaltung_techn.objektnr_extern", !reverse);
		});
		$('.sortbyObjektart').click(function() {
			loadRealEstates(page, "objektkategorie.objektart", !reverse);
		});
		$('.sortbyVermarktungsart').click(function() {
			loadRealEstates(page, "objektkategorie.vermarktungsart.KAUF", !reverse);
		});
		$('.sortbyAdresse').click(function() {
			loadRealEstates(page, "geo.strasse", !reverse);
		});
		
		$('.markrealestate').click(function(){
			if ($(this).parent().find(".markfirst").attr("style") != "min-width:50px; text-align:center; border-radius:0; pointer-events:none; background-color:#e2e2e2;") {
				_deleteRealEstates.push($(this).parent().find(".markrealestate").data("id"));
				$(this).parent().find(".markfirst").attr("style","min-width:50px; text-align:center; border-radius:0; pointer-events:none; background-color:#e2e2e2;");
				$(this).parent().find(".markgroup").attr("style","width:100%; text-align:left; border-radius:0; pointer-events:none; background-color:#e2e2e2;");
			} else {
				_deleteRealEstates.splice(_deleteRealEstates.indexOf($(this).parent().find(".markrealestate").data("id")), 1);
				$(this).parent().find(".markfirst").attr("style","min-width:50px; text-align:center; border-radius:0; pointer-events:none; background-color:none;");
				$(this).parent().find(".markgroup").attr("style","width:100%; text-align:left; border-radius:0; pointer-events:none; background-color: none;");				
			}
			if (_deleteRealEstates.length > 0)
				$("#realestatesDelete").show();
			else
				$("#realestatesDelete").hide();
		});
		
		$('.btn_manage, .btn_preview_manage').click(function() {
			holdSession();
			$("#loader_new").show();
			var preview = $(this).data('preview');
			if (preview != true) {			
				$("#content_title").html('<h1>Immobilie bearbeiten</h1>'); //$("#content_title").html('<h1>Immobilie bearbeiten</h1><font size="4" color="#FF0000">Immobilie wird geladen...');
				defaultAndDeleteAllObjectFields();
				$("#managedcontainer").hide();
				$("#nav_manage_exposes").hide();
				$("#nav_create_expose").show();
				$(".btn_back").show();
				$(".btn_delete").show();
			}
			var id = msg[$(this).data("id")].id;
			$.ajax({
				url: "https://backend.immobit.de/realestates/" + id + "?session=" +  localStorage.getItem("token"),
				type: "GET",
				success: function (msg) {
					//console.log(JSON.stringify(msg));
					$("#loader_new").hide(); //$("#content_title").html('<h1>Immobilie bearbeiten</h1>');
					_openImmo_json = msg;
					if (preview == true) {
						showpreview(_openImmo_json);
					} else {
						setFields();
						$("#managedcontainer").show();
					}
				},
				error: function (msg) {
					console.log("ERROR " + JSON.stringify(msg));
					$("#loader_new").hide();
					$("#content_title").html('<h1>Immobilie bearbeiten</h1><font size="4" color="#FF0000">Beim Laden dieser Immobilie ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.');
				}
			});
		});	
		
		$('.btn_clone_object').click(function() {
			$("#loader_manage").show();
			var id = msg[$(this).data("id")].id;
			var objektnr_extern = msg[$(this).data("id")].verwaltung_techn.objektnr_extern;
			var sorting = $(this).data("sorting");
			var reverse = $(this).data("reverse");
			$.ajax({
				url: "https://backend.immobit.de/realestates/" + id + "?session=" +  localStorage.getItem("token"),
				type: "GET",
				success: function (msg) {
					_openImmo_json = msg;
					var date = new Date();
					_openImmo_json.verwaltung_techn.objektnr_extern = getUuid();
					_openImmo_json.verwaltung_techn.stand_vom = date.getFullYear() + '-' + ('0'+(date.getMonth()+1)).substr(-2,2) + '-' + ('0'+date.getDate()).substr(-2,2);
					$.ajax({
						url: "https://backend.immobit.de/realestates?session=" + localStorage.getItem("token"),
						type:  "POST",
						data: JSON.stringify(_openImmo_json),
						success: function (msg) {
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#000">Die Immobilie <font size="4" color="#159f18">' + objektnr_extern + '</font> wurde erfolgreich unter der Nummer: <font size="4" color="#159f18">' + _openImmo_json.verwaltung_techn.objektnr_extern + '</font> dupliziert.');
							holdSession();
							getAllRealEstates(_page, sorting, reverse);
						},
						error: function (msg) {
							console.log("ERROR " + JSON.stringify(msg));
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#FF0000">Beim Duplizieren der Immobilie ' + objektnr_extern + ' ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.</font>');
							$("#loader_manage").hide();
						}
					});						
					
				},
				error: function (msg) {
					console.log("ERROR " + JSON.stringify(msg));
					$("#loader_manage").hide();
					$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#FF0000">Beim Duplizieren der Immobilie ' + objektnr_extern + ' ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.</font>');
				}
			});
		});	
		
		$('.btn_delete_object').click(function() {
			var id = $(this).data("id");
			var sorting = $(this).data("sorting");
			var reverse = $(this).data("reverse");			
			_openImmo_json = msg[id];
			swal({
				title: "Sind Sie sicher?",
				text: "Wollen Sie die Immobilie <span style='color:#5cb85c;'>" + _openImmo_json.verwaltung_techn.objektnr_extern + "</span> wirklich löschen?",
				type: "warning",
				showCancelButton: true,
				html: true,
				confirmButtonColor: "#5bb75b",
				confirmButtonText: "Ja!",
				cancelButtonText: "Nein",
				closeOnConfirm: true,
				closeOnCancel: true
			},
			function(isConfirm) {
				if (isConfirm) {
					$("#loader_manage").show();
					//for (i=0; i < msg.length; i++) { // delete all
					$.ajax({
						url: "https://backend.immobit.de/realestates/" + _openImmo_json.id + "?session=" +  localStorage.getItem("token"),
						type: "DELETE",
						success: function (msg) {
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#000">Die Immobilie <font size="4" color="#FF0000">' + _openImmo_json.verwaltung_techn.objektnr_extern + '</font> wurde gelöscht.');
							holdSession();
							getAllRealEstates(_page, sorting, reverse);
						},
						error: function (msg) {
							$("#loader_manage").hide();
							console.log("ERROR " + JSON.stringify(msg));
							$("#manage_title").html('<h1>Immobilien verwalten</h1><font size="4" color="#FF0000">Beim Löschen der Immobilie ' + id + ' ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut.</font>');
						}
					});
					//}
				}
			});
		});
		
		$('.btn_check_active').click(function() {
			var openImmo_json = {};
			openImmo_json["verwaltung_techn"] = {};
			var id = msg[$(this).data("id")].id;
			openImmo_json.verwaltung_techn.weitergabe_positiv = [];
			msg[$(this).data("id")].verwaltung_techn["weitergabe_positiv"] = [];
			if ($(this).parent().find('#immobrowse').is(':checked')) {
				openImmo_json.verwaltung_techn.weitergabe_positiv.push('immobrowse');
				msg[$(this).data("id")].verwaltung_techn.weitergabe_positiv.push('immobrowse');
			}
			if ($(this).parent().find('#immoscout24').is(':checked')) {
				openImmo_json.verwaltung_techn.weitergabe_positiv.push('immoscout24');
				msg[$(this).data("id")].verwaltung_techn.weitergabe_positiv.push('immoscout24');
			}
			if ($(this).parent().find('#immowelt').is(':checked')) {
				openImmo_json.verwaltung_techn.weitergabe_positiv.push('immowelt');
				msg[$(this).data("id")].verwaltung_techn.weitergabe_positiv.push('immowelt');
			}
			if ($(this).parent().find('#hba').is(':checked')) {
				openImmo_json.verwaltung_techn.weitergabe_positiv.push('hba');
				msg[$(this).data("id")].verwaltung_techn.weitergabe_positiv.push('hba');
			}
			if ($(this).parent().find('#breba').is(':checked')) {
				openImmo_json.verwaltung_techn.weitergabe_positiv.push('breba');
				msg[$(this).data("id")].verwaltung_techn.weitergabe_positiv.push('breba');
			}
			var date = new Date();
			openImmo_json.verwaltung_techn.stand_vom = date.getFullYear() + '-' + ('0'+(date.getMonth()+1)).substr(-2,2) + '-' + ('0'+date.getDate()).substr(-2,2);
			if (openImmo_json.verwaltung_techn.weitergabe_positiv.length > 0) {
				openImmo_json.verwaltung_techn["aktiv_von"] = null;
				openImmo_json.verwaltung_techn["aktiv_bis"] = null;
			} else {
				openImmo_json.verwaltung_techn["aktiv_von"] = "1970-01-01";
				openImmo_json.verwaltung_techn["aktiv_bis"] = "1970-01-01";
			}
			//console.log(JSON.stringify(openImmo_json));
			$.ajax({
				url: "https://backend.immobit.de/realestates/" + id + "?session=" + localStorage.getItem("token"),
				type:  "PATCH",
				data: JSON.stringify(openImmo_json),
				success: function (msg) {
				},
				error: function (msg) {
					console.log("ERROR " + JSON.stringify(msg));
				}
			});
		});
	} catch (e) {
		console.log("EXCEPTION(loadRealEstates): " + e);
		$("#realestates").html('<font size="4" color="#FF0000">Leider ist ein Fehler aufgetreten. Bitte kontaktieren Sie den Betreiber dieser Seite.</font>');
	}
	$("#loader_manage").hide();
}

function getImages() {
	if (_imagesTitles.length == 0) {
		if (_openImmo_json != null && _openImmo_json.hasOwnProperty('anhaenge')) {
			var initialPreviewConfigArray = new Array();
			var initialPreviewArray = new Array();
			for (var i = 0; i < _openImmo_json.anhaenge.anhang.length; i++) {
				initialPreviewConfigArray[i] = {caption: _openImmo_json.anhaenge.anhang[i].anhangtitel, size: "", width: "120px", key: i, showDrag: false, group: _openImmo_json.anhaenge.anhang[i].gruppe};
				initialPreviewArray[i] = "https://backend.immobit.de/attachments/" + _openImmo_json.anhaenge.anhang[i].id + "?session=" + localStorage.getItem("token");
			}
				
			$("#files-upload-input").html('<input id="files-upload" name="filesupload[]" type="file" multiple class="file-loading">');
			// Source: http://plugins.krajee.com/file-advanced-usage-demo
			_fileinput = $("#files-upload").fileinput({
				language: "de",
				uploadUrl: "https://backend.immobit.de/attachments/",
				token: "?session=",
				maxFileSize: 15000,
				allowedFileExtensions: ["jpg", "png", "gif", "jpeg"],
				initialPreview: initialPreviewArray,
				initialPreviewConfig: initialPreviewConfigArray,
				initialPreviewAsData: true,
				deleteUrl: "https://backend.immobit.de/attachments/",
				overwriteInitial: false
			});
		} else {
			//if (_openImmo_json == null)
				//$("#files-upload-input").html('Bitte speichern Sie die Immobilie erst ab und laden anschließend Bilder hoch.<br><input id="files-upload" name="filesupload[]" type="file" multiple class="file-loading">');
			//else
				$("#files-upload-input").html('<input id="files-upload" name="filesupload[]" type="file" multiple class="file-loading">');
			_fileinput = $("#files-upload").fileinput({
				language: "de",
				uploadUrl: "https://backend.immobit.de/attachments/", //uploadUrl: "https://his.homeinfo.de/fs/",
				token: "?session=",
				maxFileSize: 15000,
				allowedFileExtensions: ["jpg", "png", "gif", "jpeg"]
			});
		}
	}
}

function saveMetaDataForImages(id) { // null means all the old images, otherwise the new image
	try {
		var count = 1;
		var position = 0;
		var metadata;
		var title;
		var group;
		if (id == null /*|| _openImmo_json == null*/)
			count = _imagesTitles.length;
		else if (_openImmo_json != null && _openImmo_json.hasOwnProperty("anhaenge"))
			position =  _openImmo_json.anhaenge.anhang.length;

		for (var i = 0; i < count; i++) {
			title = $('#imagetitle' + (position+i)).val();
			group = $('#imagegroup' + (position+i) + ' option:selected').val();
			metadata = {};
			//console.log(i + ' // ' + id + ' // ' + position + ' // ' + _imagesTitles.length + ' // ' + title + ' // ' + group);
			if (id == null)
				(title.trim() == "") ?(_openImmo_json.anhaenge.anhang[i].hasOwnProperty("anhangtitel")) ?metadata.anhangtitel = null :false :(hasChanged(true,"anhaenge.anhang","anhangtitel", title, i)) ?metadata.anhangtitel = title :false;
			else if (title.trim() != "") {
				metadata.anhangtitel = title;
			}
			if (id == null)
				(group.trim() == "0") ?(_openImmo_json.anhaenge.anhang[i].hasOwnProperty("gruppe")) ?metadata.gruppe = null :false :(hasChanged(true,"anhaenge.anhang","gruppe", group, i)) ?metadata.gruppe = group :false;
			else if (group.trim() != "0")
				metadata.gruppe = group;
			if (metadata.hasOwnProperty('anhangtitel') || metadata.hasOwnProperty('gruppe')) {
				$.ajax({
					url: 'https://backend.immobit.de/attachments/' + ((id === null) ?_openImmo_json.anhaenge.anhang[i].id :id) + '?session=' + localStorage.getItem("token"),
					type: "PATCH",
					data: JSON.stringify(metadata),
					success: function (msg) {
						$(".btn_save").html('Immobilie wurde erfolgreich gespeichert');
					},
					error: function (msg) {
						console.log(JSON.stringify(msg));
					}
				});
			}
		}
	} catch (e) {
		console.log("Exception: " + e)
	}
}

function showpreview(JSONdata) {
	var win = window.open('https://immobit.de/preview/expose.html?real_estate=' + encodeURIComponent(JSON.stringify(JSONdata)) + '&session=' + localStorage.getItem("token"), '_blank');
	if (win)
		win.focus();
}
