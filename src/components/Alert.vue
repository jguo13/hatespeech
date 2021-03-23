<template>
  <div>
<!--     <b-alert variant="success" show><a :href="'http://localhost:5000/return-files/' + $store.getters.scrapedDomain +'.csv'" target="blank"><button class='btn btn-default'> The Scrape of {{ $store.getters.scrapedDomain }} is Finished</button></a></b-alert> -->
    <b-alert variant="success" show><a :href="'http://flask-service:5000/return-files/' + $store.getters.scrapedDomain +'.csv'" target="blank"><button class='btn btn-default'> The Scrape of {{ $store.getters.scrapedDomain }} is Finished</button></a></b-alert>

    <br>
  </div>
</template>

<script>
export default {
  props: {
    message: String,
    titlestring: String
  },
};
</script>

<!--  + `{ $store.getters.scrapedDomain }` -->