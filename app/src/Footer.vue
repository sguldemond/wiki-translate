<template>
  <div id="footer">
    <p>By <b>Stan Guldemond</b> // code on <a id="link" :href="githubURL" target="_blank">GitHub</a></p>
  </div>
</template>

<script>
  export default {
    name: 'footer',
    data() {
      return {
        githubURL: "https://github.com/sguldemond/wiki-translate"
      }
    }
  }
</script>

<style>
#footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>
