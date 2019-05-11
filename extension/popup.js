/*
  Expects Object o to have:
  Source
  Title
  URL
  Tone (array)
  ImageURL
*/

function li_from_news_obj(o){
  var html ="<li class='single-news-item'>";
//  html.concat("<img class='news-image' src='"+ o.image_url + "' />");
  html.concat("<h3 class='news-title'><a href='"+o.url+"'>" + o.title + "</a></h3>");
  //TODO: add tones
  html.concat("</li>");
  return html;
}

/*
TODO: add parameter
*/
function fetch_related_articles(){
  alert("starting fetch");
  $.post("http://localhost:8080/api/beer", function ( data ) {
    current = data["currentArticle"];
    related = data["relatedArticles"];
    res = "";
    alert("asdasd");
    for(var news in related){
      res += li_from_news_obj(news);
    }
    alert(res);

  }, 'application/json');
}

$(document).ready(function (){
  //alert("1");
  //fetch_related_articles();
});
