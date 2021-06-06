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

// Handle submit of the Modal form in a Dashboard
function submitForm(id=null){
  	$('.dashboard-modal-form').submit(function(event){
  		event.preventDefault();
  		var mode = $(this).data('mode');
  		var formData = $(this).serializeArray().concat(
  			{ name: 'mode', value: mode },
  			{ name: 'id', value: id }
  		);
  		var msg;
  		console.log(formData);
  		$.post($(this).data('ajaxUrl'), formData,
  		function(data){
  			// Handle success Status
  			var name = $('.dashboard-operation-status').data('objectName');
  			name = name.slice(0, -1);
  			if(data.completed){
  				if(mode == 'add'){
  					msg = 'Successfully added a new ' + name + '.';
  				}
	  			else{
	  				msg = 'Successfully modified the selected ' + name + '.';
	  			}
	  			$('.dashboard-operation-status text').removeClass('text-danger').addClass('text-success');
	  			$('#addOrModifyObjectModal').modal('hide');
	  			// Refresh items in the Dashboard
		  		viewAllItems();
  			}
  			else{
  				msg = 'Unable to ' + mode + ' the ' + name + '. Please try again.';
  				$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger');
  			}
  			$('.dashboard-operation-status text').text(msg);
  		},
  		'json'
  		);
  	});
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

  	// Handle click of Add button on a Dashboard
  	$('.dashboard-add-btn').click(function(){
  		$.get($(this).data('ajaxUrl'), {
  			'mode': $(this).data('mode')
  		},
  		function(data){
  			$('#addOrModifyObjectModal').find('.modal-content').html(data);
  			submitForm();
  		},
  		'html'
  		);
  	});

  	// Handle click of Modify button on a Dashboard
  	$('.dashboard-modify-btn').click(function(){
  		var selected_checboxes = $('input:checkbox:checked');
  		if(selected_checboxes.length == 1){
  			var id = selected_checboxes.val();
  			$.get($(this).data('ajaxUrl'), {
  				'mode': $(this).data('mode'),
  				'id': id
  			},
  			function(data){
  				$('#addOrModifyObjectModal').find('.modal-content').html(data);
  				$('#addOrModifyObjectModal').modal('show');
  				submitForm(id);
  			},
  			'html'
  			);

  		}
  		else{
  			// Handle not permitted Status
  			var name = $('.dashboard-operation-status').data('objectName');
	  		name = name.slice(0, -1);
	  		var msg;
	  		if(selected_checboxes.length)
		  		msg = 'Please select only 1 ' + name + '.';
		  	else
		  		msg = 'Please select any ' + name + '.';
	  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger');
	  		$('.dashboard-operation-status text').text(msg);
  		}
  	});

  	// Handle click of Search button on a Dashboard
  	$('#dashboard-searchbar-btn').click(function(){
  		var search_text = $('#dashboard-searchbar-input').val();
  		$.get($('#dashboard-searchbar-input').data('ajaxUrl'), {
  			'search_text': search_text
  		},
  		function(data){
  			if(data){
	  			$('.dashboard-body').html(data);
	  			inputCheckBoxes();
  			}
  			else{
  				// Handle no results found Status
  				var name = $('.dashboard-operation-status').data('objectName');
  				var msg = 'No ' + name + ' found. Try searching something else.';
  				$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger');
  				$('.dashboard-operation-status text').text(msg);
  			}
  		},
  		'html'
  		);
  	});

  	// Handle click of Delete button on a Dashboard
  	$('.dashboard-delete-btn').click(function(){
  		var id_list = [];
  		// Add the value attribute of all the checked items in an Array
  		$('input[name="dashboard-item-checkbox"]').each(function(){
  			if($(this).prop('checked')){
  				id_list.push($(this).val());
  			}
  		});
  		if(id_list.length){
  			// POST list of checked items for deletion
	  		$.post($(this).data('ajaxUrl'), {
	  			'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
	  			'id_list[]': id_list,
	  		},
	  		function(data){
	  			// Handle success Status
	  			var name = $('.dashboard-operation-status').data('objectName');
	  			var total = id_list.length;
	  			if(total == 1 && data.deleted_count ==  '1')
			      name = name.slice(0, -1);
			  	var msg;
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
	  		var name = $('.dashboard-operation-status').data('objectName');
	  		name = name.slice(0, -1);
	  		var msg = 'Please select at least 1 ' + name + '.';
	  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger');
	  		$('.dashboard-operation-status text').text(msg);
	  	}
  	});

});