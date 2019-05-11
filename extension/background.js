function doInCurrentTab(tabCallback) {
  chrome.tabs.query(
    { currentWindow: true, active: true },
    function (tabArray) { tabCallback(tabArray[0]); }
  );
}

chrome.webNavigation.onCompleted.addListener(function() {
  console.log({currentWindow: true, active : true});
  doInCurrentTab(function(tab) {
    chrome.pageAction.show(tab.id, function(){});
  });

}, {url: [{urlMatches : 'https://www.gp.se/'},{urlMatches : 'https://www.aftonbladet.se/'}, {urlMatches: 'https://www.breitbart.com/'}, {urlMatches: 'https://edition.cnn.com/'}]});
