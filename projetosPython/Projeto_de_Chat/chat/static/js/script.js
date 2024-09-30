$(document).ready(function() {
    $('#chatform').on('submit', function(e) {
        e.preventDefault();

        let query = $('#query').val();

        $.ajax({
            url: '/get_response/',
            data: JSON.stringify({'query': query}),
            type: 'POST',
            contentType: 'application/json',
            success: function(data) {
                if (data.response) {
                    $('#chatbox').append('<p><strong>Você:</strong> ' + query + '</p>');
                    $('#chatbox').append('<p><strong>Chatbot:</strong> ' + data.response + '</p>');
                } else {
                    $('#chatbox').append('<p><strong>Erro:</strong> ' + data.error + '</p>');
                }
            },
            error: function(xhr, status, error) {
                $('#chatbox').append('<p><strong>Erro:</strong> Ocorreu um erro durante o processamento da requisição</p>');
            }
        });

        $('#query').val('');
    });
});