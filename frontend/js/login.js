$.ajaxPrefilter(function(options, originalOptions, jqXHR) {
	options.crossDomain = {crossDomain: true};
	options.xhrFields = {withCredentials: true};
});
checkSession();
$(document).ready(function(){
	$("#warning").hide();
    $("#login").click(function(){
		login();
    });
	//if (localStorage.getItem("token") == null)
		//$("#container_style").show();
});
$(document).keypress(function(e) {
    if(e.which == 13) { // 'enter'
        login();
    }
});

function login() {
	/*
	$('#pageloader').show();
	his.session.login($("#username").val(), $("#password").val()).then(loginSuccess, loginError);
	*/
	$.ajax({
		timeout: 3000,
		url: "https://his.homeinfo.de/session", //&duration=5 // max 5min - 30min
		type: "POST",
		data: JSON.stringify({'account':$("#username").val(), "passwd":$("#password").val()}),
        contentType: "application/json; charset=utf-8",
        success: function (msg) {
			//console.log("Success " + msg.token)
			if (typeof(Storage) !== "undefined") {
				localStorage.setItem("token", msg.token);
				//console.log("Storage TOKEN: " + localStorage.getItem("token"));
				window.location.href = "index.html";
			} else {
				//document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Dieser Browser unterstützt keine Cookies, dadurch kann die Seite leider nicht benutzt werden.';
				$("#warning").show();
			}
		},
		error: function (msg) {
			try {
				console.log(msg);
				$('#pageloader').hide();
				if (msg.en_US == "Invalid credentials.") {
					document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> LogIn Daten sind falsch.';
					$("#warning").show();
				} else {
					document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Leider war der LogIn nicht erfolgreich. Bitte versuchen Sie es später noch einmal.';
					$("#warning").show();					
				}
			} catch(e) {
				document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Leider war der LogIn nicht erfolgreich. Bitte versuchen Sie es später noch einmal.';
				$("#warning").show();
			}
		}
	});
}
function loginSuccess(msg) {
	//console.log("Success " + msg.token)
	//if (typeof(Storage) !== "undefined") {
		//localStorage.setItem("token", msg.token);
		//console.log("Storage TOKEN: " + localStorage.getItem("token"));
		window.location.href = "index.html";
	//} else {
		//document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Dieser Browser unterstützt keine Cookies, dadurch kann die Seite leider nicht benutzt werden.';
		//$("#warning").show();
	//}
}
function loginError(msg) {
	try {
		console.log(msg);
		$('#pageloader').hide();
		if (msg.responseJSON.message == "Ungültiger Benutzername und / oder Passwort.") {
			document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> LogIn Daten sind falsch.';
			$("#warning").show();
		} else if(msg.responseJSON.message == "Benutzername und / oder Passwort nicht angegeben.") {
			document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Bitte geben Sie Benutzernamen und Passwort ein.';
			$("#warning").show();
		} else {
			document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Leider war der LogIn nicht erfolgreich. Bitte versuchen Sie es später noch einmal.';
			$("#warning").show();
		}
	} catch(e) {
		document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Leider war der LogIn nicht erfolgreich. Bitte versuchen Sie es später noch einmal.';
		$("#warning").show();
	}
}

function checkSession() {
	//console.log(his.getSessionToken());TODO
	//if (localStorage.getItem("token") != null) {
		$('#pageloader').show();
		$.ajax({
			timeout: 15000,
			url: "https://his.homeinfo.de/session/!",
			type: "GET",
			success: function (msg) {
				//console.log("Success " + msg);
				//console.log("Success " + msg.token)
				//if (msg.token == localStorage.getItem("token")) {
					window.location.href = "index.html";
				//}
			},
			error: function (xmlhttprequest, textstatus, message) { // EXPIRED
				$('#pageloader').hide();
				$("#container_style").show();
				if(textstatus === "timeout")
					document.getElementById("warning").innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Service ist leider nicht aktiv. Bitte versuchen Sie es später noch einmal.';
			}
		});
	//}	
}	
