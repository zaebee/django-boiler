from django_assets import Bundle, register

#Javascript
register('all_js',
        Bundle('js/main-form.js',
               'js/script.js',),
        filters='jsmin',
        output='cache/packed.js')

#CSS
register('less',
        Bundle('css/less/bootstrap.less',
        filters='less',
        output='cache/bootstrap.css',
        debug=False),
        )


register('all_css',
        Bundle('css/base.css',
               'css/form.css',
               'css/style.css',
               'css/humanmsg.css',),
        filters='cssmin',
        output='cache/packed.css')


register('bootstrap_js',
        Bundle('js/bootstrap/bootstrap-alerts.js',
               'js/bootstrap/bootstrap-buttons.js',
               'js/bootstrap/bootstrap-dropdown.js',
               'js/bootstrap/bootstrap-modal.js',
               'js/bootstrap/bootstrap-popover.js',
               'js/bootstrap/bootstrap-scrollspy.js',
               'js/bootstrap/bootstrap-tabs.js',
               'js/bootstrap/bootstrap-twipsy.js',),
        filters='jsmin',
        output='cache/bootstrap.js')
