jQuery(document).ready(function($){

  var min_height = jQuery(window).height();
  var win_width = jQuery(window).width();
  if (win_width >= 980) {
    jQuery('div.sidebar').css('min-height', min_height);
  }

  $(window).resize(function(){
    var min_height = jQuery(window).height();
    var win_width = jQuery(window).width();
    if (win_width >= 980) {
      jQuery('div.sidebar').css('min-height', min_height);
    }
  });

});