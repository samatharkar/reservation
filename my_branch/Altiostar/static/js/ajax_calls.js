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

// Intermediate operation in searching
function searchHelper(extra=null){
	var device_type_id_list = $('#device-type-select').val();
	var do_not_include_list = [];
	$('.added-device-list-li').each(function(){
		do_not_include_list.push($(this).data('id'));
	});
	if(extra)
		do_not_include_list = do_not_include_list.concat(extra);
  	$.get($('#search-devices-btn').data('ajaxUrl'),{
		'device_type_id_list[]': device_type_id_list,
		'do_not_include_list[]': do_not_include_list,
	},
	function(data){
		if(data){
			$('#available-device-list').html(data);
			addDevicesToSetup();
		}
		else{
			$('#available-device-list #device-select').remove();
			$('#available-device-list #add-selected-devices-btn').remove();
			if(!extra){
				msg = "No device found. Please select another Device Type.";
				$('.device-to-setup-status text').removeClass('text-success').addClass('text-danger').text(msg);
			}
		}
	},
	'html'
	);
}

// Remove devices from added list on click of button beside any of them
function removeDevicesFromAddedList(){
	$('.added-device-list-remove-btn').click(function(){
		var obj = $(this);
		var id = obj.data('id');
		var msg;
		$.get(obj.data('ajaxUrl'), {
			'id': id
		},
		function(data){
			if(data.completed){
				obj.parent().remove();
				// Update status
				msg = "1 Device removed.";
		  		$('.device-to-setup-status text').removeClass('text-danger').addClass('text-success').text(msg);
				// Update count of added devices
				var count = $('.added-device-list-li').length;
				$('#added-devices-count').text(count);
				// Refresh the list of available devices
			}
			else{
				msg = "Device not removed. Please try again.";
		  		$('.device-to-setup-status text').removeClass('text-success').addClass('text-danger').text(msg);
			}
		},
		'json'
		);
	});
}

// Add devices on click of add button in the Setup Add form in the Dashboard
function addDevicesToSetup(){
  	$('#add-selected-devices-btn').click(function(){
		var device_id_list = $('#device-select').val();
		var count = device_id_list.length;
		var msg;
		if(count){
			$('#device-add-error-text').addClass('invisible');
			$.get($(this).data('ajaxUrl'),{
				'device_id_list[]': device_id_list
			},
			function(data){
				$('#added-device-list').append(data);
				// Allow devices to be removed with the click of delete button beside them
				removeDevicesFromAddedList();
				var added_count = $('.added-device-list-li').length;
				$('#added-devices-count').text(added_count);
				if(count == 1)
					msg = "1 Device added.";
				else
					msg = count + " Devices added.";
				$('.device-to-setup-status text').removeClass('text-danger').addClass('text-success').text(msg);
				msg = device_id_list.length;
				$('.selected-devices-status text').text(msg);
	  		},
	  		'html'
	  		);
	  	}
	  	else{
	  		msg = "Please select a Device first.";
	  		$('.device-to-setup-status text').removeClass('text-success').addClass('text-danger').text(msg);
	  	}
	  	// Refresh the list of available devices
	  	searchHelper(device_id_list);

  	});
}

// Search devices on click of search button in the Setup Add form in the Dashboard
function searchDevices(){
	$('#search-devices-btn').click(function(){
		var device_type_id_list = $('#device-type-select').val();
		var msg;
		if(device_type_id_list.length){
			$('.device-to-setup-status text').text('');
			searchHelper();
		}
		else{
			msg = "Please select a Device Type first.";
	  		$('.device-to-setup-status text').removeClass('text-success').addClass('text-danger').text(msg);
	  	}
  	});
}

