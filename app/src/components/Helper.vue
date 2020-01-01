<template>
  <div role="tablist">
    <b-card no-body class="mb-1 form-element">
      <b-card-header header-tag="header" class="p-0" role="tab">
        <b-button block href="#" v-b-toggle.accordion-1 variant="outline-primary">
          {{ cards.how.title }}
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>{{ cards.how.text }}</b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1 form-element">
      <b-card-header header-tag="header" class="p-0" role="tab">
        <b-button block href="#" v-b-toggle.accordion-2 variant="outline-primary">
          {{ cards.why.title }}
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>{{ cards.why.text }}</b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "helper",
  data() {
    return {
      cards: {
        how: {
          title: "How it works",
          text: "It works like this..."
        },
        why: {
          title: "Install as PWA",
          text: "Firefox: ..., Chrome: ..."
        }
      }
    }
  }
}
</script>

<style>
</style>
