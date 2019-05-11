function doInCurrentTab(tabCallback) {
  chrome.tabs.query(
    { currentWindow: true, active: true },
    function (tabArray) { tabCallback(tabArray[0]); }
  );
}

chrome.webNavigation.onCommitted.addListener(function() {
  console.log({currentWindow: true, active : true});
  doInCurrentTab(function(tab) {
    chrome.pageAction.show(tab.id, function(){});
  });
}, {url: [{urlMatches: 'breitbart.com'},
          {urlMatches: 'cnn.com'},
          {urlMatches: 'yahoo.com'},
          {urlMatches: 'huffingtonpost.com'},
          {urlMatches: 'bbc.com'},
          {urlMatches: 'foxnews.com'},
          {urlMatches: 'nytimes.com'},
          {urlMatches: 'nbcnews.com'},
          {urlMatches: 'dailymail.co.uk'},
          {urlMatches: 'washingtonpost.com'},
          {urlMatches: 'wsj.com'},
          {urlMatches: 'usatoday.com'},
          {urlMatches: 'abcnews.go.com'},
          {urlMatches: 'thehill.com'},
          {urlMatches: 'npr.org'},
          {urlMatches: 'ktvu.com'},
          {urlMatches: 'chron.com'},
          {urlMatches: 'reuters.com'},
          {urlMatches: 'aljazeera.com'},
          {urlMatches: 'businessinsider.com'},
          {urlMatches: 'cnet.com'},
          {urlMatches: 'arstechnica.com'},
          {urlMatches: 'techradar.com'},
          {urlMatches: 'theguardian.com'}]});
