;
(function($) {
  // add select render
  $.fn.exform.renders.push(function(f) {
    if ($.fn.selectize) {
      f.find('.selectize-multiple').each(function() {
        var $el = $(this);
        $el.selectize({
          plugins: ['remove_button'],
          valueField: 'id',
          labelField: '__str__',
          searchField: '__str__',
          create: false,
          maxItems: null,
          preload: false,
          load: function(query, callback) {
            if (!query.length) return callback();
            $.ajax({
              url: $el.data('search-url') + $el.data('choices'),
              dataType: 'json',
              data: {
                '_q_': query,
                '_cols': 'id.__str__'
              },
              type: 'GET',
              error: function() {
                callback();
              },
              success: function(res) {
                callback(res.objects);
              }
            });
          }
        });
      })
    }
  });
})(jQuery)
