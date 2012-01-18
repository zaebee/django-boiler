from django_assets import Bundle, register

#Javascript
register('all_js',
        Bundle('js/main-form.js',
               'js/script.js',),
        filters='jsmin',
        output='cache/packed.js')

#CSS
register('all_css',
        Bundle('css/base.css',
               'css/form.css',
               'css/style.css',
               'css/humanmsg.css',),
        filters='cssmin',
        output='cache/packed.css')
