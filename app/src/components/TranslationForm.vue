<template>
  <div id="translation-form">
    <div id="search-form">
      <b-form-select class="form-element" id="source-lang-select" v-model="sourceLang" :options="sourceLangs" v-on:change="onSourceLangChange()">
        <template v-slot:first>
          <option :value="null" disabled>{{ sourceLangTitle }}</option>
        </template>
      </b-form-select>
      <div id="search-block" class="form-element">
        <b-form-input id="search-input" :disabled="sourceLang == null" list="search-result-list" v-model="searchValue" v-on:keyup="runSearch()" autocomplete="off"></b-form-input>
        <b-button :href="sourcePage.url" target="_blank" id="source-page-link" :disabled="sourcePage.url == null">Wiki</b-button>
      </div>
      <b-form-datalist id="search-result-list" :options="searchResults.titles"></b-form-datalist>
      <b-button variant="primary" id="search-btn" class="form-element" v-on:click="findTranslations()" :disabled="sourcePage.title == null">Find translations</b-button>
      <br/>
      <b-form-select id="lang-form" class="form-element" v-model="selectedTranslation" :options="translationOptions">
        <template v-slot:first>
          <option :value="null" disabled>{{ translationBoxText() }}</option>
        </template>
      </b-form-select>
    </div>
    <div id="result-box" class="form-element">
        <a id="result-link" v-if="selectedTranslation" v-bind:href="selectedTranslation['url']" target="blank">
          <h2>{{ selectedTranslation['*'] }}</h2>
        </a>
    </div>
  </div>
</template>

<script>
  import { wikipedia } from "../api";

  export default {
    name: 'translationForm',
    data () {
      return {
        title: 'wiki translate',
        sourceLangTitle: "Select source language",
        sourceLangs: [],
        searchValue: null,
        searchResults: {},
        sourcePage: {},
        translationOptions: [],
        selectedTranslation: null,
        sourceLang: null,
        targetLang: "en",
        debug: {
          sourcePage: "Samenstelling Tweede Kamer 2017-heden", // long translation in English
          // sourcePage: "List of members of the American Legislative Exchange Council" // no translations
        }
      }
    },
    methods: {
      setSourceLangs() {
        console.log("==> Getting source languages...")
        wikipedia.translations('Wikipedia', 'en')
          .then(res => {
            var langs = res.map(function(opt) {
              return { text: opt.langname, value: opt.lang} 
            })
            langs.push( { text: 'English', value: 'en'})
            langs.sort((a, b) => (a.text > b.text) ? 1 : -1)

            this.sourceLangs = langs
            console.log("==> Source languages set")
          })
      },
      runSearch() {
        this.selectedTranslation = null
        // console.log("==> Searching wikipedia articles...")
        wikipedia.search(this.searchValue, this.sourceLang)
          .then(res => {
            this.searchResults = {
              titles: res[1],
              urls: res[2]
            }

            if (this.searchResults.titles.length > 0) {
              this.sourcePage.title = this.searchResults.titles[0]
              this.sourcePage.url = this.searchResults.urls[0]
              console.log("==> Source page set: " + this.sourcePage.title)
            }
          });
      },
      findTranslations() {
        console.log("==> Looking for translations...")
        wikipedia.translations(this.sourcePage.title, this.sourceLang)
          .then(res => {
            var langs = res.map(function(opt) {
              return { text: opt.langname, value: opt}
            })
            langs.sort((a, b) => (a.text > b.text) ? 1 : -1)

            this.translationOptions = langs
            console.log("==> Translations found: " + langs.length)
          })
      },
      translationBoxText() {
        if (this.translationOptions.length > 0) {
          return "Select target language"
        } else {
          return "No translations found"
        }
      },
      onSourceLangChange() {
        console.log("==> Source lang code changed to: " + this.sourceLang)

        localStorage.sourceLang = this.sourceLang
      }
    },
    mounted() {
      if (localStorage.sourceLang) {
        console.log("==> Setting source lang from local storage: " + localStorage.sourceLang)
        this.sourceLang = localStorage.sourceLang
      }

      this.setSourceLangs()
    }
  }
</script>

<style>
#translation-form {
  padding-top: 20px;
}

#search-block {
  display: flex;
}

#source-page-link {
  margin-left: 10px;
}

#search-btn {
  width: 100%;
}

#result-box {
  min-height: 67px;
  border: 1px solid grey;
  border-radius: 0.25rem;
  /* padding: 10px; */
  padding-top: 15px;
  padding-bottom: 10px;
}

#result-link {
  color: black;
}
</style>
