var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");
var concat = require("gulp-concat");
var cache = require("gulp-cache");
var imagemin = require("gulp-imagemin");
var bs = require("browser-sync").create();
var fileinclude = require('gulp-file-include');

var path = {
    'html': './templates/**/',
    'css': './src/css/',
    'js': './src/js/',
    'images': './src/images/',
    'css_dist': './dist/css/',
    'js_dist': './dist/js/',
    'images_dist': './dist/images/',
}
//定义一个html的任务
gulp.task("html",function(){
    gulp.src(path.html + '*.html')//后缀名为html的文件名
        .pipe(bs.stream())//重新加载
});
//定义一个css的任务
gulp.task("css",function(){
    gulp.src(path.css + '*.css')//后缀名为css的文件名
        .pipe(cssnano())//压缩css
        .pipe(rename({"suffix":".min"}))//改后缀名
        .pipe(gulp.dest(path.css_dist))
        .pipe(bs.stream())
});
//定义一个js的任务
gulp.task("js",function(){
    gulp.src(path.js + '*.js')//后缀名为js的文件名
        .pipe(uglify())//压缩css
        .pipe(gulp.dest(path.js_dist))
        .pipe(bs.stream())
});
gulp.task("images",function(){
    gulp.src(path.js + '*.*')
        .pipe(cache(imagemin()))//缓存图片
        .pipe(gulp.dest(path.images_dist))
        .pipe(bs.stream())
})

gulp.task('fileinclude', function () {
    gulp.src(['templates/**/*.html','!templates/include/**.html'])
        .pipe(fileinclude({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp.dest('dist'));
});

//定义监听文件修改
gulp.task("watch",function(){
    gulp.watch(path.css + '*.css', ['css']);
    gulp.watch(path.html + '*.html', ['html']);
    gulp.watch(path.js + '*.js', ['js']);
    gulp.watch(path.images + '*.*', ['images']);
    gulp.watch(path.include + '*.*', ['fileinclude']);
})

//初始化brower-sync任务(实时监听修改)
gulp.task("bs",function(){
    bs.init({
        'server':{
            "baseDir":'./'
        }
    })
})

//创建默认任务
gulp.task("default",['bs','watch']);