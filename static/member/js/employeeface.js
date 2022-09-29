$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-employeeface .modal-content").html("");
        $("#modal-employeeface").modal("show");
      },
      success: function (data) {
        $("#modal-employeeface .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      cache: false,
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.form_is_valid) {
          $("#datatable-buttons tbody").html(data.html_employeeface_list);
          $("#modal-employeeface").modal("hide");
        }
        else {
          $("#modal-employeeface .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-employeeface").click(loadForm);
  $("#modal-employeeface").on("submit", ".js-employeeface-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-employeeface", loadForm);
  $("#modal-employeeface").on("submit", ".js-employeeface-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-employeeface", loadForm);
  $("#modal-employeeface").on("submit", ".js-employeeface-delete-form", saveForm);

});
