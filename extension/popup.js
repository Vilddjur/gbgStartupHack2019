/*
TODO: add parameter
*/
function fetch_related_articles(){
  $.post( "http://localhost:8080/api/coffee", { url: window.location.toString() }, function( data ) {
    $("#results").html(data);
  }, "text");
}

$(document).ready(function (){
  fetch_related_articles();
});
