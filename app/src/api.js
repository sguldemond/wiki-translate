const BASE_URL = process.env.VUE_APP_SERVER_URL;
console.log("==> Server URL set to: " + BASE_URL)

// const BASE_URL = 'http://localhost:5000';

export const wikipedia = {
  search,
  translations,
};

function search(value, lang) {
  if(value == null || lang == null) {
    console.log("No search value or lang given")
  }

  const suffix = '/search_pages';
  const params = `?lang=${lang}&text=${value}`
  const url = BASE_URL + suffix + params
  // console.log("api call:", url);
  
  return fetch(url).then(res => (res.json()));
}

function translations(pageName, lang) {
  if(pageName == null || lang == null) {
    console.log("No search pageName or lang given")
  }

  const suffix = "/get_translations";
  const params = `?lang=${lang}&page=${pageName}`
  const url = BASE_URL + suffix + params

  // console.log("api call:", url);

  return fetch(url).then(res => (res.json()));
}
