/*
TODO: add parameter
*/
function fetch_related_articles(){
  $.post( "http://localhost:8080/api/beer", { article: "asdf" }, function( data ) {
    $("#results").html(data);
  }, "text");
}

$(document).ready(function (){
  fetch_related_articles();
});
