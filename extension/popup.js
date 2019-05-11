/*
  Expects Object o to have:
  Source
  Title
  URL
  Tone (array)
  ImageURL
*/

function li_from_news_obj(o){
  var ret ="<li class='single-news-item'>";
  //ret.concat("<img class='news-image' src='"+ o.image_url + "' />");
  ret += "<h3 class='news-title'><a href='"+o["url"]+"'>" + o["title"] + "</a></h3>";
  //TODO: add tones
  ret += "</li>";
  return ret;
}

/*
TODO: add parameter
*/
function fetch_related_articles(){
  $.post( "http://localhost:8080/api/beer", { article: "asdf" }, function( data ) {
    current = data["currentArticle"];
    related = data["relatedArticles"];
    res = "";
    for(var id in related){
      console.log(related[id]);
      res += li_from_news_obj(related[id]);
    }
    $("#results").html(res);

  }, "json");
}

$(document).ready(function (){
  fetch_related_articles();
});
