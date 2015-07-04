/**
 * Created by gollum23 on 7/4/15.
 */
var gulp    = require('gulp'),
    connect = require('gulp-connect'),
    historyApiFallback = require('connect-history-api-fallback');

gulp.task('server', function() {
    connect.server({
        root: [__dirname],
        hostname: '0.0.0.0',
        port : 8080,
        livereload: true,
        middleware: function(connect, opt) {
            return [ historyApiFallback ];
        }
    });
});

gulp.task('html', function() {
    gulp.src(['./**/*.html', './css/**/*.css', './js/**/*.js'])
        .pipe(connect.reload());
});


gulp.task('watch', function() {
    gulp.watch(['./**/*.html', './statics/css/**/*.css', './statics/js/**/*.js'], ['html']);
});

gulp.task('default', ['server', 'watch']);