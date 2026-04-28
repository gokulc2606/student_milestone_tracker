$(document).ready(function() {
    $('#id_title').on('keyup', function() {
        var query = $(this).val();
        if (query.length > 2) {
            $.ajax({
                url: '/api/check-title/',
                data: {
                    'q': query
                },
                dataType: 'json',
                success: function(data) {
                    var feedback = $('#titleFeedback');
                    var submitBtn = $('#submitBtn');
                    if (data.exists) {
                        feedback.text('This project title already exists!').show();
                        submitBtn.prop('disabled', true);
                        $('#id_title').addClass('is-invalid');
                    } else {
                        feedback.hide();
                        submitBtn.prop('disabled', false);
                        $('#id_title').removeClass('is-invalid').addClass('is-valid');
                    }
                }
            });
        }
    });
});
