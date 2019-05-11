import unirest

response = unirest.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?autoCorrect=true&pageNumber=1&pageSize=10&q=Taylor+Swift&safeSearch=false",
  headers={
    "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "2281645066mshb5fe08876b82c2fp1b8045jsn816ee735b171"
  }
) 

print(response)
