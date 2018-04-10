$(document).ready(function (e) {
	$("#uploadimage").on('submit',(function(e) {
	e.preventDefault();
	$("#message").empty();
	$('#loading').show();
	var fd = new FormData(this);
	console.log("Dir");
	console.dir(fd);
	console.log("Type: " + typeof(fd));
	console.log("JSON: " + JSON.stringify(fd));
	console.log("Attrs: " + Object.getOwnPropertyNames(fd));
	for (k of fd.keys()) {
		console.log("Key: " + k);
	}
	var file = fd.getAll("file");
	console.log("File: " + file);
	console.log("Dir");
	console.dir(file);
	console.log("Type: " + typeof(file));
	console.log("JSON: " + JSON.stringify(file));
	console.log("Attrs: " + Object.getOwnPropertyNames(file));
	var blob = file[0].__proto__;
	console.log("Blob: " + blob);
	console.log("Dir");
	console.dir(blob);
	console.log("Type: " + typeof(blob));
	console.log("Attrs: " + Object.getOwnPropertyNames(blob));
	$.ajax({
		url: "https://tls.homeinfo.de/his/fs/test8?session=747bf33e-eaf7-4bbd-ab84-2968f92ad2f6", // Url to which the request is send
		type: "POST",             // Type of request to be send, called as method
		data: blob, // Data sent to server, a set of key/value pairs (i.e. form fields and values)
		contentType: false,       // The content type used when sending data to the server.
		cache: false,             // To unable request pages to be cached
		processData:false,        // To send DOMDocument or non processed data file it is set to false
		success: function(data)   // A function to be called if request succeeds
		{
			$('#loading').hide();
			$("#message").html(data);
		}
	});
	}));

	// Function to preview image after validation
	$(function() {
	$("#file").change(function() {
	$("#message").empty(); // To remove the previous error message
	var file = this.files[0];
	var imagefile = file.type;
	var match= ["image/jpeg","image/png","image/jpg"];
	if(!((imagefile==match[0]) || (imagefile==match[1]) || (imagefile==match[2])))
	{
	$('#previewing').attr('src','noimage.png');
	$("#message").html("<p id='error'>Please Select A valid Image File</p>"+"<h4>Note</h4>"+"<span id='error_message'>Only jpeg, jpg and png Images type allowed</span>");
	return false;
	}
	else
	{
	var reader = new FileReader();
	reader.onload = imageIsLoaded;
	reader.readAsDataURL(this.files[0]);
	}
	});
	});
	function imageIsLoaded(e) {
		$("#file").css("color","green");
		$('#image_preview').css("display", "block");
		$('#previewing').attr('src', e.target.result);
		$('#previewing').attr('width', '250px');
		$('#previewing').attr('height', '230px');
	};
});
