from django_assets import Bundle, register

#Javascript
register('all_js',
        Bundle('js/main-form.js',
               'js/script.js',
               'js/humanmsg.js',),
        filter='jsmin',
        output='cache/packed.js')

register('libs_js',
        Bundle('js/libs/jquery.uniform.min.js',),
        filter='jsmin',
        output='cache/packed.libs.js')

#CSS
register('all_css',
        Bundle('css/base.css',
               'css/form.css',
               'css/uniform.css',
               'css/style.css',
               'css/humanmsg.css',),
        filter='yui_css',
        output='cache/packed.css')
