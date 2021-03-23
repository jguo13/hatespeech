<template>
	  <div id="app">

	    <div class="card">
        <div class="heading">
    	    <h1> {{ date }} </h1>
        </div>   
        <h1 class="subtitle">{{ subtitle }}</h1>
	    </div>
	  </div>

</template>
<script>


export default {
	name: "HistoryCardsfront",
	props: {
		msg: String,
		date: String,
		subtitle: String,
    links: Array
	},
  components: { 
    // FlipCard
   },
  methods: {
    toggleBigger(){
    this.showButton = !this.showButton;
    },
  onScroll () {
    const progress = this.$refs.text.scrollTop / (this.$refs.text.scrollHeight - this.$refs.text.clientHeight)
    if (progress > 1) {
      this.progress = 1
    } else if (progress < 0) {
      this.progress = 0
    } else {
      this.progress = progress
    }
  }
},

  data () {
    return {
      progress: 0
    }
  }
}
</script>
<style scoped>
.heading{
  outline-style: solid;
  background-color: #f6cec4;
}


.card {
  border-radius: 3px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 1.5;
  font-size: 18px;
  color: #444;
  width: 100%;
  margin: 10px auto;
  height: 500px;
  width: 500px;
  margin-top: 10px;
/*  display: flex;
  flex-direction: column;*/
  background: white;
  outline-style: solid;
  outline-color: black;
/*  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
*/}

.subtitle {
  padding: 100px;
  text-align: center;

}

.text-section {
  height: 100%;
  max-height: 100%;
  padding: 0 10px 10px;
  overflow: scroll;
  -webkit-overflow-scrolling: touch;
  text-align: left
}


.interaction {
  border: 10px solid lightgreen;
  display: flex;
  flex: 1 0 auto;
  max-height: 225px;
  transition: max-height 0.25s ease-out;
}






</style>