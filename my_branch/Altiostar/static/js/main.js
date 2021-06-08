// Count objects to be displayed in the Status of the Dashboard
function countObjects(){
  var count = 0;
  $('input[name="dashboard-item-checkbox"]').each(function(){
    if($(this).prop('checked'))
      count++;
  });
  var name = $('.dashboard-operation-status').data('objectName');
  if(count ==  1)
    name = name.slice(0, -1);
  var msg = count + ' ' + name + ' selected';
  $('.dashboard-operation-status text').removeClass('text-success text-danger');
  $('.dashboard-operation-status text').text(msg);
}

// Handle events around checkboxes in a Dashboard
function inputCheckBoxes(){
  // Handle click anywhere on the th-0 to select the select all checkbox 
  // and selection of all checkboxes using select all in a Dashboard
  $('.th-0, #dashboard-item-select-all').click(function(){
    var obj = $('#dashboard-item-select-all');
    var checked = obj.prop('checked');
    obj.prop('checked', !checked);
    $('input[name="dashboard-item-checkbox"]').prop('checked', !checked);
    // Count objects for the Status 
    countObjects();
  });

  // Handle click anywhere on the table row to select the checbox
  $('tbody tr').click(function(){
    var obj = $(this).find('input[name="dashboard-item-checkbox"]');
    var current = obj.prop('checked');
    obj.prop('checked', !current);
    // Handle select all deselection and no of items selected in a Dashboard
    if(!obj.prop('checked') && $('#dashboard-item-select-all').prop('checked')){
      $('#dashboard-item-select-all').prop('checked', false);
    }
    // Count objects for the Status 
    countObjects();
  });

  // Handle select all deselection on change of any checkbox to False
  $('input[name="dashboard-item-checkbox"]').change(function(){
    var obj = $(this);
    obj.prop('checked', !obj.prop('checked'))
    if(!obj.prop('checked') && $('#dashboard-item-select-all').prop('checked')){
      $('#dashboard-item-select-all').prop('checked', false);
    }
    // Count objects for the Status 
    countObjects();
  });
}

$(function(){
  var dropdown = document.getElementsByClassName("dropdown-btn");
  var i;

  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  }

  // Handle sliding of main message
  $('.alert').fadeTo(5000, 1).slideUp(800);

  // On document load, perform all checkbox functions
  inputCheckBoxes();

});