from django_assets import Bundle, register

#Javascript
register('all_js',
        Bundle('js/main-form.js',
               'js/script.js',),
        filters='jsmin',
        output='cache/packed.js')

register('bootstrap_js',
        Bundle('js/bootstrap/bootstrap-alerts.js',
               'js/bootstrap/bootstrap-buttons.js',
               'js/bootstrap/bootstrap-dropdown.js',
               'js/bootstrap/bootstrap-modal.js',
               'js/bootstrap/bootstrap-scrollspy.js',
               'js/bootstrap/bootstrap-tabs.js',
               'js/bootstrap/bootstrap-twipsy.js',
               'js/bootstrap/bootstrap-popover.js',),
        filters='jsmin',
        output='cache/bootstrap.js')


#CSS
register('all_css',
        Bundle(
               'css/form.css',
               'css/style.css',),
        filters='cssmin',
        output='cache/packed.css')
