<template>
	  <div id="app">
	    <div class="card">
	      <progress-bar :value="progress"/>
	      <div class="text-section" ref="text" @scroll="onScroll"> 
          {{ msg }}
          <h5>Check out links below for more info:</h5>
          <ul>
            <li v-for="link in links" v-bind:key="link">{{ link }} </li>
          </ul>
        </div>
	    </div>
	  </div>

</template>
<script>

import ProgressBar from '../components/ProgressBar'
// import FlipCard from "../components/FlipCard"

export default {
	name: "HistoryCards",
	props: {
		msg: String,
		date: String,
		subtitle: String,
    links: Array
	},
  components: { 
  	ProgressBar,
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
/** {
  box-sizing: border-box;
}*/
/*
body {
  margin: 0;
  padding: 1px 0 0;
  width: 100vw;
  height: 100vh;
  background: #6B5CA5;
}*/

/*html {
  padding: 0;
  margin: 0;
}*/



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
  height: 100%;
  margin-top: 10px;
  height: 500px;
  width: 500px;
  display: flex;
  flex-direction: column;
  background: white;
  outline-style: solid;
  outline-color: black;
/*  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
*/}

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