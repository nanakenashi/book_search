(function($) {
  $(window).on("scroll", function() {
    var scrollHeight = $(document).height();
    var scrollPosition = $(window).height() + $(window).scrollTop();

    if ((scrollHeight - scrollPosition) / scrollHeight === 0) {
      var length = $('div.paging').length;
      var tail = $('div.paging')[length - 1]
      var params = {
        'author_id': $('div.author_id').data('author_id'),
        'page': $(tail).data('page') + 1
      }

      if (params['page'] === 0) {
        return false;
      }

      callBookApi(params).done(function (result) {
        $('section.books').append(result);
      });
    }
  });

  function callBookApi(params) {
    return $.ajax({
      type: 'GET',
      url: '/_books/',
      data: {
        author_id: params['author_id'],
        page: params['page']
      }
    });
  }
})(jQuery)
