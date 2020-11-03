$(document).ready(function() {

    var to_submit = $("#to_submit").val();

    function enc_message(submitter, form_data) {
        $.ajax({
          type: 'POST',
          url: to_submit,
          data: {"submitter": submitter, "form_data": form_data},
          dataType: "json",
          success: function(resultData) {
            // resultData.alice, resultData.bob
            // ^ needs to be added to table
//            if (resultData.hasOwnProperty("error")) {
//              alert("Failed to get action. Error: " + resultData.error);
//            } else if (resultData.hasOwnProperty("no_result")) {
//            } else {
//              alert(resultData)
//            }
          },
          error: function(e) { alert("Failed to get action.") }
        });
    }

    $("#message_form").submit(function(e) {
        e.preventDefault();
    });

    $("#alice_submit").click(function() {
        enc_message(0, $("#message_form").serialize());
    });

    $("#bob_submit").click(function() {
        enc_message(1, $("#message_form").serialize());
    });


});