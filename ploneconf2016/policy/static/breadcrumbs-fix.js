jQuery(function($) {
    $().ready(function() {

        // hide breadcrums if only "Home" is being shown (ie. home screen)
        if ( $('#breadcrumbs-home').siblings().length == 0 ) {
            $('#breadcrumbs-home').hide()
        }
    });
});
