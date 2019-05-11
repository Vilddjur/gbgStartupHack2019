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
}, {url: [{urlMatches: 'https://www.breitbart.com/'},
          {urlMatches: 'https://edition.cnn.com/'},
          {urlMatches: 'https://news.yahoo.com/'},
          {urlMatches: 'https://www.yahoo.com/'},
          {urlMatches: 'http://www.huffingtonpost.com/'},
          {urlMatches: 'https://www.bbc.com/'},
          {urlMatches: 'https://www.foxnews.com/'},
          {urlMatches: 'https://www.nytimes.com/'},
          {urlMatches: 'https://www.nbcnews.com/'},
          {urlMatches: 'https://www.dailymail.co.uk/'},
          {urlMatches: 'https://www.washingtonpost.com/'},
          {urlMatches: 'https://www.wsj.com/'},
          {urlMatches: 'https://abcnews.go.com/'},
          {urlMatches: 'https://www.theguardian.com/'}]});
