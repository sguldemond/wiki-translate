<template>
  <div id="translation-form">
    <div id="search-form">
      <b-form-select class="form-element" id="source-lang-select" v-model="sourceLang" :options="sourceLangs">
        <template v-slot:first>
          <option :value="null" disabled>{{ sourceLangTitle }}</option>
        </template>
      </b-form-select>
      <b-form-input id="search-input" :disabled="sourceLang == null" class="form-element" list="search-result-list" v-model="searchValue" v-on:keyup="runSearch()" autocomplete="off"></b-form-input>
      <b-form-datalist id="search-result-list" :options="searchResults"></b-form-datalist>
      <b-button variant="primary" id="search-btn" class="form-element" v-on:click="findTranslations()" :disabled="searchValue == null">Find translations</b-button>
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
          <!-- <h2>{{ debug.result }}</h2> -->
        </a>
    </div>
  </div>
</template>

<script>
  import { wikipedia } from "./ServerApi";

  export default {
    name: 'translationForm',
    data () {
      return {
        title: 'wiki translate',
        sourceLangTitle: "Select source language",
        sourceLangs: [],
        searchValue: null,
        searchResults: [],
        translationOptions: [],
        selectedTranslation: null,
        sourceLang: null,
        targetLang: "en",
        debug: {
          result: "Samenstelling Tweede Kamer 2017-heden"
        }
      }
    },
    methods: {
      setSourceLangs() {
        wikipedia.translations('Wikipedia', 'en')
          .then(res => {
            // console.log(res)
            var langs = res.map(function(opt) {
              return { text: opt.langname, value: opt.lang} 
            })
            langs.push( { text: 'English', value: 'en'})

            langs.sort((a, b) => (a.text > b.text) ? 1 : -1)

            this.sourceLangs = langs
          })
      },
      runSearch() {
        // console.log("Searching...")
        // console.log(this.searchValue)
        wikipedia.search(this.searchValue, this.sourceLang)
          .then(res => {
            console.log(res)
            this.searchResults =  res
          });
      },
      findTranslations() {
        console.log("Click!")

        wikipedia.translations(this.searchValue, this.sourceLang)
          .then(res => {
            console.log(res)
            var langs = res.map(function(opt) {
              return { text: opt.langname, value: opt}
            })
            langs.sort((a, b) => (a.text > b.text) ? 1 : -1)

            this.translationOptions = langs
          })
      },
      translationBoxText() {
        if (this.translationOptions.length > 0) {
          return "Select target language"
        } else {
          return "No translations found"
        }
      }
    },
    mounted() {
      this.setSourceLangs()
    }
  }
</script>

<style>
#translation-form {
  padding-top: 20px;
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
