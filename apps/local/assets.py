from django_assets import Bundle, register

#Javascript
register('all_js',
        Bundle('js/main-form.js',
               'js/script.js',),
        filter='jsmin',
        output='cache/packed.js')

#CSS
register('all_css',
        Bundle('css/base.css',
               'css/form.css',
               'css/style.css',
               'css/humanmsg.css',),
        filter='cssmin',
        output='cache/packed.css')
