<template>
  <div id="app">
    <h2>{{ title }}</h2>
    <TranslationForm />
    <Footer />
    <hr class="form-element">
    <Helper />
  </div>
</template>

<script>
  import TranslationForm from "./components/TranslationForm";
  import Footer from "./components/Footer";
  import Helper from "./components/Helper";

  export default {
    name: 'app',
    components: {
      TranslationForm,
      Footer,
      Helper
    },
    data () {
      return {
        title: 'wiki translate',
      }
    },
    methods: {
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 40px;
  padding-left: 20px;
  padding-right: 20px;
}

.form-element {
  margin-bottom: 20px;
  max-width: 400px;
  margin-right: auto;
  margin-left: auto;
}

</style>
