// Add messages
function addMessages(url, message_type, message){
	$.get(url, {
		'message_type': message_type,
		'message': message
	},
	function(data){
		$('#messages').html(data);
	},
	'html'
	);
}

// View all items in the Dashboard
function viewAllItems(){
	$.get($('.dashboard-body').data('ajaxUrl'),
	function(data){
		$('.dashboard-body').html(data);
		inputCheckBoxes();
	},
	'html'
	);
}

// On document load
$(function(){
	// Handle AJAX failure
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

  	// // Handle click of Add button on a Dashboard
  	// $('.dashbaord-add-btn').click(function(){
  	// 	$.get($(this).data('ajaxUrl'),
  	// 	function(data){
  			
  	// 	},
  	// 	'html'
  	// 	);
  	// });

  	// Handle click of Search button on a Dashboard
  	$('#dashboard-searchbar-btn').click(function(){
  		var search_text = $('#dashboard-searchbar-input').val();
  		if(search_text.length){
  			$.get($('#dashboard-searchbar-input').data('ajaxUrl'), {
  				'search_text': search_text
  			},
  			function(data){
  				$('.dashboard-body').html(data);
  				inputCheckBoxes();
  			},
  			'html'
  			);
  		}
  		else{
  			// Handle not searchable Status
  			var msg = 'Please type something to search.';
  			$('.dashboard-operation-status text').addClass('text-danger');
  			$('.dashboard-operation-status text').text(msg);
  		}
  	});

  	// Handle click of Delete button on a Dashboard
  	$('.dashboard-delete-btn').click(function(){
  		var id_list = [];
  		// Add the value attribute of all the checked items in an Array
  		$('input[name="dashboard-item"]').each(function(){
  			if($(this).prop('checked')){
  				id_list.push($(this).val());
  			}
  		});
  		if(id_list.length){
  			// POST list of checked items for deletion
	  		$.post($(this).data('ajaxUrl'), {
	  			'id_list[]': id_list,
	  			'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
	  		},
	  		function(data){
	  			// Handle success Status
	  			var name = $('.dashboard-operation-status').data('objectName');
	  			var total = id_list.length;
	  			if(total == 1 && data.deleted_count ==  '1')
			      name = name.slice(0, -1);
			  	var msg;
			  	console.log(data.deleted_count + ' | ' + data.not_deleted_count);
			  	if(data.deleted_count == '0'){
			  		msg = 'No selected ' + name + ' deleted. ';
			  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger');
			  	}
			  	else{
			  		msg = 'Successfully deleted ' + data.deleted_count + '/' + total + ' selected ' + name + '. ';
			  		$('.dashboard-operation-status text').removeClass('text-danger').addClass('text-success');	
			  	}
			  	if(data.not_deleted_count == '1')
		  			msg += '1 has an existing relationship.';
		  		else if(data.not_deleted_count >= '1')
		  			msg += data.not_deleted_count + ' have an existing relationship.';
		  		
		  		$('.dashboard-operation-status text').text(msg);
		  		// Refresh items in the Dashboard
		  		viewAllItems();
	  		},
	  		'json'
	  		);
	  	}
	  	else{
	  		// Handle not permitted Status
	  		var msg = 'Please select at least 1 device.';
	  		$('.dashboard-operation-status text').addClass('text-danger');
	  		$('.dashboard-operation-status text').text(msg);
	  	}
  	});

});