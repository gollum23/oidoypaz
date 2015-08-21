/**
 * Created by gollum23 on 7/4/15.
 */
(function () {
    $('.flexslider' ).flexslider({
        animation: 'fade',
        controlNav: false
    });
    audiojs.events.ready(function () {
        var as = document.getElementsByClassName('Track-data');
        audiojs.createAll({}, as);

        var podcast = document.getElementById('podcast');
        var voces = document.getElementById('voces');

        var a = audiojs.create(podcast,{
            trackEnded: function() {
                var next = $('ol.PodcastList li.playing').next();
                if (!next.length) next = $('ol.PodcastList li').first();
                next.addClass('playing').siblings().removeClass('playing');
                audio.load($('a', next).attr('data-src'));
                audio.play();
            }
        });

        var v = audiojs.create(voces, {
            trackEnded: function () {
                var next = $ ( 'ol.VocesList li.playing' ).next ();
                if ( !next.length ) next = $ ( 'ol.VocesList li' ).first ();
                next.addClass ( 'playing' ).siblings ().removeClass ( 'playing' );
                voces.load ( $ ( 'a', next ).attr ( 'data-src' ) );
                voces.play ();
            }
        });
        // Load in the first track
        var audio = a;
        first = $('ol.PodcastList a').attr('data-src');
        $('ol.PodcastList li').first().addClass('playing');
        audio.load(first);

        var voces = v;
        first = $('ol.VocesList a').attr('data-src');
        $('ol.VocesList li').first().addClass('playing');
        voces.load(first);

        // Load in a track on click
        $('ol.PodcastList li').click(function(e) {
            e.preventDefault();
            $(this).addClass('playing').siblings().removeClass('playing');
            audio.load($('a', this).attr('data-src'));
            audio.play();
        });
        $('ol.VocesList li').click(function(e) {
            e.preventDefault();
            $(this).addClass('playing').siblings().removeClass('playing');
            voces.load($('a', this).attr('data-src'));
            voces.play();
        });
            // Keyboard shortcuts
        $(document).keydown(function(e) {
            var unicode = e.charCode ? e.charCode : e.keyCode;
            // right arrow
            if (unicode == 39) {
                var next = $('li.playing').next();
                if (!next.length) next = $('ol li').first();
                next.click();
                // back arrow
            } else if (unicode == 37) {
                var prev = $('li.playing').prev();
                if (!prev.length) prev = $('ol li').last();
                prev.click();
                // spacebar
            } else if (unicode == 32) {
                audio.playPause();
            }
        })
    })
})();