// Handle submit of the Modal form in a Dashboard
function submitForm(id=null){
  	$('.dashboard-modal-form').submit(function(event){
  		event.preventDefault();
  		var mode = $(this).data('mode');
  		var title = $(this).data('title');
  		var formData = $(this).serializeArray().concat(
  			{ name: 'mode', value: mode },
  			{ name: 'id', value: id }
  		);
  		if(title == 'Setup'){
  			$('.added-device-list-li').each(function(){
  				formData = formData.concat(
	  				{  name: 'device_id_list[]', value: $(this).data('id') }
	  			);
  			});
  		}
  		var msg;
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
	  			$('.dashboard-operation-status text').removeClass('text-danger').addClass('text-success').text(msg);;
	  			$('#addOrModifyObjectModal').modal('hide');
	  			// Refresh items in the Dashboard
		  		viewAllItems();
  			}
  			else{
  				msg = 'Unable to ' + mode + ' the ' + name + '. Please try again.';
  				$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger').text(msg);;
  			}
  		},
  		'json'
  		);
  	});

  	$('.dashboard-modal-form-reset-btn').click(function(){
  		$('.device-to-setup-status text').removeClass('text-success').addClass('text-danger').text('');
		$('#available-device-list #device-select').remove();
		$('#available-device-list #add-selected-devices-btn').remove();
  		$('#added-device-list').empty();
  	});
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

  	// Handle click of Add button on a Dashboard
  	$('.dashboard-add-btn').click(function(){
  		var title = $(this).data('title');
  		$.get($(this).data('ajaxUrl'), {
  			'mode': $(this).data('mode')
  		},
  		function(data){
  			$('#addOrModifyObjectModal').find('.modal-content').html(data);
  			if(title == 'Setup')
  				searchDevices();
  			submitForm();
  		},
  		'html'
  		);
  	});

  	// Handle click of Modify button on a Dashboard
  	$('.dashboard-modify-btn').click(function(){
  		var selected_checkboxes = $('input:checkbox:checked');
  		var title = $(this).data('title');
  		if(selected_checkboxes.length == 1){
  			var id = selected_checkboxes.val();
  			$.get($(this).data('ajaxUrl'), {
  				'mode': $(this).data('mode'),
  				'id': id
  			},
  			function(data){
  				$('#addOrModifyObjectModal').find('.modal-content').html(data);
  				$('#addOrModifyObjectModal').modal('show');
  				if(title == 'Setup'){
	  				searchDevices();
	  				removeDevicesFromAddedList();
  				}
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
	  		if(selected_checkboxes.length)
		  		msg = 'Please select only 1 ' + name + '.';
		  	else
		  		msg = 'Please select any ' + name + '.';
	  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger').text(msg);
  		}
  	});

  	// Handle click of Search button on a Dashboard
  	$('#dashboard-searchbar-btn').click(function(){
  		var search_text = $('#dashboard-searchbar-input').val();
  		var title = $(this).data('title');
  		var search_by = null;
  		if(title == 'Device' || title == 'Setup')
	  		search_by = $('#dashboard-searchbar-selector').data('searchBy');
  		$.get($('#dashboard-searchbar-input').data('ajaxUrl'), {
  			'search_text': search_text,
  			'search_by': search_by
  		},
  		function(data){
  			if(data){
	  			$('.dashboard-body').html(data);
	  			inputCheckBoxes();
	  			countObjects();
  			}
  			else{
  				// Handle no results found Status
  				var name = $('.dashboard-operation-status').data('objectName');
  				var msg = 'No ' + name + ' found. Try searching something else.';
  				$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger').text(msg);
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
			  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger').text(msg);;
			  	}
			  	else{
			  		msg = 'Successfully deleted ' + data.deleted_count + '/' + total + ' selected ' + name + '. ';
			  		$('.dashboard-operation-status text').removeClass('text-danger').addClass('text-success').text(msg);;	
			  	}
			  	if(data.not_deleted_count == '1')
		  			msg += '1 has an existing relationship.';
		  		else if(data.not_deleted_count >= '1')
		  			msg += data.not_deleted_count + ' have an existing relationship.';
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
	  		$('.dashboard-operation-status text').removeClass('text-success').addClass('text-danger').text(msg);
	  	}
  	});

  	// Handle click of Export button on a Dashboard
  	$('.dashboard-export-btn').click(function(){
  		$.get($(this).data('ajaxUrl'),
  		function(data){
  			console.log(data);
  		}
  		);
  	});

});