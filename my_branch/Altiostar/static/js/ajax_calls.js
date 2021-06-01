$(function(){
	$.ajaxSetup({
	    error: function(xhr){
	    	if (xhr.status >=400){
	        	alert('Error!\n Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText);
	    	}
	    }
	});

	$('#add-device-to-setup-btn').click(function(){
		var device_type = $('.device_type').val();
		console.log(device_type);
		if(device_type){
			console.log($(this).data('ajaxUrl'));
			$.get($(this).data('ajaxUrl'),{
				'device_type': device_type
			},
			function(data){
				$('.modal-content').html(data);
	  		},
	  		'html'
	  		);
	  	}
	  	else{
	  		$('.alert').prepend('Please select a Device type first!');
	  	}
  	});
});