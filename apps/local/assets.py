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
register('bootstrap_less',
        Bundle('css/less/bootstrap.less',
        filters='less, cssmin',
        output='cache/bootstrap.css',
        debug=False),
        )


register('dev_less',
        Bundle('css/less/style.less',
        filters='less, cssmin',
        output='cache/dev.css',
        debug=False),
        )
