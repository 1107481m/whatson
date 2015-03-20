$(function() {

	// Get the form.
	var form = $('#user_form');

	// Get the messages div.
	var formMessages = $('#result');

	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = $(form).serialize();

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData,
            dataType: "text",
            success: function (data) {
            $(formMessages).html(data);
            $('#user_form').hide();

      }
		})
	});

});

$(function() {

	// Get the form.
	var form = $('#login_form');

	// Get the messages div.
	var formMessages = $('#loginStatus');

	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = $(form).serialize();

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData,
            dataType: "text",
            success: function (data) {
            $(formMessages).html(data);


      }
		})
	});

});

$(function() {

	// Get the form.
	var form = $('#cal_form');

	// Get the messages div.
	var formMessages = $('#cal_status');

	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = $(form).serialize();

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData,
            dataType: "text",
            success: function (data) {
            //$('#cal_form').hide();

                  var result = $(data).find("#cal_status");
                console.log(result);


            $(formMessages).html(result);


      }
		})
	});

});