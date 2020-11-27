$(document).ready(function() {

    var to_submit = $("#to_submit").val();

    function enc_message(submitter, form_data) {
        $.ajax({
          type: 'POST',
          url: to_submit,
          data: {"submitter": submitter, "form_data": form_data},
          dataType: "json",
          success: function(resultData) {
            resultData.alice.forEach((alice_message, index) => {
                $('#message_table').append('<tr><td>' + alice_message + '</td><td>' + resultData.public[index] + '</td><td>' + resultData.bob[index] + '</td></tr>');
            })
            $('#message_table').append('<tr><td>----------</td><td>----------</td><td>----------</td></tr>');
          },
          error: function(e) { alert(e.responseText) }
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