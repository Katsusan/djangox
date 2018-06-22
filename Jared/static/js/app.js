
$(function() {
  $('#log-form').validator({
    onValid: function(validity) {
      $(validity.field).closest('.am-input-group').find('.am-alert').hide();
    },

    onInValid: function(validity) {
      var $field = $(validity.field);
      var $group = $field.closest('.am-input-group');
      var $alert = $group.find('.am-alert');
      // 使用自定义的提示信息 或 插件内置的提示信息
      var msg = $field.data('validationMessage') || this.getValidationMessage(validity);

      if (!$alert.length) {
        $alert = $('<div class="log-alert am-alert am-alert-danger am-radius"></div>').hide().
          appendTo($group);
      }

      $alert.html(msg).show();
    }
  });
  
});

axios.defaults.baseURL = 'http://192.168.1.2:80';


page_config = {
  url: 'api/page',
  method: 'get',
  baseURL: 'http://192.168.1.2',
  timeout: 2000,
  responseType: 'json',
  maxContentLength: '200000'
}

artc_config = {
  url: 'api/article',
  method: 'get',
  baseURL: 'http://192.168.1.2',
  timeout: 1000,
  responseType: 'json',
  maxContentLength: '200000'
}

//n以内的随机数生成
function gen_random(n) {
  if ( typeof(n) == "number" ) {
    return  Math.ceil(n * Math.random()) % n
  }
}


function single_artc_gen(data) {
  var article_img_div = '<div class="am-u-lg-6 am-u-md-12 am-u-sm-12 blog-entry-img">\r\n' + 
                          '<img src="assets/i/f' + gen_random(10) + '.jpg" alt="" class="am-u-sm-12">\r\n' +
                          '</div>';
  
  var article_text_div = '<div class="am-u-lg-12 am-u-md-12 am-u-sm-12 blog-entry-text">\r\n' +
                          '<h1><a href="">' + data.title + '</a></h1>\r\n' +
                          '<span><a href="" class="blog-color">article &nbsp;</a></span>\r\n' +
                          '<span> @' + data.author + '&nbsp;</span>\r\n' +
                          '<span class="created-date">' + data.created_date + '</span>\r\n' +                          
                          '<p>' + data.content + '</p>\r\n' +
                          '<p><a href="/article/' + data.article_id + '/" class="blog-continue">Continue reading</a></p>\r\n'
                          '</div>';
  
  var artctile_entry = '<article class="am-g blog-entry-article">\r\n'  + article_text_div + '</article>\r\n';
  
  return artctile_entry;
}

function md_to_html(text) {
  var converter = new showdown.Converter({simpleLineBreaks: false});
  var compiled_html = converter.makeHtml(text);
  return compiled_html;
}



// render each page/default 5 articles
function init_page(pg) {
  axios.get('api/page/' + pg +'/')
    .then(function (response) {
      for (var i = 0; i < response.data.article_data.length; i++) {
        /*var re_nl = /\r\n|\r|\n/gi;
        var re_and = /&/gi;
        var re_gt = />/gi;
        var re_lt = /</gi;
        response.data[i].content = response.data[i].content.replace(re_and, "&amp;");
        response.data[i].content = response.data[i].content.replace(re_gt, "&gt;");
        response.data[i].content = response.data[i].content.replace(re_lt, "&lt;");
        response.data[i].content = response.data[i].content.replace(re_nl, "<br>");*/
        response.data.article_data[i].content = md_to_html(response.data.article_data[i].content)
        console.log(response.data.article_data[i])
        $('.blog-main').append(single_artc_gen(response.data.article_data[i]));
      }
      if (pg == 1 ) {
        $('.blog-main').append('<ul class="am-pagination">\r\n' +
                                '<li class="am-pagination-next"><a href="/page/' + (pg+1) + '/">Next &raquo;</a></li>\r\n' +
                                '</ul>\r\n');
      } else if ( pg == response.data.total_page) {
        $('.blog-main').append('<ul class="am-pagination">\r\n' + 
                                '<li class="am-pagination-prev"><a href="/page/' + (pg-1) + '/">&laquo; Prev</a></li>\r\n' + 
                                '</ul>\r\n');
      } else {
        $('.blog-main').append('<ul class="am-pagination">\r\n' + 
                                '<li class="am-pagination-prev"><a href="/page/' + (pg-1) + '/">&laquo; Prev</a></li>\r\n' + 
                                '<li class="am-pagination-next"><a href="/page/' + (pg+1) + '/">Next &raquo;</a></li>\r\n' +
                                '</ul>\r\n');        
      }

      // highlight the <pre> <code> content 
      hljs.initHighlighting();
    })
    .catch(function (response){
      console.log(response);
    })
}

function init_index(){
  init_page(1)
}

//use rest API to fetch the detail of specified article
function init_article(id) {
  axios.get('/api/article/' + id + '/')
    .then( function (response) {
      $('.am-article-title').html(response.data.title)
      $('.blog-author').html('@' + response.data.author)
      $('.blog-date').html(response.data.created_date)

      // convert markdown to html
      response.data.content = md_to_html(response.data.content)
      $('.am-article-body').html(response.data.content)

      for(var i = 0;i < response.data.tag.length; i++ ) {
        var tagname = response.data.tag[i].tagname
        $('.am-icon-tags').after('<a href="/tags/' + tagname + '/">' + tagname + '</a>' + '&nbsp;&nbsp;')
      }
      
      //highlight the <pre> <code> content 
      hljs.initHighlighting()
    })
    .catch( function (response){
      console.log(response)
    })
}


