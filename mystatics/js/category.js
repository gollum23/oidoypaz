/**
 * Created by gollum23 on 01/09/15.
 */
(function() {
    'use strict';

    $.get('/like/'+podcast+'/' )
            .done(function(data) {
                $('.likes_val' ).html(data['likes'])
            })

    $('.Like' ).find('i').on('click', function() {
        $.get('/like/plus/'+podcast+'/')
                .done(function(data) {
                    $('.likes_val' ).html(data['likes'])
                })
    })

})();