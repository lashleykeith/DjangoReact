var gulp = require('gulp');
var minifyCSS = require('gulp-minify-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css', function(){
	return gulp.src('/app/music/static/css/*.css')
	.pipe(minifyCSS())
	.pipe(gulp.dest('/app/music/static/css/build/css/'))
});

gulp.task('uglify',function(){
	return gulp.src('/app/music/static/css/js/*js')
	.pipe(uglify())
	.pipe(gulp.dest('/app/music/static/css/build/js'))
});

gulp.task('minify',['minify-css','uglify']);