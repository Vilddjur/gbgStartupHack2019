/*
TODO: add parameter
*/
function fetch_related_articles(){
  chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
    function(tabs){
      var url = tabs[0].url;
      $.post( "http://localhost:8080/api/coffee", { url: url }, function( data ) {
        $("#results").html(data);
      }, "text");
    }
  );
}

$(document).ready(function (){
  fetch_related_articles();
});
