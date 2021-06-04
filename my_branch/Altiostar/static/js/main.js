// Handle events around checkboxes in a Dashboard
function inputCheckBoxes(){
  // Handle select all checkbox in a Dashboard
  $('#dashboard-item-select-all').change(function(){
    $('input[name="dashboard-item"]').prop('checked', $(this).prop('checked'));
  });

  // Handle select all deselection and no of items selected in a Dashboard
  $('input[name="dashboard-item"]').change(function(){
    if(!$(this).prop('checked') && $('#dashboard-item-select-all').prop('checked')){
      $('#dashboard-item-select-all').prop('checked', false);
    }
    var count = 0;
    $('input[name="dashboard-item"]').each(function(){
      if($(this).prop('checked'))
        count++;
    });
    var name = $('.dashboard-operation-status').data('objectName');
    if(count ==  1)
      name = name.slice(0, -1);
    var msg = count + ' ' + name + ' selected';
    $('.dashboard-operation-status text').removeClass('text-success text-danger');
    $('.dashboard-operation-status text').text(msg);
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

  inputCheckBoxes();

});