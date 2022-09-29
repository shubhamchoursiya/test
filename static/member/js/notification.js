$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-notification .modal-content").html("");
      },
      success: function (data) {
        if (data.form_is_valid) {
          $("#datatable-buttons tbody").html(data.html_notification_list);
          $("#modal-notification").modal("hide");
        }
        else {
          $("#modal-notification .modal-content").html(data.html_form);
        }
      }
    });
  };



  /* Binding */

  // Create book
  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-notification", loadForm);

});
