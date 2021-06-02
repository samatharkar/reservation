$(function(){
	$.ajaxSetup({
	    error: function(xhr){
	    	if (xhr.status >=400){
	        	alert('Error!\n Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText);
	    	}
	    }
	});

	$('#search-devices-btn').click(function(){
		$('#add-selected-devices-btn').removeAttr('disabled');
		var device_type_id_list = $('#device-type-select').val();
		if(device_type_id_list.length){
			$('#device-search-error').text('');
			$.get($(this).data('ajaxUrl'),{
				'device_type_id_list[]': device_type_id_list
			},
			function(data){
				$('#device-list').html(data);
				if($('.no-device-found').length){
				  	$('#add-selected-devices-btn').attr('disabled', '');
			  	}
	  		},
	  		'html'
	  		);
	  	}
	  	else{
	  		$('#device-search-error').text('Please select a Device type first!');
	  	}
  	});

  	$('#add-selected-devices-btn').click(function(){
		var device_id_list = $('#device-select').val();
		var msg = "<small>" + device_id_list.length;
		if(device_id_list.length > 1)
			msg += " Devices selected</small>";
		else
			msg += " Device selected</small>";
		if(device_id_list.length){
			$('#device-add-error').text('');
			$.get($(this).data('ajaxUrl'),{
				'device_id_list[]': device_id_list
			},
			function(data){
				$('input[name="device_id_list[]"]').remove();
				$('form[name="setup-form"]').prepend(data);
				$('#selected-devices').html(msg);
				$('#device-modal-messages-div').removeAttr('hidden');
				$('#device-modal-messages').fadeTo(3000, 1).slideUp(800);
				$('#device-modal-messages').addClass('alert-success');
				$('#device-modal-messages').html('Device added!');

	  		},
	  		'html'
	  		);
	  	}
	  	else{
	  		$('#device-add-error').text('Please select a Device first!');
	  	}
  	});

});